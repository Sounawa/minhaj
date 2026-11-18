// Z2-36 — VLM round 5 : zooms ultra-ciblés à choix multiples sur les points restants.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-02';
const S = 1200 / 72.0;

const COMMON = `Zoom très agrandi d'un verset coranique calligraphié (police moucharabieh) d'un manuel marocain. Réponds par l'analyse LETTRE PAR LETTRE des formes imprimées (points au-dessus/en-dessous, boucles ouvertes/fermées, queues) — jamais par mémoire d'un texte connu.`;

const ZONES = [
  ['mum-premier-mot', 13, 143, 574, 176, 610,
   `C'est le DÉBUT d'un verset, juste après «قال الله تعالى:» (à droite, coupé). Il y a d'abord un ornement d'ouverture ﴿. Puis le premier mot. QUESTION : ce premier mot est-il «فَمَنْ» (fā' 1 point au-dessus + mīm boucle + nūn point) ou «وَمَنْ» (wāw tête ronde sans point + mīm + nūn) ou «وَنَضَعُ» (wāw + nūn + ḍād grande boucle + 'ayn) ou «وَتَمَّتْ» (wāw + tā' 2 points + mīm + tā') ? Décris chaque lettre du premier mot puis donne-le.`],
  ['mum-fin-l2', 13, 442, 606, 566, 632,
   `Ce sont les 2-4 DERNIERS mots d'un verset sur les balances (موازين), avant un médaillon. Sont-ils «هُمُ الْمُفْلِحُونَ» ou «الَّذِينَ خَسِرُوا أَنْفُسَهُمْ» ou «فِي جَهَنَّمَ خَالِدُونَ» ou autre ? Transcris lettre par lettre.`],
  ['mum-medailion', 13, 404, 606, 448, 632,
   `Médaillon ornemental de fin de verset coranique. Contient-il un numéro à l'intérieur ? Si oui, sa valeur exacte (chiffres occidentaux 103 ? 102 ? ou arabo-orientaux ١٠٣ ? ١٠٢ ?). Décris les chiffres visibles.`],
  ['baq-fin-l2', 13, 440, 262, 566, 284,
   `Suite et fin d'un verset coranique (le verset commence par ﴿وَمَا كَانَ اللهُ...). Les mots visibles ici : sont-ils «لِيُضِيعَ إِيمَانَكُمْ» ou autre chose ? Transcris lettre par lettre, puis décris ce qui suit (ornement ﴾ ?).`],
  ['baq-ref-digits', 13, 383, 262, 416, 284,
   `Référence coranique entre crochets : [البقرة: ...]. Les TROIS chiffres du numéro de verset : la valeur EXACTE imprimée est-elle 142 ou 143 ? Décris le dernier chiffre : ٢ (deux bosses en haut, courbe ouverte) ou ٣ (trois bosses, une en haut et une au milieu + courbe) ? Donne la valeur des 3 chiffres.`],
  ['taw-ref-l2', 15, 108, 410, 275, 434,
   `Début d'une ligne : référence coranique entre crochets [التوبة: ...] suivie du début de «وَمِنْهُمْ مَنْ يَبِيعُهَا لِلشَّيْطَانِ...». Donne la valeur EXACTE des chiffres du numéro de verset (111 ? 112 ? 113 ?) — décris le dernier chiffre : ١ (trait vertical simple) ou ٢ (deux bosses) ou ٣ (trois bosses) ?`],
  ['sul-r1-zoom', 16, 330, 494, 637, 528,
   `Première ligne du tableau (colonne السلوكات). Le texte de la cellule : «محبة الناس والنصح لهم» (نصح = nūn + ṣād + ḥā') ou «محبة الناس والصدق عليهم» (صدق = ṣād + dāl + qāf) ou autre ? Décris les lettres du 2e mot de la paire après «وال» et la préposition finale (لهم ou عليهم ?).`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

for (const [nom, pg, x0, y0, x1, y1] of ZONES) {
  const fp = `${DIR}/crops/vlm5-${nom}.png`;
  if (!fs.existsSync(fp)) {
    execSync(`python3 -c "
from PIL import Image
S=${S}
im=Image.open('${DIR}/r1200/p${pg}.png')
c=im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S)))
c=c.resize((int(c.width*0.8),int(c.height*0.8)),Image.LANCZOS)
c.save('${fp}')
"`);
  }
}

for (const [nom, , , , , , Q] of ZONES) {
  const out = `${DIR}/vlm5-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const img = fs.readFileSync(`${DIR}/crops/vlm5-${nom}.png`).toString('base64');
  console.log(`\n======== ${nom} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 2 && !done; attempt++) {
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
  await sleep(2000);
}
