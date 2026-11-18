import { NextResponse } from "next/server";
import { readFile } from "fs/promises";
import path from "path";
import { execSync } from "child_process";

export const dynamic = "force-dynamic";

const HOME = "/home/z/my-project";

interface PipelineState {
  ts: number;
  iso: string;
  version: string;
  startedAt?: string;
  cycles?: number;
  wakeCount?: number;
  workers?: { active: number; books: string[] };
  remainingDocs?: number | null;
  registry?: { hand: number; llm: number };
  portal?: { state: string; ts: string; detail?: string } | null;
  sourceHunt?: {
    ts: string;
    book: string | null;
    docId?: string;
    titleFr?: string;
    direct?: string;
    wayback?: string;
    detail?: string;
  } | null;
  lastAutoCommit?: { ts: string; subject: string } | null;
  lastPush?: { ts: string; ok: boolean } | null;
}

function safeExec(cmd: string): string | null {
  try {
    return execSync(cmd, { cwd: HOME, timeout: 5000, encoding: "utf-8" }).trim();
  } catch {
    return null;
  }
}

export async function GET() {
  try {
    const raw = await readFile(path.join(HOME, "tr-logs", "pipeline-status.json"), "utf-8");
    const state = JSON.parse(raw) as PipelineState;
    const ageSeconds = Math.max(0, Math.round(Date.now() / 1000 - (state.ts ?? 0)));
    const alive = ageSeconds < 180;

    // Derniers battements publics (le journal que le cron devait tenir).
    let recentTicks: string[] = [];
    try {
      const aliveRaw = await readFile(path.join(HOME, "tr-tmp", "cron-alive.log"), "utf-8");
      recentTicks = aliveRaw.split("\n").filter((l) => l.trim()).slice(-8);
    } catch {
      /* journal absent : champ vide */
    }

    const gitLine = safeExec("git log -1 --pretty=format:%h·%s·%ci") ?? null;

    return NextResponse.json(
      {
        alive,
        ageSeconds,
        version: state.version ?? "?",
        iso: state.iso ?? null,
        startedAt: state.startedAt ?? null,
        cycles: state.cycles ?? null,
        wakeCount: state.wakeCount ?? null,
        workers: state.workers ?? { active: 0, books: [] },
        remainingDocs: state.remainingDocs ?? null,
        registry: state.registry ?? null,
        portal: state.portal ?? null,
        sourceHunt: state.sourceHunt ?? null,
        lastAutoCommit: state.lastAutoCommit ?? null,
        lastPush: state.lastPush ?? null,
        recentTicks,
        git: gitLine
          ? {
              hash: gitLine.split("·")[0] ?? null,
              subject: (gitLine.split("·")[1] ?? "").slice(0, 160) || null,
              date: gitLine.split("·")[2] ?? null,
            }
          : null,
      },
      { headers: { "Cache-Control": "no-store" } },
    );
  } catch {
    return NextResponse.json(
      {
        alive: false,
        ageSeconds: null,
        version: null,
        reason:
          "pipeline-status.json illisible ou absent — le moteur autonome n'a jamais battu sur cette machine.",
        recentTicks: [],
      },
      { status: 200, headers: { "Cache-Control": "no-store" } },
    );
  }
}
