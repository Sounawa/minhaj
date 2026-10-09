/**
 * Minhāj — Pipeline de traduction savante AR→FR par LLM (GLM via z-ai-web-dev-sdk). v2
 *
 * Améliorations v2 (après QA du test 16743) :
 *   - EXEMPLE APPARIÉ AR→FR codé en dur (versets réintégrés + glossaire terme/glose)
 *   - PASSE DE RELECTURE OBLIGATOIRE (2ᵉ appel : source + traduction + liste de contrôle)
 *   - VALIDATIONS renforcées : versets réellement cités, guillemets français exclusifs,
 *     <li> orphelins, <li> vides, ratio, arabes, GT-ismes
 *
 * Usage :
 *   bun run scripts-translate/llm-translate.ts --plan
 *   bun run scripts-translate/llm-translate.ts --doc 16743 [--force] [--thinking]
 *   bun run scripts-translate/llm-translate.ts --book tafsir-5ep [--limit N] [--thinking]
 */
import { existsSync, mkdirSync, readFileSync, writeFileSync, readdirSync } from "fs";
import { execSync, spawnSync } from "child_process";
import path from "path";

const CONTENT = path.join(process.cwd(), "content");
const TR_OUT = "/home/z/tr-out";
const REGISTRY_PATH = path.join(process.cwd(), "scripts-translate", "savant-registry.json");

// ─────────────────────────────────────────────────────────────────────────────
// CLI
// ─────────────────────────────────────────────────────────────────────────────
const args = process.argv.slice(2);
const flag = (name: string) => {
  const i = args.indexOf(`--${name}`);
  return i === -1 ? null : args[i + 1];
};
const FORCE = args.includes("--force");
const THINKING = args.includes("--thinking");
const mode = args.includes("--plan") ? "plan" : args.includes("--doc") ? "doc" : args.includes("--book") ? "book" : null;
if (!mode) {
  console.error("Usage: bun run scripts-translate/llm-translate.ts --plan | --doc <docId> | --book <bookId> [--limit N] [--force] [--thinking]");
  process.exit(1);
}
const limit = flag("limit") ? parseInt(flag("limit")!, 10) : Infinity;

// ─────────────────────────────────────────────────────────────────────────────
// Registre
// ─────────────────────────────────────────────────────────────────────────────
type Registry = { hand: string[]; llm: Record<string, { at: string; bookId: string; titleFr: string }> };
const registry: Registry = existsSync(REGISTRY_PATH)
  ? JSON.parse(readFileSync(REGISTRY_PATH, "utf-8"))
  : { hand: [], llm: {} };
const saveRegistry = () => writeFileSync(REGISTRY_PATH, JSON.stringify(registry, null, 2) + "\n", "utf-8");
const isSavant = (docId: string) => registry.hand.includes(docId) || docId in registry.llm;

// ─────────────────────────────────────────────────────────────────────────────
// Corpus
// ─────────────────────────────────────────────────────────────────────────────
interface Target {
  docId: string; bookId: string; kind: "intro" | "lesson";
  titleAr: string; titleFr: string; html: string; index: number; total: number;
}
function loadBook(bookId: string): any {
  const p = path.join(CONTENT, "books", `${bookId}.json`);
  if (!existsSync(p)) throw new Error(`Livre introuvable : ${p}`);
  return JSON.parse(readFileSync(p, "utf-8"));
}
function targetsOfBook(bookId: string): Target[] {
  const data = loadBook(bookId);
  const out: Target[] = [];
  const total = (data.lessons ?? []).filter((l: any) => l.html && !l.pdfOnly).length;
  let pos = 0;
  for (const l of data.lessons ?? []) {
    if (!l.html || l.pdfOnly) continue;
    pos++;
    if (isSavant(String(l.docId))) continue;
    out.push({ docId: String(l.docId), bookId, kind: "lesson", titleAr: l.titleAr ?? "", titleFr: l.titleFr ?? "", html: l.html, index: pos, total });
  }
  if (data.intro?.html && !data.intro.pdfOnly && !isSavant(String(data.intro.docId))) {
    out.unshift({ docId: String(data.intro.docId), bookId, kind: "intro", titleAr: data.intro.titleAr ?? "", titleFr: data.intro.titleFr ?? "", html: data.intro.html, index: 0, total });
  }
  return out;
}

