"use client";

import { useMemo } from "react";
import { motion } from "framer-motion";
import { Award, BookOpenCheck, FileWarning, Layers, Loader2, ScanText } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { cn } from "@/lib/utils";
import { navigate } from "./hooks";
import { SubjectTile } from "./subject-icon";
import type { LibraryPayload, BookSummary } from "./types";

function fr(n: number) {
  return n.toLocaleString("fr-FR");
}

function pct(n: number, total: number) {
  return total > 0 ? Math.round((n / total) * 100) : 0;
}

/** Barre empilée à trois segments : savant / machine / PDF. */
function StackedBar({
  savant,
  machine,
  pdf,
  height = "h-3.5",
  rounded = "rounded-full",
  showTicks = false,
  total,
}: {
  savant: number;
  machine: number;
  pdf: number;
  height?: string;
  rounded?: string;
  showTicks?: boolean;
  total?: number;
}) {
  const sum = savant + machine + pdf;
  const w = (n: number) => (sum > 0 ? (n / sum) * 100 : 0);
  return (
    <div
      role="img"
      aria-label={`Traduction savante ${fr(savant)}, brouillon machine ${fr(machine)}, PDF seul ${fr(pdf)}`}
      className={cn("relative w-full overflow-hidden bg-muted/60", height, rounded)}
    >
      <div className="flex h-full w-full">
        <div
          className="h-full bg-gradient-to-r from-amber-600 to-orange-700 dark:from-amber-500 dark:to-orange-600"
          style={{ width: `${w(savant)}%` }}
        />
        <div
          className="h-full bg-amber-300/80 dark:bg-amber-400/50"
          style={{ width: `${w(machine)}%` }}
        />
        <div className="h-full flex-1 bg-stone-300/70 dark:bg-stone-600/50" />
      </div>
      {showTicks && total ? (
        <>
          <span
            aria-hidden="true"
            className="absolute inset-y-0 w-px bg-background/70"
            style={{ left: `${(w(savant) + w(machine)) * 0.5}%` }}
          />
          <span
            aria-hidden="true"
            className="absolute inset-y-0 w-px bg-background/70"
            style={{ left: `${w(savant) + w(machine)}%` }}
          />
        </>
      ) : null}
    </div>
  );
}

/** Pastille de légende. */
function LegendDot({ className }: { className?: string }) {
  return (
    <span
      aria-hidden="true"
      className={cn("inline-block size-2.5 shrink-0 rounded-full", className)}
    />
  );
}

interface SubjectRow {
  id: string;
  titleFr: string;
  translit: string;
  labelAr: string;
  savant: number;
  machine: number;
  pdf: number;
  total: number;
  completeBooks: number;
}

