"use client";

import { useMemo, useState } from "react";
import { motion } from "framer-motion";
import {
  ArrowRight,
  BookMarked,
  CloudDownload,
  History,
  Layers,
  Library as LibraryIcon,
  Loader2,
  RefreshCcw,
  SearchX,
  Search,
  Sparkles,
} from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Progress } from "@/components/ui/progress";
import { Skeleton } from "@/components/ui/skeleton";
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { cn } from "@/lib/utils";
import { navigate, useLastDoc, useLibrary } from "./hooks";
import { SubjectTile } from "./subject-icon";
import { CYCLES, type CycleId } from "./types";

function fr(n: number) {
  return n.toLocaleString("fr-FR");
}

function Hero({
  docsFr,
  goalDocs,
  booksDownloaded,
  booksTotal,
}: {
  docsFr: number;
  goalDocs: number;
  booksDownloaded: number;
  booksTotal: number;
}) {
  const lastDoc = useLastDoc();
  return (
    <section className="pattern-islamic relative overflow-hidden border-b border-amber-800/15">
      <div className="hero-glow absolute inset-0" aria-hidden="true" />
      <div className="relative mx-auto max-w-7xl px-4 py-14 sm:px-6 sm:py-20 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, ease: "easeOut" }}
          className="max-w-3xl"
        >
          <Badge
            variant="outline"
            className="mb-4 gap-1.5 rounded-full border-amber-800/25 bg-amber-100/60 px-3 py-1 text-[11px] font-medium uppercase tracking-[0.14em] text-amber-900 dark:border-amber-200/20 dark:bg-amber-900/30 dark:text-amber-100"
          >
            <Sparkles className="size-3.5" aria-hidden="true" />
            Programme officiel — Royaume du Maroc
          </Badge>
          <h1 className="font-serif text-4xl font-semibold leading-tight tracking-tight text-amber-950 sm:text-5xl dark:text-amber-50">
            Minhāj{" "}
            <span className="font-arabic text-primary">مناهج</span>
          </h1>
          <p className="mt-4 max-w-2xl font-serif text-lg leading-relaxed text-amber-900/85 sm:text-xl dark:text-amber-100/85">
            L&apos;enseignement traditionnel marocain —{" "}
            <em className="text-primary not-italic">Taʿlīm ʿatīq</em> — en arabe et en
            français : monothéisme, droit rituel, sīra prophétique, tajwīd, tafsīr et
            bien d&apos;autres matières, du primaire au lycée.
          </p>
          <div className="mt-7 flex flex-wrap items-center gap-3">
            <Button
              size="lg"
              className="h-12 gap-2 rounded-xl bg-gradient-to-br from-amber-600 to-orange-800 px-6 font-serif text-amber-50 shadow-md shadow-amber-900/20 ring-1 ring-amber-900/20 hover:from-amber-500 hover:to-orange-700"
              onClick={() =>
                document.getElementById("bibliotheque")?.scrollIntoView({ behavior: "smooth" })
              }
            >
              Explorer la bibliothèque
              <ArrowRight className="size-4.5" aria-hidden="true" />
            </Button>
            <Button
              size="lg"
              variant="outline"
              className="h-12 gap-2 rounded-xl border-amber-800/25 bg-card/70 px-6 font-serif text-amber-950 hover:bg-amber-100/60 dark:text-amber-50 dark:hover:bg-amber-900/40"
              onClick={() => navigate("/livre/tawhid")}
            >
              <BookMarked className="size-4.5" aria-hidden="true" />
              Ouvrir un exemple bilingue
            </Button>
          </div>
          {lastDoc && (
            <motion.button
              type="button"
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.4, delay: 0.3 }}
              onClick={() => navigate(`/livre/${lastDoc.bookId}/${lastDoc.docId}`)}
              className="group mt-5 flex max-w-2xl items-center gap-3 rounded-2xl border border-amber-800/20 bg-card/60 px-4 py-3 text-left shadow-sm backdrop-blur-sm transition hover:border-amber-700/35 hover:bg-card/85 hover:shadow-md focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-primary"
            >
              <span className="flex size-10 shrink-0 items-center justify-center rounded-xl bg-gradient-to-br from-amber-600/15 to-orange-800/15 text-primary">
                <History className="size-5" aria-hidden="true" />
              </span>
              <span className="min-w-0 flex-1">
                <span className="block text-[11px] font-medium uppercase tracking-[0.14em] text-muted-foreground">
                  Reprendre la lecture
                </span>
                <span className="mt-0.5 block truncate font-serif text-[15px] font-semibold text-amber-950 dark:text-amber-50">
                  {lastDoc.titleFr || lastDoc.titleAr}
                </span>
                <span className="block truncate text-xs text-muted-foreground">{lastDoc.bookTitleFr}</span>
              </span>
              <ArrowRight
                className="size-4.5 shrink-0 text-primary transition-transform group-hover:translate-x-1"
                aria-hidden="true"
              />
            </motion.button>
          )}
        </motion.div>

        <motion.dl
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.15, ease: "easeOut" }}
          className="mt-12 grid grid-cols-1 gap-4 sm:grid-cols-3"
        >
          <div className="rounded-2xl border border-amber-800/15 bg-card/80 p-5 shadow-sm backdrop-blur-sm">
            <dt className="flex items-center gap-2 text-xs font-medium uppercase tracking-[0.12em] text-muted-foreground">
              <LibraryIcon className="size-4 text-primary" aria-hidden="true" />
              Manuels du programme
            </dt>
            <dd className="mt-2 font-serif text-3xl font-semibold text-amber-950 dark:text-amber-50">
              {booksTotal}
              <span className="ms-1.5 text-sm font-normal text-muted-foreground">
                sur 3 cycles scolaires
              </span>
            </dd>
          </div>
          <div className="rounded-2xl border border-amber-800/15 bg-card/80 p-5 shadow-sm backdrop-blur-sm">
            <dt className="flex items-center gap-2 text-xs font-medium uppercase tracking-[0.12em] text-muted-foreground">
              <Layers className="size-4 text-primary" aria-hidden="true" />
              Leçons bilingues
            </dt>
            <dd className="mt-2 font-serif text-3xl font-semibold text-amber-950 dark:text-amber-50">
              {fr(docsFr)}
              <span className="mx-1.5 text-base font-normal text-muted-foreground">/</span>
              <span className="text-lg font-normal text-muted-foreground">{fr(goalDocs)}</span>
            </dd>
            <Progress
              value={goalDocs ? (docsFr / goalDocs) * 100 : 0}
              className="mt-3 h-2 bg-amber-800/10"
            />
          </div>
          <div className="rounded-2xl border border-amber-800/15 bg-card/80 p-5 shadow-sm backdrop-blur-sm">
            <dt className="flex items-center gap-2 text-xs font-medium uppercase tracking-[0.12em] text-muted-foreground">
              <CloudDownload className="size-4 text-primary" aria-hidden="true" />
              Manuels reconstitués
            </dt>
            <dd className="mt-2 font-serif text-3xl font-semibold text-amber-950 dark:text-amber-50">
              {booksDownloaded}
              <span className="mx-1.5 text-base font-normal text-muted-foreground">/</span>
              <span className="text-lg font-normal text-muted-foreground">{booksTotal}</span>
            </dd>
            <p className="mt-3 text-xs leading-relaxed text-muted-foreground">
              Corpus officiel en cours de reconstitution après un incident technique.
            </p>
          </div>
        </motion.dl>
      </div>
    </section>
  );
}

