/**
 * Minhāj R10 — Correction de grille (2) :
 * 14 leçons de fiqh-1ep appartiennent en réalité à d'autres manuels
 * (erreur de mapping lors de la fusion du corpus) :
 *  - 11937/11941/11943/11949/12002/12006/12011/12013 + annexes 12014/12015
 *    → fiqh-5ep (Murshid al-Muʿīn, 5ᵉ primaire — livre jusqu'ici vide : 0 leçons)
 *  - 12164 (aʿlām) + 12431 (maṣādir) → fiqh-2es (Risāla d'Ibn Abī Zayd, 2ᵉ collège)
 *  - 12351 (aʿlām) + 12352 (maṣādir) → fiqh-3es (Murshid al-Muʿīn, 3ᵉ collège)
 * Preuves : mention explicite « للسنة الخامسة/الثانية/الثالثة … » dans le html
 * de chaque leçon + référence au manuel (منظومة المرشد المعين / متن الرسالة).
 * Titres FR retravaillés selon la convention R9 (annexes alignées sur
 * « Personnalités citées (aʿlām) » / « Sources et références »).
 * Usage: bun run scripts-recovery/r10-grid-move.ts
 */
import { readFileSync, writeFileSync } from "fs";
import path from "path";

const BOOKS = path.join(process.cwd(), "content", "books");

type Lesson = { docId: number; titleAr?: string; titleFr?: string; [k: string]: any };

interface Book {
  id: string;
  subject: string;
  level: string;
  subjectAr: string;
  levelAr: string;
  titleAr: string;
  titleFr: string;
  pdfUrl: string | null;
  intro: any;
  lessons: Lesson[];
}

const load = (id: string): Book => JSON.parse(readFileSync(path.join(BOOKS, id + ".json"), "utf8"));
const save = (b: Book) =>
  writeFileSync(path.join(BOOKS, b.id + ".json"), JSON.stringify(b, null, 1) + "\n");

const num = (s: string | number) => Number(String(s).replace(/\D/g, "")) || 0;

/* destination → docIds + retitrage */
const moves: Record<string, { docId: string; titleFr?: string }[]> = {
  "fiqh-5ep": [
    { docId: "11937", titleFr: "Les obligations de l'ablution (farāʾiḍ al-wuḍūʾ)" },
    { docId: "11941", titleFr: "Les sunan de l'ablution et leurs mérites" },
    { docId: "11943", titleFr: "Des règles de l'ablution (wuḍūʾ)" },
    { docId: "11949", titleFr: "Les règles du lavage (ghusl)" },
    { docId: "12002", titleFr: "La prière du vendredi et la prière en groupe" },
    { docId: "12006", titleFr: "Les conditions de l'imāma" },
    { docId: "12011", titleFr: "Les règles de celui qui rejoint la prière en cours (masbūq)" },
    { docId: "12013", titleFr: "Les règles du masbūq — suite" },
    { docId: "12014", titleFr: "Personnalités citées (aʿlām)" },
    { docId: "12015", titleFr: "Sources et références" },
  ],
  "fiqh-2es": [
    { docId: "12164", titleFr: "Personnalités citées (aʿlām)" },
    { docId: "12431", titleFr: "Sources et références" },
  ],
  "fiqh-3es": [
    { docId: "12351", titleFr: "Personnalités citées (aʿlām)" },
    { docId: "12352", titleFr: "Sources et références" },
  ],
};

const src = load("fiqh-1ep");
const moved: Lesson[] = [];
const staying: Lesson[] = [];

for (const l of src.lessons) {
  const id = String(l.docId);
  if (Object.values(moves).some((arr) => arr.some((m) => m.docId === id))) moved.push(l);
  else staying.push(l);
}

if (staying.length + moved.length !== src.lessons.length) throw new Error("Incohérence de comptage");
if (moved.length !== 14) throw new Error(`Attendu 14 leçons à déplacer, trouvé ${moved.length}`);

src.lessons = staying;
console.log(`fiqh-1ep : ${staying.length + moved.length} → ${staying.length} leçons (30 attendues)`);
if (staying.length !== 30) throw new Error("fiqh-1ep devrait garder 30 leçons");

for (const [destId, list] of Object.entries(moves)) {
  const dest = load(destId);
  for (const m of list) {
    const l = moved.find((x) => String(x.docId) === m.docId);
    if (!l) throw new Error(`Leçon ${m.docId} introuvable dans fiqh-1ep`);
    if (m.titleFr) l.titleFr = m.titleFr;
    // retrait du préfixe livre du titleAr si présent (gardé tel quel sinon)
    dest.lessons.push(l);
    console.log(`  ${m.docId} → ${destId}${m.titleFr ? " (« " + m.titleFr + " »)" : ""}`);
  }
  // tri : leçons complètes par docId décroissant d'abord ? Non : ordre numérique croissant,
  // les pdfOnly (docIds synthétiques « pdf-N ») restent à leur place.
  dest.lessons.sort((a, b) => {
    const an = String(a.docId).startsWith("pdf-");
    const bn = String(b.docId).startsWith("pdf-");
    if (an !== bn) return an ? 1 : -1; // html d'abord, pdf ensuite
    return num(a.docId) - num(b.docId);
  });
  save(dest);
  console.log(`${destId} : ${dest.lessons.length} leçons`);
}

save(src);
console.log("✅ Grille corrigée — régénérer le manifeste : bun run scripts-recovery/regen-manifest.ts");
