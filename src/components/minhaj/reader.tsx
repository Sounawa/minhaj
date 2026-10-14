"use client";

import { useEffect, useMemo, useRef, useState, useSyncExternalStore } from "react";
import { ArrowLeft, ArrowRight, BookMarked, BookmarkCheck, Check, ChevronLeft, ChevronRight, Clock3, Columns2, Download, Eraser, ExternalLink, FileQuestion, FileText, Heart, Highlighter, Hourglass, Languages, ListTree, Loader2, Printer, StickyNote } from "lucide-react";
import { motion } from "framer-motion";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { cn } from "@/lib/utils";
import { getReadPos, navigate, setLastDoc, setReadPos, useDoc, useFavorites, useHighlights, useLocalState, useNote } from "./hooks";
import type { HlPane } from "./hooks";
import type { DocPayload } from "./types";

type ViewMode = "both" | "fr" | "ar";
type TextSize = "normal" | "large" | "xlarge";

const TEXT_SIZE_CLASS: Record<TextSize, string> = {
  normal: "text-[15.5px]",
  large: "text-[17px]",
  xlarge: "text-[18.5px] leading-relaxed",
};
const TEXT_SIZE_AR_CLASS: Record<TextSize, string> = {
  normal: "text-[17px]",
  large: "text-[18.5px]",
  xlarge: "text-[20px] leading-loose",
};

/** Temps de lecture estimé (minutes) — ~1 400 caractères/min pour un texte d'étude. */
function readMinutes(html: string | undefined): number {
  if (!html) return 0;
  const text = html.replace(/<[^>]+>/g, " ");
  return Math.max(1, Math.round(text.trim().length / 1400));
}

/** Sommaire de la leçon : titres h2/h3 extraits du HTML FR (ordre du document). */
type OutlineItem = { level: 2 | 3; text: string };
function lessonOutline(html: string | undefined): OutlineItem[] {
  if (!html) return [];
  const out: OutlineItem[] = [];
  const re = /<(h[23])\b[^>]*>([\s\S]*?)<\/\1>/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(html))) {
    const text = m[2].replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim();
    if (text) out.push({ level: m[1] === "h2" ? 2 : 3, text });
  }
  return out;
}

// ————————————————————————————————— Surlignages (CSS Custom Highlight API)

type HlBridge = { set: (k: string, v: unknown) => void; delete: (k: string) => void };
function hlBridge(): HlBridge | null {
  if (typeof window === "undefined") return null;
  const w = window as unknown as { Highlight?: unknown; CSS?: { highlights?: HlBridge } };
  return typeof w.Highlight === "function" && w.CSS?.highlights ? w.CSS.highlights : null;
}

const subscribeNoop = () => () => undefined;
const getHlSupport = () => hlBridge() !== null;
const getHlSupportServer = () => false;

/** Offset texte d'un point (nœud, offset) depuis le début d'un conteneur. */
function textOffsetFrom(container: Element, node: Node, offsetInNode: number): number | null {
  try {
    const range = document.createRange();
    range.selectNodeContents(container);
    range.setEnd(node, offsetInNode);
    return range.toString().length;
  } catch {
    return null;
  }
}

/** Range inverse : depuis des offsets texte dans un conteneur. */
function rangeFromOffsets(container: Element, start: number, end: number): Range | null {
  const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT);
  const range = document.createRange();
  let pos = 0;
  let started = false;
  let node: Node | null;
  while ((node = walker.nextNode())) {
    const len = node.textContent?.length ?? 0;
    if (len === 0) continue;
    if (!started && pos + len > start) {
      try {
        range.setStart(node, Math.max(0, start - pos));
      } catch {
        return null;
      }
      started = true;
    }
    if (started && pos + len >= end) {
      try {
        range.setEnd(node, Math.max(0, end - pos));
      } catch {
        return null;
      }
      return range;
    }
    pos += len;
  }
  return null;
}

function PdfOnlyNotice({ doc }: { doc: DocPayload }) {
  return (
    <motion.section
      key={`${doc.docId}-pdf`}
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, ease: "easeOut" }}
      className="no-print mx-auto mt-2 max-w-2xl"
    >
      <div className="rounded-2xl border border-amber-800/15 bg-gradient-to-b from-amber-100/70 to-card p-8 text-center shadow-sm dark:border-amber-200/15 dark:from-amber-900/30">
        <span className="mx-auto flex size-14 items-center justify-center rounded-2xl border border-amber-800/20 bg-card shadow-sm">
          <FileText className="size-7 text-primary" aria-hidden="true" />
        </span>
        <h2 className="mt-4 font-serif text-xl font-semibold text-amber-950 dark:text-amber-50">
          Leçon publiée au format PDF officiel
        </h2>
        <p dir="rtl" lang="ar" className="mt-2 font-arabic text-lg leading-relaxed text-amber-900 dark:text-amber-100">
          {doc.titleAr}
        </p>
        <p className="mx-auto mt-4 max-w-lg text-sm leading-relaxed text-muted-foreground">
          Le Ministère des Habous publie le texte de cette leçon uniquement au format PDF
          sur le site officiel du programme <em>Taʿlīm ʿatīq</em>. Le titre est intégré à la
          bibliothèque pour la recherche et la navigation ; consultez le document original
          pour le contenu intégral.
        </p>
        {doc.pdfUrl && (
          <Button asChild className="mt-6 gap-2 rounded-xl" size="lg">
            <a href={doc.pdfUrl} target="_blank" rel="noopener noreferrer">
              <ExternalLink className="size-4" aria-hidden="true" />
              Ouvrir le PDF officiel
            </a>
          </Button>
        )}
        <p className="mt-4 text-xs text-muted-foreground">
          habous.gov.ma — وزارة الأوقاف والشؤون الإسلامية
        </p>
      </div>
    </motion.section>
  );
}

