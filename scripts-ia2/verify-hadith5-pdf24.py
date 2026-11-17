#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-28 — vérification de la livraison hadith-5ep / pdf-24 (Préserver les commandements de Dieu)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-24.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-24']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-24 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon pp.131-137, 7 pages, 4 sections d’analyse)', 28000 <= len(src) <= 42000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 10, f'(h2={src.count("<h2>")})')
check('sous-sections h3 (أولاً/ثانياً/ثالثاً/رابعاً)', src.count('<h3>') == 4, f'(h3={src.count("<h3>")})')
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
check('0 demi-anneau (U+02BF/02BE/02BC/02BB)', not any(c in src for c in '\u02bf\u02be\u02bc\u02bb'))
check('0 point-virgule vertical (U+FE14)', '\ufe14' not in src)
check('0 double tiret résiduel', '——' not in src)
check('0 double entité &nbsp;', '&nbsp;&nbsp;' not in src)
check('0 U+00A0 littéral', '\u00a0' not in src)
check('0 ligature ﷺ (honorifique porté par le français, convention série)', '\ufdfa' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?|⟦', src))
# — correspondance FICHIER ↔ JSON —
check('htmlFr posé identique au fichier', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr conservé', l.get('titleFr') == 'Préserver les commandements de Dieu', f"({l.get('titleFr')})")
check('titleAr conservé', l.get('titleAr') == 'حفظ أوامر الله تعالى', f"({l.get('titleAr')})")
# — matière adjudiquée du manuel (Z2-28, pp.131-137 : couche bbox (glyphes, avec coordonnées
#   mot à mot) + textlayer + 7 VLM pleine page 150 dpi + VLM séries V/W (zooms 600 dpi ×1-×5,
#   scrutins lettre par lettre) + tesseract L/W/X (ara, ×1-×6, multi-seuils, psm 6/7/13) ;
#   chaque point tranché à 2-3 témoins —
for kw in ['<h1>Préserver les commandements de Dieu</h1>',
           'Vingt-quatrième leçon (24) du manuel',
           # objectifs (أَنْ أَتَعَرَّفَ — T X01 ×3+B contre VLM «يُعَرِّفَ» ;
           #            وَالْعَلَاقَةَ...بِقَدَرِهِ — bbox ; وَالتَّعَلُّقِ بِهِ — bbox+V150)
           '(أَنْ أَتَعَرَّفَ مَعْنَى حِفْظِ اللهِ)',
           '(ثَمَرَةَ حِفْظِ اللهِ وَالْعَلَاقَةَ بَيْنَهُ وَبَيْنَ الْإِيمَانِ بِقَدَرِهِ)',
           '(مِنَ الْأَمْرِ بِحِفْظِ اللهِ وَالتَّعَلُّقِ بِهِ)',
           # تمهيد (بِحِفْظٍ إِلَهِيٍّ شَامِلٍ indéfini — bbox+T W02 ; مُطْمَئِنًّا فِي نَفْسِهِ —
           #         bbox contre VLM «مُطِيعًا» ; question finale بِقَدَرِ اللهِ — VLM-B zoom+V150)
           '(أَنْ يُشْمَلَ الْعَبْدُ بِحِفْظٍ إِلَهِيٍّ شَامِلٍ)',
           '(مُطْمَئِنًّا فِي نَفْسِهِ)',
           '(وَعَلَاقَتُهُ بِالْإِيمَانِ بِقَدَرِ اللهِ؟)',
           # hadith (sanad : كُنْتُ خَلْفَ — T X04×2+V (bbox «كتداف» = ghost-dot خ/د) ;
           #         يَوْمًا فَقَالَ — T W03 «يمآ» ; وَإِنِ kasra — VLM-A lettre par lettre+V150
           #         contre T sukūn ; réf [سنن الترمذي] — VLM-A lettre par lettre (س-ن-ن)+T W03
           #         contre V150 «رواه»)
           '(كُنْتُ خَلْفَ النَّبِيِّ يَوْمًا فَقَالَ)',
           '(احْفَظِ اللهَ يَحْفَظْكَ، احْفَظِ اللهَ تَجِدْهُ تُجَاهَكَ)',
           '(إِذَا سَأَلْتَ فَاسْأَلِ اللهَ، وَإِذَا اسْتَعَنْتَ فَاسْتَعِنْ بِاللهِ)',
           '(وَإِنِ اجْتَمَعُوا عَلَى أَنْ يَضُرُّوكَ)',
           '(رُفِعَتِ الْأَقْلَامُ وَجَفَّتِ الصُّحُفُ)', '[Sunan d’at-Tirmiḏī]',
           # suite (cadre p.132 VIDE en textlayer/bbox — police décorée ; entièrement
           #        T W04+V150 : وَفِي رِوَايَةِ غَيْرِ التِّرْمِذِيِّ + [المستدرك للحاكم])
           '(وَفِي رِوَايَةِ غَيْرِ التِّرْمِذِيِّ)',
           '(تَعَرَّفْ إِلَى اللهِ فِي الرَّخَاءِ يَعْرِفْكَ فِي الشِّدَّةِ)',
           '(وَأَنَّ مَعَ الْعُسْرِ يُسْرًا)', '[Al-Mustadrak d’al-Ḥākim]',
           # ترجمة الراوي (أَحَدُ الْأَعْلَامِ — cluster bbox ا,ل,ا,ع,ل = الْأَعْلَـ exact
           #               + VLM-C lettre par lettre, contre T «العبادلة» et V150 «العلماء» ;
           #               مَنَاقِبُهُ أَكْثَرُ مِنْ أَنْ تُحْصَرَ — T W05+bbox contre VLM
           #               «ماتته أمه» ; حَنَكَهُ...بِرِيقِهِ — T+bbox ; بَحْرَ الْأُمَّةِ — ×3 ;
           #               ثَمَانِيَةٍ وَسِتِّينَ (68 H) — T+bbox contre VLM «ثمانين»)
           '(أَحَدُ الْأَعْلَامِ مِنَ الصَّحَابَةِ)',
           '(وُلِدَ قَبْلَ الْهِجْرَةِ بِثَلَاثِ سِنِينَ)',
           '(مَنَاقِبُهُ أَكْثَرُ مِنْ أَنْ تُحْصَرَ)',
           '(حَنَكَهُ الرَّسُولُ بِرِيقِهِ)',
           '(اللَّهُمَّ فَقِّهْهُ فِي الدِّينِ وَعَلِّمْهُ التَّأْوِيلَ)',
           '[Al-Mu’ǧam aṣ-ṣaġīr d’aṭ-Ṭabarānī]',
           '(فَكَانَ بَحْرَ الْأُمَّةِ وَحَبْرَهَا وَتَرْجُمَانَ الْقُرْآنِ)',
           '(عَامَ ثَمَانِيَةٍ وَسِتِّينَ لِلْهِجْرَةِ)',
           # الفهم/الشرح (8 gloses ; وَنَوَاهِيهِ — bbox+T contre VLM «وتواعيه» ;
           #               كَتَبَهُ اللهُ لَكَ: قَدَّرَهُ لَكَ — bbox+T (VLM «كنت له») ;
           #               لَا تَبْدِيلَ لَهُ — bbox+T contre VLM «لا تنقله إلا بأكثره» ;
           #               وَالْغِنَى — T+B+V contre VLM-zoom «والعافية» (hallucination) ;
           #               لَنْ يُصِيبَكَ — bbox+VLM-D contre T «أن»)
           '(اِحْفَظْ أَوَامِرَ اللهِ وَنَوَاهِيهِ بِالِامْتِثَالِ)',
           '(قَدَّرَهُ لَكَ)',
           '(أَنَّ مَا قَدَّرَهُ اللهُ لَا تَبْدِيلَ لَهُ إِلَّا بِإِذْنِهِ)',
           '(فِي الصِّحَّةِ وَالْغِنَى)',
           '(مَا قَدَّرَ اللهُ أَنْ يُخْطِئَكَ لَنْ يُصِيبَكَ أَبَدًا)',
           '(أَنَّ ذَهَابَ الشِّدَّةِ وَزَوَالَهَا يَكُونُ بَعْدَ الْعُسْرِ)',
           # استخلاص المضامين (nom de rubrique propre à cette leçon — bbox+T+V150,
           #                   différent de la leçon 23 «استنتاج» ; عَجْزَ — T X08+bbox)
           '(اِسْتِخْلَاصُ الْمَضَامِينِ)',
           '(عَجْزَ النَّاسِ كُلِّهِمْ عَنْ نَفْعِ أَحَدٍ أَوْ ضَرِّهِ بِشَيْءٍ دُونَ إِذْنٍ مِنَ اللهِ تَعَالَى)',
           # التحليل (bannière التَّحْلِيلُ — VLM-E lettre par lettre contre V150 «التطبيق» ;
           #          وَلَا يَرْكُنْ — VLM-F lettre par lettre (ن final pointé), B+T l’avaient
           #          perdu ; وَثَمَرَاتِهِ — T+bbox contre VLM «تقمراته» ;
           #          غار : فَانْحَدَرَتْ عَنْهُمُ الصَّخْرَةُ — T×3+VLM-G lettre par lettre,
           #          contre le canon «فانفرجت» ; سَابِقَةً سَبَقَتْ لَهُ مَعَ رَبِّهِ — T W31×2 ;
           #          مُؤْتَمِرًا بِأَوَامِرِهِ — T+bbox contre VLM «مقتدرا» ;
           #          بِإِصْلَاحِ الْحَالِ — T W11 «الالء»+sémantique (الحال/البال) ;
           #          بِالْإِتَابَةِ — bbox+T, graphie du tirage (pour الإثابة))
           '(التَّحْلِيلُ)', '(نُجْمِلُهَا فِي الْآتِي)',
           '(وَلَا يَرْكُنْ فِي مُخَالَفَتِهِ)',
           '(فَإِنَّكَ تَجِدُهُ مَعَكَ فِي الشَّدَائِدِ)',
           '(وَمِنْ ثَمَرَاتِ ذَلِكَ)',
           '(خُصُوصًا حَالَ الشِّدَّةِ)',
           '(فَانْحَدَرَتْ صَخْرَةٌ فَأَطْبَقَتْ عَلَيْهِمْ)',
           '(سَابِقَةً سَبَقَتْ لَهُ مَعَ رَبِّهِ)',
           '(فَانْحَدَرَتْ عَنْهُمُ الصَّخْرَةُ فَخَرَجُوا يَمْشُونَ)',
           '(مُؤْتَمِرًا بِأَوَامِرِهِ)',
           '(بِإِصْلَاحِ الْحَالِ)', '(بِالْإِتَابَةِ وَالرِّضْوَانِ)',
           # ثانياً (وَأَنْ لَا يُعَوِّلَ — T X11 thr+x2 contre W05 «يعزل» ;
           #         مَا قَلَّ مِنْهَا أَوْ كَثُرَ — VLM-I lettre par lettre ;
           #         ﴿ومن يتوكل...فهو حسبه﴾ [الطلاق: ٣] — B+T W33×2 contre VLM-I «يتق»
           #         (hallucination, 4 témoins contre) ; فَلَا تَتَوَجَّهَ — T X14×3 ;
           #         يَرْكَنُ الشَّخْصُ — T W12 ; وَالْتَجَأَ إِلَى مَنْ لَا يَضُرُّهُ وَلَا يَنْفَعُهُ —
           #         B glyphs + T + VLM-J sémantique ; [غافر: ١٣] — T×3, numérotation
           #         décalée du tirage (contenu standard 14), comme toutes les réfs de la leçon)
           '(وَأَنْ لَا يُعَوِّلَ عَلَى سِوَاهُ)',
           '(مَا قَلَّ مِنْهَا أَوْ كَثُرَ)',
           '(وَمَنْ يَتَوَكَّلْ عَلَى اللهِ فَهُوَ حَسْبُهُ)', '[Aṭ-Ṭalāq\u202f: 3]',
           '(فَبِقَدْرِ مَا يَرْكَنُ الشَّخْصُ إِلَى غَيْرِ اللهِ تَعَالَى بِطَلَبِهِ أَوْ بِقَلْبِهِ أَوْ بِأَمَلِهِ)',
           '(وَالْتَجَأَ إِلَى مَنْ لَا يَضُرُّهُ وَلَا يَنْفَعُهُ)',
           '(فَلَا تَتَوَجَّهَ إِلَى غَيْرِ اللهِ رَجَاءً وَرَغْبَةً أَوْ خَوْفًا وَرَهْبَةً)',
           '(لِتَحْفَظَ لَهُ حَقَّ الْعِبَادَةِ الْخَالِصَةِ)',
           '(فَادْعُوا اللهَ مُخْلِصِينَ لَهُ الدِّينِ)', '[Ġāfir\u202f: 13]',
           # ثالثاً (عَقَائِدِ الْإِيمَانِ — T W15 contre VLM-L «بالصدق» ;
           #         وَلَا يَسْأَلَ غَيْرَ اللهِ — T W15+VLM-L lettre par lettre ;
           #         مَا قَدَّرَتْ — VLM-M lettre par lettre (ق 2 points+shadda) ;
           #         سُبْحَانَهُ — T×5 en séquence (W15, X19×2, W36×2) + présence de glyphes
           #         en bbox entre بغيره et لانه, contre 2 VLM-zooms négatifs ;
           #         هُوَ الْفَاعِلُ — T+B ; لِمَا تَقَدَّمَ — T W16 résout le garble bbox
           #         «ماتدم» ; بِنَسْخٍ أَوْ تَبْدِيلٍ — T W16)
           '(رُكْنٌ أَسَاسِيٌّ مِنْ عَقَائِدِ الْإِيمَانِ)',
           '(وَلَا يَسْأَلَ غَيْرَ اللهِ عَزَّ وَجَلَّ)',
           '(لَا يَمْلِكُ أَحَدٌ إِنْزَالَهُ أَوْ دَفْعَهُ)',
           '(مَا قَدَّرَتْ إِلَّا بِإِذْنِ اللهِ)',
           '(بِغَيْرِهِ سُبْحَانَهُ)', '(هُوَ الْفَاعِلُ فِي الْحَقِيقَةِ)',
           '(لِمَا تَقَدَّمَ مِنْ أَنَّهُ لَا يَكُونُ خِلَافَ مَا كَتَبَهُ اللهُ لَكَ أَوْ عَلَيْكَ بِنَسْخٍ أَوْ تَبْدِيلٍ)',
           # رابعاً (فِي الرِّوَايَةِ الْأُخْرَى — T W17 contre «الزواية» ;
           #         مُعَرَّضُونَ — T X20×3 contre bbox «يكلفون» ;
           #         آية البقرة — extent W17+W18 T (ولنبلونكم…المهتدون),
           #         réf ١٥٤-١٥٦ = numérotation du tirage (contenu standard 155-157) ;
           #         آية الزمر réf ١١ (contenu standard 10))
           '(رابعاً: الْفَرَجُ مَعَ الصَّبْرِ)',
           '(فِي الرِّوَايَةِ الْأُخْرَى)',
           '(وَاعْلَمْ أَنَّ النَّصْرَ مَعَ الصَّبْرِ، وَأَنَّ الْفَرَجَ مَعَ الْكَرْبِ)',
           '(مُعَرَّضُونَ لِلْمَصَائِبِ وَالِابْتِلَاءَاتِ)',
           '(وَلَنَبْلُوَنَّكُمْ بِشَيْءٍ مِنَ الْخَوْفِ وَالْجُوعِ)',
           '(إِنَّا لِلَّهِ وَإِنَّا إِلَيْهِ رَاجِعُونَ)',
           '(أُولَئِكَ هُمُ الْمُهْتَدُونَ)', '[Al-Baqara\u202f: 154-156]',
           '(إِنَّمَا يُوَفَّى الصَّابِرُونَ أَجْرَهُمْ بِغَيْرِ حِسَابٍ)', '[Az-Zumar\u202f: 11]',
           # يستفاد (فَلْيَجْمِلْ — VLM-P lettre par lettre (ج 1 point interne) + T×3 فليجمل ;
           #          خردل — T W19+VLM-P ; [لقمان: ١٥] — T+V150+VLM-Q lettre par lettre
           #          (contenu standard 16) ; تَوْطِينُ — T W19 contre VLM «تولية» ;
           #          بِاللُّطْفِ وَاللِّينِ — T W19 contre VLM «بالظهف والبين»)
           '(فَلْيَجْمِلْ فِي الطَّلَبِ)',
           '(يَا بُنَيَّ إِنَّهَا إِنْ تَكُ مِثْقَالَ حَبَّةٍ مِنْ خَرْدَلٍ)',
           '[Luqmān\u202f: 15]',
           '(تَوْطِينُ النَّفْسِ وَتَرْبِيَتُهَا عَلَى الثِّقَةِ بِاللهِ تَعَالَى)',
           '(الْأَخْذُ بِاللُّطْفِ وَاللِّينِ فِي تَرْبِيَةِ الطِّفْلِ وَتَعْلِيمِهِ)',
           # تقويم (أُبَيِّنُ كَيْفِيَّةَ — T W20+VLM R+V150 contre VLM W46 ;
           #        أُوَفِّقُ بَيْنَ — T q3c ×2+VLM R (le وَبَيْنِ final exige la
           #        construction أوفق بين…وبين) ; نَفْعِ النَّاسِ بَعْضِهِمْ بَعْضًا —
           #        VLM R lettre par lettre (بَعْضًا tanwīn) contre bbox «تفاعل»)
           '(مَا مَعْنَى قَوْلِهِ: «احْفَظِ اللهَ يَحْفَظْكَ»؟)',
           '(أُبَيِّنُ كَيْفِيَّةَ التَّعَلُّقِ بِاللهِ)',
           '(أُوَفِّقُ بَيْنَ مَعْنَى)',
           '(وَبَيْنِ نَفْعِ النَّاسِ بَعْضِهِمْ بَعْضًا)',
           # استثمار (cadre الأنععام ornementé p.137, VIDE en textlayer — reconstruit
           #          T W21+W40+W41 (79: وجّهت…حنيفا ; 80: وحاجه قومه…أفلا تتذكرون ;
           #          81: وكيف أخاف…الفريقين ; 82: الذين آمنوا…وهم المهتدون — fin du
           #          cadre : «لهم الأمن» en bbox y0.397) + médaillons ٨٢/٨٣ VLM-U ;
           #          réf ٨٠-٨٣ = numérotation du tirage (contenu 79-82) — B (ordre
           #          inversé des mots du à l’assemblage RTL)+T+V150+VLM-U contre VLM
           #          W47 «٨٢» ; أُحَدِّدُ/الْأَمْنِ — T W22+B contre VLM «الأمر»)
           '(يَقُولُ اللهُ عَزَّ وَجَلَّ:)',
           '(إِنِّي وَجَّهْتُ وَجْهِيَ لِلَّذِي فَطَرَ السَّمَاوَاتِ وَالْأَرْضَ حَنِيفًا وَمَا أَنَا مِنَ الْمُشْرِكِينَ)',
           '(وَحَاجَّهُ قَوْمُهُ قَالَ أَتُحَاجُّونِّي فِي اللهِ وَقَدْ هَدَانِ)',
           '(وَكَيْفَ أَخَافُ مَا أَشْرَكْتُمْ وَلَا تَخَافُونَ أَنَّكُمْ أَشْرَكْتُمْ بِاللهِ مَا لَمْ يُنَزِّلْ بِهِ عَلَيْكُمْ سُلْطَانًا)',
           '(الَّذِينَ آمَنُوا وَلَمْ يَلْبِسُوا إِيمَانَهُمْ بِظُلْمٍ أُولَئِكَ لَهُمُ الْأَمْنُ وَهُمْ مُهْتَدُونَ)',
           '[Al-An’ām\u202f: 80-83]',
           '(أُحَدِّدُ مِنَ الْآيَاتِ مَا يَدُلُّ عَلَى التَّعَلُّقِ بِاللهِ عَزَّ وَجَلَّ)',
           '(إِبْرَاهِيمَ الْخَلِيلِ عَلَيْهِ السَّلَامُ إِيمَانًا بِالْقَضَاءِ وَالْقَدَرِ)',
           '(مَا مَصْدَرُ الْأَمْنِ الَّذِي يَتَحَدَّثُ عَنْهُ سَيِّدُنَا إِبْرَاهِيمُ عَلَيْهِ السَّلَامُ؟)',
           # الإعداد القبلي (bannière — T+B+VLM contre V150 «الأعمدة الفعلية» ;
           #                كَلَامَ النُّبُوَّةِ الْأُولَى — T×5 (X28×3+W43×2) contre
           #                VLM-V «الأولي» ; PAS de إِذَا avant لَمْ تَسْتَحْيِ — T+VLM-V ;
           #                الْحَيَاءِ deux fois — T×3+VLM-V contre V150 «الحجاب»)
           '(الْإِعْدَادُ الْقَبْلِيُّ)',
           '(أَحْفَظُ حَدِيثَ الدَّرْسِ الْآتِيَ، وَأَقُومُ بِمَا يَلِي:)',
           '(كَلَامَ النُّبُوَّةِ الْأُولَى)',
           '(لَمْ تَسْتَحْيِ، فَاصْنَعْ مَا شِئْتَ)',
           '(أُبَيِّنُ فَضْلَ الْحَيَاءِ وَمَظَاهِرَ الْحَيَاءِ)',
           ]:
    # les motifs courts entre parenthèses désignent des spans autonomes ; les phrases
    # d'un span long sont testées aussi sans leurs parenthèses (forme mid-span)
    hit = kw in src or (kw.startswith('(') and kw.endswith(')') and kw[1:-1] in src)
    check(f'motif « {kw[:44]}… »' if len(kw) > 44 else f'motif « {kw} »', hit)

# — livraisons/livres/site synchronisés par CI (rendu suivant le push) —
n_ok, n_fail = len(ok), len(fail)
print(f'PASS {n_ok} / FAIL {n_fail}')
for f in fail:
    print(' ÉCHEC :', f)
sys.exit(1 if n_fail else 0)
