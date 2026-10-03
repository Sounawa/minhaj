/**
 * Minhāj — Balayage complet des catégories du programme Taʿlīm ʿatīq.
 *
 * R5 : les leçons des livres « intro-only » existent en HTML, réparties dans des
 * pages catégorie (avec pagination ?start=N) que le BFS de R2 n'a pas suivies.
 * Ce script balaie TOUTES les catégories connues, énumère tous les articles,
 * et télécharge uniquement ceux qui manquent au corpus (852 docs).
 *
 * Usage: bun run scripts-recovery/sweep-categories.ts [limiteTelechargements]
 */
import { mkdirSync, existsSync, writeFileSync, readFileSync, readdirSync } from "fs";
import path from "path";

const RAW = "/home/z/tr-src/raw2";
mkdirSync(RAW, { recursive: true });

const PROXY = "https://www-habous-gov-ma.translate.goog/";
const QS = "?_x_tr_sl=ar&_x_tr_tl=fr&_x_tr_hl=fr";
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36";
const PROGRAM = "برنامج-التعليم-العتيق-الرئيسية";

const LIMIT_DL = parseInt(process.argv[2] || "1200", 10);

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

async function fetchWithRetry(url: string, tries = 4): Promise<string | null> {
  for (let a = 1; a <= tries; a++) {
    try {
      const res = await fetch(url, { headers: { "User-Agent": UA, "Accept-Language": "ar,fr;q=0.8,en;q=0.5" } });
      if (res.status === 429 || res.status === 503) {
        console.log(`    ⏳ ${res.status}, attente ${18 * a}s…`);
        await sleep(18000 * a);
        continue;
      }
      if (!res.ok) throw new Error("HTTP " + res.status);
      const html = await res.text();
      if (html.length < 1200) throw new Error("trop court: " + html.length);
      return html;
    } catch (e) {
      if (a === tries) { console.log(`    ✗ ${(e as Error).message} — ${url.slice(-60)}`); return null; }
      await sleep(5000 * a);
    }
  }
  return null;
}

function proxyUrl(p: string, extra = ""): string {
  return PROXY + p.split("/").map(encodeURIComponent).join("/") + QS + extra;
}

