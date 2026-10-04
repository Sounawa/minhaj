/**
 * Minhāj — Récupération ciblée des leçons des 19 livres « intro-only ».
 *
 * Découverte R5 : les leçons de ces livres EXISTENT en HTML sur le site officiel,
 * mais sous des chemins que le BFS de R2 a ratés (pages catégorie spécifiques +
 * liens component/content/article). Ce script :
 *   1. télécharge la page catégorie de chaque livre cible (+ pagination ?start=),
 *   2. énumère les articles de leçons (SEF + component/content/article),
 *   3. télécharge chaque leçon dans /home/z/tr-src/raw2/{docId}.html.
 *
 * Usage: bun run scripts-recovery/fetch-missing.ts
 */
import { mkdirSync, existsSync, writeFileSync, readFileSync } from "fs";
import path from "path";

const RAW = "/home/z/tr-src/raw2";
mkdirSync(RAW, { recursive: true });

const PROXY = "https://www-habous-gov-ma.translate.goog/";
const QS = "?_x_tr_sl=ar&_x_tr_tl=fr&_x_tr_hl=fr";
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36";

/** Table : bookId → chemin de catégorie (segment 1541 = Waraqat, nouveau livre). */
const TARGETS: Record<string, string> = {
  "usul-qiyam-4ep": "برنامج-التعليم-العتيق-الرئيسية/1787-المرحلة-الأولى/أصول-القيم-في-القرآن-والسنة/أصول-القيم-في-القرآن-والسنة-للسنة-الرابعة-ابتدائي-عتيق",
  "usul-qiyam-5ep": "برنامج-التعليم-العتيق-الرئيسية/1788-المرحلة-الأولى/أصول-القيم-في-القرآن-والسنة/أصول-القيم-في-القرآن-والسنة-للسنة-الخامسة-ابتدائي-عتيق",
  "usul-qiyam-6ep": "برنامج-التعليم-العتيق-الرئيسية/1789-المرحلة-الأولى/أصول-القيم-في-القرآن-والسنة/أصول-القيم-في-القرآن-والسنة-للسنة-السادسة-ابتدائي-عتيق",
  "faraid-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1700-المرحلة-الأولى/الفرائِض/الفرائض-الثانوي-الثالث-عتيق",
  "taqtit-tanawi-2": "برنامج-التعليم-العتيق-الرئيسية/1709-المرحلة-الأولى/التوقيت/التوقيت-الثانية-ثانوي",
  "taqtit-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1761-المرحلة-الأولى/التوقيت/التوقيت-الثالثة-ثانوي",
  "fikr-islami-tanawi-1": "برنامج-التعليم-العتيق-الرئيسية/1763-المرحلة-الأولى/الفكر-الإسلامي/الفكر-الإسلامي-الثانوي-الأول",
  "fikr-islami-tanawi-2": "برنامج-التعليم-العتيق-الرئيسية/1785-المرحلة-الأولى/الفكر-الإسلامي/الفكر-الإسلامي-الفلسفة-الإسلامية-الثانوي-الثاني",
  "ulum-hadith-tanawi-1": "برنامج-التعليم-العتيق-الرئيسية/1727-المرحلة-الأولى/علوم-الحديث/علوم-الحديث-الأولى-ثانوي",
  "ulum-hadith-tanawi-2": "برنامج-التعليم-العتيق-الرئيسية/1670-المرحلة-الأولى/علوم-الحديث/علوم-الحديث-الثانوي-الثاني",
  "hadith-3es": "برنامج-التعليم-العتيق-الرئيسية/1607-المرحلة-الأولى/الحديث/الحديث-الإعدادي-الثالث",
  "hadith-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1608-المرحلة-الأولى/الحديث/الحديث-الثانوي-الثالث",
  "qiraat-tanawi-2": "برنامج-التعليم-العتيق-الرئيسية/1764-المرحلة-الأولى/القراءات/القراءات-الثانية-ثانوي-عتيق",
  "qiraat-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1765-المرحلة-الأولى/القراءات/القراءات-الثالثة-ثانوي-عتيق",
  "tajwid-3es": "برنامج-التعليم-العتيق-الرئيسية/1760-المرحلة-الأولى/التجويد/التجويد-الثالثة-إعدادي-عتيق",
  "tafsir-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1605-المرحلة-الأولى/التفسير/التفسير-الثانوي-الثالث",
  "usul-fiqh-tanawi-2": "برنامج-التعليم-العتيق-الرئيسية/1708-المرحلة-الأولى/أصول-الفقه/أصول-الفقه-الثانية-ثانوي-عتيق",
  "usul-fiqh-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1707-المرحلة-الأولى/أصول-الفقه/أصول-الفقه-الثالثة-ثانوي-عتيق",
  // Nouveau livre découvert en R5 : Waraqat (1re année secondaire) — absent du manifeste
  "usul-fiqh-tanawi-1": "برنامج-التعليم-العتيق-الرئيسية/1541-المرحلة-الأولى/أصول-الفقه",
};

