#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — vérification de la livraison hadith-6ep / pdf-mut23h3b-687
# (دعم وتطبيق — leçon de consolidation, pp.46-49). Données adjudiquées Z2-42 :
# textlayer 44-50 + bbox word-level (cmap pp.46-49) + tesseract ara 600 dpi psm4/6
# (pp.45-50) + strips 1200 dpi multi-psm ×3 chunks (bin/colD/colL/ac + dilatation)
# + ultra-zooms 2400 dpi directs PDF (salami2 verbatim ; qword) + anatomie pixel
# (bandeaux pp.36/41/46 : ornements blancs 12,2-12,3 % ; mot disputé : longueur
# 36,7 pt) + recoupements wikisource/shamela 9472/273 (إحياء علوم الدين :
# فانثروا القرآن + لا يسأل أحدكم عن نفسه إلا القرآن VERBATIM) + habous.gov.ma
# (sommaire officiel : leçon 7 دعم وتطبيق). VLM INDISPONIBLE (3e tour consécutif).
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-6ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-6ep/pdf-mut23h3b-687.html'

src = open(HTML, encoding='utf-8').read()
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('titre h1', src.startswith('<h1>Consolidation et application</h1>'))
check('sections h2 = 7', src.count('<h2>') == 7, f'h2={src.count("<h2>")}')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'J’accomplis dans mon cahier', 'Les textes de la Loi',
       'Les activités', 'Le projet du cours', 'La préparation préalable']))
check('tableaux = 2 (valeurs + droits)', src.count('<table>') == 2, f'{src.count("<table>")}')
check('objectifs = 3 items', src.count('<li>Que j') == 3, f'{src.count("<li>Que j")}')
check('coquilles consignées = 2', src.count('coquille consignée') == 2,
      f'{src.count("coquille consignée")}')
