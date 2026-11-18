// Z2-38 — Round 3h : boîte jaune centrale, 2 moitiés inversées
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';
const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

const QS = [
  ['p27-top-l1i', `Première ligne (moitié supérieure) d'une boîte d'organigramme, calligraphie ici INVERSÉE en noir sur blanc. La couche texte du PDF indique que cette ligne contient la séquence «...ل بِالصَّحَابَةِ» (le mot بِالصَّحَابَةِ est présent). TRANSCRIS la ligne complète mot à mot. Quel mot précède بالصحابة ?`],
  ['p27-top-l2i', `Deuxième ligne (moitié inférieure) d'une boîte d'organigramme, calligraphie INVERSÉE. Une lecture précédente suggère «...?َ?َاقَةُ فِي الْخَيْرِ» ou similaire. TRANSCRIS la ligne complète mot à mot, lettre par lettre (le premier mot commence-t-il par وَالْـ ? contient-il لَاقَةُ/لِحَاقُ/مُنَافَسَةُ ?).`],
];

for (const [nom, Q] of QS) {
  const out = `${DIR}/vlm-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const img = fs.readFileSync(`${DIR}/crops/vlm-${nom}.png`).toString('base64');
  console.log(`\n======== ${nom} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 3 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: `Calligraphie d'un manuel scolaire marocain d'hadith (leçon «التنافس في الخير»). TRANSCRIS UNIQUEMENT ce qui est imprimé. Décris les lettres avant de conclure. Ne complète jamais par mémoire.\n\n${Q}` },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 900,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} échec: ${e.message}`); await sleep(5000*attempt); }
  }
  await sleep(2000);
}
