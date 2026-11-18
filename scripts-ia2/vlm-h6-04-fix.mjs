// Z2-38 — hadith-6ep leçon 3 «التنافس في الخير» — Round 2 : zooms décisifs
// sur les points disputés (convergence multi-outils : cmap + tesseract + VLM anatomie)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';

const COMMON = `Zoom sur un manuel scolaire marocain d'hadith (6e primaire traditionnel, arabe), leçon «التنافس في الخير». TRANSCRIS UNIQUEMENT ce qui est imprimé, mot à mot, avec les voyelles visibles. Pour chaque point demandé, DÉCRIS les lettres (nombre de points, boucles, hampes) AVANT de conclure. Ne complète jamais par mémoire d'un texte connu.`;

const ZONES = [
  ['p24-ban-hadith', 24, 600, 330, 530, 620, 630,
   `Bandeau décoratif au-dessus du bloc du hadith. TRANSCRIS-le lettre par lettre. Contient-il «الحديث الشريف» ou «الحديث» ou autre ? Décris chaque mot calligraphié.`],
  ['p24-tamhid-l1', 24, 1200, 200, 342, 600, 382,
   `Première ligne du paragraphe تمهيد: «فَيَظُنُّ الْمُسْلِمُ أَنَّ الصَّدَقَةَ ... عَلَى الْمَالِ وَالْغِنَى». Donne le verbe EXACT entre الصدقة et على: تَقِفُ ? تَتَوَقَّفُ ? تَنْوَفُ ? Décris ses lettres une à une (combien de ت ? de و ? de ق ? de ف ?). Puis donne la fin de ligne exacte.`],
  ['p24-hadith-ma', 24, 1200, 60, 645, 600, 708,
   `Deux lignes du hadith: «...وَيَتَصَدَّقُونَ بِفُضُولِ أَمْوَالِهِمْ، ...: «أَوَلَيْسَ قَدْ جَعَلَ اللهُ لَكُمْ مَا ...؟ إِنْ/إِنَّ بِكُلِّ تَسْبِيحَةٍ صَدَقَةٌ، وَكُلُّ...». Donne: (1) le verbe d'introduction avant «أوليس» (قال ou فقال ?) ; (2) la forme EXACTE du mot après «ما» (تَصَدَّقُونَ ou تُصَدِّقُونَ ?) ; (3) إِنْ ou إِنَّ (avec shadda ?) ; (4) بِكُلِّ ou بِكُلِ (kasra simple ou shadda-kasra sur كل ?).`],
  ['p25-ban-gloses', 25, 1200, 480, 368, 590, 412,
   `Bandeau décoratif de rubrique au-dessus des gloses. TRANSCRIS-le lettre par lettre. Est-ce «الشَّرْحُ» (ش 3 points, ر, ح 1 point) ou «التَّفَهُّمُ» (ت 2 points, ف 1 point, هـ, م) ou autre ? Décris la longueur du mot (5 lettres ou 7-8 ?), la présence de points groupés par 3, etc.`],
  ['p25-glose-dathur', 25, 1200, 170, 405, 540, 445,
   `Glose: «الدُّثُورُ: بِضَمِّ الدَّ... جَمْعُ دَ... بِفَتْحِهَا، وَهُوَ الْمَالُ الْكَثِيرُ.» Donne: (1) le mot après بضم: الدال ou الذال (le ل a-t-il un point au-dessus ?) ; (2) le mot après جمع: دثر (ṯāʾ avec 3 points) ou autre ? Décris les points de sa 2e lettre.`],
  ['p25-gloses-b', 25, 600, 270, 495, 570, 665,
   `Trois gloses de la rubrique الشرح. TRANSCRIS-les mot à mot: (1) «التَّسْبِيحَةُ: ...» ; (2) «التَّهْلِيلَةُ: ...» (ou تهليل ?) ; (3) «وِزْرٌ: ...». Donne les définitions exactes complètes.`],
  ['p25-istikhlal-l1', 25, 1200, 320, 678, 570, 728,
   `Premier item de la rubrique استخلاص المضامين: «1- ... الْفِقْرَةَ الدَّالَةَ عَلَى تَنَافُسِ الصَّحَابَةِ رضوان الله عليهم في الخير.». Donne le verbe EXACT de début (أَسْتَخْرِجُ ? أَحِدُ ? autre ?) et la ponctuation.`],
  ['p25-rawahu', 25, 1200, 60, 192, 570, 245,
   `Fin du hadith + référence: «...كَانَ لَهُ أَجْرٌ». [رَوَاهُ ...]. Donne la référence EXACTE entre crochets: رَوَاهُ مُسْلِمٌ ou رَوَاهُ مُسْلِمًا (tanwīn fatha sur م ?) ou رَوَاهُ مُسْلِمِ ? Décris les marques finales.`],
  ['p26-intro-l1', 26, 1200, 280, 180, 570, 225,
   `Ligne d'introduction de la rubrique التحليل: «... حَدِيثُ الرَّسُولِ ﷺ عَلَى مَا يَأْتِي:». Donne le premier verbe EXACT: يَشْتَمِلُ (ش 3 points + ت 2 points) ou يَتَضَمَّنُ (ت + ض 1 point + ن) ? Décris les lettres une à une.`],
  ['p26-awwalan-l2', 26, 1200, 60, 290, 590, 328,
   `Deuxième ligne de la section أولاً: «فَقَدْ كَانُوا ... عَنْ سُبُلِ الْخَيْرِ الَّتِي تُبَلِّغُهُمْ أَعْلَى الْمَقَامَاتِ وَالدَّرَجَاتِ». Donne le groupe EXACT après «كانوا» (يَسْأَلُونَ النَّبِيَّ ﷺ ? يَتَنَافَسُونَ في ? يَسْتَبِقُونَ إلى ? autre ?) — décris les lettres du/des mots. Puis transcris le reste de la ligne.`],
  ['p26-awwalan-l4', 26, 600, 60, 330, 600, 415,
   `Quatre lignes de la section أولاً: «الْجَنَّةُ، فَلَمَّا رَأَى الْفُقَرَاءُ مِنْهُمْ أَنَّ الْأَغْنِيَاءَ ... الْفَضْلَ الْعَظِيمَ بِإِنْفَاقِ ... سَأَلُوا رَسُولَ اللهِ ﷺ فَقَالُوا: «ذَهَبَ أَهْلُ الدُّثُورِ بِالْأُجُورِ»: أَيْ: ذَهَبَ أَهْلُ ... بِالْأَجْرِ كُلِّهِ؛ ذَلِكَ أَنَّ...». Donne: (1) le mot après الفضل العظيم (بإنفاق + quoi ?) ; (2) le mot après ذهب أهل (الأموال ?) ; (3) après ذلك: أَنَّهُ ou أَنَّهُمْ (mīm présent ?) ; (4) la suite «يُصَلُّونَ كَمَا نُصَلِّي، وَيَصُومُونَ كَمَا نَصُومُ» est-elle exacte ?`],
  ['p26-awwalan-end', 26, 1200, 300, 450, 590, 495,
   `Fin de la section أولاً: «...لِأَنَّهُ لَيْسَ عِنْدَنَا مَا نَتَصَدَّقُ بِهِ؛ فَأَرْشَدَهُمْ ﷺ إِلَى أَعْمَالٍ أُخْرَى ...». Donne la fin EXACTE (للتَّصَدُّقِ ? مِنَ الصَّدَقَاتِ ? لِلتَّصَدُّقِ بها ?). Décris le dernier mot lettre par lettre.`],
  ['p26-thani-start', 26, 1200, 60, 530, 590, 575,
   `Début de la section ثانياً: sous-titre «ثانياً: الصدقة تشمل كل أنواع الخير والمعروف» puis début du paragraphe «... فِي قَوْلِهِ ﷺ: «إِنْ/إِنَّ بِكُلِّ تَسْبِيحَةٍ صَدَقَةٌ...». Donne: (1) le premier verbe du paragraphe (تَبَيَّنَ ? بَيِّنَ ? يَتَبَيَّنُ ?) — décris ses lettres ; (2) إِنْ ou إِنَّ ; (3) la forme de بكِل (shadda sur ل ?).`],
  ['p26-thani-irshad', 26, 1200, 60, 650, 590, 695,
   `Ligne de la section ثانياً: «...وَإِرْشَادُ النَّاسِ وَتَوْجِيهُهُمْ إِلَى الْخَيْرِ ... صَدَقَةٌ مِنَ الصَّدَقَاتِ...». Donne le groupe EXACT après «إلى الخير» : وَتَحْذِيرُهُمْ ? وَتَجَنُّبُ الشَّرِّ ? autre ? Décris les lettres (ح+ذ ? ج+ن+ب ? ش ?).`],
  ['p27-diag-title', 27, 600, 60, 380, 610, 460,
   `Titre/consigne au-dessus d'un schéma (organigramme). TRANSCRIS mot à mot tout ce qui est imprimé dans cette zone (une consigne numérotée ? un titre de rubrique ?). Y a-t-il un bandeau décoratif ? Le donne intégralement.`],
  ['p27-diag-branches', 27, 600, 60, 445, 610, 570,
   `Haut d'un organigramme à deux branches: une boîte centrale et deux branches (droite et gauche) avec des étiquettes. TRANSCRIS chaque étiquette mot à mot: la boîte centrale, l'étiquette de la branche droite (avec أداء الفرائض ?), l'étiquette de la branche gauche (avec ترك الفرائض ?). Décris la structure (boîtes, flèches, liens).`],
  ['p27-diag-rows1', 27, 600, 60, 555, 610, 670,
   `Milieu de l'organigramme: rangées de cellules sous les deux branches. TRANSCRIS chaque cellule mot à mot, rangée par rangée (droite d'abord). Attendu côté droit: «الإكثار من ذكر الله» puis «التنافس في الخير» ; côté gauche: «الغفلة عن ذكر الله» then «الكسل والخمول». Vérifie chaque mot.`],
  ['p27-diag-rows2', 27, 600, 60, 650, 610, 780,
   `Bas de l'organigramme: dernière rangée de cellules. TRANSCRIS chaque cellule mot à mot. Attendu côté droit: «التمتع بالمباحات [بقصد/دون] التقرب إلى الله» ; côté gauche: «التمتع بالمباحات [دون/بقصد] التقرب إلى الله». Donne le mot EXACT (بقصد ? دون ?) dans chaque cellule.`],
  ['p28-t1', 28, 1200, 200, 108, 570, 145,
   `Item 1 de التقويم: «1- أَسْتَخْلِصُ مِنَ الْحَدِيثِ خُلُقًا مِنْ أَخْلَاقِ الصَّحَابَةِ رَضِيَ اللهُ عَنْهُمْ لِلَاقْتِدَاءِ...». Donne la fin EXACTE: لِلَاقْتِدَاءِ ? لِلَااقْتِدَاءِ بِهِمْ ? لِلِاقْتِدَاءِ بِهِمْ ? Décris les alif/lam. Y a-t-il «بهم» à la fin ?`],
  ['p28-t2t3', 28, 1200, 60, 148, 570, 225,
   `Items 2 et 3 de التقويم. Item 2: «هُنَاكَ مَنْ يَرَى أَنَّ الصَّدَقَةَ تَنْحَصِرُ فِي الْمَالِ؛ أُنَاقِشُ هَذَا الرَّأْيَ/الرَّأْيِ.» — donne la voyelle finale de الرأي (fatha ou kasra ?) et la ponctuation après المال (؛ ou ،). Item 3: «أَذْكُرُ/أُذَكِّرُ أَمْثِلَةً أُخْرَى لِلْمُبَاحَاتِ الَّتِي تَتَحَوَّلُ بِالنِّيَّةِ إِلَى عِبَادَاتٍ.» — donne la forme EXACTE du premier verbe (أذكر sans shadda ou أذكّر avec shadda sur ك ?).`],
  ['p28-cit-anta', 28, 1200, 60, 370, 570, 425,
   `Lignes de la citation d'Abû Ḏarr: «قَالَ: وَأَنْتَ/وَأَنْتُمْ فِيكَ/فِيكُمْ صَدَقَةٌ؛ رَفْعُكَ الْعَظْمَ عَنِ الطَّرِيقِ صَدَقَةٌ، وَهُدَاكَ/وَهِدَايَتُكَ الطَّرِيقَ صَدَقَةٌ، وَعَوْنُكَ الضَّعِيفَ/الضَّعِيفَ...». Donne: (1) أَنْتَ ou أَنْتُمْ ; (2) فِيكَ ou فِيكُمْ ; (3) وَهُدَاكَ ou وَهِدَايَتُكَ ; (4) الضَّعِيفَ ou الضَّعِيفِ ; (5) le mot exact après «بفضل» (قُوَّتِكَ ?).`],
  ['p28-cit-ref', 28, 1200, 180, 425, 570, 465,
   `Référence bibliographique entre crochets après la citation: «[عون المعبود شرح سنن أبي داود، ... بتصرف]». Donne la partie chiffrée EXACTE: dans quel ordre les nombres sont-ils imprimés (de droite à gauche) ? 6/121 ? 121/6 ? Quels types de chiffres (arabo-indiens ٦/١٢١ ou occidentaux) ? Décris chaque chiffre.`],
  ['p28-ex1', 28, 1200, 90, 478, 570, 520,
   `Item 1 de l'استثمار: «1- أَسْتَخْرِجُ مِنَ النَّصِّ الصَّدَقَاتِ الَّتِي لَمْ ... ذِكْرُهَا فِي حَدِيثِ الدَّرْسِ.». Donne le verbe EXACT après لم: يَرِدْ (wāw-rāʾ-dāl, actif) ou يُرَدْ (passif, damma sur le ي) ? Décris les voyelles.`],
  ['p28-iqbal', 28, 600, 60, 525, 610, 700,
   `Rubrique الإعداد القبلي en bas de page. TRANSCRIS tout: le bandeau, la consigne «... حَدِيثَ الدَّرْسِ الْمُوَالِي وَأُنْجِزُ مَا يَأْتِي:» (donne le premier verbe EXACT: أَحْفَظُ ou أُحَافِظُ — décris les lettres), puis les items «1- أُشْرِحُ: سَلَامَى - ... بَيْنَ اثْنَيْنِ - ... الْأَذَى» (le 3e terme: أُمَيِّطُ ou تُمِيطُ ou أَمِيطُ ?) et «2- أَسْتَخْرِجُ الصَّدَقَاتِ الْوَارِدَةَ فِي الْحَدِيثِ» (vérifie chaque mot).`],
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
