// IA-2 — vlm4-h6-17.mjs : position exacte du guillemet interne du matn L17.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();
const Q = `Une seule ligne d'un hadith (3600 dpi) : «هاهنا» (ou «هنا») «ويشير إلى صدره ثلاث مرات؛ بحسب امرئ من الشر أن يحقر». Sur cette ligne se trouve UN guillemet fermant » (deux chevrons pointant à gauche). SCRUTIN : entre quels MOTS exactement ce guillemet est-il imprimé ? Enumère la séquence complète des mots et signes de la droite vers la gauche, en indiquant la position du » et celle du ؛. Y a-t-il aussi un guillemet ouvrant « quelque part sur la ligne ?`;
const img = fs.readFileSync(`${DIR}/z6-p95-matn-l2-3600.png`).toString('base64');
let done = false;
for (let attempt = 1; attempt <= 4 && !done; attempt++) {
  try {
    const r = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
          { type: 'text', text: Q },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
      ] }],
      model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1200,
    });
    const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
    fs.writeFileSync(`${DIR}/vlm4-h6-17-guillemet.txt`, txt);
    console.log(txt);
    done = true;
  } catch (e) { console.log(`tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 9000 * attempt)); }
}
console.log('OK vlm4-h6-17');
