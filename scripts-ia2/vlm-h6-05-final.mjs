// Z2-39 — ROND 4 (final) : إماطة/إزالة p.32 + tableau complet p.35
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';
const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-05';
const COMMON = `Recadrage d'un manuel scolaire marocain d'hadith (arabe), leçon «شكر الله على نعمة الجوارح». Sens de lecture droite→gauche. PROTOCOLE : pour le mot disputé, décris CHAQUE lettre (points au-dessus/dessous, hampes hautes, boucles) puis conclus «CONCORDE avec le candidat X» ou «NE CORRESPOND PAS — je lis ...». Ne complète jamais par mémoire.`;
const ZONES = [
  ['p32-imata-word', 32, 1200, 225, 556, 340, 584,
   `Un mot imprimé entre «إلى» (à droite) et «كل» (à gauche). CANDIDATS: (A) «إِمَاطَةَ» (5 lettres: hamza-kasra + mīm boucle ronde + alif + ṭāʾ avec GRANDE hampe verticale + tāʾ marbūṭa) (B) «إِزَالَةَ» (5 lettres: hamza-kasra + zāy petite dent avec 1 point au-dessus SANS hampe haute + alif + lām + tāʾ marbūṭa). Décris la 2e lettre (boucle ronde de mīm ou dent pointue de zāy ?) et la 4e lettre (hampe verticale haute de ṭāʾ ou hampe de lām ?). Conclus.`],
  ['p35-jadwal-full', 35, 600, 30, 255, 615, 385,
   `Tableau complet d'une activité scolaire (3 colonnes). TRANSCRIS: (1) la ligne de consigne au-dessus du tableau si visible ; (2) les 3 EN-TÊTES de colonnes EXACTEMENT (colonne droite: الجوارح ou الجسد ? — décris les lettres: ج-و-ا-ر-ح ou ج-س-د ?) ; (3) les étiquettes de chaque ligne de la 1re colonne (اللسان ? اليدان ? الرجلان ? autres ?) ; (4) le 3e en-tête (colonne gauche) mot à mot — CANDIDATS: (A) «الشكر بترك العباد» (B) «الشكر بترك العصيان» (C) «الشكر بترك المعصية» (D) autre — décris le dernier mot lettre par lettre ; (5) indique quelles cellules sont vides. Donne la structure (nb colonnes × nb lignes).`],
];
const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
fs.mkdirSync(`${DIR}/crops`, { recursive: true });
for (const [nom, pg, dpi, x0, y0, x1, y1] of ZONES) {
  const fp = `${DIR}/crops/vlm-${nom}.png`;
  const S = dpi / 72.0;
  execSync(`python3 -c "
from PIL import Image
S=${S}
im=Image.open('${DIR}/r${dpi}/p${pg}.png')
c=im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S)))
if ${dpi} == 1200:
    c=c.resize((c.width*2, c.height*2), Image.LANCZOS)
c.save('${fp}')
"`);
}
for (const [nom, pg, , , , , , Q] of ZONES) {
  const out = `${DIR}/vlm-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const img = fs.readFileSync(`${DIR}/crops/vlm-${nom}.png`).toString('base64');
  console.log(`\n======== ${nom} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 2 && !done; attempt++) {
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
  await sleep(2000);
}
