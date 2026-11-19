// Z2-41 — test de disponibilité VLM (le quota était 429-épuisé en Z2-40)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const zai = await ZAI.create();
const img = fs.readFileSync('/home/z/my-project/scripts-ia2/tmp/h6-07/crops/p45-top.png').toString('base64');
try {
  const r = await zai.createChatCompletionVision({
    messages: [{ role: 'user', content: [
        { type: 'text', text: 'Réponds uniquement : OK' },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
    ] }],
    model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 20,
  });
  console.log('VLM DISPONIBLE →', r?.choices?.[0]?.message?.content);
} catch (e) {
  console.log('VLM INDISPONIBLE →', String(e).slice(0, 300));
}