// ─────────────────────────────────────────────────────────────────────────────
// Exemple apparié AR→FR (leçon de référence 16739, traduction manuelle R14)
// ─────────────────────────────────────────────────────────────────────────────
const PAIRED_EXAMPLE = `EXEMPLE APPARIÉ — SOURCE ARABE (extrait) :
<h2>الآيات</h2>
 <p><span></span></p>
 <p><span>سورة عبس: 1 - 10</span></p>
 <h2>الفهم</h2>
 <h3>الشرح</h3>
 <p></p>
 <p>كَلَحَ وَجْهُهُ.</p>
 <p></p>
 <p>أَعْرَضَ.</p>
 <p></p>
 <p>يُعْلِمُكَ.</p>

EXEMPLE APPARIÉ — TRADUCTION FRANÇAISE ATTENDUE :
<h2>Les versets</h2>
<p>« Il s'est renfrogné et il s'est détourné, (1) parce que l'aveugle est venu à lui. (2) Et qu'est-ce qui te fait savoir qu'il se purifierait, (3) ou qu'il se rappellerait et que le rappel lui profiterait ? (4) Quant à celui qui se passe [de toi], (5) c'est à lui que tu t'appliques, (6) et il ne t'incombe pas qu'il ne se purifie pas ; (7) et quant à celui qui est venu à toi en s'empressant, (8) lui qui craint, (9) c'est lui que tu délaisses. » (ʿAbasa, 1-10)</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<ul>
<li>ʿAbasa (il s'est renfrogné) : son visage s'est durci.</li>
<li>Tawallā (il s'est détourné) : il a tourné le dos.</li>
<li>Yudrīka (il te fait savoir) : il t'apprend.</li>
</ul>

→ OBSERVE : (a) la balise <p><span></span></p> de la section des versets est une IMAGE PERDUE : on rétablit le TEXTE INTÉGRAL des versets en français entre « », suivi de (Sourate, versets). (b) chaque paire « <p></p> (terme en image) + <p>glose</p> » du glossaire devient une entrée « Terme translittéré (glose littérale) : définition ». (c) dans le commentaire (tafsīr), le source alterne fragments de versets (balises vides) et gloses : traduis chaque fragment entre « », puis la glose après un tiret — jamais de « c'est-à-dire » orphelin sans le fragment qu'il explique.`;

// ─────────────────────────────────────────────────────────────────────────────
// Pré-remplissage des versets (les images perdues ne contiennent rien — le texte
// coranique est produit séparément puis injecté dans la consigne de traduction)
// ─────────────────────────────────────────────────────────────────────────────
function extractVerseRef(srcHtml: string, titleFr: string): { sourateFr: string; from: number; to: number } | null {
  // Référence dans le span de la section الآيات : « سورة عبس: 11 - 23 »
  const secMatch = srcHtml.match(/<h2>\s*الآيات[\s\S]{0,600}?<span>\s*([^<]*\d+\s*[–-]\s*\d+[^<]*)\s*<\/span>/);
  const refRaw = secMatch?.[1] ?? "";
  const range = refRaw.match(/(\d+)\s*[–-]\s*(\d+)/);
  if (!range) return null;
  // Nom de sourate en français depuis le titre officiel « Sourate X, versets … »
  const t = titleFr.match(/^Sourate\s+(.+?),?\s+versets/i) || titleFr.match(/^Sourate\s+([^,]+)/i);
  if (!t) return null;
  return { sourateFr: t[1].trim(), from: parseInt(range[1], 10), to: parseInt(range[2], 10) };
}

async function prefillVerses(ref: { sourateFr: string; from: number; to: number }): Promise<string> {
  return callLLM([
    { role: "assistant", content: "Tu es un traducteur savant du Coran vers le français, registre liturgique sobre et académique (traduction des sens, style éditorial français classique)." },
    { role: "user", content: `Traduis en français les versets ${ref.from} à ${ref.to} de la sourate ${ref.sourateFr} (numérotation standard du muṣḥaf). Mets chaque numéro de verset entre parenthèses après son verset : (1) (2)… Sans aucun commentaire, sans titre : uniquement la traduction suivie des numéros.` },
  ]);
}

