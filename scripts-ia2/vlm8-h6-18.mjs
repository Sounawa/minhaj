// IA-2 — vlm8-h6-18.mjs : ronde VLM 8 — 3 dernières zones.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();
const PRE = `Tu lis un crop très haute résolution du manuel marocain de hadith (document public, transcription académique). Transcris UNIQUEMENT ce qui est imprimé, mot par mot, avec vocalisation. ÉPELLE les mots contestés lettre par lettre. Ne récite pas de mémoire.`;
const QS = [
  ["z12-glose4-def", `La DÉFINITION d'une glose (noire) du terme «وَغَشِيَتْهُمْ». Elle commence par «نَزَلَتْ عَلَيْهِمْ...». Transcris la définition ENTIÈRE. ÉPELLE le SECOND verbe exactement : وَأَحَاطَتْهُمْ ? وَأَطَافَتْهِمْ ? وَأَظَلَّتْهُمْ ? وَأَطْلَتْهُمْ ? autre ? Décris ses lettres avec leurs points.`],
  ["z12-p104-table-hdr3", `La rangée d'EN-TÊTES d'un tableau d'exercice (texte BLEU/BLANC sur fond crème ou coloré, difficile à lire). Transcris CHAQUE en-tête de colonne de droite à gauche, exactement. Les candidats possibles : السُّلُوكُ ? المَوْقِفُ ? مَوْقِفِي ? التَّطْبِيقُ ? الأَعْمَالُ الفَاضِلَةُ ? ÉPELLE chaque en-tête.`],
  ["z12-p101-istikhlas-head", `Zone entre les gloses et les questions numérotées d'un manuel. Y a-t-il un TITRE de section (comme «الاستخلاص:» ou «استخلاص المضامين:» ou «أستنتج:»)? Transcris-le exactement. Transcris aussi toute ligne visible en dessous.`],
];
for (const [name, q] of QS) {
  const png = `${DIR}/${name}.png`;
  const out = `${DIR}/vlm8-h6-18-${name}.txt`;
  if (!fs.existsSync(png)) { console.log(`MANQUANT: ${png}`); continue; }
  if (fs.existsSync(out)) { console.log(`déjà: ${out}`); continue; }
  const img = fs.readFileSync(png).toString('base64');
  let done = false;
  for (let attempt = 1; attempt <= 5 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: PRE + '\n\n' + q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1100,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(`=== ${name} ===\n` + txt.slice(0, 850) + '\n');
      done = true;
    } catch (e) { console.log(`${name} tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm8-h6-18');
