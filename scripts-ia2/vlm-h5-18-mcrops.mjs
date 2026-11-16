// Z2-20 — hadith-5ep leçon pdf-18 — microcrops VLM (letter-analyzed)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-18';

const ASKS = {
  'mc-m1-obj23-p98.jpg': `Microcrop très zoomé d'un manuel arabe : les objectifs 2 et 3 de « أهداف الدرس ».
Lis LETTRE PAR LETTRE et transcris les deux objectifs complets avec tous les diacritiques.
Objectif 2 : le verbe après « أن » — est-ce « أدرك » (d-r-k) ou « أذكر » (dh-k-r) ? Le kāf vient-il avant ou après le rāʾ ?
Objectif 3 : transcris-le intégralement, lettre par lettre.`,
  'mc-m2-tamhid-p98.jpg': `Microcrop zoomé : le milieu du « تمهيد » (3 lignes).
Transcris mot à mot, en t'arrêtant sur : (1) « وهم متساوون في ... » (le complément exact : أصل الخلقة ? أصل الإنسانية ?) ; (2) « فكلهم من آدم وآدم من تراب » ? (3) la phrase contenant « روابط » : quel est le verbe et la structure exacte (« تجمعهم بهذا روابط متينة ... » ?) ; (4) ce qui suit : « أساسها الإسلام ? بناها الإسلام على ... » ; (5) la fin de ligne : « ... ومحبة شعارها أن تحب لأخيك ما تحب لنفسك » ?`,
  'mc-m3-questions-p98.jpg': `Microcrop zoomé : la fin du « تمهيد » (les questions rhétoriques) et le haut de l'encadré du hadith.
Transcris tout ce qui est imprimé : les deux questions finales du تمهيد (sont-elles « فما معنى محبة الخير للناس ؟ وما مظاهرها التي تجسدها ؟ » ?) et le haut de l'encadré.`,
  'mc-m4-duaa-bustan-death-p99.jpg': `Microcrop zoomé : trois lignes de la biographie d'Anas.
Ligne 1 (invocation) : « دعا له النبي ﷺ فقال : اللهم ... » — transcris l'invocation LETTRE PAR LETTRE jusqu'à la fin (بارك له في ماله وولده ... ? et la fin exacte : واغفر له ? واغفر ذنبه ?).
Ligne 2 : « وكان له ... في السنة مرتين » — le nom exact (بستان ? ثمر ?) et le verbe (يحمل ? يحمل؟).
Ligne 3 : « وهو آخر من مات من الصحابة بالبصرة سنة ... » — liste EXACTE des variantes d'années.`,
  'mc-m5-sharh2-p99.jpg': `Microcrop très zoomé : la deuxième entrée du « الشرح ».
Transcris-la LETTRE PAR LETTRE. Questions : (1) l'entrée commence par quel mot (المحبة ? المودة ?) ; (2) « الميل إلى ما يوافق ... » — le dernier mot : المحب (celui qui aime) ou المحبوب (celui qui est aimé) ? ; (3) « والمراد ... » — y a-t-il « بها هنا » ? et le mot avant « الخير له » (رجاء ? محبة ? إرادة ?).`,
  'mc-m6-istikhlas-p99.jpg': `Microcrop zoomé : « استخلاص المضامين » (2 items).
Transcris chaque item LETTRE PAR LETTRE depuis le début.
Item 1 : le premier mot — « أحدد ? أستخرج ? » (avec le préfixe أُ).
Item 2 : le premier mot — « أبين ? أستخرج ? إبراز ? » puis « من الحديث وجه الحث على إرادة الخير للناس » ?`,
  'mc-m7-fudayl-p100.jpg': `Microcrop zoomé : l'anecdote du Fuḍayl.
Transcris LETTRE PAR LETTRE. Arrête-toi sur le segment central : « إن كنت تحب أن يكون الناس مثلك ، فما ... النصيحة ... » — quel est EXACTEMENT le mot entre « فما » et « النصيحة » (lettre par lettre : أدّت ? نصّت ? بلّغت ?) et le mot après « النصيحة » (لك ? لكَ ?) ; et la fin « كيف وأنت تحب أن يكونوا دونك ؟ ».`,
  'mc-m8-ibnhibban-p101.jpg': `Microcrop zoomé : la fin du premier tiret de « ثانيا ».
Transcris LETTRE PAR LETTRE : « والمراد نفي كمال الإيمان كما في حديث : « لا ... عبد حقيقة الإيمان حتى يحب للناس ما يحب لنفسه من الخير » . [صحيح ابن حبان] أما أصله فحاصل بدون هذه الصفة . »
Le verbe après « لا » — lis-le lettre par lettre : يبلغ (b-l-gh) ? يذوق (dh-w-q) ? يؤمن (hamza-m-n) ?`,
  'mc-m9-mystery-bullet1-p101.jpg': `Microcrop zoomé : zone entre le titre « ثالثا » et le premier tiret.
(1) Transcris la ligne décorée/encadrée éventuelle après le titre « ثالثا : مظاهر محبة الخير للناس » — y a-t-il une phrase d'introduction (« لمحبة الخير للناس مظاهر وعلامات تدل على أن المسلم ... ») ? Transcris-la mot à mot.
(2) Puis le premier tiret : « - أنه يفرح لفرحه ، فيسره ما يسر ... » — le dernier mot de cette proposition : « يسره » ou « يسر أخاه » ? Et « ولا يكون ذلك حتى يحب له ما يحب لنفسه من الخير » ?`,
  'mc-m10-yuamilu-p101.jpg': `Microcrop zoomé : le début du dernier tiret de « ثالثا ».
Transcris LETTRE PAR LETTRE : « - أن يعامله بـ... ما يحب أن يعامل به كما جاء في صحيح مسلم أن النبي ﷺ قال ... » — après « بيعامله بـ », y a-t-il « ما » seul ou « مثل ما » ?`,
  'mc-m11-yustafad1-p102.jpg': `Microcrop zoomé : premier item de « ومما يستفاد من الحديث ».
Transcris-le LETTRE PAR LETTRE : « أن المؤمن مع المؤمن كالنفس الواحدة ، فـ... أن يحب له ما يحب لنفسه من حيث إنهما نفس واحدة ».
Le connecteur après « فـ » : « ينبغي » (y-n-b-gh-y) ? « حق » ? « على » ? Transcris le mot exact.`,
  'mc-m12-yustafad2-p102.jpg': `Microcrop zoomé : deuxième item de « ومما يستفاد من الحديث ».
Transcris-le LETTRE PAR LETTRE. Le premier mot après « أن » : « أواصر المحبة والإخاء » (a-w-ṣ-r) ou « أوصار » (a-w-ṣ-ā-r) ou autre ? Puis la suite exacte (« تبني مجتمعا متماسكا يسود فيه الأمن والسلام وتنتشر فيه السكينة والاطمئنان » ?).`,
  'mc-m13-yustafad3-p102.jpg': `Microcrop zoomé : troisième item de « ومما يستفاد من الحديث ».
Transcris-le LETTRE PAR LETTRE : « أن ائتلاف قلوب الناس وانتظام أحوالهم وتحقيق مبدأ التعايش فيما بينهم يكون بالمحبة ويزداد ... » — transcris la FIN exacte de l'item (ce qui suit « ويزداد »).`,
  'mc-m14-taqwim1-p102.jpg': `Microcrop zoomé : la première question du « التقويم ».
Transcris-la LETTRE PAR LETTRE : commence-t-elle par « هل » ? quel est le sujet exact et le verbe (يتعارض ? تتعارض ?) ?`,
};

async function main() {
  const zai = await ZAI.create();
  for (const [img, ask] of Object.entries(ASKS)) {
    const out = `${DIR}/z-${img.replace('.jpg', '.txt')}`;
    if (fs.existsSync(out)) { console.log(`skip ${img}`); continue; }
    const b64 = fs.readFileSync(`${DIR}/${img}`).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: ask },
          { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 2000,
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
