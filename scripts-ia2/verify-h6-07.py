#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — vérification de la livraison hadith-6ep / pdf-mut23h3b-686
# (لزوم السنة — hadith al-ʿIrbāḍ b. Sāriya, Abū Dāwūd + Tirmiḏī ḥasan ṣaḥīḥ / Nawawī 28).
# Leçon 6 du tirage : pp.41-45 du manuel. Données adjudiquées Z2-41 :
# textlayer 39-49 + bbox word-level (cmap glyphes + coordonnées pp.41-48) + tesseract ara
# 600 dpi psm 4/6 (pp.41-46) + strips 1200 dpi multi-psm (autocontrast, binarisation otsu,
# extraction colorée) + ultra-zooms 1200×2 / 1800 dpi + anatomie pixel des points
# diacritiques (أثر : 3 points = ث ; غضب : 2 points au-dessus ; digits des refs) +
# recoupements shamela 11244/86-87-88 (شرح ابن دقيق العيد, hadith 28 verbatim),
# islamweb 29/1760 + askimam (البحر الرائق ج3, citation verbatim), teacher's site
# ibnarabi02 (leçon entière : حديث + ترجمة + شرح + تحليل headings + مما يستفاد ×5).
# VLM INDISPONIBLE ce tour (quota 429 dès le test initial).
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-6ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-6ep/pdf-mut23h3b-686.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-mut23h3b-686']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-mut23h3b-686 unique', len(les) == 1, f'{len(les)} occurrences')
check('titre h1 présent', src.startswith('<h1>L’attachement à la Sunna</h1>'))
check('sections h2 = 10', src.count('<h2>') == 10, f'h2={src.count("<h2>")}')
check('sections h3 = 4 (extraction + أولاً + ثانياً + ثالثاً)', src.count('<h3>') == 4, f'h3={src.count("<h3>")}')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Introduction', 'Le hadith', 'Notice du transmetteur',
       'L’explication', 'Extraction des idées', 'L’analyse', 'Ce que le hadith enseigne',
       'L’évaluation', 'L’enrichissement', 'La préparation préalable']))
check('sous-titres de l’analyse', all(k in src for k in
      ['Premièrement', 'Deuxièmement', 'Troisièmement']))
check('objectifs = 3 items', src.count('<li>Que je') == 3, f'{src.count("<li>Que je")}')
check('référence du hadith', 'Rapporté par <em>Abū Dāwūd</em> et <em>at-Tirmiḏī</em>' in src
      and 'hadith <em>ḥasan ṣaḥīḥ</em>' in src)
