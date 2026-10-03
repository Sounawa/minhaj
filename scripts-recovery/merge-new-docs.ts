/**
 * Minhāj — Fusion des 84 nouveaux documents (balayage R5) dans le corpus.
 *
 * Sources : /home/z/tr-src/raw2/*.html (87 docs − 3 à ignorer).
 * Nouveaux livres : usul-fiqh-waraqat (29), usul-fiqh-tanawi-1 (intro 15371),
 * tafsir-5ep (13886), rasm-wa-dabt-6ep (18646).
 * Ajouts : qiraat-tanawi-1, mantiq-tanawi-1, ulum-quran-1es/2es, fiqh-4ep,
 * tafsir-4ep/6ep/1es, fiqh-tanawi-3, hadith-tanawi-1, tajwid-5ep, rasm-wa-dabt-4ep.
 *
 * Usage: bun run scripts-recovery/merge-new-docs.ts
 */
import { readFileSync, writeFileSync, existsSync, readdirSync } from "fs";
import path from "path";

const RAW2 = "/home/z/tr-src/raw2";
const BOOKS = path.join(process.cwd(), "content", "books");
const MANIFEST = path.join(process.cwd(), "content", "manifest.json");

const SKIP = new Set(["12576", "13984", "16713"]); // pages catégorie + actualité