function ColumnChip({ lang, label }: { lang: "fr" | "ar"; label: string }) {
  return (
    <div
      className={cn(
        "sticky top-20 z-10 -mx-1 mb-4 flex items-center gap-2 rounded-lg border px-3 py-1.5 text-xs font-semibold uppercase tracking-[0.14em] backdrop-blur-md",
        lang === "fr"
          ? "border-amber-800/15 bg-card/85 text-amber-900 dark:text-amber-100"
          : "border-amber-800/15 bg-card/85 text-amber-900 dark:text-amber-100"
      )}
    >
      <Languages className="size-3.5 text-primary" aria-hidden="true" />
      {label}
    </div>
  );
}

function DocHeader({ doc }: { doc: DocPayload }) {
  return (
    <div className="mb-8">
      <div className="flex flex-wrap items-center gap-2">
        <Badge className="rounded-full bg-gradient-to-br from-amber-600 to-orange-800 text-[11px] text-amber-50 shadow-sm">
          {doc.isIntro ? "Introduction" : `Leçon ${doc.index + 1} / ${doc.count}`}
        </Badge>
        {doc.level && (
          <Badge
            variant="outline"
            className="rounded-full border-amber-800/25 bg-amber-100/60 text-[11px] text-amber-900 dark:border-amber-200/20 dark:bg-amber-900/30 dark:text-amber-100"
          >
            {doc.level.shortFr}
          </Badge>
        )}
        {doc.subject && (
          <Badge
            variant="outline"
            className="rounded-full border-amber-800/25 bg-amber-100/60 text-[11px] text-amber-900 dark:border-amber-200/20 dark:bg-amber-900/30 dark:text-amber-100"
          >
            {doc.subject.titleFr}
          </Badge>
        )}
        {doc.savant && doc.hasFr && !doc.pdfOnly && (
          <Badge
            variant="outline"
            title="Version française révisée : terminologie académique, versets coraniques vérifiés, gloses des termes techniques."
            className="gap-1.5 rounded-full border-amber-500/50 bg-gradient-to-br from-amber-100 to-yellow-50 text-[11px] font-semibold text-amber-800 shadow-sm dark:border-amber-400/30 dark:from-amber-900/50 dark:to-amber-800/30 dark:text-amber-200"
          >
            <BookMarked className="size-3.5" aria-hidden="true" />
            Traduction savante
          </Badge>
        )}
        {doc.hasFr && !doc.pdfOnly && (
          <Badge
            variant="outline"
            title="Estimation fondée sur la longueur du texte français (≈ 1 400 caractères par minute)."
            className="gap-1.5 rounded-full border-amber-800/25 bg-card/70 text-[11px] font-medium text-amber-900/85 dark:border-amber-200/20 dark:text-amber-100/85"
          >
            <Clock3 className="size-3.5" aria-hidden="true" />
            ≈ {readMinutes(doc.htmlFr)} min de lecture
          </Badge>
        )}
        {doc.sample && (
          <Badge
            variant="outline"
            className="rounded-full border-amber-700/30 bg-amber-100/70 text-[11px] text-amber-900 dark:border-amber-300/20 dark:bg-amber-900/40 dark:text-amber-100"
          >
            échantillon de démonstration
          </Badge>
        )}
      </div>
      {doc.titleFr ? (
        <h1 className="mt-4 font-serif text-2xl font-semibold leading-tight text-amber-950 sm:text-3xl dark:text-amber-50">
          {doc.titleFr}
        </h1>
      ) : (
        <h1 className="mt-4 font-serif text-2xl font-semibold leading-tight text-amber-950 sm:text-3xl dark:text-amber-50">
          <span dir="rtl" lang="ar" className="font-arabic">
            {doc.titleAr}
          </span>
        </h1>
      )}
      {/* Filet orné entre le titre français et le titre arabe */}
      <span className="mt-3 flex items-center gap-2" aria-hidden="true">
        <span className="h-px flex-1 bg-gradient-to-r from-transparent via-amber-700/30 to-amber-700/30 dark:via-amber-300/25 dark:to-amber-300/25" />
        <svg viewBox="0 0 24 24" className="size-3.5 shrink-0 text-amber-700/70 dark:text-amber-300/70" fill="currentColor">
          <path d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4z" />
        </svg>
        <span className="h-px flex-1 bg-gradient-to-l from-transparent via-amber-700/30 to-amber-700/30 dark:via-amber-300/25 dark:to-amber-300/25" />
      </span>
      <p dir="rtl" lang="ar" className="mt-2 text-right font-arabic text-xl leading-relaxed text-primary">
        {doc.titleAr}
      </p>
    </div>
  );
}

function ViewModeToggle({ mode, onChange }: { mode: ViewMode; onChange: (m: ViewMode) => void }) {
  const options: { id: ViewMode; label: string; icon: React.ReactNode }[] = [
    { id: "both", label: "Bilingue", icon: <Columns2 className="size-4" aria-hidden="true" /> },
    { id: "fr", label: "Français", icon: <span className="font-serif text-[13px] font-semibold">FR</span> },
    { id: "ar", label: "العربية", icon: <span className="font-arabic text-[13px] font-semibold">ع</span> },
  ];
  return (
    <div
      role="group"
      aria-label="Mode d'affichage du lecteur"
      className="inline-flex items-center gap-0.5 rounded-xl border border-amber-800/15 bg-card/70 p-1 shadow-sm"
    >
      {options.map((o) => (
        <button
          key={o.id}
          type="button"
          onClick={() => onChange(o.id)}
          aria-pressed={mode === o.id}
          className={cn(
            "inline-flex min-h-9 items-center gap-1.5 rounded-lg px-3 text-xs font-medium transition",
            mode === o.id
              ? "bg-gradient-to-br from-amber-600 to-orange-800 text-amber-50 shadow-sm"
              : "text-muted-foreground hover:bg-amber-100/60 hover:text-foreground dark:hover:bg-amber-900/40"
          )}
        >
          {o.icon}
          <span className="hidden sm:inline">{o.label}</span>
        </button>
      ))}
    </div>
  );
}

