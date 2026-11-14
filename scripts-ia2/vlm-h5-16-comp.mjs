// Z2-18 — adjudication composites 600 dpi leçon 16 hadith-5ep (pp.88-92)
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-16';

const PLATES = [
  ['comp-A1-p88.jpg', 'Haut de la page 88 (leçon 16 « التورع عن الشبهات ») : bandeau titre + objectifs du cours. Transcris mot à mot les trois objectifs (أن...). Attention au 3e objectif : quel est le verbe exact et y a-t-il une préposition ? Transcris aussi le début du تمهيد.'],
  ['comp-A2-p88.jpg', 'Page 88, milieu : تمهيد de la leçon 16. Transcris mot à mot tout le passage, y compris la citation «تركتكم...» du Prophète et sa référence entre crochets, et la suite «لكنه قد تعرض أمور ملتبسة...».'],
  ['comp-A3-p88.jpg', 'Page 88, zone basse : fin du تمهيد («فما المراد بالشبهات؟...») et encadré du hadith avec isnād complet (عن أبي محمد الحسن بن علي...) + référence [رواه...]. Transcris mot à mot.'],
  ['comp-A4-p88.jpg', 'Page 88, bas : encadré du hadith «دع ما يريبك إلى ما لا يريبك» + référence du recueil. Transcris exactement la ligne de référence sous l\'encadré.'],
  ['comp-B1-p89.jpg', 'Haut de la page 89 : ترجمة الراوي (الحسن بن علي). Transcris mot à mot : la nasba complète (القرشي؟ الهاشمي المدني)، «ابن بنت رسول الله؟»، «ولد منتصف رمضان؟»، «ومات سنة...» (chiffre exact), «ودفن بالبقيع».'],
  ['comp-B2-p89.jpg', 'Page 89, milieu : note de bas de page sur السبط + encadré الفهم/الشرح : gloses de «سبط»، «دع»، «يريبك» (avec les indications grammaticales exactes : بفتح... وضم...، من راب وأراب، مشتق من...). Transcris mot à mot.'],
  ['comp-B3-p89.jpg', 'Page 89, bas : استخلاص المضامين + début du التحليل «يشتمل هذا الدرس على...» + أولا: معنى الشبهات : définitions de الحلال البين/اليقين، الحرام البين، الشبهة. Transcris mot à mot, en précisant les termes exacts البين ou اليقين.'],
  ['comp-C1-p90.jpg', 'Haut de la page 90 : fin de la définition de الشبهة + «فالورع اجتنابها؟» + titre ثانيا: موقف الشرع من الشبهات + début «حث النبي ﷺ في الحديث على ترك الشبهات للتباسها و...؟». Transcris mot à mot.'],
  ['comp-C2-p90.jpg', 'Page 90, milieu : «ذلك أن الأحكام الشرعية على قسمين: أحدهما...لا يخفى؟ على عموم الأمة...الحلال البين أو الحرام البين...» + «ثانيهما: ما لم يقطع فيه بتحريم ولا تحليل...» + «أي: نترك ما نشك في حرمته... و...؟ إلى ما لا تشك فيه منها» + référence [فتح الباري لابن رجب بتصرف]. Transcris mot à mot.'],
  ['comp-C3-p90.jpg', 'Page 90, bas : hadith «لا يبلغ العبد أن يكون من المتقين حتى يدع ما لا بأس به ...» (précise : محافظة؟ محاذرة؟ لما به بأس؟) + référence + «وهذه درجة من الورع أعلى من التي قبلها» + titre ثالثا + «1. ما لا يعفى عنه من الشبهات...» début. Transcris mot à mot.'],
  ['comp-D1-p91.jpg', 'Haut de la page 91 : types أ- ب- ج- de الاشتباه (كأن يشك الإنسان في المال أهو ملكه أو لا...؛ اختلاط الحلال بالحرام...؛ مثل الصيد...فإذا شك في ذكاته...؟ إلا بيقين الذكاة) + référence. Transcris mot à mot, surtout les phrases après «فإذا شك في ذكاته».'],
  ['comp-D2-p91.jpg', 'Page 91, milieu : «2. ما يعفى عنه من الشبهات» + intro («هناك أمور فيها معنى الشبهة لكنها...؟ لذلك لم...؟ حكمها وصارت من المعفو عنها») + les deux items (الأصل في الشيء؟ + من كثر شكه وأصيب بالوسواس...) + hadith de البخاري sur celui qui s\'imagine avoir rompu ses ablutions. Transcris mot à mot.'],
  ['comp-D3-p91.jpg', 'Page 91, bas : fin du hadith de البخاري («وهو محمول على الذي...؟ الشك كثيرا») + «ومما يستفاد من الحديث» : les deux items (أن الحلال المحض؟... بل تسكن إليه النفس؟... / أن التورع عن الشبهات...). Transcris mot à mot.'],
  ['comp-E1-p92.jpg', 'Haut de la page 92 : «أن التورع عن الشبهات يقتضي...» + التقويم (les 2 questions exactes). Transcris mot à mot.'],
  ['comp-E2-p92.jpg', 'Page 92, milieu : encadré الاستثمار «الورع أقسام» : les TROIS divisions dans l\'ordre exact (ورع الصديقين؟ المتقين؟ الصالحين؟) avec leurs définitions complètes + référence. Transcris mot à mot.'],
  ['comp-E3-p92.jpg', 'Page 92, bas : la consigne sous l\'encadré (أستخرج؟...أنواع التورع الواردة في النص مع بيان ما يعد منها وما لا...) + الإعداد القبلي complet («أحفظ حديث الدرس المقبل...» + les items numérotés sur la leçon 17 «الاشتغال بما لا يعني»). Transcris mot à mot.'],
];

async function main() {
  const zai = await ZAI.create();
  for (const [img, ask] of PLATES) {
    const p = `${DIR}/${img}`;
    if (!fs.existsSync(p)) { console.log(`ABSENT ${img}`); continue; }
    const out = `${DIR}/vlm-${img.replace('.jpg', '.txt')}`;
    if (fs.existsSync(out)) { console.log(`skip ${img}`); continue; }
    const b64 = fs.readFileSync(p).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: `Extrait haute résolution (600 dpi) d'un manuel scolaire marocain de hadith, 5e année primaire, leçon 16 «التورع عن الشبهات». ${ask}\n\nTranscris fidèlement, mot à mot, en conservant la vocalisation. Un mot illisible : [؟]. Réponds UNIQUEMENT avec la transcription.` },
          { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 3000,
        temperature: 0.1,
      });
      const txt = res?.choices?.[0]?.message?.content ?? JSON.stringify(res);
      fs.writeFileSync(out, txt);
      console.log(`OK ${img} (${txt.length} car)`);
    } catch (e) {
      console.error(`ÉCHEC ${img}: ${e.message}`);
    }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
