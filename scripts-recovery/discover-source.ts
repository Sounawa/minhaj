/**
 * Minhāj — Découverte de la source officielle du corpus Taʿlīm ʿatīq.
 *
 * Contexte (session R0) : le sandbox a été réinitialisé ; le réseau direct est
 * filtré (habous.gov.ma et archive.org inaccessibles). Le SDK z-ai-web-dev-sdk
 * exécute web_search / web_reader À DISTANCE — c'est la voie de re-téléchargement.
 * Le SDK est actuellement en 429 (rate-limit amont) : ce script retente avec
 * backoff et enregistre ses trouvailles dans content/source-report.json.
 *
 * Usage: bun run scripts-recovery/discover-source.ts [nombreEssais]
 */
import ZAI from "z-ai-web-dev-sdk";
import { existsSync, writeFileSync, readFileSync } from "fs";
import path from "path";

const OUT = path.join(process.cwd(), "content", "source-report.json");
const MAX_TRIES = parseInt(process.argv[2] || "3", 10);

interface Finding {
  query: string;
  url: string;
  name: string;
  snippet: string;
}

const QUERIES = [
  "المنهاج النموذجي للتعليم العتيق وزارة الأوقاف والشؤون الإسلامية",
  "كتاب التوحيد السنة الأولى ابتدائي عتيق تحميل site:habous.gov.ma",
  "كتب التعليم العتيق المغرب download منهج نموذجي",
  "الدرر اللوامع في تجويد كلام الله السنة الأولى عتيق",
  "تعليم عتيق منهاج الكتب الرسمية وزارة الأوقاف المغرب",
];

function sleep(ms: number) {
  return new Promise((r) => setTimeout(r, ms));
}

async function main() {
  const zai = await ZAI.create();
  const findings: Finding[] = [];
  let ok = 0;

  for (const q of QUERIES) {
    let done = false;
    for (let attempt = 1; attempt <= MAX_TRIES && !done; attempt++) {
      try {
        const res = await zai.functions.invoke("web_search", { query: q, num: 10 });
        const items = Array.isArray(res) ? res : ((res as any)?.results ?? []);
        for (const r of items) {
          findings.push({
            query: q,
            url: (r as any).url ?? "",
            name: (r as any).name ?? "",
            snippet: ((r as any).snippet ?? "").slice(0, 300),
          });
        }
        console.log(`✓ « ${q} » → ${items.length} résultats`);
        ok++;
        done = true;
      } catch (e: any) {
        const msg = String(e?.message ?? e);
        console.log(`… tentative ${attempt}/${MAX_TRIES} pour « ${q} » : ${msg.slice(0, 120)}`);
        if (msg.includes("429")) {
          await sleep(60_000 * attempt); // backoff 1 min, 2 min, 3 min…
        } else {
          done = true;
        }
      }
    }
  }

  const report = {
    generatedAt: new Date().toISOString(),
    sdkOk: ok > 0,
    queriesOk: ok,
    findings,
  };
  writeFileSync(OUT, JSON.stringify(report, null, 2) + "\n", "utf-8");
  console.log("─".repeat(60));
  console.log(`✅ Rapport écrit : content/source-report.json (${findings.length} résultats, ${ok}/${QUERIES.length} requêtes OK)`);
  if (ok === 0) {
    console.log("   SDK toujours en 429 — relancer plus tard (le script sauvegarde l'état).");
    process.exit(2);
  }
}

void main();