export function TranslationProgress({ data }: { data: LibraryPayload }) {
  const { stats } = data;

  const tiers = useMemo(() => {
    const savant = stats.docsSavant ?? 0;
    const machine = Math.max(0, stats.docsFr - savant);
    const pdf = Math.max(0, stats.docsTotal - stats.docsFr);
    return { savant, machine, pdf, total: stats.docsTotal };
  }, [stats]);

  const subjects = useMemo<SubjectRow[]>(() => {
    const map = new Map<
      string,
      { titleFr: string; translit: string; labelAr: string; savant: number; machine: number; pdf: number; completeBooks: number }
    >();
    for (const s of data.subjects) {
      map.set(s.id, { titleFr: s.titleFr, translit: s.translit, labelAr: s.labelAr, savant: 0, machine: 0, pdf: 0, completeBooks: 0 });
    }
    for (const b of data.books as BookSummary[]) {
      const row = map.get(b.subject);
      if (!row || !b.downloaded) continue;
      const savant = b.docsSavant;
      const machine = Math.max(0, b.docsFr - savant);
      const pdf = Math.max(0, b.docsTotal - b.docsFr);
      row.savant += savant;
      row.machine += machine;
      row.pdf += pdf;
      if (b.docsTotal > 0 && savant >= b.docsTotal) row.completeBooks += 1;
    }
    return [...map.entries()]
      .map(([id, r]) => ({ id, ...r, total: r.savant + r.machine + r.pdf }))
      .filter((r) => r.total > 0)
      .sort((a, b) => b.total - a.total || b.savant - a.savant);
  }, [data]);

  const completeBooks = useMemo(
    () =>
      (data.books as BookSummary[])
        .filter((b) => b.downloaded && b.docsTotal > 0 && b.docsSavant >= b.docsTotal)
        .sort((a, b) => a.order - b.order),
    [data],
  );

  const levelById = useMemo(
    () => Object.fromEntries(data.levels.map((l) => [l.id, l])),
    [data],
  );

  const savantPct = pct(tiers.savant, tiers.total);

  return (
    <section
      id="etat-traductions"
      aria-labelledby="titre-etat-traductions"
      className="mx-auto max-w-7xl scroll-mt-20 px-4 pt-10 sm:px-6 lg:px-8"
    >
      <div className="rounded-3xl border border-amber-800/15 bg-card/70 p-5 shadow-sm backdrop-blur-sm sm:p-8">
        <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <Badge
              variant="outline"
              className="mb-3 gap-1.5 rounded-full border-amber-800/25 bg-amber-100/60 px-3 py-1 text-[11px] font-medium uppercase tracking-[0.14em] text-amber-900 dark:border-amber-200/20 dark:bg-amber-900/30 dark:text-amber-100"
            >
              <Layers className="size-3.5" aria-hidden="true" />
              État des traductions
            </Badge>
            <h2
              id="titre-etat-traductions"
              className="font-serif text-2xl font-semibold text-amber-950 sm:text-3xl dark:text-amber-50"
            >
              Où en est le chantier&nbsp;?
            </h2>
            <p className="mt-2 max-w-2xl text-sm leading-relaxed text-muted-foreground">
              Chaque leçon traverse trois états&nbsp;: d&apos;abord l&apos;extraction du texte
              arabe (PDF officiel ou CMS), puis une traduction machine de brouillon, enfin la{" "}
              <strong className="font-semibold text-foreground">
                traduction savante vérifiée
              </strong>{" "}
              — versets et hadiths contrôlés à la source, terminologie normée, structure
              pédagogique restituée.
            </p>
          </div>
          <div className="shrink-0 text-right">
            <p className="font-serif text-4xl font-semibold text-amber-950 sm:text-5xl dark:text-amber-50">
              {savantPct}&nbsp;%
            </p>
            <p className="mt-1 text-xs text-muted-foreground">
              du corpus en qualité savante
            </p>
          </div>
        </div>

        {/* Barre empilée globale */}
        <div className="mt-7">
          <StackedBar
            savant={tiers.savant}
            machine={tiers.machine}
            pdf={tiers.pdf}
            height="h-4"
            showTicks
            total={tiers.total}
          />
          <dl className="mt-3.5 grid grid-cols-1 gap-x-6 gap-y-2 text-xs sm:grid-cols-3">
            <div className="flex items-start gap-2">
              <LegendDot className="mt-1 bg-gradient-to-br from-amber-600 to-orange-700" />
              <div>
                <dt className="font-semibold text-amber-950 dark:text-amber-50">
                  {fr(tiers.savant)} documents savants
                </dt>
                <dd className="text-muted-foreground">
                  {pct(tiers.savant, tiers.total)}&nbsp;% — vérifiés versets par versets
                </dd>
              </div>
            </div>
            <div className="flex items-start gap-2">
              <LegendDot className="mt-1 bg-amber-300 dark:bg-amber-400/70" />
              <div>
                <dt className="font-semibold text-amber-950 dark:text-amber-50">
                  {fr(tiers.machine)} brouillons machine
                </dt>
                <dd className="text-muted-foreground">
                  {pct(tiers.machine, tiers.total)}&nbsp;% — à relire et hisser en savant
                </dd>
              </div>
            </div>
            <div className="flex items-start gap-2">
              <LegendDot className="mt-1 bg-stone-300 dark:bg-stone-600" />
              <div>
                <dt className="font-semibold text-amber-950 dark:text-amber-50">
                  {fr(tiers.pdf)} documents en PDF seul
                </dt>
                <dd className="text-muted-foreground">
                  {pct(tiers.pdf, tiers.total)}&nbsp;% — texte arabe à extraire (OCR)
                </dd>
              </div>
            </div>
          </dl>
        </div>

        {/* Métriques clés */}
        <div className="mt-7 grid grid-cols-2 gap-3 sm:gap-4 lg:grid-cols-4">
          <div className="rounded-2xl border border-amber-700/25 bg-gradient-to-br from-amber-100/70 to-yellow-50/50 p-4 dark:border-amber-400/20 dark:from-amber-900/40 dark:to-amber-800/20">
            <div className="flex items-center gap-2 text-[11px] font-medium uppercase tracking-[0.12em] text-amber-800 dark:text-amber-200">
              <BookOpenCheck className="size-4" aria-hidden="true" />
              Livres complets
            </div>
            <p className="mt-2 font-serif text-3xl font-semibold text-amber-950 dark:text-amber-50">
              {completeBooks.length}
              <span className="ms-1 text-sm font-normal text-muted-foreground">
                / {stats.booksTotal}
              </span>
            </p>
            <p className="mt-1 text-[11px] leading-snug text-muted-foreground">
              chaque leçon traduite en qualité savante
            </p>
          </div>
          <div className="rounded-2xl border border-amber-800/15 bg-card/80 p-4">
            <div className="flex items-center gap-2 text-[11px] font-medium uppercase tracking-[0.12em] text-muted-foreground">
              <Award className="size-4 text-primary" aria-hidden="true" />
              Traductions savantes
            </div>
            <p className="mt-2 font-serif text-3xl font-semibold text-amber-950 dark:text-amber-50">
              {fr(tiers.savant)}
            </p>
            <p className="mt-1 text-[11px] leading-snug text-muted-foreground">
              documents vérifiés au registre des traducteurs
            </p>
          </div>
          <div className="rounded-2xl border border-amber-800/15 bg-card/80 p-4">
            <div className="flex items-center gap-2 text-[11px] font-medium uppercase tracking-[0.12em] text-muted-foreground">
              <Loader2 className="size-4 text-amber-600 dark:text-amber-400" aria-hidden="true" />
              Reliques à hisser
            </div>
            <p className="mt-2 font-serif text-3xl font-semibold text-amber-950 dark:text-amber-50">
              {fr(tiers.machine)}
            </p>
            <p className="mt-1 text-[11px] leading-snug text-muted-foreground">
              brouillons machine en attente de relecture savante
            </p>
          </div>
          <div className="rounded-2xl border border-amber-800/15 bg-card/80 p-4">
            <div className="flex items-center gap-2 text-[11px] font-medium uppercase tracking-[0.12em] text-muted-foreground">
              <ScanText className="size-4 text-stone-500 dark:text-stone-300" aria-hidden="true" />
              PDF à extraire
            </div>
            <p className="mt-2 font-serif text-3xl font-semibold text-amber-950 dark:text-amber-50">
              {fr(tiers.pdf)}
            </p>
            <p className="mt-1 text-[11px] leading-snug text-muted-foreground">
              leçons dont le texte n&apos;existe qu&apos;en image PDF
            </p>
          </div>
        </div>

        {/* Avancement par matière */}
        <div className="mt-8">
          <h3 className="font-serif text-lg font-semibold text-amber-950 dark:text-amber-50">
            Avancement par matière
          </h3>
          <ul className="mt-4 space-y-3">
            {subjects.map((s, i) => {
              const savantP = pct(s.savant, s.total);
              return (
                <motion.li
                  key={s.id}
                  initial={{ opacity: 0, x: -8 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true, margin: "-30px" }}
                  transition={{ duration: 0.3, delay: Math.min(i, 6) * 0.04 }}
                  className="rounded-2xl border border-amber-800/10 bg-background/50 p-3.5 transition hover:border-amber-800/25 sm:p-4"
                >
                  <div className="flex items-center gap-3">
                    <SubjectTile subjectId={s.id} className="size-9" iconClassName="size-4" />
                    <div className="min-w-0 flex-1">
                      <div className="flex flex-wrap items-baseline justify-between gap-x-3 gap-y-0.5">
                        <p className="truncate font-serif text-[15px] font-semibold text-amber-950 dark:text-amber-50">
                          {s.titleFr}
                          <span
                            lang="ar"
                            dir="rtl"
                            className="ms-2 font-arabic text-sm font-normal text-muted-foreground"
                          >
                            {s.labelAr}
                          </span>
                        </p>
                        <p className="shrink-0 text-xs text-muted-foreground">
                          <strong className="font-semibold text-foreground">{fr(s.savant)}</strong>
                          <span className="mx-1 text-muted-foreground/60">/</span>
                          {fr(s.total)} documents
                          <span className="ms-2 font-medium text-primary">{savantP}&nbsp;%</span>
                        </p>
                      </div>
                      <div className="mt-2">
                        <StackedBar savant={s.savant} machine={s.machine} pdf={s.pdf} height="h-2" />
                      </div>
                      <p className="mt-1.5 flex flex-wrap items-center gap-x-3 gap-y-0.5 text-[11px] text-muted-foreground">
                        {s.completeBooks > 0 ? (
                          <span className="inline-flex items-center gap-1 font-medium text-amber-800 dark:text-amber-300">
                            <Award className="size-3" aria-hidden="true" />
                            {s.completeBooks} livre{s.completeBooks > 1 ? "s" : ""} complet
                            {s.completeBooks > 1 ? "s" : ""}
                          </span>
                        ) : (
                          <span>aucun livre complet pour l&apos;instant</span>
                        )}
                        {s.machine > 0 && (
                          <span className="inline-flex items-center gap-1">
                            <LegendDot className="bg-amber-300 dark:bg-amber-400/70" />
                            {fr(s.machine)} brouillon{s.machine > 1 ? "s" : ""}
                          </span>
                        )}
                        {s.pdf > 0 && (
                          <span className="inline-flex items-center gap-1">
                            <LegendDot className="bg-stone-300 dark:bg-stone-600" />
                            {fr(s.pdf)} PDF
                          </span>
                        )}
                      </p>
                    </div>
                  </div>
                </motion.li>
              );
            })}
          </ul>
        </div>

        {/* Livres complets */}
        <div className="mt-8">
          <h3 className="font-serif text-lg font-semibold text-amber-950 dark:text-amber-50">
            Les {completeBooks.length} livres achevés{" "}
            <span className="font-normal text-muted-foreground">
              — chaque leçon en traduction savante
            </span>
          </h3>
          <ul className="mt-4 flex flex-wrap gap-2">
            {completeBooks.map((b) => {
              const level = levelById[b.level];
              return (
                <li key={b.id}>
                  <button
                    type="button"
                    onClick={() => navigate(`/livre/${b.id}`)}
                    title={`Ouvrir ${b.titleFr} — ${fr(b.docsTotal)} documents savants`}
                    className="group inline-flex min-h-9 items-center gap-2 rounded-full border border-amber-600/30 bg-gradient-to-br from-amber-100/80 to-yellow-50/60 px-3.5 py-1.5 text-xs font-medium text-amber-900 shadow-sm transition hover:-translate-y-0.5 hover:border-amber-700/45 hover:shadow-md focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary dark:border-amber-400/25 dark:from-amber-900/50 dark:to-amber-800/30 dark:text-amber-100"
                  >
                    <Award className="size-3.5 text-amber-700 dark:text-amber-300" aria-hidden="true" />
                    <span className="font-serif font-semibold">{b.titleFr}</span>
                    <span className="text-[10px] uppercase tracking-wide text-amber-700/70 dark:text-amber-300/70">
                      {level?.shortFr ?? b.level} · {fr(b.docsTotal)} doc
                    </span>
                  </button>
                </li>
              );
            })}
          </ul>
        </div>

        {/* Reste à faire */}
        <div className="mt-8 rounded-2xl border border-dashed border-amber-800/25 bg-amber-100/40 p-4 sm:p-5 dark:border-amber-400/20 dark:bg-amber-900/20">
          <div className="flex items-start gap-3">
            <FileWarning className="mt-0.5 size-5 shrink-0 text-amber-700 dark:text-amber-300" aria-hidden="true" />
            <div className="min-w-0">
              <p className="font-serif text-[15px] font-semibold text-amber-950 dark:text-amber-50">
                Le chemin qui reste
              </p>
              <p className="mt-1.5 text-sm leading-relaxed text-amber-900/85 dark:text-amber-100/85">
                Pour couvrir l&apos;intégralité du programme, il reste{" "}
                <strong className="font-semibold">
                  {fr(tiers.machine)} brouillons machine
                </strong>{" "}
                à hisser en traduction savante (relecture des versets, hadiths et
                terminologie), puis{" "}
                <strong className="font-semibold">{fr(tiers.pdf)} documents</strong> dont le
                texte arabe n&apos;existe qu&apos;en PDF — extraction OCR image par image,
                puis traduction savante. Les leçons concernées restent d&apos;ores et déjà
                consultables dans leur manuel officiel d&apos;origine.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