// ─────────────────────────────────────────────────────────────────────────────
// Prompt système v2
// ─────────────────────────────────────────────────────────────────────────────
const SYSTEM_PROMPT = `Tu es un traducteur savant de l'arabe vers le français, spécialiste des sciences islamiques (fiqh malikite, tafsīr, ḥadīth, tajwīd, qirāʾāt, uṣūl al-fiqh, sīra) et de la littérature pédagogique marocaine. Tu traduis les leçons du programme officiel « Taʿlīm ʿatīq » du ministère marocain des Habous pour la web app Minhāj. La qualité exigée est celle d'une édition académique publiée.

RÈGLES DE TRADUCTION (conventions éditoriales Minhāj) :

1. PÉRIMÈTRE — Traduis UNIQUEMENT le corps de la leçon, du <h1> jusqu'à la fin de la dernière section pédagogique (الإعداد القبلي / الاستثمار / التقويم). JETTE tout le reste : tableaux de grille (المرحلة، الكفايات، التوزيع)، navigation du site, pied de page du ministère (وزارة الأوقاف، المشور السعيد، الرباط، الهاتف), réseaux sociaux.

2. RÈGLE DES BALISES VIDES (LA PLUS IMPORTANTE) — Les balises <p></p>, <p><span></span></p> ou <p>&nbsp;</p> du source sont des IMAGES PERDUES du site officiel : versets coraniques, fragments cités, termes vocalisés, expressions demandées. Tu DOIS rétablir leur contenu en français à cet endroit précis : versets et fragments entre « », termes en translittération DIN 31635. AUCUNE section ne peut rester vide ou squelettique. Voir l'exemple apparié plus bas.

3. STRUCTURE MIROIR — Titres de sections EXACTEMENT ainsi :
   - أهداف الدرس → « Objectifs de la leçon » (la liste <ul> qui suit le h1 ; crée ce <h2> s'il n'existe pas)
   - تمهيد → « Introduction (tamhīd) » ; الآيات → « Les versets » ; النص → « Le texte » ; المتن → « Le texte du matn »
   - الفهم → « La compréhension » ; الشرح → « Explication des termes »
   - استخلاص مضامين الآيات / النص → « Extraction des idées du texte »
   - التفسير → « Le commentaire (tafsīr) » ; التحليل → « L'analyse »
   - التقويم → « L'évaluation » ; الاستثمار → « L'enrichissement (istithmār) » ; الإعداد القبلي → « La préparation préalable »
   - <h3> : أولاً → « Premièrement : », ثانياً → « Deuxièmement : », ثالثاً → « Troisièmement : »…

4. H1 — Utilise le TITRE OFFICIEL fourni dans la consigne, tel quel. La phrase de contexte qui suit le h1 reprend : matière, œuvre et auteurs (dates de mort en H), niveau (« cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq) »), numéro de leçon et phase.

5. CORAN — Versets en traduction française des sens entre guillemets français « … », référence (Sourate X, versets A-B) après la citation. Registre liturgique sobre et académique. Les numéros de versets peuvent suivre chaque verset : (1) (2)…

6. HADITHS — « Texte du hadith en français » — puis [Source] (al-Bukhārī, Muslim, Muwaṭṭaʾ…) quand la source l'indique.

7. GLOSSAIRE — Chaque entrée : translittération DIN 31635 du TERME (rétabli depuis la balise vide) + (glose littérale) + « : » + définition. Format <ul><li>.

8. TRANSLITTÉRATION DIN 31635 stricte : wuḍūʾ, ṣalāt, ḥadīth, al-Fātiḥa, ʿAbasa, qirāʾa, ḥizb. Noms : Ibn ʿAbbās, al-Qurṭubī, Ibn Juzayy, imam Mālik. AUCUN caractère arabe (tout translittérer) ; le symbole ﷺ est autorisé.

9. FRANÇAIS — Registre académique, grammaire IMPECCABLE : accords (une bosse → une boursouflure, jamais « une morceau »), élisions correctes (j'étudie, l'homme — jamais « J'cherche »), guillemets français « » EXCLUSIVEMENT (jamais de guillemets droits "), ponctuation française (espaces avant ; : ? !). Usages Minhāj : « Allah, le Très-Haut », majuscule aux attributs divins, chiffres occidentaux. Interdits : « En effet, Dieu », « l'antiquité » pour العتيق (dire « traditionnel » ou « ʿatīq »), « Mahomet » (dire « le Prophète ﷺ » ou « Muḥammad »).

10. SORTIE — UNIQUEMENT le HTML traduit : commence par <h1>, termine par la dernière balise fermée. Aucun commentaire, aucun bloc de code délimité, aucune balise <img>. Garde <ul>/<ol>/<h3>/<br> pertinents.

${PAIRED_EXAMPLE}`;

