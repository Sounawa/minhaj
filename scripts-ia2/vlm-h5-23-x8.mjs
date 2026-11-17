// Z2-27 — VLM derniers arbitrages X08/X09/X10 (zooms maximaux, questions NEUTRES)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-23';
const COMMON = `Recadrage très agrandi d'un manuel scolaire marocain d'hadith (5e primaire), droite→gauche. Texte possiblement blanc sur fond décoré.
Transcris mot à mot, avec vocalisation, uniquement ce qui est imprimé. Ne complète JAMAIS par mémoire d'un texte connu : si tu n'es pas sûr d'une lettre, dis-le.`;

const Q = {
  X08a: `Transcris tout ce qui est imprimé sur ce fragment (une ligne d'un encadré de verset, ou la ligne au-dessus).`,
  X08b: `Transcris tout ce qui est imprimé sur ce fragment (suite de l'encadré de verset, avec éventuellement une référence entre crochets).`,
  X09: `Transcris TOUT ce qui est imprimé sur ce fragment : une ou deux lignes qui suivent «1. أَحْفَظُ حَدِيثَ الدَّرْسِ الْآتِيَ وَأَقُومُ بِمَا يَلِي:» — probablement un extrait de hadith ou une consigne. Ne te fie à aucune mémoire : transcris les lettres une à une.`,
  X10: `Un seul mot (ou groupe de 2 mots) du début d'un verset coranique, très agrandi. Transcris-le lettre par lettre. Indique pour CHAQUE lettre sa valeur (sīn? bāʾ? qāf? ʿayn? alif? wāw?) puis le mot complet.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const t of Object.keys(Q)) {
  const out = `${DIR}/vlm23-${t}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${t}`); continue; }
  const img = fs.readFileSync(`${DIR}/z23-${t}.png`).toString('base64');
  console.log(`\n======== ${t} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q[t] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1024,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 500 ? txt.slice(0, 250) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${t} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2500);
}
