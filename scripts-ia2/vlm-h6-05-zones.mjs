// Z2-39 — hadith-6ep leçon 4 «شكر الله على نعمة الجوارح» (pp.29-35)
// — lectures VLM ciblées : cartouche-titre, bandeaux décoratifs, hadith de البخاري ومسلم,
//    citations (بينما رجل/يصبح على كل سلامى/الإيمان بضع/الغزالي إحياء), tableaux
//    (السلوكات p.34, الجدول p.35), texte souligné p.35, mots à points ambigus.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-05';

const COMMON = `Recadrage d'un manuel scolaire marocain d'hadith (6e année primaire traditionnel, en arabe), leçon «شكر الله على نعمة الجوارح» (hadith d'Abû Hurayra, al-Bukhârî et Muslim: «كل سلامى من الناس عليه صدقة...»), sens de lecture droite→gauche. TRANSCRIS mot à mot ce qui est imprimé, sans jamais compléter par mémoire d'un texte connu. Les références entre crochets utilisent des chiffres : transcris-les et donne leur valeur. Si une zone est un bandeau décoratif calligraphique, transcris-le lettre par lettre du mieux possible. Voyelles : reproduis-les telles qu'imprimées.`;

// (nom, page, dpi, x0,y0,x1,y1 en pt, question)
const ZONES = [
  ['p29-cartouche', 29, 600, 85, 55, 555, 148,
   `Cartouche-titre de la leçon (cadre décoratif, 2 lignes possibles). TRANSCRIS lettre par lettre: (1) le mot «الدرس» + le NUMÉRO (chiffre arabe ٤ ou occidental 4 ? décris sa forme) ; (2) le titre «...» mot à mot avec les voyelles. Y a-t-il un autre élément (ornement, basmala) ?`],
  ['p29-ahdaf', 29, 600, 40, 148, 610, 312,
   `Haut de page après le cartouche: (1) un bandeau/label au-dessus des objectifs — TRANSCRIS-le lettre par lettre (probablement «أهداف الدرس») ; (2) les 2 objectifs numérotés mot à mot avec voyelles. L'objectif 1 commence-t-il par «أن أتعرف عظمة نعمة الجوارح» ou autre chose ? L'objectif 2 : «أن أدرك أن استعمال جوارحي في الخير من الصدقات» ?`],
  ['p29-tamhid', 29, 600, 40, 305, 610, 500,
   `Zone de la rubrique تمهيد. TRANSCRIS: (1) le bandeau décoratif s'il est visible dans ce recadrage (probablement «تمهيد») ; (2) le paragraphe complet mot à mot avec voyelles (il commence par «كل يوم...» et contient «فأجد كل جارحة من جوارحي... عضوا من أعضائي، مفسلا من مفاصلي، أو حاسة من حواسي؛ نعمة...» — donne les formes EXACTES: مَفْصِلا ? نِعْمَةٌ ? le mot après «فيه» (الشمس ?) et le verbe (أُصبح ? تطلع ?)) ; (3) la question finale «فكيف أشكر الله على هذه النعم في كل يوم؟» — «هذه النعم» ou «هذه النعمة» ?`],
  ['p29-hadith-ban', 29, 600, 40, 490, 610, 570,
   `Zone au-dessus du cadre du hadith: (1) un bandeau décoratif — TRANSCRIS-le lettre par lettre (الحديث ? الحديث الشريف ? autre) ; (2) la première ligne de l'isnad «عن أبي هريرة رضي الله عنه قال: قال رسول الله ﷺ:...» mot à mot.`],
  ['p29-hadith', 29, 600, 40, 545, 610, 715,
   `Le hadith dans son cadre décoratif. TRANSCRIS-les ENTIÈREMENT mot à mot avec voyelles, de «كل سلامى...» jusqu'à «...وتميط الأذى عن الطريق صدقة». ثم «رواه البخاري ومسلم» — ou «متفق عليه» ? Précision demandée: (a) après «كل يوم» vient «يطلع فيه الشمس» ? (b) «وتعين الرجل في دابته» puis «فتحمله عليها» ou «فتحملها عليه» ? (c) «أو ترفع له عليها متاعه» — décris les points/lettres de «متاعه» ; (d) «وبكل خطوة تمشيها» ou «تخطوها» ?`],
  ['p30-tarjama', 29, 600, 40, 90, 610, 250,
   `Page 30, notice du transmetteur. TRANSCRIS: (1) le bandeau décoratif au-dessus (ترجمة الراوي ?) lettre par lettre ; (2) la notice ENTIÈRE mot à mot: «أبو هريرة رضي الله عنه. هو: عبد الرحمن بن صخر الدوسي...». Points précis: (a) le nasab exact («عبد الرحمن بن صخر الدوسي» ? décris les lettres de الدوسي) ; (b) l'année d'arrivée à Médine («سنة ... هـ» — quelle valeur ?) ; (c) le nombre de hadiths («روى عنه ... حديثا» — 5374 ? décris les chiffres) ; (d) «أكثر من ... من الصحابة والتابعين» (valeur ?) ; (e) «توفي عام ... هـ» — DÉCRIS les deux chiffres de l'année un par un (boucles, hampes) avant de conclure: 59 ? 95 ? autre ?`],
  ['p30-sharh-ban', 30, 600, 40, 290, 610, 340,
   `Petit bandeau décoratif entre la notice et les gloses. TRANSCRIS-le lettre par lettre (الشرح ? الفهم ? الفهم والشرح ?). Décris le nombre de mots visibles.`],
  ['p30-gloses', 30, 600, 40, 330, 610, 435,
   `Les gloses. TRANSCRIS chacune mot à mot: (1) «السلامى: ...» (la définition + la citation de القاضي عياض «وأصله عظام الكف والأصابع والأرجل ثم استعمل في سائر عظام الجسد ومفاصله» — vérifie chaque mot) ; (2) «تعدل: ...» (تفصل بالحق ? أو تقضي بالحق ?).`],
  ['p30-istikhlas', 30, 600, 40, 425, 610, 545,
   `Zone de la rubrique استخلاص. TRANSCRIS: (1) le bandeau décoratif lettre par lettre (استخلاص المضامين ?) ; (2) les 2 items numérotés mot à mot (1- أذكر النعم الواردة في الحديث / 2- ما حق الله على العباد في هذه النعم؟ — vérifie «على العباد» ou «عليّ»).`],
  ['p30-tahlil', 30, 600, 40, 540, 610, 680,
   `Zone de la rubrique التحليل: (1) le bandeau décoratif (en couleur) lettre par lettre (التحليل ?) ; (2) la phrase d'intro «يشمل هذا الدرس على ما يأتي:» (أو «يتضمن» ?) ; (3) le sous-titre «أولا: ...» mot à mot (نعمة الجوارح وشكر الله عليها ?).`],
  ['p30-awwal', 30, 600, 40, 675, 610, 745,
   `Fin de page 30, début du paragraphe de la section أولا. TRANSCRIS mot à mot: «خلق الله تعالى الإنسان في أحسن صورة، فسوى خلقته وجمل صورته، وأمده بالصحة والعافية فيه، وأسبغ عليه نعما كثيرة ظاهرة وباطنة، في بدنه ويديه...» — vérifie: «ظاهرة وباطنة» ou l'inverse ? «في بدنه» ou «ففي بدنه» ? Donne le DERNIER mot/mots de la page (jointure avec la page suivante).`],
  ['p31-awwal-end', 31, 600, 40, 70, 610, 205,
   `Haut de page 31, fin de la section أولا. TRANSCRIS mot à mot: «ورجليه وسمعه وبصره؛ إذ ما من عضو من أعضائه أو عظم من عظام جسمه إلا وفيه من نعمة الله عليه. وقد أرشدنا الرسول ﷺ في هذا الحديث إلى أن نعمة الجوارح نعمة عظيمة وجب أداء شكر الله عليها، فقال ﷺ: «كل سلامى من الناس عليه صدقة» أي على كل إنسان...». QUESTIONS: (a) après «أي على كل إنسان» viennent quel(s) mot(s) — «أن يتصدق كل يوم صدقة شكر» ? «في كل يوم» ? décris lettre par lettre ; (b) «إلا وفيه» ou «إلا فيه» ?`],
  ['p31-thani', 31, 600, 40, 200, 610, 385,
   `Sous-titre de section + intro. TRANSCRIS: (1) «ثانيا: من وجوه شكر الله على نعمة الجوارح» mot à mot ; (2) le paragraphe «الشكر من حقوق الله على عباده؛ ويكون شكر الله تعالى على نعمة الجوارح بالصدقات؛ وذلك عن طريق استعمال هذه الجوارح في وجوه الخير من العبادات والمعاملات. ومن تلك الوجوه:» — vérifie «الشكر» ou «فالشكر» ; «حقوق الله» ou «حق الله».`],
  ['p31-item1', 31, 600, 40, 400, 610, 545,
   `Premier وجيه. TRANSCRIS: (1) le sous-titre numéroté «1- إصلاح ذات البين» mot à mot ; (2) son paragraphe entier (de «قول ﷺ: «تعدل بين الاثنين صدقة» أي تصلح بينهما بالعدل...» jusqu'à «...والفرقة بينهم»). QUESTIONS: (a) «من أعظم الصدقات التي ... عليها الإنسان» — le verbe (يُؤجَّر ? يُوجَر ? يخرج ?) décris ses lettres ; (b) «لما له من أثر كبير» ou «أثره الكبير» ? ; (c) «وأنبذ الشحناء والتنازع والتقاطع والفرقة بينهم» — le premier mot (وأنبذ ? ونبذ ?).`],
  ['p31-item2', 31, 600, 40, 570, 610, 740,
   `Deuxième وجيه. TRANSCRIS: (1) le sous-titre numéroté «2- ...» mot à mot EN ENTIER (probablement «السعي في قضاء حوائج الناس ومساعدتهم» — donne sa forme exacte) ; (2) le paragraphe entier. QUESTIONS: (a) «صدقة ... عليها العبد عند الله تعالى» — le verbe (يثاب ? يستاب ? يشكر ?) décris ses lettres et points ; (b) «كما يساعد إنسانا في حمل يريد أن يضعه عن دابته» ou «في حملها» ? ; (c) «أو يحمله عليها» ou «لها» ou «عنها» ? ; (d) la fin «...التي يقوم بها المسلم ... للخير و... للغير» — donne les 2 formes exactes (محبا ? محبة ? نفعا ? قضاء ?).`],
  ['p32-item3', 32, 600, 40, 105, 610, 295,
   `Troisième وجيه (page 32). TRANSCRIS: (1) le sous-titre numéroté «3- الكلمة الطيبة» ; (2) le paragraphe entier mot à mot. QUESTIONS: (a) «فيه بيان فضل الكلمة الطيبة و... على التزامها» — le mot manquant (الحث ? وحث ?) ; (b) «الدال على الاحترام والمودة و...» (المحبة ?) ; (c) AVANT «فاحش القول» la liste «كإفشاء السلام؛ وذكر الله والصلاة على النبي ﷺ والدعاء بالخير؛ وتجنب...» — vérifie l'ordre exact ; (d) DERNIÈRE phrase: «والكلمة الطيبة هي من حسن الخلق الذي ... به المرء ... الناس» — le verbe (يكسب ? يسع ? يأتلف ?) décris ses lettres une par une, et la finale (كل الناس ? سعة الناس ?).`],
  ['p32-item4', 32, 600, 40, 325, 610, 490,
   `Quatrième وجيه. TRANSCRIS: (1) le sous-titre numéroté «4- ...» (probablement «الخطى إلى الصلاوات» — forme exacte ?) ; (2) le paragraphe: «قول الرسول ﷺ: «وبكل خطوة تمشيها إلى الصلاة صدقة» أي كل خطوة يخطوها المسلم إلى أداء الصلاة في الجماعة صدقة، وقد جاء في الحديث: «إذا توضأ فأحسن الوضوء ثم خرج إلى المسجد لا يخرجه إلا الصلاة لم يخط خطوة إلا رفعت له بها درجة وحط عنه بها خطيئة» [صحيح البخاري، كتاب الأذان، باب فضل صلاة الجماعة]» — vérifie la référence EXACTE (livre + chapitre) ; (3) la suite «يعني: ...» — le verbe et la finale (أعطي حسنة، وتكفر عنه خطيئة ? أُعطى حسنة، وحطت عنه خطيئة ?).`],
  ['p32-item5', 32, 600, 40, 485, 610, 712,
   `Cinquième وجيه. TRANSCRIS: (1) le sous-titre numéroté «5- ...» (probablement «إماطة الأذى عن الطريق») ; (2) le paragraphe introductif «يرشد قول الرسول ﷺ: «وتميط الأذى عن الطريق صدقة» إلى العناية بالمحيط وجمال البيئة والمبادرة إلى إماطة كل ما فيه أذى للإنسان أو غيره؛ لإدراك أن إماطة الأذى عن الطريق من فضائل الأعمال وشعب الإيمان كما جاء في الحديث الشريف؛ فعن أبي هريرة رضي الله عنه قال: قال رسول الله ﷺ: «الإيمان بضع وسبعون — أو بضع وستون — شعبة، فأفضلها قول لا إله إلا الله، وأدناها إماطة الأذى عن الطريق، و... شعبة من الإيمان» [صحيح مسلم، كتاب الإيمان، باب شعب الإيمان]» — QUESTIONS: (a) le mot entre «وأدناها إماطة الأذى عن الطريق» et «شعبة من الإيمان» (والحياء ? والخيا ? فالحياء ?) décris ses lettres ; (b) «بضع وسبعون» ou «بضع وسبعين» ? ; (c) vérifie la référence complète.`],
  ['p33-citation', 33, 600, 40, 68, 610, 148,
   `Haut de page 33: citation avec isnad. TRANSCRIS mot à mot: «وعن أبي هريرة رضي الله عنه قال: قال رسول الله ﷺ: «بينما رجل يمشي بطريق وجد غصن شوك على الطريق فأخره؛ فشكر الله له» فغفر له» — ou «فأخره فشكر الله له فغفر له» (ponctuation exacte) ? puis la référence [صحيح مسلم، كتاب البر والصلة والآداب، باب فضل إزالة الأذى عن الطريق] — vérifie chaque mot (الصلة ? وصلة ?).`],
  ['p33-item6', 33, 600, 40, 145, 610, 348,
   `Sixième وجيه. TRANSCRIS: (1) le sous-titre numéroté «6- ...» (probablement «ركعتا الضحى» — forme exacte avec le ta' marbuta ?) ; (2) l'intro «من عظم الصلاة ويسر الإسلام وترغيب المسلم ... بحقوق نعمة الجوارح ما جاء في قوله ﷺ: ...» — le(s) mot(s) entre «المسلم» et «بحقوق» (في القيام ? على أداء ?) ; (3) le hadith «يصبح على كل سلامى من أحدكم صدقة؛ فكل تسبيحة صدقة، وكل تحميدة صدقة، وكل تهليلة صدقة، وكل تكبيرة صدقة، وأمر بالمعروف صدقة، ونهي عن المنكر صدقة، ويجزي من ذلك ركعتان يركعهما من الضحى» ; (4) la référence [صحيح مسلم، كتاب صلاة المسافرين وقصرها، باب ...] — TRANSCRIS le chapitre complet ; (5) la suite «أي ...» jusqu'à «فإذا صلى ... كل عضو بوظيفته» (يكفي ? تفني ? — قام ? يقوم ?).`],
  ['p33-mustafad', 33, 600, 40, 425, 610, 672,
   `Zone de la rubrique «مما يستفاد...». TRANSCRIS: (1) le bandeau décoratif lettre par lettre (مما يستفاد من هذا الحديث ? مما يستفاد من الدرس ?) ; (2) les 3 items mot à mot. QUESTIONS précises: (a) item 1: «شكر الله على نعمة الجوارح من ... الله تعالى على عباده» (حقوق ? حق ?) ; (b) item 2: «اشتغال الجوارح في عبادة الله ونفع العباد والمحافظة على ...» (البيئة ? البقية ?) puis «...من أنواع الصدقات» (نوع ? نوعا ?) ; (c) item 3: «الصدقة مظهر عظيم لعبادة الله و...» (وشكره ? وشكرها ? décris la finale) puis «يؤدي فيه كل عضو من الأعضاء حقه من العبودية؛ طاعة لله تعالى وتذللا وتقربا إليه سبحانه» — le verbe après «الصدقة...» (يؤدي ? يودي ?) et la structure.`],
  ['p34-bandeaux', 34, 600, 40, 55, 610, 130,
   `Haut de page 34: il devrait y avoir un ou DEUX bandeaux décoratifs de rubriques (au-dessus des activités 1 et 2, et peut-être un autre au-dessus de l'activité 3). TRANSCRIS chaque bandeau lettre par lettre (التقويم ? الاستثمار ? أتدرب ?). Combien de bandeaux visibles dans cette zone et que disent-ils ?`],
  ['p34-items', 34, 600, 40, 120, 610, 262,
   `Les activités numérotées. TRANSCRIS chacune mot à mot: «1- أتأمل بديع صنع الله تعالى في جوارحي وأذكر نعم الله علي.» / «2- كيف أشكر الله على نعمة الجوارح في كل يوم؟» / «3- «...» أشرح ذلك ممثلا بنماذج من واقعي.» (TRANSCRIS la citation entre guillemets — «السعي في نفع العباد صدقة» ? «السعي في قضاء حوائج العباد صدقة» ? décris les lettres du 2e mot après «في») / «4- أوظف مكتسباتي من الدرس وأحدد موقفي من السلوكات في الجدول:». Vérifie la ponctuation et «ممثلا» ou «ممتلا».`],
  ['p34-table', 34, 600, 40, 262, 610, 462,
   `Le tableau des سلوكات. TRANSCRIS: (1) les en-têtes de colonnes EXACTEMENT (السلوكات | موقفي منها | ...? — le 3e en-tête: التعليل ? أعّلل ? autre) ; (2) chaque ligne: ligne 1 «... مساعدة الآخرين مخافة التهمة بالرياء» — le PREMIER mot (أتأخر ? أتأمل ? أثر ?) décris ses lettres ; ligne 2 «شارك في الأنشطة الاجتماعية بمدرستي» (ou «أشارك» ?) ; ligne 3 «... ولا أصلح بين الناس» — le début (أتهاون بنفسي ? أتهرب ? أتهاون في الإصلاح ?) décris lettre par lettre ; ligne 4 «أحافظ على نظافة مدرستي ومحيطي» (أمحيطي ?). Les cellules des colonnes 2-3 sont vides ? Combien de colonnes et de lignes ?`],
  ['p34-ghazali', 34, 600, 40, 488, 610, 726,
   `Citation de l'imam al-Ghazâlî. TRANSCRIS TOUT mot à mot avec la référence finale: «قال الإمام الغزالي رحمه الله: «اعلم أن الشكر من جملة مقامات السالكين وهو أيضا ... من علم وحال وعمل... فأما العلم فهو معرفة النعمة من المنعم، والحال هو ... الحاصل بإنعامه، والعمل هو القيام بما هو مقصود المنعم ومحبوبه... ويكون ذلك بالقلب واللسان والجوارح؛ فأما بالقلب فقصد الخير و... لكافة الخلق، وأما باللسان فإظهار الشكر لله تعالى بالتحميدات الدالة عليه، وأما بالجوارح فاستعمال نعم الله تعالى في طاعته والتوقي من الاستعانة بها على معصيته» [إحياء علوم الدين؛ ص 80 بتصرف]». QUESTIONS: (a) «وهو أيضا ...» (باب ? مقام ? tab ?) ; (b) «الحال هو ... الحاصل» (اللذة ? الفرح ?) ; (c) «فأما بالقلب فقصد الخير و... لكافة الخلق» (محبته ? محبة ?) ; (d) la valeur de la page dans la référence (80 ? 30 ? décris le(s) chiffre(s)) ; (e) «اعلم» ou «أعلم» ?`],
  ['p35-iidat', 35, 600, 40, 30, 610, 112,
   `Haut de page 35: bandeau décoratif de rubrique (probablement «الإعداد القبلي») + la première ligne «أتأمل النص وأجيب عما يأتي:». TRANSCRIS le bandeau lettre par lettre et la ligne mot à mot (أتأمل ? أتامل ?).`],
  ['p35-nass', 35, 600, 40, 108, 610, 218,
   `Activités 1 et 2. TRANSCRIS: (1) «1- أشرح ما تحته خط.» ; (2) LE TEXTE SOULIGNÉ qui suit (c'est un extrait du hadith de la leçon suivante, probablement «البر حسن الخلق...» ou un texte sur le شكر) — TRANSCRIS-LE ENTIÈREMENT mot à mot avec voyelles, et dis quelle(s) partie(s) est/sont soulignée(s) ; (3) «2- أبين كيف يكون الشكر بالعمل؛ وما مظاهر ذلك؟» (بالعمل ? للعمل ?).`],
  ['p35-jadwal', 35, 600, 40, 215, 610, 380,
   `Activité 3 et son tableau. TRANSCRIS: (1) «3- أستثمر مكتسباتي ومضمون النص في ملء الجدول الآتي:» ; (2) le tableau: en-têtes de colonnes ET de lignes EXACTEMENT. Les mots اللسان et الرجلان sont-ils des en-têtes de LIGNES ? Quelles autres lignes (العين ? اليدان ? الأذن ?) ? Les cellules sont vides ? Donne la structure complète (nb colonnes × nb lignes) et le contenu de chaque cellule non vide.`],
  ['p35-ahfaz', 35, 600, 40, 420, 610, 470,
   `Dernière ligne de la leçon: «أحفظ حديث الدرس الموالى وأستخرج منه علامة البر والإثم.» TRANSCRIS mot à mot — vérifie: (a) «الموالى» ou «الموالي» ; (b) «علامة» ou «علامات» ou «علامتي» ; (c) «البر والإثم» — décris les lettres du mot بعد «علامة» (البـ + ?).`],
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
      console.log(txt.slice(0, 600));
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${nom} échec: ${e.message}`); await sleep(5000*attempt); }
  }
  if (!done) console.log(`ECHEC ${nom} — quota ?`);
  await sleep(2000);
}
