"use client";

import { useMemo, useState } from "react";
import { motion } from "framer-motion";
import {
  ArrowLeft,
  BookOpen,
  CloudDownload,
  Compass,
  FileText,
  Hourglass,
  Languages,
  Loader2,
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
              title="Texte publié par le Ministère au format PDF officiel"
            >
              <FileText className="size-3" aria-hidden="true" />
              PDF
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
                  <Badge className="gap-1 rounded-full bg-gradient-to-br from-amber-600 to-orange-800 text-[10px] text-amber-50 shadow-sm">
                    <Languages className="size-3" aria-hidden="true" />
                    bilingue
                  </Badge>
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
            </div>

            {lessons.length === 0 ? (
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
