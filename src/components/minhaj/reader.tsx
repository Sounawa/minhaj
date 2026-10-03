"use client";

import { ArrowLeft, ArrowRight, ChevronLeft, ChevronRight, Columns2, FileQuestion, Hourglass, Languages, Loader2 } from "lucide-react";
import { motion } from "framer-motion";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { cn } from "@/lib/utils";
import { navigate, useDoc, useLocalState } from "./hooks";
import type { DocPayload } from "./types";

type ViewMode = "both" | "fr" | "ar";

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
        <div className="no-print mt-1 shrink-0">
          <ViewModeToggle mode={mode} onChange={setMode} />
        </div>
      </div>

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
                className="lesson-content text-[15.5px] text-foreground/90"
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
              className="lesson-content text-foreground"
              dangerouslySetInnerHTML={{ __html: data.html }}
            />
          </article>
        )}
      </motion.div>

      {singleCol && (
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
