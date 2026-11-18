// Z2-37 — fix4 (DERNIER lot) : 5 mots disputés, crops r600 ×2 upscale (géométrie prouvée).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03';

const COMMON = `Manuel scolaire marocain d'hadith, leçon «تحريم الظلم». Texte naskh vocalisé ou bandeau calligraphique. Lecture droite→gauche. TRANSCRIS uniquement les pixels, mot à mot, avec voyelles. Décris les lettres des mots demandés une par une (points au-dessus/dessous, formes).`;

// [nom, page, x0, y0, x1, y1, question]
const ZONES = [
  ['b19-ban', 19, 150, 106, 610, 150,
   `Le BANDEAU décoratif de rubrique (calligraphie claire sur fond coloré) au-dessus des gloses «ضال: مائل عن...». TRANSCRIS-le lettre par lettre: est-ce «الفهم» (ا-ل-ف-ه-م) ou «الشرح» (ا-ل-ش-ر-ح) ou autre? Décris chaque lettre.`],
  ['b19-intro', 19, 380, 505, 610, 542,
   `La première ligne du commentaire التحليل (après le bandeau). TRANSCRIS-la mot à mot. Le PREMIER mot est-il «يُبيِّنُ» (ي-ب-ي-ن, 4 lettres) ou «يتضمنُ» (ي-ت-ض-م-ن, 5 lettres)? Décris les lettres du premier mot une par une.`],
  ['b19-glose1', 19, 40, 142, 610, 172,
   `UNE ligne de glose: «ضالٌّ: ...». TRANSCRIS-la mot à mot. Le mot après «عن» est-il «الصراط» (ص-ر-ا-ط) ou «الطريق» (ط-ر-ي-ق)? Décris les lettres de ce mot.`],
  ['b17-obj1', 17, 40, 182, 610, 212,
   `UNE ligne: le premier objectif de la leçon (après le bandeau أهداف الدرس). TRANSCRIS-la mot à mot avec voyelles. Le verbe après «أن» est-il «أَعْرِفَ» (ع-ر-ف, 3 lettres) ou «أَتَعَرَّفَ» (ت-ع-ر-ف, 4 lettres)? Le dernier mot est-il «للظلم» (deux lâm) ou «الظلم» (un lâm)? Décris lettre par lettre.`],
  ['b21-tasaa', 21, 330, 80, 610, 112,
   `UNE ligne (partie gauche de la première ligne de page): elle contient «...قلوبهم، و... حياتهم.». TRANSCRIS-la mot à mot. Le verbe avant «حياتهم» est-il «وتسعى» (ت-س-ع-ا, alif final, pas de د) ou «وتسعد» (ت-س-ع-د, avec د)? Décris la dernière lettre de ce mot.`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

fs.mkdirSync(`${DIR}/crops/fix4`, { recursive: true });
for (const [nom, pg, x0, y0, x1, y1] of ZONES) {
  const fp = `${DIR}/crops/fix4/${nom}.png`;
  if (!fs.existsSync(fp)) {
    const S = 600 / 72.0;
    execSync(`python3 -c "
from PIL import Image, ImageOps
S=${S}
im=Image.open('${DIR}/r600/p${pg}.png').convert('L')
c=im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S)))
c=c.resize((c.width*2, c.height*2), Image.LANCZOS)
c=ImageOps.autocontrast(c)
c.save('${fp}')
"`);
  }
}

for (const [nom, , , , , , Q] of ZONES) {
  const out = `${DIR}/vlm-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const img = fs.readFileSync(`${DIR}/crops/fix4/${nom}.png`).toString('base64');
  console.log(`\n======== ${nom} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 2 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 900,
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
