// Z2-39 — hadith-6ep leçon 4 «شكر الله على نعمة الجوارح» — ROND 2 : zooms d'anatomie
// et zones manquées au rond 1 (sous-titres coupés, bandeaux استثمار/إعداد قبلي,
// notice p.30, texte souligné p.35, chiffres, points ambigus).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-05';

const COMMON = `Recadrage d'un manuel scolaire marocain d'hadith (6e année primaire traditionnel, en arabe), leçon «شكر الله على نعمة الجوارح». Sens de lecture droite→gauche. TRANSCRIS mot à mot ce qui est imprimé, sans jamais compléter par mémoire d'un texte connu. Pour chaque mot DISPUTÉ, décris les lettres une par une (points au-dessus/dessous, boucles ouvertes/fermées, hampes) AVANT de conclure. Donne les voyelles telles qu'imprimées.`;

const ZONES = [
  ['p30-tarjama2', 30, 600, 40, 88, 610, 252,
   `Notice du transmetteur. TRANSCRIS: (1) le bandeau décoratif au-dessus lettre par lettre (ترجمة الراوي ?) ; (2) la notice ENTIÈRE mot à mot: «أبو هريرة رضي الله عنه. هو: ...». Points précis: (a) le nasab («عبد الرحمن بن صخر الدوسي» ? décris les lettres finales du dernier mot) ; (b) «قدم المدينة ورسول الله ﷺ بخيبر سنة ... هـ» (valeur du chiffre ?) ; (c) «روى عنه ... حديثا» — DÉCRIS chaque chiffre du nombre (5374 ? 4055 ? autre) avant de conclure ; (d) «نقلها عنه أكثر من ... من الصحابة والتابعين» (valeur ? 800 ?) ; (e) «توفي عام ... هـ» — DÉCRIS les deux chiffres un par un (boucles, hampes) : 59 ? 95 ? autre ?`],
  ['p29-tamhid-zoom', 29, 1200, 40, 352, 610, 496,
   `Le paragraphe de تمهيد (3 lignes) + la question finale. TRANSCRIS tout mot à mot avec les voyelles EXACTES. Questions: (1) après «فأجد كل جارحة من جوارحي» — y a-t-il «، أو عضو من أعضائي» ou «؛ عضو من أعضائي» (la virgule/point-virgule ET le mot أو avant عضو) ? (2) les formes exactes: «مَفْصِلٌ» ou «مَفْصِلاً» ? «حَاسَّةٌ» ou «حَاسَّةً» ? (3) le mot après «حواسي» : «نِعَمٌ» ? «نِعْمَا» ? «نِعَمًا» ? décris ses lettres et sa voyellation ; (4) la fin du paragraphe: «وهبني الله إياها» ? décris ; (5) la question: «فكيف أشكر الله تعالى على هذه النعم في كل يوم؟» — le mot après «الله» (تعالى ? نعمى ?) et la finale (النعم ? النعمة ?).`],
  ['p29-taadul', 29, 1200, 40, 578, 610, 660,
   `Deux lignes du hadith. TRANSCRIS-les mot à mot. Questions: (1) le mot après «الشمس:» — «تَعْدِلُ» ou «تُعَادِلُ» (y a-t-il un alif entre le tāʾ et le dāl ? décris les lettres) ; (2) le mot entre «صدقة» et «وتعين» : y a-t-il «،» ou rien ; (3) confirme «فتحمله عليها» (lettre par lettre: le pronom après الحمل est-il هُ ?) ; (4) la suite de la 2e ligne jusqu'à «متاعه».`],
  ['p30-gloses-zoom', 30, 1200, 40, 330, 610, 434,
   `Les 2 gloses. TRANSCRIS mot à mot: (1) le MOT-ENTÊTE de la 1re glose: «السَّلامَى» (avec alif maqṣūra finale) ou «السَّلامُ» ? décris la finale lettre par lettre ; (2) dans la citation de القاضي عياض: «وَأَصْلُهُ» (avec hamza) ou «واصلُهُ» (sans hamza) ? décris le début du mot ; (3) la 2e glose: «تَعْدِلُ: تَفْصِلُ بِالْحَقِّ» ou «تَقْضِي بِالْحَقِّ» ? décris les lettres du 2e mot (nombre de points sur la 2e lettre: ف 1 point ? ق 2 points ? boucle ouverte/fermée ?).`],
  ['p30-awwal-zoom', 30, 1200, 40, 672, 610, 748,
   `Fin de page 30, 3 lignes de la section أولا. TRANSCRIS mot à mot: «خلق الله تعالى الإنسان في أحسن صورة، فسوى خلقته وجمل صورته، وأمده بالصحة والعافية فيه، وأسبغ عليه نعما كثيرة ظاهرة وباطنة، في بدنه ويديه». Questions: (1) «وأسبغ» (avec ghayn pointé) ou «وأسبع» (sans point) ? ; (2) «نعما كثيرة» — les tanwīn exacts: «نِعَمًا كَثِيرَةً» ou autres voyelles ? ; (3) «فيه» ou «ففيه» après العافية ? ; (4) le DERNIER mot de la page.`],
  ['p31-sub1', 31, 600, 40, 370, 610, 404,
   `Sous-titre numéroté du premier وجيه. TRANSCRIS-le mot à mot (probablement «1- إصلاح ذات البين»). Le numéro est-il un chiffre occidental 1 ou arabe ١ ?`],
  ['p31-yuajjar', 31, 1200, 40, 434, 610, 460,
   `Une ligne de la glose du premier وجيه: «فالإصلاح بين الناس من أعظم الصدقات التي ... عليها الإنسان». TRANSCRIS la ligne. Le verbe: «يُؤَجَّرُ» (avec shadda sur le jīm) ou «يُؤْجَرُ» (sans shadda) ? Décris: les lettres du mot, la présence/absence de shadda au-dessus du ج, et le siège de la hamza.`],
  ['p31-niza', 31, 1200, 40, 482, 610, 522,
   `Deux lignes: la fin du 1er وجيه. TRANSCRIS: «...في إشاعة الرحمة والمودة والإخاء بين الناس، ونبذ الشحناء و...، والتقاطع والفرقة بينهم». Questions: (1) le mot après «الشحناء»: «والنِّزَاعِ» ou «والتَّنَازُعِ» ? décris ses lettres (y a-t-il un tāʾ après le alif-lām ?) ; (2) le mot avant «الشحناء»: «ونبذ» ou «وأنبذ» ? ; (3) «إشاعة» (ʿayn sans point) ou «إشباع» (bāʾ pointé dessous) ?`],
  ['p31-sub2', 31, 600, 40, 526, 610, 570,
   `Sous-titre numéroté du 2e وجيه. TRANSCRIS-le EN ENTIER mot à mot (il commence par «2- ...» et finit par «...ومساعدتهم»). Quel est le mot entre «في» et «الناس» ? (قضاء ? حوائج ? نفع ? autre).`],
  ['p31-yubayyin', 31, 1200, 40, 568, 610, 598,
   `Première ligne du 2e وجيه. TRANSCRIS-la mot à mot. Le PREMIER mot de la ligne: «يُبَيِّنُ» (bāʾ 1 point dessous + yāʾ 2 points + shadda) ou «يَرْشَدُ» ou «كما أرشد» ? Décris ses lettres une par une.`],
  ['p31-yuthab', 31, 1200, 40, 602, 610, 634,
   `Ligne contenant «أن المبادرة بمساعدة الآخرين صدقة ... عليها العبد عند الله تعالى». TRANSCRIS. Le verbe après «صدقة»: «يُثَابُ» (yāʾ + thāʾ 3 points + alif + bāʾ) ? Décris lettre par lettre. Puis «كمن يساعد إنسانا في حمل يريد أن يضعه عن دابته» — le mot après «كمن» et le mot après «في».`],
  ['p31-tilka', 31, 1200, 40, 338, 610, 368,
   `Fin de l'intro de ثانيا: «...من العبادات والمعاملات. ومن ... الوجوه:». TRANSCRIS. Le mot après «ومن»: «تِلْكَ» (tāʾ + lām + kāf) ou «ذَلِكَ» (dhāʾ 1 point + lām + kāf) ? Décris la première lettre.`],
  ['p32-sub3', 32, 600, 40, 76, 610, 120,
   `Sous-titre numéroté du 3e وجيه. TRANSCRIS-le mot à mot (probablement «3- الكلمة الطيبة»). Le numéro: chiffre occidental 3 ou arabe ٣ ?`],
  ['p32-yani', 32, 1200, 40, 456, 610, 486,
   `Ligne: «باب فضل صلاة الجماعة] يعني: ...». TRANSCRIS la partie après «يعني:» mot à mot: «... حسنة، و... عنه ...». Questions: le 1er verbe (يُعْطَى ? أُعْطِيَ ? يُعطي ?) ; le mot après «عنه» (سيئته ? سيئة ? خطيئة ? ذنوب ?) — décris les lettres et voyelles.`],
  ['p32-kama', 32, 1200, 40, 548, 610, 616,
   `Zone du 5e وجيه: «يرشد قول الرسول ﷺ... إلى إماطة كل ما فيه أذى للإنسان أو غيره؛ ... أن إماطة الأذى عن الطريق من فضائل الأعمال وشعب الإيمان ...؛ فعن أبي هريرة...». TRANSCRIS tout. Question: ce qui suit «وشعب الإيمان» — «كما جاء في الحديث الشريف» ou «التي حث عليها الإسلام» ou autre ? Décris mot à mot.`],
  ['p33-cit1', 33, 1200, 40, 72, 610, 118,
   `Citation en haut de page 33. TRANSCRIS les 2 lignes mot à mot: «وعن أبي هريرة رضي الله عنه قال: قال رسول الله ﷺ: «بينما رجل يمشي بطريق وجد غصن شوك على الطريق ف...ه؛ فشكر الله له، فغفر له»». Questions: (1) y a-t-il un guillemet ouvrant « AVANT «وعن» au début ? (2) le verbe: «فَأَخَرَهُ» (rāʾ SANS point) ou «فَأَخَذَهُ» (dhāʾ 1 point au-dessus) ? Décris la lettre.`],
  ['p33-alalqiyam', 33, 1200, 40, 210, 610, 252,
   `Début du 6e وجيه. TRANSCRIS: le sous-titre «6- ركعتا الضحى» (confirmé) puis l'intro «من عظم الصلاة ويسر الإسلام وترغيب المسلم ... بحقوق نعمة الجوارح ما جاء في قوله ﷺ:...». Questions: (1) entre «المسلم» et «بحقوق»: «على القيام» ou «في القيام» ou «على أداء» ? décris ; (2) le premier mot du hadith: «يَصْبَحُ» ou «يِصْبِحُ» (voyelle du yāʾ) ? ; (3) «ويسر» ou «وبسر» (lettre après le wāw) ?`],
  ['p33-yujzi', 33, 1200, 40, 276, 610, 318,
   `Fin du hadith du 6e وجيه + suite. TRANSCRIS: «...وأمر بالمعروف صدقة، ونهي عن المنكر صدقة، ويجزي من ذلك ركعتان ... من الضحى» puis la référence [صحيح مسلم، كتاب صلاة المسافرين وقصرها، باب...] ENTIÈRE, puis «أي ...». Questions: (1) «ويَجْزِي» ou «ويِجْزِي» (voyelle du yāʾ) ; (2) le verbe après «ركعتان»: «يَرْكَعُهُمَا» — ses voyelles ; (3) le chapitre de la référence (باب استحباب صلاة الضحى...? décris) ; (4) le début de «أي...» jusqu'à la coupe.`],
  ['p34-nums', 34, 1200, 500, 118, 612, 264,
   `Bande de DROITE de la page (colonne des numéros d'activités). Il y a 4 numéros de lignes d'activités (en haut: «1-», puis «2-», puis le 3e, puis «4-»). TRANSCRIS chaque numéro DANS L'ORDRE vertical avec sa valeur: le 3e numéro (3e ligne) est-il «2» ou «3» ou «٢» ou «٣» ? DÉCRIS sa forme (boucles, angles) avant de conclure.`],
  ['p34-istithmar-ban', 34, 600, 40, 452, 610, 532,
   `Zone entre le tableau des سلوكات et la citation de الغزالي. TRANSCRIS: (1) le bandeau décoratif calligraphique (couleur) lettre par lettre — probablement «الاستثمار» ; (2) la première ligne de texte qui suit («قال الإمام الغزالي رحمه الله: «اعلم أن...» jusqu'à la coupe).`],
  ['p34-yantazim', 34, 1200, 40, 528, 610, 562,
   `Deux lignes de la citation الغزالي. TRANSCRIS: «اعلم أن الشكر من جملة مقامات السالكين وهو أيضا ... من علم وحال وعمل... فأما العلم فهو معرفة النعمة من المنعم، والحال هو ...». Questions: (1) le mot après «وهو أيضا»: «يَنْتَظِمُ» (yāʾ+nūn+tāʾ+ẓāʾ+mīm) ou «بِنْتَظِمُ» ou autre ? DÉCRIS la première lettre (point du yāʾ dessous ?) et la 3e lettre (tāʾ 2 points ?) ; (2) le mot après «الحال هو»: «الفرح» ou «اللذة» ? décris (fāʾ 1 point / rāʾ / ḥāʾ OU lām+dhāʾ 1 point+tāʾ marbūṭa).`],
  ['p34-wataallaq', 34, 1200, 40, 592, 610, 646,
   `Deux lignes de la citation الغزالي (suite). TRANSCRIS: «...ويتعلق ذلك العمل بالقلب ... بالجوارح ... باللسان... أما بالقلب فقصد الخير و... لكافة الخلق، وأما باللسان فإظهار الشكر لله تعالى بالتحميدات ...». Questions: (1) les prépositions: «وبالجوارح وباللسان» ou «والجوارح واللسان» (wāw seul ou wāw+bi-) ; (2) après «فقصد الخير و...»: «إضماره» (ʾalif+ḍād+mīm) ou «محبته» ou autre ? DÉCRIS lettre par lettre ; (3) après «بالتحميدات»: «الدالة عليه» ou autre ? décris.`],
  ['p35-header', 35, 600, 40, 74, 610, 112,
   `Ligne d'en-tête d'activités: «أتأمل النص وأجيب عما يأتي:». TRANSCRIS-la mot à mot avec les voyelles. Est-ce «وأجيب» ou «وأحيب» (2e lettre: jīm 1 point ou ḥāʾ sans point) ?`],
  ['p35-nass-zoom', 35, 1200, 40, 105, 610, 218,
   `Zone des activités 1 et 2 avec le TEXTE SOULIGNÉ entre elles. TRANSCRIS TOUT, ligne par ligne: (1) «1- أشرح ما تحته خط.» ; (2) LE TEXTE qui suit (sur 1-2 lignes, tiré de la citation de الغزالي, avec des mots SOULIGNÉS) — transcris-le ENTIÈREMENT mot à mot et dis quels mots portent le trait de soulignement ; (3) «2- أبين كيف يكون الشكر بالعمل، وما مظاهر ذلك؟».`],
  ['p35-iidat-ban', 35, 600, 40, 376, 610, 428,
   `Bandeau décoratif (couleur) au-dessus de la dernière ligne de la leçon. TRANSCRIS-le lettre par lettre (probablement «الإعداد القبلي»).`],
  ['p35-jadwal-hdr', 35, 1200, 40, 308, 610, 372,
   `En-têtes et lignes du tableau de l'activité 3. TRANSCRIS: (1) les 3 en-têtes de colonnes EXACTEMENT (الجوارح | الشكر بالعبادة | الشكر بترك ...) — le 3e en-tête complet («بترك العباد»? «بترك العصيان»? décris les derniers mots) ; (2) les étiquettes de lignes de la 1re colonne: «اللسان» / la 2e ligne (اليدان ? البدان ? décris la 1re lettre: yāʾ 2 points dessous ou bāʾ 1 point dessous) / «الرجلان» ; (3) y a-t-il une 4e ligne ? Les cellules des colonnes 2-3 sont vides ?`],
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
      console.log(txt.slice(0, 500));
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${nom} échec: ${e.message}`); await sleep(5000*attempt); }
  }
  if (!done) console.log(`ECHEC ${nom} — quota ?`);
  await sleep(2000);
}
