#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-32 — vérification de la livraison hadith-5ep / pdf-27 (Ce qui fait entrer au Paradis)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-27.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-27']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-27 unique', len(les) == 1, f'{len(les)} occurrences')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon pp.150-155, 6 pages, 3 sections d’analyse', 18000 <= len(src) <= 36000, f'{len(src)} car')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 10, f'h2={src.count("<h2>")}')
check('sous-sections h3 (أولاً/ثانياً/ثالثاً', src.count('<h3>') == 3, f'h3={src.count("<h3>")}')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Mise en condition', 'Le hadith', 'Le transmetteur',
       'La compréhension', 'L’analyse', 'Ce que le hadith nous apprend',
       'L’évaluation', 'L’exploitation', 'La préparation de la leçon suivante']))
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 demi-anneau (U+02BF/02BE/02BC/02BB', not any(c in src for c in '\u02bf\u02be\u02bc\u02bb'))
check('0 point-virgule vertical (U+FE14', '\ufe14' not in src)
check('0 double tiret résiduel', '——' not in src)
check('0 double entité &nbsp;', '&nbsp;&nbsp;' not in src)
check('0 U+00A0 littéral', '\u00a0' not in src)
check('0 ligature ﷺ (honorifique porté par le français, convention série', '\ufdfa' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?|⟦', src))
# — correspondance FICHIER ↔ JSON —
check('htmlFr posé identique au fichier', fr == src, f'{len(fr)} vs {len(src)} car')
check('titleFr conservé', l.get('titleFr') == 'Ce qui fait entrer au Paradis', f"({l.get('titleFr')})")
check('titleAr conservé', l.get('titleAr') == 'مما يدخل الجنة', f"({l.get('titleAr')})")
# — matière adjudiquée du manuel (Z2-32, pp.150-155 : textlayer + bbox word-level
#   + 6 VLM pleine page 150 dpi + 12 bandes VLM 1200 dpi + scrutins ciblés
#   + tesseract ara 600/1200 dpi psm 4/6 ; chaque point tranché à 2-3 témoins —
for kw in ['<h1>Ce qui fait entrer au Paradis</h1>',
           'أَنْ أَتَعَرَّفَ حُكْمَ الِاكْتِفَاءِ بِالْفَرَائِضِ وَفَضْلَ التَّطَوُّعَاتِ',
           'أَنْ أُمَيِّزَ مَرْتَبَتَيْ الِاكْتِفَاءِ بِالْفَرَائِضِ وَالِاسْتِزَادَةِ مِنَ التَّطَوُّعَاتِ',
           'أَنْ أَحْرِصَ عَلَى أَدَاءِ الْفَرَائِضِ وَالِاسْتِزَادَةِ مِنَ التَّطَوُّعَاتِ',
           'وَاجِبٌ أَسَاسٌ عَلَى الْمُكَلَّفِينَ',
           'اسْتِزَادَةٌ وَكَمَالٌ نَدَبَ إِلَيْهِمَا الشَّرْعُ',
           'لِاسْتِحْقَاقِ دُخُولِ الْجَنَّةِ؟',
           'مَرْتَبَةُ كُلٍّ مِنَ الِاكْتِفَاءِ',
           'عَنْ أَبِي عَبْدِ اللهِ جَابِرِ بْنِ عَبْدِ اللهِ الْأَنْصَارِيِّ رَضِيَ اللهُ عَنْهُمَا',
           'أَنَّ رَجُلًا سَأَلَ رَسُولَ اللهِ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ فَقَالَ',
           'أَرَأَيْتَ إِذَا صَلَّيْتُ الْمَكْتُوبَاتِ، وَصُمْتُ رَمَضَانَ',
           'وَلَمْ أَزِدْ عَلَى ذَلِكَ شَيْئًا، أَدْخُلُ الْجَنَّةَ؟ قَالَ: «نَعَمْ»',
           'جَابِرُ بْنُ عَبْدِ اللهِ بْنِ عَمْرِو بْنِ حِرَامٍ الْأَنْصَارِيُّ الْخَزْرَجِيُّ السُّلَمِيُّ',
           'شَهِدَ الْعَقَبَةَ الثَّانِيَةَ مَعَ أَبِيهِ صَغِيرًا',
           'أَلْفٌ وَخَمْسُمِائَةِ حَدِيثٍ وَأَرْبَعُونَ حَدِيثًا',
           'سَنَةَ ثَلَاثٍ وَسَبْعِينَ لِلْهِجْرَةِ عَنْ أَرْبَعٍ وَتِسْعِينَ سَنَةً',
           'أَخْبِرْنِي؛ أَوْ: مِنَ الرَّأْيِ، بِمَعْنَى: أَتَرَى وَتُفْتِي',
           'النَّعْمَانُ بْنُ قَوْقَلٍ بِفَتْحِ الْقَافَيْنِ',
           'أَدَاءَ الْمَكْتُوبَاتِ الْخَمْسِ، وَصِيَامَ رَمَضَانَ',
           'لِعَدَمِ فَرْضِهِمَا بَعْدُ، أَوْ لِأَنَّ السَّائِلَ لَمْ يُخَاطَبْ بِهِمَا',
           'نَتَنَاوَلُ مَحَاوِرَهُ عَلَى مَا يَأْتِي',
           'أَوَّلًا: مَعْنَى «أَحْلَلْتُ الْحَلَالَ وَحَرَّمْتُ الْحَرَامَ»',
           'حَرَّمْتُ الْحَرَامَ بِـ«اجْتَنَبْتُهُ»',
           '«فَعَلْتُهُ مُعْتَقِدًا حِلَّهُ»',
           'وَقَالَ ابْنُ الصَّلَاحِ',
           'أَمْرَيْنِ أَحَدُهُمَا',
           'مُجَرَّدُ اعْتِقَادِهِ حَلَالًا',
           'ثَانِيًا: حُكْمُ الِاكْتِفَاءِ بِالْفَرَائِضِ',
           'كَافٍ لِدُخُولِ الْجَنَّةِ بِرَحْمَةِ اللهِ تَعَالَى وَفَضْلِهِ',
           'لِلسَّائِلِ: أَأَدْخُلُ الْجَنَّةَ؟',
           'حَدِيثِ طَلْحَةَ بْنِ عُبَيْدِ اللهِ',
           'مِنْ أَهْلِ نَجْدٍ، ثَائِرُ الرَّأْسِ',
           'يُسْمَعُ دَوِيُّ صَوْتِهِ وَلَا يُفْقَهُ مَا يَقُولُ',
           'خَمْسُ صَلَوَاتٍ فِي الْيَوْمِ وَاللَّيْلَةِ',
           'لَا إِلَّا أَنْ تَطَوَّعَ',
           'وَصِيَامُ شَهْرِ رَمَضَانَ',
           'وَاللهِ لَا أَزِيدُ عَلَى هَذَا وَلَا أَنْقُصُ مِنْهُ',
           'أَفْلَحَ الرَّجُلُ إِنْ صَدَقَ [الموطأ]',
           'فَلَاحِ مَنِ اكْتَفَى بِالْفَرَائِضِ',
           'وَأَفَادَ صَاحِبُ الْمَفْهُومِ',
           'جَوَازِ تَرْكِ التَّطَوُّعَاتِ',
           'ثَالِثًا: فَضْلُ الِاسْتِزَادَةِ مِنَ التَّطَوُّعَاتِ',
           'نَاجِيًا مُفْلِحًا',
           'وَأَتْبَعَهَا النَّوَافِلَ كَانَ أَفْضَلَ مَرْتَبَةً وَفَلَاحًا',
           'يُثَابِرُونَ عَلَى فِعْلِ السُّنَنِ وَالْفَضَائِلِ مُثَابَرَتِهِمْ عَلَى الْفَرَائِضِ',
           'فِي اغْتِنَامِ ثَوَابِهَا، وَتَتْمِيمِ الْفَرَائِضِ بِهَا',
           'تَنْبِيهَ السَّائِلِ عَلَى السُّنَنِ وَالْفَضَائِلِ تَيْسِيرًا وَحَذَرًا مِنَ التَّنْفِيرِ',
           'لِقُرْبِ عَهْدِهِ بِالْإِسْلَامِ',
           'رَغِبَ فِيمَا رَغِبَ فِيهِ غَيْرُهُ',
           'أَوْ لِأَلَّا يَعْتَقِدَ وُجُوبَ السُّنَنِ وَالتَّطَوُّعَاتِ',
           'فَلَاحٌ أَيْ فَلَاحٌ',
           'يُتَقَرَّبُ بِهَا لِمَحَبَّتِهِ سُبْحَانَهُ',
           'وَجَبْرٌ لِمَا يَقَعُ مِنْ نَقْصٍ فِي الْفَرَائِضِ',
           'بِخُلُقِ الْيُسْرِ وَالرَّفْقِ وَالْحِكْمَةِ',
           'بَيَانٌ لِعَظَمِ شَرِيعَةِ الْإِسْلَامِ',
           'بِالْأَنَامِ',
           'طَرِيقُ الْفَلَاحِ وَالدُّخُولِ إِلَى الْجَنَّةِ',
           'تَتْمِيمٌ لِلْفَرَائِضِ وَزِيَادَةٌ فِي الدَّرَجَاتِ وَالْمَثُوبَاتِ',
           'وَهَدْيِ نَبِيِّ الرَّحْمَةِ سَيِّدِنَا مُحَمَّدٍ',
           'أَذْكُرُ حُكْمَ الِاقْتِصَارِ عَلَى الْفَرَائِضِ',
           'مِنَ الْفَوَائِدِ عَلَى الْجَمْعِ بَيْنَ الْفَرَائِضِ وَالتَّطَوُّعَاتِ',
           'مِنَ النَّقْصِ وَالِاخْتِلَالِ عَلَى تَرْكِ التَّطَوُّعَاتِ',
           'تَرَكَ النَّبِيُّ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ حَثَّ السَّائِلِ عَلَى السُّنَنِ وَالْفَضَائِلِ؟',
           'مَاذَا أَسْتَخْلِصُ مِنْ سُؤَالِ الصَّحَابِيِّ',
           'قَالَ الشِّبْرَخِيتِيُّ رَحِمَهُ اللهُ',
           'أَسْبَابٌ لِدُخُولِ الْجَنَّةِ',
           'تَعْلِيقَ الْحُكْمِ عَلَى الْوَصْفِ يُشْعِرُ بِالْعِلِّيَّةِ',
           'وَقَدْ ثَبَتَ فِي الصَّحِيحِ',
           '«لَا يُنَجِّي أَحَدًا مِنْكُمْ عَمَلُهُ»',
           'يَتَغَمَّدَنِي اللهُ بِرَحْمَتِهِ، وَلَكِنْ سَدِّدُوا»',
           'فَالْجَوَابُ أَنَّ دُخُولَ الْجَنَّةِ بِمَحْضِ فَضْلِ اللهِ تَعَالَى لَيْسَ إِلَّا',
           'وَأَمَّا اخْتِلَافُ مَرَاتِبِهَا فَبِحَسَبِ الْعَمَلِ، لَكِنْ لَا بُدَّ',
           '[الفتوحات الوهبية للشبرخيتي مع اختيار رواية أخرى للحديث مغايرة بعض الشيء]',
           'أُوَفِّقُ بَيْنَ مَا جَاءَ فِي حَدِيثِ الدَّرْسِ',
           'أَقْرَأُ نَصَّ الدَّعْمِ وَالتَّطْبِيقِ، وَأُجِيبُ عَنِ الْأَسْئِلَةِ']:
    check(f'matière : {kw[:38]}…', kw in src)
# — cohérences internes —
check('hadith 22 Arbaʿūn : Jābir [Ṣaḥīḥ de Muslim]',
      'Jābir ibn ’Abd Allāh al-Anṣārī' in src and '[Ṣaḥīḥ de Muslim]' in src)
check('récits cités : [al-Muwaṭṭa’], [Musnad de l’imam Aḥmad]',
      '[al-Muwaṭṭa’]' in src and '[Musnad de l’imam Aḥmad]' in src)
check('aš-Šubraḫītī cité avec sa source imprimée',
      'Aš-Šubraḫītī' in src and 'al-Futūḥāt al-wahbiyya' in src)
check('encadréhadith : أَدْخُلُ dans le matn, أَأَدْخُلُ dans les citations',
      'شَيْئًا، أَدْخُلُ الْجَنَّةَ؟' in src and 'أَأَدْخُلُ الْجَنَّةَ؟' in src)
check('0 espace simple après « (U+202F partout)', '« ' not in src)
check('0 espace simple avant »', ' »' not in src)

print(f'== verify-hadith5-pdf27 : {len(ok)} OK / {len(fail)} échec ==')
for f in fail:
    print('ÉCHEC :', f)
sys.exit(1 if fail else 0)
