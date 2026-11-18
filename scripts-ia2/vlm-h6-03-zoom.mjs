// Z2-37 — DERNIERE ADJUDICATION p.23 : demi-lignes zoomées ×3 (glyphes agrandis).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03';

const COMMON = `Image agrandie ×3 d'une DEMI-LIGNE d'un manuel scolaire marocain, verset coranique en police moucharabieh maghrébine (lettres anguleuses, points SOUS la ligne pour ف/ق style maghrébin). Lecture droite→gauche. PROTOCOLE: (1) compte les MOTS visibles (groupes séparés par des espaces); (2) pour chaque mot, décris les lettres une par une (avec leurs points: au-dessus? en dessous? combien?); (3) propose la lecture du mot; (4) assemble la ligne. Ne complète JAMAIS par mémoire du Coran: un mot incertain → [?] après ta meilleure proposition.`;

const ZONES = [
  // verset 1, ligne A (y 122-152): droite puis gauche
  ['z1-A-droite', 23, 1200, 300, 121, 612, 153,
   `Moitié DROITE de la 1re ligne du verset 1 (elle commence après «1- قال الله تعالى: ﴿» — le début de la ligne avec «قال الله تعالى» est peut-être visible au bord droit). Transcris les 3-5 premiers mots du verset selon le protocole.`],
  ['z1-A-gauche', 23, 1200, 38, 121, 310, 153,
   `Moitié GAUCHE de la 1re ligne du verset 1 (fin de la ligne, 3-5 mots avant le retour à la ligne). Transcris selon le protocole.`],
  // verset 1, ligne B (y 148-178): droite puis gauche
  ['z1-B-droite', 23, 1200, 300, 147, 612, 179,
   `Moitié DROITE de la 2e ligne du verset 1 (3-5 premiers mots de la ligne). Transcris selon le protocole.`],
  ['z1-B-gauche', 23, 1200, 38, 147, 310, 179,
   `Moitié GAUCHE de la 2e ligne du verset 1: elle se termine par le médaillon doré ۝ avec numéro, puis la référence bleue [sourate: numéro]. Transcris les derniers mots du verset selon le protocole, puis: (a) le numéro du médaillon (valeur, description des chiffres); (b) la référence: nom de sourate lettre par lettre + valeur des chiffres (description).`],
  // verset 2, ligne C (y 178-206): droite puis gauche
  ['z2-C-droite', 23, 1200, 300, 177, 612, 208,
   `Moitié DROITE d'une ligne du verset 2 (après «وقال الله تعالى: ﴿»). Transcris selon le protocole.`],
  ['z2-C-gauche', 23, 1200, 38, 177, 310, 208,
   `Moitié GAUCHE de la même ligne du verset 2. Transcris selon le protocole.`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

fs.mkdirSync(`${DIR}/crops/zoom`, { recursive: true });
for (const [nom, pg, dpi, x0, y0, x1, y1] of ZONES) {
  const fp = `${DIR}/crops/zoom/${nom}.png`;
  if (!fs.existsSync(fp)) {
    const S = dpi / 72.0;
    execSync(`python3 -c "
from PIL import Image, ImageOps
S=${S}
im=Image.open('${DIR}/r${dpi}/p${pg}.png').convert('L')
c=im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S)))
c=c.resize((c.width*3, c.height*3), Image.LANCZOS)
c=ImageOps.autocontrast(c)
c.save('${fp}')
"`);
  }
}

for (const [nom, , , , , , , Q] of ZONES) {
  const out = `${DIR}/vlm-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const img = fs.readFileSync(`${DIR}/crops/zoom/${nom}.png`).toString('base64');
  console.log(`\n======== ${nom} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 2 && !done; attempt++) {
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
    } catch (e) { console.log(`tentative ${attempt} ${nom} échec: ${e.message}`); await sleep(5000*attempt); }
  }
  if (!done) console.log(`ECHEC ${nom} — quota ?`);
  await sleep(2000);
}
