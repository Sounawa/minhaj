// IA-2 — vlm3-h6-16.mjs : contrôle final — fin de la puce (أسباب / أسبابها).
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();
const img = fs.readFileSync(`${DIR}/z12-p93-asbabW.png`).toString('base64');
const Q = `Fin d'une puce d'un manuel scolaire (3600 dpi). La ligne visible se termine par «...ووجوب الأخذ بكل ...». SCRUTIN : transcris la fin de la ligne mot à mot avec vocalisation. Le DERNIER mot : «أسباب» seul, ou «أسبابها» ? Décompose la fin du dernier mot lettre par lettre : y a-t-il quelque chose après le ب final (un هاء ? un alif ? un point final) ? Décris tout ce qui suit le dernier mot jusqu'au bord gauche de l'image.`;

let done = false;
for (let attempt = 1; attempt <= 4 && !done; attempt++) {
  try {
    const r = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
          { type: 'text', text: Q },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
      ] }],
      model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1500,
    });
    const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
    fs.writeFileSync(`${DIR}/vlm-v3-asbab.txt`, txt);
    console.log(txt);
    done = true;
  } catch (e) { console.log(`tentative ${attempt} échec: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
}
console.log('OK vlm3-h6-16');
