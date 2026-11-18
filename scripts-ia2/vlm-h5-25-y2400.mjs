// Z2-30 — double lecture neutre à 2400 dpi du mot contesté (p140)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-25/crops';
const PROMPT = `Recadrage natif 2400 dpi (très haute netteté) d'une fin de ligne d'un manuel scolaire marocain d'hadith (5e année primaire), lecture droite→gauche.
Transcris mot à mot ce qui est imprimé, avec la vocalisation. Puis décompose le DERNIER mot lettre par lettre : pour chaque lettre, donne sa forme, son nombre EXACT de points (0/1/2/3 — précise au-dessus ou en-dessous) et ses dents. Ne complète par mémoire d'aucun texte connu.`;

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (let run = 1; run <= 2; run++) {
  const out = `${DIR}/vlmy-r${run}.txt`;
  if (fs.existsSync(out)) { console.log(`skip r${run}`); continue; }
  const img = fs.readFileSync(`${DIR}/y1-p140.png`).toString('base64');
  let done = false;
  for (let attempt = 1; attempt <= 3 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: PROMPT },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1400,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(`\n==== run${run} ====`);
      console.log(txt.length > 700 ? txt.slice(0, 550) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`échec r${run}: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2000);
}
