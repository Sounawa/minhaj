#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-40 — vérification de la livraison hadith-6ep / pdf-mut23h3b-685
# (البر حسن الخلق — hadiths an-Nawwās b. Samʿān + Wābiṣa b. Maʿbad, Muslim / Nawawī 27).
# Leçon 5 du tirage : pp.36-40 du manuel. Données adjudiquées Z2-40 :
# textlayer 34-42 + bbox word-level (cmap glyphes + coordonnées) + tesseract ara 600 dpi psm 4/6
# + strips 1200 dpi psm 4/6/7/8/13 (autocontrast ×2-×10, binarisation) + extraction couche
# colorée (bandeaux bleus texte blanc, en-têtes bleus sur jaune) + anatomie pixel (points
# diacritiques) + recoupement شرح ابن دقيق العيد (shamela 11244/84) et leçon parallèle
# dr-alaskar.com/play-2802 (يورث نفرة، اسم جامع للخير وكل فعل مرضي، الرفق في المحاولة،
# البذل في الإحسان، سنة تسع). VLM INDISPONIBLE ce tour (quota 429 dès la 1re lecture).
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-6ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-6ep/pdf-mut23h3b-685.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-mut23h3b-685']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-mut23h3b-685 unique', len(les) == 1, f'{len(les)} occurrences')
l = les[0]
fr = l.get('htmlFr') or ''
check('livraison posée dans le JSON (htmlFr = contenu)', fr.strip() == src.strip(), f'{len(fr)} vs {len(src)}')
# — structure —
check('volume cohérent (leçon 5 pp., 24-33k car)', 24000 <= len(src) <= 33000, f'{len(src)} car')
check('titre h1 présent', src.startswith('<h1>La bonté pieuse, c’est la beauté du caractère</h1>'))
check('sections h2 = 10', src.count('<h2>') == 10, f'h2={src.count("<h2>")}')
check('sections h3 = 4 (extraction + أولاً + ثانياً + ثالثاً)', src.count('<h3>') == 4, f'h3={src.count("<h3>")}')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Introduction', 'Le hadith', 'Notice du transmetteur',
       'L’explication', 'Extraction des idées', 'L’analyse', 'Ce que le hadith enseigne',
       'L’évaluation', 'L’enrichissement', 'La préparation préalable']))
check('sous-titres de l’analyse', all(k in src for k in
      ['Premièrement', 'Deuxièmement', 'Troisièmement']))
check('1 tableau (السلوكات)', src.count('<table>') == 1, f'table={src.count("<table>")}')
check('tableau : 1 ligne d’en-tête + 4 rangées', src.count('<tr>') == 5, f'tr={src.count("<tr>")}')
check('tableau : 4 colonnes', src.count('<th>') == 4, f'th={src.count("<th>")}')
check('cellules vides à remplir = 12', src.count('<td></td>') == 12, f'{src.count("<td></td>")}')
check('objectifs = 3 items', src.count('<li>Que je') == 3, f'{src.count("<li>Que je")}')
check('2 hadiths dans la section Le hadith', src.count('[Rapporté par Muslim]') == 1 and 'Hadith <em>ḥasan</em>' in src)
# — typographie série —
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('0 ligature ﷺ (honorifique porté par le français)', '\ufdfa' not in src)
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 double tiret résiduel', '——' not in src)
check('0 U+00A0 littéral', '\u00a0' not in src)
check('0 entité &nbsp;', '&nbsp;' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?|⟦|traduire\)', src))
check('U+202F en vigueur (espaces fines devant ; : ! ? et dans « »)', src.count('\u202f') >= 80,
      f"{src.count('\u202f')} occurrences")
