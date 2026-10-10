/**
 * Minhāj — Fusion d'une traduction française produite par l'agent principal.
 *
 * Protocole (règle absolue : traduction par l'agent principal LUI-MÊME) :
 *   1. Extraire la source : content/books/{bookId}.json → /home/z/tr-src/{docId}.html
 *      + {docId}.meta.json (bookId, titleFr officiel).
 *   2. L'agent traduit → /home/z/tr-out/{docId}.html (HTML miroir, placeholders
 *      {{U1}}…{{Un}} remplacés par les URLs originales, 0 <img>, 0 caractère
 *      arabe hors href/src, ≥ 180 caractères).
 *   3. Ce script fusionne : htmlFr / titleFr dans content/books/{bookId}.json.
 *
 * Usage: bun run scripts-translate/agent-merge.ts <docId>
 */
import { existsSync, readFileSync, writeFileSync } from "fs";
import { readdirSync } from "fs";
import path from "path";

const CONTENT = path.join(process.cwd(), "content");
const TR_OUT = "/home/z/tr-out";

const docId = process.argv[2];
if (!docId) {
  console.error("Usage: bun run scripts-translate/agent-merge.ts <docId>");
  process.exit(1);
}

const outPath = path.join(TR_OUT, `${docId}.html`);
if (!existsSync(outPath)) {
  console.error(`✗ Traduction introuvable : ${outPath}`);
  process.exit(1);
}
let htmlFr = readFileSync(outPath, "utf-8").trim();

// ——— Validations qualité
const checks: string[] = [];
let failed = false;
if (!htmlFr.startsWith("<")) {
  checks.push("✗ Le fichier ne commence pas par une balise HTML.");
  failed = true;
}
if (htmlFr.includes("<img")) {
  checks.push("✗ Balises <img> interdites dans la traduction.");
  failed = true;
}
const arabicOutsideAttr = htmlFr
  .replace(/(?:href|src)="[^"]*"/g, "")
  .match(/[\u0600-\u06FF]/);
if (arabicOutsideAttr) {
  checks.push("✗ Caractères arabes détectés hors attributs href/src (utiliser la translittération).");
  failed = true;
}
if (Buffer.byteLength(htmlFr, "utf-8") < 180) {
  checks.push("✗ Traduction trop courte (< 180 octets).");
  failed = true;
}
if (/{{U\d+}}/.test(htmlFr)) {
  checks.push("✗ Placeholders {{U…}} non remplacés.");
  failed = true;
}
if (failed) {
  console.error(checks.join("\n"));
  console.error("\n→ Fusion ANNULÉE. Corrigez /home/z/tr-out/" + docId + ".html puis relancez.");
  process.exit(1);
}
if (checks.length === 0) checks.push("✓ Toutes les validations qualité sont passées.");

// ——— Localiser le document dans les manuels
const booksDir = path.join(CONTENT, "books");
let target: { file: string; data: any; kind: "intro" | "lesson" } | null = null;
outer: for (const f of readdirSync(booksDir)) {
  if (!f.endsWith(".json")) continue;
  const abs = path.join(booksDir, f);
  let data: any;
  try {
    data = JSON.parse(readFileSync(abs, "utf-8"));
  } catch {
    continue;
  }
  if (data?.intro?.docId === docId) {
    target = { file: abs, data, kind: "intro" };
    break outer;
  }
  const idx = (data?.lessons ?? []).findIndex((l: any) => l.docId === docId);
  if (idx !== -1) {
    target = { file: abs, data, kind: "lesson" };
    (target as any).lessonIndex = idx;
    break outer;
  }
}
if (!target) {
  console.error(`✗ docId ${docId} introuvable dans content/books/*.json`);
  process.exit(1);
}

// ——— meta.json optionnel (titleFr officiel)
const metaPath = path.join(TR_OUT, `${docId}.meta.json`);
let titleFr: string | undefined;
if (existsSync(metaPath)) {
  try {
    const meta = JSON.parse(readFileSync(metaPath, "utf-8"));
    if (typeof meta.titleFr === "string" && meta.titleFr.trim()) titleFr = meta.titleFr.trim();
    if (meta.bookId && meta.bookId !== target.data.id) {
      console.warn(`⚠︎ meta.bookId=${meta.bookId} ≠ bookId du fichier (${target.data.id}) — le fichier prime.`);
    }
  } catch {
    console.warn("⚠︎ meta.json illisible — ignoré.");
  }
}

// ——— Fusion
const sample = /échantillon|démonstration/i.test(titleFr ?? "");
if (target.kind === "intro") {
  target.data.intro.htmlFr = htmlFr;
  if (titleFr) target.data.intro.titleFr = titleFr;
  // Collision intro/leçon (même docId, ex. muqaddima vs première leçon) :
  // le même docId peut désigner aussi une leçon du même manuel — on écrit
  // toutes les occurrences (précédent hadith-1ep/12583 : textes jumeaux).
  const twins = (target.data.lessons ?? []).filter((l: any) => String(l.docId) === String(docId));
  for (const twin of twins) {
    twin.htmlFr = htmlFr;
    if (titleFr) twin.titleFr = titleFr;
  }
  if (twins.length) console.log(`   ⚠︎ docId partagé : ${twins.length} leçon(s) jumelle(s) mise(s) à jour avec la même traduction.`);
} else {
  const lesson = target.data.lessons[(target as any).lessonIndex];
  lesson.htmlFr = htmlFr;
  if (titleFr) lesson.titleFr = titleFr;
}
writeFileSync(target.file, JSON.stringify(target.data, null, 2) + "\n", "utf-8");

console.log("─".repeat(60));
console.log(`✅ Fusion réussie : ${docId} (${target.kind}) → ${path.relative(process.cwd(), target.file)}`);
if (titleFr) console.log(`   titleFr : ${titleFr}`);
checks.forEach((c) => console.log(`   ${c}`));
const docsFr = (target.data.intro?.htmlFr ? 1 : 0) + (target.data.lessons ?? []).filter((l: any) => (l.htmlFr || "").trim()).length;
const docsTotal = (target.data.intro ? 1 : 0) + (target.data.lessons ?? []).length;
console.log(`   Avancement du manuel : ${docsFr}/${docsTotal} documents bilingues`);
console.log(`   Vérification : curl http://localhost:3000/api/lessons/${target.data.id}/${docId} | jq -r '.htmlFr | length'`);
