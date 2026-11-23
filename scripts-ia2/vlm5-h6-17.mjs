// IA-2 — vlm5-h6-17.mjs : identité du glyphe isolé entre مرات et بحسب (3600×4).
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();
const JOBS = [
  { id: 'g1-mot6', img: 'z7-mot6-zoom.png',
    q: `Zoom extrême (3600 dpi ×4) de la fin d'une ligne de hadith : à droite le mot «مرات», puis UN SEUL signe isolé, puis le début de «بحسب». SCRUTIN : ce signe isolé — décris sa forme exactement : est-ce un point-virgule arabe ؛ (deux points superposés) ? un guillemet » (deux chevrons) ? les DEUX à la fois ؛» ? Décris chaque élément graphique visible dans le vide entre les deux mots.` },
];
for (const job of JOBS) {
  const out = `${DIR}/vlm5-h6-17-${job.id}.txt`;
  if (fs.existsSync(out)) continue;
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const img = fs.readFileSync(`${DIR}/${job.img}`).toString('base64');
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: job.q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 900,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(`=== ${job.id} ===\n` + txt);
      done = true;
    } catch (e) { console.log(`${job.id} tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 9000 * attempt)); }
  }
}
console.log('OK vlm5-h6-17');
