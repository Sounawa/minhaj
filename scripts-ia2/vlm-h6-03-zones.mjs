// Z2-37 — hadith-6ep leçon 2 «تحريم الظلم» (pp.17-23)
// — lectures VLM ciblées : citations coraniques moucharabieh (الكهف/النساء/طه...),
//    chiffres de dates et références, tableaux التقويم/الاستثمار, zones cmap-aveugles,
//    bandeaux décoratifs, mots à points ambigus.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03';

const COMMON = `Recadrage d'un manuel scolaire marocain d'hadith (6e année primaire traditionnel, en arabe), leçon «تحريم الظلم» (hadith qudsi d'Abû Ḏarr, Nawawî 24), sens de lecture droite→gauche. TRANSCRIS mot à mot ce qui est imprimé, sans jamais compléter par mémoire d'un texte connu. Les références coraniques entre crochets [sourate: verset] utilisent des chiffres : transcris-les en chiffres et donne leur valeur. Si une zone est un bandeau décoratif calligraphique, transcris-le lettre par lettre du mieux possible.`;

// (nom, page, dpi, x0,y0,x1,y1 en pt, question)
const ZONES = [
  // ===== CRITIQUES (chiffres + citations) =====
  ['date-digits', 18, 1200, 465, 640, 575, 675,
   `Ligne de fin de notice du transmetteur: "...توفي بالربذة (قرية من قرى المدينة) عام «.. ه»". Donne la valeur EXACTE des deux chiffres de l'année de mort (23 ? 32 ? autre ?). Décris chaque chiffre (forme, boucles, hauteur) avant de conclure, et transcris la ponctuation exacte autour (guillemets « », le ه final).`],
  ['p19-cit1', 19, 1200, 40, 682, 610, 737,
   `Fin de section «1- تحريم الله الظلم على نفسه». Après «فالظلم محال في حق الله سبحانه وتعالى.» il y a «قال الله تعالى: ﴿verset﴾ [sourate: numéro]. وقال» — le verset est dans un cadre ornementé en police moucharabieh maghrébine (fā' à point SOUS la ligne). TRANSCRIS le verset ENTIÈREMENT mot à mot, puis la référence EXACTE entre crochets: nom de sourate + valeur du numéro (décris chaque chiffre avant de conclure).`],
  ['p20-cit2', 20, 1200, 40, 56, 610, 106,
   `Haut de page: «وقال سبحانه: ﴿verset﴾ [النساء: رقم].» — verset en cadre moucharabieh. TRANSCRIS le verset ENTIÈREMENT mot à mot, puis la valeur EXACTE du numéro (40 ? 04 ? autre ?). Décris les chiffres avant de conclure.`],
  ['p23-cit1', 23, 1200, 40, 106, 610, 182,
   `Rubrique الاستثمار, activité 1: «1- قال الله تعالى: ﴿verset﴾ [sourate: numéro].» — verset en cadre moucharabieh sur ~2 lignes. TRANSCRIS le verset ENTIÈREMENT mot à mot, puis la référence EXACTE: nom de sourate + valeur des chiffres (décris-les avant de conclure).`],
  ['p23-cit2', 23, 1200, 40, 160, 610, 218,
   `Suite de l'activité 1: «وقال الله تعالى: ﴿verset﴾ [طه: رقم].» — verset en cadre moucharabieh. TRANSCRIS le verset ENTIÈREMENT mot à mot, puis la valeur EXACTE du numéro (131 ? 113 ? autre ?). Décris les chiffres avant de conclure.`],
  // ===== ZONES CMAP-AVEUGLES =====
  ['p22-mustafad3', 22, 600, 40, 255, 610, 340,
   `Liste «مما يستفاد من هذا الحديث», item 3 (entre l'item 2 «الظلم بين العباد حرام فلا أظلم أحدا من خلق الله» et l'item 4 «الله تعالى غني عزيز...»). TRANSCRIS l'item 3 ENTIÈREMENT mot à mot (il commence par «العباد فقراء إلى الله تعالى...» et fait peut-être 2 lignes).`],
  ['p22-table', 22, 600, 30, 518, 610, 795,
   `Bas de page: question «3- أتأمل الحديث القدسي وأملأ الجدول بما يناسب:» suivie d'un tableau. TRANSCRIS les en-têtes de colonnes EXACTEMENT, puis le contenu de chaque ligne (cellules vides précisées comme «vide»). Combien de colonnes et de lignes visibles ?`],
  ['p23-table', 23, 600, 30, 233, 610, 500,
   `Rubrique الاستثمار, activité 2: «2- العدل والشكر: من القيم المستفادة من الدرس، أقترح سلوكات لتطبيقها في الواقع.» suivie d'un tableau à 2 colonnes. TRANSCRIS les en-têtes EXACTEMENT puis le contenu des lignes (cellules vides précisées). Combien de lignes ?`],
  ['p21-bukhari', 21, 600, 40, 376, 610, 484,
   `Section ثالثاً. Après «وقد قال رسول الله ﷺ:» il y a: «إن يد الله ملأى لا تغيضها نفقة سحاء الليل والنهار» puis «وقال: أرأيتم ما أنفقتم...» puis la référence entre crochets. TRANSCRIS tout mot à mot, y compris la référence complète [صحيح البخاري...]. Le verbe après «فإنه لم» est-il يَغِضْ ou يَنْقُصْ ? Décris les lettres.`],
  ['p20-quote-intro', 20, 600, 40, 682, 610, 775,
   `Bas de page (fin de la section ثانياً). Après «فلا يبلغ العبد نفع الله تعالى ولا ضره بطاعته أو معصيته» il y a encore 2-3 lignes. TRANSCRIS tout ce qui suit mot à mot jusqu'en bas de page (probablement «فعبادة الله ما هي... وله تعالى: «يا عبادي لو أن أولكم وآخركم وإنسكم وجنكم كانوا على...»»).`],
  ['p21-quote-end', 21, 600, 40, 72, 610, 194,
   `Haut de page: fin d'une citation + commentaire. TRANSCRIS tout mot à mot depuis le premier mot de la page (la citation se termine par «...قلب رجل واحد منكم ما زاد ذلك في ملكي شيئا» تأكيد لما تقدم؛ وفيه أن تقوى المتقين مصلحة لهم وأنها لا تزيد في ملكه تعالى شيئا). Le mot de la citation juste avant «قلب» est-il أتقى ?`],
  ['p17-tamhid', 17, 600, 40, 323, 610, 532,
   `Rubrique تمهيد: le paragraphe complet (4-5 lignes) puis les 2 questions qui le suivent. TRANSCRIS tout mot à mot avec les voyelles. Donne aussi la forme EXACTE du premier mot du paragraphe.`],
  ['p21-tanbih', 21, 600, 40, 291, 610, 398,
   `Section ثالثاً suite, après la citation du hadith: passage commençant par «هذا تنبيه للخلائق على أن يعظموا...». TRANSCRIS tout mot à mot jusqu'à «وقد قال» (il parle de multiplier la demande, de ne pas mépriser un demandeur, des trésors/reservoirs inépuisables).`],
  ['p17-hadith-isnad', 17, 600, 40, 546, 610, 765,
   `Début du hadith de la rubrique الحديث: «عن أبي ذر الغفاري رضي الله عنه عن النبي ﷺ فيما يرويه عن ربه عز وجل أنه قال: «يا عبادي إني حرمت الظلم على نفسي وجعلته بينكم محرما فلا تظالموا. يا عبادي كلكم ضال إلا من هديته فاستهدوني أهدكم. يا عبادي...»». TRANSCRIS tout mot à mot avec les voyelles, et confirme la formule exacte de l'isnad (عن النبي ﷺ فيما يرويه عن ربه عز وجل).`],
  // ===== HAUT DE PAGE 17 + BANDEAUX =====
  ['p17-top', 17, 600, 40, 35, 610, 302,
   `Haut de la première page de la leçon: cartouche/bandeau décoratif avec numéro et titre de leçon, puis un bandeau de rubrique, puis les 3 objectifs. TRANSCRIS: (1) le cartouche-titre lettre par lettre (numéro de leçon ? titre «تحريم الظلم» ?) ; (2) le label au-dessus des objectifs (probablement «أهداف الدرس») ; (3) les 3 objectifs mot à mot — l'objectif 1 contient-il «وتحريمه للظلم» ou «وتحريمه الظلم» ?`],
  ['p18-ban-tarjama', 18, 600, 40, 476, 610, 528,
   `Bandeau décoratif au-dessus de la notice «أبو ذر الغفاري رضي الله عنه هو: جندب بن جنادة...». TRANSCRIS-le lettre par lettre (probablement «ترجمة الراوي»).`],
  ['p18-ban-fahm', 18, 600, 40, 718, 610, 766,
   `Bandeau décoratif en bas de page, au-dessus des gloses «ضال: مائل عن...». TRANSCRIS-le lettre par lettre (probablement «الفهم»).`],
  // ===== FINESSES DE LECTURE =====
  ['p19-gloses', 19, 600, 40, 136, 610, 337,
   `Les 6 gloses de la rubrique الفهم. TRANSCRIS chacune mot à mot: ضال: ... / فاستهدوني: ... / فاستطعموني: ... / فاستكسوني: ... / المخيط: ... / أحصيها: ... — attention: (a) «ضال: مائل عن الصراط المستقيم» ou «عن الطريق المستقيم» ? (b) «أحصيها: الإحصاء: العد المنضبط بلا زيادة ولا نقصان» ou «العد والضبط...» ?`],
  ['p19-ban-tahlil', 19, 600, 40, 486, 610, 550,
   `Bandeau décoratif de rubrique + phrase d'intro. TRANSCRIS le bandeau lettre par lettre (probablement «التحليل»), puis la phrase d'intro «...هذا الحديث القدسي عدل الله تعالى وسعة فضله ورحمته وعطفه بعباده؛ والكلام فيه كما يأتي:» mot à mot (donne son premier mot exact).`],
  ['p20-thani', 20, 600, 40, 246, 610, 304,
   `Sous-titre de section + début de paragraphe. TRANSCRIS le sous-titre mot à mot (probablement «ثانياً: مظاهر افتقار الخلق إلى الله تعالى» — confirme مظاهر ou ظاهر), puis le début du paragraphe «يدل قوله تعالى...» sur sa première ligne.`],
  ['p21-mathal', 21, 600, 40, 486, 610, 554,
   `Passage: «وقوله «إلا كما ينقص المخيط إذا أدخل البحر» تمثيل قصد به الت... إلى الأفهام بما نشاهده. والمعنى: أن ذلك لا ينقص مما عنده شيئا.» TRANSCRIS mot à mot. Le mot après «قصد به» est-il التهوين ou التقريب ?`],
  ['p21-raabi', 21, 600, 40, 551, 610, 750,
   `Fin de page: sous-titre «رابعاً: عدل الله تعالى و...» (confirme le dernier mot: توفيقه ? توفيعه ? autre) puis le paragraphe «وله تعالى: «إنما هي أعمالكم أحصيها لكم ثم أوفيكم إياها...» فيه بيان لعدل الله تعالى؛ فلا يخاف ابن آدم يوم القيامة أن يظلم فيزاد عليه في سيئاته أو ي... من حسناته. وقوله «فمن وجد خيرا فليحمد الله» إعلام للعبد أن لا يسند طاعته» — TRANSCRIS tout mot à mot (le verbe avant «من حسناته» est-il يهضم ou ينقص ?).`],
  ['p20-fineA', 20, 600, 40, 416, 610, 540,
   `Trois lignes du paragraphe sur l'افتقار. TRANSCRIS mot à mot: (a) la ligne contenant «...أمروا بطلب الهداية والطعام والكسوة والمغفرة من الله عز وجل وحده وعدم الاستغناء عنه» — quel est le PREMIER mot de la ligne (لأنهم ? لذلك ? autre) ? (b) «وفي هذا كله تنبيه على فقرنا وعجزنا عن جلب ... أو دفع المضار عن أنفسنا» — le mot après «جلب» (منافعنا ? منافعا ?) et la conjonction (أو ? و ?).`],
  ['p20-fineB', 20, 600, 40, 536, 610, 627,
   `Deux-trois lignes: «وهو يرجع إلى معنى «لا حول ولا قوة إلا بالله». ويعلم العبد أنه إذا رأى آثار هذه النعم عليه أن ذلك من عند الله ويتعين عليه شكر الله تعالى وكلما ... الإنعام يزيد في الحمد والشكر.» TRANSCRIS mot à mot ; le mot après «كلما» (ازداد ? زاد ?).`],
  ['p20-fineC', 20, 600, 40, 610, 610, 694,
   `Paragraphe: «قوله: «إنكم لن تبلغوا ضري فتضروني ولن تبلغوا نفعي فتنفعوني» بعد أن أمر الله تعالى العباد بالالتجاء إليه في الأمور كلها بيّن... أن ذلك ليس لمصلحة تعود عليه؛ لأنه سبحانه غني عن الخلق، فلا يبلغ العبد نفع الله تعالى ولا ضره بطاعته أو معصيته» — TRANSCRIS mot à mot (le mot après «كلها» est-il بيّن ou بيّن لهم ?).`],
  ['p20-fineD', 20, 600, 40, 156, 610, 187,
   `Une ligne: «لأن الظلم بعيد عن رحمة الله ... ولأن للظلم آثارا سيئة على الفرد والمجتمع» — TRANSCRIS-la mot à mot ; quel est le mot après «رحمة الله» (عز وجل ? تعالى ?).`],
  ['p22-raabi-end', 22, 600, 40, 66, 610, 154,
   `Fin de la section رابعا°: «وعبادته لنفسه، بل يسندها إلى توفيق الله ويحمده على ذلك، وقوله: «ومن وجد غير ذلك» يعني ومن وجد غير الأفضل «فلا يلومن إلا نفسه»؛ أكد الفعل بالنون تحذيرا من أن يخطر في قلب عامل أن يوجه اللوم إلى غيره.» TRANSCRIS tout mot à mot.`],
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1400,
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
