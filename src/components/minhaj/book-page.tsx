"use client";

import { useMemo, useState } from "react";
import { motion } from "framer-motion";
import {
  ArrowLeft,
  Award,
  BookMarked,
  BookOpen,
  CloudDownload,
  Compass,
  Download,
  FileText,
  Hourglass,
  Languages,
  Loader2,
  Printer,
  Search,
  SearchX,
} from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Progress } from "@/components/ui/progress";
import { Skeleton } from "@/components/ui/skeleton";
import { cn } from "@/lib/utils";
import { navigate, useBookDetail } from "./hooks";
import { SubjectTile } from "./subject-icon";
import type { LessonSummary } from "./types";

function LessonRow({
  bookId,
  lesson,
  index,
}: {
  bookId: string;
  lesson: LessonSummary;
  index: number;
}) {
  return (
    <li>
      <button
        type="button"
        onClick={() => navigate(`/livre/${bookId}/${lesson.docId}`)}
        className="group flex w-full items-center gap-4 rounded-xl border border-transparent px-3 py-3 text-left transition-all hover:border-amber-800/20 hover:bg-amber-100/50 hover:shadow-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary dark:hover:bg-amber-900/25"
        aria-label={`Ouvrir : ${lesson.titleFr || lesson.titleAr}`}
      >
        <span
          className={cn(
            "flex size-9 shrink-0 items-center justify-center rounded-lg font-serif text-sm font-semibold",
            lesson.pdfOnly
              ? "border border-amber-700/30 bg-amber-100/70 text-amber-900 dark:border-amber-300/20 dark:bg-amber-900/40 dark:text-amber-100"
              : lesson.hasFr
                ? "bg-gradient-to-br from-amber-600 to-orange-800 text-amber-50 shadow-sm"
                : "bg-secondary text-secondary-foreground"
          )}
          aria-hidden="true"
        >
          {index}
        </span>
        <span className="min-w-0 flex-1">
          {lesson.titleFr ? (
            <span className="block truncate font-serif text-sm font-medium text-amber-950 transition group-hover:text-primary dark:text-amber-50">
              {lesson.titleFr}
            </span>
          ) : (
            <span className="block truncate text-sm italic text-muted-foreground">
              Titre français à venir
            </span>
          )}
          <span
            dir="rtl"
            lang="ar"
            className="mt-0.5 block truncate text-right font-arabic text-sm leading-relaxed text-muted-foreground"
          >
            {lesson.titleAr}
          </span>
        </span>
        <span className="flex shrink-0 items-center gap-1.5">
          {lesson.savant && (
            <Badge
              variant="outline"
              title="Traduction française révisée (terminologie académique, versets vérifiés)"
              className="hidden gap-1 rounded-full border-amber-500/50 bg-gradient-to-br from-amber-100 to-yellow-50 text-[10px] font-semibold text-amber-800 sm:inline-flex dark:border-amber-400/30 dark:from-amber-900/50 dark:to-amber-800/30 dark:text-amber-200"
            >
              <BookMarked className="size-3" aria-hidden="true" />
              savante
            </Badge>
          )}
          {lesson.sample && (
            <Badge
              variant="outline"
              className="hidden rounded-full border-amber-700/30 bg-amber-100/70 text-[10px] text-amber-900 sm:inline-flex dark:border-amber-300/20 dark:bg-amber-900/40 dark:text-amber-100"
            >
              échantillon
            </Badge>
          )}
          {lesson.pdfOnly ? (
            <Badge
              variant="outline"
              className="gap-1 rounded-full border-amber-700/30 bg-amber-100/70 text-[10px] text-amber-900 dark:border-amber-300/20 dark:bg-amber-900/40 dark:text-amber-100"
              title="Texte publié par le Ministère au format PDF officiel — extraction du texte arabe par OCR disponible dans la leçon"
            >
              <FileText className="size-3" aria-hidden="true" />
              PDF · OCR
            </Badge>
          ) : lesson.hasFr ? (
            <Badge className="gap-1 rounded-full bg-gradient-to-br from-amber-600 to-orange-800 text-[10px] text-amber-50 shadow-sm">
              <Languages className="size-3" aria-hidden="true" />
              bilingue
            </Badge>
          ) : (
            <Badge
              variant="secondary"
              className="gap-1 rounded-full text-[10px]"
              title="Texte ar disponible — traduction en cours"
            >
              <Hourglass className="size-3" aria-hidden="true" />
              ar
            </Badge>
          )}
        </span>
      </button>
    </li>
  );
}

