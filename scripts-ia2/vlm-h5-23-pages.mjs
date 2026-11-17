// Z2-27 — hadith-5ep leçon 23 «التقوى وحسن الخلق» (pp.125-130) — lectures VLM pleine page 150 dpi
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-23';
const COMMON = `Page entière (150 dpi) d'un manuel scolaire marocain d'hadith (5e année primaire traditionnel), leçon 23 «التقوى وحسن الخلق» (pp.125-130), sens de lecture droite→gauche.
TRANSCRIS TOUT ce qui est imprimé sur la page, rubrique par rubrique, mot à mot, avec la vocalisation. Balise les titres de rubrique comme [TITRE] ... [/TITRE], les encadrés comme [CADRE] ... [/CADRE], les hadiths et versets entre « » avec leurs références entre crochets. Les bandeaux décoratifs illisibles : [؟]. Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé.`;

const Q = {
  125: `Page 125 : le bandeau de titre de la leçon (transcris le numéro EXACTEMENT — chiffres arabes orientaux — et le titre complet التَّقْوَى), أهداف الدرس (3 objectifs numérotés), le texte d'introduction (تمهيد — avec la citation prophétique et SA RÉFÉRENCE entre crochets), la question de transition, l'en-tête الْأَحَادِيثُ et L'ENCADRÉ DU HADITH COMPLET (sanad double : Abū Ḏarr et Muʿāḏ + matn + référence entre crochets). Transcris tout.`,
  126: `Page 126 : la rubrique تَرْجَمَةُ الرَّاوِي (DEUX notices : Abū Ḏarr avec la citation prophétique et sa référence, puis Muʿāḏ b. Ǧabal — transcris dates de décès et éloges EXACTEMENT), puis الْفَهْمُ avec اَلشَّرْحُ (3 gloses en tirets : اتَّقِ اللهَ, ... , خَالِقِ النَّاسَ — transcris la glose du milieu MOT À MOT avec sa vocalisation) et اِسْتِنْتَاجُ الْمَضَامِينَ (2 questions numérotées). Transcris tout.`,
  127: `Page 127 : le début du التَّحْلِيل (phrase d'intro يشتمل الحديث...), le titre أولاً (الأمر بالتقوى...) avec : قول الرسول ﷺ «اتق الله حيثما كنت» أي في..., وسبب ورود هذا الحديث (l'histoire d'Abū Ḏarr al-Ġifārī — transcris le récit complet mot à mot), puis les phrases الأَمْرُ مُوَجَّهٌ لكل مسلم..., فالمسلم بالتقوى في أمكنة..., ثم le titre ثانياً (الأمر بإتباع السيئة الحسنة) avec وصف النبي ﷺ, وعلائقتهم..., قَدْ يَخِلُّ..., فالمطلوب... Transcris tout.`,
  128: `Page 128 : la suite de ثانياً : وَالْمُرَادُ بِالْحَسَنَةِ... (avec le hadith d'Abū Hurayra «الصلوات الخمس...» — transcris le matn complet et la fin مكفرات ما بينهن ما اجتنبت الكبائر), puis le titre ثالثاً (الأمر بحسن الخلق وفضله), puis 1. أهمية حسن الخلق (وصف النبي ﷺ بمخالقة الناس, «وخالق الناس بخلق حسن» أي..., ومن حسن الخلق معاملة الناس بالصدق...), puis le titre 2. فضل حسن الخلق (الخلق الحسن فضل عظيم...). Transcris tout.`,
  129: `Page 129 : la suite de 2. فضل حسن الخلق : محبة في الدنيا..., citation du hadith «ما شيء أثقل في ميزان المؤمن يوم القيامة من خُلق حسن...» AVEC sa référence entre crochets, puis «وصاحب الخلق الحسن من الناس...», la citation «إن من أحبكم إليّ...» avec sa référence, puis la rubrique وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ (items en TIRETS, transcris-les tous), puis le titre اَلتَّقْوِيمُ et les questions 1 et 2. Transcris tout.`,
  130: `Page 130 : la question 3 du تقويم (بماذا تنصح شخصاً...؟), puis la rubrique الاِسْتِثْمَار : l'ENCADRÉ DU VERSET [آل عمران: ...] (transcris le texte coranique vocalisé complet et la référence EXACTE), puis les 3 activités numérotées (تحدث عن الأخلاق..., بين من الآيات ما يؤكد..., أستخرج...), puis la rubrique الإِعْدَادُ الْقَبْلِيُ avec TOUS ses items numérotés (أحفظ حديث الدرس الآتي وأقوم بما يلي... — transcris chaque item mot à mot, y compris les mentions de la leçon suivante حفظ الله). Transcris tout.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const p of Object.keys(Q)) {
  const out = `${DIR}/vlm23-p-${p}.txt`;
  if (fs.existsSync(out)) { console.log(`skip p${p}`); continue; }
  const img = fs.readFileSync(`${DIR}/r150/p${p}.png`).toString('base64');
  console.log(`\n======== p${p} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q[p] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 2048,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 600 ? txt.slice(0, 300) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} p${p} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(3000);
}
