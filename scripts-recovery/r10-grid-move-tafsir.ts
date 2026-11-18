/**
 * Minhāj R10 — Correction de grille (3) : tafsir.
 * tafsir-1ep (4ep, Fātiḥa + qṣār al-suwar) contenait 30 documents d'AUTRES livres :
 *  - 12609 : taqdīm officielle du manuel 5ep (Ḥizb 59) → tafsir-5ep
 *  - 13897, 13907, 13915, 13920, 13931, 13936, 13979, 13983, 13992, 14005, 14018,
 *    14042, 14052, 14063, 14067, 16227, 16711, 16714, 16717, 16719, 16724, 16733,
 *    16737, 16739, 16743, 16751, 16757, 16767, 16784 : leçons Ḥizb 59 (Infiṭār→Ṭāriq,
 *    Nabaʾ, Nāziʿāt, ʿAbasa, Takwīr) + annexes → tafsir-5ep
 * Preuve : la taqdīm 12609 liste exactement ce sommaire (Nabaʾ×3, Nāziʿāt×4, ʿAbasa×4,
 * Takwīr×3, Infiṭār×2, Muṭaffifīn×4, Inshiqāq×3, Burūj×3, Ṭāriq×2, aʿlām, maṣādir).
 * Fix : 16743 titré « ʿAbasa 1-10 » est en réalité ʿAbasa 11-23 (h1 du contenu).
 * Restent dans tafsir-1ep : 27 leçons 4ep + annexes 13621/13622 = 29.
 * Usage: bun run scripts-recovery/r10-grid-move-tafsir.ts
 */
import { readFileSync, writeFileSync } from "fs";
import path from "path";

const BOOKS = path.join(process.cwd(), "content", "books");
const load = (id: string): any => JSON.parse(readFileSync(path.join(BOOKS, id + ".json"), "utf8"));
const save = (b: any) => writeFileSync(path.join(BOOKS, b.id + ".json"), JSON.stringify(b, null, 1) + "\n");
const num = (s: string | number) => Number(String(s).replace(/\D/g, "")) || 0;

const moves: { docId: string; titleFr?: string; titleAr?: string }[] = [
  { docId: "12609", titleFr: "Préface du manuel (taqdīm)" },
  { docId: "16711", titleFr: "Sourate al-Nabaʾ, versets 1 à 16" },
  { docId: "16714", titleFr: "Sourate al-Nabaʾ, versets 17 à 30" },
  { docId: "16717", titleFr: "Sourate al-Nabaʾ, versets 31 à 40" },
  { docId: "16719", titleFr: "Sourate al-Nāziʿāt, versets 1 à 14" },
  { docId: "16724", titleFr: "Sourate al-Nāziʿāt, versets 15 à 26" },
  { docId: "16733", titleFr: "Sourate al-Nāziʿāt, versets 27 à 33" },
  { docId: "16737", titleFr: "Sourate al-Nāziʿāt, versets 34 à 45" },
  { docId: "16739", titleFr: "Sourate ʿAbasa, versets 1 à 10" },
  { docId: "16743", titleFr: "Sourate ʿAbasa, versets 11 à 23", titleAr: "سورة عبس الآيات من 11 إلى 23" },
  { docId: "16751", titleFr: "Sourate ʿAbasa, versets 24 à 32" },
  { docId: "16757", titleFr: "Sourate ʿAbasa, versets 33 à 42" },
  { docId: "16767", titleFr: "Sourate al-Takwīr, versets 1 à 14" },
  { docId: "16784", titleFr: "Sourate al-Takwīr, versets 15 à 21" },
  { docId: "16227", titleFr: "Sourate al-Takwīr, versets 22 à 29" },
  { docId: "13897", titleFr: "Sourate al-Infiṭār, versets 9 à 19" },
  { docId: "13907", titleFr: "Sourate al-Muṭaffifīn, versets 1 à 6" },
  { docId: "13915", titleFr: "Sourate al-Muṭaffifīn, versets 7 à 17" },
  { docId: "13920", titleFr: "Sourate al-Muṭaffifīn, versets 18 à 28" },
  { docId: "13931", titleFr: "Sourate al-Muṭaffifīn, versets 29 à 36" },
  { docId: "13936", titleFr: "Sourate al-Inshiqāq, versets 1 à 9" },
  { docId: "13979", titleFr: "Sourate al-Inshiqāq, versets 10 à 15" },
  { docId: "13983", titleFr: "Sourate al-Inshiqāq, versets 16 à 25" },
  { docId: "13992", titleFr: "Sourate al-Burūj, versets 1 à 9" },
  { docId: "14005", titleFr: "Sourate al-Burūj, versets 10 à 16" },
  { docId: "14018", titleFr: "Sourate al-Burūj, versets 17 à 22" },
  { docId: "14042", titleFr: "Sourate al-Ṭāriq, versets 1 à 10" },
  { docId: "14052", titleFr: "Sourate al-Ṭāriq, versets 11 à 17" },
  { docId: "14063", titleFr: "Personnalités citées (aʿlām)" },
  { docId: "14067", titleFr: "Sources et références" },
];

const src = load("tafsir-1ep");
const dest = load("tafsir-5ep");
const ids = new Set(moves.map((m) => m.docId));
const moved = src.lessons.filter((l: any) => ids.has(String(l.docId)));
if (moved.length !== 30) throw new Error(`Attendu 30, trouvé ${moved.length}`);
for (const m of moves) {
  const l = moved.find((x: any) => String(x.docId) === m.docId);
  if (m.titleFr) l.titleFr = m.titleFr;
  if (m.titleAr) l.titleAr = m.titleAr;
}
src.lessons = src.lessons.filter((l: any) => !ids.has(String(l.docId)));
dest.lessons.push(...moved);
// tri tafsir-5ep : taqdīm en tête, puis html par docId, puis pdf synthétiques
dest.lessons.sort((a: any, b: any) => {
  const ap = String(a.docId) === "12609" ? 0 : String(a.docId).startsWith("pdf-") ? 2 : 1;
  const bp = String(b.docId) === "12609" ? 0 : String(b.docId).startsWith("pdf-") ? 2 : 1;
  return ap !== bp ? ap - bp : num(a.docId) - num(b.docId);
});
save(src); save(dest);
console.log(`tafsir-1ep : 59 → ${src.lessons.length} leçons (29 attendues)`);
console.log(`tafsir-5ep : ${dest.lessons.length} leçons (dont pdf ${dest.lessons.filter((l: any) => l.pdfOnly).length})`);
console.log("✅ Grille tafsīr corrigée — régénérer le manifeste");