/** Export du manuel entier : impression du bundle HTML, page autonome, EPUB. */
function BookExportMenu({ bookId, docsTotal }: { bookId: string; docsTotal: number }) {
  const [open, setOpen] = useState(false);
  const base = `/api/export/${bookId}`;
  return (
    <div className="relative shrink-0">
      <Button
        variant="outline"
        size="sm"
        aria-label="Exporter le manuel complet"
        title="Exporter le manuel complet"
        aria-expanded={open}
        className="h-10 gap-2 rounded-xl border-amber-800/15 bg-card/70 text-amber-900 hover:bg-amber-100/60 dark:text-amber-100 dark:hover:bg-amber-900/40"
        onClick={() => setOpen((o) => !o)}
      >
        <Download className="size-4" aria-hidden="true" />
        Exporter
      </Button>
      {open && (
        <>
          <div className="fixed inset-0 z-40" onClick={() => setOpen(false)} aria-hidden="true" />
          <div
            role="dialog"
            aria-label="Exporter le manuel"
            className="absolute end-0 top-12 z-50 w-72 rounded-xl border border-amber-800/15 bg-card p-1.5 shadow-lg"
          >
            <p className="px-2.5 pb-1 pt-2 text-[11px] font-semibold uppercase tracking-wide text-muted-foreground">
              Manuel complet · {docsTotal} documents
            </p>
            <a
              href={`${base}?format=html&print=1`}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-start gap-2.5 rounded-lg px-2.5 py-2 text-left text-[13px] text-foreground transition hover:bg-amber-100/70 dark:hover:bg-amber-900/40"
              onClick={() => setOpen(false)}
            >
              <Printer className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
              <span>
                <span className="block font-medium">Imprimer (PDF)</span>
                <span className="block text-[11px] leading-snug text-muted-foreground">
                  Ouvre le manuel bilingue puis le dialogue d’impression.
                </span>
              </span>
            </a>
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
                  Sommaire cliquable + toutes les leçons — sans connexion.
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
                  Un chapitre par leçon — pour liseuse (EPUB 3).
                </span>
              </span>
            </a>
          </div>
        </>
      )}
    </div>
  );
}