check('0 caractère cyrillique/latin suspect', not re.search(r'[а-яА-Яієґ]', src))
# — données adjudiquées : fragments arabes du tirage (pp.36-40) —
FRAGS = [
    # أهداف (3) — item 2 avec le double «بين» (psm6 1200 ×2)
    'أَنْ أَتَعَرَّفَ مَعْنَى الْبِرِّ وَالْإِثْمِ.',
    'أَنْ أُمَيِّزَ بَيْنَ عَلَامَةِ الْبِرِّ وَبَيْنَ عَلَامَةِ الْإِثْمِ.',
    'أَنْ أَتَمَثَّلَ أَخْلَاقَ الْبِرِّ لِأَتَّصِفَ بِحُسْنِ الْخُلُقِ.',
    # تمهيد — نَقْسِمُ (cmap ن + tesseract ×2), يأتيها, علامتهما (psm7+psm6 1200)
    'نَقْسِمُ الْأَعْمَالَ الَّتِي يَأْتِيهَا الْإِنْسَانُ إِلَى ثَلَاثَةِ أَقْسَامٍ:',
    'قِسْمٌ اتَّضَحَ كَوْنُهُ مِنَ الْبِرِّ،',
    'وَقِسْمٌ يَتَأَرْجَحُ بَيْنَ الْبِرِّ وَالْإِثْمِ؛',
    'عَلَامَةً يُفْصِلُ بِهَا بَيْنَ أَعْمَالِ الْبِرِّ وَأَعْمَالِ الْإِثْمِ.',
    'وَمَا هِيَ عَلَامَتُهُمَا؟',
    # hadith 1 — «عن النبي ﷺ قال» (isnad comprimé du tirage, tesseract ×2)
    'الْبِرُّ حُسْنُ الْخُلُقِ،',
    'وَالْإِثْمُ مَا حَاكَ فِي نَفْسِكَ وَكَرِهْتَ أَنْ يَطْلِعَ عَلَيْهِ النَّاسُ',
    # hadith 2 — shamela 11244/84 VERBATIM (جئت تسأل عن البر؟ / نعم / واطمأن إليه القلب)
    'أَتَيْتُ رَسُولَ اللهِ فَقَالَ: «جِئْتَ تَسْأَلُ عَنِ الْبِرِّ؟»',
    'قُلْتُ: نَعَمْ.',
    'اسْتَفْتِ قَلْبَكَ؛',
    'الْبِرُّ مَا اطْمَأَنَّتْ إِلَيْهِ النَّفْسُ وَاطْمَأَنَّ إِلَيْهِ الْقَلْبُ،',
    'وَالْإِثْمُ مَا حَاكَ فِي النَّفْسِ وَتَرَدَّدَ فِي الصَّدْرِ،',
    'وَإِنْ أَفْتَاكَ النَّاسُ وَأَفْتَوْكَ».',
    # réf. hadith 2 — الدرامي IMPRIMÉ (tesseract ×10 + source shamela ibn Daqīq : والدرامي)
    'حَدِيثٌ حَسَنٌ؛ رَوَيْنَاهُ فِي مُسْنَدَيِ الْإِمَامَيْنِ: أَحْمَدَ بْنِ حَنْبَلٍ وَالدَّرَامِيِّ؛ بِإِسْنَادٍ حَسَنٍ',
    # ترجمة الراوي — النواس
    'ابْنُ سِمْعَانَ بْنِ خَالِدِ بْنِ عَبْدِ اللهِ بْنِ أَبِي بَكْرِ بْنِ رَبِيعَةَ،',
    'مَعْدُودٌ فِي الشَّامِيِّينَ.',
    'تُوُفِّيَ فِي حُدُودِ الْخَمْسِينَ لِلْهِجْرَةِ، وَرَوَى لَهُ مُسْلِمٌ وَالْأَرْبَعَةُ.',
    # ترجمة الراوي — وابصة (أبا شداد : cmap ش-د-ا-د + tesseract ×3 ; سنة تسع)
    'ابْنُ مَعْبَدِ بْنِ مَالِكِ بْنِ عُبَيْدٍ الْأَسَدِيُّ مِنْ بَنِي أَسَدِ بْنِ خُزَيْمَةَ،',
    'يُكْنَى أَبَا شَدَّادٍ.',
    'أَسْلَمَ سَنَةَ تِسْعٍ عِنْدَمَا وَفَدَ عَلَى رَسُولِ اللهِ،',
    'وَلَهُ أَحَادِيثُ.',
    'لَا يَمْلِكُ دُمُوعَهُ إِذَا قَرَأَ الْقُرْآنَ؛',
    'سَكَنَ الْكُوفَةَ ثُمَّ تَحَوَّلَ إِلَى الرَّقَّةِ، وَتُوُفِّيَ بِهَا فِي حُدُودِ السِّتِّينَ مِنَ الْهِجْرَةِ.',
    # الشرح — glose unique («ولم» : psm6/8 ×4, PAS «ولا») ; deuxi-points portés par le français
    '(حَاكَ فِي نَفْسِكَ)',
    'تُخَالِجُ فِي بَاطِنِكَ وَلَمْ تَطْمَئِنَّ إِلَيْهِ.',
    # استخلاص (2 items, cmap)
    'أَسْتَخْرِجُ مِنَ الْحَدِيثِ تَعْرِيفَ الْبِرِّ وَالْإِثْمِ.',
    'أَسْتَخْلِصُ مِنَ الْحَدِيثِ عَلَامَةَ الْبِرِّ وَالْإِثْمِ.',
    # التحليل — intro + أولاً
    'يَتَنَاوَلُ هَذَا الدَّرْسُ بَيَانَ الْبِرِّ وَالْإِثْمِ وَالْعَلَامَةِ الْمُمَيِّزَةَ لِكُلٍّ مِنْهُمَا،',
    'أَوَّلًا: تَعْرِيفُ الْبِرِّ وَبَيَانُ فَضْلِهِ',
    # أولاً — définition (به : tesseract ×2 + cmap ; يلحقه ; عز وجل : cmap ع-ز)
    'الْبِرُّ هُوَ: الْعَمَلُ الَّذِي يَبِرُّ بِهِ فَاعِلُهُ وَيُلْحِقُهُ بِالْأَبْرَارِ وَهُمُ الْمُطِيعُونَ لِلَّهِ عَزَّ وَجَلَّ.',
    'اسْمٌ جَامِعٌ لِلْخَيْرِ وَلِكُلِّ فِعْلٍ مَرْضِيٍّ،',
    # citation الفتوحات — jointure pp.37-38 : تزكية النفس / كالبر بالضم في تغذية البدن / ص 214
    'وَهُوَ فِي تَزْكِيَةِ النَّفْسِ كَالْبُرِّ بِالضَّمِّ فِي تَغْذِيَةِ الْبَدَنِ',
    'الْفُتُوحَاتُ الْوَهْبِيَّةُ',
    'p.\u202f214]',
    # وقال العلماء — لواحقها (cmap ل-و-ا-ح catégorique, tesseract أنواعها REJETÉ)
    'الْبِرُّ يَكُونُ بِمَعْنَى الصِّلَةِ وَبِمَعْنَى الصَّدْقِ،',
    'بِمَعْنَى اللُّطْفِ وَالْمَبَرَّةِ، وَحُسْنِ الْعِشْرَةِ، وَالصُّحْبَةِ، وَلِينِ الْجَانِبِ، وَاحْتِمَالِ الْأَذَى،',
    'وَبِمَعْنَى الطَّاعَةِ بِسَائِرِ لَوَاحِقِهَا،',
    # آية البقرة 177 (imprimée 176, coquille consignée) — fragments clés
    'لَيْسَ الْبِرَّ أَنْ تُوَلُّوا وُجُوهَكُمْ قَبْلَ الْمَشْرِقِ وَالْمَغْرِبِ',
    'وَلَٰكِنَّ الْبِرَّ مَنْ آمَنَ بِاللهِ وَالْيَوْمِ الْآخِرِ وَالْمَلَائِكَةِ وَالْكِتَابِ وَالنَّبِيِّينَ،',
    'وَآتَى الْمَالَ عَلَىٰ حُبِّهِ ذَوِي الْقُرْبَىٰ وَالْيَتَامَىٰ وَالْمَسَاكِينَ وَابْنَ السَّبِيلِ وَالسَّائِلِينَ وَفِي الرِّقَابِ،',
    'وَالْمُوفُونَ بِعَهْدِهِمْ إِذَا عَاهَدُوا وَالصَّابِرِينَ فِي الْبَأْسَاءِ وَالضَّرَّاءِ وَحِينَ الْبَأْسِ،',
    'أُولَٰئِكَ الَّذِينَ صَدَقُوا وَأُولَٰئِكَ هُمُ الْمُتَّقُونَ',
    '176',  # référence imprimée
    'le tirage imprime «\u202f176\u202f», coquille consignée',  # note de coquille
    # فمجامع (alif : cmap + psm4/psm6)
    'فَمَجَامِعُ حُسْنِ الْخُلُقِ هِيَ الْبِرُّ.',
    # الحج عرفة — باب 57 (tesseract ×3) / رقم 889 (tesseract ×3 + cmap 8-8-9)
    '«الْحَجُّ عَرَفَةٌ»',
    'chapitre 57, hadith numéro 889',
    # المراد بحسن الخلق — المحاولة (tesseract ×3 + dr-alaskar) / البذل (psm4 + dr-alaskar)
    'الْإِنْصَافُ فِي الْمُعَامَلَةِ، وَالرِّفْقُ فِي الْمُحَاوَلَةِ،',
    'وَالْعَدْلُ فِي الْأَحْكَامِ، وَالْبَذْلُ فِي الْإِحْسَانِ،',
    # آية الأنفال 2-4
    'إِنَّمَا الْمُؤْمِنُونَ الَّذِينَ إِذَا ذُكِرَ اللهُ وَجِلَتْ قُلُوبُهُمْ',
    'وَإِذَا تُلِيَتْ عَلَيْهِمْ آيَاتُهُ زَادَتْهُمْ إِيمَانًا وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ،',
    'الَّذِينَ يُقِيمُونَ الصَّلَاةَ وَمِمَّا رَزَقْنَاهُمْ يُنْفِقُونَ،',
    'لَهُمْ دَرَجَاتٌ عِنْدَ رَبِّهِمْ وَمَغْفِرَةٌ وَرِزْقٌ كَرِيمٌ',
    'al-’Anfāl',
    # ثانياً — تعريف الإثم (cmap subtitle)
    'ثَانِيًا: تَعْرِيفُ الْإِثْمِ',
    '«وَالْإِثْمُ مَا حَاكَ فِي نَفْسِكَ وَكَرِهْتَ أَنْ يَطْلِعَ عَلَيْهِ النَّاسُ».',
    # نفرة (dr-alaskar + p.39 نفسها ; tesseract ذفرة ×4 REJETÉ par recoupement source)
    'يُورِثُ نَفْرَةً فِي الْقَلْبِ،',
    'فَالْبِرُّ: كَلِمَةٌ جَامِعَةٌ لِجَمِيعِ أَفْعَالِ الْخَيْرِ وَخِصَالِ الْمَعْرُوفِ،',
    'كَلِمَةٌ جَامِعَةٌ لِجَمِيعِ أَفْعَالِ الشَّرِّ وَالْقَبَائِحِ كَبِيرِهَا وَصَغِيرِهَا.',
    # قابل بينهما هو (cmap : ه-و après بينهما ; PAS de mot dans l'intervalle — f6 zoom vide)
    'وَلِهَذَا السَّبَبِ قَابَلَ بَيْنَهُمَا هُوَ، وَجَعَلَهُمَا ضِدَّيْنِ.',
    # ثالثاً (sous-titre couleur, extraction couche bleue)
    'ثَالِثًا: عَلَامَةُ الْبِرِّ وَالْإِثْمِ',
    'نَفْرَةَ الْقَلْبِ، وَكَرَاهَةَ الِاطِّلَاعِ.',
    'طُمَأْنِينَةُ النَّفْسِ،',
    '«الْبِرُّ مَا اطْمَأَنَّتْ إِلَيْهِ النَّفْسُ».',
    # وليس معنى الحديث — فتوى (psm7+psm6 1200, PAS فتاوى)
    'عَلَى فَتْوَى النُّفُوسِ،',
    'بَلْ لَا بُدَّ فِيهَا مِنْ سُؤَالِ أَهْلِ الْعِلْمِ وَالْأَخْذِ بِمَا يَقُولُونَ.',
    'وَأَمَّا اسْتِفْتَاءُ الْقَلْبِ فَمَعْنَاهُ:',
    'مِنَ الْمَسَائِلِ الْمُشْتَبِهَةِ،',
    'وَأُخْبِرَ بِأَنَّهَا حَلَالٌ،',
    'فَلَمْ تَطْمَئِنُّ نَفْسُهُ وَبَقِيَ مُتَرَدِّدًا فِيهَا،',
    'غَيْرُ مُطْمَئِنٍّ إِلَيْهِ، اسْتِبْرَاءً لِدِينِهِ.',
    # hadiths de soutien + références
    '«فَمَنِ اتَّقَى الشُّبُهَاتِ فَقَدِ اسْتَبْرَأَ لِدِينِهِ وَعِرْضِهِ».',
    'كِتَابُ الْمُسَاقَاةِ' if 'كِتَابُ الْمُسَاقَاةِ' in src else 'livre des baux ruraux',
    '«دَعْ مَا يَرِيبُكَ إِلَى مَا لَا يَرِيبُكَ».',
    'Rapporté par at-Tirmiḏī et an-Nasāʾī',
    # مما يستفاد — إصلاح (ص : lexical + précédent L4 ; tesseract ض ×5 REJETÉ, flag worklog)
    'أَهَمِّيَّةُ إِصْلَاحِ الْقَلْبِ بِأَنْوَاعِ الْبِرِّ لِإِصْلَاحِ حَرَكَاتِ الْجَوَارِحِ،',
    'وَالتَّرْغِيبُ فِي حُسْنِ الْخُلُقِ.',
    'الْمُؤْمِنُ لَا يُقَدِّمُ عَلَى شَيْءٍ لَا تَطْمَئِنُّ نَفْسُهُ إِلَيْهِ.',
    'إِخْبَارُهُ وَابِصَةَ عَمَّا فِي نَفْسِهِ مُعْجِزَةٌ مِنَ الْمُعْجِزَاتِ.',
    # التقويم (3 items — numérotation saine 1-2-3, PAS de coquille)
    'أُعَرِّفُ الْبِرَّ وَأُبَيِّنُ أَهَمِّيَتَهُ فِي تَزْكِيَةِ النَّفْسِ.',
    'مَتَّى يُعْتَمَدُ عَلَى طُمَأْنِينَةِ الْقَلْبِ فِي تَحْدِيدِ الْبِرِّ؟',
    'أَمْلَأُ الْجَدْوَلَ الْآتِيَ بِمَا يُنَاسِبُ:',
    # tableau — en-têtes (extraction couche bleue sur jaune : ما يدخل ×2 + التعليل)
    'السُّلُوكَاتُ وَالتَّصَرُّفَاتُ',
    'مَا يَدْخُلُ فِي الْبِرِّ',
    'مَا يَدْخُلُ فِي الْإِثْمِ',
    'التَّعْلِيلُ',
    # tableau — 4 rangées (psm6/psm7 1200)
    'الْمُشَارَكَةُ فِي الْأَنْشِطَةِ الْمَدْرَسِيَّةِ لِلتَّوْعِيَةِ بِأَهَمِّيَّةِ الْحِفَاظِ عَلَى الْبِيئَةِ',
    'إِكْرَامُ النَّاسِ وَحُسْنُ الظَّنِّ بِهِمْ',
    'الْمُسَاعَدَةُ عَلَى الْغِشِّ فِي الِامْتِحَانِ',
    'مُسَاعَدَةُ الْمَكْفُوفِ وَالْيَتِيمِ',
    # الاستثمار — آية الفرقان 63 + ref 63-77 + إلى آخر السورة
    'فِي عِدَّةِ آيَاتٍ، مِنْهَا قَوْلُهُ تَعَالَى:',
    '«وَعِبَادُ الرَّحْمَنِ الَّذِينَ يَمْشُونَ عَلَى الْأَرْضِ هَوْنًا»',
    'al-Furqān',
    '63-77',
    'إِلَى آخِرِ السُّورَةِ.',
    # activités 1-3 (الضبط avec ḍād : psm6/psm7 1200 ×2)
    'أَكْتُبُ الْآيَاتِ فِي دَفْتَرِي كَامِلَةً وَفْقَ قَوَاعِدِ الرَّسْمِ وَالضَّبْطِ وَالْوَقْفِ.',
    'أُصَنِّفُ فِي خُطَّاطَةِ صِفَاتِ الْمُؤْمِنِينَ الْوَارِدَةِ فِي هَذِهِ الْآيَاتِ.',
    'أَخْتَارُ مِنَ الْآيَاتِ صِفَتَيْنِ وَأُبَيِّنُ كَيْفَ أُطَبِّقُهُمَا فِي مُحِيطِي.',
    # الإعداد القبلي — الموالى (alif maqṣūra : psm7/8 ×5 + L4 précédent)
    'أَحْفَظُ حَدِيثَ الدَّرْسِ الْمُوَالَى وَأُنْجِزُ مَا يَأْتِي:',
    'أَشْرَحُ الْمُفْرَدَاتِ الْآتِيَةَ: وَجَلَتْ - ذَرَفَتْ.',
    'أَبْحَثُ عَنْ فَوَائِدِ السَّمْعِ وَالطَّاعَةِ لِوَلِيِّ الْأَمْرِ.',
]
for f in FRAGS:
    check(f'fragment « {f[:44]}… »' if len(f) > 44 else f'fragment « {f} »', f in src)
