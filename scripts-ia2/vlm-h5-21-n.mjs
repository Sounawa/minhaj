// Z2-24 — hadith-5ep leçon 21 — adjudications VLM lettre-niveau SÉRIE N (n01-n39+b) pp.114-119
// Usage: node vlm-h5-21-n.mjs <liste de tags, ex: n01 n02> (défaut: tous)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-21';

const COMMON = `Extrait 600 dpi agrandi d'un manuel scolaire marocain d'hadith (5e année primaire), leçon 21 «النهي عن الغضب» (pp.114-119), sens de lecture droite→gauche.
TRANSCRIS EXACTEMENT ce qui est imprimé, mot à mot, avec la vocalisation. Analyse LES LETTRES UNE À UNE pour les mots signalés : nomme chaque lettre de base (alif, bāʾ, tāʾ, thāʾ, ǧīm, ḥāʾ, khāʾ, dāl, dhāl, rāʾ, zāy, sīn, shīn, ṣād, ḍād, ṭāʾ, ẓāʾ, ʿayn, ġayn, fāʾ, qāf, kāf, lām, mīm, nūn, hāʾ, wāw, yāʾ) et les points (0/1/2/3) au-dessus/dessous, plus les diacritiques (fatha, kasra, ḍamma, sukūn, shadda, tanwīn). Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé. Illisible : [؟]. Réponds par : TRANSCRIPTION puis RÉPONSES.`;