export function BookPage({ bookId }: { bookId: string }) {
  const { data, error, loading } = useBookDetail(bookId);
  const [query, setQuery] = useState("");

  const lessons = useMemo(() => {
    if (!data) return [];
    const q = query.trim().toLowerCase();
    if (!q) return data.lessons;
    return data.lessons.filter(
      (l) =>
        l.titleFr.toLowerCase().includes(q) ||
        l.titleAr.includes(query.trim()) ||
        l.docId.includes(q)
    );
  }, [data, query]);

  if (loading) {
    return (
      <div className="mx-auto max-w-5xl px-4 py-10 sm:px-6 lg:px-8">
        <div className="flex items-center gap-3 text-muted-foreground">
          <Loader2 className="size-5 animate-spin text-primary" aria-hidden="true" />
          <p className="font-serif">Chargement du manuel…</p>
        </div>
        <Skeleton className="mt-8 h-44 rounded-2xl bg-amber-800/10" />
        <div className="mt-6 space-y-3">
          {Array.from({ length: 6 }).map((_, i) => (
            <Skeleton key={i} className="h-16 rounded-xl bg-amber-800/10" />
          ))}
        </div>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-20 text-center sm:px-6">
        <SearchX className="mx-auto size-10 text-primary" aria-hidden="true" />
        <h2 className="mt-4 font-serif text-2xl font-semibold text-amber-950 dark:text-amber-50">
          Manuel introuvable
        </h2>
        <p className="mt-2 text-sm text-muted-foreground">
          {error ?? `Le manuel « ${bookId} » n'existe pas dans la bibliothèque.`}
        </p>
        <Button className="mt-6" variant="outline" onClick={() => navigate("/")}>
          <ArrowLeft className="size-4" aria-hidden="true" />
          Retour à la bibliothèque
        </Button>
      </div>
    );
  }

  const { book, level, subject, program } = data;
  const pct = book.docsTotal ? Math.round((book.docsFr / book.docsTotal) * 100) : 0;
  const savantPct = book.docsFr
    ? Math.min(100, Math.round((book.docsSavant / book.docsFr) * 100))
    : 0;
  // Intégrale = toutes les traductions FR existantes sont de niveau savant
  // (les leçons PDF-only, sans texte source, sont hors du champ de la traduction).
  const fullSavant = book.docsFr > 0 && book.docsSavant >= book.docsFr;

  return (
    <div className="mx-auto max-w-5xl px-4 py-8 sm:px-6 lg:px-8">
      <nav aria-label="Fil d'Ariane" className="mb-5">
        <Button
          variant="ghost"
          size="sm"
          className="-ms-2 gap-2 text-muted-foreground hover:text-foreground"
          onClick={() => navigate("/")}
        >
          <ArrowLeft className="size-4" aria-hidden="true" />
          Bibliothèque
        </Button>
      </nav>

      <motion.header
        initial={{ opacity: 0, y: 12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="pattern-islamic relative overflow-hidden rounded-2xl border border-amber-800/15 bg-card/70 shadow-sm"
      >
        <div className="hero-glow absolute inset-0" aria-hidden="true" />
        <div className="relative flex flex-col gap-5 p-6 sm:flex-row sm:items-start sm:p-8">
          <SubjectTile subjectId={book.subject} className="size-16 shrink-0" iconClassName="size-8" />
          <div className="min-w-0 flex-1">
            <div className="flex flex-wrap items-center gap-2">
              <Badge className="gap-1.5 rounded-full bg-gradient-to-br from-amber-600 to-orange-800 text-[11px] text-amber-50 shadow-sm">
                {level?.shortFr ?? book.level}
              </Badge>
              {subject && (
                <Badge
                  variant="outline"
                  className="gap-1.5 rounded-full border-amber-800/25 bg-amber-100/60 text-[11px] text-amber-900 dark:border-amber-200/20 dark:bg-amber-900/30 dark:text-amber-100"
                >
                  <Compass className="size-3" aria-hidden="true" />
                  {subject.titleFr}
                </Badge>
              )}
            </div>
            <h1 className="mt-3 font-serif text-2xl font-semibold leading-tight text-amber-950 sm:text-3xl dark:text-amber-50">
              {book.titleFr}
            </h1>
            <p dir="rtl" lang="ar" className="mt-1.5 text-right font-arabic text-xl leading-relaxed text-primary">
              {book.titleAr}
            </p>
            <p className="mt-2 text-sm italic text-muted-foreground">{level?.labelFr}</p>

            {book.downloaded ? (
              <div className="mt-5 max-w-md">
                <div className="flex items-center justify-between text-xs text-muted-foreground">
                  <span>
                    {book.docsFr}/{book.docsTotal} documents bilingues · {book.lessonsTotal}{" "}
                    leçon{book.lessonsTotal > 1 ? "s" : ""}
                    {book.hasIntro ? " + introduction" : ""}
                  </span>
                  <span className="font-semibold text-primary">{pct}%</span>
                </div>
                <Progress value={pct} className="mt-1.5 h-2 bg-amber-800/10" />
                {book.docsSavant > 0 && !fullSavant && book.docsFr > 0 && (
                  <div className="mt-1.5">
                    <div className="flex items-center justify-between text-[11px] text-muted-foreground">
                      <span className="flex items-center gap-1">
                        <BookMarked
                          className="size-3 text-amber-700/80 dark:text-amber-400/80"
                          aria-hidden="true"
                        />
                        dont couche savante
                      </span>
                      <span className="font-semibold tabular-nums text-amber-700 dark:text-amber-400">
                        {book.docsSavant}/{book.docsFr}
                      </span>
                    </div>
                    <div
                      className="mt-1 h-1.5 w-full overflow-hidden rounded-full bg-amber-800/10"
                      role="progressbar"
                      aria-label="Documents en traduction savante"
                      aria-valuemin={0}
                      aria-valuemax={100}
                      aria-valuenow={savantPct}
                    >
                      <div
                        className="bar-savant h-full rounded-full"
                        style={{ width: `${savantPct}%` }}
                      />
                    </div>
                  </div>
                )}
                {book.docsSavant > 0 && (
                  <div className="mt-2.5 flex flex-wrap items-center gap-2">
                    {fullSavant ? (
                      <Badge
                        variant="outline"
                        title={`Toutes les traductions de ce manuel (${book.docsSavant}/${book.docsFr}) sont de niveau savant : terminologie académique, versets et hadiths vérifiés`}
                        className="gap-1.5 rounded-full border-amber-500/50 bg-gradient-to-br from-amber-100 to-yellow-50 px-2.5 py-0.5 font-semibold text-amber-800 dark:border-amber-400/30 dark:from-amber-900/50 dark:to-amber-800/30 dark:text-amber-200"
                      >
                        <Award className="size-3.5" aria-hidden="true" />
                        Traduction savante intégrale
                      </Badge>
                    ) : (
                      <Badge
                        variant="outline"
                        title="Documents en traduction savante (registre) dans ce manuel"
                        className="gap-1.5 rounded-full border-amber-700/30 bg-amber-100/70 px-2.5 py-0.5 text-amber-900 dark:border-amber-300/20 dark:bg-amber-900/40 dark:text-amber-100"
                      >
                        <BookMarked className="size-3.5" aria-hidden="true" />
                        {book.docsSavant}/{book.docsFr} traductions savantes
                      </Badge>
                    )}
                    {!fullSavant && (
                      <span className="text-[11px] font-medium text-amber-700 dark:text-amber-400">
                        {savantPct}% du corpus traduit en niveau savant
                      </span>
                    )}
                  </div>
                )}
              </div>
            ) : (
              <div className="mt-5 flex items-center gap-2 rounded-xl border border-dashed border-amber-800/30 bg-amber-100/40 px-4 py-3 text-sm text-amber-900 dark:bg-amber-900/20 dark:text-amber-100">
                <CloudDownload className="size-4.5 shrink-0 text-primary" aria-hidden="true" />
                Ce manuel n&apos;est pas encore reconstitué — le corpus officiel est en cours de
                re-téléchargement.
              </div>
            )}
          </div>
        </div>
      </motion.header>

      {book.downloaded ? (
        <>
          {data.intro && (
            <motion.section
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.4, delay: 0.1 }}
              className="mt-6"
              aria-labelledby="titre-intro"
            >
              <button
                type="button"
                onClick={() => navigate(`/livre/${bookId}/${data.intro!.docId}`)}
                className="group flex w-full items-center gap-4 rounded-2xl border border-amber-800/20 bg-gradient-to-br from-amber-100/70 to-orange-100/50 p-5 text-left shadow-sm transition-all hover:-translate-y-0.5 hover:shadow-md hover:ring-1 hover:ring-primary/25 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary dark:from-amber-900/30 dark:to-orange-950/30"
              >
                <span className="flex size-11 shrink-0 items-center justify-center rounded-xl bg-gradient-to-br from-amber-600 to-orange-800 text-amber-50 shadow-sm">
                  <BookOpen className="size-5.5" aria-hidden="true" />
                </span>
                <span className="min-w-0 flex-1">
                  <span id="titre-intro" className="block font-serif text-base font-semibold text-amber-950 transition group-hover:text-primary dark:text-amber-50">
                    Introduction du manuel
                  </span>
                  <span dir="rtl" lang="ar" className="mt-0.5 block truncate text-right font-arabic text-sm text-muted-foreground">
                    {data.intro.titleAr}
                  </span>
                </span>
                {data.intro.hasFr ? (
                  <span className="flex shrink-0 items-center gap-1.5">
                    {data.intro.savant && (
                      <Badge
                        variant="outline"
                        title="Traduction française révisée (terminologie académique, versets vérifiés)"
                        className="gap-1 rounded-full border-amber-500/50 bg-gradient-to-br from-amber-100 to-yellow-50 text-[10px] font-semibold text-amber-800 dark:border-amber-400/30 dark:from-amber-900/50 dark:to-amber-800/30 dark:text-amber-200"
                      >
                        <BookMarked className="size-3" aria-hidden="true" />
                        savante
                      </Badge>
                    )}
                    <Badge className="gap-1 rounded-full bg-gradient-to-br from-amber-600 to-orange-800 text-[10px] text-amber-50 shadow-sm">
                      <Languages className="size-3" aria-hidden="true" />
                      bilingue
                    </Badge>
                  </span>
                ) : (
                  <Badge variant="secondary" className="gap-1 rounded-full text-[10px]">
                    <Hourglass className="size-3" aria-hidden="true" />
                    ar
                  </Badge>
                )}
              </button>
            </motion.section>
          )}

          <section className="mt-8" aria-labelledby="titre-lecons">
            <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
              <h2 id="titre-lecons" className="font-serif text-xl font-semibold text-amber-950 dark:text-amber-50">
                Leçons{" "}
                <span className="text-sm font-normal text-muted-foreground">
                  ({data.lessons.length})
                </span>
              </h2>
              <div className="flex flex-col gap-2 sm:flex-row sm:items-center">
                {data.lessons.length > 0 && (
                  <div className="relative w-full sm:max-w-xs">
                    <Search
                      className="pointer-events-none absolute start-3 top-1/2 size-4 -translate-y-1/2 text-muted-foreground"
                      aria-hidden="true"
                    />
                    <Input
                      type="search"
                      value={query}
                      onChange={(e) => setQuery(e.target.value)}
                      placeholder="Filtrer les leçons…"
                      aria-label="Filtrer les leçons"
                      className="h-10 rounded-xl border-amber-800/20 bg-card/70 ps-9 text-sm shadow-none focus-visible:ring-primary/40"
                    />
                  </div>
                )}
                <BookExportMenu bookId={bookId} docsTotal={book.docsTotal} />
              </div>
            </div>

            {data.lessons.length === 0 && data.book.unpublished ? (
              <div className="mt-6 rounded-2xl border border-amber-800/20 bg-gradient-to-br from-amber-50/80 to-orange-50/60 p-6 shadow-sm dark:from-amber-950/30 dark:to-orange-950/20">
                <p className="flex items-center gap-2 font-serif text-base font-semibold text-amber-950 dark:text-amber-50">
                  <Hourglass className="size-4.5 text-primary" aria-hidden="true" />
                  Leçons non publiées par le ministère
                </p>
                <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
                  Contrairement aux autres niveaux, le portail officiel du ministère des Habous
                  ne publie à ce jour ni page d'ouvrage ni pages de cours pour cette année. La
                  présentation bilingue ci-dessus résume le programme attendu ; les leçons
                  seront intégrées dès leur publication officielle.
                </p>
              </div>
            ) : lessons.length === 0 ? (
              <p className="mt-6 rounded-xl border border-dashed border-amber-800/25 bg-card/50 p-6 text-center text-sm text-muted-foreground">
                Aucune leçon ne correspond à « {query} ».
              </p>
            ) : (
              <ol className="scroll-autumn mt-4 max-h-[28rem] space-y-1.5 overflow-y-auto rounded-2xl border border-amber-800/15 bg-card/60 p-2 shadow-inner">
                {lessons.map((l, i) => (
                  <LessonRow key={l.docId} bookId={bookId} lesson={l} index={i + 1} />
                ))}
              </ol>
            )}
          </section>
        </>
      ) : (
        <div className="mt-8 rounded-2xl border border-dashed border-amber-800/25 bg-card/50 p-10 text-center">
          <FileText className="mx-auto size-9 text-muted-foreground" aria-hidden="true" />
          <p className="mt-3 font-serif text-lg text-amber-950 dark:text-amber-50">
            Contenu en attente
          </p>
          <p className="mx-auto mt-2 max-w-md text-sm leading-relaxed text-muted-foreground">
            Ce manuel ({program.nameFr}) sera disponible dès la fin de la reconstitution du
            corpus officiel. Les traductions françaises suivront ensuite, leçon par leçon.
          </p>
        </div>
      )}
    </div>
  );
}