interface Lesson { docId: string; url: string; pathAr: string; bookId: string; }

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

async function fetchWithRetry(url: string, tries = 4): Promise<string | null> {
  for (let a = 1; a <= tries; a++) {
    try {
      const res = await fetch(url, { headers: { "User-Agent": UA, "Accept-Language": "ar,fr;q=0.8,en;q=0.5" } });
      if (res.status === 429 || res.status === 503) {
        console.log(`    ⏳ HTTP ${res.status}, attente ${15 * a}s…`);
        await sleep(15000 * a);
        continue;
      }
      if (!res.ok) throw new Error("HTTP " + res.status);
      const html = await res.text();
      if (html.length < 1200) throw new Error("page trop courte: " + html.length);
      return html;
    } catch (e) {
      if (a === tries) { console.log(`    ✗ ${(e as Error).message}`); return null; }
      await sleep(4000 * a);
    }
  }
  return null;
}

function proxyUrl(pathAr: string, extra = ""): string {
  return PROXY + pathAr.split("/").map(encodeURIComponent).join("/") + QS + extra;
}

/** Extrait les articles (leçons) d'une page catégorie. */
function extractArticles(html: string, catPath: string, bookId: string): Lesson[] {
  const out: Lesson[] = [];
  const seen = new Set<string>();
  const catSegs = catPath.split("/").length;

  // 1) liens SEF du programme : .../1541-.../أصول-الفقه/11926-حكم-الاجتهاد-ومراتبه.html
  const reSef = /href="(https:\/\/www-habous-gov-ma\.translate\.goog\/([^"?#]+))(?:\?[^"]*)?"/g;
  for (const m of html.matchAll(reSef)) {
    let p: string;
    try { p = decodeURIComponent(m[2]); } catch { continue; }
    if (!p.startsWith("برنامج-التعليم-العتيق-الرئيسية/")) continue;
    const segs = p.split("/");
    const last = segs[segs.length - 1];
    if (!last.endsWith(".html")) continue;
    const mm = last.match(/^(\d{3,6})-.+\.html$/);
    if (!mm) continue;
    // l'article doit être DANS la catégorie (même préfixe de chemin)
    const parent = segs.slice(0, -1).join("/");
    if (!catPath.startsWith(parent) && !parent.startsWith(catPath)) continue;
    if (parent.split("/").length < catSegs - 1) continue;
    if (seen.has(mm[1])) continue;
    seen.add(mm[1]);
    out.push({ docId: mm[1], url: m[1] + QS, pathAr: p, bookId });
  }

  // 2) liens component/content/article/... (non-SEF, mêmes articles)
  const reComp = /href="(https:\/\/www-habous-gov-ma\.translate\.goog\/component\/content\/article\/([^"?#]+))(?:\?[^"]*)?"/g;
  for (const m of html.matchAll(reComp)) {
    let p: string;
    try { p = decodeURIComponent(m[2]); } catch { continue; }
    const segs = p.split("/");
    const last = segs[segs.length - 1];
    const mm = last.match(/^(\d{3,6})-.+\.html$/);
    if (!mm) continue;
    if (seen.has(mm[1])) continue;
    seen.add(mm[1]);
    out.push({ docId: mm[1], url: m[1] + QS, pathAr: "component/content/article/" + p, bookId });
  }
  return out;
}

