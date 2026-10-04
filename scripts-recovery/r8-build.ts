/**
 * Minhāj R8 — Intégration des 5 nouveaux livres + intros + leçons PDF-référence.
 *
 * Nouveaux livres  : hadith-5ep (10958), hadith-2es (10960), fiqh-5ep (11930),
 *                    fiqh-tanawi-2 (12177), fiqh-2es (12019)  → 63 livres.
 * Intros ajoutées  : 11505→fiqh-1es, 13014→hadith-1es, 12583→hadith-1ep,
 *                    13360→tafsir-1es, 12016→tafsir-4ep, 15373→ulum-quran-1es,
 *                    17502→tajwid-6ep (+ 14101/11509/13876/14170/18646 leçon→intro).
 * Chirurgie        : split fiqh-tanawi-1 → t2 ; merge fiqh-4ep → fiqh-1ep ;
 *                    retrait article d'actualité 20436 (ulum-hadith-tanawi-3).
 * Leçons PDF       : stubs titrés (hadith-5ep, hadith-2es, fiqh-3es).
 *
 * Usage: bun run scripts-recovery/r8-build.ts
 */
import { readFileSync, writeFileSync, existsSync, readdirSync, rmSync } from "fs";
import path from "path";

const PAGES = "/tmp/r8-pages";
const BOOKS = path.join(process.cwd(), "content", "books");
const MANIFEST = path.join(process.cwd(), "content", "manifest.json");
const TRCACHE = "/tmp/r8-trcache.json";

// ———————————————————————————————————— Traduction (Google dict API)

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));
const trCache: Record<string, string> = existsSync(TRCACHE) ? JSON.parse(readFileSync(TRCACHE, "utf-8")) : {};
let reqCount = 0;

