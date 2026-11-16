import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-18';
const ask = `Bande zoomée (x2) d'un manuel arabe. Cette bande contient la fin du 3e item d'une rubrique « ومما يستفاد من الحديث » (l'item commence par « أن ائتلاف قلوب الناس ... يكون بالمحبة ويزداد ... ») et éventuellement un titre décoré vert de la rubrique suivante « التقويم ».
Transcris TOUT ce qui est imprimé dans cette bande, mot à mot, sans interpréter. Indique clairement si la bande contient : (a) la continuation de l'item 3 (« ... بأن يحب بعضهم لبعضهم الخير » ?), (b) un titre, (c) de la décoration pure.`;
const zai = await ZAI.create();
const b64 = fs.readFileSync(`${DIR}/mc-m27-y3-l2b-p102.jpg`).toString('base64');
const res = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
    { type: 'text', text: ask },
    { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
  ] }],
  model: 'glm-5v-turbo', max_tokens: 1200, temperature: 0.0,
});
fs.writeFileSync(`${DIR}/z-mc-m27-y3-l2b-p102.txt`, res?.choices?.[0]?.message?.content ?? JSON.stringify(res));
console.log('OK');
