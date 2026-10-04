/**
 * Génère content/manifest.json — structure du programme Taʿlīm ʿatīq
 * (منهاج نموذجي للتعليم العتيق — ministère des Habous, Maroc).
 *
 * NOTE: manifeste PROVISOIRE reconstruit après la réinitialisation du sandbox.
 * Les bookId connus (issus des sessions précédentes) sont marqués "known".
 * Ce manifeste sera corrigé/définalisé par le re-téléchargement du corpus
 * officiel (scripts-recovery/discover-source.ts) dès que le SDK sera disponible.
 *
 * Usage: bun run scripts-recovery/gen-manifest.ts
 */
import { writeFileSync, mkdirSync } from "fs";
import path from "path";

interface Level { id: string; cycle: "ep" | "es" | "tanawi"; year: number; labelAr: string; labelFr: string; shortFr: string; }
interface Subject { id: string; labelAr: string; titleFr: string; translit: string; icon: string; }
interface Book { id: string; subject: string; level: string; titleAr: string; titleFr: string; order: number; known?: boolean; textbookAr?: string; }

const levels: Level[] = [];
const epLabels: Record<number, [string, string, string]> = {
  1: ["السنة الأولى من السلك الابتدائي العتيق", "1ʳᵉ année — primaire", "1ʳᵉ primaire"],
  2: ["السنة الثانية من السلك الابتدائي العتيق", "2ᵉ année — primaire", "2ᵉ primaire"],
  3: ["السنة الثالثة من السلك الابتدائي العتيق", "3ᵉ année — primaire", "3ᵉ primaire"],
  4: ["السنة الرابعة من السلك الابتدائي العتيق", "4ᵉ année — primaire", "4ᵉ primaire"],
  5: ["السنة الخامسة من السلك الابتدائي العتيق", "5ᵉ année — primaire", "5ᵉ primaire"],
  6: ["السنة السادسة من السلك الابتدائي العتيق", "6ᵉ année — primaire", "6ᵉ primaire"],
};
for (let y = 1; y <= 6; y++) {
  levels.push({ id: `${y}ep`, cycle: "ep", year: y, labelAr: epLabels[y][0], labelFr: epLabels[y][1], shortFr: epLabels[y][2] });
}
const esLabels: Record<number, [string, string, string]> = {
  1: ["السنة الأولى من السلك الإعدادي العتيق", "1ʳᵉ année — collège", "1ᵉʳ collège"],
  2: ["السنة الثانية من السلك الإعدادي العتيق", "2ᵉ année — collège", "2ᵉ collège"],
  3: ["السنة الثالثة من السلك الإعدادي العتيق", "3ᵉ année — collège", "3ᵉ collège"],
};
for (let y = 1; y <= 3; y++) {
  levels.push({ id: `${y}es`, cycle: "es", year: y, labelAr: esLabels[y][0], labelFr: esLabels[y][1], shortFr: esLabels[y][2] });
}
const tnLabels: Record<number, [string, string, string]> = {
  1: ["السنة الأولى من السلك التأهيلي العتيق", "1ʳᵉ année — lycée", "1ᵉʳ lycée"],
  2: ["السنة الثانية من السلك التأهيلي العتيق", "2ᵉ année — lycée", "2ᵉ lycée"],
  3: ["السنة الثالثة من السلك التأهيلي العتيق", "3ᵉ année — lycée", "3ᵉ lycée"],
};
for (let y = 1; y <= 3; y++) {
  levels.push({ id: `tanawi-${y}`, cycle: "tanawi", year: y, labelAr: tnLabels[y][0], labelFr: tnLabels[y][1], shortFr: tnLabels[y][2] });
}

const subjects: Subject[] = [
  { id: "tawhid", labelAr: "التوحيد", titleFr: "Le Monothéisme", translit: "tawḥīd", icon: "Sparkles" },
  { id: "fiqh", labelAr: "الفقه", titleFr: "Le Droit rituel", translit: "fiqh", icon: "Scale" },
  { id: "sira", labelAr: "السيرة النبوية", titleFr: "La Biographie prophétique", translit: "sīra", icon: "ScrollText" },
  { id: "tajwid", labelAr: "التجويد", titleFr: "La Psalmodie coranique", translit: "tajwīd", icon: "AudioLines" },
  { id: "tafsir", labelAr: "التفسير", titleFr: "L'Exégèse coranique", translit: "tafsīr", icon: "BookOpenText" },
  { id: "nahu", labelAr: "النحو والصرف", titleFr: "La Grammaire et la morphologie", translit: "naḥw wa ṣarf", icon: "Languages" },
  { id: "hadith", labelAr: "الحديث", titleFr: "La Tradition prophétique", translit: "ḥadīth", icon: "MessagesSquare" },
  { id: "mantiq", labelAr: "المنطق", titleFr: "La Logique", translit: "manṭiq", icon: "Brain" },
  { id: "faraid", labelAr: "الفرائض", titleFr: "Le Droit successoral", translit: "farāʾiḍ", icon: "Landmark" },
  { id: "balagha", labelAr: "البلاغة", titleFr: "La Rhétorique", translit: "balāġa", icon: "Feather" },
  { id: "usul-fiqh", labelAr: "أصول الفقه", titleFr: "Les Principes du droit", translit: "uṣūl al-fiqh", icon: "Compass" },
  { id: "adab", labelAr: "الأدب", titleFr: "La Littérature", translit: "adab", icon: "Library" },
];

