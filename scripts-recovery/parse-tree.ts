/**
 * Minhāj — Extraction de l'arbre du programme Taʿlīm ʿatīq depuis la page
 * principale du site du ministère (récupérée via le proxy translate.goog).
 *
 * Usage: bun run scripts-recovery/parse-tree.ts [fichier.html]
 */
import { readFileSync, writeFileSync, mkdirSync, existsSync } from "fs";
import path from "path";

const SRC = process.argv[2] || "/tmp/atieq-main.html";
const OUT_DIR = path.join(process.cwd(), "content");
const OUT = path.join(OUT_DIR, "source-tree.json");

const html = readFileSync(SRC, "utf-8");

// ———————————————————————— Helpers

const decodeEntities = (s: string) =>
  s
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");

interface Entry {
  docId: string;
  pathAr: string; // chemin SEF arabe complet (décodé)
  slugAr: string; // dernier segment (id-slug)
  titleAr: string; // slug sans l'id
  href: string; // URL translate.goog originale
  cycle?: string;
  subject?: string;
  level?: string;
  kind: "book" | "lesson" | "unknown";
}

const PROGRAM_ROOT = "برنامج-التعليم-العتيق-الرئيسية";
const BOOKS_ROOT = "الكتب-المدرسية";

const links = new Map<string, Entry>();

// Tous les liens translate.goog du programme
const re = /href="(https:\/\/www-habous-gov-ma\.translate\.goog\/([^"?]+)\?_x_tr_sl=ar&amp;_x_tr_tl=fr[^"]*)"/g;
for (const m of html.matchAll(re)) {
  const href = m[1].replace(/&amp;/g, "&");
  const rawPath = decodeURIComponent(m[2]);
  const segs = rawPath.split("/").filter(Boolean);
  const last = segs[segs.length - 1];
  if (!last || !last.includes(".html")) continue;
  const mm = last.match(/^(\d{3,6})-(.+)\.html$/);
  if (!mm) continue;
  const docId = mm[1];
  const slugAr = mm[2];
  const isProgram = segs[0] === PROGRAM_ROOT || segs[0] === BOOKS_ROOT;
  if (!isProgram) continue;

  let cycle: string | undefined;
  let subject: string | undefined;
  let level: string | undefined;
  if (segs[0] === PROGRAM_ROOT && segs.length >= 4) {
    // programme/{cycleId-cycleName}/{subject}/{level}/{docId-slug}.html
    cycle = segs[1].replace(/^\d+-/, "");
    subject = segs[2];
    level = segs[3];
  } else if (segs[0] === BOOKS_ROOT) {
    // livres/{catId-catName}(/{subId-subName})?/{docId-slug}.html
    const cat = segs[1]?.replace(/^\d+-/, "");
    subject = segs[2]?.replace(/^\d+-/, "") ?? cat;
    cycle = subject;
  }

  const kind: Entry["kind"] = /^(كتاب|الكتاب)\b/.test(slugAr)
    ? "book"
    : slugAr.includes("كتاب-") || /من-متن|من-مختصر|من-خلال/.test(slugAr)
      ? "book"
      : "lesson";

  const entry: Entry = {
    docId,
    pathAr: rawPath,
    slugAr,
    titleAr: slugAr.replace(/-/g, " "),
    href,
    cycle,
    subject,
    level,
    kind,
  };
  if (!links.has(docId)) links.set(docId, entry);
}

const entries = [...links.values()];
console.log(`Liens du programme extraits : ${entries.length}`);
const books = entries.filter((e) => e.kind === "book");
const lessons = entries.filter((e) => e.kind === "lesson");
console.log(`  ≈ livres (heuristique) : ${books.length}`);
console.log(`  ≈ leçons (heuristique) : ${lessons.length}`);

// Groupements par matière+niveau
const groups = new Map<string, Entry[]>();
for (const e of entries) {
  const key = [e.subject ?? "?", e.level ?? (e.kind === "book" ? "livre" : "?")].filter(Boolean).join(" / ");
  if (!groups.has(key)) groups.set(key, []);
  groups.get(key)!.push(e);
}
console.log("\nGroupes matière/niveau :");
for (const [k, v] of [...groups.entries()].sort()) {
  console.log(`  ${k}: ${v.length} liens (ex: ${v[0].docId})`);
}

// Distinct subjects & levels
const subjects = new Set(entries.map((e) => e.subject).filter(Boolean));
const levels = new Set(entries.map((e) => e.level).filter(Boolean));
console.log("\nMatières:", [...subjects].join(", "));
console.log("Niveaux:", [...levels].join(", "));

// ———————————————————————— Écriture
mkdirSync(OUT_DIR, { recursive: true });
const tree = {
  version: 1,
  generatedAt: new Date().toISOString(),
  source: "habous.gov.ma via translate.goog — page برنامج التعليم العتيق الرئيسية",
  counts: { total: entries.length, books: books.length, lessons: lessons.length },
  entries,
};
writeFileSync(OUT, JSON.stringify(tree, null, 2) + "\n", "utf-8");
console.log(`\n✅ Arbre écrit → content/source-tree.json (${entries.length} entrées)`);
