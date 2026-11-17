// Z2-24 — hadith-5ep leçon 21 «النهي عن الغضب» (pp.114-119) — lecture VLM r-série (25 bandes pleine largeur)
// Usage: node vlm-h5-21-r.mjs [start] [end]   (numéros de bandes, défaut 1..25)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-21';

const COMMON = `Extrait 600 dpi d'un manuel scolaire marocain d'hadith (5e année primaire), leçon 21 «النهي عن الغضب» (pp.114-119), sens de lecture droite→gauche.
TRANSCRIS EXACTEMENT ce qui est imprimé, mot à mot, avec la vocalisation. Pour les mots signalés, analyse LES LETTRES UNE À UNE : nomme chaque lettre de base (alif, bāʾ, tāʾ, thāʾ, ǧīm, ḥāʾ, khāʾ, dāl, dhāl, rāʾ, zāy, sīn, shīn, ṣād, ḍād, ṭāʾ, ẓāʾ, ʿayn, ġayn, fāʾ, qāf, kāf, lām, mīm, nūn, hāʾ, wāw, yāʾ), les points (0/1/2/3) au-dessus/dessous, et les diacritiques (fatha, kasra, ḍamma, sukūn, shadda, tanwīn). Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé. Illisible : [؟]. Réponds en deux parties : TRANSCRIPTION (lignes dans l'ordre, droite→gauche) puis RÉPONSES aux questions.`;

