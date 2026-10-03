/**
 * fix-long-titles.ts — Tronque le boilerplate GT des titres de leçons.
 * « Les ablutions et leurs règlements, suite de la jurisprudence du texte
 *   d'Al-Akhdari, expliquée par Al-Abi Al-Azhari, pour la quatrième année… »
 *   → « Les ablutions et leurs règlements (suite) »
 *
 * Usage : bun scripts-recovery/fix-long-titles.ts [--dry]
 */
import * as fs from "fs";
import * as path from "path";

const ROOT = path.join(import.meta.dir, "..");
const BOOKS = path.join(ROOT, "content", "books");
const DRY = process.argv.includes("--dry");

// Marqueurs de début de boilerplate (dans l'ordre de test).
const MARKERS: RegExp[] = [
  // « X, suite de la jurisprudence… » → X (suite)
  /,?\s*suite de (?:la |du |l')/i,
  // « X, une leçon de … » / « X : une leçon… »
  /[:,]?\s*(?:une |la )?le[çc]on de /i,
  // « X, jurisprudence tirée du texte… »
  /,?\s*jurisprudence /i,
  // « X : Le livre de… »
  /:\s*(?:le|la|un) livre /i,
  // « X Jurisprudence du texte… » (collé sans virgule)
  /\s+Jurisprudence du texte/i,
  // « X Interprétation à travers… »
  /\s+Interpr[ée]tation /i,
  // « X, hadith de… » (hadith boilerplate)
  /,?\s*hadith (?:de|du|tir[ée])/i,
  // « X, tafsir du texte… »
  /,?\s*tafs[ie]r (?:de|du|tir[ée])/i,
  // « X, pour la Nième année… »
  /,?\s*pour la (?:premi[èe]re|deuxi[èe]me|troisi[èe]me|quatri[èe]me|cinqui[èe]me|sixi[èe]me)/i,
  // « X à travers Tafsir/le … »
  /\s+[àa] travers (?:le |la |Tafsir|tafsir|l')/i,
  // « X du texte du message/résumé… »
  /,?\s*(?:du|de) texte du /i,
  // « X est un texte / une leçon… »
  /,?\s*est (?:un|une) (?:texte|le[çc]on)/i,
  // « X, avec une explication… »
  /,?\s*avec une explication/i,
  // « X est le texte du résumé… » / « X. Texte du résumé… » / « X, d'après le texte… »
  /,?\s*est le texte du|[.:]\s*Texte du|,?\s*d'apr[èe]s le texte/i,
  // Mantiq : « X : la logique de Nazm / est issue / des systèmes… »
  /[:,]?\s*(?:la |La )?logique (?:de Nazm|d'|est issue|est tir[ée]e|des syst[èe]mes|issue des)/i,
  // « X, jurisprudence, d'après… » (2e vague)
  /,?\s*jurisprudence,?\s+d'apr[èe]s/i,
  // « X à travers Arjouza… » / « X. Arjouza Umdat… »
  /\s+[àa] travers Arjouza|[.,]\s*Arjouza Umdat/i,
  // « X, un résumé de… »
  /,?\s*un r[ée]sum[ée] de/i,
];

function truncate(title: string): { title: string; cut: boolean } {
  let best: { idx: number; suite: boolean } | null = null;
  for (const re of MARKERS) {
    const m = re.exec(title);
    if (m && m.index > 8) {
      // garde-fou : ne pas couper avant 8 caractères
      if (!best || m.index < best.idx) {
        best = { idx: m.index, suite: /suite/i.test(m[0]) };
      }
    }
  }
  if (!best) return { title, cut: false };
  let out = title.slice(0, best.idx).replace(/[\s,:;·—-]+$/u, "").trim();
  if (best.suite) {
    if (!/\(suite\)$/i.test(out)) out += " (suite)";
  }
  return { title: out, cut: true };
}

let files = fs.readdirSync(BOOKS).filter((f) => f.endsWith(".json"));
let total = 0, changed = 0, skipped = 0;
const samples: string[] = [];

for (const f of files) {
  const p = path.join(BOOKS, f);
  const book = JSON.parse(fs.readFileSync(p, "utf8"));
  let touched = false;
  for (const l of book.lessons ?? []) {
    total++;
    const t = l.titleFr || "";
    if (t.length < 100) continue; // seuls les longs titres GT
    const { title, cut } = truncate(t);
    if (!cut || title.length < 10) {
      skipped++;
      if (samples.length < 12 && !cut && t.length > 130)
        samples.push(`NON-CUT ${f} ${l.docId} : ${t.slice(0, 100)}`);
      continue;
    }
    if (samples.length < 14) samples.push(`${t.slice(0, 44)}…  →  ${title}`);
    l.titleFr = title;
    changed++;
    touched = true;
  }
  if (touched && !DRY) fs.writeFileSync(p, JSON.stringify(book, null, 1) + "\n");
}

console.log(`Leçons: ${total} | tronquées: ${changed} | longues non coupées: ${skipped}`);
console.log("\n— Échantillon —");
samples.forEach((s) => console.log("  " + s));
if (DRY) console.log("\n[dry] aucun fichier modifié");
