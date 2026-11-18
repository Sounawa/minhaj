#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-39 — vérification de la livraison hadith-6ep / pdf-mut23h3b-684
# (شكر الله على نعمة الجوارح — hadith Abū Hurayra, البخاري ومسلم, Nawawī 26 suite).
# Leçon 4 du tirage : pp.29-35 du manuel (7 pages). Données adjudiquées Z2-39 :
# textlayer 27-36 + bbox word-level + tesseract ara 600 psm 4/6 (+psm6 extractions
# ciblées) + VLM 4 vagues (~75 lectures, quota 429 en fin de tour) + anatomie des
# points + recoupement إحياء علوم الدين (Ghazālī, kitāb aṣ-ṣabr wa-l-šukr).
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-6ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-6ep/pdf-mut23h3b-684.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-mut23h3b-684']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-mut23h3b-684 unique', len(les) == 1, f'{len(les)} occurrences')
l = les[0]
fr = l.get('htmlFr') or ''
# — structure —
check('volume cohérent (leçon 7 pp., 21-34k car)', 21000 <= len(src) <= 34000, f'{len(src)} car')
check('titre h1 présent', src.startswith('<h1>La gratitude envers Dieu pour le don des facultés</h1>'))
check('sections h2 = 10', src.count('<h2>') == 10, f'h2={src.count("<h2>")}')
check('sections h3 = 3 (extraction + أولاً + ثانياً)', src.count('<h3>') == 3, f'h3={src.count("<h3>")}')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Introduction', 'Le hadith', 'Notice du transmetteur',
       'L’explication', 'Extraction des idées', 'L’analyse', 'Ce que le hadith enseigne',
       'L’évaluation', 'L’enrichissement', 'La préparation préalable']))
