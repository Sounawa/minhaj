// IA-2 — vlm5-h6-16.mjs : identification des CHIFFRES de cartouche (formes).
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

const COMMON = `Image binarisée extraite d'un cartouche de manuel scolaire marocain : en bas, sous le mot «الدرس», sont imprimés UN OU DEUX CHIFFRES arabo-indiens. Rappel des formes : ١ = simple trait vertical ; ٢ = coupelle avec hampe ; ٣ = trois pointes en zigzag (w) ; ٤ = forme angulaire fermée comme un epsilon renversé / «4» stylisé ; ٥ = boucle fermée ovale (comme un cœur ou un 0 renflé) ; ٦ = crochet ouvert, comme un 7 arabe ; ٧ = V renversé. Décris chaque chiffre visible de DROITE à GAUCHE (position, forme, boucle ouverte/fermée, nombre de pointes), puis donne le nombre. Ne devine pas : décris ce que tu vois.`;

const IMGS = ['z10-digits-L15.png', 'z10-digits-L16.png', 'z15-p76-digits.png'];

for (const k of IMGS) {
  const out = `${DIR}/vlm-v5-${k}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${k}`); continue; }
  const img = fs.readFileSync(`${DIR}/${k}`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1200,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 600 ? txt.slice(0, 480) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000 * attempt); }
  }
  await sleep(2500);
}
console.log('OK vlm5-h6-16');
