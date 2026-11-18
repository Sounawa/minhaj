/**
 * Minhāj R8b — Nettoyage des stubs PDF : suppression boilerplates/couvertures,
 * révision manuelle des titres FR (convention académique R7).
 * Usage: bun run scripts-recovery/r8-fix-stubs.ts
 */
import { readFileSync, writeFileSync } from "fs";
import path from "path";

const BOOKS = path.join(process.cwd(), "content", "books");
const readBook = (id: string) => JSON.parse(readFileSync(path.join(BOOKS, id + ".json"), "utf-8"));
const writeBook = (j: any) => writeFileSync(path.join(BOOKS, j.id + ".json"), JSON.stringify(j, null, 1) + "\n", "utf-8");

// [bookId, docId, nouveau titreFr] — null = suppression
const FIXES: [string, string, string | null][] = [
  // ————— hadith-5ep (Arbaʿīn Nawawiyya)
  ["hadith-5ep", "pdf-1", "Présentation de l'auteur et de l'ouvrage"],
  ["hadith-5ep", "pdf-2", "Les actes ne valent que par les intentions"],
  ["hadith-5ep", "pdf-3", "L'islam et la foi (īmān)"],
  ["hadith-5ep", "pdf-4", "L'excellence (iḥsān) et les signes de l'Heure"],
  ["hadith-5ep", "pdf-5", "Les piliers de l'islam"],
  ["hadith-5ep", "pdf-6", "Les étapes de la création de l'homme"],
  ["hadith-5ep", "pdf-7", "Soutien et application"],
  ["hadith-5ep", "pdf-8", "Le décret et la prédestination (qaḍāʾ et qadar)"],
  ["hadith-5ep", "pdf-9", "Les innovations (bidʿa) dans la religion"],
  ["hadith-5ep", "pdf-10", "Le licite, l'illicite et le douteux"],
  ["hadith-5ep", "pdf-11", "La réforme du cœur"],
  ["hadith-5ep", "pdf-12", "La religion, c'est le conseil (naṣīḥa)"],
  ["hadith-5ep", "pdf-13", "La facilité de la religion islamique"],
  ["hadith-5ep", "pdf-14", "Soutien et application"],
  ["hadith-5ep", "pdf-15", "Le licite et l'exaucement de l'invocation"],
  ["hadith-5ep", "pdf-16", "La circonspection envers le douteux (waraʿ)"],
  ["hadith-5ep", "pdf-17", "Délaisser ce qui ne nous regarde pas"],
  ["hadith-5ep", "pdf-18", "Aimer le bien pour les gens"],
  ["hadith-5ep", "pdf-19", "Des qualités de la foi"],
  ["hadith-5ep", "pdf-20", "Soutien et application"],
  ["hadith-5ep", "pdf-21", "L'interdiction de la colère"],
  ["hadith-5ep", "pdf-22", "L'excellence (iḥsān) en toute chose"],
  ["hadith-5ep", "pdf-23", "La piété (taqwā) et le bon caractère"],
  ["hadith-5ep", "pdf-24", "Préserver les commandements de Dieu"],
  ["hadith-5ep", "pdf-25", "La pudeur fait partie de la foi"],
  ["hadith-5ep", "pdf-26", "La droiture (istiqāma)"],
  ["hadith-5ep", "pdf-27", "Ce qui mène au Paradis"],
  ["hadith-5ep", "pdf-28", "Soutien et application"],
  ["hadith-5ep", "pdf-29", "Liste des sources et références"],
  ["hadith-5ep", "pdf-30", null], // couverture du livre
  // ————— hadith-2es (Muwaṭṭaʾ, suite)
  ["hadith-2es", "pdf-1", null], // إضاءات منهجية (boilerplate)
  ["hadith-2es", "pdf-2", "Règles du raccourcissement et du regroupement des prières (voyage et séjour)"],
  ["hadith-2es", "pdf-4", "Des actes recommandés et bienséances de la prière"],
  ["hadith-2es", "pdf-5", "Se retourner, claquer des mains et parler pendant la prière"],
  ["hadith-2es", "pdf-6", "Ce qu'il faut faire ou délaisser dans la prière, obligatoire ou surérogatoire"],
  ["hadith-2es", "pdf-7", "Les règles des deux fêtes (ʿīd)"],
  ["hadith-2es", "pdf-8", "La prière de la peur, des éclipses solaire et lunaire"],
  ["hadith-2es", "pdf-9", "La prière de demande de pluie (istisqāʾ)"],
  ["hadith-2es", "pdf-10", "Règles de la qibla et mérite de la mosquée du Prophète ﷺ"],
  ["hadith-2es", "pdf-11", "Pureté pour toucher le Coran et prosternation de la récitation"],
  ["hadith-2es", "pdf-12", "Le mérite de l'évocation (dhikr) et de l'invocation"],
  ["hadith-2es", "pdf-13", "Statut de la prière après faḍr et ʿaṣr"],
  ["hadith-2es", "pdf-16", "La zakāt : notion et conditions"],
  ["hadith-2es", "pdf-17", "Zakāt des métaux, des bijoux et des biens des orphelins"],
  ["hadith-2es", "pdf-18", "Zakāt de l'héritage, des dettes et des marchandises"],
  ["hadith-2es", "pdf-19", "La zakāt du bétail"],
  ["hadith-2es", "pdf-20", "Zakāt du bétail en association (khalṭa)"],
  ["hadith-2es", "pdf-21", "Zakāt des fruits et des céréales"],
  ["hadith-2es", "pdf-22", "Biens exempts de zakāt et ayants droit"],
  ["hadith-2es", "pdf-27", "Jeûnes interdits, obligatoires et cas de dispense"],
  ["hadith-2es", "pdf-28", "Rattrapage et compensation (fiḍya) du jeûne"],
  ["hadith-2es", "pdf-29", "Mérite du jeûne ; vendredi et six jours de shawwāl"],
  ["hadith-2es", "pdf-30", "Index des figures citées"],
  ["hadith-2es", "pdf-32", null], // couverture
  // ————— fiqh-3es (Risāla, suite — transactions)
  ["fiqh-3es", "pdf-1", "Vente et usure (ribā) dans les aliments"],
  ["fiqh-3es", "pdf-2", "Les catégories d'aliments et leur vente avant prise de possession"],
  ["fiqh-3es", "pdf-3", "Vente à option (khayār) et vente invalide"],
  ["fiqh-3es", "pdf-4", "Règles du prêt (qarḍ) et certaines ventes proscrites"],
  ["fiqh-3es", "pdf-5", "Vente des fruits, de la chose absente et à terme (salam)"],
  ["fiqh-3es", "pdf-6", "Crédit à terme (kalīʾ bi-kalīʾ), ventes différées, à vue et sur description"],
  ["fiqh-3es", "pdf-7", "Règles du louage (ijāra), de l'entreprise (juʿāla) et de la location"],
  ["fiqh-3es", "pdf-8", "Règles de l'association (sharika) et certains de ses types"],
  ["fiqh-3es", "pdf-9", "Règles de l'irrigation partagée (musāqāt)"],
  ["fiqh-3es", "pdf-10", "Règles du bail à ferme (muzāraʿa)"],
  ["fiqh-3es", "pdf-11", "Droit de préemption (shufʿa) et libéralités"],
  ["fiqh-3es", "pdf-12", "Règles de l'immobilisation (ḥabs) et de la donation récompensée"],
  ["fiqh-3es", "pdf-13", "Règles du gage (rahn), du prêt à usage et du dépôt"],
  ["fiqh-3es", "pdf-14", "Règles de l'objet trouvé (luqaṭa) et de la spoliation (ghaṣb)"],
  ["fiqh-3es", "pdf-15", "Règles des jugements et des témoignages"],
  ["fiqh-3es", "pdf-16", "Témoins irrecevables et procédure d'attestation"],
  ["fiqh-3es", "pdf-17", "Témoignage des garçons et différend entre les contractants"],
  ["fiqh-3es", "pdf-18", "Règles du mandat (wakāla), de la transaction (ṣulḥ) et de la revendication"],
  ["fiqh-3es", "pdf-19", "Litiges fonciers et questions connexes"],
  ["fiqh-3es", "pdf-20", "Règles du transfert de dette (ḥawāla) et du partage"],
  ["fiqh-3es", "pdf-21", "Règles du legs (waṣiyya) et de la prise de possession"],
  ["fiqh-3es", "pdf-22", "Chapitre des successions (farāʾiḍ) et des bienséances"],
  ["fiqh-3es", "pdf-23", "Un ensemble de nobles caractères"],
  ["fiqh-3es", "pdf-24", "Les traits de la fitra et quelques bienséances"],
  ["fiqh-3es", "pdf-25", "Applications de questions juridiques"],
  ["fiqh-3es", "pdf-26", "Index et notices biographiques"],
];

async function main() {
  const byBook = new Map<string, { fixes: Map<string, string | null> }>();
  for (const [book, docId, title] of FIXES) {
    if (!byBook.has(book)) byBook.set(book, { fixes: new Map() });
    byBook.get(book)!.fixes.set(docId, title);
  }
  for (const [bookId, { fixes }] of byBook) {
    const b = readBook(bookId);
    let removed = 0, fixed = 0;
    const kept: any[] = [];
    for (const l of b.lessons || []) {
      if (fixes.get(String(l.docId)) === null) { removed++; continue; }
      const t = fixes.get(String(l.docId));
      if (typeof t === "string") { l.titleFr = t; fixed++; }
      kept.push(l);
    }
    b.lessons = kept;
    writeBook(b);
    console.log(`${bookId}: ${fixed} titres corrigés, ${removed} supprimés, ${kept.length} leçons`);
  }
}
main();
