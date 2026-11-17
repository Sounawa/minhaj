#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-27 — vérification de la livraison hadith-5ep / pdf-23 (La piété (taqwā) et le bon caractère)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-23.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-23']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-23 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon pleine pp.125-130, 6 pages)', 12000 <= len(src) <= 26000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 10, f'(h2={src.count("<h2>")})')
check('sous-sections h3 (أولاً/ثانياً/ثالثاً)', src.count('<h3>') == 3, f'(h3={src.count("<h3>")})')
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
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?|⟦', src))
# — correspondance FICHIER ↔ JSON —
check('htmlFr posé identique au fichier', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr conservé', l.get('titleFr') == 'La piété (taqwā) et le bon caractère', f"({l.get('titleFr')})")
check('titleAr conservé', l.get('titleAr') == 'التقوى وحسن الخلق', f"({l.get('titleAr')})")
# — matière adjudiquée du manuel (Z2-27, pp.125-130 : couche bbox + textlayer + 6 VLM
#   pleine page + VLM séries V/W/X (zooms 600 dpi) + tesseract L/Z/W/X (ara, ×2-×3) ;
#   points tranchés à 2-3 témoins —
for kw in ['<h1>La piété (taqwā) et le bon caractère</h1>',
           'Vingt-troisième leçon (23) du manuel',
           # bandeau (numéro ٢٣ + titre complet — W13/V01-X01 contre le VLM 150 dpi qui lisait «24»)
           '(أَهْدَافُ الدَّرْسِ)',
           # objectifs (وَوَسِيلَةَ الْحِفَاظِ — bboxlines ; وَالْمُحَافَظَةَ عَلَى الْحَسَنَةِ — X02+bound
           #            contre V02 «أخلاقي» et W01 hallucinés)
           '(أَنْ أَتَعَرَّفَ)', '(أَنْ أُدْرِكَ)', '(أَنْ أَتَمَثَّلَ)',
           '(وَوَسِيلَةَ الْحِفَاظِ عَلَيْهَا)', '(وَالْمُحَافَظَةَ عَلَى الْحَسَنَةِ)',
           # تمهيد (الرُّسُلَ دُعَاةً — bboxlines contre L03 tesseract «الرسول» ;
           #         حَقَّ التَّقْوَى — bound+bboxlines ; [Muwaṭṭa’] — bboxlines «الموطأ»
           #         contre bound-VLM «المِوْظَةُ»)
           '(تَمْهِيدٌ)', '(الرُّسُلَ دُعَاةً)', '(حَقَّ التَّقْوَى)', '[Muwaṭṭa’]',
           '(صَالِحَ الْأَخْلَاقِ)',
           # question نُخَالِطُ (V03 corrigé + bound, contre V03-première-lecture)
           '(نُخَالِطُ بِهِ النَّاسَ)',
           # الحديث (الْأَحَادِيثُ bandeau — bound ; sanad double Abū Ḏarr+Muʿāḏ — L04 INV+brut ;
           #         [سنن الترمذي] — L04 ×2 tesseract contre bound «رواه»)
           '(الْأَحَادِيثُ)', '(اتَّقِ اللهَ حَيْثُمَا كُنْتَ)',
           '(وَأَتْبِعِ السَّيِّئَةَ الْحَسَنَةَ تَمْحُهَا)',
           '(وَخَالِقِ النَّاسَ بِخُلْقٍ حَسَنٍ)', '[Sunan d’at-Tirmiḏī]',
           # ترجمة الراوي (الغِفَارِيُّ — bboxlines+bound contre tesseract «العمّاري» ;
           #               [سنن الترمذي] éloge — L05 ; الرَّبَذَةَ عام 31 — L05 ;
           #               وَسِنُّهُ — L06 contre bound-VLM «وسئل» ;
           #               أَعْلَمَ النَّاسِ بِالْحَلَالِ وَالْحَرَامِ — L06+bboxlines)
           '(أَحَدُ السَّابِقِينَ الْأَوَّلِينَ)',
           '(مَا أَظَلَّتِ الْخَضْرَاءُ وَلَا أَقَلَّتِ الْغَبْرَاءُ أَصْدَقَ مِنْ أَبِي ذَرٍّ)',
           '(نَزَلَ الرَّبَذَةَ)', '(أَسْلَمَ وَسِنُّهُ لَا يَتَجَاوَزُ ثَمَانَ عَشْرَةَ سَنَةً)',
           '(أَعْلَمَ النَّاسِ بِالْحَلَالِ وَالْحَرَامِ)',
           # الفهم/الشرح (3 gloses ; تُزِيلُ آثَارَهَا — bboxlines «تزل» contre W02 «تذهب» ;
           #               وَتُلْغِيهَا — W02 zoom max)
           '(الْفَهْمُ)', '(الشَّرْحُ)', '(وِقَايَةً)',
           '(تُزِيلُ آثَارَهَا وَتُلْغِيهَا)', '(خَالِقِ النَّاسَ)',
           # استنتاج (مُخَالَقَة — L08 tesseract contre bound-VLM «مخالفة»)
           '(اِسْتِنْتَاجُ الْمَضَامِينَ)',
           '(فَضْلُ اتِّبَاعِ السَّيِّئَةِ الْحَسَنَةِ وَمُخَالَقَةِ النَّاسِ بِالْخُلُقِ الْحَسَنِ)',
           # التحليل (أولاً/ثانياً/ثالثاً — L10/L12/L14+bboxlines ;
           #          سبب الورود récit complet — L10 : حِرْصَهُ عَلَى الْمُقَامِ مَعَهُ،
           #          وَعَلِمَ أَنَّهُ لَا يَقْدِرُ عَلَى ذَلِكَ ;
           #          عَثْرَةٌ/صِغَارِ الْمَعَاصِي — L12+bboxlines ;
           #          فَطُلِبَ مِنْهُ — Z08)
           '(التَّحْلِيلُ)', '(يَشْتَمِلُ حَدِيثُ الدَّرْسِ عَلَى مَا يَأْتِي)',
           '(أَوَّلًا: أَمْرُ اللهِ عَزَّ وَجَلَّ بِالتَّقْوَى فِي كُلِّ مَكَانٍ)',
           '(حِرْصَهُ عَلَى الْمُقَامِ مَعَهُ)', '(وَعَلِمَ أَنَّهُ لَا يَقْدِرُ عَلَى ذَلِكَ)',
           '(وَلَيْسَ فِي مَكَانٍ أَوْ زَمَانٍ دُونَ آخَرَ)', '(وَفِي التَّرْبِيَةِ وَالتَّعْلِيمِ)',
           '(ثَانِيًا: الْأَمْرُ بِاتِّبَاعِ السَّيِّئَةِ الْحَسَنَةِ)',
           'حِفَاظًا عَلَى مُدَاوَمَةِ التَّقْوَى',
           '(قَدْ يَخِلُّ مِنْهُ عَثْرَةٌ)', '(أَوْ يَقَعُ فِي صِغَارِ الْمَعَاصِي)',
           '(فَطُلِبَ مِنْهُ إِتْبَاعُ السَّيِّئَةِ بِالْحَسَنَةِ)',
           # المراد بالحسنة (zone VLM-hallucinée p.128 restaurée — L13+Z10 ×2 : التَّوْبَةَ
           #                  وَالِاسْتِغْفَارَ ; hadith Abū Hurayra + [Ṣaḥīḥ de Muslim] —
           #                  VLM p.128 + Ṣaḥīḥ Muslim 233)
           '(مَا يَشْمَلُ التَّوْبَةَ وَالِاسْتِغْفَارَ)',
           '(كَالصَّدَقَةِ وَالصَّلَاةِ وَالصِّيَامِ وَالتَّعَاوُنِ)',
           '(مُكَفِّرَاتٌ مَا بَيْنَهُنَّ إِذَا اجْتُنِبَتِ الْكَبَائِرُ)',
           '[Ṣaḥīḥ de Muslim]',
           # آية هود 114 (cadre p.128 : عَلَى تَقْوَاهُ يَقُولُ اللهُ — tesseract ×3+X04 ;
           #               إِنَّ الْحَسَنَاتِ يُذْهِبْنَ السَّيِّئَاتِ — V05+L13)
           '(عَلَى تَقْوَاهُ)', '(إِنَّ الْحَسَنَاتِ يُذْهِبْنَ السَّيِّئَاتِ)', '[Hūd\u202f: 114]',
           # ثالثاً (1. الْأَمْرُ بِحُسْنِ الْخُلُقِ — VLM p.128+L14+bboxlines contre «أهمية» ;
           #         كَمَا تُحِبُّ أَنْ يُعَامِلُوكَ أَيْضًا — L15+bboxlines ;
           #         وَكَفُّ الْأَذَى عَنْهُمْ بِعَدَمِ الْكَذِبِ وَالْغِشِّ — V06+L15 ;
           #         2. فَضْلُ حُسْنِ الْخُلُقِ ; فَضْلٌ عَظِيمٌ وَأَجْرٌ عَمِيمٌ — bboxlines
           #         contre VLM «عظيم» ×2)
           '(ثَالِثًا: الْأَمْرُ بِحُسْنِ الْخُلُقِ وَفَضْلِهِ)',
           '(الْأَمْرُ بِحُسْنِ الْخُلُقِ)', '(فَضْلُ حُسْنِ الْخُلُقِ)',
           '(مُعَامَلَةُ النَّاسِ بِالصِّدْقِ وَالْإِحْسَانِ وَالْوَفَاءِ بِالْعُهُودِ)',
           '(وَكَفُّ الْأَذَى عَنْهُمْ بِعَدَمِ الْكَذِبِ وَالْغِشِّ وَالْغِيبَةِ وَالنَّمِيمَةِ)',
           '(فَضْلٌ عَظِيمٌ وَأَجْرٌ عَمِيمٌ)',
           # فضل حسن الخلق (suite p.129 : مَحْمَدَةٌ — Z13 ×3 contre VLM «محمد ﷺ» ;
           #                 وَنَيْلٌ لِمَحَبَّةِ النَّاسِ ; hadith «مَا شَيْءٌ أَثْقَلُ»
           #                 [سنن الترمذي] ; أَحَاسِنَكُمْ أَخْلَاقًا — Z14+W06+L16/17
           #                 contre «أحسنكم» ; يَعْفُونَ وَيَصْفَحُونَ)
           '(مَحْمَدَةٌ وَعِبَادَةٌ وَنَيْلٌ لِمَحَبَّةِ النَّاسِ)',
           '(وَإِنَّ اللهَ لَيُبْغِضُ الْفَاحِشَ الْبَذِيءَ)',
           '(أَحَاسِنَكُمْ أَخْلَاقًا)',
           '(وَحُسْنُ الْخُلُقِ مِنْ صِفَاتِ النَّبِيِّينَ وَالْمُرْسَلِينَ وَخِيَارِ الْمُؤْمِنِينَ)',
           'فَلَا يَجْزُونَ بِالسَّيِّئَةِ السَّيِّئَةَ بَلْ يَعْفُونَ وَيَصْفَحُونَ',
           # ومما يستفاد (4 items EN TIRETS ; قَرِينَانِ — L18+bboxlines contre V07 «فريقان» ;
           #               يُحَقِّقُ تَفَاعُلَ النَّاسِ — bboxlines glyphes contre VLM «نفع/تعاون» ;
           #               فَيَتُوبُ الْمُؤْمِنُ — L18+bboxlines ; بِالنَّسَبِ — L18)
           '(وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ)', '(قَرِينَانِ)',
           '(يُحَقِّقُ تَفَاعُلَ النَّاسِ بَعْضِهِمْ لِبَعْضٍ)',
           '(أَنْ جَعَلَ الْحَسَنَاتِ يُذْهِبْنَ السَّيِّئَاتِ)',
           '(فَيَتُوبُ الْمُؤْمِنُ وَلَا يَسْتَبِدُّ بِهِ الْقُنُوطُ وَالْحَسْرَةُ)',
           '(دُونَ تَفْرِيقٍ بِالنَّسَبِ أَوِ الدِّينِ أَوِ اللَّوْنِ أَوْ غَيْرِهَا)',
           # التقويم (3 questions ; بِمَ أَنْصَحُ شَخْصًا — VLM p.130+bboxlines)
           '(التَّقْوِيمُ)', '(مُسْتَشْهِدًا بِبَعْضِ النُّصُوصِ الشَّرْعِيَّةِ)',
           '(بِمَ أَنْصَحُ شَخْصًا يُدَاوِمُ عَلَى مَا اقْتَرَفَ مِنَ الْمَعَاصِي)',
           # الاستثمار (آية [آل عمران: 133-136] ; سَابِقُوا — X07+X10 tesseract, lecture
           #             warch du manuel marocain, contre W11/V08 «سارعوا» ;
           #             الْمُتَّقِينَ activité 1 — X05+L22 contre V09 «المنافقين»+bboxlines ;
           #             activité 3 فَضْلَ حُسْنِ الْخُلُقِ الْوَارِدَ — W08+V09)
           '(الِاسْتِثْمَارُ)', 'سَابِقُوا إِلَى مَغْفِرَةٍ مِنْ رَبِّكُمْ',
           'أُعِدَّتْ لِلْمُتَّقِينَ', '[Āl ’Imrān\u202f: 133-136]',
           '(مِنْ أَوْصَافِ الْمُتَّقِينَ)',
           '(فَضْلَ حُسْنِ الْخُلُقِ الْوَارِدَ فِي الْآيَاتِ)',
           # الإعداد القبلي (item 1 أحفظ حديث الدرس الآتي ; item 2 أُشْرِحُ — W09+X11+V10 ×3
           #                 contre hallucination VLM-X09 ; item 3 — Z22+bboxlines)
           '(الْإِعْدَادُ الْقَبْلِيُّ)', '(أَحْفَظُ حَدِيثَ الدَّرْسِ الْآتِيَ وَأَقُومُ بِمَا يَلِي)',
           '(أُشْرِحُ)', '(تُجَاهَكَ)', '(جَفَّتِ الصُّحُفُ)', '(تَعَرَّفَ إِلَى اللهِ)',
           '(مَا أَخْطَأَكَ لَمْ يَكُنْ لِيُصِيبَكَ)',
           '(مَعْنَى حِفْظِ اللهِ تَعَالَى وَالتَّعَلُّقِ بِهِ)',
           ]:
    check(f'motif « {kw[:44]}… »' if len(kw) > 44 else f'motif « {kw} »', kw in src)

# — livraisons/livres/site synchronisés par CI (rendu suivant le push) —
n_ok, n_fail = len(ok), len(fail)
print(f'PASS {n_ok} / FAIL {n_fail}')
for f in fail:
    print(' ÉCHEC :', f)
sys.exit(1 if n_fail else 0)