const R = {
  r01: `ZONE : bandeau titre de la leçon (haut de la p.114).
TRANSCRIS tout le bandeau (n° du leçon, titre, décorations éventuelles).
QUESTIONS : (1) le numéro : « الدرس » suivi de quoi (chiffre ٢١ / 21 ou lettres) ? (2) LETTRE PAR LETTRE le titre : est-ce « النَّهْيُ » (nūn+fatha, khāʾ+shadda, yāʾ+ḍamma) ou « النِّهَايَةُ » ou autre ? puis « عَنِ » (kasra sous nūn) ou « عَنْ » (sukūn) ? puis « الْغَضَبِ » (kasra finale) ? Décris chaque lettre et diacritique du titre. (3) Y a-t-il autre chose imprimé dans le bandeau (verset, formule) ?`,
  r02: `ZONE : encadré أهداف الدرس (4 objectifs numérotés, p.114).
TRANSCRIS les 4 objectifs complets avec la vocalisation.
QUESTIONS : (1) objectif 1 : le verbe après « أَنْ » — « أَتَعَرَّفَ » (tāʾ+shadda, ʿayn, rāʾ+shadda, fāʾ) ou « أَعْرِفَ » (4 lettres seulement) ? Puis « الْغَضَبَ » (fatha) ou « الْغَضَبِ » (kasra) ? (2) objectif 2 : transcris-le lettre par lettre — quels sont les mots entre « أَنْ » et « عِنْدَ الْغَضَبِ » ? Y a-t-il « ثَمَرَاتَ » ou « مَرَاتِبَ » ou « آثَارَ » ou « ثَمَرَةَ » ? et « ضَبْطِ » ou « كَظْمِ » ou autre ? (3) objectifs 3 et 4 : transcris-les intégralement, lettre par lettre pour les verbes après « أَنْ ».`,
  r03: `ZONE : paragraphe تمهيد (p.114).
TRANSCRIS tout le paragraphe mot à mot.
QUESTIONS : (1) la 1re phrase : après « وَلِهَذَا كَانَ » vient quoi — « مِمَّنْ » seul puis « يُخَالِطُ الْآخَرِينَ », ou d'autres mots entre ? (2) après « فَيَصِيبُهُ مِنْهُمْ » : transcris exactement (peut-être « الْأَذَى مِنْ قَوْلٍ أَوْ فِعْلٍ » ?). (3) LETTRE PAR LETTRE ce qui suit « وَتَتَحَرَّكُ » — est-ce « فِيهِ دَاعِيَةُ » ou « فِيهِ لِمُقَابَلَةِ » ou autre ? (4) la phrase « وَقَدْ جَعَلَ ... » : qui est le sujet de جَعَلَ — « الشَّرْعُ » ou autre ? puis « لِلْغَضَبِ مَوْقِفًا » ou « مِنَ الْغَضَبِ مَوْقِفًا » ? (5) LETTRE PAR LETTRE le mot après « يَقْبَلُهُ » ou équivalent : « الرَّشِيدُ » ou « الْحَكِيمُ » ou « الْوَسِيطُ » ou « الرَّحِيمُ » ? (6) le mot avant « الْفَرْدِ » : « تَهْذِيبِ » (tāʾ+hāʾ+dhāl+yāʾ+bāʾ) ou « تَرْبِيَةِ » ou « تَفْسِيرِ » ?`,
  r04: `ZONE : questions de transition + en-tête + CADRE DU HADITH (bas de p.114) — LE TEXTE LE PLUS IMPORTANT DE LA LEÇON.
TRANSCRIS : (a) les deux questions, (b) l'en-tête du cadre s'il y en a un (p.ex. نَصُّ الْحَدِيثِ), (c) la chaîne (sanad) COMPLETE, (d) le matn complet, (e) la référence.
QUESTIONS : (1) les questions : « فَمَا مَوْقِفُ الشَّرْعِ مِنَ الْغَضَبِ ؟ وَمَا أَثَرُ مَلْكِ النَّفْسِ عِنْدَ الْغَضَبِ ؟ » — LETTRE PAR LETTRE « مَلْكِ » (mīm+lām+kāf, SANS alif) ou « مَالِكِ » (avec alif) ? (2) sanad : transcris-le exactement — « عَنْ أَبِي هُرَيْرَةَ رَضِيَ اللهُ عَنْهُ ... » ? Qui parle dans le matn — « قُلْتُ » (je) ou « أَنَّ رَجُلًا » (un homme) ou autre ? (3) matn : LETTRE PAR LETTRE « أَوْصِنِي » (alif+wāw+ṣād+kasra+nūn+yāʾ) ; puis le mot répété : « لَا تَغْضَبْ » combien de fois ? que dit le texte entre les deux occurrences (« فَرَدَّدْتُ » / « فَرَدَّدَ مِرَارًا » / autre) ? (4) la référence exacte : [صحيح البخاري] ou autre ? (5) tout autre texte imprimé dans le cadre.`,
  r05: `ZONE : تَرْجَمَةُ الرَّاوي + début du الشَّرْح (haut p.115).
TRANSCRIS tout.
QUESTIONS : (1) la ligne de تَرْجَمَة : LETTRE PAR LETTRE le nom du rāwī — « أَبُو هُرَيْرَةَ » ? puis ce qui suit « رَضِيَ اللهُ عَنْهُ » : « سَبَقَتْ تَرْجَمَتُهُ » ou autre ? transcris la ligne complète. (2) الشَّرْح : transcris l'item 1 complet (le mot expliqué peut être « أَوْصِنِي » ou « لَا تَغْضَبْ » ou autre) avec sa définition. LETTRE PAR LETTRE les 2-3 premiers mots de la définition.`,
  r06: `ZONE : الشَّرْح items suivants (p.115) + éventuel item 3.
TRANSCRIS tous les items visibles.
QUESTIONS : (1) LETTRE PAR LETTRE l'en-tête de l'item 2 : « فَرَدَّدَ » (fāʾ+rāʾ+dāl+SHADDA+dāl) ou « فَرَدَدَ » (sans shadda) ou « فَرَدَّدْتُ » ? puis « مِرَارًا » (avec alif) ou « مَرَّةً » ? (2) sa définition : « كَرَّرَ النَّهْيَ ... » — transcris la fin exactement : « عَنْهُ مِرَّاتٍ » ou « مِرَّةً بَعْدَ مِرَّةٍ » ou autre ? (3) item 3 (s'il existe) : transcris-le intégralement — quel mot est expliqué et comment ?`,
  r07: `ZONE : استخلاص المضامين (2 questions) + début du التحليل + titre أولاً (p.115).
TRANSCRIS tout.
QUESTIONS : (1) question 1 : « أُحَدِّدُ سَبَبَ ... » — LETTRE PAR LETTRE ce qui suit « سَبَبَ » : « قَوْلِهِ » directement, ou « تِكْرَارِ قَوْلِهِ », ou autre ? (2) question 2 : transcris-la intégralement. (3) l'intro du التحليل : « حَدِيثُ الرَّسُولِ ﷺ مِنْ جَوَامِعِ كَلِمِهِ ... » — transcris la phrase complète ; LETTRE PAR LETTRE le mot après « كَلِمِهِ » (p.ex. « لِخُصُوصِ » ?). (4) le titre « أَوَّلًا: ... » : transcris-le (sans doute « النَّهْيُ عَنِ الْغَضَبِ وَمَا أُرِيدَ بِهِ »).`,
  r08: `ZONE : suite du التحليل (fin p.115).
TRANSCRIS toutes les lignes.
QUESTIONS : (1) la ligne après le titre أولاً : transcris-la LETTRE PAR LETTRE (elle commence peut-être par « أَنَّ » ou similaire). (2) « لَمَّا طَلَبَ الصَّحَابِيُّ رَضِيَ اللهُ عَنْهُ مِنَ الرَّسُولِ ﷺ الْوَصِيَّةَ ... » — LETTRE PAR LETTRE ce qui suit « الْوَصِيَّةَ » : « بِمَا يَنْفَعُهُ » ou « بِمَا يَنْفَعُ » ou autre ? (3) « وَتُعَدُّ هَذِهِ الْجُمْلَةُ الْمُخْتَصَرَةُ مِنْ جَوَامِعِ كَلِمِهِ ﷺ ... » — transcris EXACTEMENT la fin de la phrase jusqu'à « فَفِيهَا » : quels mots entre ﷺ et « صِيَاغَةً » / « شَامِلَةً » ? (4) transcris la dernière ligne complète.`,
  r09: `ZONE : suite du التحليل (haut p.116) — phrase dense.
TRANSCRIS tout.
QUESTIONS : (1) la 1re phrase : « النَّهْيُ عَنْ ... الْغَضَبِ وَتَدْرِيبُ النَّفْسِ عَلَى ذَلِكَ وَالْأَمْرُ بِضَبْطِ ... » — LETTRE PAR LETTRE le mot entre « عَنْ » et « الْغَضَبِ » : « تَثْبِيطِ » (thāʾ+bāʾ+yāʾ+ṭāʾ) ou « تَحْرِيكِ » (ḥāʾ+rāʾ+kāf) ou autre ? (2) LETTRE PAR LETTRE les mots après « بِضَبْطِ » : « اللِّسَانِ وَالْعَيْنِ » ou « الثَّغْرِ وَالْعَيْنِ » ou « اللِّسَانِ وَالْعَيْنِ وَالْيَدِ » ou autre ? (3) « الَّذِي هُوَ مِنْ أَفْعَالِ الْمُحْسِنِينَ الَّذِينَ ... » — LETTRE PAR LETTRE la suite : « مَلَكُوا » ? puis quoi (« قُلُوبَهُمْ » ? « كَلِمَتَهُمْ » ?) jusqu'à la fin de la phrase.`,
  r10: `ZONE : titre « 2. الْمُرَادُ بِقَوْلِهِ ﷺ لَا تَغْضَبْ » + début du sens (p.116).
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le titre numéroté 2 complet. (2) la ligne du sens : « مَعْنَى قَوْلِهِ ﷺ لَا تَغْضَبْ ... » — LETTRE PAR LETTRE le début de l'explication : « أَيْ » (alif+yāʾ) ou « أَيْ: » ? puis LETTRE PAR LETTRE le verbe : « تُثِرْ » (tāʾ+ḍamma, thāʾ+kasra, rāʾ+sukūn — 3 lettres) ou « تُحَرِّكْ » (avec shadda sur rāʾ) ou « تَسْتَحِبَّ » ou autre ? puis « دَاعِيَ الْغَضَبِ » ou « دَاعِيَةَ الْغَضَبِ » ? (3) la fin de ligne : « فِي نَفْسِكَ » ou « فِي نَّفْسِكَ » ?`,
  r11: `ZONE : suite du sens + phrase sur la غريزة (p.116).
TRANSCRIS tout.
QUESTIONS : (1) « وَلَا تَنْجَرَّ إِلَى إِمْلَاءَاتِهِ » — LETTRE PAR LETTRE le mot « إِمْلَاءَاتِهِ » (alif+mīm+lām+alif+hamza+tāʾ+hāʾ ?). (2) « فَالْمُرَادُ بِالنَّهْيِ فِي الْحَدِيثِ النَّهْيُ عَنِ الْعَمَلِ بِمَا يَقْتَضِيهِ الْغَضَبُ ... » — LETTRE PAR LETTRE le mot après « الْغَضَبُ » : « مُقَابَلَةً » (ḍamma sur mīm, tanwīn fatha sur lām) ou autre ? puis « لِلْأَذَى بِالْأَذَى وَالشَّرِّ بِمِثْلِهِ » ou « بِمِثْلِهَا » (tāʾ marbūṭa) ? (3) « وَلِأَنَّهُ مِنْ طَبَائِعِهِ وَشُعُورِهِ ... » — transcris EXACTEMENT la suite : « قَلَّ إِنْسَانٌ » ou « قَلَّ مِنَ الْإِنْسَانِ » ou autre ? (4) « لَكِنْ يُمْكِنُهُ أَنْ يُهَذِّبَ هَذِهِ الْغَرِيزَةَ بِأَنْ يَتَمَلَّكَهَا وَلَا ... » — LETTRE PAR LETTRE le verbe après « وَلَا » : « يُنَادِلَهَا » (nūn) ou « يُجَادِلَهَا » (ǧīm) ? (5) transcris la suite : « فَيُطْفِئَ جَمْرَةَ غَضَبِهِ وَيَمْنَعُ ... » — quels mots exacts suivent « وَيَمْنَعُ » et précèdent « فِي حَالَةِ الْغَضَبِ » ?`,
  r12: `ZONE : fin de la phrase + hadith de عَطِيَّةَ السَّعْدِيِّ (p.116).
TRANSCRIS tout.
QUESTIONS : (1) la ligne de transition avant le hadith (contient peut-être « الشَّيْطَانُ » et « طَبْعُ الْبَشَرِيِّ ») : transcris-la LETTRE PAR LETTRE intégralement. (2) l'intro du hadith : « وَقَدْ جَاءَ فِي الْحَدِيثِ عَنْ عَطِيَّةَ السَّعْدِيِّ رَضِيَ اللهُ عَنْهُ ... » — LETTRE PAR LETTRE « عَطِيَّةَ » (ʿayn, ṭāʾ, yāʾ+shadda, hāʾ ?) et « السَّعْدِيِّ ». (3) qui est cité après « قَالَ » — « رَسُولُ اللهِ ﷺ » ? (4) le début du matn : « إِنَّ الْغَضَبَ مِنَ الشَّيْطَانِ وَإِنَّ الشَّيْطَانَ خُلِقَ مِنَ النَّارِ ... » — transcris ce qui est visible ; LETTRE PAR LETTRE ce qui suit « وَإِنَّمَا » : « تُطْفَأُ النَّارُ بِالْمَاءِ » ou autre ?`,
  r13: `ZONE : fin du hadith عطية + conséquences du غضب (p.116).
TRANSCRIS tout.
QUESTIONS : (1) la fin du matn : « ... فَإِذَا غَضِبَ أَحَدُكُمْ [X] » — LETTRE PAR LETTRE [X] : « فَلْيَغْتَسِلْ » (fāʾ+lām+yāʾ+ĠAYN+tāʾ+sīn+lām) ou « فَلْيَتَوَضَّأْ » (wāw+ḍād+shadda) ou autre ? Décris chaque lettre. (2) « وَلِهَذَا يَخْرُجُ الْإِنْسَانُ بِالْغَضَبِ مِنِ اعْتِدَالِ حَالِهِ ... » — LETTRE PAR LETTRE « اعْتِدَالِ ». (3) les trois verbes consécutifs : « فَيَقُولُ [X] وَيَرْتَكِبُ [Y] وَيَنْتَهِكُ [Z] » — transcris [X] [Y] [Z] exactement (peut-être « الْبَاطِلَ / الْمَآثِمَ / الْحُدُودَ » ?). (4) la fin : « وَغَيْرَ ذَلِكَ مِنَ ... » — quel mot exact (« الْمُحَرَّمَاتِ » ?).`,
  r14: `ZONE : الشيطان يزين + الاستعاذة (fin p.116).
TRANSCRIS tout.
QUESTIONS : (1) « فَالشَّيْطَانُ هُوَ الَّذِي ... » — LETTRE PAR LETTRE le verbe : « زَيَّنَ » (zāy+yāʾ+shadda+nūn) ou autre ? puis « لَهُ » ? puis transcris EXACTEMENT ce qui suit jusqu'à « الْغَضَبِ ». (2) « وَيَدْفَعُ ... » — transcris le reste de la phrase (objets du verbe). (3) « فَمَنِ اسْتَجَابَ لِلشَّيْطَانِ مِنْ حَيْثُ لَا يَشْعُرُ » — confirme lettre par lettre « فَمَنِ » et « اسْتَجَابَ ». (4) « وَالِاسْتِعَاذَةُ بِاللهِ مِنَ الشَّيْطَانِ مِنْ أَقْوَى ... » — LETTRE PAR LETTRE la fin : « الْحِيَلِ » (ḥāʾ+yāʾ+lām) ou « الْحِيَلَةِ » ? puis « دَفْعُ كَيْدِهِ » ou « دَفْعَ كَيْدِهِ » ou « لِدَفْعِ كَيْدِهِ » ?`,
  r15: `ZONE : titre « ثانياً » + intro + الثمرات (haut p.117).
TRANSCRIS tout.
QUESTIONS : (1) le titre : « ثَانِيًا: ... » — transcris-le ; LETTRE PAR LETTRE « مَلْكِ » (mīm+lām+kāf SANS alif) ou « مَالِكِ » (avec alif) dans « فَضْلُ مَلْكِ النَّفْسِ » ? (2) la phrase d'intro : « لِأَنَّ ... » — transcris-la LETTRE PAR LETTRE intégralement (elle contient peut-être « عَزْمِ الْإِنَاةِ وَالتَّجَلُّدِ » ou « الْإِنَاةِ » ou « جِمَاعَ الْفَضْلِ » ou « رَكِيزَةَ » ...). (3) l'en-tête de liste : « الثَّمَرَاتُ مِنْ ذَلِكَ: » — transcris-le.`,
  r16: `ZONE : الثمرة 1 + verset آل عمران 134 + hadith ليس الشديد (p.117).
TRANSCRIS tout.
QUESTIONS : (1) « 1. ... » — LETTRE PAR LETTRE les 2 premiers mots de l'item 1 : « الْفَوْزُ بِمَدْحِ » ou « الْفَضْلُ » ou autre ? puis « اللهِ عَزَّ وَجَلَّ وَمَحَبَّتِهِ لِمَنْ يَكْظِمُ [X] » — LETTRE PAR LETTRE [X] : « غَيْظَهُ » (ġayn+yāʾ+ẓāʾ+hāʾ) ou « غَضَبَهُ » (ġayn+ḍād) ou les deux ? (2) le verset : transcris-le ENTIER tel qu'imprimé (avec crochets ou accolades) + la référence EXACTE (numéro(s)). (3) « وَفَضْلُ مَدْحِ الرَّسُولِ ﷺ: ... » — transcris la citation « لَيْسَ الشَّدِيدُ ... » LETTRE PAR LETTRE : « بِالصُّرَعَةِ » (ṣād+rāʾ+ʿayn) ou « بِالصُّرَعِ » ? « يَمْلِكُ نَفْسَهُ » ou « يَمْلِكُ نَفْسَهُ عِنْدَ الْغَضَبِ » ? (4) la référence de ce hadith.`,
  r17: `ZONE : الثمرة 2 + début الثمرة 3 (p.117).
TRANSCRIS tout.
QUESTIONS : (1) « 2. ... » — transcris l'item complet ; LETTRE PAR LETTRE le premier mot : « الْقُرْبُ » ou « الْقُرْبِ » ou autre ? (2) la citation « مَنْ كَظَمَ ... » : LETTRE PAR LETTRE le mot après « وَهُوَ يَسْتَطِيعُ أَنْ » : « يُنَفِّذَهُ » (yāʾ+nūn+fāʾ+SHADDA+dhāl+hāʾ) ou « يَنْفُذَهُ » (sans shadda) ou « يُمْضِيَهُ » ? puis transcris la suite jusqu'à la fin de la citation (peut contenir « دَعَاهُ اللهُ عَزَّ وَجَلَّ عَلَى رُؤُوسِ الْخَلَائِقِ يَوْمَ الْقِيَامَةِ حَتَّى يُخَيِّرَهُ مِنَ الْحُورِ الْعِينِ أَيَّمَا شَاءَ »). (3) la référence de cette citation. (4) « 3. أَنَّهُ أَحَدُ ... » — LETTRE PAR LETTRE : « أَبْوَابِ الْقُرْبِ » ou « أَبْوَابِ الْجَنَّةِ » ou autre ? y a-t-il une préposition avant « الْجَنَّةِ » (بِ / إِلَى) ?`,
  r18: `ZONE : verset آل عمران 133-134 (suite الثمرة 3) + الثمرة 4 (p.117).
TRANSCRIS tout.
QUESTIONS : (1) le verset : transcris-le ENTIER tel qu'imprimé + LETTRE PAR LETTRE la référence : « [آل عمران: 133-134] » ou « [آل عمران: 133-134] » avec quels chiffres exacts (arabe/indien) ? (2) la الثمرة 4 : transcris-la INTÉGRALEMENT lettre par lettre (elle contient peut-être une citation avec « يَوْمَ الْقِيَامَةِ ») — je ne devine pas son contenu : donne chaque mot. (3) sa référence exacte (peut-être [رواه الطبراني] ou [للطبراني]).`,
  r19: `ZONE : الثمرة 5 (bas p.117).
TRANSCRIS tout.
QUESTIONS : (1) « 5. ... » — LETTRE PAR LETTRE les premiers mots : « إِرَاحَةُ الْقَلْبِ » ou autre ? (2) « وَالْحِفَاظُ عَلَى الصِّحَّةِ النَّفْسِيَّةِ وَالْجَسَدِيَّةِ وَالْعَلَاقَاتِ الِاجْتِمَاعِيَّةِ » — confirme « الْحِفَاظُ » (kasra sous ḥāʾ) et « الْعَلَاقَاتِ ». (3) « لِأَنَّ الِاسْتِجَابَةَ لِلْغَضَبِ تُعَرِّضُ ... » — transcris la fin exactement : « لِلْمَخَاطِرِ » ou « لِلْمَخَاطِرِ » (kasra) ou autre ?`,
  r20: `ZONE : fin du التحليل (haut p.118) — 2 lignes.
TRANSCRIS tout.
QUESTIONS : (1) la 1re ligne commence par « وَالْأَ.. » — LETTRE PAR LETTRE ce mot : « الْأَعْرَاضُ » (ʿayn SANS point) ou « الْأَغْرَاضُ » (ġayn 1 point) ? puis « السَّلْبِيَّةِ » ou « السَّلْبِيَّةُ » ? (2) la 2e ligne : « كَمَا أَنَّ فِي دَفْعِ الْغَضَبِ عَنِ ... » — LETTRE PAR LETTRE le mot après « عَنِ » : « النَّفْسِ » (nūn+fatha, fāʾ+sukūn, sīn+kasra) ou autre ? puis « حِفَاظًا عَلَى الْعَلَاقَاتِ الْأُسْرِيَّةِ وَالِاجْتِمَاعِيَّةِ » — confirme « حِفَاظًا » (tanwīn) et « الْأُسْرِيَّةِ ».`,
  r21: `ZONE : rubrique مما يستفاد (p.118) — header + items.
TRANSCRIS tout (header décoratif inclus).
QUESTIONS : (1) le titre de la rubrique : « مِمَّا يُسْتَفَادُ » ou « مِمَّا يُسْتَفَادُ : » ? (2) item 1 : transcris-le INTÉGRALEMENT lettre par lettre (il parle du Prophète ﷺ avec ce compagnon — je ne devine pas : chaque mot). (3) item 2 : « الِاخْتِصَارُ فِي النَّصِيحَةِ وَالْحِرْصُ عَلَى أَنْ تَكُونَ جَامِعَةً » — LETTRE PAR LETTRE « الِاخْتِصَارُ » et le mot avant « أَوْ » à la fin : « كَلِمَتَيْنِ » (kāf+lām+mīm+tāʾ+yāʾ+nūn) ou « كَلِمَاتٍ » ou autre ? et « ثَلَاثٍ » (SANS tāʾ marbūṭa) ou « ثَلَاثَةٍ » ?`,
  r22: `ZONE : rubrique التَّقْوِيم (p.118) — 3 questions.
TRANSCRIS les 3 questions complètes.
QUESTIONS : (1) question 1 : transcris le début exact — « 1. مَا الْمُرَادُ » ou « 1. أُبَيِّنُ الْمُرَادَ » ou autre ? (2) question 2 : « تَخَيَّلْ » ou « تَصَوَّرْ » en premier mot ? puis LETTRE PAR LETTRE le passage « وَهُوَ يُرِيدُ أَنْ [X] » : [X] = « يُنَفِّذَ غَضَبَهُ » ou « يُثْبِتَ غَضَبَهُ » ou autre ? puis « فَكَيْفَ أُقْنِعُهُ » (alif+ḍamma+qāf) ou « فَكَيْفَ تُقْنِعُهُ » (tāʾ) ? (3) question 3 : transcris-la INTÉGRALEMENT lettre par lettre (dernière question, peut commencer par « وَأُذْكِرُ » ou « وَأَقْتَرِحُ » ou autre).`,
  r23: `ZONE : rubrique الِاسْتِثْمَارُ + hadith 1 (haut p.119).
TRANSCRIS tout (titre de rubrique + sanad + matn + référence).
QUESTIONS : (1) le titre : « الِاسْتِثْمَارُ » ? (2) le sanad : « عَنْ سُلَيْمَانَ بْنِ صُرَدٍ » — LETTRE PAR LETTRE « صُرَدٍ » (ṣād+ḍamma, rāʾ+fatha, dāl+tanwīn kasra) ? puis « رَضِيَ اللهُ عَنْهُ قَالَ: كُنْتُ جَالِسًا مَعَ النَّبِيِّ ﷺ » ? (3) le matn : transcris-le ENTIER ; LETTRE PAR LETTRE « وَرَجُلَانِ يَسْتَبَّانِ » (bāʾ+shadda) ; puis « إِنِّي لَأَعْلَمُ كَلِمَةً لَوْ قَالَهَا ذَهَبَ عَنْهُ مَا يَجِدُ » ; puis la formule finale : « أَعُوذُ بِاللهِ مِنَ الشَّيْطَانِ » — y a-t-il « الرَّجِيمِ » après الشَّيْطَانِ ? (4) la référence exacte : [صحيح البخاري] ?`,
  r24: `ZONE : hadith 2 du الِاسْتِثْمَارُ (p.119).
TRANSCRIS tout (sanad + matn + référence).
QUESTIONS : (1) le sanad : « وَعَنْ أَبِي ذَرٍّ الْغِفَارِيِّ » — LETTRE PAR LETTRE le nom : y a-t-il « أَبِي » puis « ذَرٍّ » (dhāl+shadda+rāʾ) puis « الْغِفَارِيِّ » (ġayn+fāʾ+alif+rāʾ+yāʾ+shadda) ? (2) le matn : « إِذَا غَضِبَ أَحَدُكُمْ وَهُوَ قَائِمٌ فَلْيَجْلِسْ ... » — LETTRE PAR LETTRE ce qui suit « فَلْيَجْلِسْ » : « فَإِنْ ذَهَبَ عَنْهُ الْغَضَبُ » puis « وَإِلَّا فَلْيَضْطَجِعْ » ou autre enchaînement ? « فَلْيَضْطَجِعْ » (ḍād+ṭāʾ+ǧīm) — confirme les lettres. (3) la référence exacte : [سنن أبي داود] ?`,
  r25: `ZONE : question de synthèse + الإعداد القبلي (bas p.119).
TRANSCRIS tout.
QUESTIONS : (1) la question sur les deux hadiths : transcris-la INTÉGRALEMENT — LETTRE PAR LETTRE le verbe d'ouverture (avant « مِنَ الْحَدِيثَيْنِ » ou similaire) et le mot après « إِلَى » : « تَخْفِيفِ » ou « دَفْعِ » ? (2) le titre : « الْإِعْدَادُ الْقَبْلِيُّ » ou « الْإِعْدَادُ الْقَبْلِيُّ: » ? (3) « أَحْفَظُ حَدِيثَ الدَّرْسِ [X]، ثُمَّ [Y]: » — LETTRE PAR LETTRE [X] : « الْآتِيَ » ou « الْمُقْبِلِ » ? et [Y] : « أُجِيبُ » ou « أُلَازِمُ » ou autre ? (4) item 1 : transcris-le LETTRE PAR LETTRE (peut-être « أَتَعَرَّفُ الْإِحْسَانَ » ?). (5) item 2 : transcris-le INTÉGRALEMENT.`,
};

const zai = await ZAI.create();
const a = parseInt(process.argv[2] || '1', 10);
const b = parseInt(process.argv[3] || '25', 10);
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (let i = a; i <= b; i++) {
  const k = 'r' + String(i).padStart(2, '0');
  if (!R[k]) continue;
  const img = fs.readFileSync(`${DIR}/z21-${k}.png`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: COMMON + '\n\n' + R[k] },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo',
        temperature: 0.1,
        max_tokens: 1400,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(`${DIR}/z21-${k}.txt`, txt);
      console.log(txt);
      done = true;
    } catch (e) {
      console.log(`tentative ${attempt} ${k} échec: ${e.message}`);
      await sleep(8000 * attempt);
    }
  }
  if (!done) console.log(`ABANDON ${k}`);
  await sleep(3000);
}
console.log('\nVAGUE R TERMINÉE');