// ─────────────────────────────────────────────────────────────────────────────
// Appel LLM avec retry/backoff
// ─────────────────────────────────────────────────────────────────────────────
async function callLLM(messages: { role: string; content: string }[]): Promise<string> {
  const { default: ZAI } = await import("z-ai-web-dev-sdk");
  const zai = await ZAI.create();
  let lastErr = "";
  for (let attempt = 1; attempt <= 5; attempt++) {
    try {
      const completion = await zai.chat.completions.create({
        messages: messages as any,
        thinking: { type: THINKING ? "enabled" : "disabled" },
      });
      const out = completion.choices[0]?.message?.content;
      if (!out || !out.trim()) throw new Error("Réponse vide");
      return out.trim();
    } catch (e: any) {
      lastErr = e?.message ?? String(e);
      console.error(`   ⚠︎ tentative ${attempt}/5 échouée : ${lastErr.slice(0, 120)}`);
      await new Promise((r) => setTimeout(r, Math.min(60_000, 3_000 * 3 ** (attempt - 1))));
    }
  }
  throw new Error(`LLM indisponible après 5 tentatives : ${lastErr}`);
}

// ─────────────────────────────────────────────────────────────────────────────
// Nettoyage + validation v2
// ─────────────────────────────────────────────────────────────────────────────
function clean(raw: string): string {
  let s = raw.trim();
  s = s.replace(/^```(?:html)?\s*/i, "").replace(/```\s*$/i, "");
  const first = s.indexOf("<h1");
  if (first > 0) s = s.slice(first);
  const last = s.lastIndexOf(">");
  if (last !== -1 && last < s.length - 1) s = s.slice(0, last + 1);
  return s.trim();
}

function stripTags(s: string): string {
  return s.replace(/<[^>]+>/g, "");
}