const Q = {
  n01: `Tuile DROITE de l'encadré أهداف الدرس (objectifs 1-2, p.114). Transcris tout.
QUESTIONS : (1) objectif 1 : le verbe après « أَنْ » — LETTRE PAR LETTRE : أَتَعَرَّفَ (tāʾ, ʿayn, rāʾ+shadda, fāʾ) ou أَعْرِفَ (4 lettres) ? (2) après ce verbe : « الْغَضَبَ » (FATHA, objet direct) ou « الْغَضَبِ » (kasra) ? (3) puis « وَمَوْقِفَ » (fatha, 2e objet) ou « وَمَوْقِفُ » (ḍamma) ou « وَمَوْقِفِ » (kasra) ? puis « الشَّرْعِ مِنْهُ » ? (4) objectif 2 : transcris-le en entier, LETTRE PAR LETTRE le verbe après « أَنْ » (أَدْرِكَ ? أُدْرِكَ ?) et « ثَمَرَاتِ ضَبْطِ النَّفْسِ عِنْدَ الْغَضَبِ ».`,
  n02: `Tuile GAUCHE de l'encadré أهداف الدرس (p.114, fins de lignes). Transcris tout ce qui est visible.
QUESTIONS : (1) y a-t-il un objectif 4 ? Combien d'objectifs numérotés en tout ? (2) objectif 3 : transcris-le INTÉGRALEMENT — LETTRE PAR LETTRE le verbe après « أَنْ » (أَتَمَثَّلُ ? أَتَخَلَّقُ ?) et les mots « الْمَقَاصِدَ الشَّرْعِيَّةَ لِلنَّهْيِ عَنِ الْغَضَبِ » ou autre.`,
  n03: `Tuile DROITE du تمهيد (p.114, début). Transcris tout.
QUESTIONS : (1) « الْإِنْسَانُ اجْتِمَاعِيٌّ بِطَبْعِهِ » — LETTRE PAR LETTRE « بِطَبْعِهِ » (bāʾ+kasra, ṭāʾ+fatha, bāʾ+sukūn, ʿayn+kasra, hāʾ) : y a-t-il une tāʾ marbūṭa (بِطَبْعَتِهِ) ? (2) « وَلِهَذَا كَانَ مِمَّنْ يُخَالِطُ الْآخَرِينَ » — confirme. (3) « فَيَصِيبُهُ مِنْهُمْ أَذًى مِنْ قَوْلٍ أَوْ فِعْلٍ » — LETTRE PAR LETTRE « أَذًى » et « فِعْلٍ ».`,
  n04: `Tuile GAUCHE du تمهيد (p.114, phrases 2-3). Transcris tout.
QUESTIONS : (1) après « فَيَغْضَبُ » : « وَيَتَحَرَّكُ » (wāw+yāʾ) ou « وَتَتَحَرَّكُ » (wāw+tāʾ) ? LETTRE PAR LETTRE. (2) puis « لِيُقَابِلَ الْأَذَى بِالْأَذَى وَالشَّرِّ بِمِثْلِهِ » — LETTRE PAR LETTRE le dernier mot : بِمِثْلِهِ (hāʾ finale SANS point) ou بِمِثْلِهَا (tāʾ marbūṭa 2 points) ? (3) la phrase suivante : transcris-la INTÉGRALEMENT — commence-t-elle par « وَلِدَفْعِ ذَلِكَ » ou « وَقَدْ جَعَلَ » ou autre ? y a-t-il « لِلشَّرْعِ » ou « الشَّرْعُ » comme sujet ? « مَوْقِفًا مِنَ الْغَضَبِ » ou « مَوْقِفٍ » ? (4) le mot après « يَقْبَلُهُ » (ou le verbe équivalent) — LETTRE PAR LETTRE. (5) « تَهْذِيبِ الْفَرْدِ وَسُلُوكِهِ وَمُعَامَلَاتِهِ » — LETTRE PAR LETTRE le mot avant « الْفَرْدِ ».`,
  n05: `Tuile DROITE de la ligne des questions de transition (p.114, sous le تمهيد). Transcris tout.
QUESTIONS : LETTRE PAR LETTRE la 1re question : « فَمَا مَوْقِفُ الشَّرْعِ مِنَ الْغَضَبِ ؟ » — vocalisation de مَوْقِفُ (ḍamma) et الشَّرْعِ (kasra) et مِنَ (fatha sur nūn) ? Transcris la ligne complète.`,
  n05b: `Tuile GAUCHE de la ligne des questions (p.114). Transcris tout.
QUESTIONS : LETTRE PAR LETTRE le mot entre « أَثَرُ » et « النَّفْسِ » : تَمَلُّكِ (tāʾ+mīm+lām+SHADDA+kāf+kasra) ou مَلْكِ (mīm+lām+kāf) ou تَمَالِكِ ou مَالِكِ ? Décris chaque lettre et diacritique. Puis « عِنْدَ الْغَضَبِ ؟ » — confirme.`,
  n06: `Tuile DROITE du CADRE DU HADITH (p.114) : pastille de titre + début du sanad. Transcris tout.
QUESTIONS : (1) la pastille/titre au-dessus du cadre : LETTRE PAR LETTRE — « الْحَدِيثُ » ou « أَحْدِيثُ » ou « نَصُّ الْحَدِيثِ » ou autre ? (2) le sanad : « عَنْ أَبِي هُرَيْرَةَ رَضِيَ اللهُ عَنْهُ أَنَّ رَجُلًا قَالَ لِلنَّبِيِّ » — LETTRE PAR LETTRE « أَنَّ رَجُلًا » (hamza+lām+shadda? rāʾ+ǧīm? tanwīn?) ; la formule après لِلنَّبِيِّ est-elle la ligature ﷺ ou « صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ » écrite en toutes lettres ?`,
  n07: `Tuile GAUCHE du CADRE DU HADITH (p.114) : fin du sanad + matn + référence. Transcris tout.
QUESTIONS : (1) « أَوْصِنِي » — LETTRE PAR LETTRE (alif, wāw+sukūn, ṣād+kasra, nūn+kasra, yāʾ). (2) combien de fois « لَا تَغْضَبْ » est-il imprimé dans le cadre ? Transcris TOUT le matn dans l'ordre exact, avec ce qui est entre les occurrences (« قَالَ: » / « فَرَدَّدَ مِرَارًا، » / autre). (3) la référence : [صحيح البخاري] exactement ? (4) y a-t-il une ponctuation (.) après « أَوْصِنِي » ?`,
  n08: `Tuile DROITE de la rubrique تَرْجَمَةُ الرَّاوِي (p.115). Transcris tout.
QUESTIONS : (1) LETTRE PAR LETTRE le nom : « أَبُو هُرَيْرَةَ » ? (2) après « رَضِيَ اللهُ عَنْهُ » : y a-t-il « ، » ou « ؛ » puis quoi — « سَبَقَتْ » suivi de QUOI exactement ? Transcris le reste de la ligne mot à mot (« تَرْجَمَتُهُ » ? « فِي » ? autre ?).`,
  n08b: `Tuile GAUCHE de la rubrique تَرْجَمَةُ الرَّاوِي (p.115, fins de lignes). Transcris tout.
QUESTIONS : (1) transcris chaque fragment visible lettre par lettre. (2) la bio se termine par quoi (un point ? une phrase complète ?) ?`,
  n09: `Tuile DROITE : titre الشَّرْح + item 1 (p.115). Transcris tout.
QUESTIONS : (1) le titre : « الشَّرْحُ : » ou « الشَّرْح: » ? (2) item 1 : quel est le mot-vedette (en gras/coloré) — « أَوْصِنِي » ? « أَوْصِي » ? — LETTRE PAR LETTRE. (3) le DÉBUT de sa définition : transcris les 3-6 premiers mots LETTRE PAR LETTRE (peut être « أَعْهِدْ إِلَيَّ... » ou « أَرْشِدْنِي... » ou autre).`,
  n10: `Tuile GAUCHE : fin de l'item 1 + item 2 du الشَّرْح (p.115). Transcris tout.
QUESTIONS : (1) la fin de la définition de l'item 1. (2) item 2 : le mot-vedette LETTRE PAR LETTRE : « فَرَدَّدَ مِرَارًا » (dāl+shadda) ou « فَرَدَدَ مِرَارًا » ? (3) sa définition : « كَرَّرَ [X] [Y] » — transcris X et Y LETTRE PAR LETTRE (« النَّهْيَ » ? « عَنْهُ » ? « عَدَّةَ مَرَّاتٍ » ? « مِرَّاتٍ » ?).`,
  n11: `Tuile DROITE : item 3 du الشَّرْح + titre استخلاص + question 1 (p.115). Transcris tout.
QUESTIONS : (1) item 3 : mot-vedette « لَا تَغْضَبْ » ? sa définition LETTRE PAR LETTRE (peut être « لَا تَنْفُذْ/لَا تُنَفِّذْ غَضَبَكَ ضِدَّ مَنْ أَغْضَبَكَ » ou autre). (2) le titre de rubrique : « اِسْتِخْلَاصُ الْمَضَامِينِ » ou « اسْتِخْلَاصُ الْمَضَامِينِ : » — LETTRE PAR LETTRE le second mot (م-ض-ا-م-ي-ن ?). (3) question 1 : transcris-la INTÉGRALEMENT — LETTRE PAR LETTRE le verbe d'ouverture (أُحَدِّدُ ?) et ce qui suit « سَبَبَ » (تِكْرَارِ ? حَصْرِ ? حَظْرِ ? rien ?) et la citation « لَا تَغْضَبْ ».`,
  n12: `Tuile DROITE : question 2 de استخلاص + début du التحليل (p.115). Transcris tout.
QUESTIONS : (1) question 2 : transcris-la INTÉGRALEMENT — LETTRE PAR LETTRE le verbe d'ouverture (أَسْتَنْتِجُ / أَسْتَوْجِبُ / أَسْتَخْرِجُ / أَسْتَبِينُ ?) ; puis « سَبَبَ [X] الْجَوَابِ فِي كَلِمَةِ » — LETTRE PAR LETTRE [X] : حَصْرِ (ḥāʾ+ṣād SANS point+rāʾ) ou حَظْرِ (ḥāʾ+ẓāʾ 1 point+rāʾ) ou تِكْرَارِ ? (2) le titre « التَّحْلِيلُ » puis l'intro : « حَدِيثُ الرَّسُولِ ﷺ مِنْ جَوَامِعِ كَلِمِهِ... » — transcris la phrase complète.`,
  n13: `Tuile GAUCHE : suite de l'intro du التحليل (p.115). Transcris tout.
QUESTIONS : (1) LETTRE PAR LETTRE ce qui suit « كَلِمِهِ ﷺ » (ou la formule équivalente) : « لَخَّصَ » ? « وَقَدْ لَخَّصَ » ? puis les mots jusqu'à « مَا يَأْتِي : » (peut contenir « عُدَّةً », « ضَوَابِطَ », « مَضَامِينَ »...). (2) le titre « أَوَّلًا: ... » : transcris-le en entier.`,
  n14: `Tuile DROITE : titre أولاً + ligne numérotée en vert + début « لَمَّا طَلَبَ » (p.115). Transcris tout.
QUESTIONS : (1) « أَوَّلًا : النَّهْيُ عَنِ الْغَضَبِ وَالْمُرَادُ بِهِ » ou « وَمَا أُرِيدَ بِهِ » ? LETTRE PAR LETTRE la fin du titre. (2) la ligne suivante (numérotée, en vert) : transcris-la INTÉGRALEMENT LETTRE PAR LETTRE — commence-t-elle par « 1. » ou « ١. » ? quel est le premier mot (« التَّهْيِئَةُ » ? « التَّحْذِيرُ » ? autre ?) et la suite jusqu'à la fin de ligne. (3) le début de « لَمَّا طَلَبَ الصَّحَابِيُّ رَضِيَ اللهُ عَنْهُ... » si visible.`,
  n15: `Tuile GAUCHE : fin du § أولاً (p.115, lignes « بِمَا يَنْفَعُهُ... » et dernière ligne). Transcris tout.
QUESTIONS : (1) « وَتُعَدُّ » ou « وَتَعُدُّ » — LETTRE PAR LETTRE le verbe (shadda sur ʿayn ? ḍamma sur tāʾ ?). (2) « مِنْ جَوَامِعِ كَلِمِهِ ﷺ » puis les mots suivants jusqu'à « شَامِلَةً » : transcris-les INTÉGRALEMENT LETTRE PAR LETTRE (peut contenir « الْمُظْهِرَةَ », « لِسَمْوِ », « صِيَاغَةً »...). (3) la dernière ligne se termine par « فَفِيهَا » ou « فَفِيهِ » ?`,
  n16: `Tuile DROITE : haut de la p.116 (« فَفِيهَا النَّهْيُ عَنْ... »). Transcris tout.
QUESTIONS : (1) LETTRE PAR LETTRE le mot entre « عَنْ » et « الْغَضَبِ » : تَثْبِيطِ (thāʾ 3 points + bāʾ + yāʾ + ṭāʾ) ou تَحْرِيكِ (ḥāʾ + rāʾ + kāf) ou تَحْبِيطِ ou autre ? (2) « وَتَدْرِيبُ النَّفْسِ » (ḍamma) ou « وَتَدْرِيبِ » (kasra) ? (3) « وَالْأَمْرُ بِضَبْطِ النَّفْسِ وَكَظْمِ الْغَيْظِ » — LETTRE PAR LETTRE « وَكَظْمِ » (kāf+ẓāʾ 1 point+mīm). (4) la suite : « الَّذِي هُوَ مِنْ أَفْعَالِ الْمُحْسِنِينَ الَّذِينَ مَلَكُوا أَنْفُسَهُمْ... » — transcris la fin de la dernière ligne visible.`,
  n17: `Tuile DROITE : titre « 2. الْمُرَادُ بِقَوْلِهِ ﷺ لَا تَغْضَبْ » + ligne du sens (p.116). Transcris tout.
QUESTIONS : (1) le numéro : chiffre arabe-oriental ٢ ou occidental 2 ? (2) LETTRE PAR LETTRE le titre complet (guillemets autour de لَا تَغْضَبْ ?). (3) la ligne du sens : « مَعْنَى قَوْلِهِ ﷺ « لَا تَغْضَبْ » أَيْ : لَا [VERBE] [X] الْغَضَبِ فِي نَفْسِكَ » — LETTRE PAR LETTRE le VERBE : تَسْتَجِبْ (tāʾ+sīn+tāʾ+ǦĪM 1 POINT DESSOUS+bāʾ+sukūn) ou تَسْتَحِبَّ (tāʾ+sīn+tāʾ+ḤĀʾ 0 POINT+bāʾ) ou تُثِرْ ou autre ? Combien de points sur la 4e lettre ? Puis LETTRE PAR LETTRE [X] : لِدَاعِي (lām+dāl+ʿayn+yāʾ) ou دَاعِيَ ou دَاعِيَةَ ou الذَّائِعَ ?`,
  n18: `Tuile GAUCHE : « فَالْمُرَادُ بِالنَّهْيِ... وَلِأَنَّهُ مِنْ طَبَائِعِهِ... » (p.116). Transcris tout.
QUESTIONS : (1) « مُقَابَلَةً لِلْأَذَى بِالْأَذَى وَالشَّرِّ بِ[X] » — LETTRE PAR LETTRE [X] : مِثْلِهِ (mīm+thāʾ+lām+hāʾ SANS point) ou مِثْلِهَا (tāʾ marbūṭa) ? (2) « وَلِأَنَّهُ مِنْ طَبَائِعِهِ وَشُعُورِهِ [SUITE] » — transcris la SUITE INTÉGRALEMENT LETTRE PAR LETTRE (peut être « قَلَّ مِنَ الْإِنْسَانِ مَنْ يَسْلَمُ مِنْهُ » ou « قَلَّ إِنْسَانٌ إِلَّا وَهُوَ... » ou autre).`,
  n19: `Tuile DROITE : « لَكِنْ يُمْكِنُهُ أَنْ يُهَذِّبَ هَذِهِ الْغَرِيزَةَ... » (p.116). Transcris tout.
QUESTIONS : (1) LETTRE PAR LETTRE « يُهَذِّبَ » (shadda sur dhāl) et « يَتَمَلَّكَهَا » (shadda sur lām). (2) après « وَلَا » : LETTRE PAR LETTRE le verbe — يُنَادِلَهَا (yāʾ+nūn+alif+dāl+lām) ou يُجَادِلَهَا (yāʾ+ǦĪM+alif+dāl+lām) ou يُنَازِلَهَا (zāy) ou يُنَافِسَهَا ? Décris la 2e lettre de base et ses points. (3) « فَيُطْفِئَ جَمْرَةَ غَضَبِهِ » — LETTRE PAR LETTRE le siège de la hamza dans فَيُطْفِئَ. (4) la suite de la ligne (« وَيَمْنَعُ... ») si visible.`,
  n20: `Tuile GAUCHE : « وَيَمْنَعُ ... فِي حَالَةِ الْغَضَبِ وَيُقَاوِمُ... » + transition (p.116). Transcris tout.
QUESTIONS : (1) LETTRE PAR LETTRE les 2-4 mots entre « وَيَمْنَعُ » et « فِي حَالَةِ الْغَضَبِ » (peut être « لِسَانَهُ عَنِ السَّفَهِ » ou « نَفْسَهُ عَنْ تَصَرُّفَاتٍ » ou autre). (2) « وَيُقَاوِمُ [SUITE] » — transcris la suite LETTRE PAR LETTRE jusqu'à « الطَّبْعِ الْبَشَرِيِّ » (peut contenir « وَسَاوِسَ الشَّيْطَانِ », « وَانْفِعَالَاتِ »...). (3) transcris toute ligne supplémentaire visible.`,
  n21: `Tuile DROITE : hadith de عَطِيَّةَ السَّعْدِيِّ (p.116). Transcris tout.
QUESTIONS : (1) « وَقَدْ جَاءَ فِي الْحَدِيثِ عَنْ عَطِيَّةَ السَّعْدِيِّ رَضِيَ اللهُ عَنْهُ » — LETTRE PAR LETTRE « عَطِيَّةَ » et « السَّعْدِيِّ ». (2) après « عَنْهُ » : « قَالَ: » puis « قَالَ رَسُولُ اللهِ ﷺ: » ou direct ? (3) le matn : « إِنَّ الْغَضَبَ مِنَ الشَّيْطَانِ وَإِنَّ الشَّيْطَانَ خُلِقَ مِنَ النَّارِ وَإِنَّمَا [X] النَّارُ بِالْمَاءِ » — LETTRE PAR LETTRE [X] : تُطْفَأُ (tāʾ+ṭāʾ+fāʾ+hamza) ou تُقْمَعُ ou يُطْفِئُ ou autre ? (4) la fin visible du matn (« فَإِذَا غَضِبَ أَحَدُكُمْ [Y] ») — LETTRE PAR LETTRE [Y] : فَلْيَغْتَسِلْ (fāʾ+lām+yāʾ+ĠAYN+tāʾ+sīn+lām) ou فَلْيَتَوَضَّأْ (wāw+ḍād+shadda+hamza) ou فَلْيَنْضَحْ ? Décris CHAQUE lettre.`,
  n22: `Tuile DROITE : « وَلِهَذَا يَخْرُجُ الْإِنْسَانُ بِالْغَضَبِ مِنِ اعْتِدَالِ حَالِهِ... » (p.116). Transcris tout.
QUESTIONS : (1) LETTRE PAR LETTRE « اعْتِدَالِ ». (2) les trois compléments : « فَيَقُولُ [X] وَيَرْتَكِبُ [Y] وَيَنْتَهِكُ [Z] » — LETTRE PAR LETTRE X, Y, Z (peut être الْبَاطِلَ / الْمَآثِمَ / الْحُدُودَ / الْحُرُمَاتِ...). (3) « وَغَيْرُ » ou « وَغَيْرَ » ? puis « ذَلِكَ مِنَ الْمُحَرَّمَاتِ » ou « مِنَ الْمُحَرَّمَةِ » ?`,
  n23: `Tuile GAUCHE : « فَالشَّيْطَانُ هُوَ الَّذِي زَيَّنَ... » + الاستعاذة (bas p.116). Transcris tout.
QUESTIONS : (1) « فَالشَّيْطَانُ هُوَ الَّذِي زَيَّنَ لَهُ [X] الْغَضَبِ وَيَدْفَعُ [Y] » — LETTRE PAR LETTRE [X] et [Y] et la suite. (2) « فَمَنِ اسْتَجَابَ لِلشَّيْطَانِ مِنْ حَيْثُ لَا يَشْعُرُ » — confirme. (3) « وَالِاسْتِعَاذَةُ بِاللهِ مِنَ الشَّيْطَانِ مِنْ أَقْوَى [X] [Y] كَيْدِهِ » — LETTRE PAR LETTRE [X] (الْحِيَلِ ou الْحِيَلَةِ) et [Y] (دَفْعُ ou دَفْعَ ou لِدَفْعِ).`,
  n24: `Tuile DROITE : titre « ثَانِيًا » + phrase d'intro (haut p.117). Transcris tout.
QUESTIONS : (1) « ثَانِيًا : فَضْلُ [X] النَّفْسِ عِنْدَ الْغَضَبِ » — LETTRE PAR LETTRE [X] : مِلْكِ (mīm+kasra, lām+sukūn, kāf+kasra) ou مَلْكِ (fatha sur mīm) ou مَالِكِ (avec alif) ? (2) la phrase d'intro : transcris-la INTÉGRALEMENT LETTRE PAR LETTRE — commence-t-elle par « لِأَنَّ فِي » ou « لَا يَخْفِي أَنَّ فِي » ? quels mots entre « فِي » et « عِنْدَ الْغَضَبِ » (عَزْمِ الْإِنَاةِ وَالتَّجَلُّدِ ? كَظْمِ الْغَيْظِ ? autre) ? et après « عِنْدَ الْغَضَبِ » (جِمَاعَ الْفَضْلِ ? رَكِيزَةَ ? الْخَيْرِ ?). (3) « الثَّمَرَاتُ مِنْ ذَلِكَ : » — confirme.`,
  n25: `Tuile DROITE : الثمرة 1 (p.117). Transcris tout.
QUESTIONS : (1) LETTRE PAR LETTRE les 2 premiers mots après « 1. » (peut être « الْفَوْزُ بِمَدْحِ » ou « نَيْلُ مَدْحِ » ou « نَيْلُ فَضْلِ » ou autre) — décris chaque lettre. (2) « اللهِ تَعَالَى » ou « اللهِ عَزَّ وَجَلَّ » ? (3) « لِمَنْ يَكْظِمُ [X] » — LETTRE PAR LETTRE [X] : غَضَبَهُ (ġayn+ḍād) ou غَيْظَهُ (ġayn+yāʾ+ẓāʾ) ou les DEUX « غَضَبَهُ وَغَيْظَهُ » ? (4) « قَالَ تَعَالَى : » puis le début du verset si visible.`,
  n26: `Tuile GAUCHE : fin الثمرة 1 (« لَيْسَ الشَّدِيدُ... ») + début الثمرة 2 (p.117). Transcris tout.
QUESTIONS : (1) « وَفَضْلُ مَدْحِ الرَّسُولِ ﷺ بِقَوْلِهِ : « لَيْسَ الشَّدِيدُ بِ[X] إِنَّمَا الشَّدِيدُ الَّذِي [Y] نَفْسَهُ عِنْدَ الْغَضَبِ » » — LETTRE PAR LETTRE [X] (الصُّرَعَةِ : ṣād+rāʾ+ʿayn+tāʾ marbūṭa ?) et [Y] (يَمْلِكُ ou مَلَكَ). (2) la référence : [صحيح البخاري] ? (3) le début de la الثمرة 2 : « 2. [Z] » — LETTRE PAR LETTRE [Z] (الْفَوْزُ بِمَا دَلَّ عَلَيْهِ ? الْقُرْبُ ? autre).`,
  n27: `Tuile DROITE : الثمرة 2 (p.117). Transcris tout.
QUESTIONS : (1) « « مَنْ كَظَمَ غَيْظَهُ وَهُوَ يَسْتَطِيعُ أَنْ [X] دَعَاهُ اللهُ عَزَّ وَجَلَّ عَلَى رُؤُوسِ الْخَلَائِقِ يَوْمَ الْقِيَامَةِ » — LETTRE PAR LETTRE [X] : يُنَفِّذَهُ (yāʾ+nūn+fāʾ+shadda+dhāl+hāʾ) ou يَنْفُذَهُ (sans shadda) ou يُمْضِيَهُ ? (2) « حَتَّى يُخَيِّرَهُ مِنَ الْحُورِ [Y] شَاءَ » — LETTRE PAR LETTRE [Y] : الْعِينِ أَيَّمَا ou أَيَّمَا ou مَا ou rien ? (3) la référence : [سنن الترمذي] ou [رواه الترمذي] ou autre ?`,
  n28: `Tuile DROITE : الثمرة 3 + verset (p.117). Transcris tout.
QUESTIONS : (1) « 3. أَنَّهُ أَحَدُ أَبْوَابِ [X] [Y] الْجَنَّةِ » — LETTRE PAR LETTRE [X] (الْفَوْزِ ou الْقُرْبِ) et [Y] (بِ ou إِلَى ou rien). (2) « لِقَوْلِهِ عَزَّ وَجَلَّ : » puis le verset : transcris le DÉBUT (contient « وَسَارِعُوا إِلَى مَغْفِرَةٍ... » ?) — LETTRE PAR LETTRE le 1er mot du verset.`,
  n29: `Tuile GAUCHE : fin du verset + référence + الثمرة 4 (p.117). Transcris tout.
QUESTIONS : (1) la fin du verset (jusqu'à « الْمُحْسِنِينَ » ?). (2) la référence EXACTE : « [آل عمران: 133-134] » — quels chiffres (arabe-oriental ١٣٣-١٣٤ ou occidental) ? quel séparateur ? (3) الثمرة 4 : transcris-la INTÉGRALEMENT LETTRE PAR LETTRE, du « 4. » jusqu'à la référence (je ne devine pas son contenu : chaque mot, y compris la citation avec « يَوْمَ الْقِيَامَةِ »). (4) sa référence exacte ([رواه الطبراني] ? [للطبراني] ? autre ?).`,
  n30: `Tuile DROITE : 2 lignes fin du التحليل (haut p.118). Transcris tout.
QUESTIONS : (1) 1er mot : « وَالْأَعْرَاضُ » (ʿayn SANS point) ou « وَالْأَغْرَاضُ » (ġayn 1 point) ou « وَالْإِعْرَاضُ » ? LETTRE PAR LETTRE. (2) « السَّلْبِيَّةُ » : ḍamma finale ou kasra ? y a-t-il une virgule ou un point après ? (3) « كَمَا أَنَّ فِي دَفْعِ الْغَضَبِ عَنِ النَّفْسِ حِفَاظًا عَلَى الْعَلَاقَاتِ » — LETTRE PAR LETTRE « عَنِ النَّفْسِ » et « حِفَاظًا ».`,
  n31: `Tuile DROITE : titre de rubrique (mبما يستفاد?) + item 1 (p.118). Transcris tout.
QUESTIONS : (1) le titre de la rubrique : transcris-le EXACTEMENT — « مِمَّا يُسْتَفَادُ : » ou « وَمَا يُسْتَفَادُ مِنَ الْحَدِيثِ : » ou autre ? LETTRE PAR LETTRE. (2) item 1 : transcris-le INTÉGRALEMENT — LETTRE PAR LETTRE le premier mot après « 1. » (الْجَلَدُ ? اللُّجُوءُ ? الاِلْتِجَاءُ ? autre) et la suite (« حَيْثُ لَجَأَ هَذَا الرَّجُلُ... » ?).`,
  n32: `Tuile GAUCHE : items 2-3 du مما يستفاد (p.118). Transcris tout.
QUESTIONS : (1) item 2 : « [X] الْإِنْسَانَ بِمَا يُنَاسِبُ حَالَهُ... مَعَ هَذَا الصَّحَابِيِّ؛ حَيْثُ نَاصَحَهُ [Y] » — LETTRE PAR LETTRE le premier mot [X] (نَصْحُ ? مُنَاسَبَةُ ? autre) et [Y] (بِدَفْعِ الْغَضَبِ عِنْدَ نُزُوعِهِ ? بِرِفْقٍ ? autre). (2) item 3 : « الِاخْتِصَارُ فِي النَّصِيحَةِ وَالْحِرْصُ عَلَى أَنْ تَكُونَ جَامِعَةً؛ فَالرَّسُولُ ﷺ جَعَلَ وَصِيَّتَهُ لِهَذَا الصَّحَابِيِّ [Z] أَوْ [W] » — LETTRE PAR LETTRE [Z] (كَلِمَتَيْنِ ? جَامِلَةً ? autre) et [W] (ثَلَاثٍ SANS tāʾ marbūṭa ou ثَلَاثَةً AVEC).`,
  n33: `Tuile DROITE : rubrique التَّقْوِيم + questions 1-2 (p.118). Transcris tout.
QUESTIONS : (1) question 1 : LETTRE PAR LETTRE le début — « 1. أُحَدِّدُ الْمُرَادَ » ou « 1. أُبَيِّنُ الْمُرَادَ » ou « 1. أَخُصُّ » ou « 1. مَا الْمُرَادُ » ou autre ? (2) question 2 : LETTRE PAR LETTRE le début — « 2. تَخَيَّلْ » ou « 2. أَتَانِي » ou « 2. تَأَتَّى » ou autre ? puis « أَحَدُ [X] » — [X] = صَدِيقَيَّ (dual : ṣād+dāl+yāʾ+qāf+yāʾ) ou صَدِيقِينَ ou أَصْدِقَائِكَ ? puis « غَاضِبًا مِنْ صَدِيقِهِ » ou « غَضِبَ مِنْ صَدِيقِهِ » ?`,
  n34: `Tuile GAUCHE : fin question 2 + question 3 du التَّقْوِيم (p.118). Transcris tout.
QUESTIONS : (1) « وَهُوَ [X] [Y] غَضَبَهُ » — LETTRE PAR LETTRE [X] et [Y] (يُرِيدُ أَنْ يُنَفِّذَ ? يُهَدِّدُ بِتَنْفِيذِ ? يُرِيدُ تَنْفِيذَ ? autre). (2) « فَكَيْفَ أُقْنِعُهُ بِكَظْمِ غَيْظِهِ وَعَدَمِ الِانْسِيَاقِ وَرَاءَ غَضَبِهِ ؟ » — confirme. (3) question 3 : transcris-la INTÉGRALEMENT LETTRE PAR LETTRE (peut être « أُذَكِّرُ آثَارَ كَظْمِ الْغَيْظِ عَلَى الْفَرْدِ وَالْمُجْتَمَعِ » ou autre).`,
  n35: `Tuile DROITE : hadith 1 du الِاسْتِثْمَار (p.119, sanad + début matn). Transcris tout.
QUESTIONS : (1) « عَنْ سُلَيْمَانَ بْنِ صُرَدٍ » — LETTRE PAR LETTRE « صُرَدٍ » ; y a-t-il « رَضِيَ اللهُ عَنْهُ » ? puis « قَالَ: كُنْتُ جَالِسًا مَعَ النَّبِيِّ ﷺ » ? (2) « وَرَجُلَانِ [X] » — LETTRE PAR LETTRE [X] : يَسْتَبَّانِ (bāʾ+shadda) ou يَتَسَابَّانِ (avec tāʾ initiale) ? (3) la suite : « وَأَحَدُهُمَا قَدِ [Y] وَجْهُهُ وَ[Z] أَوْدَاجُهُ » — LETTRE PAR LETTRE [Y] (احْمَرَّ ?) et [Z] (وَانْتَفَخَتْ ? وَانْتَفَضَتْ ?). Décris les lettres de [Z] une à une.`,
  n36: `Tuile GAUCHE : fin hadith 1 (p.119). Transcris tout.
QUESTIONS : (1) « فَقَالَ النَّبِيُّ ﷺ : « إِنِّي لَأَعْلَمُ كَلِمَةً لَوْ قَالَهَا ذَهَبَ عَنْهُ مَا يَجِدُ » — transcris la structure EXACTE : combien de fois « ذَهَبَ عَنْهُ مَا يَجِدُ » est-il imprimé ? où se trouve « لَوْ قَالَ : » ? (2) la formule : « أَعُوذُ بِاللهِ مِنَ الشَّيْطَانِ » — y a-t-il « الرَّجِيمِ » après الشَّيْطَانِ ? (3) la référence : [صحيح البخاري] exactement ? (4) la ponctuation de fin.`,
  n37: `Tuile DROITE : hadith 2 du الِاسْتِثْمَار (p.119). Transcris tout.
QUESTIONS : (1) « وَعَنْ أَبِي ذَرٍّ الْغِفَارِيِّ رَضِيَ اللهُ عَنْهُ قَالَ : قَالَ [X] رَسُولُ اللهِ ﷺ : » — [X] = لَنَا ou rien ? LETTRE PAR LETTRE « ذَرٍّ » (dhāl+shadda+rāʾ+tanwīn) et « الْغِفَارِيِّ ». (2) le matn : « إِذَا غَضِبَ أَحَدُكُمْ وَهُوَ قَائِمٌ فَلْيَجْلِسْ، [Y] » — LETTRE PAR LETTRE [Y] (فَإِنْ ذَهَبَ عَنْهُ الْغَضَبُ وَإِلَّا فَلْيَضْطَجِعْ ou autre enchaînement) ; LETTRE PAR LETTRE « فَلْيَضْطَجِعْ » (ḍād+ṭāʾ+ǧīm). (3) la référence exacte : [سنن أبي داود] ?`,
  n38: `Ligne de question de synthèse après les deux hadiths (p.119). Transcris tout.
QUESTIONS : LETTRE PAR LETTRE : (1) le verbe d'ouverture (« اِسْتَخْرِجْ » ? « اِسْتَنْتِجْ » ? autre ?). (2) « مِنَ الْحَدِيثَيْنِ أَهَمَّ الْوَسَائِلِ [X] الْغَضَبِ عَنِ الْإِنْسَانِ » — [X] = الَّتِي تَدْفَعُ (lām+tāʾ yāʾ + tāʾ+dāl+fāʾ+ʿayn) ou إِلَى دَفْعِ (alif+lām+ḍamma) ou إِلَى تَخْفِيفِ ? Décris chaque lettre de [X].`,
  n39: `Rubrique الْإِعْدَادُ الْقَبْلِيُّ complète (p.119). Transcris tout.
QUESTIONS : (1) le titre : « الْإِعْدَادُ الْقَبْلِيُّ : » — LETTRE PAR LETTRE (alif-lām, hamza SOUS l'alif?, ḍamma sur dāl?). (2) « أَحْفَظُ حَدِيثَ الدَّرْسِ [X]، ثُمَّ [Y] : » — LETTRE PAR LETTRE [X] (الْآتِيَ ou الْمُقْبِلِ) et [Y] (أُجِيبُ ou أُوَافِقُ ou autre). (3) item 1 : transcris-le en entier LETTRE PAR LETTRE (après « 1. »). (4) item 2 : transcris-le en entier LETTRE PAR LETTRE (après « 2. »).`,
};

const zai = await ZAI.create();
const args = process.argv.slice(2);
const keys = args.length ? args : Object.keys(Q);
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of keys) {
  if (!Q[k]) { console.log(`INCONNU ${k}`); continue; }
  const img = fs.readFileSync(`${DIR}/z21-${k}.png`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: COMMON + '\n\n' + Q[k] },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo',
        temperature: 0.1,
        max_tokens: 1300,
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
  await sleep(20000);
}
console.log('\nN-SÉRIE TERMINÉE');