function RecoveryBanner() {
  return (
    <div className="mx-auto mt-6 max-w-7xl px-4 sm:px-6 lg:px-8">
      <div className="flex items-start gap-3 rounded-xl border border-amber-600/30 bg-amber-100/60 p-4 text-sm text-amber-900 dark:border-amber-400/20 dark:bg-amber-900/25 dark:text-amber-100">
        <RefreshCcw className="mt-0.5 size-4.5 shrink-0 text-amber-700 dark:text-amber-300" aria-hidden="true" />
        <p className="leading-relaxed">
          <strong>Reconstitution du corpus en cours.</strong> Après un incident technique, les
          manuels officiels sont en cours de re-téléchargement ; les traductions françaises
          sont réintégrées progressivement, document par document. Merci de votre patience.
        </p>
      </div>
    </div>
  );
}

export function Home() {
  const { data, error, loading } = useLibrary();
  const [cycle, setCycle] = useState<CycleId>("all");
  const [subject, setSubject] = useState<string>("all");
  const [query, setQuery] = useState("");

  const levelById = useMemo(
    () => Object.fromEntries((data?.levels ?? []).map((l) => [l.id, l])),
    [data]
  );
  const subjectById = useMemo(
    () => Object.fromEntries((data?.subjects ?? []).map((s) => [s.id, s])),
    [data]
  );

  const books = useMemo(() => {
    if (!data) return [];
    const q = query.trim().toLowerCase();
    return data.books
      .filter((b) => (cycle === "all" ? true : levelById[b.level]?.cycle === cycle))
      .filter((b) => (subject === "all" ? true : b.subject === subject))
      .filter((b) => {
        if (!q) return true;
        const level = levelById[b.level];
        const subj = subjectById[b.subject];
        return (
          b.titleFr.toLowerCase().includes(q) ||
          b.titleAr.includes(query.trim()) ||
          b.id.includes(q) ||
          (subj?.titleFr.toLowerCase().includes(q) ?? false) ||
          (subj?.translit.toLowerCase().includes(q) ?? false) ||
          (level?.labelFr.toLowerCase().includes(q) ?? false)
        );
      })
      .sort((a, b) => a.order - b.order);
  }, [data, cycle, subject, query, levelById, subjectById]);

  if (loading) {
    return (
      <div className="mx-auto max-w-7xl px-4 py-16 sm:px-6 lg:px-8">
        <div className="flex items-center gap-3 text-muted-foreground">
          <Loader2 className="size-5 animate-spin text-primary" aria-hidden="true" />
          <p className="font-serif">Chargement de la bibliothèque…</p>
        </div>
        <div className="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          {Array.from({ length: 8 }).map((_, i) => (
            <Skeleton key={i} className="h-40 rounded-2xl bg-amber-800/10" />
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
          Bibliothèque indisponible
        </h2>
        <p className="mt-2 text-sm text-muted-foreground">{error}</p>
        <Button className="mt-6" variant="outline" onClick={() => window.location.reload()}>
          Réessayer
        </Button>
      </div>
    );
  }

  const { stats } = data;

  return (
    <>
      <Hero
        docsFr={stats.docsFr}
        goalDocs={stats.goalDocs}
        booksDownloaded={stats.booksDownloaded}
        booksTotal={stats.booksTotal}
      />
      {stats.booksDownloaded < stats.booksTotal && <RecoveryBanner />}

      <section
        id="bibliotheque"
        className="mx-auto max-w-7xl scroll-mt-20 px-4 py-10 sm:px-6 lg:px-8"
        aria-labelledby="titre-bibliotheque"
      >
        <div className="flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
          <div>
            <h2 id="titre-bibliotheque" className="font-serif text-2xl font-semibold text-amber-950 sm:text-3xl dark:text-amber-50">
              Bibliothèque
            </h2>
            <p className="mt-1 text-sm text-muted-foreground">
              {books.length} manuel{books.length > 1 ? "s" : ""} affiché
              {books.length > 1 ? "s" : ""} sur {stats.booksTotal}
            </p>
          </div>
          <div className="relative w-full md:max-w-xs">
            <Search
              className="pointer-events-none absolute start-3 top-1/2 size-4 -translate-y-1/2 text-muted-foreground"
              aria-hidden="true"
            />
            <Input
              type="search"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Rechercher un manuel, une matière…"
              aria-label="Rechercher un manuel"
              className="h-11 rounded-xl border-amber-800/20 bg-card/70 ps-9 text-sm shadow-none focus-visible:ring-primary/40"
            />
          </div>
        </div>

        <div className="mt-6 space-y-4">
          <Tabs value={cycle} onValueChange={(v) => setCycle(v as CycleId)}>
            <TabsList className="h-11 w-full justify-start gap-1 overflow-x-auto rounded-xl border border-amber-800/15 bg-secondary/70 p-1 sm:w-auto">
              {CYCLES.map((c) => (
                <TabsTrigger
                  key={c.id}
                  value={c.id}
                  title={c.desc}
                  className="min-h-9 rounded-lg px-4 text-sm data-[state=active]:bg-gradient-to-br data-[state=active]:from-amber-600 data-[state=active]:to-orange-800 data-[state=active]:text-amber-50 data-[state=active]:shadow-sm"
                >
                  {c.label}
                </TabsTrigger>
              ))}
            </TabsList>
          </Tabs>

          <div
            className="scroll-autumn flex items-center gap-2 overflow-x-auto pb-2"
            role="group"
            aria-label="Filtrer par matière"
          >
            <button
              type="button"
              onClick={() => setSubject("all")}
              aria-pressed={subject === "all"}
              className={cn(
                "inline-flex min-h-9 shrink-0 items-center gap-1.5 rounded-full border px-3.5 py-1.5 text-xs font-medium transition",
                subject === "all"
                  ? "border-amber-800/30 bg-primary text-primary-foreground shadow-sm"
                  : "border-amber-800/20 bg-card/70 text-muted-foreground hover:border-amber-800/35 hover:text-foreground"
              )}
            >
              Toutes les matières
            </button>
            {data.subjects
              .filter((s) => s.booksCount > 0)
              .map((s) => (
                <button
                  key={s.id}
                  type="button"
                  onClick={() => setSubject(s.id === subject ? "all" : s.id)}
                  aria-pressed={subject === s.id}
                  className={cn(
                    "inline-flex min-h-9 shrink-0 items-center gap-1.5 rounded-full border px-3.5 py-1.5 text-xs font-medium transition",
                    subject === s.id
                      ? "border-amber-800/30 bg-primary text-primary-foreground shadow-sm"
                      : "border-amber-800/20 bg-card/70 text-muted-foreground hover:border-amber-800/35 hover:text-foreground"
                  )}
                >
                  <span className="font-arabic text-sm leading-none">{s.labelAr}</span>
                  <span className="hidden sm:inline">· {s.titleFr.replace(/^(Le|La|Les|L’) /, "")}</span>
                </button>
              ))}
          </div>
        </div>

        {books.length === 0 ? (
          <div className="mt-12 rounded-2xl border border-dashed border-amber-800/25 bg-card/50 p-10 text-center">
            <SearchX className="mx-auto size-8 text-muted-foreground" aria-hidden="true" />
            <p className="mt-3 font-serif text-lg text-amber-950 dark:text-amber-50">
              Aucun manuel ne correspond à cette recherche.
            </p>
            <Button
              variant="link"
              className="mt-2 text-primary"
              onClick={() => {
                setQuery("");
                setSubject("all");
                setCycle("all");
              }}
            >
              Réinitialiser les filtres
            </Button>
          </div>
        ) : (
          <ul className="mt-6 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            {books.map((b, i) => {
              const level = levelById[b.level];
              const subj = subjectById[b.subject];
              const pct = b.docsTotal ? Math.round((b.docsFr / b.docsTotal) * 100) : 0;
              return (
                <motion.li
                  key={b.id}
                  initial={{ opacity: 0, y: 10 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true, margin: "-40px" }}
                  transition={{ duration: 0.35, delay: Math.min(i % 8, 5) * 0.04 }}
                >
                  <button
                    type="button"
                    onClick={() => navigate(`/livre/${b.id}`)}
                    className={cn(
                      "group flex h-full w-full flex-col rounded-2xl border p-5 text-left shadow-sm transition-all duration-200 hover:-translate-y-0.5 hover:shadow-md hover:ring-1 hover:ring-primary/25 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary",
                      b.downloaded
                        ? "border-amber-800/15 bg-card/80 hover:border-amber-800/30"
                        : "border-dashed border-amber-800/25 bg-card/40"
                    )}
                    aria-label={`Ouvrir le manuel ${b.titleFr} — ${level?.shortFr ?? b.level}`}
                  >
                    <div className="flex items-start justify-between gap-3">
                      <SubjectTile
                        subjectId={b.subject}
                        className="size-11"
                        iconClassName="size-5.5"
                      />
                      <Badge
                        variant="secondary"
                        className="rounded-full border border-amber-800/15 bg-secondary/80 text-[11px] font-medium text-secondary-foreground"
                      >
                        {level?.shortFr ?? b.level}
                      </Badge>
                    </div>
                    <h3 className="mt-3.5 font-serif text-lg font-semibold leading-snug text-amber-950 transition group-hover:text-primary dark:text-amber-50">
                      {b.titleFr}
                    </h3>
                    <p
                      dir="rtl"
                      lang="ar"
                      className="mt-1 text-right font-arabic text-base leading-relaxed text-muted-foreground"
                    >
                      {b.titleAr}
                    </p>
                    <p className="mt-1 text-xs italic text-muted-foreground/80">
                      {subj?.translit}
                    </p>
                    <div className="mt-auto pt-4">
                      {b.downloaded ? (
                        <>
                          <div className="flex items-center justify-between text-[11px] text-muted-foreground">
                            <span>
                              {b.docsFr}/{b.docsTotal} documents bilingues
                            </span>
                            <span className="font-medium text-primary">{pct}%</span>
                          </div>
                          <Progress value={pct} className="mt-1.5 h-1.5 bg-amber-800/10" />
                        </>
                      ) : (
                        <p className="flex items-center gap-1.5 text-xs text-muted-foreground">
                          <CloudDownload className="size-3.5" aria-hidden="true" />
                          Manuel en attente de reconstitution
                        </p>
                      )}
                    </div>
                  </button>
                </motion.li>
              );
            })}
          </ul>
        )}
      </section>
    </>
  );
}