function validate(fr: string, srcHtml: string, t: Target): { ok: boolean; errors: string[]; warnings: string[] } {
  const errors: string[] = [];
  const warnings: string[] = [];
  if (!fr.startsWith("<")) errors.push("ne commence pas par une balise HTML");
  if (/<img/i.test(fr)) errors.push("contient <img>");
  if (/{{U\d+}}/.test(fr)) errors.push("placeholders {{U…}} non remplacés");
  const arabicOutsideAttr = fr.replace(/(?:href|src)="[^"]*"/g, "").match(/[\u0600-\u06FF]/);
  if (arabicOutsideAttr) errors.push("caractères arabes hors attributs (translittérer en DIN 31635)");
  if (Buffer.byteLength(fr, "utf-8") < 400) errors.push("traduction trop courte (< 400 octets)");
  if (/(En effet, Dieu|Ainsi, Dieu\b|l'antiquité|Mahomet|Google Translate)/i.test(fr))
    errors.push("GT-isme détecté (tournure automatique interdite)");
  if (/<\/p>\s*<li>/.test(fr) || /(?<![>\n])<li>/.test(fr.slice(0, 200))) errors.push("élément <li> orphelin hors liste");
  if (/<li>\s*(?:&nbsp;|\s)*<\/li>/.test(fr)) errors.push("entrées de liste vides (balises image non rétablies)");
  if (/<ul>\s*<ul>/.test(fr)) errors.push("imbrication <ul> dans <ul> erronée");
  const straightQuotes = stripTags(fr).match(/"/);
  if (straightQuotes) errors.push("guillemets droits \" dans le texte (utiliser « »)");
  const ratio = fr.length / srcHtml.length;
  if (ratio < 0.25 || ratio > 0.95) errors.push(`ratio longueur FR/AR anormal : ${ratio.toFixed(2)} (attendu 0,30-0,90)`);
  const h2 = (fr.match(/<h2/g) || []).length;
  if (h2 < 4) errors.push(`trop peu de sections h2 (${h2})`);
  // Versets : si le source a une section الآيات, la traduction doit citer les versets
  if (/<h2>\s*الآيات/.test(srcHtml) || /الآيات\s*<\/h2>/.test(srcHtml)) {
    const m = fr.match(/<h2>\s*Les versets\s*<\/h2>([\s\S]*?)(?=<h2|$)/i);
    const verseSec = m ? m[1] : "";
    const verseText = stripTags(verseSec);
    if (!m) errors.push("section « Les versets » absente alors que le source a الآيات");
    else {
      if (!verseSec.includes("«")) errors.push("versets non cités entre « » dans « Les versets »");
      if (verseText.replace(/\(?\d+\)?/g, "").trim().length < 250)
        errors.push("section « Les versets » trop courte — versets non rétablis (images perdues)");
    }
  }
  if (!fr.includes("«")) warnings.push("aucun guillemet français « — inhabituel");
  if (t.kind === "lesson" && !/<h1>/.test(fr)) errors.push("h1 manquant");
  return { ok: errors.length === 0, errors, warnings };
}

// ─────────────────────────────────────────────────────────────────────────────
// Relecture obligatoire (passe 2)
// ─────────────────────────────────────────────────────────────────────────────
const REVIEW_CHECKLIST = `RÉVISION OBLIGATOIRE — applique cette liste de contrôle et corrige TOUT, puis rends la version finale :
1. VERSETS CORANIQUES : chaque balise <p> vide (ou <p><span></span></p>, <p>&nbsp;</p>) du source est une image perdue → rétablis le texte français du verset/fragment entre « » — dans « Les versets » ET dans le commentaire (chaque « c'est-à-dire » doit suivre un fragment cité).
2. GLOSSAIRE : chaque paire (balise vide = terme + glose visible) → « Terme translittéré (glose littérale) : définition » en <li>.
3. PRÉPARATION PRÉALABLE / questions : rétablis les expressions demandées dans les balises vides.
4. GRAMMAIRE FRANÇAISE : accords, élisions (j'étudie, jamais « J'cherche »), aucune faute de frappe, ponctuation française (espace avant ; : ? !).
5. GUILLEMETS : « » exclusivement, jamais de guillemets droits ".
6. COHÉRENCE : h1 = titre officiel fourni ; toutes les sections du corps présentes ; aucune section squelettique ; l'arabe intégralement translittéré.
7. NE RACCOURCIS PAS : chaque paragraphe du corps doit avoir sa traduction.
Rends UNIQUEMENT le HTML final complet corrigé, sans commentaire.`;

// ─────────────────────────────────────────────────────────────────────────────
// Traitement d'un document
// ─────────────────────────────────────────────────────────────────────────────
async function processTarget(t: Target): Promise<boolean> {
  console.log(`\n━━━ ${t.bookId}/${t.docId} (${t.kind === "intro" ? "intro" : `leçon ${t.index}/${t.total}`}) — ${t.titleFr}`);
  const book = loadBook(t.bookId);
  let verseBlock = "";
  const vref = extractVerseRef(t.html, t.titleFr);
  if (vref) {
    const verses = await prefillVerses(vref);
    verseBlock = `

TEXTE DES VERSETS (traduction Minhāj — intègre-le TEL QUEL dans la section « Les versets », entre guillemets « … », suivi de (${vref.sourateFr}, ${vref.from}-${vref.to}) ; dans le commentaire, cite les fragments depuis CE texte) :
« ${verses.trim()} » (${vref.sourateFr}, ${vref.from}-${vref.to})`;
    console.log(`   ⸙ versets ${vref.sourateFr} ${vref.from}-${vref.to} pré-remplis (${verses.trim().length} car)`);
  }
  const userMsg = `MANUEL : ${book.titleFr} — ${t.kind === "intro" ? "présentation du manuel" : `leçon ${t.index} sur ${t.total}`}.
TITRE OFFICIEL FR (à utiliser TEL QUEL pour le <h1>) : « ${t.titleFr} »${verseBlock}

SOURCE ARABE À TRADUIRE (HTML du site officiel des Habous — jette le boilerplate ministère/navigation) :
${t.html}`;

  // Passe 1 : traduction
  let fr = clean(await callLLM([{ role: "assistant", content: SYSTEM_PROMPT }, { role: "user", content: userMsg }]));
  mkdirSync(TR_OUT, { recursive: true });
  writeFileSync(path.join(TR_OUT, `${t.docId}.pass1.html`), fr, "utf-8");

  // Passe 2 : relecture obligatoire avec le source sous les yeux
  let fr2 = clean(await callLLM([
    { role: "assistant", content: SYSTEM_PROMPT },
    { role: "user", content: userMsg },
    { role: "assistant", content: fr },
    { role: "user", content: REVIEW_CHECKLIST },
  ]));
  if (fr2.startsWith("<h1")) fr = fr2; // si la passe 2 délire, on garde la passe 1
  writeFileSync(path.join(TR_OUT, `${t.docId}.pass2.html`), fr2, "utf-8");

  // Validation + éventuelle passe 3 de correction ciblée
  let v = validate(fr, t.html, t);
  if (!v.ok) {
    console.log(`   ↻ passe 3 de correction : ${v.errors.join(" ; ")}`);
    const fr3 = clean(await callLLM([
      { role: "assistant", content: SYSTEM_PROMPT },
      { role: "user", content: userMsg },
      { role: "assistant", content: fr },
      { role: "user", content: `${REVIEW_CHECKLIST}\n\nERREURS DÉTECTÉES PAR LA VALIDATION AUTOMATIQUE (à résoudre impérativement) :\n- ${v.errors.join("\n- ")}` },
    ]));
    if (fr3.startsWith("<h1")) {
      writeFileSync(path.join(TR_OUT, `${t.docId}.pass3.html`), fr3, "utf-8");
      const v3 = validate(fr3, t.html, t);
      if (v3.ok || v3.errors.length < v.errors.length) { fr = fr3; v = v3; }
    }
  }
  if (!v.ok) {
    console.error(`   ✗ ${t.docId} REJETÉ après 3 passes : ${v.errors.join(" ; ")}`);
    return false;
  }
  v.warnings.forEach((w) => console.log(`   ⚠︎ ${w}`));

  mkdirSync(TR_OUT, { recursive: true });
  writeFileSync(path.join(TR_OUT, `${t.docId}.html`), fr, "utf-8");
  writeFileSync(
    path.join(TR_OUT, `${t.docId}.meta.json`),
    JSON.stringify({ docId: t.docId, bookId: t.bookId, kind: t.kind, titleFr: t.titleFr, engine: "llm", at: new Date().toISOString() }, null, 2) + "\n",
    "utf-8"
  );

  const merge = spawnSync("bun", ["run", "scripts-translate/agent-merge.ts", t.docId], { encoding: "utf-8" });
  if (merge.status !== 0) {
    console.error(`   ✗ agent-merge a échoué pour ${t.docId} :\n${(merge.stdout || "") + (merge.stderr || "")}`);
    return false;
  }
  console.log(`   ✓ fusion OK — htmlFr ${fr.length.toLocaleString("fr-FR")} car (source ${t.html.length.toLocaleString("fr-FR")}, ratio ${(fr.length / t.html.length).toFixed(2)})`);

  registry.llm[t.docId] = { at: new Date().toISOString(), bookId: t.bookId, titleFr: t.titleFr };
  saveRegistry();

  try {
    execSync(`git add content/books/${t.bookId}.json scripts-translate/savant-registry.json && git commit -q -m ${JSON.stringify(`Minhāj LLM — ${t.bookId}/${t.docId} « ${t.titleFr} » (traduction savante assistée v2 : 3 passes, validations passées)`)}`, { cwd: process.cwd() });
    console.log(`   ✓ commit`);
  } catch (e: any) {
    console.warn(`   ⚠︎ commit échoué : ${e?.message?.slice(0, 120)}`);
  }
  return true;
}

// ─────────────────────────────────────────────────────────────────────────────
// Main
// ─────────────────────────────────────────────────────────────────────────────
(async () => {
  if (mode === "plan") {
    const books = readdirSync(path.join(CONTENT, "books")).filter((f) => f.endsWith(".json")).map((f) => f.replace(/\.json$/, ""));
    let grand = 0;
    const priority = [
      "tafsir-5ep", "rasm-wa-dabt-4ep", "tajwid-5ep", "fiqh-6ep", "tajwid-6ep", "tafsir-6ep",
      "hadith-6ep", "rasm-wa-dabt-5ep", "fiqh-1ep", "tafsir-1ep", "fiqh-5ep",
    ];
    const ordered = [...priority.filter((b) => books.includes(b)), ...books.filter((b) => !priority.includes(b))];
    for (const b of ordered) {
      const ts = targetsOfBook(b);
      if (!ts.length) continue;
      grand += ts.length;
      console.log(`${b.padEnd(20)} ${String(ts.length).padStart(3)} doc(s) : ${ts.slice(0, 6).map((x) => x.docId).join(" ")}${ts.length > 6 ? " …" : ""}`);
    }
    console.log(`\nTotal restant (hors pdfOnly) : ${grand} documents savants à produire.`);
    process.exit(0);
  }

  let targets: Target[];
  if (mode === "doc") {
    const docId = flag("doc")!;
    targets = [];
    for (const f of readdirSync(path.join(CONTENT, "books"))) {
      if (!f.endsWith(".json")) continue;
      const data = JSON.parse(readFileSync(path.join(CONTENT, "books", f), "utf-8"));
      const all: Target[] = [];
      const total = (data.lessons ?? []).filter((l: any) => l.html && !l.pdfOnly).length;
      let pos = 0;
      for (const l of data.lessons ?? []) {
        if (!l.html || l.pdfOnly) continue;
        pos++;
        all.push({ docId: String(l.docId), bookId: data.id, kind: "lesson", titleAr: l.titleAr ?? "", titleFr: l.titleFr ?? "", html: l.html, index: pos, total });
      }
      if (data.intro?.html && !data.intro.pdfOnly) {
        all.unshift({ docId: String(data.intro.docId), bookId: data.id, kind: "intro", titleAr: data.intro.titleAr ?? "", titleFr: data.intro.titleFr ?? "", html: data.intro.html, index: 0, total });
      }
      const hit = all.find((x) => x.docId === docId);
      if (hit) { targets.push(hit); break; }
    }
    if (!targets.length) throw new Error(`docId ${docId} introuvable`);
    if (isSavant(targets[0].docId) && !FORCE) throw new Error(`${docId} déjà savant (registre) — utilise --force pour refaire`);
  } else {
    targets = targetsOfBook(flag("book")!);
  }

  console.log(`Pipeline LLM Minhāj v2 — ${targets.length} document(s) ciblé(s)${limit !== Infinity ? ` (limit ${limit})` : ""}${THINKING ? " [thinking]" : ""}.`);
  let ok = 0, ko = 0;
  const t0 = Date.now();
  for (const t of targets.slice(0, limit)) {
    try {
      (await processTarget(t)) ? ok++ : ko++;
    } catch (e: any) {
      console.error(`   ✗ exception sur ${t.docId} : ${e?.message?.slice(0, 200)}`);
      ko++;
    }
    await new Promise((r) => setTimeout(r, 800));
  }
  const mins = ((Date.now() - t0) / 60_000).toFixed(1);
  console.log(`\n═══ Bilan : ${ok} traduit(s) ✓, ${ko} rejeté(s) ✗ — ${mins} min — registre : ${Object.keys(registry.llm).length} LLM + ${registry.hand.length} main ═══`);
})();
