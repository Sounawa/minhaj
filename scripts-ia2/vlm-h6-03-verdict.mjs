// Z2-37 — VERDICT FINAL p.23 : candidats vs pixels (protocol strict de vérification).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03';

const COMMON = `Manuel scolaire marocain, verset coranique en police moucharabieh maghrébine. On te donne DEUX CANDIDATS pour le texte imprimé. TA MISSION: comparer PIXEL PAR PIXEL chaque mot du candidat avec l'image. Pour chaque mot du candidat: CONCORDE / NE CORRESPONDE PAS / ILLISIBLE. Puis rends un VERDICT global: candidat A, candidat B, ou AUCUN (et dans ce dernier cas transcris ce que tu vois). Ne choisis JAMAIS un candidat par préférence de mémoire: uniquement les pixels.`;

const ZONES = [
  ['v1-verdict', 23, 1200, 40, 118, 610, 180,
   `Le VERSAT 1 complet (2 lignes dans le cadre, après «1- قال الله تعالى:») avec médaillon(s) ۝ et référence [sourate: num].
CANDIDAT A: ﴿وَلَوْ شَاءَ رَبُّكَ لَجَعَلَ النَّاسَ أُمَّةً وَاحِدَةً وَلَا يَزَالُونَ مُخْتَلِفِينَ ۝ إِلَّا مَن رَّحِمَ رَبُّكَ ۚ وَلِذَٰلِكَ خَلَقَهُمْ ۗ وَتَمَّتْ كَلِمَةُ رَبِّكَ لَأَمْلَأَنَّ جَهَنَّمَ مِنَ الْجِنَّةِ وَالنَّاسِ أَجْمَعِينَ﴾ [هود: 119]
CANDIDAT B: ﴿لَقَدْ أَرْسَلْنَا رُسُلَنَا بِالْبَيِّنَاتِ وَأَنزَلْنَا مَعَهُمُ الْكِتَابَ وَالْمِيزَانَ لِيَقُومَ النَّاسُ بِالْقِسْطِ﴾ [الحديد: 25]
Analyse mot à mot les DEUX candidats, décris les chiffres des médaillons et de la référence (nom de sourate lettre par lettre), puis VERDICT.`],
  ['v2-verdict', 23, 1200, 40, 150, 610, 228,
   `Le VERSET 2 complet (3 lignes: après «وقال الله تعالى: ﴿», puis suite, puis fin) avec médaillon ۝ et référence [طه: num].
CANDIDAT A: ﴿وَأْمُرْ أَهْلَكَ بِالصَّلَاةِ وَاصْطَبِرْ عَلَيْهَا ۖ لَا نَسْأَلُكَ رِزْقًا ۖ نَحْنُ نَرْزُقُكَ ۗ وَالْعَاقِبَةُ لِلتَّقْوَىٰ﴾ [طه: 132]
CANDIDAT B: ﴿وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦ أَزْوَاجًا مِّنْهُمْ زَهْرَةَ الْحَيَاةِ الدُّنْيَا لِنَفْتِنَهُمْ فِيهِ ۚ وَرِزْقُ رَبِّكَ خَيْرٌ وَأَبْقَىٰ﴾ [طه: 131]
Analyse mot à mot les DEUX candidats, décris les chiffres du médaillon et de la référence, puis VERDICT.`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

fs.mkdirSync(`${DIR}/crops/verd`, { recursive: true });
for (const [nom, pg, dpi, x0, y0, x1, y1] of ZONES) {
  const fp = `${DIR}/crops/verd/${nom}.png`;
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

for (const [nom, , , , , , , Q] of ZONES) {
  const out = `${DIR}/vlm-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const img = fs.readFileSync(`${DIR}/crops/verd/${nom}.png`).toString('base64');
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
  if (!done) console.log(`ECHEC ${nom} — quota ?`);
  await sleep(2000);
}
