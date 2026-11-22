#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — verify-h6-15 : contrôles de la livraison pdf-mut23h3b-694 (L14 hadith-6ep
# «دعم وتطبيق» pp.81-84). Vérrouille les adjudications du tour : présence des
# formes retenues, ABSENCE des lectures rejetées (bruit OCR / hallucinations VLM).
import re, sys

H = open("/home/z/my-project/minhaj/scripts-ia2/livraisons/hadith-6ep/pdf-mut23h3b-694.html",
         encoding="utf-8").read()

PRESENT = [
    ("h1", "Consolidation et application"),
    ("leçon 14", "Quatorzième leçon (14)"),
    ("objectifs header", "أَهْدَافُ الْأَنْشِطَةِ"),
    ("obj item 1", "أَنْ أُرَسِّخَ مُكْتَسَبَاتِي الْمَعْرِفِيَّةَ"),
    ("obj item 2", "أَنْ أَتَدَرَّبَ عَلَى فَهْمِ النُّصُوصِ الشَّرْعِيَّةِ وَتَحْلِيلِهَا"),
    ("obj item 3 ouazziqa", "أَنْ أُوَظِّفَ مُكْتَسَبَاتِي فِي وَضْعِيَّاتٍ جَدِيدَةٍ"),
    ("nachat1 item1 mahabba", "مِنْ أَسْبَابِ مَحَبَّةِ اللهِ لِلْعَبْدِ"),
    ("nachat1 item2 farada", "«إِنَّ اللهَ فَرَضَ .......»"),
    ("nachat1 item3", "أُبَيِّنُ الْفَرْقَ بَيْنَ الضَّرَرِ وَالضِّرَارِ"),
    ("nachat1 item4 lisan", "حَذَّرَ الرَّسُولُ ﷺ مِنْ خُطُورَةِ اللِّسَانِ"),
    ("nachat1 item5 sahabiy", "مُعَاذُ بْنُ جَبَلٍ - أَبِي سَعِيدٍ الْخُدْرِيِّ رَضِيَ اللهُ عَنْهُمَا"),
    ("hadith1 isnad", "عَنْ عَبْدِ اللهِ بْنِ عَمْرٍو أَنَّ رَسُولَ اللهِ ﷺ قَالَ"),
    ("hadith1 Q1", "«أَتَدْرُونَ مَنِ الْمُسْلِمُ؟»"),
    ("hadith1 R1", "«مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ.»"),
    ("hadith1 Q2", "قَالُوا: فَمَنِ الْمُؤْمِنُ؟"),
    ("hadith1 R2", "«مَنْ أَمِنَهُ الْمُؤْمِنُونَ عَلَى أَمْوَالِهِمْ وَأَنْفُسِهِمْ.»"),
    ("hadith1 Q3", "قَالُوا: فَمَنِ الْمُهَاجِرُ؟"),
    ("hadith1 R3 sharr", "«مَنْ هَجَرَ الشَّرَّ وَاجْتَنَبَهُ.»"),
    ("hadith1 takhrij", "مَكَارِمُ الْأَخْلَاقِ وَمَعَالِيهَا وَمَحْمُودُ طَرَائِقِهَا؛ لِلْخَرَائِطِيِّ"),
    ("hadith2 isnad", "عَنْ أَنَسِ بْنِ مَالِكٍ قَالَ: قَالَ رَسُولُ اللهِ ﷺ"),
    ("hadith2 matn", "لَا يَسْتَقِيمُ إِيمَانُ عَبْدٍ حَتَّى يَسْتَقِيمَ قَلْبُهُ"),
    ("hadith2 clause jara", "وَلَا يَدْخُلُ رَجُلٌ الْجَنَّةَ لَا يَأْمَنُ جَارُهُ بَوَائِقَهُ"),
    ("hadith2 takhrij", "مُسْنَدُ الْإِمَامِ أَحْمَدَ؛ مُسْنَدُ أَنَسِ بْنِ مَالِكٍ رَضِيَ اللهُ عَنْهُ"),
    ("hadith3 isnad", "عَنْ عُبَادَةَ بْنِ الصَّامِتِ قَالَ: قَالَ رَسُولُ اللهِ ﷺ"),
    ("hadith3 six clauses", "اصْدُقُوا إِذَا حَدَّثْتُمْ، وَأَوْفُوا إِذَا وَعَدْتُمْ، وَأَدُّوا إِذَا اؤْتُمِنْتُمْ"),
    ("hadith3 fin", "وَاحْفَظُوا فُرُوجَكُمْ، وَغُضُّوا أَبْصَارَكُمْ، وَكَفُّوا أَيْدِيَكُمْ"),
    ("hadith3 takhrij 8066", "الْمُسْتَدْرَكُ لِلْحَاكِمِ؛ كِتَابُ الْحُدُودِ، رَقْمُ: 8066"),
    ("questions header aʿlahu", "أَتَأَمَّلُ الْأَحَادِيثَ أَعْلَاهُ وَأُجِيبُ عَنِ الْأَسْئِلَةِ فِي دَفْتَرِي"),
    ("q1 huquq ghayr", "احْتِرَامِ حُقُوقِ الْغَيْرِ"),
    ("q3 thani", "أُبَيِّنُ كَيْفَ يَسْتَقِيمُ إِيمَانُ الْعَبْدِ انْطِلَاقًا مِنَ الْحَدِيثِ الثَّانِي"),
    ("q4", "ثَلَاثَةَ مَظَاهِرَ لِلِاسْتِقَامَةِ"),
    ("q5", "أَخْتَارُ مِنَ الْحَدِيثِ الثَّالِثِ قِيمَتَيْنِ"),
    ("q5 table head", "اقْتِرَاحُ سُلُوكَاتٍ لِتَطْبِيقِهَا فِي الْوَاقِعِ"),
    ("nachat3 item1 dars", "أَسْتَثْمِرُ مُكْتَسَبَاتِي مِنَ الدَّرْسِ وَأَمْلَأُ الْجَدْوَلَ"),
    ("table1 head", "الْمَوَاقِفُ وَالسُّلُوكَاتُ"),
    ("table1 head2", "مَوْقِفِي مِنْهَا مَعَ التَّعْلِيلِ"),
    ("table1 row1", "أَحْرِصُ عَلَى النَّوَافِلِ لِتَزْكِيَةِ النَّفْسِ"),
    ("table1 row2", "تَقْدِيمُ الْهَدَايَا لِلْأَصْدِقَاءِ فِي مُخْتَلَفِ الْمُنَاسَبَاتِ"),
    ("table1 row3 iʿtiyad", "اعْتِيَادُ التَّلَفُّظِ بِالْكَلَامِ الْفَاحِشِ"),
    ("table1 row4", "تَرْكُ الْعَمَلِ بِدَعْوَى الزُّهْدِ"),
    ("nachat3 item2 tadammanat", "تَضَمَّنَتْ أَحَادِيثُ الدُّرُوسِ السَّابِقَةِ مَجْمُوعَةً مِنَ الْأَخْلَاقِ الْحَسَنَةِ وَالْقِيمِ النَّبِيلَةِ"),
    ("table2 head3 thamarat", "ثَمَرَاتُ التَّحَلِّي بِهَا"),
    ("table2 row1", "«ازْهَدْ فِي الدُّنْيَا يُحِبَّكَ اللهُ»"),
    ("table2 row2", "«كُفَّ عَلَيْكَ هَذَا» وَأَشَارَ بِيَدِهِ إِلَى لِسَانِهِ"),
    ("table2 row3", "«لَا ضَرَرَ وَلَا ضِرَارَ»"),
    ("nachat4 titre", "عَرْضُ الْمَطْوِيَّةِ الْمُنْجَزَةِ بِعُنْوَانِ: «أَنْوَاعُ الْحُقُوقِ فِي الْإِسْلَامِ»"),
    ("nachat4 etape3 aqtarih", "أَقْتَرِحُ وَأُنَاقِشُ"),
    ("idad munakar", "وَأَبْحَثُ عَنْ تَعْرِيفٍ لِلْمُنْكَرِ، وَأُحَدِّدُ مَرَاتِبَ تَغْيِيرِهِ"),
]