/** Nettoyage HTML (identique à build-corpus.ts). */
function cleanArticleHtml(raw: string): { titleAr: string; html: string } | null {
  const m = raw.match(/<div class="item-page"[^>]*>([\s\S]*?)<\/div>\s*<div class="(?:module|clearfix|pagination|tags)/);
  let inner = m ? m[1] : null;
  if (!inner) {
    const m2 = raw.match(/<div class="item-page"[^>]*>([\s\S]{50,40000}?)<\/article>/);
    inner = m2 ? m2[1] : null;
  }
  if (!inner) {
    const m3 = raw.match(/<div class="item-page"[^>]*>([\s\S]*)/);
    inner = m3 ? m3[1].split(/<div class="(?:module|sidebar|footer|bottom)/)[0] : null;
  }
  if (!inner) return null;
  const tm = inner.match(/<h2[^>]*>([\s\S]*?)<\/h2>/);
  let titleAr = tm ? tm[1].replace(/<[^>]+>/g, "").trim() : "";
  if (!titleAr) {
    const tm2 = inner.match(/<h[23][^>]*>([\s\S]*?)<\/h[23]>/);
    titleAr = tm2 ? tm2[1].replace(/<[^>]+>/g, "").trim() : "";
  }
  let html = inner.replace(/<h2[^>]*>[\s\S]*?<\/h2>/, "");
  html = html.replace(/(?:الاثنين|الثلاثاء|الأربعاء|الخميس|الجمعة|السبت|الأحد)[^<]{0,40}\d{4}/g, "");
  html = html
    .replace(/<script[\s\S]*?<\/script>/gi, "")
    .replace(/<style[\s\S]*?<\/style>/gi, "")
    .replace(/<form[\s\S]*?<\/form>/gi, "")
    .replace(/<iframe[\s\S]*?<\/iframe>/gi, "")
    .replace(/<img[^>]*>/gi, "")
    .replace(/<button[\s\S]*?<\/button>/gi, "")
    .replace(/<input[^>]*>/gi, "")
    .replace(/<!--[\s\S]*?-->/g, "");
  html = html.replace(/\s(?:class|id|style|onclick|onload|data-[a-z-]+)="[^"]*"/gi, "");
  html = html.replace(/<a\s[^>]*href="[^"]*"[^>]*>([\s\S]*?)<\/a>/gi, "$1");
  html = html.replace(/\n{3,}/g, "\n\n").replace(/[ \t]{2,}/g, " ").trim();
  if (html.length < 60) return null;
  return { titleAr, html };
}

/** Mapping docId → { bookId, role } — établi par analyse des chemins/titres R5. */
const SPECIAL: Record<string, { bookId: string; role: "intro" | "lesson" }> = {
  "11798": { bookId: "usul-fiqh-waraqat", role: "intro" },
  "15371": { bookId: "usul-fiqh-tanawi-1", role: "intro" },
  "16302": { bookId: "mantiq-tanawi-1", role: "lesson" }, // préface du livre → leçon liminaire
  "13886": { bookId: "tafsir-5ep", role: "lesson" },
  "18646": { bookId: "rasm-wa-dabt-6ep", role: "lesson" },
  "19725": { bookId: "rasm-wa-dabt-4ep", role: "lesson" },
};

/** Règles par plage de docId (sources : catégories du balayage). */
function mapDoc(docId: string, pathAr: string, titleAr: string): { bookId: string; role: "intro" | "lesson" } | null {
  if (SPECIAL[docId]) return SPECIAL[docId];
  const p = pathAr.replace("component/content/article/", "");
  const segs = p.split("/");
  const subj = segs[2] || "";
  const cat = segs[3] || "";
  const n = parseInt(docId, 10);

  // Waraqat : leçons 11800-11926 sous 1541/أصول-الفقه
  if (subj === "أصول-الفقه" && n >= 11800 && n <= 11926) return { bookId: "usul-fiqh-waraqat", role: "lesson" };

  // Fiqh 4ep (Akhdari) : 11367-11394 (arbre livres, ابتدائي)
  if ((subj === "الفقه" || subj === "الفقه") && n >= 11360 && n <= 11415) return { bookId: "fiqh-4ep", role: "lesson" };

  // Tafsir 4ep (Jalalayn ابتدائي 1548) : 12017, 12018, 12302
  if (subj === "التفسير" && ["12017", "12018", "12302"].includes(docId)) return { bookId: "tafsir-4ep", role: "lesson" };
  // Tafsir 6ep : 14430 (السادس)
  if (docId === "14430") return { bookId: "tafsir-6ep", role: "lesson" };
  // Tafsir 1es (التسهيل إعدادي) : 12381
  if (docId === "12381") return { bookId: "tafsir-1es", role: "lesson" };

  // Tajwid 5ep (الخامس ابتدائي) : 15839, 15852
  if (subj === "التجويد" && ["15839", "15852"].includes(docId)) return { bookId: "tajwid-5ep", role: "lesson" };

  // Qiraat tanawi-1 (أولى ثانوي) : 18645, 19030-19205
  if (subj === "القراءات" && ((n >= 18640 && n <= 18660) || (n >= 19000 && n <= 19210))) return { bookId: "qiraat-tanawi-1", role: "lesson" };

  // Ulum Quran 1es (السنة أولى إعدادي) : 15381, 15396-15887
  if ((subj === "علوم-القُرآن" || subj === "علوم-القرآن" || p.startsWith("15381")) &&
      (["15381", "15396", "15402", "15423", "15653", "15752", "15765", "15841", "15855", "15875", "15887"].includes(docId)))
    return { bookId: "ulum-quran-1es", role: "lesson" };
  // Ulum Quran 2es : 19261 (التفسير الفقهي — السنة الثانية إعدادي)
  if (docId === "19261") return { bookId: "ulum-quran-2es", role: "lesson" };

  // Mantiq tanawi-1 : 16143-16167
  if ((subj === "المنطِق" || subj === "المنطق") && n >= 16140 && n <= 16170) return { bookId: "mantiq-tanawi-1", role: "lesson" };

  // Fiqh tanawi-3 (الثانوي الثالث) : 19360, 19655 ; 19756 (فهرس الأعلام — même livre que 19757)
  if (["19360", "19655", "19756"].includes(docId)) return { bookId: "fiqh-tanawi-3", role: "lesson" };

  // Hadith tanawi-1 : 13124
  if (docId === "13124") return { bookId: "hadith-tanawi-1", role: "lesson" };

  // Repli : sujet + niveau depuis la catégorie
  const SUBJ: Record<string, string> = {
    "التوحيد": "tawhid", "الفقه": "fiqh", "السيرة-النبوية": "sira", "التجويد": "tajwid",
    "التفسير": "tafsir", "الحديث": "hadith", "الفرائض": "faraid", "الفرائِض": "faraid",
    "أصول-الفقه": "usul-fiqh", "المنطق": "mantiq", "المنطِق": "mantiq", "علوم-الحديث": "ulum-hadith",
    "علوم-القُرآن": "ulum-quran", "علوم-القرآن": "ulum-quran", "القراءات": "qiraat",
    "الرسم-والضبط": "rasm-wa-dabt", "التوقيت": "taqtit", "الفكر-الإسلامي": "fikr-islami",
    "أصول-القيم-في-القرآن-والسنة": "usul-qiyam",
  };
  const s = SUBJ[subj];
  if (!s) return null;
  const t = (cat + " " + titleAr).replace(/-/g, " ");
  const level =
    /ابتدائي/.test(t) && /الرابع|الرابعة/.test(t) ? "4ep" :
    /ابتدائي/.test(t) && /الخامس|الخامسة/.test(t) ? "5ep" :
    /ابتدائي/.test(t) && /السادس|السادسة/.test(t) ? "6ep" :
    /إعدادي/.test(t) && /الأول|الأولى/.test(t) ? "1es" :
    /إعدادي/.test(t) && /الثاني|الثانية/.test(t) ? "2es" :
    /إعدادي/.test(t) && /الثالث|الثالثة/.test(t) ? "3es" :
    /ثانوي/.test(t) && /الأول|الأولى/.test(t) ? "tanawi-1" :
    /ثانوي/.test(t) && /الثاني|الثانية/.test(t) ? "tanawi-2" :
    /ثانوي/.test(t) && /الثالث|الثالثة/.test(t) ? "tanawi-3" : null;
  if (!level) return null;
  return { bookId: `${s}-${level}`, role: "lesson" };
}

// Métadonnées des nouveaux livres
const NEW_BOOKS: Record<string, { subject: string; level: string; subjectAr: string; levelAr: string; titleAr: string }> = {
  "usul-fiqh-waraqat": {
    subject: "usul-fiqh", level: "tanawi-2", subjectAr: "أصول الفقه", levelAr: "السنة الثانية من التعليم الثانوي العتيق",
    titleAr: "كتاب أصول الفقه من ورقات إمام الحرمين بشرح الحطاب الرعيني",
  },
  "usul-fiqh-tanawi-1": {
    subject: "usul-fiqh", level: "tanawi-1", subjectAr: "أصول الفقه", levelAr: "السنة الأولى من التعليم الثانوي العتيق",
    titleAr: "أصول الفقه من منظومة مرتقى الوصول إلى الضروري من الأصول",
  },
  "tafsir-5ep": {
    subject: "tafsir", level: "5ep", subjectAr: "التفسير", levelAr: "السنة الخامسة من التعليم الابتدائي العتيق",
    titleAr: "التفسير من خلال تفسير الجلالين للسنة الخامسة من التعليم الابتدائي العتيق",
  },
  "rasm-wa-dabt-6ep": {
    subject: "rasm-wa-dabt", level: "6ep", subjectAr: "الرسم والضبط", levelAr: "السنة السادسة من التعليم الابتدائي العتيق",
    titleAr: "الرسم والضبط من أرجوزة عمدة البيان لإدريس الودغيري",
  },
};

// ─── 1. Parser les nouveaux documents ────────────────────────────────────────
interface NewDoc { docId: string; titleAr: string; html: string; bookId: string; role: "intro" | "lesson"; }
const found: Array<[string, string]> = JSON.parse(readFileSync(path.join(RAW2, "sweep-found.json"), "utf-8"));
const pathById = new Map(found);

const newDocs: NewDoc[] = [];
let skipped = 0, unmapped = 0;
for (const f of readdirSync(RAW2)) {
  if (!f.endsWith(".html") || f.startsWith("cat-")) continue;
  const docId = f.replace(".html", "");
  if (SKIP.has(docId)) { skipped++; continue; }
  const raw = readFileSync(path.join(RAW2, f), "utf-8");
  const parsed = cleanArticleHtml(raw);
  if (!parsed || parsed.html.length < 80) { console.log(`  ✗ parse ${docId}`); skipped++; continue; }
  const pathAr = pathById.get(docId) || "";
  const mapping = mapDoc(docId, pathAr, parsed.titleAr);
  if (!mapping) { console.log(`  ? non mappé : ${docId} — ${parsed.titleAr.slice(0, 45)}`); unmapped++; continue; }
  newDocs.push({ docId, titleAr: parsed.titleAr, html: parsed.html, ...mapping });
}
console.log(`Nouveaux docs : ${newDocs.length} (ignorés: ${skipped}, non mappés: ${unmapped})`);

// ─── 2. Fusionner dans les livres ────────────────────────────────────────────
const byBook = new Map<string, NewDoc[]>();
for (const d of newDocs) {
  if (!byBook.has(d.bookId)) byBook.set(d.bookId, []);
  byBook.get(d.bookId)!.push(d);
}

let added = 0, createdBooks = 0, updatedBooks = 0;
for (const [bookId, docs] of byBook) {
  const file = path.join(BOOKS, bookId + ".json");
  let book: any;
  if (existsSync(file)) {
    book = JSON.parse(readFileSync(file, "utf-8"));
  } else if (NEW_BOOKS[bookId]) {
    const meta = NEW_BOOKS[bookId];
    book = { id: bookId, subject: meta.subject, level: meta.level, subjectAr: meta.subjectAr, levelAr: meta.levelAr, titleAr: meta.titleAr, titleFr: "", pdfUrl: null, intro: null, lessons: [] };
    createdBooks++;
  } else {
    console.log(`  ? livre inconnu ${bookId} — ignoré`);
    continue;
  }
  const existing = new Set<string>([(book.intro?.docId ?? "").toString(), ...(book.lessons || []).map((l: any) => String(l.docId))]);
  for (const d of docs) {
    if (existing.has(d.docId)) continue;
    if (d.role === "intro" && !book.intro) {
      book.intro = { docId: d.docId, titleAr: d.titleAr, titleFr: "", html: d.html, htmlFr: "" };
    } else {
      book.lessons = book.lessons || [];
      book.lessons.push({ docId: d.docId, titleAr: d.titleAr, titleFr: "", html: d.html, htmlFr: "" });
    }
    added++;
  }
  book.lessons?.sort((a: any, b: any) => parseInt(a.docId, 10) - parseInt(b.docId, 10));
  writeFileSync(file, JSON.stringify(book, null, 2) + "\n", "utf-8");
  updatedBooks++;
  console.log(`  ✓ ${bookId} : ${docs.length} docs (total leçons: ${book.lessons?.length ?? 0}${book.intro ? " + intro" : ""})`);
}
console.log(`\nFusion : +${added} documents, ${createdBooks} nouveaux livres, ${updatedBooks} livres mis à jour.`);

// ─── 3. Mettre à jour le manifeste ──────────────────────────────────────────
const manifest = JSON.parse(readFileSync(MANIFEST, "utf-8"));
const existingIds = new Set(manifest.books.map((b: any) => b.id));
const SUBJECT_FR: Record<string, { labelAr: string; titleFr: string; icon: string }> = {
  "usul-fiqh": { labelAr: "أصول الفقه", titleFr: "Principes du droit", icon: "Scale" },
  tafsir: { labelAr: "التفسير", titleFr: "Exégèse coranique", icon: "BookOpenText" },
  "rasm-wa-dabt": { labelAr: "الرسم والضبط", titleFr: "Graphie et vocalisation", icon: "PenLine" },
};
let order = Math.max(...manifest.books.map((b: any) => b.order || 0));
for (const [bookId, meta] of Object.entries(NEW_BOOKS)) {
  if (existingIds.has(bookId)) continue;
  order += 1;
  manifest.books.push({ id: bookId, subject: meta.subject, level: meta.level, titleAr: meta.titleAr, titleFr: "", order });
  // s'assurer que le sujet existe
  let subj = manifest.subjects.find((s: any) => s.id === meta.subject);
  if (!subj) {
    const s = SUBJECT_FR[meta.subject] || { labelAr: meta.subjectAr, titleFr: meta.subject, icon: "BookOpenText" };
    manifest.subjects.push({ id: meta.subject, labelAr: s.labelAr, titleFr: s.titleFr, translit: "", icon: s.icon, booksCount: 0 });
  }
}
// s'assurer que les niveaux 5ep/6ep existent (ils existent déjà)
manifest.books.sort((a: any, b: any) => (a.order || 0) - (b.order || 0));
// recompter booksCount
const counts: Record<string, number> = {};
for (const b of manifest.books) counts[b.subject] = (counts[b.subject] || 0) + 1;
for (const s of manifest.subjects) s.booksCount = counts[s.id] || 0;

const totalDocs = manifest.books.reduce((acc: number, b: any) => {
  const f = path.join(BOOKS, b.id + ".json");
  if (!existsSync(f)) return acc;
  const j = JSON.parse(readFileSync(f, "utf-8"));
  return acc + (j.lessons?.length || 0) + (j.intro ? 1 : 0);
}, 0);
manifest.goalDocs = totalDocs;
manifest.note = `Corpus Taʿlīm ʿatīq — ${manifest.books.length} livres, ${totalDocs} documents bilingues (source : site officiel via proxy).`;
writeFileSync(MANIFEST, JSON.stringify(manifest, null, 2) + "\n", "utf-8");
console.log(`Manifeste : ${manifest.books.length} livres, ${totalDocs} documents au total.`);
