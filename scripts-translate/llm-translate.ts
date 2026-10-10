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
import { existsSync, mkdirSync, readFileSync, writeFileSync, readdirSync, rmSync, statSync } from "fs";
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
const sleepSync = (sec: number) => { try { execSync(`sleep ${sec}`); } catch {} };
const saveRegistry = () => {
  // — Parallélisme multi-livres : verrou mkdir (atomique) + fusion avec l'état disque le plus récent
  const lockDir = `${REGISTRY_PATH}.lock`;
  let locked = false;
  for (let i = 0; i < 40; i++) {
    try { mkdirSync(lockDir); locked = true; break; } catch { sleepSync(0.25); }
  }
  try {
    const fresh: Registry = JSON.parse(readFileSync(REGISTRY_PATH, "utf-8"));
    fresh.llm = { ...fresh.llm, ...registry.llm };
    if (!Array.isArray(fresh.hand) || fresh.hand.length < registry.hand.length) fresh.hand = registry.hand;
    registry.hand = fresh.hand;
    registry.llm = fresh.llm;
  } catch { /* registre absent/illisible : on écrit notre état */ }
  writeFileSync(REGISTRY_PATH, JSON.stringify(registry, null, 2) + "\n", "utf-8");
  if (locked) { try { rmSync(lockDir, { recursive: true, force: true }); } catch {} }
};
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
// Cache coranique local — le texte des versets est TOUJOURS injecté depuis le
// cache (scripts-translate/quran-cache.json : uṯmānī + trad. Hamidullah).
// JAMAIS de verset « généré de mémoire » par le LLM (risque d'hallucination).
// ─────────────────────────────────────────────────────────────────────────────
const QURAN_CACHE_PATH = path.join(process.cwd(), "scripts-translate", "quran-cache.json");
function loadQuran(): any | null {
  try { return JSON.parse(readFileSync(QURAN_CACHE_PATH, "utf-8")); } catch { return null; }
}
const SURAHS: Record<string, number> = {
  fatiha: 1, hamd: 1, baqara: 2, imran: 3, nisa: 4, maida: 5, anam: 6, araf: 7, anfal: 8,
  tawba: 9, baraa: 9, yunus: 10, hud: 11, yusuf: 12, rad: 13, ibrahim: 14, hijr: 15, nahl: 16,
  isra: 17, kahf: 18, maryam: 19, taha: 20, anbiya: 21, hajj: 22, muminun: 23, nur: 24,
  furqan: 25, shuara: 26, naml: 27, qasas: 28, ankabut: 29, rum: 30, luqman: 31, sajda: 32,
  assajda: 32, ahzab: 33, saba: 34, fatir: 35, yasin: 36, saffat: 37, sad: 38, zumar: 39,
  gafir: 40, ghafir: 40, fussilat: 41, shura: 42, zukhruf: 43, dukhan: 44, jathiya: 45,
  jathya: 45, ahqaf: 46, muhammad: 47, fath: 48, hujurat: 49, qaf: 50, dhariyat: 51,
  dariyat: 51, tur: 52, najm: 53, qamar: 54, rahman: 55, waqia: 56, hadid: 57, mujadala: 58,
  hashr: 59, mumtahana: 60, saf: 61, assaf: 61, jumu: 62, jumua: 62, munafiqun: 63,
  taghabun: 64, talaq: 65, tahrim: 66, mulk: 67, qalam: 68, haqqa: 69, marij: 70, nuh: 71,
  jinn: 72, muzzammil: 73, muddaththir: 74, muddathir: 74, muddassir: 74, qiyama: 75,
  insan: 76, mursalat: 77, naba: 78, naziat: 79, abasa: 80, takwir: 81, infitar: 82,
  mutaffifin: 83, inshiqaq: 84, inchikak: 84, inshikak: 84, inchiqaq: 84, buruj: 85,
  tariq: 86, ala: 87, ghashiya: 88, ghachiya: 88, fajr: 89, balad: 90, shams: 91, layl: 92,
  duha: 93, dhuha: 93, sharh: 94, tin: 95, alaq: 96, iqra: 96, qadr: 97, bayyina: 98,
  zalzala: 99, adiyat: 100, qaria: 101, takathur: 102, asr: 103, humaza: 104, fil: 105,
  quraysh: 106, quraish: 106, maun: 107, kawthar: 108, kausar: 108, kafirun: 109, nasr: 110,
  masad: 111, ikhlas: 112, falaq: 113, nas: 114,
};
function normalizeName(raw: string): string {
  let s = raw.toLowerCase().trim();
  s = s.replace(/^sourates?\s+/, "").replace(/^surah\s+/, "");
  s = s.replace(/[\u02BE\u02BF\u2019'`]/g, "");
  s = s.replace(/\u1E25/g, "h").replace(/\u1E63/g, "s").replace(/\u1E0D/g, "d").replace(/\u1E6D/g, "t")
       .replace(/\u1E93/g, "z").replace(/\u0101/g, "a").replace(/\u012B/g, "i").replace(/\u016B/g, "u")
       .replace(/\u01E7/g, "g").replace(/\u01E2/g, "a")
       .replace(/\u00E2/g, "a").replace(/\u00EE/g, "i").replace(/\u00FB/g, "u").replace(/\u00F4/g, "o");
  s = s.replace(/[\u00E9\u00E8\u00EA\u00EB]/g, "e").replace(/[\u00E0\u00E4]/g, "a")
       .replace(/[\u00F9\u00FC]/g, "u").replace(/\u00E7/g, "c").replace(/\u0153/g, "oe");
  s = s.replace(/[^a-z]/g, "");
  s = s.replace(/^sourate/, "");
  s = s.replace(/^al/, "");
  s = s.replace(/^a([nsrtdzlshj])\1/, "$1"); // assimilation de l'article (as-sajda → sajda)
  return s;
}
function nameToSurah(raw: string): number | null {
  const s = normalizeName(raw);
  if (!s) return null;
  if (s in SURAHS) return SURAHS[s];
  for (const [k, n] of Object.entries(SURAHS)) {
    if (s.length >= 4 && (s.startsWith(k) || k.startsWith(s)) && Math.abs(s.length - k.length) <= 3) return n;
  }
  return null;
}
function quranWindow(cache: any, surah: number, from: number, to: number) {
  const s = cache[String(surah)];
  if (!s) return null;
  const lo = Math.max(1, from - 4);
  const hi = Math.min(s.nAyahs, to + 8);
  const pick = (arr: [number, string][]) =>
    arr.filter(([n]) => n >= lo && n <= hi).map(([n, t]) => `(${n}) ${t}`).join("\n");
  return { englishName: s.englishName, nAyahs: s.nAyahs, lo, hi, ar: pick(s.ar), fr: pick(s.fr) };
}

function extractVerseRef(srcHtml: string, titleFr: string): { sourateFr: string; from: number; to: number } | null {
  // Nom de sourate depuis le titre officiel (fiable, normalisé R11)
  const t = titleFr.match(/^Sourate\s+(.+?),?\s+versets/i) || titleFr.match(/^Sourate\s+([^,]+)/i);
  if (!t) return null;
  const sourateFr = t[1].trim();
  // Intervalle : le TITRE officiel prime ; sinon le span arabe (tatweel neutralisés)
  const titleRange = titleFr.match(/versets?\s+(\d+)\s+(?:\u00E0|a|jusqu'|[\u2013-])\s*(\d+)/i);
  const srcNorm = srcHtml.replace(/\u0640/g, "");
  const secMatch = srcNorm.match(/<h2[^>]*>\s*\u0627\u0644\u0622\u064A\u0627\u062A[\s\S]{0,600}?<span>\s*([^<]*\d+\s*[\u2013-]\s*\d+[^<]*)\s*<\/span>/);
  const spanRange = secMatch?.[1]?.match(/(\d+)\s*[\u2013-]\s*(\d+)/);
  let from = 0, to = 0;
  if (titleRange) { from = parseInt(titleRange[1], 10); to = parseInt(titleRange[2], 10); }
  else if (spanRange) { from = parseInt(spanRange[1], 10); to = parseInt(spanRange[2], 10); }
  if (!(from >= 1 && to >= from)) return null;
  return { sourateFr, from, to };
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

5. CORAN — Versets en traduction française des sens entre guillemets français « … », référence (Sourate X, versets A-B) après la citation. Registre liturgique sobre et académique. Les numéros de versets peuvent suivre chaque verset : (1) (2)… SI UN « TEXTE CORANIQUE DE RÉFÉRENCE » est fourni dans la consigne, il est la SEULE source autorisée des versets et fragments cités : utilise-le fidèlement (ponctuation et style Minhāj ajustables, JAMAIS de changement de sens), n'emprunte AUCUN verset à une autre sourate et ne « reconstitue » rien de mémoire. Le Coran est un texte sacré : une citation inexacte est une faute GRAVE.

6. HADITHS — « Texte du hadith en français » — puis [Source] (al-Bukhārī, Muslim, Muwaṭṭaʾ…) quand la source l'indique.

7. GLOSSAIRE — Chaque entrée : translittération DIN 31635 du TERME (rétabli depuis la balise vide) + (glose littérale) + « : » + définition. Format <ul><li>.

8. TRANSLITTÉRATION DIN 31635 stricte : wuḍūʾ, ṣalāt, ḥadīth, al-Fātiḥa, ʿAbasa, qirāʾa, ḥizb. Noms : Ibn ʿAbbās, al-Qurṭubī, Ibn Juzayy, imam Mālik. AUCUN caractère arabe (tout translittérer) ; le symbole ﷺ est autorisé.

9. FRANÇAIS — Registre académique, grammaire IMPECCABLE : accords (une bosse → une boursouflure, jamais « une morceau »), élisions correctes (j'étudie, l'homme — jamais « J'cherche »), guillemets français « » EXCLUSIVEMENT (jamais de guillemets droits "), ponctuation française (espaces avant ; : ? !). Usages Minhāj : « Allah, le Très-Haut », majuscule aux attributs divins, chiffres occidentaux. FRANÇAIS NATUREL : reformule de façon idiomatique et fluide — jamais de calque mot-à-mot de l'arabe. Interdits : « En effet, Dieu », « l'antiquité » pour العتيق (dire « traditionnel » ou « ʿatīq »), « Mahomet » (dire « le Prophète ﷺ » ou « Muḥammad »), l'anglicisme « guidance » (dire « guidée »), « guidage » pour توجيه (dire « orientation » ou « mise en garde » selon le contexte).

10. SORTIE — UNIQUEMENT le HTML traduit : commence par <h1>, termine par la dernière balise fermée. Aucun commentaire, aucun bloc de code délimité, aucune balise <img>. Garde <ul>/<ol>/<h3>/<br> pertinents.

${PAIRED_EXAMPLE}`;

// ─────────────────────────────────────────────────────────────────────────────
// Appel LLM avec retry/backoff
// ─────────────────────────────────────────────────────────────────────────────
async function callLLM(messages: { role: string; content: string }[]): Promise<string> {
  const { default: ZAI } = await import("z-ai-web-dev-sdk");
  const zai = await ZAI.create();
  let lastErr = "";
  for (let attempt = 1; attempt <= 8; attempt++) {
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
      const is429 = /429|Too many/i.test(lastErr);
      const waitMs = is429
        ? Math.min(300_000, 20_000 * attempt) // 429 : patience longue (20 s → 5 min)
        : Math.min(60_000, 3_000 * 3 ** (attempt - 1));
      console.error(`   ⚠︎ tentative ${attempt}/8 échouée${is429 ? " [429]" : ""} : ${lastErr.slice(0, 120)}`);
      await new Promise((r) => setTimeout(r, waitMs));
    }
  }
  throw new Error(`LLM indisponible après 8 tentatives : ${lastErr}`);
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
  // Guillemets droits appariés → guillemets français, UNIQUEMENT dans les nœuds
  // texte (jamais dans les attributs des balises)
  const quoteFix = (txt: string) => txt.replace(/"([^"\n]{1,300}?)"/g, "« $1 »");
  let out = "";
  let rest = s;
  const tagRe = /<[^>]*>/;
  while (rest.length) {
    const tag = rest.match(tagRe);
    if (!tag || tag.index === undefined) { out += quoteFix(rest); break; }
    out += quoteFix(rest.slice(0, tag.index));
    out += tag[0];
    rest = rest.slice(tag.index + tag[0].length);
  }
  return out.trim();
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
  // Documents courts (intros « muqaddima », présentations) : seuils adaptés
  const tiny = Buffer.byteLength(srcHtml, "utf-8") < 2500 || t.kind === "intro";
  if (ratio < (tiny ? 0.1 : 0.25) || ratio > (tiny ? 6 : 0.95)) errors.push(`ratio longueur FR/AR anormal : ${ratio.toFixed(2)} (attendu ${tiny ? "0,10-6,00" : "0,30-0,90"})`);
  const h2 = (fr.match(/<h2/g) || []).length;
  if (h2 < (tiny ? 1 : 4)) errors.push(`trop peu de sections h2 (${h2})`);
  // Versets : si le source a une section الآيات (tatweel neutralisés), la traduction doit citer les versets
  const srcNormHtml = srcHtml.replace(/\u0640/g, "");
  if (/<h2[^>]*>\s*\u0627\u0644\u0622\u064A\u0627\u062A/.test(srcNormHtml)) {
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
8. FIDÉLITÉ DU SENS : aucun contresens ni inversion (ex. « s'égare » pour « se guide », « il interdit » pour « il ordonne » = faute GRAVE) ; si un TEXTE CORANIQUE DE RÉFÉRENCE est fourni, les versets et fragments cités doivent en être IDENTIQUES (au style près).
9. MOTS-PIÈGES (contrôle obligatoire ligne à ligne) : هدى/هُدَى = guider, guidée (JAMAIS « s'égare » = ضلّّ، JAMAIS l'anglicisme « guidance ») ; توجيه = orientation / mise en garde selon le contexte (pas « guidage ») ; كفور = ingrat ; تقوى = crainte (d'Allah). Relis chaque verbe à sens réversible en comparant l'arabe.
Rends UNIQUEMENT le HTML final complet corrigé, sans commentaire.`;

// ─────────────────────────────────────────────────────────────────────────────
// Passe 3 — polissage du français (relecteur d'édition, sans le source)
// ─────────────────────────────────────────────────────────────────────────────
const POLISH_PROMPT = `Tu es un relecteur professionnel d'éditions académiques et patrimoniales françaises. On te livre la traduction française finale d'une leçon du programme officiel marocain (HTML Minhāj). Mission : la polir SANS rien retrancher ni réorganiser :
1. GRAMMAIRE : accords, conjugaisons, élisions (j'étudie, l'homme — jamais « J'cherche »), ponctuation française (espace avant ; : ? !), guillemets « » exclusifs, majuscules.
2. FRANÇAIS NATUREL : élimine tout calque mot-à-mot de l'arabe (ex. « Au guidage d'Allah pour Son Prophète » → « Après qu'Allah, le Très-Haut, eut orienté Son Prophète ») et tout anglicisme (« guidance » → « guidée », « guidance » interdit).
3. SENS : si tu remarques un contresens, rétablis le SENS EXACT (هدى = guider ; ضلّ = s'égarer — jamais l'un pour l'autre ; « qu'il s'égare par sa guidée » doit devenir « qu'il se guide par sa guidée »).
4. INTANGIBLES : ne modifie NI les citations entre « … » (versets, hadiths, fragments), NI le contenu, NI l'ordre des sections, NI la structure HTML, NI les <h1>/<h2>/<h3>, NI les références (Sourate X, versets A-B), NI les translittérations DIN 31635.
Rends UNIQUEMENT le HTML complet corrigé, sans commentaire.`;

// ─────────────────────────────────────────────────────────────────────────────
// Mode TURBO (livres non coraniques) — polissage fusionné dans la passe 2.
// Économise ~1 appel sur 3-4 par document (≈ -30 % de quota LLM) sous
// contrainte de débit. Les livres tafsir-* et ulum-quran-* (versets
// omniprésents, risque sacré maximal) gardent le pipeline complet à 4
// passes. La passe 2 (fidélité AVEC le source sous les yeux) et la
// validation + passe 4 corrective restent TOUJOURS — seul le polissage
// style-only est fusionné.
// ─────────────────────────────────────────────────────────────────────────────
const isTurboBook = (bookId: string) => !/^(tafsir-|ulum-quran-)/.test(bookId);
const TURBO_POLISH_ADDON = `

POLISSAGE DU FRANÇAIS (fusionné dans cette passe) : en plus de la révision de fidélité ci-dessus, polis le style pour une édition académique — grammaire et accords, élisions correctes, ponctuation française (espace avant ; : ? !), guillemets « » exclusifs ; élimine tout calque mot-à-mot de l'arabe et tout anglicisme (« guidance » interdit → « guidée ») ; si tu remarques un contresens, rétablis le SENS EXACT. INTANGIBLES : ne modifie ni les citations entre « … », ni le contenu, ni l'ordre des sections, ni la structure HTML, ni les références, ni les translittérations DIN.`;

// ─────────────────────────────────────────────────────────────────────────────
// Traitement d'un document
// ─────────────────────────────────────────────────────────────────────────────
async function processTarget(t: Target): Promise<boolean> {
  const turbo = isTurboBook(t.bookId);
  console.log(`\n━━━ ${t.bookId}/${t.docId} (${t.kind === "intro" ? "intro" : `leçon ${t.index}/${t.total}`}) — ${t.titleFr}${turbo ? " [turbo]" : ""}`);
  const book = loadBook(t.bookId);
  let verseBlock = "";
  const vref = extractVerseRef(t.html, t.titleFr);
  if (vref) {
    const surah = nameToSurah(vref.sourateFr);
    const quran = loadQuran();
    const w = surah && quran ? quranWindow(quran, surah, vref.from, vref.to) : null;
    if (w && w.fr.length > 40) {
      verseBlock = `

TEXTE CORANIQUE DE RÉFÉRENCE — sourate ${w.englishName} (${vref.sourateFr}), traduction française de référence (M. Hamidullah), numérotation STANDARD du muṣḥaf :
${w.fr}

TEXTE ARABE CORRESPONDANT (édition uṯmānī, même fenêtre, versets ${w.lo}-${w.hi}) :
${w.ar}

CONSIGNE POUR « Les versets » : la leçon couvre les versets ${vref.from} à ${vref.to} selon la numérotation du muṣḥaf marocain (Warsh), parfois légèrement différente de la numérotation standard ci-dessus. Intègre le passage authentique correspondant — repère-le grâce au glossaire et aux fragments du commentaire — avec les numéros STANDARD entre parenthèses, entre « … », suivi de la référence (${vref.sourateFr}, ${vref.from}-${vref.to}). La traduction de référence ci-dessus est ta base FIDÈLE : style et ponctuation ajustables aux conventions Minhāj, sens JAMAIS modifié, AUCUN verset inventé ni emprunté à une autre sourate. Dans le commentaire, cite les fragments depuis CE texte.`;
      console.log(`   ⸙ sourate ${w.englishName} : texte authentique v.${w.lo}-${w.hi} injecté (base Hamidullah)`);
    } else {
      console.error(`   ✗ ${t.docId} REPORTÉ : sourate « ${vref.sourateFr} » non résolue ou cache coranique absent — traitement requis avant fusion (qualité sacrée).`);
      return false;
    }
  }
  const userMsg = `MANUEL : ${book.titleFr} — ${t.kind === "intro" ? "présentation du manuel" : `leçon ${t.index} sur ${t.total}`}.
TITRE OFFICIEL FR (à utiliser TEL QUEL pour le <h1>) : « ${t.titleFr} »${verseBlock}

SOURCE ARABE À TRADUIRE (HTML du site officiel des Habous — jette le boilerplate ministère/navigation) :
${t.html}`;

  // Passe 1 : traduction
  let fr = clean(await callLLM([{ role: "assistant", content: SYSTEM_PROMPT }, { role: "user", content: userMsg }]));
  mkdirSync(TR_OUT, { recursive: true });
  writeFileSync(path.join(TR_OUT, `${t.docId}.pass1.html`), fr, "utf-8");

  // Passe 2 : relecture de FIDÉLITÉ avec le source sous les yeux
  // (TURBO : le polissage de style est fusionné ici pour économiser un appel)
  let fr2 = clean(await callLLM([
    { role: "assistant", content: SYSTEM_PROMPT },
    { role: "user", content: userMsg },
    { role: "assistant", content: fr },
    { role: "user", content: turbo ? REVIEW_CHECKLIST + TURBO_POLISH_ADDON : REVIEW_CHECKLIST },
  ]));
  if (fr2.startsWith("<h1")) fr = fr2; // si la passe 2 délire, on garde la passe 1
  writeFileSync(path.join(TR_OUT, `${t.docId}.pass2.html`), fr2, "utf-8");

  // Passe 3 : polissage du français — grammaire, naturel, anti-calques
  // (uniquement en pipeline complet ; en TURBO le polissage est fusionné
  //  dans la passe 2 — la fidélité et la validation restent identiques)
  if (!turbo) {
    const frPolish = clean(await callLLM([
      { role: "assistant", content: POLISH_PROMPT },
      { role: "user", content: `Polissage final du document suivant (HTML Minhāj déjà traduit) :\n\n${fr}` },
    ]));
    if (frPolish.startsWith("<h1")) fr = frPolish;
    writeFileSync(path.join(TR_OUT, `${t.docId}.pass3.html`), frPolish, "utf-8");
  }

  // Validation + éventuelle passe 4 de correction ciblée
  let v = validate(fr, t.html, t);
  if (!v.ok) {
    console.log(`   ↻ passe 4 de correction : ${v.errors.join(" ; ")}`);
    const fr4 = clean(await callLLM([
      { role: "assistant", content: SYSTEM_PROMPT },
      { role: "user", content: userMsg },
      { role: "assistant", content: fr },
      { role: "user", content: `${REVIEW_CHECKLIST}\n\nERREURS DÉTECTÉES PAR LA VALIDATION AUTOMATIQUE (à résoudre impérativement) :\n- ${v.errors.join("\n- ")}` },
    ]));
    if (fr4.startsWith("<h1")) {
      writeFileSync(path.join(TR_OUT, `${t.docId}.pass4.html`), fr4, "utf-8");
      const v4 = validate(fr4, t.html, t);
      if (v4.ok || v4.errors.length < v.errors.length) { fr = fr4; v = v4; }
    }
  }
  if (!v.ok) {
    console.error(`   ✗ ${t.docId} REJETÉ après 4 passes : ${v.errors.join(" ; ")}`);
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
    let committed = false;
    for (let i = 0; i < 12 && !committed; i++) {
      try {
        // index.lock périmé (> 90 s) d'un processus mort : on le retire
        try {
          const st = statSync(path.join(process.cwd(), ".git", "index.lock"));
          if (Date.now() - st.mtimeMs > 90_000) rmSync(path.join(process.cwd(), ".git", "index.lock"));
        } catch {}
        execSync(`git add content/books/${t.bookId}.json scripts-translate/savant-registry.json && git commit -q -m ${JSON.stringify(`Minhāj LLM — ${t.bookId}/${t.docId} « ${t.titleFr} » (traduction savante assistée v3 : 4 passes, Coran authentique injecté, validations passées)`)}`, { cwd: process.cwd() });
        committed = true;
      } catch (e: any) {
        if (!String(e?.message ?? "").includes("index.lock")) throw e;
        sleepSync(1 + i * 0.5);
      }
    }
    if (!committed) throw new Error("index.lock occupé après 12 tentatives");
    console.log(`   ✓ commit`);
  } catch (e: any) {
    console.warn(`   ⚠︎ commit échoué (sera rattrapé au balayage de fin de vague) : ${e?.message?.slice(0, 120)}`);
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