ABSENT = [
    ("الشرك (adjudiqué الشر, tesseract ×5 + canon alsunniah)", "الشِّرْكِ"),
    ("السوء (variante Ityāf, non imprimée)", "السُّوءَ"),
    ("6608 (chiffres inversés couche IA)", "6608"),
    ("Q3 الثالث (rejeté, 3 témoins الثاني)", "انْطِلَاقًا مِنَ الْحَدِيثِ الثَّالِثِ"),
    ("أعمال (hallucination VLM rangée)", "أَعْمَال"),
    ("النميمة (hallucination VLM rangée)", "النَّمِيمَة"),
    ("كاره (hallucination VLM mot الشرك)", "كَارَه"),
    ("اجتناب rangée 3 (rejeté, tesseract ×5 اعتياد)", "اجْتِنَابُ التَّلَفُّظِ"),
    ("أطبق (L7, différent ici)", "أُطَبِّقَ"),
    ("الآتية (rejeté pour أعلاه)", "الْأَحَادِيثَ الْآتِيَةَ"),
    ("من الدروس (item 1 نشاط 3 — le singulier est imprimé)", "مِنَ الدُّرُوسِ وَأَمْلَأُ"),
]

fails = 0
for name, s in PRESENT:
    if s not in H:
        print(f"ÉCHEC présence [{name}] : {s[:60]}")
        fails += 1
for name, s in ABSENT:
    if s in H:
        print(f"ÉCHEC absence [{name}] : {s[:60]} trouvé à tort")
        fails += 1

n_ar = len(re.findall(r"[\u0600-\u06FF]", re.sub(r'<span[^>]*dir="rtl"[^>]*>.*?</span>', '', H, flags=re.S)))
n_ap = re.sub(r'<span[^>]*dir="rtl"[^>]*>.*?</span>', '', H, flags=re.S).count("'")
if n_ar or n_ap:
    print(f"ÉCHEC doctrine FR-seule : arabe hors span={n_ar}, apostrophe droite={n_ap}")
    fails += 1
if H.count("«") != H.count("»"):
    print(f"ÉCHEC guillemets : {H.count('«')}« / {H.count('»')}»")
    fails += 1

print(f"\n{len(PRESENT)} contrôles présence + {len(ABSENT)} absence — "
      f"{'TOUT PASS' if fails == 0 else str(fails) + ' ÉCHEC(S)'} — {len(H)} car")
sys.exit(1 if fails else 0)
