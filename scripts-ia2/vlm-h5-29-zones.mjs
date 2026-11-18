// Z2-34 — hadith-5ep leçon 29 «لائحة المصادر والمراجع» (pp.159-166, bibliographie)
// — lectures VLM ciblées sur les 5 zones restées aveugles (cmap vide / tesseract muet).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-29';
const S600 = 600 / 72.0;

const COMMON = `Recadrage d'un manuel scolaire marocain d'hadith (5e année primaire traditionnel, en arabe), bibliographie finale «لائحة المصادر والمراجع», sens de lecture droite→gauche. TRANSCRIS mot à mot ce qui est imprimé, sans jamais compléter par mémoire d'un texte connu. Chiffres arabo-orientaux : transcris-les en chiffres et donne leur valeur. Si une zone est un bandeau décoratif calligraphique, transcris-le lettre par lettre du mieux possible.`;

// (nom, page, x0,y0,x1,y1 en pt, question)
const ZONES = [
  ['A-ligne2', 159, 40, 195, 600, 265,
   `Deux lignes de la première rubrique «القرآن :». La ligne 1 se termine par «...من طريق الأزرق؛ المصحف ...». TRANSCRIS la ligne 2 ENTIÈREMENT mot à mot (elle peut mentionner une édition, un comité, une imprimerie, ou continuer le titre). Donne aussi la fin exacte de la ligne 1 après «المصحف».`],
  ['B-abudawud', 159, 25, 638, 350, 690,
   `Fin de l'entrée «4- سنن أبي داود؛ لمؤلفه: سليمان بن الأشعث أبي داود السجستاني الأزدي ...» puis début de la ligne suivante. Y a-t-il une date de mort «(المتوفى: ٢٧٥ه)» ou autre chose entre «الأزدي» et la fin de ligne ? TRANSCRIS les derniers mots de la ligne 1 après «السجستاني» EXACTEMENT (caractère par caractère si besoin), puis le début de la ligne 2.`],
  ['D-rubrique', 162, 40, 538, 600, 600,
   `Entre la fin de l'entrée 19 (فضائل الصحابة) et l'entrée «20- شرح الأربعين النووية...», il y a une ligne décorative/calligraphique centrée. TRANSCRIS cette ligne lettre par lettre (c'est probablement un titre de rubrique). Puis la première ligne de l'entrée 20.`],
  ['E-date-ayni', 163, 400, 652, 600, 718,
   `Fin de l'entrée «26- عمدة القاري شرح صحيح البخاري؛ لمؤلفه: بدر الدين أبي محمد محمود ابن أحمد بن موسى بن أحمد بن حسين الغيتابي الحنفي العيني (المتوفى: ...» — la ligne suivante commence par la date de mort. Donne le nombre EXACT de chiffres et leur valeur (en chiffres arabo-orientaux), puis «ه)» ou pas, puis la suite «الناشر: ...».`],
  ['G-entree37', 165, 40, 570, 600, 655,
   `Sous la rubrique «مراجع أخرى :», la première entrée commence par «37- جامع بيان العلم وفضله؛ لمؤلفه: ...» et se poursuit sur la ligne suivante par «بن عبد البر بن عاصم النمري القرطبي، الطبعة الأولى: 1414ه.». TRANSCRIS la ligne d'en-tête ENTIÈREMENT mot à mot, surtout les mots entre «لمؤلفه:» et la fin de ligne (noms de l'auteur : أبو عمر يوسف ... ?). Donne le numéro d'entrée exact (37 ?).`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// générer les crops 600 dpi si absents
for (const [nom, pg, x0, y0, x1, y1] of ZONES) {
  const fp = `${DIR}/crops/vlm-${nom}.png`;
  if (!fs.existsSync(fp)) {
    execSync(`python3 -c "
from PIL import Image
S=${S600}
im=Image.open('${DIR}/r600/p${pg}.png')
im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S))).save('${fp}')
"`);
  }
}

for (const [nom, pg, , , , , Q] of ZONES) {
  const out = `${DIR}/vlm29-${nom}.txt`;
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1500,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${nom} échec: ${e.message}`); await sleep(6000*attempt); }
  }
  await sleep(2500);
}
