// IA-2 — vlm6-h6-18.mjs : ronde VLM 6 — identification آية + derniers points.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();

const PRE = `Tu lis un crop du manuel marocain de hadith (document public, transcription académique). Transcris UNIQUEMENT ce qui est imprimé. ÉPELLE les éléments contestés. Ne récite pas de mémoire.`;

const QS = [
  ["z10-p104-aya-full", `ENCADRÉ complet avec un VERSET coranique en calligraphie ornementée (1 ou 2 lignes), une référence [الـ...: N] et le début d'une question. (1) Combien de lignes compte le verset ? (2) Transcris le verset ligne par ligne, mot par mot, TEL QU'IMPRIMÉ (même si le rasm diffère du canon). (3) IDENTIFIE la sourate et le numéro d'après les mots que tu lis. (4) Épele la référence imprimée [nom + chiffres].`],
  ["z10-aya-ref2", `Ce segment contient la FIN du verset, puis la référence [الـ...: N] (peut-être en bleu), puis «كيف أوافق...». Transcris tout ce segment. ÉPELLE le nom de la sourate et CHAQUE CHIFFRE de la référence (١٥ ? ١٩ ? ٢١ ? autre ?).`],
  ["z10-manas-junction", `Deux morceaux empilés : EN HAUT le DÉBUT (droite) d'une ligne, EN BAS la FIN (gauche) de la ligne précédente. La phrase complète est : «...ومعنى قوله ﷺ: «ومن بطأ به عمله لم يسرع به نسبه» أن من أخر عمله [BAS] ... [HAUT] ... لا يتقدم به نسبه...». Transcris : (1) la fin de la ligne du BAS (les 2-3 derniers mots) ; (2) le début de la ligne du HAUT (les 3-4 premiers mots). ÉPELLE le premier mot du HAUT et le dernier mot du BAS.`],
  ["z10-p101-glos-zone", `Zone complète entre «ترجمة الراوي» et le texte numéroté. QUESTIONS : (1) Transcris le titre de section «الشرح :» ou équivalent. (2) Combien de GLOSES (terme rouge : définition noire) sont imprimées ? Transcris-les TOUTES exactement. (3) Y a-t-il un titre «الاستخلاص :» ou similaire ? Transcris-le. (4) Transcris tout autre texte visible.`],
  ["z10-p104-table-full", `Zone complète d'un TABLEAU d'exercice (entre la question 3 «أستثمر تعلماتي وأملأ الجدول في دفتري بما يناسب:» et la suite). (1) Décris la structure : rangée d'en-têtes ? combien de rangées de contenu ? colonnes ? (2) Si une rangée d'en-têtes existe (texte éventuellement blanc/crème sur fond coloré), transcris chaque en-tête. (3) Transcris le contenu de chaque case remplie. (4) Qu'y a-t-il SOUS le tableau ?`],
];

for (const [name, q] of QS) {
  const png = `${DIR}/${name}.png`;
  const out = `${DIR}/vlm6-h6-18-${name}.txt`;
  if (!fs.existsSync(png)) { console.log(`MANQUANT: ${png}`); continue; }
  if (fs.existsSync(out)) { console.log(`déjà fait: ${out}`); continue; }
  const img = fs.readFileSync(png).toString('base64');
  let done = false;
  for (let attempt = 1; attempt <= 5 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: PRE + '\n\n' + q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1600,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(`=== ${name} ===\n` + txt.slice(0, 1000) + '\n');
      done = true;
    } catch (e) { console.log(`${name} tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm6-h6-18');