check('aucun tableau (leçon sans tableau)', src.count('<table>') == 0)
check('titre translittéré', '<em>luzūmu s-sunna</em>' in src)
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
check('U+202F en vigueur', src.count('\u202f') >= 90, f"{src.count('\u202f')} occurrences")
check('0 caractère cyrillique/latin suspect', not re.search(r'[а-яА-Яієґ]', src))
# — données adjudiquées : fragments arabes du tirage (pp.41-45) —
FRAGS = [
    # أهداف (3) — item 2 «فوائد» (psm6+psm8 + parallèle تقويم item 1 ; psm7 isolé «قوائد» rejeté)
    'أَنْ أَتَعَرَّفَ حُكْمَ اتِّبَاعِ السُّنَّةِ وَالْتِزَامَ بِهَا.',
    'أَنْ أُدْرِكَ فَوَائِدَ التَّمَسُّكِ بِالسُّنَّةِ وَطَاعَةِ وَلِيِّ الْأَمْرِ.',
    'أَنْ أَحْرِصَ عَلَى اتِّبَاعِ السُّنَّةِ وَطَاعَةِ وَلِيِّ الْأَمْرِ.',
    # تمهيد — «من مظاهر رحمة النبي محمد ﷺ» (psm13 ×3), إيصال الخير (psm6 ×2), يوجههم/يضمن
    'مِنْ مَظَاهِرِ رَحْمَةِ النَّبِيِّ مُحَمَّدٍ وَحَرْصِهِ عَلَى إِيصَالِ الْخَيْرِ لِجَمِيعِ النَّاسِ،',
    'يُوَجِّهُهُمْ إِلَى مَا يُقَوِّي صِلَتَهُمْ بِاللهِ وَيَضْمِنُ لَهُمْ صَلَاحَ أَمُورِ دِينِهِمْ وَدُنْيَاهُمْ؛',
    'فَكَانَ مِنْ وَصَايَاهُ عَلَيْهِ الصَّلَاةُ وَالسَّلَامُ: التَّمَسُّكُ بِتَقْوَى اللهِ',
    'وَمَا قَوَاعِدُ السَّمْعِ وَالطَّاعَةِ لِوَلِيِّ الْأَمْرِ؟',
    # hadith — shamela 11244/86 VERBATIM (وإن تأمر عليكم عبد — PAS de «حبشي» ; فسيرى)
    'وَعَظَنَا رَسُولُ اللهِ مَوْعِظَةً وَجِلَتْ مِنْهَا الْقُلُوبُ وَذَرَفَتْ مِنْهَا الْعُيُونُ،',
    'يَا رَسُولَ اللهِ كَأَنَّهَا مَوْعِظَةُ مُوَدِّعٍ فَأَوْصِنَا.',
    'وَإِنْ تَأَمَّرَ عَلَيْكُمْ عَبْدٌ،',
    'فَإِنَّهُ مَنْ يَعِشْ مِنْكُمْ فَسَيَرَى اخْتِلَافًا كَثِيرًا،',
    'عَضُّوا عَلَيْهَا بِالنَّوَاجِذِ،',
    'وَكُلُّ بِدْعَةٍ ضَلَالَةٌ',
    # ترجمة الراوي — التوبة 92 (imprimé 93, coquille), السلمي/أبو نجيح/الصفة (psm4+psm6+site)
    'الْعِرْبَاضُ بْنُ سَارِيَةَ السُّلَمِيُّ أَبُو نَجِيحٍ، أَحَدُ أَصْحَابِ الصُّفَّةِ،',
    'وَمِمَّنْ نَزَلَ فِيهِمْ قَوْلُهُ تَعَالَى:',
    'وَأَعْيُنُهُمْ تَفِيضُ مِنَ الدَّمْعِ حَزَنًا أَلَّا يَجِدُوا مَا يُنْفِقُونَ',
    'تُوُفِّيَ سَنَةَ 75 لِلْهِجْرَةِ.',
    # الشرح — 2 gloses (وجلت: خافت ×4 lectures ; النواجذ: مؤخر الأضراس ×3)
    'خَافَتْ.',
    'مُؤَخَّرُ الْأَضْرَاسِ.',
    # استخلاص (2)
    'أَسْتَخْرِجُ مِنَ الْحَدِيثِ أَثَرَ الْمَوْعِظَةِ عَلَى الصَّحَابَةِ.',
    'تُؤَكِّدُ الِاتِّبَاعَ وَتُحَذِّرُ مِنَ الِابْتِدَاعِ.',
    # تحليل — intro + أولاً (أنatomie : 3 points = ث, + site «أثر الموعظة») + corps
    'يَشْتَمِلُ هَذَا الدَّرْسُ عَلَى مَا يَأْتِي:',
    'أَوَّلًا: أَثَرُ الْمَوْعِظَةِ عَلَى الصَّحَابَةِ رِضْوَانُ اللهِ عَلَيْهِمْ',
    'بِوَجَلِ الْقُلُوبِ عِنْدَ ذِكْرِ اللهِ تَعَالَى وَذَرْفِ الدُّمُوعِ مِنْ مَخَافَتِهِ،',
    'إِنَّمَا الْمُؤْمِنُونَ الَّذِينَ إِذَا ذُكِرَ اللهُ وَجِلَتْ قُلُوبُهُمْ',
    'يَصْفُو قَلْبُهُ وَيَقْشَعِرُّ جِلْدُهُ وَيَلِينُ لِذِكْرِ اللهِ تَعَالَى.',
    'وَقَدْ أَلْقَى إِلَيْهِمْ بِمَوْعِظَةٍ بَلِيغَةٍ',
    'بِمَا لِلْوَصِيَّةِ مِنْ أَثَرٍ فِي النُّفُوسِ،',
    'فَأَوْصَاهُمْ وَصِيَّةَ مُشْفِقٍ رَؤُوفٍ رَحِيمٍ.',
    # ثانياً — heading (site + psm7 ×8) + تعريف التقوى (غضب : 2 points au-dessus, ×3 lectures)
    'ثَانِيًا: الْأَمْرُ بِتَقْوَى اللهِ وَالسَّمْعِ وَالطَّاعَةِ',
    'تَضَمَّنَتْ وَصِيَّتُهُ أَمْرَيْنِ: التَّقْوَى، وَالسَّمْعَ وَالطَّاعَةَ.',
    'بَيْنَهُ وَبَيْنَ غَضَبِ اللهِ وِقَايَةً تَقِيهِ مِنْهُ،',
    'هِيَ سَبَبُ كُلِّ خَيْرٍ وَفَلَاحٍ وَسَعَادَةٍ فِي الدُّنْيَا وَالْآخِرَةِ،',
    'وَمَنْ يَتَّقِ اللهَ يَجْعَلْ لَهُ مَخْرَجًا',
    'وَمَنْ يَتَّقِ اللهَ يَجْعَلْ لَهُ مِنْ أَمْرِهِ يُسْرًا',
    'مَنْهَجُ الْإِسْلَامِ فِي حِفْظِ نِظَامِ الْأُمَّةِ،',
    'فَإِنْ تَنَازَعْتُمْ فِي شَيْءٍ فَرُدُّوهُ إِلَى اللهِ وَالرَّسُولِ',
    'حَتَّى لَوْ حَكَمَ رَسُولُ اللهِ فِي ذَوَاتِ أَنْفُسِهِمْ؛',
    'إِنَّمَا كَانَ قَوْلُ الْمُؤْمِنِينَ إِذَا دُعُوا إِلَى اللهِ وَرَسُولِهِ',
    'وَيُسَلِّمُوا تَسْلِيمًا',
    # ثالثاً — heading + آل عمران 103 (cmap digits 1-0-3 + psm7 «103»)
    'ثَالِثًا: التَّمَسُّكُ بِسُنَّةِ الرَّسُولِ وَخُلَفَائِهِ الرَّاشِدِينَ',
    'وَأَرْشَدَهَا إِلَى التِّزَامِ سُنَّتِهِ وَسُنَّةِ الْخُلَفَاءِ الرَّاشِدِينَ:',
    'مِنَ الِاعْتِقَادَاتِ وَالْأَقْوَالِ وَالْأَعْمَالِ يَعْصِمُ النَّاسَ',
    'غَرْسِ قِيَمِ الْوَحْدَةِ وَالتَّآلُفِ وَالتَّآزُرِ بَيْنَ أَفْرَادِ الْمُجْتَمَعِ،',
    'وَاعْتَصِمُوا بِحَبْلِ اللهِ جَمِيعًا وَلَا تَفَرَّقُوا',
    'إِذْ كُنْتُمْ أَعْدَاءً فَأَلَّفَ بَيْنَ قُلُوبِكُمْ',
    # وفي قوله — البدعة (site verbatim : «فلا يدخل في البدعة»)
    'نَهْيٌ عَنِ ابْتِدَاعِ شَيْءٍ يُزَادُ عَلَى السُّنَّةِ أَوْ يُسْتَبْدَلُ مَكَانَهَا،',
    'وَالْبِدْعَةُ: إِيجَادُ شَيْءٍ لَيْسَ لَهُ أَصْلٌ فِي الشَّرْعِ.',
    'أَمَّا مَا اقْتَضَتْهُ الْمَصَالِحُ وَالْمَقَاصِدُ الْعَامَّةُ لِلشَّرْعِ فَلَا يَدْخُلُ فِي الْبِدْعَةِ.',
    # مما يستفاد (5) — site verbatim
    'أَهَمِّيَّةُ الْمَوْعِظَةِ الصَّادِقَةِ فِي تَرْقِيقِ الْقُلُوبِ وَقَبُولِ الْحَقِّ.',
    'حِرْصُ الصَّحَابَةِ رَضِيَ اللهُ عَنْهُمْ عَلَى الِاسْتِزَادَةِ مِنَ الْخَيْرِ.',
    'وُجُوبُ التَّقْوَى وَالسَّمْعِ وَالطَّاعَةِ لِوُلَاةِ الْأُمُورِ.',
    'وَالتَّحْذِيرُ مِنِ ابْتِدَاعِ شَيْءٍ لَيْسَ لَهُ أَصْلٌ فِي الشَّرْعِ.',
    'شَرَفُ الْخُلَفَاءِ الرَّاشِدِينَ وَفَضْلُهُمْ وَالْأَمْرُ بِاتِّبَاعِ سُنَّتِهِمْ.',
    # التقويم (3) — items cmap-aveugles lus psm7/psm6 1200
    'أُبَيِّنُ فَوَائِدَ التَّمَسُّكِ بِالسُّنَّةِ وَطَاعَةِ وَلِيِّ الْأَمْرِ.',
    'أُوَضِّحُ بِأَمْثِلَةٍ مِنَ الْوَاقِعِ أَثَرَ السَّمْعِ فِي اسْتِقْرَارِ الْمُجْتَمَعِ.',
    'أَكْتُبُ فَقْرَةً أُضَمِّنُهَا آثَارَ التَّقْوَى عَلَى الْفَرْدِ وَالْمُجْتَمَعِ.',
    # الاستثمار — البحر الرائق ج3 ص258 (islamweb/askimam verbatim)
    'كَالرَّفْعَةِ مِنَ الِارْتِفَاعِ؛',
    'عَلَى مَا هُوَ نَقْصٌ فِي الدِّينِ أَوْ زِيَادَةٌ،',
    'لَكِنْ قَدْ يَكُونُ بَعْضُهَا غَيْرَ مَكْرُوهٍ،',
    'مَا شَهِدَ لِجِنْسِهِ أَصْلٌ فِي الشَّرْعِ،',
    'تُدْفَعُ بِهَا مَفْسَدَةٌ.',
    'أَتَأَمَّلُ النَّصَّ وَأَسْتَخْلِصُ مِنْهُ مَا يَأْتِي:',
    'تَعْرِيفًا لِلْبِدْعَةِ فِي الدِّينِ.',
    'تَعْرِيفًا لِلْبِدْعَةِ الْمُبَاحَةِ.',
    # الإعداد القبلي — عرض «عناية الإسلام بجمال البيئة» (687 leçon suivante : présentation du même عرض)
    'أُرَاجِعُ دُرُوسِي وَأَسْتَعِدُّ لِحِصَّةِ الدَّعْمِ وَالتَّطْبِيقِ:',
    'عَرْضًا بِعُنْوَانِ «عِنَايَةِ الْإِسْلَامِ بِجَمَالِ الْبِيئَةِ»',
    'تَحْدِيدِ مَحَاوِرِ الْعَرْضِ.',
    'زِيَارَةِ مَكْتَبَةِ الْمُؤَسَّسَةِ وَالْمَكْتَبَاتِ الْمَحَلِّيَّةِ لِجَمْعِ الْمَعْلُومَاتِ.',
    'التَّعَاوُنِ مَعَ الْأَصْدِقَاءِ عَلَى كِتَابَةِ الْمَحْوَرِ الَّذِي كُلِّفْنَا بِإِعْدَادِهِ.',
]
for f in FRAGS:
    check(f'frag: {f[:38]}…' if len(f) > 38 else f'frag: {f}', f in src)