# — motifs d'ABSENCE (lectures rejetées) —
ABSENTS = [
    ('ذَفْرَة (rejet : dr-alaskar + p.39 نفرة)', 'ذَفْرَة'),
    ('زَفْرَة (rejet)', 'زَفْرَة'),
    ('الْمُحَاوَرَة (rejet : tesseract ×3 + source = المحاولة)', 'الْمُحَاوَرَة'),
    ('الْبَدْلُ فِي الْإِحْسَانِ (rejet : البذل, dr-alaskar)', 'الْبَدْلُ فِي'),
    ('إِضْلَاح (rejet : lexical إصلاح + L4 précédent)', 'إِضْلَاح'),
    ('أَنْوَاعِهَا (rejet : cmap ل-و-ا-ح = لواحقها)', 'أَنْوَاعِهَا'),
    ('الدَّارِمِي (rejet : imprime الدرامي, source idem)', 'الدَّارِمِي'),
    ('فَتَاوَى (rejet : فتوى imprimé)', 'فَتَاوَى'),
    ('وَلَمْ تَطْمَئِن', None),  # présent — contrôle inversé ci-dessous
]
for name, pat in ABSENTS:
    if pat is not None:
        check(f'absence {name}', pat not in src)
check('présence وَلَمْ تَطْمَئِنَّ (glose, ×4 lectures)', 'وَلَمْ تَطْمَئِنَّ إِلَيْهِ' in src)
check('absence وَلَا تَطْمَئِن (variant rejeté)', 'وَلَا تَطْمَئِن' not in src)
check('absence عَلَامَاتُهُمَا (variant rejeté : psm7+psm6 = علامتهما)', 'عَلَامَاتُهُمَا' not in src)
check('absence مَوْقِفِي مِنْهَا (en-tête de L4, absent ici)', 'مَوْقِفِي مِنْهَا' not in src)
check('absence سُؤَال الْحُكْم (rejet : طمأنينة القلب, psm7 1200)', 'حُكْمِ الْقَلْبِ' not in src)
# — métadonnées JSON —
check('titleFr conforme (catalogue, apostrophe droite des titres)', l['titleFr'] == "La bonté pieuse, c'est la beauté du caractère", l['titleFr'])
check('titleAr conforme', l['titleAr'] == 'البر حسن الخلق', l['titleAr'])
check('docId', l['docId'] == 'pdf-mut23h3b-685')

print(f"OK {len(ok)} / ÉCHECS {len(fail)}")
for f in fail:
    print('  ÉCHEC:', f)
sys.exit(1 if fail else 0)