function TextSizeControl({ size, onChange }: { size: TextSize; onChange: (s: TextSize) => void }) {
  const cycle: TextSize[] = ["normal", "large", "xlarge"];
  const next = () => onChange(cycle[(cycle.indexOf(size) + 1) % cycle.length]);
  const label = size === "normal" ? "normale" : size === "large" ? "grande" : "très grande";
  return (
    <Button
      variant="outline"
      size="icon"
      aria-label={`Taille du texte : ${label} — toucher pour agrandir`}
      title="Taille du texte"
      className="size-10 border-amber-800/15 bg-card/70 text-amber-900 hover:bg-amber-100/60 dark:text-amber-100 dark:hover:bg-amber-900/40"
      onClick={next}
    >
      <span className="font-serif text-[15px] font-bold" aria-hidden="true">
        A<span className="align-super text-[10px]">+</span>
      </span>
    </Button>
  );
}

/** Sommaire flottant : saut vers les titres h2/h3 de la leçon (défilement doux + flash ambre). */
function OutlineButton({ items }: { items: OutlineItem[] }) {
  const [open, setOpen] = useState(false);
  if (items.length < 3) return null;
  const jump = (idx: number) => {
    const col = Array.from(document.querySelectorAll<HTMLElement>(".reader-col")).find((c) =>
      c.querySelector(".lesson-content")
    );
    if (!col) return;
    const heads = col.querySelectorAll(".lesson-content h2, .lesson-content h3");
    const el = heads[idx] as HTMLElement | undefined;
    if (!el) return;
    el.scrollIntoView({ behavior: "smooth", block: "start" });
    el.classList.remove("outline-flash");
    void el.offsetWidth; // relance l'animation
    el.classList.add("outline-flash");
    setOpen(false);
  };
  return (
    <div className="relative">
      <Button
        variant="outline"
        size="icon"
        aria-label={`Sommaire de la leçon — ${items.length} sections`}
        title="Sommaire de la leçon"
        aria-expanded={open}
        className="size-10 border-amber-800/15 bg-card/70 text-amber-900 hover:bg-amber-100/60 dark:text-amber-100 dark:hover:bg-amber-900/40"
        onClick={() => setOpen((o) => !o)}
      >
        <ListTree className="size-4.5" aria-hidden="true" />
      </Button>
      {open && (
        <>
          <div className="fixed inset-0 z-40" onClick={() => setOpen(false)} aria-hidden="true" />
          <nav
            role="dialog"
            aria-label="Sommaire de la leçon"
            className="absolute right-0 top-12 z-50 max-h-96 w-72 overflow-y-auto rounded-xl border border-amber-800/15 bg-card p-3 shadow-lg [scrollbar-width:thin]"
          >
            <p className="px-1.5 pb-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-muted-foreground">
              Sommaire — {items.length} sections
            </p>
            <ol className="mt-0.5 space-y-0.5">
              {items.map((it, i) => (
                <li key={i}>
                  <button
                    type="button"
                    onClick={() => jump(i)}
                    className={cn(
                      "w-full rounded-lg px-2.5 py-1.5 text-left text-[13px] leading-snug text-foreground/85 transition-colors hover:bg-amber-100/70 hover:text-foreground focus-visible:outline-2 focus-visible:outline-ring dark:hover:bg-amber-900/40",
                      it.level === 3 && "ps-5 text-[12.5px] text-muted-foreground"
                    )}
                  >
                    {it.text}
                  </button>
                </li>
              ))}
            </ol>
          </nav>
        </>
      )}
    </div>
  );
}

/** Notes personnelles par leçon (localStorage, auto-sauvegarde à la frappe).
 *  Compteur de notes : badge sur le bouton + décompte mots/caractères dans le panneau. */
