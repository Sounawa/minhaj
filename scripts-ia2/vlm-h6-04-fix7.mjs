// Z2-38 — Round 3g : boîte jaune centrale (image inversée texte-noir-sur-blanc)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';
const Q = `Boîte centrale d'un organigramme (texte calligraphié, ici inversé en noir sur blanc pour la lisibilité). Le contexte: un schéma pédagogique d'un manuel marocain d'hadith (leçon «التنافس في الخير») opposant les comportements du croyant. La boîte contient probablement 1 à 2 lignes. TRANSCRIS le texte complet mot à mot, avec les voyelles visibles. La couche texte du PDF suggère que le texte contient «...ل بِالصَّحَابَةِ» (fin de ligne 1) et des lettres comme ص...ار (ligne 2). Décris les lettres avant de conclure. Ne complète jamais par mémoire.`;

const zai = await ZAI.create();
const img = fs.readFileSync(`${DIR}/crops/vlm-p27-top-inv.png`).toString('base64');
const r = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
      { type: 'text', text: Q },
      { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
  ] }],
  model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 900,
});
console.log(r?.choices?.[0]?.message?.content ?? JSON.stringify(r));
fs.writeFileSync(`${DIR}/vlm-p27-top-inv.txt`, r?.choices?.[0]?.message?.content ?? '');
