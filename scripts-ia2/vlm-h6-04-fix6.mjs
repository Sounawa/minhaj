// Z2-38 — Round 3f : boîte jaune centrale (2 lignes) + 2 boîtes bleues — zooms ×6/×8
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';
const COMMON = `Micro-recadrage très grossi d'un manuel scolaire marocain d'hadith (arabe, leçon «التنافس في الخير»). TRANSCRIS UNIQUEMENT ce qui est imprimé, mot à mot, avec les voyelles visibles. Décris les lettres avant de conclure. Ne complète jamais par mémoire.`;

const ZONES = [
  ['p27-top-l1', [27, 195, 390, 445, 414, 6],
   `Première ligne du texte d'une boîte jaune d'organigramme. Le texte se termine probablement par «...بِالصَّحَابَةِ» (d'après la couche texte: ل بِالصَّحَابَةِ est visible vers x=243-325). TRANSCRIS la ligne ENTIÈRE mot à mot. Quel est le ou les mots AVANT «بالصحابة» ?`],
  ['p27-top-l2', [27, 195, 412, 445, 440, 6],
   `Deuxième ligne du texte d'une boîte jaune d'organigramme (sous la ligne contenant بالصحابة). TRANSCRIS-la mot à mot. La couche texte suggère des lettres comme ص...ار ou similaire vers x=242-393.`],
  ['p27-bleud2', [27, 396, 478, 520, 508, 8],
   `Boîte bleue de DROITE (petite, 1-2 mots). Elle est l'en-tête de la colonne des bons comportements (أداء الفرائض، الإكثار من ذكر الله، التنافس في الخير، تصحيح النية للتقرب إلى الله). TRANSCRIS son texte lettre par lettre. Un candidat lu auparavant: «الْآخِرَةُ» (alif-lam + alif-madda + khāʾ + tāʾ marbūṭa). CONCORDE ou autre ?`],
  ['p27-bleug2', [27, 121, 478, 255, 508, 8],
   `Boîte bleue de GAUCHE (petite, 1-2 mots). Elle est l'en-tête de la colonne des mauvais comportements (ترك الفرائض، الغفلة عن ذكر الله، الكسل والخمول، التمتع بالمباحات دون قصد). TRANSCRIS son texte lettre par lettre. Candidats déjà proposés: «أَجْنَبٌ» / «أَجْرَأَ» / «الدُّنْيَا». Décris chaque lettre (la première est-elle alif-hamza ou dāl ? y a-t-il un jīm, un nūn, un bāʾ ?).`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

for (const [nom, spec, Q] of ZONES) {
  const out = `${DIR}/vlm-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const [pg, x0, y0, x1, y1, z] = spec;
  const fp = `${DIR}/crops/vlm-${nom}.png`;
  if (!fs.existsSync(fp)) {
    execSync(`python3 -c "
from PIL import Image
S=600/72.0
im=Image.open('${DIR}/r600/p${pg}.png')
c=im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S)))
c=c.resize((int(c.width*${z}),int(c.height*${z})),Image.LANCZOS)
c.save('${fp}')
"`);
  }
  for (const psm of [7, 6]) {
    try {
      execSync(`tesseract ${fp} ${DIR}/tcrops/t-${nom}-psm${psm} -l ara --tessdata-dir /home/z/my-project/scripts-translate/tessdata --psm ${psm}`, {stdio:'pipe'});
      const tt = fs.readFileSync(`${DIR}/tcrops/t-${nom}-psm${psm}.txt`, 'utf8').trim().replace(/\n+/g, ' ⏎ ');
      if (tt) console.log(`[tesseract ${nom} psm${psm}]: ${tt}`);
    } catch (e) {}
  }
  const img = fs.readFileSync(fp).toString('base64');
  console.log(`\n======== ${nom} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 3 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1000,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${nom} échec: ${e.message}`); await sleep(5000*attempt); }
  }
  if (!done) console.log(`ECHEC ${nom} — quota ?`);
  await sleep(2000);
}