check('réf. إحياء ج1 p.372', 'vol. 1, p. 372' in src)
# — typographie série —
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('0 ligature ﷺ', '\ufdfa' not in src)
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 double tiret résiduel', '——' not in src)
check('0 U+00A0 littéral', '\u00a0' not in src)
check('0 entité &nbsp;', '&nbsp;' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?|⟦|traduire\)', src))
check('U+202F en vigueur', src.count('\u202f') >= 50, f"{src.count('\u202f')} occurrences")
check('0 caractère cyrillique/latin suspect', not re.search(r'[а-яА-Яієґ]', src))
# — données adjudiquées : fragments arabes du tirage (pp.46-49) —
FRAGS = [
    # أهداف (3) — psm4 ×3 (أرسّخ/أتدرّب/أطبّق)
    'أَنْ أُرَسِّخَ مُكْتَسَبَاتِي الْمَعْرِفِيَّةَ مِنَ الدُّرُوسِ السَّابِقَةِ.',
    'أَنْ أَتَدَرَّبَ عَلَى فَهْمِ النُّصُوصِ الشَّرْعِيَّةِ وَتَحْلِيلِهَا.',
    'أَنْ أُطَبِّقَ مُكْتَسَبَاتِي فِي وَضْعِيَّاتٍ جَدِيدَةٍ.',
    # أنجز في دفتري — item 1 (strip psm6+psm7 : «الطهور شطر الإيمان» + points)
    'أُكْمِلُ الْحَدِيثَ الْآتِيَ:',
    'الطُّهُورُ شَطْرُ الْإِيمَانِ',
    # item 2 — 2400 dpi salami2 VERBATIM (psm7/6/13/8 concordants)
    'أَمْلَأُ الْفَرَاغَ بِمَا يُنَاسِبُ:',
    'كُلُّ سُلَامَى مِنَ النَّاسِ عَلَيْهِ',
    'وَالْكَلِمَةُ الطَّيِّبَةُ صَدَقَةٌ',
    'وَتُمِيطُ الْأَذَى عَنِ الطَّرِيقِ صَدَقَةٌ',
    # item 3 (psm6/psm13 : أستدل للمعاني الآتية بما أحفظه من الأحاديث)
    'أَسْتَدِلُّ لِلْمَعَانِي الْآتِيَةِ بِمَا أَحْفَظُهُ مِنَ الْأَحَادِيثِ:',
    'النِّيَّةُ الْحَسَنَةُ تُحَوِّلُ الْعَادَةَ إِلَى عِبَادَةٍ.',
    'الْأَمْرُ بِاتِّبَاعِ السُّنَّةِ وَاجْتِنَابِ الْبِدْعَةِ.',
    # item 4 (psm4+psm6 : البر ما اطمأنت إليه النفس... أذكر الحديث الدال)
    'الْبِرُّ مَا اطْمَأَنَّتْ إِلَيْهِ النَّفْسُ، وَالْإِثْمُ مَا لَمْ تَطْمَئِنَّ إِلَيْهِ.',
    'أَذْكُرُ الْحَدِيثَ الدَّالَّ عَلَى ذَلِكَ.',
    # item 5 (psm6/psm13 : العرباض + وابصة بن معبد)
    'أُعَرِّفُ بِالصَّحَابِيَّيْنِ الْجَلِيلَيْنِ:',
    'الْعِرْبَاضُ بْنُ سَارِيَةَ - وَابِصَةَ بْنِ مَعْبَدٍ - رَضِيَ اللهُ عَنْهُمَا.',
    # النص الأول — النساء 59 (imprimé 58, coquille ; cmap+bbox digits)
    'يَا أَيُّهَا الَّذِينَ آمَنُوا أَطِيعُوا اللهَ وَأَطِيعُوا الرَّسُولَ وَأُولِي الْأَمْرِ مِنْكُمْ',
    'فَإِنْ تَنَازَعْتُمْ فِي شَيْءٍ فَرُدُّوهُ إِلَى اللهِ وَالرَّسُولِ',
    'ذَلِكَ خَيْرٌ وَأَحْسَنُ تَأْوِيلًا',
    # النص الثاني — البقرة 177 (imprimé 176, coquille)
    'لَيْسَ الْبِرَّ أَنْ تُوَلُّوا وُجُوهَكُمْ قِبَلَ الْمَشْرِقِ وَالْمَغْرِبِ',
    'وَلَكِنَّ الْبِرَّ مَنْ آمَنَ بِاللهِ وَالْيَوْمِ الْآخِرِ وَالْمَلَائِكَةِ وَالْكِتَابِ وَالنَّبِيِّينَ',
    'وَأَقَامَ الصَّلَاةَ وَآتَى الزَّكَاةَ',
    'وَالصَّابِرِينَ فِي الْبَأْسَاءِ وَالضَّرَّاءِ وَحِينَ الْبَأْسِ',
    'أُولَئِكَ الَّذِينَ صَدَقُوا وَأُولَئِكَ هُمُ الْمُتَّقُونَ',
    # النص الثالث — إحياء علوم الدين ج1 ص372 بتصرف (wikisource/shamela 9472/273 VERBATIM)
    'إِذَا أَرَدْتُمُ الْعِلْمَ فَانْثُرُوا الْقُرْآنَ؛ فَإِنَّ فِيهِ عِلْمَ الْأَوَّلِينَ وَالْآخِرِينَ',
    'لَا يَسْأَلُ أَحَدُكُمْ عَنْ نَفْسِهِ إِلَّا الْقُرْآنَ، فَإِنْ كَانَ يُحِبُّ الْقُرْآنَ وَيُعْجِبُهُ فَهُوَ يُحِبُّ اللهَ سُبْحَانَهُ وَرَسُولَهُ',
    # header questions — mot disputé ADJUDIQUÉ وأحللها (longueur 36,7 pt + objectif 2)
    'أَتَأَمَّلُ النُّصُوصَ وَأُحَلِّلُهَا، ثُمَّ أُجِيبُ عَنِ الْأَسْئِلَةِ فِي دَفْتَرِي:',
    # أسئلة (5) — psm4+psm6
    'بِمَاذَا يَأْمُرُ اللهُ تَعَالَى فِي الْآيَةِ الْأُولَى؟',
    'طَرِيقَةَ تَدْبِيرِ الْمُسْلِمِينَ لِخِلَافَاتِهِمْ.',
    'مَا تَضَمَّنَتْهُ مِنْ صُوَرِ الْبِرِّ وَأُبَيِّنُ نَوْعَهَا فِي جَدْوَلٍ.',
    'مَكَانَةَ الْقُرْآنِ وَمَنْزِلَتَهُ.',
    'مِعْيَارَ مَحَبَّةِ اللهِ وَرَسُولِهِ.',
    # أنشطة 1 — entêtes + 3 valeurs (zoom 2400 : العناية NON الاهتمام)
    'أَنْقُلُ الْجَدْوَلَ إِلَى دَفْتَرِي وَأَمْلَؤُهُ بِمَا يُنَاسِبُ:',
    'الْقِيمَةُ', 'فَوَائِدُ الِالْتِزَامِ بِهَا', 'عَوَاقِبُ غِيَابِهَا',
    'الْعِنَايَةُ بِجَمَالِ الْبِيئَةِ', 'مُسَاعَدَةُ الْآخَرِينَ', 'الطَّهَارَةُ',
    # أنشطة 2 — أميّز (cmap تميز + série 1re pers.) + تنوع (cmap+psm6 ; تتنوع rejeté)
    'أُمَيِّزُ الْحُقُوقَ فِي الْإِسْلَامِ بِكَوْنِهَا تَنَوَّعَ إِلَى حُقُوقِ اللهِ وَحُقُوقِ النَّفْسِ وَحُقُوقِ الْغَيْرِ.',
    'أَتَأَمَّلُ أَحَادِيثَ الدُّرُوسِ السَّابِقَةِ وَأَسْتَخْلِصُ مِنْهَا فِي دَفْتَرِي أَنْوَاعَ الْحُقُوقِ:',
    'أَنْوَاعُ الْحُقُوقِ:', 'حُقُوقُ اللهِ', 'حُقُوقُ النَّفْسِ', 'حُقُوقُ الْغَيْرِ',
    # مشروع — قراءة ومناقشة العرض + 3 étapes (bbox+psm4+psm6)
    'قِرَاءَةُ وَمُنَاقَشَةُ الْعَرْضِ الْمُنْجَزِ بِعُنْوَانِ: «عِنَايَةُ الْإِسْلَامِ بِجَمَالِ الْبِيئَةِ» مَعَ اتِّبَاعِ الْخُطُوَاتِ الْآتِيَةِ:',
    'أُقَدِّمُ خُلَاصَةً لِلْمَحْوَرِ الَّذِي كُلِّفْتُ بِهِ أَمَامَ أُسْتَاذِي وَأَصْدِقَائِي فِي الْفَصْلِ.',
    'أُسْهِمُ فِي مُنَاقَشَةِ الْعُرُوضِ الْأُخْرَى مُتَحَلِّيًا بِآدَابِ الْحِوَارِ وَالِاخْتِلَافِ فِي الرَّأْيِ.',
    'أُسْهِمُ مَعَ أَصْدِقَائِي فِي الْفَصْلِ فِي صِيَاغَةِ الْخُلَاصَاتِ الَّتِي تَمَّ التَّوَصُّلُ إِلَيْهَا.',
    # الإعداد القبلي (psm6/psm7/psm13 + textlayer)
    'أَحْفَظُ حَدِيثَ الدَّرْسِ الْمُوَالِي، وَأَسْتَخْرِجُ مِنْهُ فَوَائِدَ الصَّوْمِ وَالصَّدَقَةِ.',
]
for f in FRAGS:
    check(f'frag «{f[:36]}…»' if len(f) > 36 else f'frag «{f}»', f in src)
