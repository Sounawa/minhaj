/**
 * Minhāj R11 — Normalisation des titres FR de hadith-1ep
 * (fin des titres GT « La vertu de… » → convention savante « Le mérite de… »,
 * translittération DIN 31635 alignée sur R9/R10-e).
 */
import { readFileSync, writeFileSync } from "fs";
import path from "path";

const file = path.join(process.cwd(), "content/books/hadith-1ep.json");
const data = JSON.parse(readFileSync(file, "utf-8"));

const titles: Record<string, string> = {
  "12583": "Présentation du manuel",
  "12788": "Le mérite de la lecture du Noble Coran",
  "12792": "Le mérite des sourates al-Fātiḥa et al-Ikhlāṣ",
  "12797": "Le mérite de la lecture de la sourate al-Kahf",
  "12799": "Le mérite des deux sourates al-Muʿawwidhatayn",
  "12800": "Le mérite du verset du Trône (āyat al-kursī)",
  "12803": "Le mérite des derniers versets de la sourate al-Baqara",
  "12810": "Le mérite d'apprendre le Coran et de l'enseigner",
  "12811": "L'exhortation à entretenir la récitation du Coran",
  "12814": "Le mérite de la maîtrise dans la mémorisation du Noble Coran",
  "12816": "Embellir la voix par la récitation du Coran",
  "12818": "L'importance de l'écoute du Coran récité par autrui",
  "12822": "L'exhortation à réciter le Coran dans les demeures",
  "12827": "Le mérite de la réunion pour réciter le Coran et l'étudier",
  "12829": "L'effet du Coran sur son compagnon en ce bas-monde et dans l'au-delà",
  "12830": "Les états des gens dans leurs relations avec le Noble Coran",
  "12834": "La hiérarchie des gens selon leur relation au Noble Coran",
  "12840": "Le mérite de la quête du savoir",
  "12842": "Le mérite de la compréhension de la religion",
  "12845": "La sincérité (ikhlāṣ) dans la quête du savoir",
  "12846": "La fiabilité (amāna) dans la réception du savoir et sa transmission",
  "12847": "Le mérite du voyage dans la quête du savoir",
  "12849": "Le mérite de l'enseignement du savoir",
  "12850": "Le mérite de guider les gens par le savoir",
  "12853": "La noble compétition dans l'enseignement du savoir et de la sagesse",
  "12856": "Le mérite des savants",
  "12857": "Les états des gens dans le profit qu'ils tirent du savoir",
  "12859": "Les conséquences de la dissimulation du savoir",
  "12861": "La disparition du savoir (qabḍ al-ʿilm)",
  "12863": "Biographies des Compagnons — qu'Allah les agrée (aʿlām)",
  "12866": "Sources et références",
};

let n = 0;
for (const l of data.lessons ?? []) {
  if (titles[l.docId] && l.titleFr !== titles[l.docId]) {
    l.titleFr = titles[l.docId];
    n++;
  }
}
if (data.intro?.docId && titles[data.intro.docId]) {
  data.intro.titleFr = titles[data.intro.docId];
}
writeFileSync(file, JSON.stringify(data, null, 2) + "\n", "utf-8");
console.log(`✅ ${n} titres normalisés dans hadith-1ep.json`);
