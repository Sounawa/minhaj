// Z2-19 — adjudication composites 600 dpi leçon 17 hadith-5ep (pp.93-97)
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-16';

const PLATES = [
  ['c17-G2-p93.jpg', 'Page 93, milieu : fin des objectifs + تمهيد complet (يتجاوز بعض الناس الأدب... وما آثاره المترتبة عليه؟). Transcris mot à mot.'],
  ['c17-G3-p93.jpg', 'Page 93, bas : fin du تمهيد + encadré du hadith «من حسن إسلام المرء تركه ما لا يعنيه» + référence. Transcris mot à mot.'],
  ['c17-H2-p94.jpg', 'Page 94, milieu : gloses (حسن/المرء/ما لا يعنيه/العناية) + استخلاص + début التحليل. Transcris mot à mot.'],
  ['c17-H3-p94.jpg', 'Page 94, bas : fin de l\'intro du التحليل + أولا: الحث على ترك ما لا يعني (début : حث النبي ﷺ في الحديث... وجعل ﷺ ترك المرء...). Transcris mot à mot.'],
  ['c17-I1-p95.jpg', 'Haut de la page 95 : fin de أولا («فقال ﷺ من حسن إسلام المرء تركه ما لا يعنيه» + «فهو المحسن الكف؟/الحق؟ لأنه...») + titre ثانيا + intro (حث الإسلام على ترك ما لا يعني لما له من أضرار...). Transcris mot à mot.'],
  ['c17-I2-p95.jpg', 'Page 95, milieu : items أ- ب- (تضييع الوقت النفيس... + citation الزرقاني + التفريط في أداء الواجبات). Transcris mot à mot, surtout la citation entre guillemets.'],
  ['c17-I3-p95.jpg', 'Page 95, bas : item ج- (الاشتغال بما لا يعني غالبا ما تكون عاقبته الندم...) + مالك بن دينار («إذا رأيت قساوة في قلبك...») + référence. Transcris mot à mot.'],
  ['c17-J1-p96.jpg', 'Haut de la page 96 : «وقد فهم السلف الصالح...» + item أ- (قول أبي ذر... «ومن حسب كلامه من عمله قل كلامه إلا فيما يعنيه») + référence. Transcris mot à mot.'],
  ['c17-J2-p96.jpg', 'Page 96, milieu : item ب- (ذكر مالك أنه قيل للقمان...) + ج- (الحسن البصري) + ثالثا + début (دل الحديث على أن من حسن إسلام المرء...). Transcris mot à mot.'],
  ['c17-J3-p96.jpg', 'Page 96, bas : citation de l\'imam الزرقاني («فإن الذي يغنيه الإسلام والإيمان العمل...») + référence + مما يستفاد. Transcris mot à mot, surtout la citation.'],
  ['c17-K1-p97.jpg', 'Haut de la page 97 : rubrique التقويم avec ses questions EXACTES (combien ? quelles formulations ?). Transcris mot à mot.'],
  ['c17-K2-p97.jpg', 'Page 97, milieu : encadré الاستثمار — citation Ġazālī complète («دع/حدِّث ما لا يعنيك في الكلام... إلى ...كان خاسرا») + référence. Transcris mot à mot avec le plus grand soin (calligraphie + vocalisation).'],
  ['c17-K3-p97.jpg', 'Page 97, bas : «أستخرج من النص: 1. ضابط الاشتغال بما لا يعني. 2. آثار الاشتغال بما لا يعني.» + الإعداد القبلي complet («أحفظ حديث الدرس المقبل وأنجز ما يلي:» + les 2 items sur محبة الخير للناس). Transcris mot à mot.'],
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
          { type: 'text', text: `Extrait haute résolution (600 dpi) d'un manuel scolaire marocain de hadith, 5e année primaire, leçon 17 «ترك ما لا يعني». ${ask}\n\nTranscris fidèlement, mot à mot, en conservant la vocalisation. Un mot illisible : [؟]. Réponds UNIQUEMENT avec la transcription.` },
          { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 2800,
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