/** Articles d'une page : renvoie [docId, pathAr][] */
function extractArticles(html: string): Array<[string, string]> {
  const out = new Map<string, string>();
  for (const m of html.matchAll(/href="https:\/\/www-habous-gov-ma\.translate\.goog\/([^"?#]+)(?:\?[^"]*)?"/g)) {
    let p: string;
    try { p = decodeURIComponent(m[1]); } catch { continue; }
    if (!p.startsWith(PROGRAM + "/") && !p.startsWith("component/content/article/")) continue;
    const segs = p.replace("component/content/article/", "").split("/");
    const last = segs[segs.length - 1];
    const mm = last.match(/^(\d{3,6})-.+\.html$/);
    if (!mm) continue;
    if (!out.has(mm[1])) out.set(mm[1], p);
  }
  return [...out.entries()];
}

// ─── Corpus existant (docIds déjà traduits) ──────────────────────────────────
const corpusIds = new Set<string>();
{
  for (const f of readdirSync("content/books")) {
    const j = JSON.parse(readFileSync(path.join("content/books", f), "utf-8"));
    if (j.intro?.docId) corpusIds.add(String(j.intro.docId));
    for (const l of j.lessons || []) corpusIds.add(String(l.docId));
  }
}
console.log(`Corpus actuel : ${corpusIds.size} docIds connus.`);

// ─── File des catégories ─────────────────────────────────────────────────────
const catFile = "/home/z/tr-src/raw2/sweep-cats.json";
const doneCats = new Set<string>(existsSync(catFile) ? JSON.parse(readFileSync(catFile, "utf-8")) : []);
const catQueue: string[] = [];
const catSeen = new Set<string>(doneCats);

// Découvertes persistantes (fusion inter-passes)
const found = new Map<string, string>(); // docId -> pathAr
const FOUND_FILE = "/home/z/tr-src/raw2/sweep-found.json";
if (existsSync(FOUND_FILE)) {
  for (const [id, p] of JSON.parse(readFileSync(FOUND_FILE, "utf-8"))) found.set(id, p);
  console.log(`Index précédent chargé : ${found.size} articles (fusion).`);
}

function pushCat(c: string) {
  if (!c.startsWith(PROGRAM + "/")) return;
  if (c.endsWith(".html")) return; // pas une catégorie
  if (catSeen.has(c)) return;
  catSeen.add(c);
  catQueue.push(c);
}

// amorçage : 43 catégories du menu + celles de fetch-missing + sujets
for (const c of JSON.parse(readFileSync("/tmp/cats-from-menu.json", "utf-8"))) pushCat(c);
for (const c of [
  `${PROGRAM}/1541-المرحلة-الأولى/أصول-الفقه`,
  `${PROGRAM}/1553-المرحلة-الأولى/الحديث/ثانوي`,
  `${PROGRAM}/1538-المرحلة-الأولى/التفسير`,
  `${PROGRAM}/1614-المرحلة-الأولى/الرسم-والضبط`,
  `${PROGRAM}/1658-المرحلة-الأولى/علوم-القُرآن`,
  `${PROGRAM}/1661-المرحلة-الأولى/التجويد`,
  `${PROGRAM}/1702-المرحلة-الأولى/القراءات`,
  `${PROGRAM}/1660-المرحلة-الأولى/المنطق`,
  `${PROGRAM}/1618-المرحلة-الأولى/التوحيد`,
  `${PROGRAM}/1621-المرحلة-الأولى/السيرة-النبوية`,
  `${PROGRAM}/1545-المرحلة-الأولى/الفقه`,
  `${PROGRAM}/1548-المرحلة-الأولى/التفسير`,
  `${PROGRAM}/1549-المرحلة-الأولى/التفسير`,
  `${PROGRAM}/1552-المرحلة-الأولى/الحديث`,
  `${PROGRAM}/1600-المرحلة-الأولى/الفقه`,
  `${PROGRAM}/1603-المرحلة-الأولى/التفسير`,
  `${PROGRAM}/1605-المرحلة-الأولى/التفسير`,
  `${PROGRAM}/1606-المرحلة-الأولى/الحديث`,
  `${PROGRAM}/1607-المرحلة-الأولى/الحديث`,
  `${PROGRAM}/1608-المرحلة-الأولى/الحديث`,
]) pushCat(c);

console.log(`Catégories en file : ${catQueue.length}`);

let ci = 0;
for (const cat of [...catQueue]) {
  ci++;
  const url = proxyUrl(cat);
  console.log(`\n[${ci}/${catQueue.length}] ${cat.slice(46, 110)}`);
  let html = await fetchWithRetry(url);
  if (!html) continue;
  // articles de la page 1
  for (const [id, p] of extractArticles(html)) if (!found.has(id)) found.set(id, p);
  // pagination
  const starts = [...new Set([...html.matchAll(/[?&](?:start|limitstart)=(\d+)/g)].map(m => m[1]))]
    .map(Number).sort((a, b) => a - b);
  let prev = -1;
  for (const s of starts) {
    if (s === prev) continue; prev = s;
    const pgHtml = await fetchWithRetry(url + "&start=" + s);
    if (!pgHtml) continue;
    const before = found.size;
    for (const [id, p] of extractArticles(pgHtml)) if (!found.has(id)) found.set(id, p);
    console.log(`   start=${s} : ${found.size - before} nouveaux`);
    await sleep(350 + Math.random() * 300);
    // nouvelles catégories découvertes
    for (const [id, p] of extractArticles(pgHtml)) {
      const segs = p.split("/");
      const parent = segs.slice(0, -1).join("/");
      pushCat(parent);
    }
  }
  // catégories dérivées des articles de la page 1
  for (const [, p] of extractArticles(html)) {
    const segs = p.replace("component/content/article/", "").split("/");
    const parent = segs.slice(0, -1).join("/");
    pushCat(parent);
  }
  doneCats.add(cat);
  writeFileSync(catFile, JSON.stringify([...doneCats]), "utf-8");
  writeFileSync(FOUND_FILE, JSON.stringify([...found.entries()]));
  await sleep(350 + Math.random() * 300);
  if (catQueue.length > 400) { console.log("⚠️ trop de catégories, arrêt de la phase 1"); break; }
}

// file élargie pendant l'itération ?
while (catQueue.length > ci) {
  const cat = catQueue[ci]; ci++;
  console.log(`\n[+] ${cat.slice(46, 110)}`);
  const html = await fetchWithRetry(proxyUrl(cat));
  if (!html) { doneCats.add(cat); continue; }
  for (const [id, p] of extractArticles(html)) if (!found.has(id)) found.set(id, p);
  doneCats.add(cat);
  writeFileSync(catFile, JSON.stringify([...doneCats]), "utf-8");
  writeFileSync(FOUND_FILE, JSON.stringify([...found.entries()]));
  await sleep(350 + Math.random() * 300);
}

const missing = [...found.entries()].filter(([id]) => !corpusIds.has(id) && id !== "13981");
console.log(`\n═`.repeat(2));
console.log(`Articles découverts : ${found.size} | manquants au corpus : ${missing.length}`);
writeFileSync("/home/z/tr-src/raw2/sweep-found.json", JSON.stringify([...found.entries()], null, 1));

// ─── PHASE 2 : téléchargement des articles manquants ────────────────────────
console.log(`\nTéléchargement des ${missing.length} articles manquants (limite ${LIMIT_DL})…`);
let done = 0, failed = 0;
const queue = missing.slice(0, LIMIT_DL);

async function worker(id: number) {
  for (;;) {
    const item = queue.shift();
    if (!item) return;
    const [docId, pathAr] = item;
    const dest = path.join(RAW, docId + ".html");
    if (existsSync(dest) && readFileSync(dest, "utf-8").length > 1500) continue;
    const html = await fetchWithRetry(proxyUrl(pathAr.replace(/^component\/content\/article\//, "")));
    if (html) { writeFileSync(dest, html, "utf-8"); done++; } else failed++;
    if ((done + failed) % 25 === 0) console.log(`  [w${id}] ${done + failed}/${queue.length + done + failed} (${failed} échecs)`);
    await sleep(300 + Math.random() * 450);
  }
}

await Promise.all(Array.from({ length: 4 }, (_, i) => worker(i + 1)));
console.log(`\n✅ Balayage : ${found.size} articles découverts, ${missing.length} manquants, ${done} téléchargés, ${failed} échecs.`);
console.log(`   Catégories balayées : ${doneCats.size}`);
