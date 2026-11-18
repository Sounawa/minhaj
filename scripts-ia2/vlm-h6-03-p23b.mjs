// Z2-37 — p.23 الاستثمار : relectures VLM finales (marges corrigées) + agrandissement x2
// des amas de chiffres (médaillon ۝ + crochets de référence).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03';

const COMMON = `Recadrage d'un manuel scolaire marocain d'hadith, leçon «تحريم الظلم», rubrique استثمار, activité 1 (deux versets coraniques à comparer). Les versets sont en police moucharabieh maghrébine dans des cadres ornementés. Lecture droite→gauche. TRANSCRIS UNIQUEMENT ce que tu vois, mot à mot. N'utilise JAMAIS ta mémoire du Coran pour compléter: mot illisible → [illisible].`;

const ZONES = [
  ['p23-LB2', null, null, null, null, null, null,
   `Ligne complète (marges généreuses). Elle contient dans l'ordre droite→gauche: (1) la FIN du verset 1 (fin du cadre moucharabieh, ~3-6 mots, possiblement des mots ressemblant à «الكتاب مسطورا») ; (2) le crochet fermant ﴾ ou l'ornement de fin ; (3) un médaillon décoratif doré avec un numéro (décris les chiffres: combien? quelles formes?) ; (4) la référence entre crochets bleus [sourate: numéro] — transcris le nom de la sourate LETTRE PAR LETTRE et le numéro avec sa valeur exacte ; (5) un point ; (6) «وقال الله تعالى:» ; (7) le DÉBUT du verset 2 dans un nouveau cadre moucharabieh (~4-8 mots, la ligne suivante continue). TRANSCRIS TOUT dans l'ordre.`],
  ['p23-LC2', null, null, null, null, null, null,
   `Ligne complète. Elle contient: la suite du verset 2 (cadre moucharabieh, ~6-10 mots) puis la référence entre crochets bleus [طه: numéro] puis un point. TRANSCRIS tout mot à mot dans l'ordre, puis décris les chiffres de la référence (combien de chiffres? quelles formes? valeurs?).`],
  ['p23-LD2', null, null, null, null, null, null,
   `Dernière ligne de la citation: elle contient la FIN du verset 2 (2-4 mots moucharabieh), puis un médaillon décoratif avec numéro, puis la référence bleue [طه: numéro] et un point. TRANSCRIS tout mot à mot. Décris les chiffres du médaillon ET ceux du crochet: sont-ils identiques?`],
  ['p23-MED1', 23, 1200, 368, 149, 400, 178,
   `AMAS DE CHIFFRES agrandi x2. C'est soit un médaillon décoratif de fin de verset coranique (۝), soit des chiffres d'une référence. Décris CHAQUE glyphe numérique: combien de chiffres? Pour chacun: boucle fermée? ouverte? trait supérieur? queue? Donne la valeur la plus probable (en chiffres arabes orientaux ٠١٢٣٤٥٦٧٨٩ ou occidentaux 0-9, précise lesquels).`],
  ['p23-REF1B', 23, 1200, 295, 149, 345, 178,
   `ZONE AGRANDIE x2 contenant la fin d'une référence coranique entre crochets: «...: numéro]». Décris CHAQUE chiffre visible (combien? formes? valeurs?) et transcris les lettres bleues visibles (nom de sourate? fin de mot?).`],
];

// pré-crops pour les zones avec coordonnées (MED1, REF1B) avec agrandissement x2
for (const [nom, pg, dpi, x0, y0, x1, y1] of ZONES) {
  if (pg === null) continue;
  const fp = `${DIR}/crops/vlm-${nom}.png`;
  if (!fs.existsSync(fp)) {
    const S = dpi / 72.0;
    execSync(`python3 -c "
from PIL import Image, ImageOps
S=${S}
im=Image.open('${DIR}/r${dpi}/p${pg}.png').convert('L')
c=im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S)))
c=c.resize((c.width*2, c.height*2), Image.LANCZOS)
c=ImageOps.autocontrast(c)
c.save('${fp}')
"`);
  }
}
// copies des crops tess13 (marges corrigées) vers les noms vlm
for (const [nom] of ZONES) {
  if (nom.endsWith('2')) {
    const src = `${DIR}/crops/t13-p23-${nom.slice(4,6)}.png`;  // p23-LB2 -> t13-p23-LB.png
    const dst = `${DIR}/crops/vlm-${nom}.png`;
    if (fs.existsSync(src) && !fs.existsSync(dst)) fs.copyFileSync(src, dst);
  }
}

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const [nom, , , , , , , Q] of ZONES) {
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1400,
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
