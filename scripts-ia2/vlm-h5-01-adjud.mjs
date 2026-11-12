// Z2-1 — adjudications par zooms 300 dpi (pages 13-17)
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-01';
const jobs = [
  { img: 'z-013-top.png', ask: `Demi-page haute d'un manuel arabe d'hadith (5ᵉ primaire marocain), leçon « التعريف بالمؤلف والمؤلف ». Transcris EXACTEMENT en arabe, mot à mot, vocalisation imprimée comprise : (1) le titre de la leçon avec son numéro ; (2) les trois objectifs (أهداف الدرس) ; (3) le paragraphe التمهيد ENTIÈREMENT (attention aux mots حظي/اقتنوا/بأن — écris ce qui est réellement imprimé lettre par lettre) ; (4) les premiers mots de l'encadré النص. Marque [؟] si un mot est illisible. Ne devine pas.` },
  { img: 'z-013-bot.png', ask: `Demi-page basse d'un manuel arabe d'hadith. Elle contient la fin du paragraphe التمهيد puis un encadré (النص) citant l'imam al-Nawawī dans l'introduction des Quarante. Transcris EXACTEMENT en arabe mot à mot : (1) la fin du تمهيد ; (2) TOUTE la citation de l'encadré, vocalisation comprise, jusqu'à la référence finale [مقدمة الأربعين النووية]. Mot illisible : [؟].` },
  { img: 'z-014-top.png', ask: `Demi-page haute d'un manuel arabe d'hadith, rubrique التفهم. Transcris EXACTEMENT en arabe mot à mot : (1) le titre التفهم et le mot الشرح ; (2) chaque glose (الشرح) ligne par ligne — pour chaque terme glosé écris le terme EXACTEMENT tel qu'imprimé suivi de sa définition (notamment la 3e glose : quel est le terme glosé — الأذان؟ الفضائل؟ المفاهيم ?) ; (3) les deux numéros de استخلاص المضامين (attention : le 2e commence par « أن أدرك ... » — écris ce qui est réellement imprimé) ; (4) le titre qui suit (التحليل ?) et la phrase d'introduction complète qui le suit.` },
  { img: 'z-014-bot.png', ask: `Demi-page basse d'un manuel arabe d'hadith : biographie de l'imam al-Nawawī (1. الإمام النووي). Transcris EXACTEMENT en arabe mot à mot tout le paragraphe, lettre par lettre, vocalisation comprise. Points d'attention : les épithètes après الحافظ (قدوة؟ حجة؟) ; l'année de naissance ; « نوى وهي بلدة ... » (بسيطة؟ بسيح؟ ناحية؟) ; l'année où son père l'amena à Damas et son âge ; le nombre de leçons par jour et le mot après « درسا » (تحريكا؟ تصحيحا؟ تدريسا؟). Mot illisible : [؟].` },
  { img: 'z-015-top.png', ask: `Demi-page haute d'un manuel arabe d'hadith : suite de la biographie de l'imam al-Nawawī (ses professeurs, élèves, œuvres, mort). Transcris EXACTEMENT en arabe mot à mot TOUT le passage avant le titre « 2. الإمام ابن دقيق العيد ». Points d'attention lettre par lettre : « درس على ... » (le nom du ou des professeurs — الأستاذان؟ البرهان ابن خلكان؟ الرحابي؟) ; « وزين/واخذ اللقاء عند ... » ; les trois élèves (صدر الدين سليمان ...؟ أحمد بن ...؟ علاء الدين ...؟) ; la liste des œuvres ; la date et le lieu de mort. Mot illisible : [؟].` },
  { img: 'z-015-bot.png', ask: `Demi-page basse d'un manuel arabe d'hadith : biographie de l'imam Ibn Daqīq al-ʿĪd (2. الإمام ابن دقيق العيد). Transcris EXACTEMENT en arabe mot à mot TOUT, lettre par lettre : la généalogie (محمد بن علي بن وهب بن متاع؟ مطيع؟) et ses laqabs ; l'année et le lieu de naissance (قرية ... من أجناد على ساحل البحر الأحمر) ; son établissement (نشأ بقوص...) ; la charge (ولاية القضاء) et l'année ; ses œuvres (إحكام الأحكام؟ الإيمام؟ الاقتراح؟ شرح المطرزي؟) ; l'année de sa mort. Mot illisible : [؟].` },
  { img: 'z-016-top.png', ask: `Demi-page haute d'un manuel arabe d'hadith, rubrique « ثانيا: مكانة الأربعين النووية ». Transcris EXACTEMENT en arabe mot à mot : (1) le titre et la phrase d'introduction ; (2) les TROIS premières puces (-) en entier, lettre par lettre (attention : « التزام الإمام النووي ... الصحة؟ في كل أحاديثه » — écris le mot réel ; « معظمها في صحيح البخاري ومسلم » ?) ; (3) le début de la 4e puce avec le hadith « من حفظ ... » jusqu'à « الزمرة الفقهاء والعلماء ». Mot illisible : [؟].` },
  { img: 'z-016-bot.png', ask: `Demi-page basse d'un manuel arabe d'hadith. Transcris EXACTEMENT en arabe mot à mot : (1) la FIN de la 4e puce (les deux riwāyāt « وفي رواية ... وفي رواية أخرى ... » + la référence [شعب الإيمان للبيهقي]) ; (2) la 5e puce ENTIÈRE (تلقّي الناس ... شرقا وغربا? حفظا وتعليما?) ; (3) le titre « وما يستفاد من هذه المقدمة » et les TROIS puces qui suivent, lettre par lettre (attention à la 3e : « إبراز فضل العلماء؟ إذ كان فضل العلماء؟ في جمع أحاديث النبي ... وبيان هديه للناس »). Mot illisible : [؟].` },
  { img: 'z-017-top.png', ask: `Demi-page haute d'un manuel arabe d'hadith. Transcris EXACTEMENT en arabe mot à mot : (1) la rubrique التقويم et ses trois numéros ; (2) le titre de la rubrique suivante (الاستثمار ?) ; (3) TOUTE la citation de l'encadré (passage de l'introduction d'al-Nawawī sur les savants qui ont compilé les Quarante : عبد الله بن المبارك، محمد بن أسلم الطوسي...) lettre par lettre jusqu'à « المتقدمين والمتأخرين », avec la vocalisation imprimée. Mot illisible : [؟].` },
  { img: 'z-017-bot.png', ask: `Demi-page basse d'un manuel arabe d'hadith. Transcris EXACTEMENT en arabe mot à mot : (1) la question qui suit l'encadré (« اذكر ثلاثة من ... ») ; (2) le titre de la dernière rubrique de la page — écris-le EXACTEMENT (الأعداد القبلية ? الأعماد القبلية ?) — puis TOUTE la rubrique : la phrase d'intro (أحفظ حديث الدرس المقبل...) et les numéros 1-2-3 lettre par lettre (notamment le n°1 : أعرّف براوي الحديث ... عمر بن الخطاب ؟) ; (3) le numéro de page en bas. Mot illisible : [؟].` },
];

async function main() {
  const zai = await ZAI.create();
  const out = [];
  for (const j of jobs) {
    const b64 = fs.readFileSync(`${DIR}/${j.img}`).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: j.ask },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ]}],
        model: 'glm-5v-turbo', max_tokens: 2000,
      });
      const txt = res.choices[0].message.content;
      out.push(`\n\n========== ${j.img} ==========\n` + txt);
      console.log(`${j.img} OK (${txt.length} car)`);
      fs.writeFileSync(`${DIR}/adjudications.md`, out.join(''));
    } catch (e) {
      console.log(`${j.img} FAIL: ${e.message}`);
      out.push(`\n\n========== ${j.img} = FAIL: ${e.message} ==========\n`);
    }
  }
  fs.writeFileSync(`${DIR}/adjudications.md`, out.join(''));
  console.log('Écrit:', `${DIR}/adjudications.md`);
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