function formatCount(n: number): string {
  return n >= 1000 ? `${(n / 1000).toFixed(1).replace(".", ",")}k` : String(n);
}
function NotesButton({ bookId, docId }: { bookId: string; docId: string }) {
  const [open, setOpen] = useState(false);
  const { text, setNote, hasNote } = useNote(bookId, docId);
  const charCount = text.trim().length;
  const wordCount = charCount === 0 ? 0 : text.trim().split(/\s+/).length;
  return (
    <div className="relative">
      <Button
        variant="outline"
        size="icon"
        aria-label={
          hasNote
            ? `Notes personnelles — ${formatCount(charCount)} caractère${charCount > 1 ? "s" : ""} notés pour cette leçon`
            : "Notes personnelles"
        }
        title={hasNote ? `Notes personnelles (${formatCount(charCount)} caractères)` : "Notes personnelles"}
        aria-expanded={open}
        className={cn(
          "size-10 border-amber-800/15 bg-card/70 hover:bg-amber-100/60 dark:hover:bg-amber-900/40",
          hasNote ? "text-amber-700 dark:text-amber-300" : "text-amber-900/80 dark:text-amber-100/80"
        )}
        onClick={() => setOpen((o) => !o)}
      >
        <StickyNote className={cn("size-4.5", hasNote && "fill-amber-300/60 dark:fill-amber-700/50")} aria-hidden="true" />
        {hasNote && (
          <span
            className="absolute -right-1 -top-1 flex h-4 min-w-4 items-center justify-center rounded-full bg-amber-600 px-1 text-[9px] font-bold leading-none text-amber-50 shadow"
            aria-hidden="true"
          >
            {charCount > 99 ? "99+" : charCount}
          </span>
        )}
      </Button>
      {open && (
        <>
          <div className="fixed inset-0 z-40" onClick={() => setOpen(false)} aria-hidden="true" />
          <div
            role="dialog"
            aria-label="Notes personnelles"
            className="absolute right-0 top-12 z-50 w-80 max-w-[calc(100vw-2rem)] rounded-xl border border-amber-800/15 bg-card p-3 shadow-lg"
          >
            <div className="flex items-center justify-between gap-2 px-1">
              <label
                htmlFor="mnhj-note"
                className="block text-[11px] font-semibold uppercase tracking-[0.14em] text-muted-foreground"
              >
                Mes notes sur cette leçon
              </label>
              {charCount > 0 && (
                <span
                  className="shrink-0 rounded-full border border-amber-700/25 bg-amber-100/70 px-2 py-0.5 text-[10px] font-semibold tabular-nums text-amber-800 dark:border-amber-300/20 dark:bg-amber-900/40 dark:text-amber-200"
                  aria-live="polite"
                >
                  {wordCount} mot{wordCount > 1 ? "s" : ""} · {formatCount(charCount)} car.
                </span>
              )}
            </div>
            <textarea
              id="mnhj-note"
              value={text}
              onChange={(e) => setNote(e.target.value)}
              rows={6}
              placeholder="À comprendre, à mémoriser, questions à poser…"
              className="mt-2 w-full resize-y rounded-lg border border-amber-800/20 bg-background/60 px-3 py-2 text-[13px] leading-relaxed text-foreground outline-none transition focus:border-amber-500/60 focus:ring-2 focus:ring-amber-500/25"
            />
            <p className="mt-2 flex items-center gap-1.5 px-1 text-[11px] text-muted-foreground">
              <Check className="size-3 text-primary" aria-hidden="true" />
              Enregistrée automatiquement — conservée sur cet appareil
            </p>
          </div>
        </>
      )}
    </div>
  );
}

/** Export / impression : menu regroupant impression navigateur, HTML autonome et EPUB. */
function ExportMenu({ doc }: { doc: DocPayload }) {
  const [open, setOpen] = useState(false);
  const disabled = doc.pdfOnly || (!doc.html && !doc.htmlFr);
  if (disabled) {
    return (
      <Button
        variant="outline"
        size="icon"
        disabled
        aria-label="Export indisponible — leçon au format PDF officiel uniquement"
        title="Export indisponible"
        className="size-10 border-amber-800/15 bg-card/70 text-amber-900/40 dark:text-amber-100/40"
      >
        <Printer className="size-4.5" aria-hidden="true" />
      </Button>
    );
  }
  const base = `/api/export/${doc.bookId}/${doc.docId}`;
  return (
    <div className="relative">
      <Button
        variant="outline"
        size="icon"
        aria-label="Imprimer ou exporter cette leçon"
        title="Imprimer / exporter"
        aria-expanded={open}
        className="size-10 border-amber-800/15 bg-card/70 text-amber-900 hover:bg-amber-100/60 dark:text-amber-100 dark:hover:bg-amber-900/40"
        onClick={() => setOpen((o) => !o)}
      >
        <Printer className="size-4.5" aria-hidden="true" />
      </Button>
      {open && (
        <>
          <div className="fixed inset-0 z-40" onClick={() => setOpen(false)} aria-hidden="true" />
          <div
            role="dialog"
            aria-label="Imprimer ou exporter"
            className="absolute right-0 top-12 z-50 w-64 rounded-xl border border-amber-800/15 bg-card p-1.5 shadow-lg"
          >
            <button
              type="button"
              className="flex w-full items-start gap-2.5 rounded-lg px-2.5 py-2 text-left text-[13px] text-foreground transition hover:bg-amber-100/70 dark:hover:bg-amber-900/40"
              onClick={() => {
                setOpen(false);
                window.print();
              }}
            >
              <Printer className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
              <span>
                <span className="block font-medium">Imprimer (PDF)</span>
                <span className="block text-[11px] leading-snug text-muted-foreground">
                  Dialogue d’impression du navigateur — « Enregistrer en PDF ».
                </span>
              </span>
            </button>
            <a
              href={`${base}?format=html`}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-start gap-2.5 rounded-lg px-2.5 py-2 text-left text-[13px] text-foreground transition hover:bg-amber-100/70 dark:hover:bg-amber-900/40"
              onClick={() => setOpen(false)}
            >
              <FileText className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
              <span>
                <span className="block font-medium">Page web autonome</span>
                <span className="block text-[11px] leading-snug text-muted-foreground">
                  Fichier HTML bilingue — s’ouvre partout, sans connexion.
                </span>
              </span>
            </a>
            <a
              href={`${base}?format=epub`}
              className="flex items-start gap-2.5 rounded-lg px-2.5 py-2 text-left text-[13px] text-foreground transition hover:bg-amber-100/70 dark:hover:bg-amber-900/40"
              onClick={() => setOpen(false)}
            >
              <Download className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
              <span>
                <span className="block font-medium">Livre numérique EPUB</span>
                <span className="block text-[11px] leading-snug text-muted-foreground">
                  Pour liseuse (EPUB 3) — français et arabe.
                </span>
              </span>
            </a>
          </div>
        </>
      )}
    </div>
  );
}