const subjectById = Object.fromEntries(subjects.map((s) => [s.id, s]));
const books: Book[] = [];
let order = 0;
const push = (id: string, subject: string, level: string, opts: { known?: boolean; textbookAr?: string } = {}) => {
  const s = subjectById[subject];
  if (!s) throw new Error(`Sujet inconnu: ${subject}`);
  books.push({ id, subject, level, titleAr: s.labelAr, titleFr: s.titleFr, order: ++order, ...(opts.known ? { known: true } : {}), ...(opts.textbookAr ? { textbookAr: opts.textbookAr } : {}) });
};

// ————— السلك الابتدائي العتيق (primaire : 6 niveaux × 5 matières = 30)
const epSubjects = ["tawhid", "fiqh", "sira", "tajwid", "tafsir"] as const;
for (let y = 1; y <= 6; y++) {
  const lvl = `${y}ep`;
  for (const subj of epSubjects) {
    let id: string;
    const opts: { known?: boolean; textbookAr?: string } = {};
    if (y === 1 && subj === "tawhid") { id = "tawhid"; opts.known = true; }
    else if (y === 1 && subj === "sira") { id = "sira-1ep"; opts.known = true; }
    else if (y === 1 && subj === "tafsir") { id = "tafsir-tashil-1ep"; opts.known = true; }
    else if (y === 1 && subj === "tajwid") { id = "tajwid-durar-lawami-1ep"; opts.known = true; opts.textbookAr = "الدرر اللوامع في تجويد كلام الله"; }
    else if (subj === "tajwid") { id = `tajwid-ibtidai-${y}`; if (y === 5) opts.known = true; }
    else { id = `${subj}-${y}ep`; }
    push(id, subj, lvl, opts);
  }
}

// ————— السلك الإعدادي العتيق (collège : 3 niveaux × 6 matières = 18)
const esSubjects = ["tawhid", "fiqh", "sira", "tajwid", "tafsir", "nahu"] as const;
for (let y = 1; y <= 3; y++) {
  const lvl = `${y}es`;
  for (const subj of esSubjects) {
    let id: string;
    if (y === 1 && subj === "tafsir") { id = "tafsir-muharrar-1es"; push(id, subj, lvl, { known: true }); continue; }
    id = `${subj}-${y}es`;
    push(id, subj, lvl);
  }
}

// ————— السلك التأهيلي العتيق (lycée : 16 manuels)
push("tawhid-tanawi-1", "tawhid", "tanawi-1");
push("fiqh-tanawi-1", "fiqh", "tanawi-1");
push("tafsir-tanawi-1", "tafsir", "tanawi-1");
push("mantiq-tanawi-1", "mantiq", "tanawi-1", { known: true });
push("hadith-tanawi-1", "hadith", "tanawi-1");
push("tawhid-tanawi-2", "tawhid", "tanawi-2");
push("fiqh-tanawi-2", "fiqh", "tanawi-2");
push("tafsir-tanawi-2", "tafsir", "tanawi-2");
push("faraid-tanawi-2", "faraid", "tanawi-2", { known: true });
push("hadith-tanawi-2", "hadith", "tanawi-2");
push("tawhid-tanawi-3", "tawhid", "tanawi-3");
push("fiqh-tanawi-3", "fiqh", "tanawi-3");
push("tafsir-tanawi-3", "tafsir", "tanawi-3");
push("faraid-tanawi-3", "faraid", "tanawi-3");
push("usul-fiqh-tanawi-3", "usul-fiqh", "tanawi-3");
push("adab-tanawi-3", "adab", "tanawi-3");

const manifest = {
  version: 3,
  provisional: true,
  note: "Manifeste reconstruit après réinitialisation du sandbox (session R0). Structure provisoire du programme Taʿlīm ʿatīq — à corriger lors du re-téléchargement du corpus officiel. Les bookId marqués « known » sont ceux attestés dans les sessions précédentes.",
  program: {
    nameAr: "المنهاج النموذجي للتعليم العتيق",
    nameFr: "Programme modèle de l'enseignement traditionnel (Taʿlīm ʿatīq)",
    publisherAr: "وزارة الأوقاف والشؤون الإسلامية — المملكة المغربية",
    publisherFr: "Ministère des Habous et des Affaires islamiques — Royaume du Maroc",
    goalBooks: 64,
    goalDocs: 1152,
  },
  levels,
  subjects,
  books,
};

const outDir = path.join(process.cwd(), "content");
mkdirSync(outDir, { recursive: true });
const outPath = path.join(outDir, "manifest.json");
writeFileSync(outPath, JSON.stringify(manifest, null, 2) + "\n", "utf-8");

const known = books.filter((b) => b.known).map((b) => b.id);
console.log(`✅ manifest.json généré : ${books.length} livres, ${levels.length} niveaux, ${subjects.length} matières`);
console.log(`   bookId connus (${known.length}) : ${known.join(", ")}`);
