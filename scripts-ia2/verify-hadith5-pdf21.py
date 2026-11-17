#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-24 — vérification de la livraison hadith-5ep / pdf-21 (L'interdiction de la colère)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-21.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-21']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-21 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon pleine pp.114-119)', 11000 <= len(src) <= 18000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 10, f'(h2={src.count("<h2>")})')
check('sous-sections h3 (أولاً/ثانياً)', src.count('<h3>') == 2, f'(h3={src.count("<h3>")})')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Mise en condition', 'Le texte', 'Le transmetteur',
       'La compréhension', 'L’analyse', 'Ce que le hadith nous apprend',
       'L’évaluation', 'L’exploitation', 'La préparation de la leçon suivante']))
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 demi-anneau (U+02BF/02BE)', '\u02bf' not in src and '\u02be' not in src)
check('0 point-virgule vertical (U+FE14)', '\ufe14' not in src)
check('0 double tiret résiduel', '——' not in src)
check('0 double entité &nbsp;', '&nbsp;&nbsp;' not in src)
check('0 U+00A0 littéral', '\u00a0' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?|⟦', src))
# — correspondance FICHIER ↔ JSON —
check('htmlFr posé identique au fichier', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr conservé', l.get('titleFr') == "L'interdiction de la colère", f"({l.get('titleFr')})")
check('titleAr conservé', l.get('titleAr') == 'النهي عن الغضب', f"({l.get('titleAr')})")
# — matière adjudiquée du manuel (Z2-24, pp.114-119 : couche bbox + textlayer + 3 VLM
#   pleine page + 8 bandes r VLM + OCR tesseract ara (bandes r01-r25, recadrages
#   m/L/W binarisés) + canoniques Buḫārī 6116/3282, Tirmiḏī 2021, Abū Dāwūd 4782,
#   Musnad Aḥmad, al-Mu’ǧam aṣ-Ṣaġīr) —
for kw in ['<h1>L’interdiction de la colère</h1>',
           'lā taġḍab', '(لَا تَغْضَبْ)',
           'Vingt et unième leçon (21) du manuel',
           # objectifs
           '(أَهْدَافُ الدَّرْسِ)', 'ثَمَرَاتِ', '(الْمَقَاصِدَ الشَّرْعِيَّةَ)',
           # تمهيد
           '(تَمْهِيدٌ)', '(اجْتِمَاعِيٌّ بِطَبْعِهِ)', 'تَمَالُكِ النَّفْسِ',
           # النص (forme complète canonique établie par cadre inversé OCR + شرح)
           '(أَوْصِنِي)', '(فَرَدَّدَ مِرَارًا)', '[Ṣaḥīḥ d’al-Buḫārī]',
           # ترجمة الراوي
           '(سَبَقَتْ تَرْجَمَتُهُ)',
           # الشرح (تُنَفِّذْ غَضَبَكَ établi par W04 binarisé)
           '(لَا تُنَفِّذْ غَضَبَكَ)', '(ضِدَّ مَنْ أَغْضَبَكَ)', '(كَرَّرَ النَّهْيَ عِدَّةَ مَرَّاتٍ)',
           # استخلاص (أستوحي établi par 3 témoins ; حَصْرِ)
           '(أَسْتَوْحِي)', '(حَصْرِ الْجَوَابِ)',
           # التحليل أولاً
           '(أَوَّلًا: النَّهْيُ عَنِ الْغَضَبِ وَالْمُرَادُ بِهِ)', '(تَنْفِيذِ الْغَضَبِ)',
           # التحليل 2 (فليتوضأ [مسند الإمام أحمد] — 3 témoins)
           '(فَلْيَتَوَضَّأْ)', '[Musnad de l’imam Aḥmad]',
           '(اعْتِدَالِ حَالِهِ)', '(التَّفَاعُلَ مَعَ الْغَضَبِ)',
           '(وَالْوُضُوءُ)', '(الِاسْتِعَاذَةُ بِاللهِ)', '(وَسَاوِسِ الشَّيْطَانِ)',
           # التحليل ثانياً (5 ثمرات)
           '(ثَانِيًا: فَضْلُ مَلْكِ النَّفْسِ عِنْدَ الْغَضَبِ)',
           '(وَالْكَاظِمِينَ الْغَيْظَ)', '[Āl ’Imrān\u202f: 134]',
           '(بِالصُّرَعَةِ)',
           '(حَتَّى يُخَيِّرَهُ مِنَ الْحُورِ مَا شَاءَ)', '[Sunan d’at-Tirmiḏī]',
           '[Āl ’Imrān\u202f: 133-134]',
           'al-Mu’ǧam aṣ-Ṣaġīr d’aṭ-Ṭabarānī',
           '(الْعَلَاقَاتِ الِاجْتِمَاعِيَّةِ)',
           # مما يستفاد
           '(وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ)', 'deux ou trois paroles',
           # التقويم
           '(أُلَخِّصُ)', '(يُهَدِّدُ بِتَنْفِيذِ غَضَبِهِ)',
           # الاستثمار (سليمان بن صرد + أبو ذر)
           '(يَسْتَبَّانِ)', 'visage rouge et les veines gonflées',
           '(فَلْيَضْطَجِعْ)', '[Sunan d’Abū Dāwūd]',
           '(أَسْتَخْرِجُ)',
           # الإعداد القبلي (singulier, أَنْجُزُ مَا يَلِي — tesseract ×2)
           '(الْإِعْدَادُ الْقَبْلِيُّ)', '(الْآتِيَ)', '(أَنْجُزُ)',
           '(الْإِحْسَانَ)', '(أَذْكُرُ أُمْثِلَةً لِلْإِحْسَانِ)', '(فِي كُلِّ شَيْءٍ)',
           ]:
    check(f'contenu « {kw[:44]}… »' if len(kw) > 44 else f'contenu « {kw} »', kw in src)

print(f"—— {len(ok)} contrôles OK / {len(fail)} échec")
for f_ in fail:
    print('  ÉCHEC:', f_)
sys.exit(1 if fail else 0)