function MissingFr() {
  return (
    <div className="reader-col" dir="ltr" lang="fr">
      <ColumnChip lang="fr" label="Français" />
      <div className="flex min-h-40 items-center justify-center rounded-2xl border border-dashed border-amber-800/25 bg-amber-100/40 p-8 text-center dark:bg-amber-900/20">
        <div>
          <Hourglass className="mx-auto size-8 text-primary" aria-hidden="true" />
          <p className="mt-3 font-serif text-base font-medium text-amber-950 dark:text-amber-50">
            Traduction française en cours
          </p>
          <p className="mx-auto mt-1.5 max-w-xs text-sm leading-relaxed text-muted-foreground">
            Le texte arabe est disponible dans la colonne ci-contre. La traduction de ce
            document sera publiée prochainement.
          </p>
        </div>
      </div>
    </div>
  );
}

function DocNav({ doc }: { doc: DocPayload }) {
  return (
    <nav
      aria-label="Navigation entre les documents"
      className="no-print mt-10 flex items-center justify-between gap-3 border-t border-amber-800/15 pt-6"
    >
      {doc.prev ? (
        <Button
          variant="outline"
          className="h-12 max-w-[42%] flex-col items-start gap-0.5 rounded-xl border-amber-800/20 bg-card/70 px-4 text-left hover:bg-amber-100/60 dark:hover:bg-amber-900/40"
          onClick={() => navigate(`/livre/${doc.bookId}/${doc.prev!.docId}`)}
        >
          <span className="flex items-center gap-1 text-[10px] uppercase tracking-[0.12em] text-muted-foreground">
            <ChevronLeft className="size-3" aria-hidden="true" />
            Précédent
          </span>
          <span className="w-full truncate font-serif text-sm font-medium">
            {doc.prev.titleFr || doc.prev.titleAr}
          </span>
        </Button>
      ) : (
        <span className="w-[10%]" />
      )}
      <div className="hidden shrink-0 flex-col items-center gap-0.5 sm:flex">
        <Button
          variant="ghost"
          size="sm"
          className="gap-1.5 text-muted-foreground hover:text-foreground"
          onClick={() => navigate(`/livre/${doc.bookId}`)}
        >
          Sommaire
        </Button>
        {(doc.prev || doc.next) && (
          <span className="flex items-center gap-1 text-[10px] text-muted-foreground/70" title="Navigation clavier">
            <kbd className="rounded border border-border bg-muted px-1 font-sans text-[9px] leading-4">←</kbd>
            <kbd className="rounded border border-border bg-muted px-1 font-sans text-[9px] leading-4">→</kbd>
          </span>
        )}
      </div>
      {doc.next ? (
        <Button
          variant="outline"
          className="h-12 max-w-[42%] flex-col items-end gap-0.5 rounded-xl border-amber-800/20 bg-card/70 px-4 text-right hover:bg-amber-100/60 dark:hover:bg-amber-900/40"
          onClick={() => navigate(`/livre/${doc.bookId}/${doc.next!.docId}`)}
        >
          <span className="flex items-center gap-1 text-[10px] uppercase tracking-[0.12em] text-muted-foreground">
            Suivant
            <ChevronRight className="size-3" aria-hidden="true" />
          </span>
          <span className="w-full truncate font-serif text-sm font-medium">
            {doc.next.titleFr || doc.next.titleAr}
          </span>
        </Button>
      ) : (
        <span className="w-[10%]" />
      )}
    </nav>
  );
}

