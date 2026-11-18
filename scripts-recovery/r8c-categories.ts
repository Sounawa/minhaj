/**
 * Minhāj R8c — Moisson des leçons PDF-référence depuis les pages catégories
 * des livres intro-only (~26 livres). Dédoublonne contre les leçons existantes.
 *
 * Usage: bun run scripts-recovery/r8c-categories.ts
 */
import { readFileSync, writeFileSync, existsSync } from "fs";
import path from "path";

const BOOKS = path.join(process.cwd(), "content", "books");
const CATS = "/tmp/r8-cats";
const TRCACHE = "/tmp/r8-trcache.json";
import { mkdirSync } from "fs";
mkdirSync(CATS, { recursive: true });

// ———————————————————— Cibles (bookId → chemin catégorie sur habous.gov.ma)
const TARGETS: Record<string, string> = {
  "hadith-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1608-المرحلة-الأولى/الحديث/الحديث-الثانوي-الثالث",
  "usul-qiyam-4ep": "برنامج-التعليم-العتيق-الرئيسية/1787-المرحلة-الأولى/أصول-القيم-في-القرآن-والسنة/أصول-القيم-في-القرآن-والسنة-للسنة-الرابعة-ابتدائي",
  "fikr-islami-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1784-المرحلة-الأولى/الفكر-الإسلامي/الفكر-الإسلامي-التصوف-الإسلامي-الثانوي-الثالث",
  "usul-fiqh-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1707-المرحلة-الأولى/أصول-الفقه/أصول-الفقه-الثالثة-ثانوي-عتيق",
  "ulum-hadith-tanawi-1": "برنامج-التعليم-العتيق-الرئيسية/1727-المرحلة-الأولى/علوم-الحديث/علوم-الحديث-الأولى-ثانوي",
  "fikr-islami-tanawi-2": "برنامج-التعليم-العتيق-الرئيسية/1785-المرحلة-الأولى/الفكر-الإسلامي/الفكر-الإسلامي-الفلسفة-الإسلامية-الثانوي-الثاني",
  "usul-fiqh-tanawi-2": "برنامج-التعليم-العتيق-الرئيسية/1708-المرحلة-الأولى/أصول-الفقه/أصول-الفقه-الثانية-ثانوي-عتيق",
  "usul-qiyam-5ep": "برنامج-التعليم-العتيق-الرئيسية/1788-المرحلة-الأولى/أصول-القيم-في-القرآن-والسنة/أصول-القيم-في-القرآن-والسنة-للسنة-الخامسة-ابتدائي",
  "tafsir-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1605-المرحلة-الأولى/التفسير/التفسير-الثانوي-الثالث",
  "ulum-hadith-tanawi-2": "برنامج-التعليم-العتيق-الرئيسية/1670-المرحلة-الأولى/علوم-الحديث/علوم-الحديث-الثانوي-الثاني",
  "qiraat-tanawi-2": "برنامج-التعليم-العتيق-الرئيسية/1764-المرحلة-الأولى/القراءات/القراءات-الثانية-ثانوي-عتيق",
  "faraid-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1700-المرحلة-الأولى/الفرائِض/الفرائض-الثانوي-الثالث-عتيق",
  "taqtit-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1761-المرحلة-الأولى/التوقيت/التوقيت-الثالثة-ثانوي",
  "qiraat-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1765-المرحلة-الأولى/القراءات/القراءات-الثالثة-ثانوي-عتيق",
  "hadith-3es": "برنامج-التعليم-العتيق-الرئيسية/1607-المرحلة-الأولى/الحديث/الحديث-الإعدادي-الثالث",
  "fikr-islami-tanawi-1": "برنامج-التعليم-العتيق-الرئيسية/1763-المرحلة-الأولى/الفكر-الإسلامي/الفكر-الإسلامي-الثانوي-الأول",
  "tajwid-3es": "برنامج-التعليم-العتيق-الرئيسية/1760-المرحلة-الأولى/التجويد/التجويد-الثالثة-إعدادي-عتيق",
  "usul-qiyam-6ep": "برنامج-التعليم-العتيق-الرئيسية/1789-المرحلة-الأولى/أصول-القيم-في-القرآن-والسنة/أصول-القيم-في-القرآن-والسنة-للسنة-السادسة-ابتدائي",
  "taqtit-tanawi-2": "برنامج-التعليم-العتيق-الرئيسية/1709-المرحلة-الأولى/التوقيت/التوقيت-الثانية-ثانوي",
  "ulum-hadith-tanawi-3": "برنامج-التعليم-العتيق-الرئيسية/1706-المرحلة-الأولى/علوم-الحديث/علوم-الحديث-الثالثة-ثانوي-عتيق",
  "tafsir-2es": "برنامج-التعليم-العتيق-الرئيسية/1689-المرحلة-الأولى/التفسير/التفسير-الإعدادي-الثاني",
  "tafsir-3es": "برنامج-التعليم-العتيق-الرئيسية/1604-المرحلة-الأولى/التفسير/التفسير-الإعدادي-الثالث",
  "rasm-wa-dabt-5ep": "برنامج-التعليم-العتيق-الرئيسية/1667-المرحلة-الأولى/الرسم-والضبط/الرسم-والضبط-الخامس-ابتدائي",
  "rasm-wa-dabt-6ep": "برنامج-التعليم-العتيق-الرئيسية/1699-المرحلة-الأولى/الرسم-والضبط/الرسم-والضبط-السادسة-إبتدائي-عتيق",
  "hadith-6ep": "برنامج-التعليم-العتيق-الرئيسية/1606-المرحلة-الأولى/الحديث/الحديث-الابتدائي-السادس",
  "tafsir-5ep": "برنامج-التعليم-العتيق-الرئيسية/1538-المرحلة-الأولى/التفسير/التفسير-من-خلال-تفسير-الجلالين-للسنة-الخامسة-من-التعليم-الإبتدائي-العتيق-تفسير-الحزب-التاسع-وخمسين-من-القرآن-الكريم",
};

