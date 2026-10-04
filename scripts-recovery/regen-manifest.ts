/**
 * Minhāj — Régénère content/manifest.json depuis content/books/*.json
 * (ordre : niveau → matière → id ; stats réelles).
 * Usage: bun run scripts-recovery/regen-manifest.ts
 */
import { readFileSync, writeFileSync, readdirSync } from "fs";
import path from "path";

const BOOKS = path.join(process.cwd(), "content", "books");
const manifest = JSON.parse(readFileSync(path.join(process.cwd(), "content", "manifest.json"), "utf-8"));

const levelRank: Record<string, number> = {};
manifest.levels.forEach((l: any, i: number) => { levelRank[l.id] = i; });
const subjectRank: Record<string, number> = {};
manifest.subjects.forEach((s: any, i: number) => { subjectRank[s.id] = i; });

const ids = readdirSync(BOOKS).filter((f) => f.endsWith(".json")).map((f) => f.replace(".json", ""));
const files = new Map<string, any>();
let docs = 0, lessons = 0, intros = 0, pdfLessons = 0, fullText = 0;
for (const id of ids) {
  const f = JSON.parse(readFileSync(path.join(BOOKS, id + ".json"), "utf-8"));
  files.set(id, f);
  if (f.intro) { intros++; docs++; }
  for (const l of f.lessons || []) {
    lessons++; docs++;
    if (l.pdfOnly) pdfLessons++;
    else if ((l.htmlFr || "").trim()) fullText++;
  }
}

const oldById = new Map<string, any>(manifest.books.map((b: any) => [b.id, b]));
const books = ids.map((id) => {
  const f = files.get(id);
  const old = oldById.get(id);
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
  (levelRank[a.level] ?? 99) - (levelRank[b.level] ?? 99) ||
  (subjectRank[a.subject] ?? 99) - (subjectRank[b.subject] ?? 99) ||
  a.id.localeCompare(b.id));
books.forEach((b: any, i: number) => { b.order = i + 1; });

manifest.version = 6;
manifest.provisional = false;
manifest.books = books;
manifest.goalDocs = docs;
manifest.note =
  `Corpus Taʿlīm ʿatīq — ${books.length} livres (grille en ligne complète), ${docs} documents ` +
  `(${fullText} leçons bilingues intégrales, ${intros} introductions, ` +
  `${pdfLessons} leçons référence PDF officiel). ` +
  `hadith-tanawi-2 (Muwaṭṭaʾ 2ᵉ lycée) : leçons non publiées à ce jour par le ` +
  `ministère — présentation seule. Objectif officiel du programme : 64 manuels.`;

writeFileSync(path.join(process.cwd(), "content", "manifest.json"), JSON.stringify(manifest, null, 2) + "\n", "utf-8");
console.log(`Manifeste v6 : ${books.length} livres / ${docs} docs | ${fullText} intégral | ${intros} intros | ${pdfLessons} réf. PDF`);
