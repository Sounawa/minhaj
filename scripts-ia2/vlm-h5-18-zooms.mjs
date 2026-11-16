// Z2-20 — hadith-5ep leçon pdf-18 — zooms VLM composites 600 dpi (pp.98-103)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-18';

const ASKS = {
  'c18-A1-p98.jpg': `Bande 600 dpi d'un manuel marocain d'hadith (5e primaire), page 98, partie HAUTE : rubrique « أهداف الدرس » (3 items) puis début du « تمهيد ».
Transcris MOT À MOT les trois objectifs avec leurs diacritiques exacts. Points à trancher : objectif 1 : « أن أتعرف » ou « أن أعرف » ? objectif 2 : « أن أدرك » ou « أن أذكر » (verbe exact) ? objectif 3 : recopie-le intégralement.`,
  'c18-A2-p98.jpg': `Bande 600 dpi, page 98, milieu : le paragraphe du « تمهيد ».
Transcris-le MOT À MOT. Points à trancher : (1) début : « شاءت حكمة الله عز وجل أن يجعل الناس مختلفين من حيث ... » (2) après « آيات الله » : quel épithète exact (الدالة على / الجليلة) ? (3) « وهم متساوون في ... » (complément exact) ; (4) la phrase autour de « روابط متينة » : que dit-elle exactement (أساسها الإسلام ? بناها على ?) ; (5) la fin : « فما معنى ... وما مظاهرها ... ? » recopie les deux questions.`,
  'c18-A3-p98.jpg': `Bande 600 dpi, page 98, bas : l'encadré du hadith (bandeau « 13 »).
Transcris l'intégralité : l'isnād (عن أبي حمزة أنس بن مالك ... ?) et le matn mot à mot avec diacritiques, puis la référence entre crochets [ ... ] telle qu'imprimée.`,
  'c18-B1-p99.jpg': `Bande 600 dpi, page 99, haut : « ترجمة الراوي » (biographie d'Anas ibn Mālik).
Transcris MOT À MOT. Points à trancher : (1) la chaîne généalogique exacte (أنس بن مالك بن النضر الأنصاري النجاري الخزرجي) ; (2) le verbe avant « النبي ﷺ » dans la phrase de l'invocation (دعا له النبي ?) ; (3) le texte de l'invération « اللهم بارك ... » mot à mot ; (4) la phrase « وكان له ... في السنة مرتين » (le nom exact : ثمر ? يحمل ? يحصل ?) ; (5) les variantes de l'année de mort (سنة تسعين أو إحدى أو اثنتين أو ثلاث وتسعين ?) ; (6) la fin (على خلاف بين الرواة ?).`,
  'c18-B2-p99.jpg': `Bande 600 dpi, page 99, milieu : « الفهم / الشرح » (explication des mots).
Transcris chaque entrée MOT À MOT : « لا يؤمن : ... », « المحبة : الميل إلى ما يوافق المحب ... », et l'entrée suivante éventuelle (المراد بها هنا ? / المودة ?). Donne le libellé EXACT de chaque entrée et de sa glose.`,
  'c18-B3-p99.jpg': `Bande 600 dpi, page 99, bas : « استخلاص المضامين ».
Transcris les items MOT À MOT : item 1 (معنى « يحب لأخيه ما يحب لنفسه ») et item 2 (الحث على ... ?). S'agit-il de phrases nominales ou verbales ?`,
  'c18-C1-p100.jpg': `Bande 600 dpi, page 100, haut : introduction du « التحليل » + « أولا : معنى محبة الخير للناس » (premier paragraphe).
Transcris MOT À MOT. Points à trancher : (1) la phrase d'intro (« يدعو الحديث إلى ... في المحاور الثلاثة الآتية ») ; (2) « محبة الخير للناس كرم في النفس يدفع عنها ... » ; (3) le verbe relatif : « الرعونات النفسية التي تدفع إلى أخلاق ذميمة » (تدفع ? تنفع ? تؤدي ?) ; (4) la liste « مثل الحسد والأنانية والاستئثار ونحوها » ; (5) « ويجعل صاحبها يحب الخير لنفسه ولكل الناس » (يحب ? يحبّ ?).`,
  'c18-C2-p100.jpg': `Bande 600 dpi, page 100, milieu : suite du premier axe.
Transcris MOT À MOT : (1) « وقد عبر النبي ﷺ عن هذا بعبارة ... في قوله : حتى يحب لأخيه ما يحب لنفسه » (l'épithète de l'expression : أوجز وأبلغ ? أعمق وأبلغ ?) ; (2) « إذ بلغ بكرم هذه النفس إلى أن تحب لغيرها كل ما تحب لنفسها من الخير وليس مطلق الخير فحسب » (verbes exacts) ; (3) la citation de la رواية النسائي complète avec sa référence ; (4) « ومعناه : لا يكمل إيمان أحدكم حتى يحب لأخيه في الإسلام ما يحب لنفسه من الخير » ; (5) « ويحصل ذلك في أدنى مراتبه أن يحب له حصول مثل ما حصل لنفسه ومن أكملها أن يحب للناس أكثر مما هو عليه » (structure exacte).`,
  'c18-C3-p100.jpg': `Bande 600 dpi, page 100, bas : l'anecdote de الفضيل بن عياض et سفيان بن عيينة, puis « ومن مقتضى هذه المحبة ... ».
Transcris MOT À MOT. Points à trancher : (1) « يُحكى / يُحكي أن الفضيل بن عياض قال لسفيان بن عيينة : ... » ; (2) le milieu de la citation : « إن كنت تحب أن يكون الناس مثلك فما ... » (recopie le segment central EXACT) ; (3) « كيف وأنت تحب أن يكونوا دونك ? » ; (4) la phrase « ومن مقتضى هذه المحبة أن الإنسان كما يحب أن ينتصف من حقه ومظلمته ينبغي أن يبادر إلى إنصاف أخيه من نفسه إن كان له عنده مظلمة أو حق وإن كان عليه في ذلك مشقة » (forme exacte).`,
  'c18-C4-p100.jpg': `Bande 600 dpi, page 100, tout bas : « ثانيا : فضل محبة الخير للناس » (titre + phrase d'intro + premier tiret).
Transcris MOT À MOT : (1) l'intro (« لمحبة الغير وإرادة الخير له مكانة كبيرة في الإسلام تتجلى في : » ?) ; (2) le premier tiret (« أن ذلك من خصال الإيمان بل من واجباته التي لا يتم إلا بها، يدل على ذلك قول النبي ﷺ : لا يؤمن أحدكم ... والمراد نفي كمال ... »).`,
  'c18-D1-p101.jpg': `Bande 600 dpi, page 101, haut : suite du premier tiret de « ثانيا ».
Transcris MOT À MOT : (1) la fin de la phrase interrompue (« والمراد نفي كمال الإيمان كما في حديث : ... ») ; (2) le hadith cité : premier mot exact (« لا يذوق عبد حقيقة الإيمان حتى يحب للناس ما يحب لنفسه من الخير » ? — يذوق ? يؤمن ?) ; (3) sa référence [ ... ] ; (4) « أما أصله فحاصل بدون هذه الصفة » ?`,
  'c18-D2-p101.jpg': `Bande 600 dpi, page 101, haut-milieu : le deuxième tiret de « ثانيا ».
Transcris MOT À MOT. Points à trancher : (1) « أن الرجل إنما يحب لأخيه ما يحب لنفسه إذا سلم من ... » (liste EXACTE des traits : الحسد والغل والغش والحقد والأنانية ?) ; (2) le hadith « لا تدخلوا الجنة حتى تؤمنوا ولا تؤمنوا حتى تحابوا ... » avec sa référence EXACTE [ ... ] ; (3) la phrase de synthèse « فمحبة الخير للناس سبب لطهارة القلب من الحقد والحسد وغيرهما وعلامة على صلاح القلب وكمال الإيمان » ?`,
  'c18-D3-p101.jpg': `Bande 600 dpi, page 101, milieu : « ثالثا : مظاهر محبة الخير للناس » (titre + intro + premier tiret).
Transcris MOT À MOT : (1) l'intro (« لمحبة الخير للناس مظاهر وعلامات تدل على أن المسلم فعلا يحب لأخيه ما يحب لنفسه من ذلك : » ?) ; (2) le premier tiret (« أنه يفرح لفرحه فيسره ما يسره ولا يكون كذلك حتى يحب له ما يحب لنفسه من الخير » ?) ; (3) toute autre ligne imprimée dans cette bande (encadré, filet, citation éventuelle).`,
  'c18-D4-p101.jpg': `Bande 600 dpi, page 101, bas : les deux derniers tirets de « ثالثا ».
Transcris MOT À MOT : (1) « أنه يحزن لحزنه فيسوءه ما يسوءه كما في حديث النعمان بن بشير عن النبي ﷺ قال : مثل المؤمنين في توادهم وتعاطفهم وتراحمهم مثل الجسد إذا اشتكى منه عضو تداعى له سائر الجسد بالحمى والسهر » + sa référence ; (2) « أن يعامله بما يحب أن يعامل به كما جاء في صحيح مسلم أن النبي ﷺ قال : فمن أحب أن يزحزح عن النار ويدخل الجنة فلتأته منيته وهو يؤمن بالله واليوم الآخر وليأت إلى الناس الذي يحب أن يؤتى إليه » + sa référence.`,
  'c18-E1-p102.jpg': `Bande 600 dpi, page 102, haut : « ومما يستفاد من الحديث ».
Transcris les items MOT À MOT. Points à trancher : item 1 : « أن المؤمن مع المؤمن كالنفس الواحدة فـ ... » (la suite EXACTE) ; item 2 : le premier mot (« أن آصال المحبة والإخاء » ? « أن أوصار » ?) et la suite (« تبني مجتمعا متماسكا يسود فيه الأمن والسلام وتنتشر فيه السكينة والاطمئنان » ?) ; item 3 : « أن ائتلاف قلوب الناس وانتظام أحوالهم وتحقيق مبدأ التعايش فيما بينهم يكون بالمحبة ويزداد ... » (fin EXACTE).`,
  'c18-E2-p102.jpg': `Bande 600 dpi, page 102, milieu : « التقويم ».
Transcris les questions MOT À MOT. Point à trancher : question 1 — recopie-la intégralement (هل ... يتعارض ... ? quel est le sujet et le verbe exacts).`,
  'c18-E3-p102.jpg': `Bande 600 dpi, page 102, bas-milieu : l'encadré de l'« استثمار ».
Transcris la citation MOT À MOT : « قال الإمام ... : ودّت أن الناس ... » — qui est l'imam cité (le nom exact) et que dit la citation exactement (تعلموا هذا العلم ولم ينسب إلي منه شيء ?) + la référence entre crochets [ ... ] telle qu'imprimée.`,
  'c18-E4-p102.jpg': `Bande 600 dpi, page 102, bas : les questions de l'« استثمار » sous l'encadré.
Transcris-les MOT À MOT (2 questions).`,
  'c18-F1-p103.jpg': `Bande 600 dpi, page 103 : « الإعداد القبلي ».
Transcris MOT À MOT : l'intitulé, la phrase d'intro (« أحفظ حديث الدرس المقبل وأنجز ما يلي » ?) et les 2 items (point à trancher sur l'item 2 : « وأذكر علاقة الإيمان بإكرام الجار والضيف » ? ou « والصديق » ?).`,
  'c18-F2-p103.jpg': `Bande 600 dpi, page 103, partie basse (sous l'الإعداد القبلي).
Décris ce qui est imprimé dans cette bande : texte éventuel, en-tête de la leçon 19, image, ou page blanche ? Transcris tout caractère arabe visible.`,
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
