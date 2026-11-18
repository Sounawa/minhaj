// Z2-30 — triple lecture NEUTRE des 2 occurrences du mot contesté (leçon 25)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-25/crops';
const PROMPT = `Recadrage natif 1200 dpi d'un manuel scolaire marocain d'hadith (5e année primaire), lecture droite→gauche.
Transcris UNIQUEMENT ce qui est imprimé sur ce fragment, mot à mot, avec la vocalisation. Décompose ensuite le DERNIER mot lettre par lettre (forme + points + dents). Ne complète par mémoire d'aucun texte connu : si une lettre est illisible, dis-le.`;

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of ['w1b-p139', 'w2b-p140']) {
  for (let run = 1; run <= 3; run++) {
    const out = `${DIR}/vlmn-${k}-r${run}.txt`;
    if (fs.existsSync(out)) { console.log(`skip ${k} r${run}`); continue; }
    const img = fs.readFileSync(`${DIR}/${k}.png`).toString('base64');
    let done = false;
    for (let attempt = 1; attempt <= 3 && !done; attempt++) {
      try {
        const r = await zai.createChatCompletionVision({
          messages: [{ role: 'user', content: [
              { type: 'text', text: PROMPT },
              { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
          ] }],
          model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1200,
        });
        const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
        fs.writeFileSync(out, txt);
        console.log(`\n==== ${k} run${run} ====`);
        console.log(txt.length > 420 ? txt.slice(0, 320) + '\n[...]' : txt);
        done = true;
      } catch (e) { console.log(`tentative ${attempt} ${k} r${run} échec: ${e.message}`); await sleep(8000*attempt); }
    }
    await sleep(2000);
  }
}