/** Liens de pagination (?start=N) d'une page catégorie. */
function extractPagination(html: string, catPath: string): string[] {
  const out: string[] = [];
  for (const m of html.matchAll(/href="[^"]*[?&](?:start|limitstart)=(\d+)[^"]*"/g)) {
    out.push("&start=" + m[1]);
  }
  return [...new Set(out)];
}

// ─── Main ────────────────────────────────────────────────────────────────────
const lessons: Lesson[] = [];
const lessonSeen = new Set<string>();

console.log("═".repeat(72));
console.log("PHASE 1 — Pages catégories des livres cibles");
console.log("═".repeat(72));

for (const [bookId, catPath] of Object.entries(TARGETS)) {
  const catUrl = proxyUrl(catPath);
  console.log(`\n▸ ${bookId} — ${catPath.split("/").slice(1, 3).join("/")}`);
  const html = await fetchWithRetry(catUrl);
  if (!html) continue;
  // articles de la 1re page
  const arts = extractArticles(html, catPath, bookId);
  for (const a of arts) {
    if (!lessonSeen.has(a.docId)) { lessonSeen.add(a.docId); lessons.push(a); }
  }
  console.log(`   page 1 : ${arts.length} articles`);

  // pagination
  const pages = extractPagination(html, catPath).sort((a, b) => parseInt(a.slice(6)) - parseInt(b.slice(6)));
  for (const pg of pages) {
    const pgUrl = catUrl + pg;
    const pgHtml = await fetchWithRetry(pgUrl);
    if (!pgHtml) continue;
    const pgArts = extractArticles(pgHtml, catPath, bookId);
    for (const a of pgArts) {
      if (!lessonSeen.has(a.docId)) { lessonSeen.add(a.docId); lessons.push(a); }
    }
    console.log(`   ${pg.replace("&", "")} : ${pgArts.length} articles`);
    await sleep(400 + Math.random() * 300);
  }
  await sleep(400 + Math.random() * 300);
}

console.log(`\n═`.repeat(1));
console.log(`Total articles uniques découverts : ${lessons.length}`);
writeFileSync("/home/z/tr-src/raw2/lessons-index.json", JSON.stringify(lessons, null, 1));
console.log("Index → /home/z/tr-src/raw2/lessons-index.json");

// PHASE 2 : téléchargement des leçons
console.log("\n" + "═".repeat(72));
console.log("PHASE 2 — Téléchargement des leçons");
console.log("═".repeat(72));

let done = 0, cached = 0, failed = 0;
const queue = [...lessons];

async function worker(id: number) {
  for (;;) {
    const item = queue.shift();
    if (!item) return;
    const dest = path.join(RAW, item.docId + ".html");
    if (existsSync(dest) && readFileSync(dest, "utf-8").length > 1500) { cached++; continue; }
    const html = await fetchWithRetry(item.url);
    if (html) {
      writeFileSync(dest, html, "utf-8");
      done++;
    } else failed++;
    if ((done + cached + failed) % 25 === 0) {
      console.log(`  [w${id}] ${done + cached}/${lessons.length} téléchargées (${failed} échecs)`);
    }
    await sleep(300 + Math.random() * 400);
  }
}

await Promise.all(Array.from({ length: 4 }, (_, i) => worker(i + 1)));

console.log(`\n✅ Terminé : ${done} nouvelles leçons, ${cached} en cache, ${failed} échecs.`);
console.log(`   Total fichiers dans ${RAW} : ${lessons.length - failed} / ${lessons.length}`);
