// Z2-38 — Round 3k : zone p28 y=220-340 (espace de réponse + bandeau استثمار ?)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';
const zai = await ZAI.create();
const img = fs.readFileSync(`${DIR}/crops/vlm-p28-gap.png`).toString('base64');
const r = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
      { type: 'text', text: `Zone d'un manuel scolaire marocain d'hadith (leçon «التنافس في الخير»), entre les items numérotés de la rubrique التقويم et une citation commençant par «عن أبي ذر». Décris ce qui s'y trouve: (1) des lignes de réponse pointillées ? combien ? (2) un bandeau décoratif de rubrique ? lequel (probablement الاستثمار) ? (3) une consigne écrite avant la citation ? Si oui, transcris-la mot à mot.` },
      { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
  ] }],
  model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 800,
});
const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
fs.writeFileSync(`${DIR}/vlm-p28-gap.txt`, txt);
console.log(txt);
