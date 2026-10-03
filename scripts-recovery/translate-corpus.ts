/**
 * Minhāj — Traduction française massive du corpus via l'API Google
 * (client dict-chrome-ex, preserve le HTML).
 *
 * Stratégie :
 *  - titres en batch multi-lignes (1 requête pour ~30 titres)
 *  - HTML par chunks ~1100 car. coupés aux frontières de balises
 *  - 5 workers parallèles, backoff sur 429
 *  - sauvegarde continue (reprise possible à tout moment)
 *
 * Usage: bun run scripts-recovery/translate-corpus.ts [livreId]
 */
import { readFileSync, writeFileSync, existsSync, readdirSync } from "fs";
import path from "path";

const BOOKS = path.join(process.cwd(), "content", "books");
const only = process.argv[2] || null;
const CHUNK = 1100;
const WORKERS = 5;

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

let reqCount = 0;
let last429 = 0;

async function translate(text: string, sl = "ar", tl = "fr"): Promise<string> {
  const url = `https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=${sl}&tl=${tl}&dt=t&q=${encodeURIComponent(text)}`;
  for (let attempt = 1; attempt <= 5; attempt++) {
    try {
      const res = await fetch(url, { headers: { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36" } });
      if (res.status === 429 || res.status === 503) {
        const wait = 15000 + Date.now() - last429;
        last429 = Date.now();
        await sleep(Math.min(wait, 60000));
        continue;
      }
      if (!res.ok) throw new Error("HTTP " + res.status);
      const d = (await res.json()) as any;
      reqCount++;
      return (d[0] as any[]).map((s) => (s && s[0]) || "").join("");
    } catch (e) {
      if (attempt === 5) throw e;
      await sleep(3000 * attempt);
    }
  }
  return "";
}

/** Découpe le HTML en chunks à la frontière des balises. */
function chunkHtml(html: string): string[] {
  const chunks: string[] = [];
  let i = 0;
  while (i < html.length) {
    if (html.length - i <= CHUNK + 200) { chunks.push(html.slice(i)); break; }
    // chercher la dernière frontière de balise avant CHUNK
    let cut = -1;
    const window = html.slice(i, i + CHUNK);
    for (let j = window.length - 1; j > 100; j--) {
      if (window[j] === ">" && window[j + 1] === "<") { cut = i + j + 1; break; }
    }
    if (cut === -1) {
      // chercher un espace avant CHUNK
      const sp = window.lastIndexOf(" ");
      cut = sp > 100 ? i + sp : i + CHUNK;
    }
    chunks.push(html.slice(i, cut));
    i = cut;
  }
  return chunks.filter((c) => c.trim().length > 0);
}

async function translateHtml(html: string): Promise<string> {
  const chunks = chunkHtml(html);
  const out: string[] = [];
  for (const c of chunks) {
    if (!/[؀-ۿ]/.test(c)) { out.push(c); continue; } // pas d'arabe → tel quel
    out.push(await translate(c));
  }
  return out.join("");
}

/** Traduit un batch de titres (séparés par \n, préservés par l'API). */
async function translateTitles(titles: string[]): Promise<string[]> {
  const out: string[] = [];
  const BATCH = 25;
  for (let i = 0; i < titles.length; i += BATCH) {
    const batch = titles.slice(i, i + BATCH);
    const joined = batch.join("\n");
    if (!/[؀-ۿ]/.test(joined)) { out.push(...batch); continue; }
    const res = await translate(joined);
    const lines = res.split("\n").map((l) => l.trim());
    if (lines.length === batch.length) out.push(...lines);
    else {
      // repli : titres un par un
      for (const t of batch) out.push((await translate(t)).replace(/\n+/g, " ").trim());
    }
  }
  return out;
}

// ———————————————————————————————————————— Orchestration

interface Lesson { docId: string; titleAr: string; titleFr?: string; html: string; htmlFr?: string; }
interface BookFile { id: string; titleAr: string; titleFr?: string; intro?: any; lessons: Lesson[]; }

const files = readdirSync(BOOKS).filter((f) => f.endsWith(".json")).map((f) => f.replace(".json", "")).filter((id) => !only || id === only);

interface Job { bookId: string; kind: "title" | "intro" | "lesson"; docId: string; }
const jobs: Job[] = [];
const books = new Map<string, BookFile>();

for (const id of files) {
  const b: BookFile = JSON.parse(readFileSync(path.join(BOOKS, id + ".json"), "utf-8"));
  books.set(id, b);
  if (!b.titleFr && b.titleAr) jobs.push({ bookId: id, kind: "title", docId: "" });
  if (b.intro && !b.intro.htmlFr && b.intro.html) jobs.push({ bookId: id, kind: "intro", docId: b.intro.docId });
  for (const l of b.lessons ?? []) {
    if (!l.htmlFr && l.html) jobs.push({ bookId: id, kind: "lesson", docId: l.docId });
  }
}

console.log(`Traduction : ${files.length} livres, ${jobs.length} documents à traduire.`);
const t0 = Date.now();
let done = 0;

function saveBook(id: string) {
  const b = books.get(id)!;
  writeFileSync(path.join(BOOKS, id + ".json"), JSON.stringify(b, null, 2) + "\n", "utf-8");
}

// Titres en premier (rapide, rend le site navigable immédiatement)
console.log("— Phase 1 : titres");
for (const id of files) {
  const b = books.get(id)!;
  const titles: string[] = [];
  const keys: Array<["book" | "intro" | number, string]> = [];
  if (!b.titleFr && b.titleAr) { titles.push(b.titleAr); keys.push(["book", ""]); }
  if (b.intro && !b.intro.titleFr && b.intro.titleAr) { titles.push(b.intro.titleAr); keys.push(["intro", ""]); }
  (b.lessons ?? []).forEach((l, i) => { if (!l.titleFr && l.titleAr) { titles.push(l.titleAr); keys.push([i, l.docId]); } });
  if (!titles.length) continue;
  const translated = await translateTitles(titles);
  keys.forEach(([slot], i) => {
    const t = (translated[i] || titles[i]).trim();
    if (slot === "book") b.titleFr = t;
    else if (slot === "intro") b.intro.titleFr = t;
    else b.lessons[slot as number].titleFr = t;
  });
  // recompter les jobs restants
  saveBook(id);
  done += titles.length;
  if (reqCount % 10 === 0) console.log(`  titres: ${done} traduits (${Math.round((Date.now() - t0) / 1000)}s, ${reqCount} req)`);
}
console.log(`  ✅ titres: ${done} (${reqCount} requêtes)`);

// Contenus (5 workers)
console.log("— Phase 2 : contenus");
const contentJobs: Job[] = jobs.filter((j) => j.kind === "intro" || j.kind === "lesson");
let ci = 0;
let saved = 0;

async function contentWorker(wid: number) {
  for (;;) {
    const job = contentJobs[ci++];
    if (!job) return;
    const b = books.get(job.bookId)!;
    try {
      if (job.kind === "intro") {
        b.intro.htmlFr = await translateHtml(b.intro.html);
        saveBook(job.bookId);
        done++; saved++;
        console.log(`[w${wid}] ✓ intro ${job.bookId} (${done}/${jobs.length})`);
      } else {
        const l = b.lessons.find((x) => x.docId === job.docId)!;
        l.htmlFr = await translateHtml(l.html);
        if (++saved % 5 === 0) saveBook(job.bookId);
        done++;
        if (done % 10 === 0) {
          const rate = done / ((Date.now() - t0) / 60000);
          console.log(`[w${wid}] ${done}/${jobs.length} docs (${rate.toFixed(1)} docs/min, ${reqCount} req)`);
        }
      }
    } catch (e) {
      console.log(`[w${wid}] ✗ ${job.bookId}/${job.docId}: ${(e as Error).message}`);
    }
    await sleep(150 + Math.random() * 250);
  }
}

await Promise.all(Array.from({ length: WORKERS }, (_, i) => contentWorker(i + 1)));
for (const id of files) saveBook(id);
console.log(`\n✅ Traduction terminée : ${done}/${jobs.length} docs, ${reqCount} requêtes, ${Math.round((Date.now() - t0) / 1000)}s`);