export function Reader({ bookId, docId }: { bookId: string; docId: string }) {
  const { data, error, loading } = useDoc(bookId, docId);
  const [mode, setMode] = useLocalState<ViewMode>("minhaj.viewMode", "both");
  const [textSize, setTextSize] = useLocalState<TextSize>("minhaj.textSize", "normal");
  const { toggle, has } = useFavorites();
  const [justToggled, setJustToggled] = useState(false);
  const [progress, setProgress] = useState(0);
  const { ranges: hlRanges, add: hlAdd, clearAll: hlClear, count: hlCount } = useHighlights(bookId, docId);
  const [hlSel, setHlSel] = useState<{ pane: HlPane; start: number; end: number; x: number; y: number } | null>(null);
  const [hlPopover, setHlPopover] = useState(false);
  const hlSupport = useSyncExternalStore(subscribeNoop, getHlSupport, getHlSupportServer);
  const outline = useMemo(() => lessonOutline(data?.htmlFr), [data?.htmlFr]);
  // Mémoïser les objets dangerouslySetInnerHTML est CRUCIAL : React ré-exécute
  // innerHTML (reconstruction complète du DOM, ~117 nœuds) lorsque l'objet
  // { __html } change d'identité à chaque re-rendu — p.ex. à chaque image du
  // défilement via la barre de progression. Identité stable → DOM intact.
  const htmlFr = data?.htmlFr;
  const htmlAr = data?.html;
  const frHtml = useMemo(() => (htmlFr != null ? { __html: htmlFr } : null), [htmlFr]);
  const arHtml = useMemo(() => (htmlAr != null ? { __html: htmlAr } : null), [htmlAr]);
  const [restoredNote, setRestoredNote] = useState(false);

  // Mémoriser la dernière lecture (reprise depuis l'accueil)
  useEffect(() => {
    if (data?.docId) {
      setLastDoc({
        bookId,
        docId,
        titleFr: data.titleFr || data.titleAr,
        titleAr: data.titleAr,
        bookTitleFr: data.bookTitleFr,
      });
    }
  }, [data?.docId, data?.titleFr, data?.titleAr, data?.bookTitleFr, bookId, docId]);

  // Reprise de la position de lecture (une seule fois par document — AVANT l'effet
  // de sauvegarde pour capturer la valeur avant toute écriture)
  const posDone = useRef(false);
  useEffect(() => {
    if (!data || data.pdfOnly || posDone.current) return;
    posDone.current = true;
    const pct = getReadPos(bookId, docId);
    if (pct === null) return;
    const mountedAt = Date.now();
    const t = window.setTimeout(() => {
      // annulé si l'utilisateur a déjà défilé entre-temps
      if (lastSaveRef.current > mountedAt) return;
      const el = document.documentElement;
      const max = el.scrollHeight - el.clientHeight;
      if (max > 40) {
        window.scrollTo({ top: (pct / 100) * max, behavior: "auto" });
        setRestoredNote(true);
        window.setTimeout(() => setRestoredNote(false), 2600);
      }
    }, 420);
    return () => {
      window.clearTimeout(t);
      posDone.current = false;
    };
  }, [data, bookId, docId]);

  // Barre de progression de lecture (défilement du document) + mémorisation position
  const lastSaveRef = useRef(0);
  useEffect(() => {
    const compute = () => {
      const doc = document.documentElement;
      const max = doc.scrollHeight - doc.clientHeight;
      return max > 40 ? Math.min(100, Math.max(0, (doc.scrollTop / max) * 100)) : 0;
    };
    const onScroll = () => {
      const pct = compute();
      setProgress(pct);
      if (data && !data.pdfOnly && pct > 2) {
        const now = Date.now();
        if (now - lastSaveRef.current > 500) {
          lastSaveRef.current = now;
          setReadPos(bookId, docId, pct);
        }
      }
    };
    onScroll(); // état initial (sauvegarde sans effet au sommet : pct 0 → garde)
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
    };
  }, [docId, data, bookId]);

  // Tableaux de vers (manẓūma) : marquer les structures hémistiche/séparateur/hémistiche
  // pour la mise en forme poétique (voir .verse-table dans globals.css).
  // Citations coraniques (colonne FR) : paragraphes ouvrés par « et clôturés par
  // une référence de verset — p.ex. « … » (Al-Shura, 18-20) — mis en exergue
  // par un panneau ambre discret (voir .quran-quote dans globals.css).
  useEffect(() => {
    if (!data || data.pdfOnly) return;
    document.querySelectorAll<HTMLElement>(".lesson-content table").forEach((table) => {
      if (table.classList.contains("verse-table")) return;
      const rows = Array.from(table.querySelectorAll("tr"));
      if (rows.length === 0 || table.querySelector("th")) return;
      const isVerse = rows.every((row) => {
        const cells = Array.from(row.children).filter((c) => c.tagName === "TD");
        if (cells.length !== 3) return false;
        const mid = (cells[1] as HTMLElement).innerText.replace(/[\u00a0\u202f ]/g, "");
        return mid === "";
      });
      if (isVerse) table.classList.add("verse-table");
    });
    const QUOTE_REF = /\([^()]{2,40},\s*[\d\s\u2013-]+\)\s*[»"]?\s*$/;
    document.querySelectorAll<HTMLElement>(".reader-col[dir='ltr'] .lesson-content > p").forEach((p) => {
      if (p.classList.contains("quran-quote")) return;
      const t = (p.innerText ?? "").trim();
      if (t.startsWith("«") && t.length > 120 && QUOTE_REF.test(t)) {
        p.classList.add("quran-quote");
      }
    });
  }, [data, mode, textSize]);

  // Surlignages persistants : inscription des ranges dans CSS.highlights (une
  // portée « mnhj-fr » / « mnhj-ar » par colonne — aucune mutation du DOM React)
  useEffect(() => {
    const bridge = hlBridge();
    if (!bridge || !data || data.pdfOnly) return;
    const W = window as unknown as { Highlight: new (...rs: Range[]) => unknown };
    const apply = () => {
      document.querySelectorAll<HTMLElement>(".reader-col").forEach((col) => {
        const pane: HlPane = col.getAttribute("dir") === "rtl" ? "ar" : "fr";
        const content = col.querySelector(".lesson-content");
        if (!content) return;
        const list = pane === "fr" ? hlRanges.fr : hlRanges.ar;
        const live = (list ?? [])
          .map(([s, e]) => rangeFromOffsets(content, s, e))
          .filter((r): r is Range => r !== null);
        if (live.length) bridge.set(`mnhj-${pane}`, new W.Highlight(...live));
        else bridge.delete(`mnhj-${pane}`);
      });
    };
    apply();
    return () => {
      bridge.delete("mnhj-fr");
      bridge.delete("mnhj-ar");
    };
  }, [data, mode, textSize, hlRanges]);

  // Sélection courante dans une colonne → barre flottante « Surligner »
  useEffect(() => {
    if (!hlSupport) return;
    const readSelection = () => {
      const sel = document.getSelection();
      if (!sel || sel.isCollapsed || sel.rangeCount === 0) {
        setHlSel(null);
        return;
      }
      const range = sel.getRangeAt(0);
      const node = range.commonAncestorContainer;
      const el = node instanceof Element ? node : node.parentElement;
      const col = el?.closest(".reader-col");
      const content = col?.querySelector(".lesson-content");
      if (!col || !content || !content.contains(range.startContainer) || !content.contains(range.endContainer)) {
        setHlSel(null);
        return;
      }
      const pane: HlPane = col.getAttribute("dir") === "rtl" ? "ar" : "fr";
      const s = textOffsetFrom(content, range.startContainer, range.startOffset);
      const e = textOffsetFrom(content, range.endContainer, range.endOffset);
      const rect = range.getBoundingClientRect();
      if (s === null || e === null || Math.abs(e - s) < 2 || (rect.width === 0 && rect.height === 0)) {
        setHlSel(null);
        return;
      }
      setHlSel({
        pane,
        start: Math.min(s, e),
        end: Math.max(s, e),
        x: Math.min(Math.max(rect.left + rect.width / 2, 90), window.innerWidth - 90),
        y: rect.top,
      });
    };
    const onSelChange = () => window.setTimeout(readSelection, 10);
    const onHide = () => setHlSel(null);
    document.addEventListener("selectionchange", onSelChange);
    window.addEventListener("scroll", onHide, { passive: true });
    return () => {
      document.removeEventListener("selectionchange", onSelChange);
      window.removeEventListener("scroll", onHide);
    };
  }, [hlSupport]);

  // Navigation clavier : ← → entre leçons (sauf saisie dans un champ)
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey) return;
      const el = e.target as HTMLElement | null;
      if (el && (el.tagName === "INPUT" || el.tagName === "TEXTAREA" || el.isContentEditable)) return;
      if (e.key === "ArrowLeft" && data?.prev) {
        navigate(`/livre/${bookId}/${data.prev.docId}`);
      } else if (e.key === "ArrowRight" && data?.next) {
        navigate(`/livre/${bookId}/${data.next.docId}`);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [bookId, data?.prev, data?.next]);

  if (loading) {
    return (
      <div className="mx-auto max-w-6xl px-4 py-10 sm:px-6 lg:px-8">
        <div className="flex items-center gap-3 text-muted-foreground">
          <Loader2 className="size-5 animate-spin text-primary" aria-hidden="true" />
          <p className="font-serif">Chargement du document…</p>
        </div>
        <Skeleton className="mt-8 h-24 rounded-2xl bg-amber-800/10" />
        <div className="mt-6 grid gap-6 lg:grid-cols-2">
          <Skeleton className="h-96 rounded-2xl bg-amber-800/10" />
          <Skeleton className="h-96 rounded-2xl bg-amber-800/10" />
        </div>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-20 text-center sm:px-6">
        <FileQuestion className="mx-auto size-10 text-primary" aria-hidden="true" />
        <h2 className="mt-4 font-serif text-2xl font-semibold text-amber-950 dark:text-amber-50">
          Document introuvable
        </h2>
        <p className="mt-2 text-sm text-muted-foreground">
          {error ?? `Le document « ${docId} » n'existe pas dans ce manuel.`}
        </p>
        <Button className="mt-6" variant="outline" onClick={() => navigate(`/livre/${bookId}`)}>
          <ArrowLeft className="size-4" aria-hidden="true" />
          Retour au manuel
        </Button>
      </div>
    );
  }

  const showFr = mode !== "ar";
  const showAr = mode !== "fr";
  const singleCol = mode !== "both";
  const isFav = has(bookId, docId);

  return (
    <div className="mx-auto max-w-6xl px-4 py-8 sm:px-6 lg:px-8">
      {/* Progression de lecture */}
      <div
        className="no-print fixed inset-x-0 top-0 z-40 h-0.5 bg-transparent"
        role="progressbar"
        aria-label="Progression de la lecture"
        aria-valuemin={0}
        aria-valuemax={100}
        aria-valuenow={Math.round(progress)}
      >
        <div
          className="relative h-full bg-gradient-to-r from-amber-500 via-orange-500 to-amber-600 transition-[width] duration-150 ease-out"
          style={{ width: `${progress}%` }}
        >
          {progress > 1 && progress < 99.5 && (
            <span
              className="absolute -right-[3px] top-1/2 size-[7px] -translate-y-1/2 rounded-full bg-amber-400 shadow-[0_0_8px_2px_rgba(251,191,36,0.75)]"
              aria-hidden="true"
            />
          )}
        </div>
      </div>
      <nav aria-label="Fil d'Ariane" className="mb-5 flex items-center gap-1 text-sm">
        <Button
          variant="ghost"
          size="sm"
          className="-ms-2 gap-2 text-muted-foreground hover:text-foreground"
          onClick={() => navigate("/")}
        >
          <ArrowLeft className="size-4" aria-hidden="true" />
          Bibliothèque
        </Button>
        <ChevronRight className="size-3.5 text-muted-foreground/60" aria-hidden="true" />
        <Button
          variant="ghost"
          size="sm"
          className="max-w-[14rem] gap-2 truncate text-muted-foreground hover:text-foreground"
          onClick={() => navigate(`/livre/${bookId}`)}
        >
          {data.bookTitleFr}
        </Button>
      </nav>

      <div className="flex flex-wrap items-start justify-between gap-4">
        <DocHeader doc={data} />
        <div className="no-print mt-1 flex min-w-0 flex-wrap items-center justify-end gap-2">
          <ViewModeToggle mode={mode} onChange={setMode} />
          <TextSizeControl size={textSize} onChange={setTextSize} />
          {data && !data.pdfOnly && <OutlineButton items={outline} />}
          {data && !data.pdfOnly && <NotesButton bookId={bookId} docId={docId} />}
          <Button
            variant="outline"
            size="icon"
            aria-label={isFav ? "Retirer des favoris" : "Ajouter aux favoris"}
            title={isFav ? "Retirer des favoris" : "Ajouter aux favoris"}
            className={cn(
              "size-10 border-amber-800/15 bg-card/70 hover:bg-amber-100/60 dark:hover:bg-amber-900/40",
              isFav ? "text-rose-600 dark:text-rose-400" : "text-amber-900 hover:text-rose-600 dark:text-amber-100 dark:hover:text-rose-400"
            )}
            onClick={() => {
              toggle({
                bookId,
                docId,
                titleFr: data.titleFr || data.titleAr,
                titleAr: data.titleAr,
                bookTitleFr: data.bookTitleFr,
              });
              setJustToggled(true);
              setTimeout(() => setJustToggled(false), 1200);
            }}
          >
            <Heart className={cn("size-4.5 transition-transform", isFav && "fill-current", justToggled && "scale-125")} aria-hidden="true" />
          </Button>
          {hlSupport && (
            <div className="relative">
              <Button
                variant="outline"
                size="icon"
                aria-label={hlCount > 0 ? `Surlignages (${hlCount}) — gérer` : "Aucun surlignage"}
                title={hlCount > 0 ? `${hlCount} surlignage${hlCount > 1 ? "s" : ""} enregistré${hlCount > 1 ? "s" : ""}` : "Surlignages : sélectionnez un passage puis « Surligner »"}
                aria-expanded={hlPopover}
                className={cn(
                  "size-10 border-amber-800/15 bg-card/70 hover:bg-amber-100/60 dark:hover:bg-amber-900/40",
                  hlCount > 0 ? "text-amber-700 dark:text-amber-300" : "text-amber-900/70 dark:text-amber-100/70"
                )}
                onClick={() => setHlPopover((o) => !o)}
              >
                <Highlighter className={cn("size-4.5", hlCount > 0 && "fill-amber-200/70 dark:fill-amber-700/50")} aria-hidden="true" />
                {hlCount > 0 && (
                  <span className="absolute -right-1.5 -top-1.5 flex size-5 items-center justify-center rounded-full bg-amber-600 text-[10px] font-semibold leading-none text-white shadow">
                    {hlCount > 9 ? "9+" : hlCount}
                  </span>
                )}
              </Button>
              {hlPopover && (
                <>
                  <div className="fixed inset-0 z-40" onClick={() => setHlPopover(false)} aria-hidden="true" />
                  <div
                    role="dialog"
                    aria-label="Gestion des surlignages"
                    className="absolute right-0 top-12 z-50 w-64 rounded-xl border border-amber-800/15 bg-card p-3 shadow-lg"
                  >
                    {hlCount === 0 ? (
                      <p className="text-xs leading-relaxed text-muted-foreground">
                        Sélectionnez un passage du texte — français ou arabe — puis touchez
                        « Surligner » : il sera conservé d’une visite à l’autre.
                      </p>
                    ) : (
                      <>
                        <p className="text-xs text-muted-foreground">
                          {hlCount} surlignage{hlCount > 1 ? "s" : ""} enregistré{hlCount > 1 ? "s" : ""} pour cette leçon.
                        </p>
                        <Button
                          variant="outline"
                          size="sm"
                          className="mt-2 w-full gap-1.5 border-rose-800/20 text-rose-700 hover:bg-rose-100/60 dark:text-rose-300 dark:hover:bg-rose-900/30"
                          onClick={() => {
                            hlClear();
                            setHlPopover(false);
                          }}
                        >
                          <Eraser className="size-3.5" aria-hidden="true" />
                          Tout effacer
                        </Button>
                      </>
                    )}
                  </div>
                </>
              )}
            </div>
          )}
          <ExportMenu doc={data} />
        </div>
      </div>

      {justToggled && (
        <p className="no-print mt-2 flex items-center gap-1.5 text-xs text-muted-foreground" role="status">
          <BookmarkCheck className="size-3.5 text-rose-500" aria-hidden="true" />
          {isFav ? "Leçon ajoutée à vos favoris — accessible depuis l'en-tête" : "Leçon retirée des favoris"}
        </p>
      )}

      {restoredNote && (
        <p className="no-print mt-2 flex items-center gap-1.5 text-xs text-muted-foreground" role="status">
          <Hourglass className="size-3.5 text-primary" aria-hidden="true" />
          Position de lecture restaurée
        </p>
      )}

      {data.pdfOnly ? (
        <PdfOnlyNotice doc={data} />
      ) : (
        <motion.div
          key={`${docId}-${mode}`}
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.35, ease: "easeOut" }}
          className={cn("grid gap-6", mode === "both" ? "lg:grid-cols-2" : "grid-cols-1")}
        >
          {showFr &&
            (data.hasFr ? (
              <article className="reader-col" dir="ltr" lang="fr">
                <ColumnChip lang="fr" label="Français — traduction" />
                <div
                  className={cn("lesson-content text-foreground/90", TEXT_SIZE_CLASS[textSize])}
                  dangerouslySetInnerHTML={frHtml ?? undefined}
                />
              </article>
            ) : (
              <MissingFr />
            ))}
          {showAr && (
            <article className="reader-col" dir="rtl" lang="ar">
              <ColumnChip lang="ar" label="العربية — الأصل" />
              <div
                className={cn("lesson-content text-foreground", TEXT_SIZE_AR_CLASS[textSize])}
                dangerouslySetInnerHTML={arHtml ?? undefined}
              />
            </article>
          )}
        </motion.div>
      )}

      {!data.pdfOnly && singleCol && (
        <p className="no-print mt-4 text-center text-xs text-muted-foreground">
          <ArrowRight className="me-1 inline size-3 rotate-180" aria-hidden="true" />
          Astuce : activez le mode « Bilingue » pour lire la traduction et l&apos;original
          côte à côte.
        </p>
      )}

      {/* Barre flottante « Surligner » (sélection active dans une colonne) */}
      {hlSupport && hlSel && (
        <div
          className="no-print fixed z-50 -translate-x-1/2 -translate-y-full"
          style={{ left: hlSel.x, top: Math.max(hlSel.y - 10, 46) }}
          role="toolbar"
          aria-label="Marquer la sélection"
        >
          <button
            type="button"
            onMouseDown={(e) => e.preventDefault()}
            onClick={() => {
              hlAdd(hlSel.pane, hlSel.start, hlSel.end);
              document.getSelection()?.removeAllRanges();
              setHlSel(null);
            }}
            className="flex items-center gap-1.5 rounded-full border border-amber-800/25 bg-card px-3.5 py-1.5 text-xs font-medium text-amber-900 shadow-lg transition-colors hover:bg-amber-100 focus-visible:outline-2 focus-visible:outline-ring dark:border-amber-200/20 dark:text-amber-100 dark:hover:bg-amber-900/60"
          >
            <Highlighter className="size-3.5" aria-hidden="true" />
            Surligner
          </button>
        </div>
      )}

      <DocNav doc={data} />
    </div>
  );
}
