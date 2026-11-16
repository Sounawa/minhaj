import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-18';
const ask = `UNE seule ligne d'imprimé arabe (fin d'item, pleine largeur). Le début de la ligne est : « ...فيما بينهم يكون بالمحبة ويزداد » — transcris la SUITE exacte de la ligne jusqu'au point final, en te basant UNIQUEMENT sur les pixels. Choisis ensuite parmi : (1) « ذلك بأن يحب بعضهم لبعضهم الخير . » (2) « ذلك بأن يحب بعضهم بعضا الخير . » (3) « ذلك بأن يصحب بعضهم بعضا بمحبة الخير . » (4) autre — recopie-la.`;
const zai = await ZAI.create();
const b64 = fs.readFileSync(`${DIR}/mc-m28-y3-full-p102.jpg`).toString('base64');
const res = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
    { type: 'text', text: ask },
    { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
  ] }],
  model: 'glm-5v-turbo', max_tokens: 1200, temperature: 0.0,
});
fs.writeFileSync(`${DIR}/z-mc-m28-y3-full-p102.txt`, res?.choices?.[0]?.message?.content ?? JSON.stringify(res));
console.log('OK');
