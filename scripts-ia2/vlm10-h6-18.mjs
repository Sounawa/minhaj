import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();
const img = fs.readFileSync(`${DIR}/z16-p101-tahlil-head.png`).toString('base64');
const r = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
    { type: 'text', text: `Zone d'un manuel marocain (document public). Y a-t-il un TITRE de section en bleu/coloré (comme «التَّحْلِيلُ:») ? Transcris-le exactement, épelé lettre par lettre. S'il n'y a pas de titre, dis-le. Transcris aussi la 1re ligne de texte visible.` },
    { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
  ] }],
  model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 700,
});
console.log(r?.choices?.[0]?.message?.content ?? JSON.stringify(r));
fs.writeFileSync(`${DIR}/vlm10-tahlil-head.txt`, r?.choices?.[0]?.message?.content ?? '');
