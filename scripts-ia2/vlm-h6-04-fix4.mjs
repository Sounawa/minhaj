// Z2-38 — Round 3d : 4 dernières décisions (قال/فقال، الدال/الذال، هداك/هدايتك، organigramme p27)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';
const COMMON = `Micro-recadrage (grossi) d'un manuel scolaire marocain d'hadith (6e primaire, arabe), leçon «التنافس في الخير». TRANSCRIS UNIQUEMENT ce qui est imprimé. Vérifie lettre par lettre (points, boucles, hampes) et conclus par CONCORDE ou NE CORRESPOND PAS pour chaque candidat. Ne complète jamais par mémoire.`;

const ZONES = [
  ['p24-faqala2', [24, 45, 644, 145, 674, 6],
   `Un ou deux mots d'une fin de ligne du hadith: «...قَالَ:» ou «...فَقَالَ:». Candidats: (A) «قَالَ» (commence par qāf à 2 points, SANS lettre avant) ; (B) «فَقَالَ» (fāʾ à 1 point au-dessus AVANT le qāf). Décris ce qui est imprimé à droite du qāf. CONCORDE/NE CORRESPOND PAS pour (A) et (B).`],
  ['p25-dal2', [25, 402, 412, 472, 442, 6],
   `Un mot d'une glose: «ال...الِ» (entre «بِضَمِّ» et «جَمْعُ»). Le mot complet attendu: «الدَّالِ» ou «الذَّالِ». La lettre entre le premier «ال» et le «ال» final (ou avant le ā final): est-elle un د (angle SANS point) ou un ذ (angle AVEC 1 point au-dessus) ? Décris la zone au-dessus de cette lettre. CONCORDE/NE CORRESPOND PAS.`],
  ['p28-hadi3', [28, 398, 398, 485, 432, 6],
   `Un mot d'une citation: «وَ...َ الطَّرِيقَ» (après «...عَنِ الطَّرِيقِ صَدَقَةٌ،» et avant «الطريق صدقة»). Candidats: (A) «هُدَاكَ» (hāʾ + dāl + alif + kāf — 4 lettres, PAS de tāʾ marbūṭa) ; (B) «هِدَايَتُكَ» (hāʾ + dāl + alif + yāʾ + tāʾ marbūṭa à 2 points + kāf — 6 lettres) ; (C) «هَادِي» (hāʾ + alif + dāl + yāʾ). Décris les lettres une à une, de droite à gauche. CONCORDE/NE CORRESPOND PAS pour chacun.`],
  ['p27-diag-full', [27, 55, 385, 610, 778, 2],
   `Un ORGANIGRAMME complet d'un manuel scolaire (sens de lecture droite→gauche). Décris sa STRUCTURE précisément: (1) la boîte du haut et son texte ; (2) les boîtes du niveau suivant (droite et gauche) et leurs textes ; (3) les boîtes ou cellules des niveaux inférieurs, colonne par colonne (droite d'abord, puis gauche), avec leur texte complet. Indique les liens (traits verticaux). TRANSCRIS chaque texte mot à mot. Le thème: les comportements du croyant (مؤمن) — côté droit probablement positif (أداء الفرائض، الإكثار من ذكر الله، التنافس في الخير...), côté gauche négatif (الغفلة، الكسل والخمول...). Ne complète pas par mémoire: transcris ce que tu vois.`],
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
  // couche tesseract sur le même crop
  const tOut = `${DIR}/tcrops/t-${nom}`;
  try {
    execSync(`tesseract ${fp} ${tOut}-psm7 -l ara --tessdata-dir /home/z/my-project/scripts-translate/tessdata --psm 7`, {stdio:'pipe'});
    const tt = fs.readFileSync(tOut + '-psm7.txt', 'utf8').trim();
    console.log(`[tesseract ${nom} psm7]: ${tt || '(vide)'}`);
  } catch (e) { console.log(`[tesseract ${nom}]: échec`); }

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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1600,
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
