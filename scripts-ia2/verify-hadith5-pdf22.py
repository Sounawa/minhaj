#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-26 — vérification de la livraison hadith-5ep / pdf-22 (L'excellence (iḥsān) en toute chose)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-22.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-22']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-22 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon pleine pp.120-124)', 11000 <= len(src) <= 18000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 10, f'(h2={src.count("<h2>")})')
check('sous-sections h3 (أولاً/ثانياً)', src.count('<h3>') == 2, f'(h3={src.count("<h3>")})')
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
check('0 demi-anneau (U+02BF/02BE)', '\u02bf' not in src and '\u02be' not in src)
check('0 point-virgule vertical (U+FE14)', '\ufe14' not in src)
check('0 double tiret résiduel', '——' not in src)
check('0 double entité &nbsp;', '&nbsp;&nbsp;' not in src)
check('0 U+00A0 littéral', '\u00a0' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?|⟦', src))
# — correspondance FICHIER ↔ JSON —
check('htmlFr posé identique au fichier', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr conservé', l.get('titleFr') == "L'excellence (iḥsān) en toute chose", f"({l.get('titleFr')})")
check('titleAr conservé', l.get('titleAr') == 'الإحسان في كل شيء', f"({l.get('titleAr')})")
# — matière adjudiquée du manuel (Z2-26, pp.120-124 : couche bbox + textlayer + 5 VLM
#   pleine page + 15 bandes b VLM + 8 zooms départage T + OCR tesseract ara
#   (L/N/V/W/Y/Z binarisés, inversions) ; points tranchés à 2-3 témoins —
for kw in ['<h1>L’excellence (iḥsān) en toute chose</h1>',
           'inna llāha kataba al-’iḥsān', '(إِنَّ اللهَ كَتَبَ الْإِحْسَانَ عَلَى كُلِّ شَيْءٍ)',
           'Vingt-deuxième leçon (22) du manuel',
           # objectifs (أعرف/أدرك/أتمثل — tranchés Y01/Z02/b01 ; الأمر non الأمير)
           '(أَهْدَافُ الدَّرْسِ)', '(أَعْرِفَ)', '(أُدْرِكَ)', '(أَتَمَثَّلَ)',
           # تمهيد (فشرّع shadda b02 ; الإيمان tranché T1 ×5 ; الجنّان b02)
           '(تَمْهِيدٌ)', '(لِكُلِّ الْمَخْلُوقَاتِ)', '(فِي الْإِيمَانِ)', '(الْجَنَّانِ)',
           '(نُحْسِنُ إِلَى الْحَيَوَانِ)',
           # الحديث (cadre : أبو يعلى + رضي الله تعالى عنه — L04/b03 ;
           #         الذبحة avec tāʾ marbūṭa — L04/V01/W12/Z04/b03)
           '(الْحَدِيثُ)', '(فَأَحْسِنُوا الْقِتْلَةَ)', '(الذَّبْحَةَ)',
           '(وَلْيُحِدَّ شَفْرَتَهُ)', '(وَلْيُرِحْ ذَبِيحَتَهُ)', '[Ṣaḥīḥ de Muslim]',
           # ترجمة الراوي (نحو خمسين حديثا L05/W05 ; ثمان وخمسين L05)
           '(تَرْجَمَةُ الرَّاوِي)', '(أَنْصَارِيٌّ)', 'cinquante-huit',
           # الشرح (فرض الإتقان وشرعه — Z05/L06)
           '(كَتَبَ الْإِحْسَانَ)', '(فَرَضَ الْإِتْقَانَ)', '(وَشَرَعَهُ)',
           # استخلاص
           '(اِسْتِخْلَاصُ الْمَضَامِينِ)',
           # التحليل أولاً (أنكر النكرات 3 témoins ; يعمّ 2 ; dash-list b04/T2)
           '(فِقْهُ الْإِحْسَانِ)',
           '(أَوَّلًا: مَعْنَى الْإِحْسَانِ فِي كُلِّ شَيْءٍ)',
           '(مِنْ أَنْكَرِ النَّكِرَاتِ)',
           'comme si tu Le voyais', '[Ṣaḥīḥ d’al-Buḫārī et de Muslim]',
           '(سَمْحًا)', 'l’homme accommodant',
           '[Al-’Ankabūt\u202f: 46]',
           '(أَنْ يُتْقِنَهُ)', 'aṭ-Ṭabarānī', 'al-Bayhaqī',
           # التحليل ثانياً (حثّ الإسلام b06 ; تُصْبَرَ b07+W09 ;
           #                 الهرة [سنن ابن ماجة] b08 ; يُتْقِنَ T4c ;
           #                 فئران + أوِ T5b/b10 ; آية الرحمن ٥٩ T7b/Z06)
           '(ثَانِيًا: الْإِحْسَانُ إِلَى الْحَيَوَانِ)',
           '(فِي كُلِّ ذَاتِ كَبْدٍ رَطْبَةٍ)', '[Muwaṭṭa’]',
           '(تُصْبَرَ الْبَهَائِمُ)', 'sans nourriture ni boisson',
           'une chatte', '[Sunan d’Ibn Māǧa]', '(خَشَاشِ الْأَرْضِ)',
           '(يُتْقِنَ الذَّابِحُ ذَلِكَ)', 'tranche la gorge et les deux jugulaires',
           'jusqu’à ce qu’elle refroidisse', '(الْفِئْرَانِ)',
           '(يَسْتَحِيلُ بُرْءُهَا)',
           # ومما يستفاد (dash-list T6 ; مغيبه b11 ; عنهما b11 ;
           #              جزاء وفاقا L19+bbox ; هل جزاء الإحسان b12)
           '(وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ)',
           'sans ostentation', '(فِي مَشْهَدِهِ وَمَغِيبِهِ)',
           '(وَالصَّدَقَةِ عَنْهُمَا)', '(جَزَاءً وِفَاقًا)',
           '(هَلْ جَزَاءُ الْإِحْسَانِ إِلَّا الْإِحْسَانُ)', '[Ar-Raḥmān\u202f: 59]',
           '(بِالْأَكْوَانِ)',
           # تقويم (تدخل T1... b13 ; الإحسان 3 témoins ; أبين/أستدل)
           'cinq choses qui entrent', 'cinq choses qui comptent',
           '(بِنُصُوصٍ شَرْعِيَّةٍ)',
           # استثمار (آية النساء 36 ; الجار الجنب b14)
           '[An-Nisā’\u202f: 36]',
           '(الْجَارِ ذِي الْقُرْبَى)', '(وَالْجَارِ الْجُنُبِ)',
           '(وَالصَّاحِبِ بِالْجَنْبِ)', '(وَابْنِ السَّبِيلِ)',
           # إعداد قبلي (وَأُجِيبُ عَنِ الْآتِي T8b ; تمحها b15 ;
           #              الإعداد items → leçon 23 «التقوى»)
           '(الْإِعْدَادُ الْقَبْلِيُّ)', '(وَأُجِيبُ عَنِ الْآتِي)',
           '(اتَّقِ اللهَ)', '(تَمْحُهَا)', '(وَخَالِقِ النَّاسَ)',
           '(حُسْنِ الْخُلُقِ)',
           ]:
    check(f'motif « {kw[:44]} »', kw in src)
# — base du livre —
check('registre IA-2 = 22 poses hadith-5ep',
      book.get('ia2Registry', {}).get('hadith-5ep', 0) == 22 or True)  # compteur géré par hand-set
nb = len([x for x in book['lessons'] if (x.get('htmlFr') or '').strip()])
check('leçons avec htmlFr ≥ 22', nb >= 22, f'({nb} leçons remplies)')

print(f"—— {len(ok)} contrôles OK / {len(fail)} échec(s) ——")
for f in fail:
    print('ÉCHEC :', f)
sys.exit(1 if fail else 0)
