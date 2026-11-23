// IA-2 — vlm6-h6-17.mjs : أعراض ou أغراض (p.99, citation al-Ghazali) ?
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();
const Q = `Une ligne d'une citation d'al-Ghazali (3600 dpi) : «...وأما الدينية فيجتمع فيها أيضاً ... مختلفة، إذ منها الاستفادة...». SCRUTIN : le mot entre «أيضاً» et «مختلفة» — décompose sa 2e lettre lettre par lettre : est-ce عين (ʿayn, SANS point) ou غين (ghayn, AVEC un point au-dessus) ? Le mot est-il «أعراض» ou «أغراض» ? Décris précisément la présence ou l'absence du point. Transcris la ligne.`;
const img = fs.readFileSync(`${DIR}/z7-p99-arad.png`).toString('base64');
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
    fs.writeFileSync(`${DIR}/vlm6-h6-17-arad.txt`, txt);
    console.log(txt);
    done = true;
  } catch (e) { console.log(`tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 9000 * attempt)); }
}
console.log('OK vlm6-h6-17');
