// Z2-40 — hadith-6ep leçon 5 «الْبِرُّ حُسْنُ الْخُلُقِ» (pp.36-40)
// — lectures VLM ciblées vague 1 : cartouche-titre, bandeaux, DEUX hadiths (النواس + وابصة),
//    DEUX notices de transmetteurs, glose الشرح, citation الفتوحات الوهبية, آيتا البقرة والأنفال,
//    آية الفرقان (الاستثمار), tableaux (السلوكات p.40), références à chiffres, mots à points ambigus.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-06';

const COMMON = `Recadrage d'un manuel scolaire marocain d'hadith (6e année primaire traditionnel, en arabe), leçon «البر حسن الخلق» (hadiths d'an-Nawwās b. Samʿān et de Wābisa b. Maʿbad: «البر حسن الخلق، والإثم ما حاك في نفسك وكرهت أن يطلع عليه الناس»), sens de lecture droite→gauche. TRANSCRIS mot à mot ce qui est imprimé, sans jamais compléter par mémoire d'un texte connu. Les références entre crochets utilisent des chiffres : transcris-les et donne leur valeur. Si une zone est un bandeau décoratif calligraphique, transcris-le lettre par lettre du mieux possible. Voyelles : reproduis-les telles qu'imprimées.`;

// (nom, page, dpi, x0,y0,x1,y1 en pt, question)
const ZONES = [
  ['p36-cartouche', 36, 600, 85, 50, 555, 155,
   `Cartouche-titre de la leçon (cadre décoratif, 2 lignes possibles). TRANSCRIS lettre par lettre: (1) le mot «الدرس» + le NUMÉRO (chiffre arabe ٥ ou occidental 5 ? décris sa forme) ; (2) le titre mot à mot avec les voyelles (probablement «الْبِرُّ حُسْنُ الْخُلُقِ» — décris les voyelles/doubles de البر et الخلق) ; (3) tout autre élément (ornement, basmala).`],
  ['p36-ahdaf', 36, 600, 40, 150, 610, 315,
   `Zone des objectifs. TRANSCRIS: (1) le bandeau au-dessus (probablement «أهداف الدرس») lettre par lettre ; (2) les 3 objectifs numérotés mot à mot avec voyelles. Question précise: l'objectif 2 contient-il «بين علامة البر وبين علامة الإثم» (deux fois «بين») ou «بين علامة البر وعلامة الإثم» ? L'objectif 1: «أن أتعرف معنى البر والإثم» ? L'objectif 3: «أن أتمثل أخلاق البر لأتصف بحسن الخلق» ?`],
  ['p36-tamhid', 36, 600, 40, 300, 610, 478,
   `Zone de la rubrique تمهيد. TRANSCRIS: (1) le bandeau décoratif (تمهيد ?) ; (2) le paragraphe complet mot à mot avec voyelles — il commence par «تُقسَم? أو نُقسَم? الأعمال التي يأتيها? أو يقوم بها? الإنسان إلى ثلاثة أقسام: قسم اتضح كونه من البر، وقسم اتضح فيه وجه الإثم، وقسم يتأرجح بين البر والإثم، إلا أن من فضل الله على الإنسان أن جعل له علامة يفصل بها بين أعمال البر وأعمال الإثم» — donne le PREMIER verbe exactement (نُقسم ? تُقسم ? تُقسمّ ?) et «يأتيها» ou «يقوم بها» ; (3) la ligne de questions finale: «فما هو البر؟ وما هو الإثم؟ وما هي علامتهما?» — le DERNIER mot exact (علامتهما ? علاماتها ? علامتها ?).`],
  ['p36-hadith-ban', 36, 600, 40, 478, 610, 570,
   `Zone au-dessus du cadre du hadith: (1) un bandeau décoratif — TRANSCRIS-le lettre par lettre (الحديث ? الحديث الشريف ? autre) ; (2) la ligne d'isnad «عَنِ النَّوَاسِ بْنِ سِمْعَانَ رَضِيَ اللهُ عَنْهُ، عَنِ النَّبِيِّ ﷺ قَالَ:» mot à mot — y a-t-il «سألت رسول الله عن البر والإثم» quelque part ? Le mot après «عنه» est-il «عن النبي» ou directement «قال» ?`],
  ['p36-hadith', 36, 600, 40, 545, 610, 630,
   `Le hadith dans son cadre + sa référence. TRANSCRIS mot à mot avec voyelles: «الْبِرُّ حُسْنُ الْخُلُقِ، وَالْإِثْمُ مَا حَاكَ فِي نَفْسِكَ وَكَرِهْتَ أَنْ يَطْلِعَ عَلَيْهِ النَّاسُ» puis la référence entre crochets ([رواه مسلم] ? décris chaque mot). Ponctuation exacte (virgules, tirets) ?`],
  ['p36-wabisa', 36, 600, 40, 612, 610, 735,
   `Deuxième hadith (en bas de page). TRANSCRIS ENTIÈREMENT mot à mot avec voyelles: «وَعَنْ وَابِصَةَ بْنِ مَعْبَدٍ رَضِيَ اللهُ عَنْهُ قَالَ: أَتَيْتُ رَسُولَ اللهِ ﷺ فَقَالَ: «جِئْتَ تَسْأَلُ عَنِ الْبِرِّ؟» قُلْتُ: نَعَمْ. قَالَ: «اسْتَفْتِ قَلْبَكَ؛ الْبِرُّ مَا اطْمَأَنَّتْ إِلَيْهِ النَّفْسُ وَاطْمَأَنَّ إِلَيْهِ الْقَلْبُ، وَالْإِثْمُ مَا حَاكَ فِي النَّفْسِ وَتَرَدَّدَ فِي الصَّدْرِ، وَإِنْ أَفْتَاكَ النَّاسُ وَأَفْتَوْكَ».» puis la référence entre crochets. QUESTIONS: (a) «جئت تسأل عن البر» ou «عن البر والإثم» ? (b) la référence: «[حديث حسن؛ رويناه في مسندي الإمامين: أحمد بن حنبل والدارمي؛ بإسناد حسن]» ? — le mot «والدارمي» (د-ا-ر-م-ي) ou «والدرامي» (د-ر-ا-م-ي) ? décris l'ordre des lettres ; (c) «مسندي» (avec alif après le dāl) ou «مسند» ?`],
  ['p37-tarjama1', 37, 600, 40, 80, 610, 178,
   `Haut de page 37: bandeau décoratif de rubrique + notice du premier transmetteur. TRANSCRIS: (1) le bandeau (ترجمة الراوي ?) lettre par lettre ; (2) la notice ENTIÈRE mot à mot: «النَّوَاسُ رَضِيَ اللهُ عَنْهُ، هُوَ: ابْنُ سِمْعَانَ بْنِ خَالِدِ بْنِ عَبْدِ اللهِ بْنِ أَبِي ... بْنِ رَبِيعَةَ، ... فِي الشَّامِيِّينَ. تُوُفِّيَ فِي حُدُودِ الْخَمْسِينَ لِلْهِجْرَةِ، وَرَوَى لَهُ مُسْلِمٌ وَالْأَرْبَعَةُ.» — PRÉCISIONS: (a) le mot après «بْنِ أَبِي» (بكر ? عمرو ? autre — décris les lettres) ; (b) le mot entre «رَبِيعَةَ» et «فِي الشَّامِيِّينَ» (المعدود ? المشهور ? المكنى ? — décris ses lettres) ; (c) «الشاميين» ou «الشآميين» ?`],
  ['p37-tarjama2', 37, 600, 40, 178, 610, 312,
   `Notice du deuxième transmetteur وابصة. TRANSCRIS ENTIÈREMENT mot à mot: «وَابِصَةُ رَضِيَ اللهُ عَنْهُ، هُوَ: ابْنُ مَعْبَدِ بْنِ مَالِكِ بْنِ عُبَيْدٍ الْأَسَدِيُّ مِنْ بَنِي أَسَدِ بْنِ خُزَيْمَةَ، يُكْنَى ... أَسْلَمَ سَنَةَ ... عِنْدَمَا وَفَدَ عَلَى رَسُولِ اللهِ ﷺ، وَلَهُ ... أَحَادِيثُ. وَكَانَ قَارِئًا لِكِتَابِ اللهِ، بَكَّاءً، لَا يَمْلِكُ دُمُوعَهُ إِذَا قَرَأَ الْقُرْآنَ؛ سَكَنَ الْكُوفَةَ ثُمَّ تَحَوَّلَ إِلَى الرَّقَّةِ، وَتُوُفِّيَ بِهَا فِي حُدُودِ السِّتِّينَ مِنَ الْهِجْرَةِ.» QUESTIONS: (a) la kunya après «يُكْنَى» (أبا شداد ? أبا سالم ? أبا الشعثاء ? — décris CHAQUE lettre: ش ou س ? د ou ل ?) ; (b) l'année d'islam: «سَنَةَ تِسْعٍ» ou «سَبْعٍ» (ت ou س en première lettre ?) ; (c) le mot entre «وله» et «أحاديث» s'il existe (عدة ? بضعة ? rien ?) ; (d) «خزيمة» — confirme les lettres (خ-ز-ي-م-ة).`],
  ['p37-sharh', 37, 600, 40, 352, 610, 437,
   `Zone de la rubrique الشرح. TRANSCRIS: (1) le bandeau décoratif (الشرح ?) lettre par lettre ; (2) la ou les gloses mot à mot: «حَاكَ فِي نَفْسِكَ: تُخَالِجُ فِي بَاطِنِكَ وَ... تَطْمَئِنُّ إِلَيْهِ.» — le mot entre «و» et «تطمئن» (لا ? لم ?) ; (3) y a-t-il UNE ou PLUSIEURS gloses (y a-t-il une glose pour «البر» ou «حسن الخلق» avant ou après) ? Donne tout le texte imprimé de la zone.`],
  ['p37-istikhlas', 37, 600, 40, 437, 610, 537,
   `Zone de la rubrique استخلاص المضامين. TRANSCRIS: (1) le bandeau décoratif lettre par lettre (استخلاص المضامين ?) ; (2) Y a-t-il une ligne au-dessus des items numérotés (une consigne comme «أستخرج من الحديث...» ou juste la décoration) ? ; (3) les items numérotés mot à mot: «1- ... تعريف البر والإثم.» / «2- ... علامة البر والإثم.» — le verbe exact de chaque item (أستخرج ? أستخلص ?).`],
  ['p37-tahlil', 37, 600, 40, 528, 610, 765,
   `Zone de la rubrique التحليل (fin de page 37). TRANSCRIS: (1) le bandeau décoratif (التحليل ?) lettre par lettre ; (2) la phrase d'intro «يَتَنَاوَلُ هَذَا الدَّرْسُ بَيَانَ الْبِرِّ وَالْإِثْمِ وَالْعَلَامَةِ الْمُمَيِّزَةَ لِكُلٍّ مِنْهُمَا، وَتَفْصِيلُ ...» — le(s) mot(s) après «وتفصيل» jusqu'à la fin de la phrase ; (3) le sous-titre «أَوَّلًا: تَعْرِيفُ الْبِرِّ وَبَيَانُ فَضْلِهِ» (ou autre ?) ; (4) le paragraphe entier mot à mot: «الْبِرُّ هُوَ الْعَمَلُ الَّذِي يَبِرُّ بِهِ فَاعِلُهُ؟ وَيُلْحِقُهُ؟ بِالْأَبْرَارِ، وَهُمُ الْمُطِيعُونَ لِلهِ تَعَالَى؟ ... وَهُوَ اسْمٌ جَامِعٌ لِلْخَيْرِ ...» — donne la fin de la page mot à mot (les mots exacts après «وهو اسم جامع للخير»: كُلِّهِ ? وَلِكُلِّ مَا يَرْضَى ? ثم quel mot vient après ?). QUESTIONS: (a) «يَبِرُّ بِهِ فَاعِلُهُ» ou «يَبَرُّ فَاعِلُهُ» (présence du ب ?) ; (b) «وَيُلْحِقُهُ بِالْأَبْرَارِ» ou «فَيُلْحَقُ بِالْأَبْرَارِ» ; (c) le mot après «المطيعون» (لله ? لله تعالى ?).`],
  ['p38-citation', 38, 600, 40, 55, 610, 118,
   `Haut de page 38: fin d'une citation + référence. TRANSCRIS mot à mot la ligne complète et la référence: «... قَالَ؟ ... بالضَّمِّ فِي تَغْذِيَةِ؟ الْبَدَنِ» [الفتوحات الوهبية على الأربعين النووية؛ ص: 214]». QUESTIONS: (a) le PREMIER mot de la ligne (كَانَ ? قَالَ ? البِرُّ ? وَالْبِرُّ ?) ; (b) «تَغْذِيَةِ» (ت-غ-ذ-ي-ة) ou «تَعْذِيَةِ» (ت-ع-ذ-ي-ة) ? décris la 2e lettre ; (c) «الْبَدَنِ» ou «الْبَتَنِ» ? ; (d) la valeur du numéro de page dans la référence (214 ? 213 ? décris les chiffres un par un).`],
  ['p38-ulama', 38, 600, 40, 100, 610, 205,
   `«وَقَالَ الْعُلَمَاءُ: الْبِرُّ يَكُونُ بِمَعْنَى الصِّلَةِ وَبِمَعْنَى الصَّدْقِ، وَبِمَعْنَى اللُّطْفِ وَالْمَبَرَّةِ، وَحُسْنِ الْعِشْرَةِ، وَالصُّحْبَةِ، وَلِينِ الْجَانِبِ، وَاحْتِمَالِ الْأَذَى، وَبِمَعْنَى الطَّاعَةِ بِسَائِرِ ...، وَمِنْهُ قَوْلُهُ تَعَالَى: {لَيْسَ الْبِرَّ أَنْ تُوَلُّوا وُجُوهَكُمْ قَبْلَ الْمَشْرِقِ وَالْمَغْرِبِ...». QUESTIONS: (a) le mot après «بسائر» (لَوَاحِقِهَا ? أَنْوَاعِهَا ? — décris: ل ou أ ? و ou ن ? ق ou ع ?) ; (b) «اللطف» ou «الصفا» ? ; (c) l'ordre exact: «اللطف والمبرة» ou «الصفا والمبرة» ? ; (d) transcris le début de l'ayah mot à mot tel qu'imprimé (avec les voyelles).`],
  ['p38-aya-end', 38, 600, 40, 195, 610, 305,
   `Fin de l'ayah de al-Baqara + phrase de synthèse. TRANSCRIS: (1) la fin de l'ayah: «...وَأَقَامَ الصَّلَاةَ وَآتَى الزَّكَاةَ وَالْمُوفُونَ بِعَهْدِهِمْ إِذَا عَاهَدُوا وَالصَّابِرِينَ فِي الْبَأْسَاءِ وَالضَّرَّاءِ وَحِينَ الْبَأْسِ أُولَئِكَ الَّذِينَ صَدَقُوا وَأُولَئِكَ هُمُ الْمُتَّقُونَ» + la référence entre crochets [البقرة: ...] ; (2) la phrase: «فَمَجَامِعُ؟ حُسْنِ الْخُلُقِ هِيَ الْبِرُّ» — مَجَامِعُ (avec alif: ج-ا-م-ع) ou مَجْمَعُ (sans alif) ? ; (3) DÉCRIS le NUMÉRO de la référence [البقرة: ١٧٦ ou ١٧٧ or 176 or 177] chiffre par chiffre (forme occidentale ou arabe ? premier chiffre 1 ? deuxième 7 ? troisième 6 ou 7 ?).`],
  ['p38-haj', 38, 600, 40, 290, 610, 372,
   `«وَقَوْلُهُ ﷺ: «الْبِرُّ حُسْنُ الْخُلُقِ» يَعْنِي أَنَّ حُسْنَ الْخُلُقِ أَعْظَمُ خَصَالِ الْبِرِّ، كَمَا قَالَ ﷺ: «الْحَجُّ عَرَفَةٌ» [référence]». TRANSCRIS tout mot à mot + la référence EXACTE entre crochets. QUESTIONS: (a) la structure de la référence: «[سنن الترمذي في الحج؛ باب ...؛ حديث رقم 889]» ? — les mots exacts entre «الترمذي» et «باب» (في الحج ? كتاب الحج ?) ; (b) le numéro du باب: DÉCRIS les chiffres un par un (57 ? 25 ? 257 ?) ; (c) le numéro du hadith (889 ? décris les trois chiffres).`],
  ['p38-murad', 38, 600, 40, 360, 610, 575,
   `Section «وَالْمُرَادُ بِحُسْنِ الْخُلُقِ» + ayah al-Anfāl + sous-titre suivant. TRANSCRIS: (1) «وَالْمُرَادُ بِحُسْنِ الْخُلُقِ: الْإِنْصَافُ فِي الْمُعَامَلَةِ، وَالرِّفْقُ؟ فِي الْمُحَاوَرَةِ؟، وَالْعَدْلُ فِي الْأَحْكَامِ، وَالْبَذْلُ؟ فِي الْإِحْسَانِ؟، إِلَى غَيْرِ ذَلِكَ مِنْ صِفَاتِ الْمُؤْمِنِينَ الَّذِينَ وَصَفَهُمُ اللَّهُ تَعَالَى فَقَالَ:» — donne les mots 2 et 4 exactement (الرفق في المحاورة ? المحاولة ? / البذل في الإحسان ? الإكرام ?) ; (2) l'ayah ENTIÈRE: «{إِنَّمَا الْمُؤْمِنُونَ الَّذِينَ إِذَا ذُكِرَ اللهُ وَجِلَتْ قُلُوبُهُمْ...» jusqu'à «...وَرِزْقٌ كَرِيمٌ}» [الأنفال: 2-4] ; (3) le sous-titre coloré qui suit: «ثَانِيًا: تَعْرِيفُ الْإِثْمِ» (ثانيا ou ثانئا ?).`],
  ['p38-thani', 38, 600, 40, 570, 610, 765,
   `Section ثانيا (définition de l'إثم), fin de page 38. TRANSCRIS ENTIÈREMENT mot à mot: «وَقَوْلُهُ ﷺ: «وَالْإِثْمُ مَا حَاكَ فِي نَفْسِكَ وَكَرِهْتَ أَنْ يَطْلِعَ عَلَيْهِ النَّاسُ». يَعْنِي أَنَّ الْإِثْمَ هُوَ الشَّيْءُ الَّذِي يُورِثُ ... فِي الْقَلْبِ، وَيَكْرَهُ صَاحِبُهُ أَنْ يَطْلِعَ عَلَيْهِ النَّاسُ؛ وَهُوَ بِخِلَافِ الْبِرِّ؛ فَالْبِرُّ: كَلِمَةٌ جَامِعَةٌ لِجَمِيعِ أَفْعَالِ الْخَيْرِ وَخِصَالِ الْمَعْرُوفِ، وَالْإِثْمُ: كَلِمَةٌ جَامِعَةٌ لِجَمِيعِ أَفْعَالِ الشَّرِّ وَالْقَبَائِحِ كَبِيرِهَا وَصَغِيرِهَا. وَلِهَذَا السَّبَبِ قَابَلَ ... بَيْنَهُمَا وَجَعَلَهُمَا ضِدَّيْنِ.» QUESTIONS: (a) le mot après «يُورِثُ» (نَفْرَةً ? ذَفْرَةً ? زَفْرَةً ? — décris la première lettre: ن bol avec point DESSUS, ذ dāl avec point DESSUS, ز pointue avec point DESSUS, ص boucle SANS point ?) ; (b) le mot entre «قَابَلَ» et «بَيْنَهُمَا» (كُلٌّ ? كِلَا ? كَلِمَةٌ ? rien ?) ; (c) «وَالْقَبَائِحِ» (avec hamza) ?`],
  ['p39-thalith', 39, 600, 40, 55, 610, 162,
   `Haut de page 39: sous-titre de section (peut-être en couleur/style décoré) + paragraphe. TRANSCRIS: (1) le sous-titre «ثَالِثًا: عَلَامَةُ الْبِرِّ وَالْإِثْمِ» (ثالثا ou ثالثئا ?) ; (2) le paragraphe: «جَعَلَ الْحَدِيثُ لِلْإِثْمِ عَلَامَتَيْنِ: نَفْرَةَ الْقَلْبِ، وَكَرَاهَةَ؟ الِاطِّلَاعَ؟. وَأَمَّا عَلَامَةُ الْبِرِّ فَهِيَ طُمَأْنِينَةُ النَّفْسِ، كَمَا فِي الْحَدِيثِ: «الْبِرُّ مَا اطْمَأَنَّتْ إِلَيْهِ النَّفْسُ».» — le mot 2 exact (وَكَرَاهَةُ ? وَكَرَامَةُ ?) et le mot 3 (الِاطِّلَاعُ ? الِاطِّلَاعَ ? أَنْ يَطَّلِعَ ?).`],
  ['p39-mana', 39, 600, 40, 150, 610, 302,
   `Milieu de page 39. TRANSCRIS ENTIÈREMENT mot à mot: «وَلَيْسَ مَعْنَى الْحَدِيثِ أَنْ يَعْتَمِدَ الْإِنْسَانُ فِي مَسَائِلِ الْحَلَالِ وَالْحَرَامِ عَلَى ... النُّفُوسِ، بَلْ لَا بُدَّ؟ فِيهَا مِنْ سُؤَالِ أَهْلِ الْعِلْمِ وَالْأَخْذِ بِمَا يَقُولُونَ. وَأَمَّا اسْتِفْتَاءُ؟ الْقَلْبِ فَمَعْنَاهُ: أَنَّ الْإِنْسَانَ إِذَا عَرَضَتْ لَهُ مَسْأَلَةٌ مِنَ الْمَسَائِلِ الْمُشْتَبِهَةِ ...». QUESTIONS: (a) le mot entre «عَلَى» et «النُّفُوسِ» (فَتَاوَى ? فَتْوَى ? فَتَا ?) ; (b) «بَلْ لَا بُدَّ فِيهَا» ou «بَلِ الْفَتْوَى فِيهَا» ? décris lettre par lettre ; (c) «وَأَمَّا اسْتِفْتَاءُ الْقَلْبِ» ou «وَمَا اسْتِفْتَاءُ» ? ; (d) la suite après «المشتبهة»: «فَسَأَلَ عَنْهَا وَأَفْتَاهُ؟ بِأَنَّهَا حَلَالٌ، فَلَمْ تَطْمَئِنُّ نَفْسُهُ وَبَقِيَ مُتَرَدِّدًا فِيهَا، فَإِنَّ مِنَ السَّلَامَةِ أَنْ يَتْرُكَ هَذَا الْأَمْرَ الَّذِي هُوَ غَيْرُ مُطْمَئِنٍّ؟ إِلَيْهِ، اسْتِبْرَاءً لِدِينِهِ» — le mot après «فَسَأَلَ عَنْهَا» (وَأَفْتَاهُ ? فَأَفْتَاهُ ? وَأَجَابَهُ ?) et après «هو» (غَيْرُ مُطْمَئِنٍّ إِلَيْهِ ? مُطْمَئِنٌّ إِلَيْهِ ?).`],
  ['p39-daa', 39, 600, 40, 300, 610, 400,
   `Fin du paragraphe + deux hadiths de soutien. TRANSCRIS: (1) «وَهَذَا كَقَوْلِهِ ﷺ: «فَمَنِ اتَّقَى الشُّبُهَاتِ فَقَدِ اسْتَبْرَأَ لِدِينِهِ وَعِرْضِهِ». [صَحِيحُ مُسْلِمٍ، كِتَابُ الْمُسَاقَاةِ، بَابُ أَخْذِ الْحَلَالِ وَتَرْكِ الشُّبُهَاتِ]» — vérifie chaque mot de la référence ; (2) «وَكَقَوْلِهِ ﷺ: «دَعْ مَا يَرِيبُكَ إِلَى مَا لَا يَرِيبُكَ». [رَوَاهُ التِّرْمِذِيُّ وَالنَّسَائِيُّ؟]» — la référence exacte: «رواه الترمذي والنسائي» ou «رواه الترمذي» seul, ou avec «وقال حديث حسن صحيح» ? TRANSCRIS tout ce qui est imprimé.`],
  ['p39-mustafad', 39, 600, 40, 395, 610, 575,
   `Zone de la rubrique «مما يستفاد...». TRANSCRIS: (1) le bandeau décoratif lettre par lettre (مما يستفاد من هذا الحديث ? مما يستفاد من الدرس ?) ; (2) les 3 items mot à mot. QUESTIONS: (a) item 1: «أَهَمِّيَّةُ؟ إِصْلَاحِ الْقَلْبِ بِأَنْوَاعِ الْبِرِّ لِإِصْلَاحِ حَرَكَاتِ الْجَوَارِحِ، وَالتَّرْغِيبُ فِي حُسْنِ الْخُلُقِ» — le premier mot (أهمية ? أهميةٌ ?) et le mot إصلاح: ص SANS point ou ض AVEC point au-dessus ? (b) item 2: «الْمُؤْمِنُ لَا يُقَدِّمُ عَلَى شَيْءٍ لَا تَطْمَئِنُّ نَفْسُهُ إِلَيْهِ» ; (c) item 3: «إِخْبَارُهُ ﷺ وَابِصَةَ عَمَّا فِي نَفْسِهِ مُعْجِزَةٌ مِنَ الْمُعْجِزَاتِ» — «لِوَابِصَةَ» ou «وَابِصَةَ» ?`],
  ['p39-taqwim', 39, 600, 40, 568, 610, 745,
   `Zone de la rubrique التقويم (bas de page 39). TRANSCRIS: (1) le bandeau décoratif (التقويم ?) ; (2) les items numérotés visibles mot à mot: «1- أُعَرِّفُ الْبِرَّ وَأُبَيِّنُ أَهَمِّيَتَهُ فِي تَزْكِيَةِ النَّفْسِ.» / «2- مَتَّى يُعْتَمَدُ عَلَى ... الْقَلْبِ فِي تَحْدِيدِ الْبِرِّ؟» — DÉCRIS les numéros imprimés (1 ? 2 ?) et le mot entre «على» et «القلب» (طُمَأْنِينَةِ ? حُكْمِ ? رَأْيِ ?) ; (3) combien d'items au total sur cette page (2 ? 3 ?).`],
  ['p40-taqwim3', 40, 600, 40, 55, 610, 385,
   `Haut de page 40: activité numérotée + tableau. TRANSCRIS: (1) la ligne d'activité «3-؟ أَمْلَأُ الْجَدْوَلَ الْآتِيَ بِمَا يُنَاسِبُ:» — DÉCRIS le numéro (3 ? 4 ?) et le premier verbe (أَمْلَأُ ? أُمَلِّلُ ?) ; (2) le tableau COMPLET: en-têtes de colonnes EXACTEMENT (السلوكات والتصرفات | ... | ...) — y a-t-il un en-tête à 2 niveaux (الحكم divisé en «في البر» et «في الإثم») et une colonne «التعليل» ? ; (3) CHAQUE ligne de la première colonne mot à mot (4-5 lignes: «المشاركة في الأنشطة المدرسية للتوعية بأهمية الحفاظ على البيئة» / «... الناس وحسن الظن? بهم» / «...» / «...») — donne chaque ligne ENTIÈREMENT avec les mots exacts ; (4) les autres cellules sont-elles vides ?`],
  ['p40-istithmar', 40, 600, 40, 345, 610, 612,
   `Zone de la rubrique الاستثمار. TRANSCRIS: (1) le bandeau décoratif (الاستثمار ?) ; (2) le paragraphe introductif: «وَصَفَ اللهُ تَعَالَى الْمُؤْمِنِينَ فِي ... مِنْهَا قَوْلُهُ تَعَالَى: {وَعِبَادُ الرَّحْمَنِ؟ الَّذِينَ يَمْشُونَ عَلَى الْأَرْضِ هَوْنًا؟...} [الْفُرْقَان: 63-77؟] إِلَى آخِرِ السُّورَةِ.» — le mot entre «في» et «منها» (عِدَّةِ آيَاتٍ ? آيَاتٍ ?) et le texte exact de l'ayah cité (jusqu'où va la citation: «هَوْنًا» ? plus loin ?) ; (3) les 3 activités numérotées mot à mot: «1- أَكْتُبُ الْآيَاتِ فِي دَفْتَرِي كَامِلَةً وَفْقَ قَوَاعِدِ الرَّسْمِ وَالضَّبْطِ؟ وَالوَقْفِ.» / «2- أُصَنِّفُ؟ فِي خُطَّاطَةِ؟ صِفَاتِ الْمُؤْمِنِينَ الْوَارِدَةَ فِي هَذِهِ الْآيَاتِ.» / «3- أَخْتَارُ مِنَ الْآيَاتِ صِفَتَيْنِ وَأُبَيِّنُ كَيْفَ أُطَبِّقُهُمَا فِي مُحِيطِي.» — PRÉCISIONS: (a) le mot dans l'activité 1: «وَالصَّبْطِ» (ص SANS point) ou «وَالضَّبْطِ» (ض AVEC point au-dessus) ? ; (b) l'activité 2: le verbe (أُصَنِّفُ ? أَعِدُّ ? أُنْجِزُ ?) et «خُطَّاطَةِ» ou «خُطَاطَةِ» ? ; (c) le titre ou la consigne de l'activité 2 s'il y en a un avant.`],
  ['p40-iidad', 40, 600, 40, 600, 610, 770,
   `Bas de page 40: rubrique الإعداد القبلي. TRANSCRIS: (1) le bandeau décoratif (الإعداد القبلي ?) ; (2) «أَحْفَظُ حَدِيثَ الدَّرْسِ الْمُوَالَى وَأُنْجِزُ مَا يَأْتِي:» ; (3) «1- أَشْرَحُ الْمُفْرَدَاتِ الْآتِيَةَ: وَجَلَتْ - ذَرَفَتْ.» — le mot «الموالي» ou «الموالى» (alif final avec ou sans hamza) ? Y a-t-il d'autres mots après «ذرفت» (بليغة ? قلوبهم ?) ? ; (4) «2- أَبْحَثُ عَنْ فَوَائِدِ السَّمْعِ وَالطَّاعَةِ لِوَلِيِّ الْأَمْرِ.» ; (5) Y a-t-il UN ENCADRÉ ou texte décoré en bas de page (avec un début de hadith comme «عن أبي نجيح العُرباض بن سارية...») ? TRANSCRIS tout ce qui est imprimé dans la zone.`],
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
