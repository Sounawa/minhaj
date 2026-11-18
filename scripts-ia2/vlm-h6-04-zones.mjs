// Z2-38 — hadith-6ep leçon 3 «التنافس في الخير» (pp.24-28)
// — Round 1 : lectures VLM par bandes (structure complète de la leçon)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';

const COMMON = `Recadrage d'un manuel scolaire marocain d'hadith (6e année primaire traditionnel, en arabe), leçon «التنافس في الخير» (hadith d'Abû Ḏarr, Nawawî 26 : «ذهب أهل الدثور بالأجور...»), sens de lecture droite→gauche. TRANSCRIS mot à mot ce qui est imprimé, avec les voyelles, sans jamais compléter par mémoire d'un texte connu. Si une zone contient un bandeau décoratif calligraphique, transcris-le lettre par lettre. Les crochets [ ] et guillemets « » doivent être restitués tels qu'imprimés.`;

// (nom, page, dpi, x0,y0,x1,y1 en pt, question)
const ZONES = [
  // ===== p.24 : cartouche + objectifs + تمهيد =====
  ['p24-top', 24, 600, 30, 100, 610, 340,
   `Haut de la première page de la leçon: bandeau/cartouche décoratif (numéro et titre de leçon ?), puis un label de rubrique (probablement «أهداف الدرس»), puis 3 objectifs numérotés. TRANSCRIS: (1) le cartouche-titre lettre par lettre ; (2) le label de rubrique ; (3) les 3 objectifs MOT À MOT avec la numérotation exacte (1-, 2-, 3-). L'objectif 2 commence par «أن أذكر» ou autre chose ? L'objectif 3 commence par «أقتدي» ou «أن أقتدي» ?`],
  ['p24-tamhid', 24, 600, 30, 330, 610, 520,
   `Rubrique تمهيد: le paragraphe complet (5-6 lignes) + les questions qui le suivent. TRANSCRIS tout mot à mot. Donne la forme EXACTE du premier mot du paragraphe (يظنّ ؟ يقدر ؟ غير). La phrase «كما أن هناك أعمالا مباحة تتحول بالنية الحسنة إلى عبادة يؤجر فاعلها» est-elle exacte ? Les questions finales sont «فما هذه الأعمال؟ وما فضلها؟ وما أثر النية في المباحات؟» ou autre ?`],
  ['p24-hadith-start', 24, 600, 30, 520, 610, 740,
   `Bloc du hadith (rubrique الحديث الشريف ou similaire): bandeau éventuel, puis isnad «عن أبي ذر رضي الله عنه أيضاً...» puis le début du hadith «قالوا: يا رسول الله ذهب أهل الدثور بالأجور...» jusqu'à «...قال:». TRANSCRIS tout mot à mot. (1) Le bandeau au-dessus dit-il «الحديث الشريف» ? (2) L'isnad exact : «عن أبي ذر رضي الله عنه أيضاً أنه قال:» ou «أن ناسا من أصحاب رسول الله ﷺ قالوا» ? (3) La partie «يصلون كما نصلي ويصومون كما نصوم ويتصدقون بفضول أموالهم» est-elle dans le hadith ici ?`],
  // ===== p.25 : fin du hadith + gloses =====
  ['p25-hadith-end', 25, 600, 30, 50, 610, 260,
   `Haut de page: fin du hadith. TRANSCRIS tout mot à mot: «...وكل تكبيرة صدقة وكل تحميدة صدقة وكل تهليلة صدقة وأمر بالمعروف صدقة ونهي عن منكر صدقة وفي بضع أحدكم صدقة. قالوا: يا رسول الله أيأتي أحدنا شهوته ويكون له فيها أجر؟ قال: أرأيتم لو وضعها في الحرام أكان عليها فيها وزر؟ فكذلك إذا وضعها في الحلال كان له أجر» puis la référence [رواه مسلم]. Vérifie: «أكان عليه فيها وزر» ou «أكان عليها فيها وزر» ? La référence finale exacte entre crochets ?`],
  ['p25-note-tarjama', 25, 600, 30, 270, 610, 360,
   `Petite note après le hadith, avant les gloses. TRANSCRIS-la mot à mot (probablement «تقدمت ترجمة الراوي في الدرس الثاني.»). Y a-t-il un numéro ou une ponctuation particulière ?`],
  ['p25-ban-sharh', 25, 600, 30, 360, 610, 415,
   `Bandeau décoratif de rubrique au-dessus des gloses. TRANSCRIS-le lettre par lettre. Est-ce «الشرح» ou «الفهم» ? Décris l'anatomie de la 2e lettre (ش a 3 points, ف 1 point) avant de conclure.`],
  ['p25-gloses1', 25, 600, 30, 400, 610, 545,
   `Les gloses (rubrique الشرح/الفهم), première série. TRANSCRIS chacune mot à mot: «الدثور: ...» / «الأجور: ...» / «فضول: ...» / «تسبيحة: ...». Donne les définitions exactes et complètes (la glose الدثور est-elle «بضم الذال جمع دثر بفتحها وهو المال الكثير» ?).`],
  ['p25-wazr', 25, 600, 30, 590, 610, 660,
   `Une glose isolée (probablement «وزر: ...»). TRANSCRIS-la mot à mot avec sa définition exacte (ذنب ؟ إثم ؟ حمل الذنب ؟ autre ?).`],
  ['p25-istikhlal', 25, 600, 30, 640, 610, 770,
   `Bas de page: bandeau de rubrique (probablement «استخلاص المضامين») + le premier item numéroté. TRANSCRIS le bandeau lettre par lettre, puis l'item 1 mot à mot («أستخرج الفقرة الدالة على تنافس الصحابة رضوان الله عليهم في الخير» ?). Y a-t-il un item 2 commencé en bas de page ?`],
  // ===== p.26 : استخلاص suite + التحليل =====
  ['p26-istikhlal2', 26, 600, 30, 40, 610, 160,
   `Haut de page: suite de la rubrique استخلاص المضامين (items numérotés). TRANSCRIS chaque item mot à mot avec sa numérotation exacte. Item attendu: «أستخرج من الحديث فضل الذكر والأمر بالمعروف» et «أستخلص من الحديث ما يحول العادة عبادة» — vérifie les formes exactes («ما يحول» ou «ما يحول العادة إلى عبادة» ?).`],
  ['p26-intro-tahlil', 26, 600, 30, 160, 610, 265,
   `Zone de transition: fin éventuelle d'item, puis bandeau de rubrique (probablement «التحليل») et phrase d'intro «يشتمل حديث الرسول ﷺ على ما يأتي:» puis le sous-titre «أولاً: تنافس الصحابة في الخير». TRANSCRIS tout mot à mot (le premier mot de l'intro est-il «يشتمل» ou autre ?).`],
  ['p26-awwalan', 26, 600, 30, 265, 610, 500,
   `Paragraphe de la section أولاً: تنافس الصحابة في الخير (7-8 lignes). TRANSCRIS tout mot à mot: «التنافس في الخيرات من أخلاق الصحابة رضوان الله عليهم؛ فقد كانوا ...». Donne exactement: (1) le verbe après «فقد كانوا» (يتنافسون ؟ يتنافس ؟) ; (2) ce qui suit «التي تبلغهم» ; (3) le mot après «أن الأغنياء» (حازوا ؟ خاروا ؟) ; (4) la fin du paragraphe («فأرشدهم ﷺ إلى أعمال أخرى...» — quelle est la fin exacte ?).`],
  ['p26-thaniyan', 26, 600, 30, 490, 610, 720,
   `Sous-titre «ثانياً: الصدقة تشمل كل أنواع الخير والمعروف» + paragraphe complet jusqu'en bas de page. TRANSCRIS tout mot à mot. Donne: (1) le début du paragraphe («بين في قوله ﷺ...» ou «تبين في قوله...» ?) ; (2) la citation interne complète ; (3) la phrase «فذكر الله بالتسبيح والتكبير والتحميد والتهليل وإرشاد الناس...» — que dit-elle exactement après «وإرشاد الناس» (وتحذيرهم من كذا ?) ; (4) la fin «...كما يثاب على الصدقة بالمال».`],
  // ===== p.27 : ثالثاً? + مما يستفاد + tableau =====
  ['p27-top', 27, 600, 30, 30, 610, 215,
   `Haut de page: Y a-t-il un sous-titre «ثالثاً: ...» avant le paragraphe «وفي قول النبي ﷺ وفي بضع أحدكم صدقة بيان أن...» ? TRANSCRIS tout ce qui est imprimé sur cette zone mot à mot, y compris un éventuel sous-titre. Le paragraphe parle des الزوجان والمقاصد الحسنة — transcris-le entièrement.`],
  ['p27-mustafad', 27, 600, 30, 210, 610, 380,
   `Rubrique «مما يستفاد من هذا الحديث:» + les items. TRANSCRIS le bandeau/titre et chaque item mot à mot avec ses puces (dashes). Combien d'items ? Attendus: الصدقة تشمل كل أنواع الخير والمعروف / فضيلة التسبيح وسائر الأذكار والأمر بالمعروف والنهي عن المنكر / النيات الصادقة تجعل المباحات طاعات يثاب عليها صاحبها / حرص الصحابة على السبق إلى الخيرات والتنافس في الأعمال الصالحة.`],
  ['p27-table-top', 27, 600, 30, 380, 610, 570,
   `Zone sous مما يستفاد: titre de rubrique ou consigne (probablement التقويم) + éventuel premier item + début de tableau. TRANSCRIS tout mot à mot: la consigne exacte, les items numérotés éventuels, les en-têtes de colonnes du tableau s'il y en a. Le tableau oppose-t-il des comportements (ذكر الله / الغفلة عن ذكر الله) ?`],
  ['p27-table-bot', 27, 600, 30, 550, 610, 770,
   `Bas de page: suite du tableau. TRANSCRIS toutes les cellules visibles mot à mot (rangée par rangée, droite→gauche). Les cellules contiennent des expressions comme «المداومة على ذكر الله / الغفلة عن ذكر الله», «التنافس في الخير / الكسل والخمول», «التمتع بالمباحات دون قصد التقرب إلى الله / ...». Donne le nombre de colonnes et de rangées.`],
  // ===== p.28 : التقويم + الاستثمار + الإعداد القبلي =====
  ['p28-taqwim', 28, 600, 30, 70, 610, 250,
   `Haut de page: items numérotés de la rubrique التقويم (ou suite du tableau). TRANSCRIS tout mot à mot: item 1 «أستخلص من الحديث خلقا من أخلاق الصحابة رضي الله عنهم للاقتداء» ? item 2 «هناك من يرى أن الصدقة تنحصر في المال؛ أناقش هذا الرأي» ? item 3 «أذكر أمثلة أخرى للمباحات التي تتحول بالنية إلى عبادات» ? Donne la numérotation exacte et s'il y a des cellules de tableau entre les items.`],
  ['p28-citation', 28, 600, 30, 250, 610, 480,
   `Rubrique الاستثمار (bandeau + consigne éventuelle) + citation d'un texte d'Abû Ḏarr avec référence [عون المعبود شرح سنن أبي داود 6/121 بتصرف]. TRANSCRIS tout mot à mot: le bandeau, la consigne, la citation complète «عن أبي ذر قال: قلت يا رسول الله ذهب الأغنياء بالأجر...» (avec toutes ses lignes: يصلون ويصومون ويحجون... وأنتم فيك صدقة رفعك العظم عن الطريق صدقة وهداك الطريق صدقة وعونك الضعيف بفضل قوتك صدقة...) et la référence EXACTE (chiffres: 121/6 ? 6/121 ?).`],
  ['p28-exercises', 28, 600, 30, 470, 610, 690,
   `Bas de page: items numérotés de l'استثمار + rubrique الإعداد القبلي (bandeau + consigne + 2 items). TRANSCRIS tout mot à mot: «1- أستخرج من النص الصدقات التي لم يرد ذكرها في حديث الدرس» / «2- أبين أثر هذه الصدقات في تقوية العلاقات الاجتماعية» (vérifie la formulation) puis «أحفظ حديث الدرس الموالي وأنجز ما يأتي: 1- أشرح: سلامى - أعدل بين اثنين - أميط الأذى 2- أستخرج الصدقات الواردة في الحديث» (vérifie chaque mot).`],
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

for (const [nom, pg, , , , , , Q] of ZONES) {
  const out = `${DIR}/vlm-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const img = fs.readFileSync(`${DIR}/crops/vlm-${nom}.png`).toString('base64');
  console.log(`\n======== ${nom} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 3 && !done; attempt++) {
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
