/**
 * Minhāj — Moisson complète du CDX arquivo.pt pour habous.gov.ma (pagination).
 * Usage: bun run scripts-recovery/arquivo-harvest.ts
 */
import { writeFileSync, existsSync, readFileSync } from "fs";

const OUT = "/home/z/my-project/scripts-recovery/arquivo-all.jsonl";
const results: string[] = [];
let seen = new Set<string>();

// Fenêtres temporelles (le CDX plafonne à ~2000 lignes par requête)
const windows = [
  ["2018", "2019"],
  ["2019", "2020"],
  ["2020", "2021"],
  ["2021", "2022"],
  ["2022", "2023"],
  ["2023", "2024"],
  ["2024", "2025"],
  ["2025", "2027"],
];

for (const [from, to] of windows) {
  const url = `https://arquivo.pt/wayback/cdx?url=habous.gov.ma*&output=json&limit=10000&from=${from}&to=${to}`;
  try {
    const res = await fetch(url, { headers: { "Accept": "application/json" } });
    if (!res.ok) {
      console.log(`✗ ${from}-${to}: HTTP ${res.status}`);
      continue;
    }
    const text = await res.text();
    const lines = text.split("\n").filter((l) => l.trim().startsWith("{"));
    let added = 0;
    for (const l of lines) {
      try {
        const j = JSON.parse(l);
        const key = j.url + "|" + j.timestamp;
        if (!seen.has(key)) {
          seen.add(key);
          results.push(l);
          added++;
        }
      } catch {
        /* ignore */
      }
    }
    console.log(`✓ ${from}–${to}: ${lines.length} lignes, ${added} nouvelles (total ${results.length})`);
  } catch (e) {
    console.log(`✗ ${from}-${to}: ${e instanceof Error ? e.message : e}`);
  }
}

writeFileSync(OUT, results.join("\n") + "\n", "utf-8");
console.log(`\n✅ ${results.length} captures uniques → ${OUT}`);

// Analyse : URLs de la section التعليم العتيق
const atieq = results.filter((l) => {
  try {
    const u = JSON.parse(l).url as string;
    return decodeURIComponent(u).includes("التعليم-العتيق") || decodeURIComponent(u).includes("التعليم العتيق");
  } catch {
    return false;
  }
});
console.log(`\nCaptures de la section « التعليم العتيق » : ${atieq.length}`);
for (const l of atieq.slice(0, 30)) {
  const j = JSON.parse(l);
  console.log("  ", j.timestamp.slice(0, 8), decodeURIComponent(j.url).slice(0, 120));
}