# — coquilles consignées (4 refs décalées, cf. L5 [البقرة: 176] pour 177) —
check('coquille consignée [التوبة: 93→92]', 'le tirage imprime «\u202f93\u202f»' in src)
check('coquille consignée [النساء: 58→59]', 'le tirage imprime «\u202f58\u202f»' in src)
check('coquille consignée [النور: 49→51]', 'le tirage imprime «\u202f49\u202f»' in src)
check('coquille consignée [النساء: 64→65]', 'le tirage imprime «\u202f64\u202f»' in src)
# — absences : lectures rejetées —
ABSENT = [
    'حَبَشِيّ',        # PAS dans le tirage (shamela 11244/86 non plus)
    'قَوَاعِدَ التَّمَسُّكِ',  # أهداف item 2 : psm7 isolé rejeté (فوائد ×3 + parallèle تقويم)
    'يُرَادُ عَلَى',    # بدعة : psm8 isolé rejeté (يزاد psm7 + «أو زيادة» de la citation)
    'مُعَايَرَةَ',      # مغايرة retenue (ghayn, cf. خافت/حافت ; 3 outils lisent ع)
    'وَطَلَاعَة',       # coquille L4-style absente : سمع والطاعة sains
    'الطُّهُورَ',       # 687, pas cette leçon
    'خَافَتٌ',          # vocalisation fautive
    'صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ',  # formule développée interdite (série : 0 ﷺ)
]
for a in ABSENT:
    check(f'absence: {a}', a not in src)
# — volume —
check('volume cohérent (leçon 5 pp., 28-38k car)', 28000 <= len(src) <= 38000, f'{len(src)} car')
# — sortie —
print(f"OK   {len(ok)}")
print(f"FAIL {len(fail)}")
for f in fail:
    print('  ✗', f)
sys.exit(1 if fail else 0)