async function gt(text: string, sl = "ar", tl = "fr"): Promise<string> {
  const key = `${sl}>${tl}:${text}`;
  if (trCache[key] !== undefined) return trCache[key];
  const url = `https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=${sl}&tl=${tl}&dt=t&q=${encodeURIComponent(text)}`;
  for (let attempt = 1; attempt <= 6; attempt++) {
    try {
      const res = await fetch(url, { headers: { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36" } });
      if (res.status === 429 || res.status === 503) { await sleep(12000 + 4000 * attempt); continue; }
      if (!res.ok) throw new Error("HTTP " + res.status);
      const d = (await res.json()) as any;
      const out = (d[0] as any[]).map((s) => (s && s[0]) || "").join("");
      reqCount++;
      trCache[key] = out;
      return out;
    } catch (e) {
      if (attempt === 6) throw e;
      await sleep(2500 * attempt);
    }
  }
  return "";
}

const CHUNK = 1100;
function chunkHtml(html: string): string[] {
  const chunks: string[] = [];
  let i = 0;
  while (i < html.length) {
    if (html.length - i <= CHUNK + 200) { chunks.push(html.slice(i)); break; }
    let cut = -1;
    const win = html.slice(i, i + CHUNK);
    for (let j = win.length - 1; j > 100; j--) if (win[j] === ">" && win[j + 1] === "<") { cut = i + j + 1; break; }
    if (cut === -1) { const sp = win.lastIndexOf(" "); cut = sp > 100 ? i + sp : i + CHUNK; }
    chunks.push(html.slice(i, cut));
    i = cut;
  }
  return chunks.filter((c) => c.trim().length > 0);
}
async function gtHtml(html: string): Promise<string> {
  const out: string[] = [];
  for (const c of chunkHtml(html)) {
    if (!/[؀-ۿ]/.test(c)) { out.push(c); continue; }
    out.push(await gt(c));
    await sleep(350);
  }
  return out.join("");
}
async function gtTitles(titles: string[]): Promise<string[]> {
  const out: string[] = [];
  const B = 22;
  for (let i = 0; i < titles.length; i += B) {
    const batch = titles.slice(i, i + B);
    const joined = batch.join("\n");
    if (!/[؀-ۿ]/.test(joined)) { out.push(...batch); continue; }
    const res = await gt(joined);
    const lines = res.split("\n").map((l) => l.trim());
    if (lines.length === batch.length) out.push(...lines);
    else for (const t of batch) out.push((await gt(t)).replace(/\n+/g, " ").trim());
    await sleep(400);
  }
  return out;
}

// ———————————————————————————————————— Parsing des pages proxées GT

function parseItemPage(raw: string): { titleAr: string; html: string } | null {
  const i = raw.indexOf('<div class="item-page"');
  if (i < 0) return null;
  let chunk = raw.slice(i);
  // borne de fin : module / article-info suivant ou fin du bloc
  const endM = chunk.search(/<div class="(?:module|blog|items-|clearfix item-page)/);
  if (endM > 200) chunk = chunk.slice(0, endM);
  const tm = chunk.match(/<h1[^>]*>([\s\S]*?)<\/h1>/) || chunk.match(/<h2[^>]*>([\s\S]*?)<\/h2>/);
  const titleAr = tm ? tm[1].replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim() : "";
  let html = chunk.replace(/<h1[^>]*>[\s\S]*?<\/h1>/, "").replace(/<h2[^>]*>[\s\S]*?<\/h2>/, "");
  html = html
    .replace(/<dl class="article-info">[\s\S]*?<\/dl>/, "")
    .replace(/<script[\s\S]*?<\/script>/gi, "").replace(/<style[\s\S]*?<\/style>/gi, "")
    .replace(/<form[\s\S]*?<\/form>/gi, "").replace(/<iframe[\s\S]*?<\/iframe>/gi, "")
    .replace(/<img[^>]*>/gi, "").replace(/<button[\s\S]*?<\/button>/gi, "").replace(/<input[^>]*>/gi, "")
    .replace(/<!--[\s\S]*?-->/g, "");
  html = html.replace(/\s(?:class|id|style|onclick|onload|data-[a-z-]+)="[^"]*"/gi, "");
  html = html.replace(/<a\s[^>]*href="[^"]*"[^>]*>([\s\S]*?)<\/a>/gi, "$1");
  html = html.replace(/\n{3,}/g, "\n\n").replace(/[ \t]{2,}/g, " ").trim();
  if (html.length < 60) return null;
  return { titleAr, html };
}

interface PdfLesson { url: string; title: string; }
function parsePdfAnchors(raw: string): PdfLesson[] {
  const anchors = [...raw.matchAll(/<a\s[^>]*href="([^"]+\.pdf[^"]*)"[^>]*>([\s\S]*?)<\/a>/gi)];
  const seen = new Set<string>();
  const out: PdfLesson[] = [];
  for (const a of anchors) {
    let url = a[1].replace(/&amp;/g, "&");
    const title = a[2].replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim();
    const path = decodeURIComponent(url).split("?")[0];
    if (seen.has(path) || title.length < 4) continue;
    seen.add(path);
    out.push({ url, title });
  }
  return out;
}

/** PDF officiel (origine) depuis l'URL proxée. */
function originUrl(proxied: string): string {
  return decodeURIComponent(proxied)
    .replace("https://www-habous-gov-ma.translate.goog", "https://www.habous.gov.ma")
    .split("?")[0];
}

const SKIP_PDF = ["منهجية التأليف", "كيف أستعمل كتابي", "كفايات تدريس", "التوزيع الدوري", "التعريف بالمؤلف"];
const isBoilerplate = (t: string) => SKIP_PDF.some((s) => t.includes(s));

// ———————————————————————————————————— Helpers corpus

const readBook = (id: string) => JSON.parse(readFileSync(path.join(BOOKS, id + ".json"), "utf-8"));
const writeBook = (j: any) => writeFileSync(path.join(BOOKS, j.id + ".json"), JSON.stringify(j, null, 1) + "\n", "utf-8");

// ———————————————————————————————————— MAIN

async function main() {
  // 1. Parse des pages
  const page: Record<string, { titleAr: string; html: string } | null> = {};
  for (const id of ["10958", "10960", "11930", "12019", "12177", "13014", "11505", "13360", "12583", "12016", "15373", "14101", "17502", "13876"]) {
    const f = path.join(PAGES, id + ".html");
    page[id] = existsSync(f) ? parseItemPage(readFileSync(f, "utf-8")) : null;
    console.log(`page ${id}: ${page[id] ? `« ${page[id].titleAr.slice(0, 60)} » (${page[id].html.length} car.)` : "✗"}`);
  }

  // 2. Leçons PDF (galeries)
  const galleries: Record<string, PdfLesson[]> = {};
  for (const id of ["10958", "10960", "13876"]) {
    const all = parsePdfAnchors(readFileSync(path.join(PAGES, id + ".html"), "utf-8"));
    galleries[id] = all.filter((p) => !isBoilerplate(p.title));
    console.log(`galerie ${id}: ${all.length} ancres → ${galleries[id].length} leçons retenues`);
  }

  // 3. Traductions
  console.log("\n— Traduction des titres de leçons PDF…");
  const trTitle: Record<string, string[]> = {};
  for (const [id, g] of Object.entries(galleries)) {
    trTitle[id] = await gtTitles(g.map((p) => p.title));
    console.log(`  ${id}: ${trTitle[id].length} titres traduits`);
  }

  console.log("— Traduction des intros (HTML)…");
  const trHtml: Record<string, string> = {};
  const trIntroTitle: Record<string, string> = {};
  for (const [id, p] of Object.entries(page)) {
    if (!p) continue;
    trIntroTitle[id] = (await gt(p.titleAr)).replace(/\n+/g, " ").trim();
    trHtml[id] = await gtHtml(p.html);
    console.log(`  ${id}: titre + html traduits (${trHtml[id].length} car.)`);
  }
  writeFileSync(TRCACHE, JSON.stringify(trCache), "utf-8");
  console.log(`(${reqCount} requêtes GT, cache: ${Object.keys(trCache).length})`);

  // 4. Nouveaux livres
  const mkLesson = (docId: string, titleAr: string, titleFr: string, url: string) => ({
    docId, titleAr, titleFr, html: "", htmlFr: "", pdfUrl: originUrl(url), pdfOnly: true,
  });

  const newBooks: any[] = [];
  // — hadith-5ep
  {
    const g = galleries["10958"], trs = trTitle["10958"];
    newBooks.push({
      id: "hadith-5ep", subject: "hadith", level: "5ep",
      subjectAr: "الحديث", levelAr: "الحديث-الخامس-ابتدائي-عتيق",
      titleAr: "الحديث من كتاب الأربعين النووية للإمام النووي بشرح ابن دقيق العيد للسنة الخامسة من التعليم الابتدائي العتيق",
      titleFr: "Ḥadīth — les Quarante hadiths d'al-Nawawī, comm. d'Ibn Daqīq al-ʿĪd (5ᵉ primaire)",
      pdfUrl: null,
      intro: { docId: "10958", titleAr: page["10958"]!.titleAr, titleFr: trIntroTitle["10958"], html: page["10958"]!.html, htmlFr: trHtml["10958"] },
      lessons: g.map((p, i) => mkLesson("pdf-" + (i + 1), p.title, trs[i] || p.title, p.url)),
    });
  }
  // — hadith-2es
  {
    const g = galleries["10960"], trs = trTitle["10960"];
    newBooks.push({
      id: "hadith-2es", subject: "hadith", level: "2es",
      subjectAr: "الحديث", levelAr: "الحديث-الثانية-إعدادي-عتيق",
      titleAr: "الحديث من موطأ الإمام مالك بشرح الزرقاني للسنة الثانية من التعليم الإعدادي العتيق",
      titleFr: "Ḥadīth — le Muwaṭṭaʾ de l'imam Mālik, comm. d'al-Zarqānī (2ᵉ collège)",
      pdfUrl: null,
      intro: { docId: "10960", titleAr: page["10960"]!.titleAr, titleFr: trIntroTitle["10960"], html: page["10960"]!.html, htmlFr: trHtml["10960"] },
      lessons: g.map((p, i) => mkLesson("pdf-" + (i + 1), p.title, trs[i] || p.title, p.url)),
    });
  }
  // — fiqh-5ep
  newBooks.push({
    id: "fiqh-5ep", subject: "fiqh", level: "5ep",
    subjectAr: "الفقه", levelAr: "الفقه-الخامس-ابتدائي-عتيق",
    titleAr: "الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة الفاسي للسنة الخامسة من التعليم الابتدائي العتيق",
    titleFr: "Fiqh — le Murshid al-Muʿīn d'Ibn ʿĀshir, comm. de Mayyāra al-Fāsī (5ᵉ primaire)",
    pdfUrl: null,
    intro: { docId: "11930", titleAr: page["11930"]!.titleAr, titleFr: trIntroTitle["11930"], html: page["11930"]!.html, htmlFr: trHtml["11930"] },
    lessons: [],
  });
  // — fiqh-2es
  newBooks.push({
    id: "fiqh-2es", subject: "fiqh", level: "2es",
    subjectAr: "الفقه", levelAr: "الفقه-الثانية-إعدادي-عتيق",
    titleAr: "الفقه من رسالة ابن أبي زيد القيرواني بشرح كفاية الطالب الرباني بحاشية العدوي للسنة الثانية من التعليم الإعدادي العتيق",
    titleFr: "Fiqh — la Risāla d'Ibn Abī Zayd, comm. al-Kifāya + ḥāshiya al-ʿAdawī (2ᵉ collège)",
    pdfUrl: null,
    intro: { docId: "12019", titleAr: page["12019"]!.titleAr, titleFr: trIntroTitle["12019"], html: page["12019"]!.html, htmlFr: trHtml["12019"] },
    lessons: [],
  });

  for (const b of newBooks) { writeBook(b); console.log(`+ livre ${b.id} (${b.lessons.length} leçons)`); }

  // 5. fiqh-tanawi-2 : intro 12177 + leçons déplacées de fiqh-tanawi-1
  {
    const t1 = readBook("fiqh-tanawi-1");
    const moved = t1.lessons.filter((l: any) => parseInt(l.docId, 10) >= 12230);
    const kept = t1.lessons.filter((l: any) => parseInt(l.docId, 10) < 12230 && String(l.docId) !== "12177" && String(l.docId) !== "11509");
    const intro12177 = t1.lessons.find((l: any) => String(l.docId) === "12177");
    const intro11509 = t1.lessons.find((l: any) => String(l.docId) === "11509");
    const t2 = {
      id: "fiqh-tanawi-2", subject: "fiqh", level: "tanawi-2",
      subjectAr: "الفقه", levelAr: "الفقه-الثانية-ثانوي-عتيق",
      titleAr: "الفقه من مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي للسنة الثانية من التعليم الثانوي العتيق",
      titleFr: "Fiqh — le Mukhtaṣar de Khalīl, comm. d'al-Dardīr et ḥāshiya al-Dasūqī (2ᵉ lycée)",
      pdfUrl: null,
      intro: intro12177
        ? { docId: "12177", titleAr: intro12177.titleAr, titleFr: intro12177.titleFr || trIntroTitle["12177"] || "", html: intro12177.html, htmlFr: intro12177.htmlFr || trHtml["12177"] || "" }
        : (page["12177"] ? { docId: "12177", titleAr: page["12177"]!.titleAr, titleFr: trIntroTitle["12177"], html: page["12177"]!.html, htmlFr: trHtml["12177"] } : null),
      lessons: moved,
    };
    writeBook(t2);
    // t1 réécrit : intro 11509 + leçons kept
    const newT1 = {
      ...t1,
      titleFr: "Fiqh — le Mukhtaṣar de Khalīl, comm. d'al-Dardīr et ḥāshiya al-Dasūqī (1ᵉʳ lycée)",
      intro: intro11509
        ? { docId: "11509", titleAr: intro11509.titleAr, titleFr: intro11509.titleFr || "Présentation du manuel", html: intro11509.html, htmlFr: intro11509.htmlFr || "" }
        : t1.intro,
      lessons: kept,
    };
    writeBook(newT1);
    console.log(`+ livre fiqh-tanawi-2 (${moved.length} leçons déplacées) ; fiqh-tanawi-1 → ${kept.length} leçons + intro`);
  }

  // 6. Intros pour livres existants (nouvelles pages traduites)
  const addIntro = (bookId: string, docId: string) => {
    const b = readBook(bookId);
    if (b.intro) { console.log(`· ${bookId} a déjà une intro — ignoré`); return; }
    const p = page[docId];
    if (!p) { console.log(`✗ page ${docId} introuvable pour ${bookId}`); return; }
    b.intro = { docId, titleAr: p.titleAr, titleFr: trIntroTitle[docId], html: p.html, htmlFr: trHtml[docId] };
    writeBook(b);
    console.log(`+ intro ${docId} → ${bookId}`);
  };
  addIntro("fiqh-1es", "11505");
  addIntro("hadith-1es", "13014");
  addIntro("hadith-1ep", "12583");
  addIntro("tafsir-1es", "13360");
  addIntro("tafsir-4ep", "12016");
  addIntro("ulum-quran-1es", "15373");
  addIntro("tajwid-6ep", "17502");

  // 7. Conversions leçon→intro (contenu déjà traduit dans le corpus)
  const lessonToIntro = (bookId: string, docId: string, titleFrFallback?: string) => {
    const b = readBook(bookId);
    const l = (b.lessons || []).find((x: any) => String(x.docId) === docId);
    if (!l) { console.log(`✗ leçon ${docId} non trouvée dans ${bookId}`); return; }
    b.intro = { docId: String(l.docId), titleAr: l.titleAr, titleFr: l.titleFr || titleFrFallback || "Présentation du manuel", html: l.html, htmlFr: l.htmlFr };
    b.lessons = b.lessons.filter((x: any) => String(x.docId) !== docId);
    writeBook(b);
    console.log(`↻ leçon ${docId} → intro de ${bookId}`);
  };
  lessonToIntro("fiqh-6ep", "14101");
  lessonToIntro("hadith-6ep", "14170");
  lessonToIntro("rasm-wa-dabt-6ep", "18646");
  lessonToIntro("fiqh-3es", "13876");

  // 8. fiqh-3es : leçons PDF de la galerie 13876
  {
    const b = readBook("fiqh-3es");
    const g = galleries["13876"], trs = trTitle["13876"];
    const existing = new Set((b.lessons || []).map((l: any) => String(l.docId)));
    const stubs = g.map((p, i) => mkLesson("pdf-" + (i + 1), p.title, trs[i] || p.title, p.url));
    b.lessons = [...(b.lessons || []), ...stubs];
    writeBook(b);
    console.log(`+ fiqh-3es : ${stubs.length} leçons PDF-référence`);
  }

  // 9. Merge fiqh-4ep → fiqh-1ep
  {
    const f1 = readBook("fiqh-1ep");
    const f4 = readBook("fiqh-4ep");
    const have = new Set(f1.lessons.map((l: any) => String(l.docId)));
    const added = f4.lessons.filter((l: any) => !have.has(String(l.docId)));
    f1.lessons = [...f1.lessons, ...added].sort((a: any, b: any) => parseInt(a.docId, 10) - parseInt(b.docId, 10));
    writeBook(f1);
    rmSync(path.join(BOOKS, "fiqh-4ep.json"));
    console.log(`↝ fiqh-4ep fusionné dans fiqh-1ep (+${added.length} leçons, doublons ignorés) ; fichier supprimé`);
  }

  // 10. ulum-hadith-tanawi-3 : retrait de l'article d'actualité 20436
  {
    const b = readBook("ulum-hadith-tanawi-3");
    const before = b.lessons.length;
    b.lessons = b.lessons.filter((l: any) => String(l.docId) !== "20436");
    writeBook(b);
    console.log(`− ulum-hadith-tanawi-3 : ${before} → ${b.lessons.length} leçons (article d'actualité retiré)`);
  }

  // 11. Manifeste v6
  const manifest = JSON.parse(readFileSync(MANIFEST, "utf-8"));
  const levelRank: Record<string, number> = {};
  manifest.levels.forEach((l: any, i: number) => { levelRank[l.id] = i; });
  const subjectRank: Record<string, number> = {};
  manifest.subjects.forEach((s: any, i: number) => { subjectRank[s.id] = i; });
  // reconstruire la liste des livres depuis le FS
  const ids = readdirSync(BOOKS).filter((f) => f.endsWith(".json")).map((f) => f.replace(".json", ""));
  const byId = new Map<string, any>();
  for (const id of ids) byId.set(id, readBook(id));
  const oldBooks: any[] = manifest.books.filter((b: any) => byId.has(b.id));
  const books = ids.map((id) => {
    const old = oldBooks.find((b) => b.id === id);
    const f = byId.get(id);
    return {
      id,
      subject: f.subject || old?.subject || "adab",
      level: f.level || old?.level || "tanawi-1",
      titleAr: f.titleAr || old?.titleAr || "",
      titleFr: f.titleFr || old?.titleFr || "",
      order: 0,
      ...(old?.textbookAr ? { textbookAr: old.textbookAr } : {}),
    };
  });
  books.sort((a: any, b: any) =>
    (levelRank[a.level] ?? 99) - (levelRank[b.level] ?? 99) || (subjectRank[a.subject] ?? 99) - (subjectRank[b.subject] ?? 99) || a.id.localeCompare(b.id));
  books.forEach((b: any, i: number) => { b.order = i + 1; });

  // stats réelles
  let docs = 0, lessons = 0, intros = 0, pdfLessons = 0, fullText = 0;
  for (const [, f] of byId) {
    if (f.intro) { intros++; docs++; }
    for (const l of f.lessons || []) {
      lessons++; docs++;
      if (l.pdfOnly) pdfLessons++;
      else if ((l.htmlFr || "").trim()) fullText++;
    }
  }
  manifest.version = 6;
  manifest.provisional = false;
  manifest.books = books;
  manifest.goalDocs = docs;
  manifest.note = `Corpus Taʿlīm ʿatīq — ${books.length} livres, ${docs} documents (${fullText} leçons bilingues intégrales, ${intros} introductions, ${pdfLessons} leçons référence PDF officiel). 63/64 livres du programme officiel ; hadith-tanawi-2 reste à sourcer (leçons PDF non publiées en HTML).`;
  writeFileSync(MANIFEST, JSON.stringify(manifest, null, 2) + "\n", "utf-8");
  console.log(`\n✅ Manifeste v6 : ${books.length} livres / ${docs} docs (${fullText} texte intégral, ${intros} intros, ${pdfLessons} réf. PDF)`);
}

main().catch((e) => { console.error(e); process.exit(1); });
