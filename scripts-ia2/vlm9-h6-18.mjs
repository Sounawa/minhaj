// IA-2 — vlm9-h6-18.mjs : les deux TOUT derniers crops.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();
const PRE = `Tu lis un crop très haute résolution du manuel marocain de hadith (document public, transcription académique). Transcris UNIQUEMENT ce qui est imprimé. ÉPELLE les mots contestés. Ne récite pas de mémoire.`;
const QS = [
  ["z13-p104-table-hdr4", `La rangée d'EN-TÊTES d'un tableau (texte BLEU sur fond crème/coloré). Il y a plusieurs colonnes. Transcris CHAQUE en-tête de droite à gauche, exactement, puis épele-les un par un.`],
  ["z13-p101-istikhl-head2", `UN titre de section en bleu, sur une ou deux lignes. Transcris-le EXACTEMENT. Est-ce «الاستخلاص:» (al-istikhlāṣ, 9 lettres avec سين) ? «التخلاص:» (sans سين) ? «استخلاص المضامين:» ? ÉPELLE le titre lettre par lettre avec les points.`],
];
for (const [name, q] of QS) {
  const png = `${DIR}/${name}.png`;
  const out = `${DIR}/vlm9-h6-18-${name}.txt`;
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1000,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(`=== ${name} ===\n` + txt.slice(0, 800) + '\n');
      done = true;
    } catch (e) { console.log(`${name} tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm9-h6-18');
