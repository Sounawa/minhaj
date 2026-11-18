// Z2-37 — lecture VLM ligne par ligne de la zone الاستثمار p.23 (hadith-6ep leçon 2)
// Structure établie par encre+bbox : LA(y127-150) LB(y150-174) LC(y180-202) LD(y199-222)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03';

const COMMON = `Recadrage FIN d'une ligne d'un manuel scolaire marocain d'hadith, leçon «تحريم الظلم», rubrique استثمار. Les versets coraniques sont dans des cadres ornementés ﴿...﴾ en police moucharabieh maghrébine (fā' à point SOUS la ligne). Lecture droite→gauche. TRANSCRIS UNIQUEMENT ce que tu vois, mot à mot. N'utilise JAMAIS ta mémoire du Coran pour compléter : si un mot est illisible, écris [illisible]. Décris aussi les chiffres/médaillons décoratifs.`;

const ZONES = [
  ['p23-LA', 23, 1200, 40, 127, 610, 150,
   `Cette ligne commence par «1- قال الله تعالى:» puis le DÉBUT d'un verset dans un cadre moucharabieh (la suite est sur la ligne suivante). TRANSCRIS: «1- قال الله تعالى: ﴿...» — le contenu du cadre mot à mot (~6-10 mots).`],
  ['p23-LB', 23, 1200, 40, 150, 610, 174,
   `Cette ligne contient: la FIN du verset 1 (cadre moucharabieh), puis un médaillon décoratif avec numéro d'ayah, puis la référence entre crochets [sourate: numéro], puis un point, puis «وقال الله تعالى:» puis le DÉBUT du verset 2 (cadre moucharabieh, suite sur la ligne suivante). TRANSCRIS TOUT mot à mot dans l'ordre: (1) fin du verset 1 ; (2) numéro du médaillon ; (3) référence [sourate: numéro] — nom de sourate lettre par lettre + valeur des chiffres (décris-les) ; (4) début du verset 2.`],
  ['p23-LC', 23, 1200, 40, 180, 610, 203,
   `Cette ligne contient: la suite et FIN du verset 2 (cadre moucharabieh), puis la référence entre crochets [طه: numéro], puis un point. TRANSCRIS tout mot à mot: (1) la fin du verset 2 ; (2) la référence [طه: chiffres] avec la valeur EXACTE des chiffres (décris chaque chiffre: un seul chiffre ? deux ? trois ?) ; (3) la ponctuation finale.`],
  ['p23-LD', 23, 1200, 40, 199, 610, 223,
   `Cette ligne suit la référence [طه: ...] de la ligne du dessus. TRANSCRIS tout ce qu'elle contient mot à mot (soit la fin de la citation, soit une consigne de l'activité comme «أبحث عن تفسير الآيتين...», soit autre chose).`],
  ['p23-REF1', 23, 1200, 290, 149, 420, 175,
   `Zone contenant la référence du verset 1 entre crochets: [sourate: numéro]. TRANSCRIS le nom de la sourate LETTRE PAR LETTRE (chaque lettre: ا? ب? ت? ...), puis donne la valeur EXACTE des chiffres en décrivant chaque chiffre (boucles, traits). Y a-t-il un médaillon décoratif avec un numéro à proximité ? Quelle valeur ?`],
  ['p23-REF2', 23, 1200, 315, 179, 425, 204,
   `Zone contenant la référence du verset 2 entre crochets: [طه: numéro]. Donne la valeur EXACTE des chiffres: combien de chiffres ? Décris chaque chiffre (un «1»? un «3»? un «131»?). TRANSCRIS aussi le mot avant les crochets (fin du verset) tel que visible.`],
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
