"use client";

import { useEffect, useState } from "react";
import { ArrowLeft, ArrowRight, BookMarked, BookmarkCheck, ChevronLeft, ChevronRight, Columns2, ExternalLink, FileQuestion, FileText, Heart, Hourglass, Languages, Loader2, Printer } from "lucide-react";
import { motion } from "framer-motion";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { cn } from "@/lib/utils";
import { navigate, setLastDoc, useDoc, useFavorites, useLocalState } from "./hooks";
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
      <p dir="rtl" lang="ar" className="mt-1.5 text-right font-arabic text-xl leading-relaxed text-primary">
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
      <Button
        variant="ghost"
        size="sm"
        className="hidden shrink-0 gap-1.5 text-muted-foreground hover:text-foreground sm:inline-flex"
        onClick={() => navigate(`/livre/${doc.bookId}`)}
      >
        Sommaire
      </Button>
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
        <div className="no-print mt-1 flex shrink-0 flex-wrap items-center justify-end gap-2">
          <ViewModeToggle mode={mode} onChange={setMode} />
          <TextSizeControl size={textSize} onChange={setTextSize} />
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
          <Button
            variant="outline"
            size="icon"
            aria-label="Imprimer cette leçon"
            title="Imprimer"
            className="size-10 border-amber-800/15 bg-card/70 text-amber-900 hover:bg-amber-100/60 dark:text-amber-100 dark:hover:bg-amber-900/40"
            onClick={() => window.print()}
          >
            <Printer className="size-4.5" aria-hidden="true" />
          </Button>
        </div>
      </div>

      {justToggled && (
        <p className="no-print mt-2 flex items-center gap-1.5 text-xs text-muted-foreground" role="status">
          <BookmarkCheck className="size-3.5 text-rose-500" aria-hidden="true" />
          {isFav ? "Leçon ajoutée à vos favoris — accessible depuis l'en-tête" : "Leçon retirée des favoris"}
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
                  dangerouslySetInnerHTML={{ __html: data.htmlFr }}
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
                dangerouslySetInnerHTML={{ __html: data.html }}
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

      <DocNav doc={data} />
    </div>
  );
}