# — motifs d'ABSENCE (lectures rejetées par l'adjudication) —
ABSENT = [
    'الاهتمام بجمال البيئة',   # rejeté : العناية (zoom 2400 psm6/dil ×2)
    'تتنوع',                   # rejeté : cmap تنوع
    'تنقسم',                   # non imprimé (attendu par la grammaire, absent du tirage)
    'فليثور',                  # variante إحياء NON suivie par le tirage
    'ص 273', 'p. 273',         # digits inversés par tesseract/bbox : la page est 372
    'واثلة',                   # compagnon rejeté : وابصة بن معبد (×4 lectures)
    'وابضة',                   # psm13 isolé rejeté
]
for a in ABSENT:
    check(f'ABSENT «{a}»', a not in src)
# — JSON : posé identique après hand-set (contrôle post-pose si déjà posé) —
try:
    book = json.load(open(PATH, encoding='utf-8'))
    les = [l for l in book['lessons'] if l['docId'] == 'pdf-mut23h3b-687']
    check('leçon 687 unique dans le JSON', len(les) == 1, f'{len(les)} occurrences')
    if les and les[0].get('htmlFr'):
        check('htmlFr posé identique', les[0]['htmlFr'].strip() == src.strip(),
              f'JSON={len(les[0]["htmlFr"])} car / HTML={len(src)} car')
    else:
        check('htmlFr pas encore posé (posé à venir)', True)
except Exception as e:
    check('JSON lisible', False, str(e))

print(f'════ QA pdf-mut23h3b-687 : {len(ok)} OK / {len(fail)} échec(s) ════')
for f in fail:
    print(f'  ✗ {f}')
if not fail:
    print('  ✓ aucun échec')
sys.exit(1 if fail else 0)
