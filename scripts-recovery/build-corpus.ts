/**
 * Minhāj — Construction du corpus bilingue depuis les pages brutes crawlées
 * (/home/z/tr-src/raw/*.html) → content/books/{bookId}.json + manifest réel.
 *
 * Parsing :
 *  - item-page Joomla = article (leçon ou page livre)
 *  - matière/niveau depuis le chemin SEF, ou le nom du livre dans le slug
 *  - leçons ordonnées par docId
 *
 * Usage: bun run scripts-recovery/build-corpus.ts
 */
import { readFileSync, writeFileSync, mkdirSync, existsSync, readdirSync } from "fs";
import path from "path";

const RAW = "/home/z/tr-src/raw";
const OUT_BOOKS = path.join(process.cwd(), "content", "books");
const idx: Record<string, string> = JSON.parse(readFileSync(path.join(RAW, "index.json"), "utf-8"));
mkdirSync(OUT_BOOKS, { recursive: true });

// ———————————————————————————————————————— Nettoyage HTML

function cleanArticleHtml(raw: string): { titleAr: string; html: string } | null {
  // div item-page (article Joomla)
  const m = raw.match(/<div class="item-page"[^>]*>([\s\S]*?)<\/div>\s*<div class="(?:module|clearfix|pagination|tags)/);
  let inner = m ? m[1] : null;
  if (!inner) {
    // repli : capture bornée
    const m2 = raw.match(/<div class="item-page"[^>]*>([\s\S]{50,40000}?)<\/article>/);
    inner = m2 ? m2[1] : null;
  }
  if (!inner) {
    const m3 = raw.match(/<div class="item-page"[^>]*>([\s\S]*)/);
    // dernier recours : jusqu'à la fin des colonnes principales
    inner = m3 ? m3[1].split(/<div class="(?:module|sidebar|footer|bottom)/)[0] : null;
  }
  if (!inner) return null;

  // Titre : h2 du début
  const tm = inner.match(/<h2[^>]*>([\s\S]*?)<\/h2>/);
  let titleAr = tm ? tm[1].replace(/<[^>]+>/g, "").trim() : "";
  if (!titleAr) {
    const tm2 = inner.match(/<h[23][^>]*>([\s\S]*?)<\/h[23]>/);
    titleAr = tm2 ? tm2[1].replace(/<[^>]+>/g, "").trim() : "";
  }
  // retirer le bloc titre/date du contenu
  let html = inner.replace(/<h2[^>]*>[\s\S]*?<\/h2>/, "");
  // retirer la date de publication (ex: الخميس 28 نوفمبر 2024)
  html = html.replace(/(?:الاثنين|الثلاثاء|الأربعاء|الخميس|الجمعة|السبت|الأحد)[^<]{0,40}\d{4}/g, "");
  // balises à éliminer totalement
  html = html
    .replace(/<script[\s\S]*?<\/script>/gi, "")
    .replace(/<style[\s\S]*?<\/style>/gi, "")
    .replace(/<form[\s\S]*?<\/form>/gi, "")
    .replace(/<iframe[\s\S]*?<\/iframe>/gi, "")
    .replace(/<img[^>]*>/gi, "")
    .replace(/<button[\s\S]*?<\/button>/gi, "")
    .replace(/<input[^>]*>/gi, "")
    .replace(/<!--[\s\S]*?-->/g, "");
  // classes/ids inline inutiles
  html = html.replace(/\s(?:class|id|style|onclick|onload|data-[a-z-]+)="[^"]*"/gi, "");
  // liens → texte (le protocole Minhāj n'inclut pas de liens externes)
  html = html.replace(/<a\s[^>]*href="[^"]*"[^>]*>([\s\S]*?)<\/a>/gi, "$1");
  // espaces multiples
  html = html.replace(/\n{3,}/g, "\n\n").replace(/[ \t]{2,}/g, " ").trim();
  if (html.length < 60) return null;
  return { titleAr, html: html };
}

// ———————————————————————————————————————— Mappages matières / niveaux

const SUBJECTS: Record<string, { id: string; fr: string }> = {
  "التوحيد": { id: "tawhid", fr: "Monothéisme" },
  "الفقه": { id: "fiqh", fr: "Droit rituel" },
  "السيرة-النبوية": { id: "sira", fr: "Biographie prophétique" },
  "التجويد": { id: "tajwid", fr: "Psalmodie coranique" },
  "التفسير": { id: "tafsir", fr: "Exégèse coranique" },
  "الحديث": { id: "hadith", fr: "Tradition prophétique" },
  "الفرائض": { id: "faraid", fr: "Droit successoral" },
  "الفرائِض": { id: "faraid", fr: "Droit successoral" },
  "أصول-الفقه": { id: "usul-fiqh", fr: "Principes du droit" },
  "المنطق": { id: "mantiq", fr: "Logique" },
  "المنطِق": { id: "mantiq", fr: "Logique" },
  "علوم-الحديث": { id: "ulum-hadith", fr: "Sciences du hadith" },
  "علوم-القُرآن": { id: "ulum-quran", fr: "Sciences coraniques" },
  "علوم-القرآن": { id: "ulum-quran", fr: "Sciences coraniques" },
  "القراءات": { id: "qiraat", fr: "Lectures coraniques" },
  "الرسم-والضبط": { id: "rasm-wa-dabt", fr: "Graphie et vocalisation" },
  "التوقيت": { id: "taqtit", fr: "Découpage temporel" },
  "الفكر-الإسلامي": { id: "fikr-islami", fr: "Pensée islamique" },
  "أصول-القيم-في-القرآن-والسنة": { id: "usul-qiyam", fr: "Valeurs du Coran et de la Sunna" },
  "النحو-والصرف": { id: "nahu", fr: "Grammaire et morphologie" },
  "النحو": { id: "nahu", fr: "Grammaire" },
  "البلاغة": { id: "balagha", fr: "Rhétorique" },
  "الأدب": { id: "adab", fr: "Littérature" },
};

function parseLevel(text: string): string | null {
  const t = text.replace(/-/g, " ");
  const isIbtidai = /ابتدائي/.test(t);
  const isIhdadi = /إعدادي/.test(t);
  const isThanawi = /ثانوي/.test(t);
  const n =
    /السادس|السادسة/.test(t) ? 6 :
    /الخامس|الخامسة/.test(t) ? 5 :
    /الرابع|الرابعة/.test(t) ? 4 :
    /الثالث|الثالثة/.test(t) ? 3 :
    /الثاني|الثانية/.test(t) ? 2 :
    /الأول|الأولى/.test(t) ? 1 : null;
  if (isIbtidai && n) return `${n}ep`;
  if (isIhdadi && n) return `${n}es`;
  if (isThanawi && n) return `tanawi-${n}`;
  if (isIbtidai) return "1ep";
  if (isIhdadi) return "1es";
  if (isThanawi) return "tanawi-1";
  return null;
}

// ———————————————————————————————————————— 1. Lire tous les docs

interface Doc {
  docId: string;
  pathAr: string;
  subjectAr?: string;
  levelAr?: string;
  titleAr: string;
  html: string;
  slug: string;
}

const docs: Doc[] = [];
let unparsed = 0;
for (const [docId, pathAr] of Object.entries(idx)) {
  if (docId === "main" || docId.startsWith("cat:")) continue;
  const f = path.join(RAW, docId + ".html");
  if (!existsSync(f)) continue;
  const raw = readFileSync(f, "utf-8");
  const parsed = cleanArticleHtml(raw);
  if (!parsed || parsed.html.length < 80) { unparsed++; continue; }
  const segs = pathAr.split("/");
  let subjectAr: string | undefined;
  let levelAr: string | undefined;
  if (segs[0] === "برنامج-التعليم-العتيق-الرئيسية" && segs.length >= 5) {
    subjectAr = segs[2];
    levelAr = segs[3];
  }
  docs.push({
    docId,
    pathAr,
    subjectAr,
    levelAr,
    titleAr: parsed.titleAr,
    html: parsed.html,
    slug: segs[segs.length - 1].replace(/\.html$/, ""),
  });
}
console.log(`Docs analysés : ${docs.length} (non exploitables : ${unparsed})`);

// ———————————————————————————————————————— 2. Livres = groupes (matière, niveau)

interface BookDraft {
  bookId: string;
  subjectAr: string;
  levelAr: string;
  subject: string;
  level: string;
  introDoc: Doc | null;
  lessons: Doc[];
  titleAr: string;
}

const drafts = new Map<string, BookDraft>();

function ensureBook(subjectAr: string, levelAr: string): BookDraft | null {
  const subj = SUBJECTS[subjectAr];
  const level = parseLevel(levelAr) ?? parseLevel(subjectAr + " " + levelAr);
  if (!subj || !level) return null;
  const bookId = `${subj.id}-${level}`;
  if (!drafts.has(bookId)) {
    drafts.set(bookId, {
      bookId, subjectAr, levelAr,
      subject: subj.id, level,
      introDoc: null, lessons: [],
      titleAr: "",
    });
  }
  return drafts.get(bookId)!;
}

// Classification livre/leçon :
//  - slug contient « كتاب-… » juste après le titre → leçon dont le slug porte le nom du livre
//  - le doc est une PAGE LIVRE si : slug commence par كتاب / contient مقدمة / c'est le doc
//    le plus « présentation » (contient « منهج »/« مقدمة الكتاب ») et le groupe est dense.
const isBookPage = (d: Doc) =>
  /^كتاب/.test(d.slug.replace(/^\d+-/, "")) ||
  d.html.includes("مقدمة الكتاب") ||
  d.html.includes("توزيع الدوري") ||
  d.html.includes("كيف أستعمل كتابي");

for (const d of docs) {
  // 1) arbre programme → matière/niveau explicites
  if (d.subjectAr && d.levelAr) {
    const b = ensureBook(d.subjectAr, d.levelAr);
    if (b) {
      if (isBookPage(d) && !b.introDoc) b.introDoc = d;
      else b.lessons.push(d);
      continue;
    }
  }
  // 2) arbre الكتب-المدرسية / autres : déduire du slug « …-كتاب-{livre} »
  const sm = d.slug.match(/-كتاب-(.{6,})$/);
  if (sm) {
    const bookSlug = sm[1];
    // matière : chercher un mot-clé dans le nom du livre
    let subjectAr = "";
    for (const key of Object.keys(SUBJECTS)) {
      if (bookSlug.includes(key.replace(/-/g, " ")) || bookSlug.includes(key)) { subjectAr = key; break; }
    }
    // niveau : mot-clé dans le nom du livre
    const level = parseLevel(bookSlug);
    if (subjectAr && level) {
      const b = ensureBook(subjectAr, bookSlug);
      if (b) {
        const exists = b.lessons.some((l) => l.docId === d.docId) || b.introDoc?.docId === d.docId;
        if (!exists) b.lessons.push(d);
        continue;
      }
    }
  }
  // 3) rien trouvé → essai matière depuis le path incomplet
  const segs = d.pathAr.split("/");
  if (segs.length >= 3) {
    const b = ensureBook(segs[2], segs[segs.length - 2]);
    if (b) {
      const exists = b.lessons.some((l) => l.docId === d.docId) || b.introDoc?.docId === d.docId;
      if (!exists) b.lessons.push(d);
      continue;
    }
  }
}

// Titres arabes des livres : depuis le slug de l'intro ou le suffixe des leçons
for (const b of drafts.values()) {
  if (b.introDoc) {
    b.titleAr = b.introDoc.titleAr || b.introDoc.slug.replace(/^\d+-كتاب-/, "").replace(/-/g, " ");
  }
  if (!b.titleAr && b.lessons.length) {
    const sm = b.lessons[0].slug.match(/-كتاب-(.{6,})$/);
    if (sm) b.titleAr = sm[1].replace(/-/g, " ").replace(/ التعليم العتيق$/, "").trim();
  }
  if (!b.titleAr) b.titleAr = (SUBJECTS[b.subjectAr]?.fr ?? b.subjectAr) + " — " + b.levelAr.replace(/-/g, " ");
  b.lessons.sort((a, z) => parseInt(a.docId, 10) - parseInt(z.docId, 10));
}

console.log(`Livres reconstitués : ${drafts.size}`);
let totalLessons = 0;
const manifestBooks: any[] = [];
const LEVEL_ORDER = (l: string) => parseInt(l, 10) || 0;
const order = [...drafts.values()].sort((a, b) => {
  const cyc = (x: string) => (x.endsWith("ep") ? 1 : x.endsWith("es") ? 2 : 3);
  return cyc(a.level) - cyc(b.level) || LEVEL_ORDER(a.level) - LEVEL_ORDER(b.level) || a.subject.localeCompare(b.subject);
});

order.forEach((b, i) => {
  const data = {
    id: b.bookId,
    subject: b.subject,
    level: b.level,
    subjectAr: b.subjectAr,
    levelAr: b.levelAr,
    titleAr: b.titleAr,
    titleFr: "",
    pdfUrl: null,
    intro: b.introDoc
      ? { docId: b.introDoc.docId, titleAr: b.introDoc.titleAr, titleFr: "", html: b.introDoc.html, htmlFr: "" }
      : null,
    lessons: b.lessons.map((l) => ({
      docId: l.docId,
      titleAr: l.titleAr,
      titleFr: "",
      html: l.html,
      htmlFr: "",
    })),
  };
  writeFileSync(path.join(OUT_BOOKS, `${b.bookId}.json`), JSON.stringify(data, null, 2) + "\n", "utf-8");
  totalLessons += b.lessons.length;
  manifestBooks.push({
    id: b.bookId, subject: b.subject, level: b.level,
    titleAr: b.titleAr, titleFr: "", order: i + 1,
    ...(b.introDoc ? {} : {}),
  });
  const flag = b.lessons.length < 8 ? " ⚠︎" : "";
  console.log(`  ${String(b.lessons.length).padStart(3)} leçons${b.introDoc ? " +intro" : "       "} | ${b.bookId}${flag}`);
});

// Manifeste réel
const manifest = JSON.parse(readFileSync(path.join(process.cwd(), "content", "manifest.json"), "utf-8"));
manifest.version = 4;
manifest.provisional = false;
manifest.note = "Structure reconstruite depuis le site officiel (habous.gov.ma via proxy Google Translate), session R2. Les titres FR et traductions sont ajoutés progressivement.";
manifest.subjects = Object.entries(SUBJECTS).map(([ar, s]) => ({ id: s.id, labelAr: ar, titleFr: s.fr, translit: "", icon: "BookOpenText", booksCount: manifestBooks.filter((b) => b.subject === s.id).length }));
manifest.books = manifestBooks;
manifest.goalDocs = totalLessons;
manifest.program.goalDocs = totalLessons;
manifest.program.goalBooks = manifestBooks.length;
writeFileSync(path.join(process.cwd(), "content", "manifest.json"), JSON.stringify(manifest, null, 2) + "\n", "utf-8");

console.log(`\n✅ Corpus construit : ${manifestBooks.length} livres, ${totalLessons} leçons (+${order.filter((b) => b.introDoc).length} intros)`);
