// Z2-37 — relectures VLM ligne-à-ligne des 4 citations moucharabieh mal lues au 1er tour
// (cadres trop larges → hallucination ; méthode Z2-36 : recadrage par ligne, 1200 dpi)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03';

const COMMON = `Recadrage FIN d'une SEULE ligne (ou deux lignes serrées) d'un manuel scolaire marocain d'hadith, leçon «تحريم الظلم». La ligne contient un verset coranique dans un cadre ornementé ﴿...﴾ en police moucharabieh maghrébine (lettres anguleuses, fā' à point SOUS la ligne, style tawqi'/andalous). Lecture droite→gauche. TRANSCRIS UNIQUEMENT ce que tu vois, lettre par lettre puis mot par mot. N'utilise JAMAIS ta mémoire du Coran pour compléter : si tu ne vois pas un mot, écris [illisible]. Donne ensuite ta meilleure lecture du segment.`;

// (nom, page, dpi, x0,y0,x1,y1, question)
const ZONES = [
  ['p19-cit1-ligne', 19, 1200, 40, 691, 610, 724,
   `Une ligne de texte courant contenant un petit cadre inline: «قال الله تعالى: ﴿...﴾ [الكهف: ...]. وقال». TRANSCRIS: (1) le début «قال الله تعالى:» ; (2) le contenu du cadre ﴿...﴾ MOT À MOT (le verset fait ~4-6 mots, il contient probablement un mot ressemblant à ربك et un mot ressemblant à أحدا — mais vérifie sur les pixels) ; (3) la référence [الكهف: chiffre(s)] avec la valeur exacte des chiffres (décris chaque chiffre) ; (4) le mot final «وقال».`],
  ['p20-cit2-ligne', 20, 1200, 40, 62, 610, 102,
   `Une ligne en haut de page: «وقال سبحانه: ﴿...﴾ [النساء: ...].» Le cadre contient un verset court (~4-8 mots) en police moucharabieh. TRANSCRIS mot à mot le contenu du cadre (il contient probablement un mot ressemblant à يظلم et un mot ressemblant à مثقال et/ou ذرة — mais vérifie sur les pixels), puis la référence [النساء: chiffres] avec la valeur exacte (décris chaque chiffre).`],
  ['p23-cit1-l1', 23, 1200, 55, 120, 600, 148,
   `Première ligne d'un verset coranique dans un cadre ornementé (police moucharabieh). La ligne commence à droite après «1- قال الله تعالى:». TRANSCRIS la partie du verset sur CETTE ligne, mot à mot (5-8 mots attendus). Ne complète pas par mémoire.`],
  ['p23-cit1-l2', 23, 1200, 55, 144, 600, 176,
   `Deuxième ligne du même verset en cadre moucharabieh + la référence. TRANSCRIS la fin du verset mot à mot (elle se termine probablement par un mot comme مُّبِينٍ), puis le numéro d'ayah dans le médaillon décoratif (s'il y en a un), puis la référence entre crochets [sourate: chiffres] — donne le nom de la sourate EXACTEMENT tel qu'imprimé (lettre par lettre) et la valeur des chiffres (décris-les).`],
  ['p23-cit2-ligne', 23, 1200, 55, 168, 600, 208,
   `Une ligne: «وقال الله تعالى: ﴿...﴾ [طه: ...].» Le cadre contient un verset (~8-12 mots) en police moucharabieh sur cette ligne. TRANSCRIS le verset mot à mot (probablement des mots ressemblant à تمدنّ/عينيك/الحياة الدنيا/رزق — mais vérifie sur les pixels), puis la référence [طه: chiffres] avec la valeur exacte (décris chaque chiffre).`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

fs.mkdirSync(`${DIR}/crops`, { recursive: true });
for (const [nom, pg, dpi, x0, y0, x1, y1] of ZONES) {
  const fp = `${DIR}/crops/vlm-${nom}.png`;
  if (!fs.existsSync(fp)) {
    const S = dpi / 72.0;
    execSync(`python3 -c "
from PIL import Image
S=${S}
im=Image.open('${DIR}/r${dpi}/p${pg}.png')
im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S))).save('${fp}')
"`);
  }
}

for (const [nom, pg, , , , , , Q] of ZONES) {
  const out = `${DIR}/vlm-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const img = fs.readFileSync(`${DIR}/crops/vlm-${nom}.png`).toString('base64');
  console.log(`\n======== ${nom} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 3 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1200,
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
