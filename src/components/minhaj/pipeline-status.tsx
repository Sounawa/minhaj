"use client";

/**
 * PipelineStatus — le voyant public du moteur autonome (R457).
 *
 * Directive utilisateur R456/R457 : « le cron doit s'activer et AVANCER —
 * je veux le voir ». Ce composant rend l'autonomie VISIBLE sur chaque page :
 * un voyant battant (état du superviseur v4, rafraîchi toutes les 30 s),
 * dépliable en un relevé complet (workers, portail, chasse aux sources,
 * derniers battements, dernier commit poussé).
 */

import { useEffect, useState } from "react";
import { Activity, ChevronDown, RefreshCw } from "lucide-react";

interface PipelineData {
  alive: boolean;
  ageSeconds: number | null;
  version: string | null;
  iso: string | null;
  startedAt: string | null;
  cycles: number | null;
  wakeCount: number | null;
  workers: { active: number; books: string[] };
  remainingDocs: number | null;
  registry: { hand: number; llm: number } | null;
  portal: { state: string; ts: string; detail?: string } | null;
  sourceHunt: {
    ts: string;
    book: string | null;
    docId?: string;
    titleFr?: string;
    direct?: string;
    wayback?: string;
    collection?: string;
    detail?: string;
  } | null;
  lastAutoCommit: { ts: string; subject: string } | null;
  lastPush: { ts: string; ok: boolean } | null;
  recentTicks: string[];
  git: { hash: string | null; subject: string | null; date: string | null } | null;
  reason?: string;
}

function fmtAge(sec: number | null): string {
  if (sec === null) return "—";
  if (sec < 60) return `il y a ${sec} s`;
  if (sec < 3600) return `il y a ${Math.floor(sec / 60)} min`;
  return `il y a ${Math.floor(sec / 3600)} h`;
}

function portalLabel(state: string | undefined): string {
  switch (state) {
    case "OUVERTE":
      return "portail OUVERT — reprise du flux";
    case "FERMÉE":
      return "portail en maintenance";
    case "ERR":
      return "portail injoignable";
    default:
      return state ? `portail ${state.toLowerCase()}` : "portail non sondé";
  }
}