// ———————————————————— GT traduction (cache)
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));
const trCache: Record<string, string> = existsSync(TRCACHE) ? JSON.parse(readFileSync(TRCACHE, "utf-8")) : {};
async function gt(text: string): Promise<string> {
  const key = `ar>fr:${text}`;
  if (trCache[key] !== undefined) return trCache[key];
  const url = `https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=ar&tl=fr&dt=t&q=${encodeURIComponent(text)}`;
  for (let attempt = 1; attempt <= 6; attempt++) {
    try {
      const res = await fetch(url, { headers: { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36" } });
      if (res.status === 429 || res.status === 503) { await sleep(12000 + 4000 * attempt); continue; }
      if (!res.ok) throw new Error("HTTP " + res.status);
      const d = (await res.json()) as any;
      const out = (d[0] as any[]).map((s) => (s && s[0]) || "").join("");
      trCache[key] = out;
      return out;
    } catch (e) {
      if (attempt === 6) throw e;
      await sleep(2500 * attempt);
    }
  }
  return "";
}
async function gtTitles(titles: string[]): Promise<string[]> {
  const out: string[] = [];
  const B = 22;
  for (let i = 0; i < titles.length; i += B) {
    const batch = titles.slice(i, i + B);
    const joined = batch.join("\n");
    const res = await gt(joined);
    const lines = res.split("\n").map((l) => l.trim());
    if (lines.length === batch.length) out.push(...lines);
    else for (const t of batch) out.push((await gt(t)).replace(/\n+/g, " ").trim());
    await sleep(400);
  }
  return out;
}

// ———————————————————— Parsing
const stripTashkil = (s: string) => s.replace(/[\u064B-\u065F\u0670\u06D6-\u06ED]/g, "").replace(/ـ/g, "").replace(/\s+/g, " ").trim();
const SKIP = ["منهجية التأليف", "كيف أستعمل كتابي", "كفايات تدريس", "التوزيع الدوري", "التعريف بالمؤلف", "غلاف الكتاب", "إضاءات منهجية", "الدليل البيداغوجي", "دليل الأستاذ", "تقديم الكتاب", "كيفية استعمال"].map(stripTashkil);
const isBoilerplate = (t: string) => SKIP.some((s) => stripTashkil(t).includes(s) || s.includes(stripTashkil(t)));

function parsePdfAnchors(raw: string): { url: string; title: string }[] {
  const anchors = [...raw.matchAll(/<a\s[^>]*href="([^"]+\.pdf[^"]*)"[^>]*>([\s\S]*?)<\/a>/gi)];
  const seen = new Set<string>();
  const out: { url: string; title: string }[] = [];
  for (const a of anchors) {
    const url = a[1].replace(/&amp;/g, "&");
    const title = a[2].replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim();
    const p = decodeURIComponent(url).split("?")[0];
    if (seen.has(p) || title.length < 4) continue;
    seen.add(p);
    out.push({ url, title });
  }
  return out;
}
const originUrl = (u: string) => decodeURIComponent(u).replace("https://www-habous-gov-ma.translate.goog", "https://www.habous.gov.ma").split("?")[0];

// ———————————————————— MAIN
async function main() {
  const galleries: Record<string, { url: string; title: string }[]> = {};
  // 1. fetch catégories
  for (const [book, cat] of Object.entries(TARGETS)) {
    const file = path.join(CATS, book + ".html");
    if (existsSync(file)) {
      galleries[book] = parsePdfAnchors(readFileSync(file, "utf-8")).filter((p) => !isBoilerplate(p.title));
      console.log(`- ${book}: déjà là (${galleries[book].length} PDF)`);
      continue;
    }
    const url = `https://www-habous-gov-ma.translate.goog/${encodeURIComponent(cat).replace(/%2F/g, "/")}?_x_tr_sl=ar&_x_tr_tl=fr`;
    let ok = false;
    for (let a = 1; a <= 4 && !ok; a++) {
      try {
        const res = await fetch(url);
        const html = await res.text();
        if (res.status === 200 && html.length > 40000) {
          writeFileSync(file, html, "utf-8");
          const all = parsePdfAnchors(html);
          galleries[book] = all.filter((p) => !isBoilerplate(p.title));
          console.log(`✓ ${book}: ${all.length} ancres → ${galleries[book].length} leçons`);
          ok = true;
        } else {
          console.log(`△ ${book}: essai ${a} → ${res.status} ${html.length}B`);
          await sleep(3500 * a);
        }
      } catch (e) { console.log(`✗ ${book}: ${String(e).slice(0, 80)}`); await sleep(3000 * a); }
    }
    if (!ok) console.log(`✗✗ ${book}: abandonné`);
    await sleep(1100);
  }

  // 2. dédoublonner contre leçons existantes + traduire
  const jobs: { book: string; pdfs: { url: string; title: string }[] }[] = [];
  for (const [book, pdfs] of Object.entries(galleries)) {
    const j = JSON.parse(readFileSync(path.join(BOOKS, book + ".json"), "utf-8"));
    const existing = new Set<string>([
      ...((j.lessons || []) as any[]).map((l) => stripTashkil(l.titleAr || "")),
      j.intro ? stripTashkil(j.intro.titleAr || "") : "",
    ]);
    const fresh = pdfs.filter((p) => !existing.has(stripTashkil(p.title)));
    if (fresh.length) jobs.push({ book, pdfs: fresh });
    else console.log(`= ${book}: rien de neuf (tout déjà présent)`);
  }
  const total = jobs.reduce((s, j) => s + j.pdfs.length, 0);
  console.log(`\n— ${total} nouvelles leçons PDF à créer sur ${jobs.length} livres`);
  // traduction par lots globaux
  const allTitles = jobs.flatMap((j) => j.pdfs.map((p) => p.title));
  const allTrs = await gtTitles(allTitles);
  writeFileSync(TRCACHE, JSON.stringify(trCache), "utf-8");
  console.log(`— ${allTrs.length} titres traduits`);

  // 3. écrire les stubs
  let k = 0;
  for (const { book, pdfs } of jobs) {
    const p = path.join(BOOKS, book + ".json");
    const j = JSON.parse(readFileSync(p, "utf-8"));
    const stubs = pdfs.map((pdf) => {
      const tr = allTrs[k++] || pdf.title;
      return { docId: `pdf-${Date.now().toString(36)}-${k}`, titleAr: pdf.title, titleFr: tr, html: "", htmlFr: "", pdfUrl: originUrl(pdf.url), pdfOnly: true };
    });
    j.lessons = [...(j.lessons || []), ...stubs];
    writeFileSync(p, JSON.stringify(j, null, 1) + "\n");
    console.log(`+ ${book}: ${stubs.length} stubs (total leçons ${j.lessons.length})`);
  }
}
main().catch((e) => { console.error(e); process.exit(1); });
