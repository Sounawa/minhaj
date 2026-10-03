/**
 * Minhāj — Remplissage des lacunes : pour chaque préfixe (matière/niveau) du
 * programme, construit l'URL de la page de catégorie Joomla et la télécharge
 * (avec pagination ?start=N) pour y découvrir les leçons manquantes.
 *
 * Usage: bun run scripts-recovery/gap-fill.ts
 */
import { mkdirSync, existsSync, writeFileSync, readFileSync, statSync, readdirSync } from "fs";
import { createHash } from "crypto";
import path from "path";

const RAW = "/home/z/tr-src/raw";
const SEEN_DB = path.join(RAW, "index.json");
mkdirSync(RAW, { recursive: true });

const PROGRAM = "برنامج-التعليم-العتيق-الرئيسية";
const BOOKS = "الكتب-المدرسية";
const PROXY = "https://www-habous-gov-ma.translate.goog/";
const QS = "?_x_tr_sl=ar&_x_tr_tl=fr&_x_tr_hl=fr";
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36";

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

let seen: Record<string, string> = JSON.parse(readFileSync(SEEN_DB, "utf-8"));

/** Page d'un doc = son id numérique ; page de catégorie = "cat:<path>". */
function catKeyFor(p: string, query = "") { return "cat:" + p + query; }

async function fetchUrl(url: string, dest: string): Promise<string | null> {
  if (existsSync(dest) && statSync(dest).size > 2000) return readFileSync(dest, "utf-8");
  for (let attempt = 1; attempt <= 4; attempt++) {
    try {
      const res = await fetch(url, { headers: { "User-Agent": UA, "Accept-Language": "ar,fr;q=0.8" } });
      if (res.status === 429 || res.status === 503) { await sleep(20000 * attempt); continue; }
      if (!res.ok) throw new Error("HTTP " + res.status);
      const html = await res.text();
      if (html.length < 1500) throw new Error("court");
      writeFileSync(dest, html, "utf-8");
      return html;
    } catch (e) {
      if (attempt === 4) { console.log(`  ✗ ${decodeURIComponent(url).slice(60, 130)} (${(e as Error).message})`); return null; }
      await sleep(5000 * attempt);
    }
  }
  return null;
}

function extractDocLinks(html: string): { docId: string; pathAr: string; url: string }[] {
  const out: { docId: string; pathAr: string; url: string }[] = [];
  const re = /href="(https:\/\/www-habous-gov-ma\.translate\.goog\/([^"?#]+)(?:\?[^"]*)?)"/g;
  for (const m of html.matchAll(re)) {
    let p: string;
    try { p = decodeURIComponent(m[2]); } catch { continue; }
    const segs = p.split("/").filter(Boolean);
    if (!segs.length || (segs[0] !== PROGRAM && segs[0] !== BOOKS)) continue;
    const last = segs[segs.length - 1];
    const mm = last.match(/^(\d{3,6})-.+\.html$/);
    if (!mm) continue;
    out.push({ docId: mm[1], pathAr: p, url: m[1].replace(/&amp;/g, "&") });
  }
  return out;
}

// ————————————————————————————————— 1. Préfixes distincts
const prefixes = new Map<string, string>(); // pathAr → encodedPath
for (const [k, p] of Object.entries(seen)) {
  if (k === "main") continue;
  const segs = p.split("/");
  for (let i = 1; i < segs.length - 1; i++) {
    const prefix = segs.slice(0, i + 1).join("/");
    if (!prefixes.has(prefix)) {
      prefixes.set(prefix, segs.slice(0, i + 1).map(encodeURIComponent).join("/"));
    }
  }
}
// aussi depuis les fichiers cat
for (const f of readdirSync(RAW)) {
  if (!f.startsWith("cat-") || !f.endsWith(".html")) continue;
  const html = readFileSync(path.join(RAW, f), "utf-8");
  const m = html.match(/wbinfo\.capture_url = "([^"]+)"/);
  if (m) {
    const u = new URL(m[1].replace(/&amp;/g, "&"));
    const p = decodeURIComponent(u.pathname.replace(/^\//, ""));
    if ((p.split("/")[0] === PROGRAM || p.split("/")[0] === BOOKS) && !prefixes.has(p)) {
      prefixes.set(p, u.pathname.replace(/^\//, ""));
    }
  }
}

console.log(`Préfixes de catégorie candidats : ${prefixes.size}`);

// ————————————————————————————————— 2. Télécharger les pages de catégorie (+pagination)
let newDocs = 0;
let newCats = 0;
const found: Record<string, string> = {};

for (const [prefixPath, encPrefix] of prefixes) {
  const ck = catKeyFor(prefixPath);
  const dest = path.join(RAW, "cat-" + createHash("sha1").update(ck).digest("hex").slice(0, 20) + ".html");
  const url = PROXY + encPrefix + QS;
  const html = await fetchUrl(url, dest);
  if (!html) continue;
  if (!seen[ck]) { seen[ck] = prefixPath; newCats++; }
  for (const l of extractDocLinks(html)) {
    if (!seen[l.docId] && !found[l.docId]) { found[l.docId] = l.pathAr; newDocs++; }
  }
  // Pagination Joomla : ?start=N
  const pagin = new Set<number>();
  for (const m of html.matchAll(/[?&]start=(\d{1,4})/g)) pagin.add(parseInt(m[1], 10));
  for (const start of pagin) {
    const ck2 = catKeyFor(prefixPath, `?start=${start}`);
    const dest2 = path.join(RAW, "cat-" + createHash("sha1").update(ck2).digest("hex").slice(0, 20) + ".html");
    const html2 = await fetchUrl(PROXY + encPrefix + `?start=${start}` + QS.replace("?", "&"), dest2);
    if (!html2) continue;
    if (!seen[ck2]) { seen[ck2] = prefixPath + `?start=${start}`; newCats++; }
    for (const l of extractDocLinks(html2)) {
      if (!seen[l.docId] && !found[l.docId]) { found[l.docId] = l.pathAr; newDocs++; }
    }
    await sleep(300);
  }
  await sleep(250);
  if (newDocs > 0 && newDocs % 50 < 5) console.log(`  … ${newDocs} nouveaux docs, ${newCats} cats`);
}

writeFileSync(SEEN_DB, JSON.stringify(seen, null, 1), "utf-8");
const foundPath = path.join(RAW, "gap-found.json");
writeFileSync(foundPath, JSON.stringify(found, null, 1), "utf-8");
console.log(`\n✅ Catégories: ${newCats} nouvelles. Docs nouveaux découverts: ${newDocs} → gap-found.json`);
if (newDocs > 0) {
  console.log(`   → relancer crawl.ts pour les télécharger.`);
}