export function PipelineStatus() {
  const [data, setData] = useState<PipelineData | null>(null);
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    let cancelled = false;
    const load = () => {
      setLoading(true);
      fetch("/api/pipeline-status", { cache: "no-store" })
        .then((r) => (r.ok ? r.json() : null))
        .then((d: PipelineData | null) => {
          if (!cancelled) setData(d);
        })
        .catch(() => undefined)
        .finally(() => {
          if (!cancelled) setLoading(false);
        });
    };
    load();
    const id = setInterval(load, 30_000);
    return () => {
      cancelled = true;
      clearInterval(id);
    };
  }, []);

  const alive = data?.alive === true;
  const neverBeat = data !== null && data.alive === false && data.version === null;

  return (
    <details
      className="group/pipeline w-full"
      onToggle={(e) => setOpen((e.target as HTMLDetailsElement).open)}
    >
      <summary
        className="flex cursor-pointer list-none items-center gap-2 rounded-lg px-2 py-1.5 text-xs transition-colors hover:bg-amber-800/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary [&::-webkit-details-marker]:hidden"
        title="État du moteur de production autonome — cliquer pour le relevé complet"
      >
        <span className="relative flex size-2.5 shrink-0" aria-hidden="true">
          {alive ? (
            <>
              <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-500 opacity-60" />
              <span className="relative inline-flex size-2.5 rounded-full bg-emerald-600" />
            </>
          ) : (
            <span
              className={`relative inline-flex size-2.5 rounded-full ${
                neverBeat ? "bg-stone-400" : "bg-amber-500"
              }`}
            />
          )}
        </span>
        <span className="flex min-w-0 flex-wrap items-center gap-x-1.5 gap-y-0.5 text-muted-foreground">
          <span className="font-medium text-amber-950 dark:text-amber-50">
            Production autonome
          </span>
          <span aria-hidden="true">·</span>
          {data === null ? (
            <span>interrogation du moteur…</span>
          ) : neverBeat ? (
            <span>moteur jamais démarré sur cette machine</span>
          ) : alive ? (
            <span>
              moteur {data.version} actif — battement {fmtAge(data.ageSeconds)}
              {data.workers?.active ? `, ${data.workers.active} worker${data.workers.active > 1 ? "s" : ""} en cours` : ""}
            </span>
          ) : (
            <span>battement ancien ({fmtAge(data.ageSeconds)}) — reprise au réveil</span>
          )}
        </span>
        <ChevronDown
          className={`ml-auto size-3.5 shrink-0 text-muted-foreground transition-transform ${
            open ? "rotate-180" : ""
          }`}
          aria-hidden="true"
        />
      </summary>

      <div className="mt-2 rounded-lg border border-amber-800/15 bg-background/70 p-3 text-xs leading-relaxed text-muted-foreground">
        {data === null ? (
          <p className="flex items-center gap-2">
            <RefreshCw className="size-3.5 animate-spin" aria-hidden="true" />
            Lecture de l&apos;état du moteur…
          </p>
        ) : (
          <div className="grid gap-2 sm:grid-cols-2">
            <p className="flex items-start gap-2 sm:col-span-2">
              <Activity className="mt-0.5 size-3.5 shrink-0 text-primary" aria-hidden="true" />
              <span>
                Superviseur {data.version} démarré {data.startedAt ? `le ${data.startedAt.replace("T", " ").replace("Z", " UTC")}` : "—"}
                {data.cycles !== null ? ` · ${data.cycles.toLocaleString("fr-FR")} cycles` : ""}
                {data.wakeCount ? ` · ${data.wakeCount} réveil${data.wakeCount > 1 ? "s" : ""} après gel` : ""}
                {typeof data.remainingDocs === "number" && (
                  <>
                    {" "}· {data.remainingDocs.toLocaleString("fr-FR")} document
                    {data.remainingDocs > 1 ? "s" : ""} en file de traduction
                  </>
                )}
                {data.registry && (
                  <>
                    {" "}· registre {":"} {(data.registry.hand + data.registry.llm).toLocaleString("fr-FR")} (
                    {data.registry.llm.toLocaleString("fr-FR")} par le moteur)
                  </>
                )}
              </span>
            </p>
            <p>
              <span className="font-medium text-amber-950 dark:text-amber-50">Canari portail :</span>{" "}
              {data.portal ? `${portalLabel(data.portal.state)} — sondé ${fmtAge(Math.max(0, Math.round((Date.now() - Date.parse(data.portal.ts)) / 1000)))}` : "pas encore sondé"}
            </p>
            <p className="sm:col-span-2">
              <span className="font-medium text-amber-950 dark:text-amber-50">Chasse aux sources :</span>{" "}
              {data.sourceHunt?.book
                ? `${data.sourceHunt.book}/${data.sourceHunt.docId} — arbre ${data.sourceHunt.direct}, Wayback ${data.sourceHunt.wayback}${data.sourceHunt.collection ? `, miroir ${data.sourceHunt.collection.replace(/^collection:/, "")}` : ""}`
                : "aucune leçon vide à sonder"}
            </p>
            <p className="sm:col-span-2">
              <span className="font-medium text-amber-950 dark:text-amber-50">Dernier commit poussé :</span>{" "}
              {data.lastPush?.ok
                ? `${data.git?.hash ?? "—"} — ${(data.git?.subject ?? "").slice(0, 90)}`
                : "périodicité de 10 min — le prochain cycle pousse"}
            </p>
            {data.recentTicks.length > 0 && (
              <div className="sm:col-span-2">
                <p className="mb-1 font-medium text-amber-950 dark:text-amber-50">
                  Derniers battements (journal public) :
                </p>
                <ul className="max-h-36 space-y-0.5 overflow-y-auto rounded-md bg-secondary/50 p-2 font-mono text-[10px] leading-snug">
                  {data.recentTicks.map((t) => (
                    <li key={t} className="whitespace-pre-wrap break-all">
                      {t}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}
        {loading && (
          <span className="sr-only" role="status">
            Rechargement de l&apos;état du moteur autonome
          </span>
        )}
      </div>
    </details>
  );
}
