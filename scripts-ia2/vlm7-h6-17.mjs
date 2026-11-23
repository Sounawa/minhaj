// IA-2 — vlm7-h6-17.mjs : début de la ligne 2 du matn — y a-t-il un » après هاهنا ?
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();
const Q = `Début (moitié droite) d'une ligne de hadith (3600 dpi ×2). Le premier mot à droite est «هاهنا». SCRUTIN : immédiatement à gauche de «هاهنا» (entre «هاهنا» et «ويشير») y a-t-il un guillemet fermant » ou tout autre signe de ponctuation ? Décris ce qui occupe l'espace entre ces deux mots. Décris aussi ce qui suit «هاهنا» à droite (fin de zone). Transcris les 3-4 premiers mots de la ligne.`;
const img = fs.readFileSync(`${DIR}/z7-l2-right.png`).toString('base64');
let done = false;
for (let attempt = 1; attempt <= 4 && !done; attempt++) {
  try {
    const r = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
          { type: 'text', text: Q },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
      ] }],
      model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1000,
    });
    const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
    fs.writeFileSync(`${DIR}/vlm7-h6-17-l2right.txt`, txt);
    console.log(txt);
    done = true;
  } catch (e) { console.log(`tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 9000 * attempt)); }
}
console.log('OK vlm7-h6-17');
