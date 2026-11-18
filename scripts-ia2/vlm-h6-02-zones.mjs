// Z2-36 — hadith-6ep leçon 1 «المسارعة في الخيرات» (pp.11-16)
// — lectures VLM ciblées sur les zones restées aveugles (versets coraniques en police
//    moucharabieh, chiffres de références [sourate: verset], mots à points ambigus,
//    bandeaux décoratifs de rubriques, en-têtes de tableau).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-02';
const S600 = 600 / 72.0;

const COMMON = `Recadrage d'un manuel scolaire marocain d'hadith (6e année primaire traditionnel, en arabe), leçon «المسارعة في الخيرات» (hadith d'Abû Mâlik al-Ash'arî), sens de lecture droite→gauche. TRANSCRIS mot à mot ce qui est imprimé, sans jamais compléter par mémoire d'un texte connu. Les références coraniques entre crochets [sourate: verset] utilisent des chiffres : transcris-les en chiffres et donne leur valeur. Si une zone est un bandeau décoratif calligraphique, transcris-le lettre par lettre du mieux possible.`;

// (nom, page, x0,y0,x1,y1 en pt, question)
const ZONES = [
  ['fussilat', 16, 40, 262, 600, 322,
   `Activité 1 de la rubrique الاستثمار. La ligne commence par «1- قال الله تعالى:» puis cite un verset coranique entre «...» et se termine par une référence entre crochets [فصلت: ...]. TRANSCRIS le verset ENTIÈREMENT mot à mot (2 lignes imprimées), puis la référence exacte avec la valeur du numéro de verset.`],
  ['muddathir', 13, 40, 155, 600, 200,
   `Fin de section «أولاً: الطهور» du commentaire. Après «واجتناب كل قبيح، قال الله تعالى:» il y a un verset coranique entre «...» suivi d'une référence entre crochets [المدثر: ...]. TRANSCRIS le verset mot à mot (il parle de purifier les vêtements), puis la référence exacte avec la valeur du ou des numéros de verset (un seul verset ou deux ?).`],
  ['baqara', 13, 40, 228, 600, 282,
   `Section sur «الطهور شطر الإيمان». Après «وقيل: المراد بالإيمان هنا: الصلاة، قال الله تعالى:» il y a un verset coranien entre «...» suivi de la référence [البقرة: ...] puis «أي صلاتكم». TRANSCRIS le verset mot à mot, puis la référence exacte : le numéro de verset est-il 142 ou 143 ? Donne la valeur EXACTE des chiffres imprimés.`],
  ['muminun', 13, 40, 570, 600, 632,
   `Section «ثانياً: التحميد والتسبيح». Après «على وزن الأعمال وثقل الموازين وخفتها، قال الله تعالى:» il y a un verset coranique sur 2 lignes suivi de la référence [المؤمنون: ...]. TRANSCRIS le verset mot à mot (il parle de balances lourdes), puis la référence exacte : la valeur des chiffres (102 ? 103 ? 102-103 ?).`],
  ['tawba', 15, 40, 392, 600, 435,
   `Section «خامساً: فضل السعي في طاعة الله». Après «فيعتقها من العذاب، كما قال الله تعالى:» il y a un verset coranique sur 2 lignes suivi de la référence [التوبة: ...]. TRANSCRIS le verset mot à mot (il parle d'acquérir les âmes et les biens des croyants), puis la référence exacte : la valeur des chiffres (111 ? 112 ?).`],
  ['urf', 12, 40, 145, 600, 175,
   `Notice du transmetteur (ترجمة الراوي) d'Abû Mâlik al-Ash'arî. La ligne contient «... وشهد المشاهد، ... بنصيحته لله ورسوله حتى في آخر حياته، سكن مصر...». Quel est EXACTEMENT le mot entre «المشاهد،» et «بنصيحته» : عُرِفَ (ayn, 1 point au-dessus, crochet ouvert) ou غُرِفَ (ghayn, 1 point au-dessus, tête fermée ronde) ou autre ? Décris la forme de la première lettre puis donne le mot.`],
  ['wafat', 12, 40, 205, 600, 230,
   `Même notice, dernière ligne : «توفي في خلافة عمر رضي الله عنه سنة ... ه.». Donne la valeur EXACTE des chiffres de l'année de mort (18 ? 81 ? autre ?) et la ponctuation autour.`],
  ['sulukat', 16, 30, 405, 610, 500,
   `Haut du tableau de l'activité 2 de الاستثمار («أتأمل السلوكات الآتية وأميزها وفق المطلوب في الجدول»). TRANSCRIS les en-têtes de colonnes EXACTEMENT : la colonne de droite (السلوكات ?), et les deux autres en-têtes (des formules du genre «ما يُساهم في تزكية النفس» / «ما يتناقض مع تزكية النفس» — donne la formulation exacte, mot à mot).`],
  ['bande-titre', 11, 40, 55, 600, 175,
   `Haut de page de la première page de la leçon. Il y a un bandeau décoratif (calligraphie). TRANSCRIS ce qui y est écrit lettre par lettre : numéro de leçon ? titre «المسارعة في الخيرات» ? autre chose ? Décris aussi ce qui est sous le bandeau jusqu'aux objectifs.`],
  ['bande-ahdaf', 11, 40, 165, 600, 210,
   `Petit bandeau/label au-dessus de la liste des 3 objectifs («أن أتعرف أعمالاً...»). TRANSCRIS-le lettre par lettre (probablement «أهداف الدرس» ou une icône avec label).`],
  ['bande-tamhid', 11, 40, 300, 600, 400,
   `Entre la liste des objectifs et le paragraphe «حث الإسلام على إتيان الطاعات...» il y a un bandeau décoratif de rubrique. TRANSCRIS-le lettre par lettre (probablement «تمهيد» ou «التمهيد»).`],
  ['bande-hadith', 11, 40, 462, 600, 550,
   `Avant le hadith «عن أبي مالك الأشعري...» il y a un bandeau décoratif de rubrique. TRANSCRIS-le lettre par lettre (probablement «الحديث» ou «متن الحديث»).`],
  ['bande-tarjama', 12, 40, 55, 600, 125,
   `Haut de page : bandeau décoratif avant «أبو مالك هو كعب بن عاصم...». TRANSCRIS-le lettre par lettre (probablement «ترجمة الراوي»).`],
  ['bande-tahlil', 12, 40, 548, 600, 648,
   `Entre «2- أذكر الصفات والفضائل...» et «هذا الحديث أصل من أصول الإسلام» il y a un bandeau décoratif de rubrique. TRANSCRIS-le lettre par lettre (probablement «التحليل»).`],
  ['bande-sabr', 14, 40, 405, 600, 460,
   `Entre la fin du paragraphe «ب- الصدقة برهان...» et «قوله ﷺ: «والصبر ضياء» معناه...» il y a peut-être un sous-titre. TRANSCRIS ce qui s'y trouve lettre par lettre (probablement «ج- الصبر ضياء»).`],
  ['bande-taqwim', 16, 40, 55, 600, 135,
   `Haut de page : bandeau décoratif avant la question «1- أين تتجلى أهمية الطهارة؟». TRANSCRIS-le lettre par lettre (probablement «التقويم»).`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

fs.mkdirSync(`${DIR}/crops`, { recursive: true });
for (const [nom, pg, x0, y0, x1, y1] of ZONES) {
  const fp = `${DIR}/crops/vlm-${nom}.png`;
  if (!fs.existsSync(fp)) {
    execSync(`python3 -c "
from PIL import Image
S=${S600}
im=Image.open('${DIR}/r600/p${pg}.png')
im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S))).save('${fp}')
"`);
  }
}

for (const [nom, pg, , , , , Q] of ZONES) {
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
