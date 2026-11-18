// Z2-38 — Round 3e : les 3 boîtes d'en-tête de l'organigramme p27 + cellule bas-droite + mot وهد?اك
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';
const COMMON = `Micro-recadrage d'un manuel scolaire marocain d'hadith (arabe). TRANSCRIS UNIQUEMENT ce qui est imprimé, mot à mot. Décris les lettres (points, boucles, hampes) puis conclus par CONCORDE ou NE CORRESPOND PAS pour chaque candidat. Ne complète jamais par mémoire.`;

const ZONES = [
  ['p27-box-top', [27, 197, 394, 441, 440, 5],
   `Boîte centrale d'un organigramme, contenant 1-2 lignes de texte arabe calligraphié. TRANSCRIS son texte complet. Le contexte: un schéma opposant les bons comportements (أداء الفرائض، الإكثار من ذكر الله، التنافس في الخير، تصحيح النية) aux mauvais (ترك الفرائض، الغفلة، الكسل والخمول). Candidats pour la boîte: (A) «مُجَاهَدَةُ النَّفْسِ» ; (B) «مَا يَلِيقُ بِالْمُؤْمِنِ» ; (C) «أَخْلَاقُ الْمُؤْمِنِ» ; (D) un mot avec ال + بِالصَّحَابَةِ ou بِالصَّلَاةِ — transcris-le tel quel. Donne aussi le nombre de mots et de lignes.`],
  ['p27-line-under', [27, 140, 434, 580, 472, 4],
   `Une ligne de texte juste sous la boîte centrale d'un organigramme (ou la dernière ligne de la boîte). TRANSCRIS-la mot à mot. Candidats possibles: une consigne en «أُ...ُ» (verbe à la 1re personne) ou une phrase avec الصَّحَابَة. Transcris ce qui est réellement imprimé.`],
  ['p27-box-bleud', [27, 393, 474, 522, 510, 5],
   `Petite boîte bleue (côté DROIT) d'un organigramme, contenant 1-2 mots. Elle sert d'en-tête à la colonne des bons comportements (أداء الفرائض، الإكثار من ذكر الله...). TRANSCRIS son texte. Candidats: (A) «الْمُفْلِحُ» (م+ف+ل+ح) ; (B) «الْمُؤْمِنُ» ; (C) «الْمُطِيعُ» ; (D) autre — transcris lettre par lettre.`],
  ['p27-box-bleug', [27, 116, 474, 258, 510, 5],
   `Petite boîte bleue (côté GAUCHE) d'un organigramme, contenant 1-2 mots. Elle sert d'en-tête à la colonne des mauvais comportements (ترك الفرائض، الغفلة، الكسل والخمول...). TRANSCRIS son texte. Candidats: (A) «الْمُفَرِّطُ» ; (B) «الْخَاسِرُ» ; (C) «الْمُحْرُومُ» ; (D) «أَجْنَبٌ» ; (E) autre — transcris lettre par lettre (la 1re lettre est-elle un alif-hamza isolé ? y a-t-il un jīm ?).`],
  ['p27-cell-br', [27, 385, 658, 528, 748, 3],
   `Cellule du bas de la colonne DROITE d'un organigramme (2 lignes de texte). Candidats: (A) «تَصْحِيحُ النِّيَّةِ لِلتَّقَرُّبِ إِلَى اللهِ» (avec ح sans point comme 3e lettre du 1er mot) ; (B) «تَصْرِيحُ النِّيَّةِ...» (avec ر) ; (C) «تَحْصِيلُ النِّيَّةِ...». Décris la 3e lettre du premier mot (ح boucle ouverte SANS point vs ر hampe courbe) et la présence de «لِلْ» ou «ال» avant التَّقَرُّبِ. CONCORDE/NE CORRESPOND PAS.`],
  ['p28-hadi4', [28, 420, 402, 480, 430, 8],
   `UN SEUL MOT d'une citation: «وَ...» (juste avant «الطَّرِيقَ صَدَقَةٌ»). Candidats: (A) «هُدَاكَ» (هـ + د + ا + ك — 4 lettres, kāf final à hampe) ; (B) «هِدَايَتُكَ» (هـ + د + ا + ي + ة + ك — tāʾ marbūṭa à 2 points AVANT le kāf) ; (C) «هَادِي» (هـ + ا + د + ي). Décris les lettres une à une de droite à gauche et le nombre de lettres. CONCORDE/NE CORRESPOND PAS pour chacun.`],
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
  for (const psm of [7, 6, 11]) {
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