check('2 tableaux (السلوكات + الجوارح)', src.count('<table>') == 2, f'table={src.count("<table>")}')
check('tables : السلوكات 5 rangées + الجوارح 4 rangées', src.count('<tr>') == 9, f'tr={src.count("<tr>")}')
check('objectifs = 3 items', src.count('<li>Que je') == 3, f'{src.count("<li>Que je")}')
# — typographie série —
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('0 ligature ﷺ (honorifique porté par le français)', '\ufdfa' not in src)
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 double tiret résiduel', '——' not in src)
check('0 double entité &nbsp;', '&nbsp;&nbsp;' not in src)
check('0 U+00A0 littéral', '\u00a0' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?|⟦', src))
check('U+202F en vigueur (espaces fines devant ; : ! ? et dans « »)', src.count('\u202f') >= 100,
      f"{src.count('\u202f')} occurrences")
check('0 caractère cyrillique/latin suspect', not re.search(r'[а-яА-Яієґ]', src))
# — données adjudiquées du manuel (Z2-39, pp.29-35) —
KW = [
    '<h1>La gratitude envers Dieu pour le don des facultés</h1>',
    'شُكْرُ اللهِ عَلَى نِعْمَةِ الْجَوَارِحِ',
    # objectifs (3 — le 3e cmap-aveugle, tranché psm6 ×1 + VLM ×2)
    'أَنْ أَتَعَرَّفَ عَظْمَةَ نِعْمَةِ الْجَوَارِحِ، وَكَيْفَ أَشْكُرُ اللهَ عَلَيْهَا',
    'أَنْ أُدْرِكَ أَنَّ اسْتِعْمَالَ جَوَارِحِي فِي الْخَيْرِ مِنَ الصَّدَقَاتِ',
    'أَنْ أَحْرُصَ كُلَّ يَوْمٍ عَلَى اسْتِعْمَالِ جَوَارِحِي فِي الْخَيْرِ',
    # تمهيد (ou devant عضو + نعمًا عظيمةً tranchés VLM 1200 dpi ; تعالى tranché tesseract ×2)
    'كُلَّ يَوْمٍ تَطْلُعُ فِيهِ الشَّمْسُ أَنْظُرُ إِلَى جِسْدِي', 'أَوْ عُضْوٍ مِنْ أَعْضَائِي',
    'نِعَمًا عَظِيمَةً وَهَبَنِي اللهُ إِيَّاهَا', 'تَعَالَى عَلَى هٰذِهِ النِّعَمِ',
    # hadith (تعدل sans alif — anatomie ; فتحمله عليها — tesseract ×2 + VLM r1 ; تمشيها — VLM r3 ;
    # والكلمة الطيبة صدقة — tesseract ×2 + شرح p.32 ; رواه البخاري ومسلم — VLM r3)
    'كُلُّ سَلَامَى مِنَ النَّاسِ عَلَيْهِ صَدَقَةٌ', 'تَعْدِلُ بَيْنَ اثْنَيْنِ صَدَقَةٌ',
    'وَتُعِينُ الرَّجُلَ فِي دَابَّتِهِ فَتَحْمِلُهُ عَلَيْهَا',
    'أَوْ تَرْفَعُ لَهُ عَلَيْهَا مَتَاعَهُ صَدَقَةٌ', 'وَالْكَلِمَةُ الطَّيِّبَةُ صَدَقَةٌ',
    'وَبِكُلِّ خُطْوَةٍ تَمْشِيهَا إِلَى الصَّلَاةِ صَدَقَةٌ',
    'وَتَمِيطُ الْأَذَى عَنِ الطَّرِيقِ صَدَقَةٌ', 'Rapporté par al-Bukhārī et Muslim',
    # ترجمة الراوي (nasab صخر — CONCORDE ; dates 7/5374/800/59 — chiffre à chiffre VLM)
    'عَبْدُ الرَّحْمَنِ بْنُ صَخْرٍ الدَّوْسِيُّ', 'كَانَ أَكْثَرَ الصَّحَابَةِ حِفْظًا',
    'بِخَيْبَرَ سَنَةَ 7 هـ', 'وَرَوَى عَنْهُ 5374 حَدِيثًا',
    'أَكْثَرُ مِنْ 800 مِنَ الصَّحَابَةِ', 'تُوُفِّيَ عَامَ «59 هـ»',
    # الشرح (السَّلامَى alif maqṣūra + وأصله hamza + استُعمل passif + تفصل بالحق — anatomie ف/ق)
    'السَّلَامَى', 'وَأَصْلُهُ عِظَامُ الْكَفِّ', 'ثُمَّ اسْتُعْمِلَ فِي سَائِرِ عِظَامِ الْجَسَدِ',
    'تَفْصِلُ بِالْحَقِّ',
    # استخلاص (على العباد — CONCORDE)
    'أَذْكُرُ النِّعَمَ الْوَارِدَةَ فِي الْحَدِيثِ', 'مَا حَقُّ اللهِ عَلَى الْعِبَادِ',
    # التحليل أولاً (أسبغ ghayn pointé ; pas de فيه — CONCORDE ; أن يتصدق — VLM r2 lettre à lettre)
    'وَأَسْبَغَ عَلَيْهِ نِعَمًا كَثِيرَةً ظَاهِرَةً وَبَاطِنَةً',
    'أَنْ يَتَصَدَّقَ كُلَّ يَوْمٍ صَدَقَةَ شُكْرٍ',
    # التحليل ثانياً + 6 وجوه (تلك — anatomie ت/ذ ; إصلاح ذات البين ; يؤجر sans shadda — CONCORDE ;
    # إشاعة + الإخاء + ونبذ + النزاع — anatomie ; إعانة الناس — CONCORDE ن point dessus ;
    # يبين — cmap y…n ; يثاب — anatomie ; أطيب الكلام + الغلظة + يسع — cmap ; يعني يُعطى حسنة وتكفر — cmap ;
    # البيئة + إزالة — CONCORDE 2× ; التي حث عليها الإسلام — psm6 ; والحياء + بضع وسبعون — VLM ;
    # ركعتا الضحى dual ; على القيام + ويسر + يصبح + عظم + يكفي + فقد قام — CONCORDE/cmap)
    'الشُّكْرُ مِنْ حُقُوقِ اللهِ عَلَى عِبَادِهِ', 'وَمِنْ تِلْكَ الْوُجُوهِ',
    'إِصْلَاحُ ذَاتِ الْبَيْنِ', 'الَّتِي يُؤْجَرُ عَلَيْهَا الْإِنْسَانُ',
    'إِشَاعَةِ الرَّحْمَةِ', 'وَنَبْذِ الشَّحْنَاءِ وَالنِّزَاعِ',
    'إِعَانَةُ النَّاسِ وَمُسَاعَدَتُهُمْ', 'يُبَيِّنُ الرَّسُولُ',
    'صَدَقَةٌ يُثَابُ عَلَيْهَا الْعَبْدُ', 'كَمَنْ يُسَاعِدُ إِنْسَانًا فِي حَمْلٍ',
    'مَحَبَّةً لِلْخَيْرِ وَنَفْعًا لِلْغَيْرِ',
    'الْكَلِمَةُ الطَّيِّبَةُ', 'بِأَطْيَبِ الْكَلَامِ الدَّالِّ',
    'وَالْغِيبَةِ وَالْغَلْظَةِ وَالْفَظَاظَةِ', 'يَسَعُ بِهِ الْمَرْءُ كُلَّ النَّاسِ',
    'الْخُطَى إِلَى الصَّلَوَاتِ', 'يُعْطَى حَسَنَةً، وَتُكَفَّرُ عَنْهُ سَيِّئَتُهُ',
    'إِمَاطَةُ الْأَذَى عَنِ الطَّرِيقِ', 'وَجَمَالِ الْبِيئَةِ', 'وَالْمُبَادَرَةِ إِلَى إِزَالَةِ',
    'الَّتِي حَثَّ عَلَيْهَا الْإِسْلَامُ', 'وَالْحَيَاءُ شُعْبَةٌ مِنَ الْإِيمَانِ',
    'الْإِيمَانُ بِضْعٌ وَسَبْعُونَ', 'رَكْعَتَا الضُّحَى',
    'عَلَى الْقِيَامِ بِحُقُوقِ نِعْمَةِ الْجَوَارِحِ', 'يَصْبَحُ عَلَى كُلِّ سَلَامَى',
    'يَكْفِي مِنْ هٰذِهِ الصَّدَقَاتِ', 'فَقَدْ قَامَ كُلُّ عُضْوٍ بِوَظِيفَتِهِ',
    # مما يستفاد (حقوق + البيئة + وشكره + يؤدي — VLM lettre à lettre)
    'مِنْ حُقُوقِ اللهِ تَعَالَى عَلَى عِبَادِهِ', 'وَالْمُحَافَظَةِ عَلَى الْبِيئَةِ',
    'لِعِبَادَةِ اللهِ وَشُكْرِهِ', 'يُؤَدِّي فِيهِ كُلُّ عُضْوٍ',
    # التقويم (4 items, coquille de numérotation 1,2,2,4 consignée + table)
    'أَتَأَمَّلُ بَدِيعَ صُنْعِ اللهِ', 'كَيْفَ أَشْكُرُ اللهَ عَلَى نِعْمَةِ الْجَوَارِحِ فِي كُلِّ يَوْمٍ',
    'السَّعْيُ فِي نَفْعِ الْعِبَادِ صَدَقَةٌ', 'coquille manifeste',
    'أَوَظِّفُ مُكْتَسَبَاتِي مِنَ الدَّرْسِ', 'السُّلُوكَاتُ', 'التَّعْلِيلُ',
    'أَتَأَخَّرُ مُسَاعَدَةَ الْآخَرِينَ مَخَافَةَ التُّهْمَةِ بِالرِّيَاءِ',
    'أُشَارِكُ فِي الْأَنْشِطَةِ الِاجْتِمَاعِيَّةِ', 'أَهَمُّ بِنَفْسِي وَلَا أُصْلِحُ بَيْنَ النَّاسِ',
    'أُحَافِظُ عَلَى نَظَافَةِ مَدْرَسَتِي وَمُحِيطِي',
    # الاستثمار (الغزالي — ينتظم/الفرح/إضماره/وبالجوارح وباللسان recoupés Iḥyāʾ + psm6 + CONCORDE ;
    # soulignements مقامات السالكين/بالتحميدات/والتوقي — détection numpy filets y536/566/686/716)
    'al-Ghazālī', 'إحياء علوم الدين', 'الْجَوَارِحِ بِالصَّدَقَاتِ',
    'أَتَأَمَّلُ النَّصَّ وَأُجِيبُ عَمَّا يَأْتِي', 'أَشْرَحُ مَا تَحْتَهُ خَطْ',
    'وَمَا مَظَاهِرُ ذَلِكَ', 'مَلْءِ الْجَدْوَلِ الْآتِي',
    'مَقَامَاتِ السَّالِكِينَ', 'بِالتَّحْمِيدَاتِ', 'وَالتَّوْقِي',
    'Iḥyā’ ’ulūm ad-dīn', 'بِتَصَرُّفٍ', 'p. 80',
    'الشُّكْرُ بِنَفْعِ الْعِبَادِ', 'اللِّسَانُ', 'الْيَدَانِ', 'الرِّجْلَانِ',
    # الإعداد القبلي (الموالى alif maqṣūra + علامة singulier + البر والإثم — VLM)
    'أَحْفَظُ حَدِيثَ الدَّرْسِ الْمُوَالَى وَأَسْتَخْرِجُ مِنْهُ عَلَامَةَ الْبِرِّ وَالْإِثْمِ',
    # bornage : la leçon suivante (L5 البر حسن الخلق) annoncée — préparation
    'le hadith de la leçon suivante',
]
for kw in KW:
    check(f'motif présent : {kw[:44]}…', kw in src)
# DATUM : عناصر attendus mais ABSENTS (lectures rejetées par adjudication)
for bad, why in [
    ('تعادل', 'alif non imprimé — tesseract ×2 + anatomie VLM'),
    ('تخطوها', 'تمشيها — anatomie mīm sans hampe'),
    ('التنازع', 'النزاع — anatomie sans tāʾ'),
    ('إشباع', 'إشاعة — ʿayn non pointé'),
    ('العقوق', 'الغلظة — cmap + tesseract'),
    ('فَأَخَذَهُ', 'فأخره — cmap ر + tesseract ×2 + canon Muslim'),
    ('بنظم', 'ينتظم — CONCORDE + psm6 + Iḥyāʾ'),
    ('اللذة', 'الفرح — CONCORDE + psm6 + Iḥyāʾ'),
    ('وَصْفُهُ', 'وإضماره — psm6 + Iḥyāʾ'),
    ('بِتَرْكِ', 'بنفع العباد — psm11 + lexique de la leçon'),
    ('متفق عليه', 'رواه البخاري ومسلم — VLM r3'),
    ('حُطَّتْ', 'وتكفر — cmap وتكفر'),
    ('البِدان', 'اليدان — anatomie yāʾ 2 points'),
    ('الجَسَدُ', 'الجوارح — tesseract psm6 + VLM r1'),
]:
    check(f'absence confirmée : {bad} ({why})', bad not in src)
# — correspondance FICHIER ↔ JSON —
check('htmlFr posé identique au fichier', fr == src, f'{len(fr)} vs {len(src)} car')
check('titleFr conservé', l.get('titleFr') == 'La gratitude envers Dieu pour le don des facultés', f"({l.get('titleFr')})")
check('titleAr conservé', l.get('titleAr') == 'شكر الله على نعمة الجوارح', f"({l.get('titleAr')})")
check('pdfOnly conservé', l.get('pdfOnly') is True)

print(f'{len(ok)} OK / {len(fail)} échec(s)')
for f in fail:
    print('  ÉCHEC :', f)
sys.exit(1 if fail else 0)
