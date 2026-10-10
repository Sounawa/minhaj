/**
 * Minhāj — Cache coranique local (une seule exécution nécessaire).
 * Récupère les 114 sourates : texte arabe (uthmani) + traduction française
 * de référence (M. Hamidullah) via api.alquran.cloud, puis les stocke dans
 * scripts-translate/quran-cache.json pour une injection fidèle dans le
 * pipeline llm-translate.ts (aucune génération de versets « de mémoire »).
 *
 * Usage : bun run scripts-translate/quran-cache.ts
 */
import { writeFileSync } from "fs";
import path from "path";

const OUT = path.join(process.cwd(), "scripts-translate", "quran-cache.json");
const CONC = 6;
const jobs: number[] = Array.from({ length: 114 }, (_, i) => i + 1);
const results: Record<string, any> = {};
let done = 0;

// La basmala est préfixée au verset 1 de chaque sourate (sauf 1 et 9) dans
// l'édition uthmani — on la retire pour ne pas polluer les fenêtres injectées.
const AR_BASMALA = /^بِسْمِ\s*ٱللَّهِ\s*ٱلرَّحْمَٰنِ\s*ٱلرَّحِيمِ\s*/;
const FR_BASMALA = /^Au nom d'Allah[^.]*Miséricordieux\.?\s*/i;

async function fetchSurah(n: number): Promise<void> {
  for (let attempt = 1; attempt <= 5; attempt++) {
    try {
      const r = await fetch(`https://api.alquran.cloud/v1/surah/${n}/editions/quran-uthmani,fr.hamidullah`, { signal: AbortSignal.timeout(30_000) });
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      const j = await r.json();
      const [ar, fr] = j.data as any[];
      if (!ar?.ayahs?.length || !fr?.ayahs?.length) throw new Error("payload vide");
      const strip = (t: string, re: RegExp) => (n === 1 || n === 9 ? t : t.replace(re, ""));
      results[n] = {
        number: n,
        englishName: ar.englishName,
        nAyahs: ar.numberOfAyahs,
        ar: ar.ayahs.map((a: any) => [a.numberInSurah, strip(String(a.text), AR_BASMALA)]),
        fr: fr.ayahs.map((a: any) => [a.numberInSurah, strip(String(a.text), FR_BASMALA)]),
      };
      done++;
      if (done % 12 === 0) console.log(`  ${done}/114 sourates`);
      return;
    } catch (e: any) {
      if (attempt === 5) { console.error(`✗ sourate ${n} : ${e?.message ?? e}`); return; }
      await new Promise((r) => setTimeout(r, 1500 * attempt));
    }
  }
}

async function worker() {
  while (jobs.length) { const n = jobs.shift()!; await fetchSurah(n); }
}

(async () => {
  console.log("Téléchargement du Coran (uthmani + Hamidullah)…");
  await Promise.all(Array.from({ length: CONC }, worker));
  const ok = Object.keys(results).length;
  writeFileSync(OUT, JSON.stringify(results), "utf-8");
  console.log(`✓ ${ok}/114 sourates → ${OUT}`);
  if (ok < 114) { console.error("✗ Cache INCOMPLET — relancer le script."); process.exit(1); }
})();
