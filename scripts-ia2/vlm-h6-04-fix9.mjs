// Z2-38 — Round 3i : boîte jaune centrale en r1200 (dernière tentative)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';
const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// crops depuis r1200 (déjà haute résolution)
const CROPS = [
  ['p27-top-r1200', 195, 390, 445, 442, 1],
  ['p27-bleug-r1200', 121, 476, 255, 510, 2],
];

for (const [nom, x0, y0, x1, y1, z] of CROPS) {
  const fp = `${DIR}/crops/vlm-${nom}.png`;
  if (!fs.existsSync(fp)) {
    execSync(`python3 -c "
from PIL import Image
S=1200/72.0
im=Image.open('${DIR}/r1200/p27.png')
c=im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S)))
if (${z} > 1): c=c.resize((c.width*${z},c.height*${z}),Image.LANCZOS)
c.save('${fp}')
"`);
  }
}

const QS = [
  ['p27-top-r1200', `Boîte centrale (fond bleu, calligraphie claire) d'un organigramme pédagogique, leçon «التنافس في الخير». La couche texte du PDF montre que la 1re ligne contient «...? بِالصَّحَابَةِ» (x≈242-325) et la 2e ligne des fragments «ص...ار» (x≈310-393). La boîte fait ~2 lignes. TRANSCRIS le texte complet ligne par ligne, mot à mot. Décris les mots du DÉBUT de la ligne 1 (à droite, x≈325-440, calligraphie). Candidats à vérifier: «وَلَا?َةٍ تَدَاءٍ بِالصَّحَابَةِ» / «مَوَدَّةٍ تَدَاعٍ بِالصَّحَابَةِ» / «التَّنَافُسُ... بَيْنَ الصَّحَابَةِ» / autre.`],
  ['p27-bleug-r1200', `Petite boîte bleue de GAUCHE d'un organigramme (en-tête de la colonne négative: ترك الفرائض، الغفلة، الكسل والخمول، التمتع دون قصد). Une lecture précédente donne «أَجْتَنَبُ» (alif-hamza + jīm-sukūn + tāʾ + nūn + bāʾ-damma). CONFIRME lettre par lettre ou propose autre chose. Le mot est-il أَجْتَنِبُ / أَتَجَنَّبُ / أَجْنَبُ / autre ?`],
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
            { type: 'text', text: `Calligraphie d'un manuel scolaire marocain d'hadith. TRANSCRIS UNIQUEMENT ce qui est imprimé. Décris les lettres avant de conclure. Ne complète jamais par mémoire.\n\n${Q}` },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1000,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} échec: ${e.message}`); await sleep(5000*attempt); }
  }
  await sleep(2000);
}
