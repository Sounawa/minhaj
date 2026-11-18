// Z2-38 — Round 3l : isnad de la citation p28 (الغفاري ?)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';
const zai = await ZAI.create();
const img = fs.readFileSync(`${DIR}/crops/vlm-p28-cit1.png`).toString('base64');
const r = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
      { type: 'text', text: `Première ligne d'une citation encadrée d'un manuel d'hadith: «عَنْ أَبِي ذَرٍّ ... قَالَ: قُلْتُ: يَا رَسُولَ اللهِ: "ذَ...». Entre «أبي ذر» et «قال», y a-t-il «الْغِفَارِيِّ رَضِيَ اللهُ عَنْهُ» ou seulement «رَضِيَ اللهُ عَنْهُ» ou rien ? TRANSCRIS la ligne complète mot à mot. CONCORDE/NE CORRESPOND PAS pour: (A) عن أبي ذر الغفاري رضي الله عنه قال ; (B) عن أبي ذر رضي الله عنه قال ; (C) عن أبي ذر قال.` },
      { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
  ] }],
  model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 700,
});
const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
fs.writeFileSync(`${DIR}/vlm-p28-cit1.txt`, txt);
console.log(txt);
