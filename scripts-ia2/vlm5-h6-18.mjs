// IA-2 — vlm5-h6-18.mjs : ronde VLM 5 — dernière arbitration (mots contestés isolés).
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();

const PRE = `Tu lis un micro-crop très haute résolution (3600 dpi) du manuel marocain de hadith (document public, transcription académique). Transcris UNIQUEMENT ce qui est imprimé. ÉPELLE les mots contestés lettre par lettre avec leurs points. Ne récite pas de mémoire.`;

const QS = [
  ["z9-item4-word", `Ce segment contient : la fin «...وَذَلِكَ بِأَنْ» puis UN ou PLUSIEURS mots puis «بِمَا يُمْكِنُ...». (1) COMBIEN de mots séparés y a-t-il entre «بأن» et «بما» ? (2) Transcris-les TOUS avec leur vocalisation. (3) ÉPELLE le premier d'entre eux lettre par lettre (avec points) : commence-t-il par ياء (2 points dessous) ou لام-ألف ? Contient-il une عين ? une دال ?`],
  ["z9-manas-w23", `Segment : la suite d'une ligne qui a commencé par «التَّسْوِيفُ». Transcris les 2-4 mots visibles avec vocalisation. ÉPELLE le premier : بِتَفْرِيطِهِ ? بِفَرْطِهِ ? autre ? Et le second : وَتَقْصِيرِهِ ? وَنَقْصِهِ ? autre ?`],
  ["z9-aya-ref", `Le début (droite) contient la fin d'un verset coranique puis la référence entre crochets [الـ...: N] (peut-être en bleu). Transcris les derniers mots du verset, puis ÉPELLE le nom de la sourate et le NUMÉRO chiffre par chiffre (١٥ ? ١٩ ? ٢١ ? autre ?). Décris chaque chiffre.`],
  ["z9-aya2-end", `La fin (gauche) de la 2e ligne d'un verset coranique ornementé. Transcris les 3-6 derniers mots TELS QU'IMPRIMÉS. (Indice de contrôle — ne l'utilise que pour vérifier ta lecture : la fin attendue pourrait ressembler à «كُلُّ امْرِئٍ بِمَا كَسَبَ رَهِينٌ» — mais transcris ce que tu VOIS.)`],
  ["z9-p101-glose23b", `Une glose lexicographique : terme en rouge, deux-points, définition en noire. Le terme commence par أ-ذ-ا-ل ? Transcris la glose ENTIERE (terme + définition) telle qu'imprimée, avec vocalisation.`],
  ["z9-p104-table-hdr", `Le HAUT d'un tableau d'exercice : cherche une rangée d'EN-TÊTES. Le texte d'en-tête peut être en BLANC ou CRÈME sur fond coloré (invisible en noir/blanc). (1) Y a-t-il une rangée d'en-têtes ? (2) Transcris chaque en-tête de colonne exactement. (3) Combien de colonnes ?`],
  ["z8-p101-ragabba4", `Cette ligne contient : «رَغَّبَ النبيُّ ﷺ في [X] الناس وبذل النفع إليهم والإحسان إليهم،». QUESTION CIBLÉE sur X : (a) X contient-il la lettre ق (qāf, 2 points au-dessus) ? (b) contient-il la lettre ح (ḥāʾ, sans point) ? (c) X = الِاقْتِرَابِ ? الْإِحْسَانِ ? الْإِكْثَارِ ? ÉPELLE X lettre par lettre. (d) Après «الناس» y a-t-il «وبذل» ? (e) La ligne se termine par quoi (، ؛ :) ?`],
];

for (const [name, q] of QS) {
  const png = `${DIR}/${name}.png`;
  const out = `${DIR}/vlm5-h6-18-${name}.txt`;
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1200,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(`=== ${name} ===\n` + txt.slice(0, 850) + '\n');
      done = true;
    } catch (e) { console.log(`${name} tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm5-h6-18');
