// Z2-40 — vague VLM d'ajustement (si quota revenu) : mots disputés de la leçon 5.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-06';
const COMMON = `Recadrage d'un manuel scolaire marocain d'hadith (arabe, 6e primaire traditionnel), leçon «البر حسن الخلق». TRANSCRIS mot à mot ce qui est imprimé, sans compléter par mémoire d'un texte connu. Voyelles : reproduis-les telles qu'imprimées.`;

// (nom, page, dpi, x0,y0,x1,y1 en pt, question)
const ZONES = [
  ['a1-cartouche', 36, 600, 85, 50, 555, 155,
   `Cartouche-titre. TRANSCRIS lettre par lettre: (1) «الدرس» + NUMÉRO (chiffre arabe ٥ ou occidental 5 ? décris sa forme) ; (2) le titre mot à mot avec voyelles ; (3) tout autre élément.`],
  ['a2-madud', 37, 1200, 340, 138, 475, 165,
   `Le mot entre «بْنِ رَبِيعَةَ،» et «فِي الشَّامِيِّينَ». TRANSCRIS-le lettre par lettre avec voyelles (المعدود ? معدود ? غير ذلك ?) et décris chaque lettre. TRANSCRIS aussi «بن ربيعة» et «في الشاميين» pour contexte.`],
  ['a3-kunya', 37, 1200, 270, 226, 480, 252,
   `La phrase «...بْنِ خُزَيْمَةَ، يُكْنَى ... . أَسْلَمَ سَنَةَ ... عِنْدَمَا وَفَدَ عَلَى رَسُولِ اللهِ ﷺ،». TRANSCRIS mot à mot: (1) خزيمة (avec ou sans ز ?) ; (2) la kunya après يكنى (أبا شداد ? أبا سالم ? — décris CHAQUE lettre: ش ou س ? د ou ل ?) ; (3) l'année (تسع ? سبع ?).`],
  ['a4-lahu', 37, 1200, 350, 254, 520, 278,
   `Le début de la ligne «وَلَهُ ... أَحَادِيثُ. وَكَانَ قَارِئًا لِكِتَابِ اللهِ...». TRANSCRIS mot à mot — y a-t-il un mot entre «وله» et «أحاديث» (عِدَّةُ ? بِضْعَةُ ? rien ?) ?`],
  ['a5-tahlil-tail', 37, 1200, 60, 695, 400, 735,
   `Fin de la page. TRANSCRIS mot à mot: «...مَرْضِيٍّ. [??] فِي تَزْكِيَةِ؟ النَّفْسِ؟» — après «مرضي» viennent quel(s) mot(s) avant la fin de ligne ? Décris lettre par lettre les mots entre «مرضي» et «النفس» (هو في تزكية النفس ? وما هو في تربية النفس ? autre chose ?).`],
  ['a6-citation', 38, 1200, 130, 74, 565, 112,
   `La citation en haut de page. TRANSCRIS mot à mot avec voyelles: «... بِالضَّمِّ فِي تَغْذِيَةِ؟ الْبَدَنِ» [الفتوحات الوهبية على الأربعين النووية؛ ص: 214] — (1) le PREMIER mot (قَالَ ? وَالْبِرُّ ? كَالْبِرُّ ? décris: ق ou ك ? combien de mots ?) ; (2) تَغْذِيَةِ (ت-غ) ou تَعْذِيَةِ (ت-ع) ? ; (3) الْبَدَنِ ou الْبَتَنِ ? ; (4) le numéro de page chiffre par chiffre.`],
  ['a7-nafra', 38, 1200, 280, 618, 360, 652,
   `Le mot entre «يُورِثُ» et «فِي الْقَلْبِ». TRANSCRIS lettre par lettre et DÉCRIS la première lettre: ن (bol avec point DESSUS) ? ذ (dāl avec point DESSUS) ? ز (forme pointue avec point DESSUS) ? ث (3 points) ? Donne le mot complet avec voyelles (نَفْرَةً ? ذَفْرَةً ? زَفْرَةً ?).`],
  ['a8-qabil', 38, 1200, 420, 700, 470, 738,
   `Le mot entre «قَابَلَ» et «بَيْنَهُمَا» (fin de page). TRANSCRIS-le lettre par lettre avec voyelles et décris chaque lettre (كُلٌّ ? كِلْتَيْهِمَا ? كَلِمَتَيْهِمَا ? غير ذلك ?). S'il y a aussi «هُوَ» après بينهما, confirme-le.`],
  ['a9-badl', 38, 1200, 320, 402, 480, 438,
   `Le mot entre «وَ» et «فِي الْإِحْسَانِ» (الْبَذْلُ ou الْبَدْلُ). DÉCRIS la 2e lettre: ذ avec UN point AU-DESSUS, ou د SANS point ? Donne le mot complet avec voyelles.`],
  ['a10-islah', 39, 1200, 320, 440, 540, 476,
   `Le 2e mot: «إِصْلَاحِ» ou «إِضْلَاحِ». DÉCRIS la 2e lettre: ص (boucle SANS point) ou ض (boucle AVEC UN point AU-DESSUS) ? Donne le mot complet. TRANSCRIS aussi le mot suivant (القلب) et le contexte «أهمية ... القلب بأنواع البر».`],
  ['a11-furqan', 40, 600, 90, 402, 560, 452,
   `L'ayah encadrée. TRANSCRIS-la ENTIÈREMENT mot à mot avec voyelles (probablement «وَعِبَادُ الرَّحْمَنِ الَّذِينَ يَمْشُونَ عَلَى الْأَرْضِ هَوْنًا») puis la référence [الفرقان: 63-77] et «إِلَى آخِرِ السُّورَةِ».`],
  ['a12-ruwah', 36, 600, 230, 600, 470, 626,
   `La référence sous le premier hadith. TRANSCRIS-la mot à mot ([رواه مسلم] ? autre ?).`],
  ['a13-darami', 36, 1200, 130, 696, 340, 720,
   `La fin de la référence du 2e hadith: «...أَحْمَدَ بْنِ حَنْبَلٍ وَال...». TRANSCRIS le dernier mot lettre par lettre (الدَّارِمِي ? الدَّرَامِي ? — ordre des lettres: د-ا-ر-م-ي ou د-ر-ا-م-ي ?) puis ce qui suit (بِإِسْنَادٍ حَسَنٍ]).`],
  ['a14-muhawara', 38, 1200, 190, 375, 350, 410,
   `Les mots entre «وَالْإِنْصَافُ فِي الْمُعَامَلَةِ،» et «وَالْعَدْلِ». TRANSCRIS mot à mot (وَالرِّفْقُ فِي الْمُحَاوَرَةِ ? الْمُحَاوَلَةِ ? — décris la lettre entre ا-و-ا et ة: ر ou ل ?).`],
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
for (const [nom, , , , , , , Q] of ZONES) {
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 900,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.slice(0, 450));
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${nom} échec: ${e.message.slice(0, 80)}`); await sleep(4000*attempt); }
  }
  if (!done) console.log(`ECHEC ${nom}`);
  await sleep(1500);
}
