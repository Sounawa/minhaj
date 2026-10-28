#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translittération des citations arabes des fragments 19769 (convention 0-arabe du livre)."""
import re

# Table: arabe exact -> translittération (dessin -> latin académique)
T = {
    "قَالُوا۟ لَا تَخَفْ": "qālū lā taḫaf",
    "تَخَافْ": "taḫāf",
    "بِخَٰزِنِينَ": "bi-ḫāzinīna",
    "شَٰمِخَٰتٍۢ": "šāmiḫātin",
    "بِخَٰرِجِينَ": "bi-ḫāriǧīna",
    "وَمَا هُم بِخَٰرِجِينَ مِنَ ٱلنَّارِ": "wa-mā hum bi-ḫāriǧīna mina n-nāri",
    "وَمَا هُم بِخَٰرِجِينَ مِنْهَا": "wa-mā hum bi-ḫāriǧīna minhā",
    "بِخَارِجٍۢ": "bi-ḫāriǧin",
    "لَيْسَ بِخَارِجٍۢ مِّنْهَا": "laysa bi-ḫāriǧin minhā",
    "خَاسِرَةٌۭ": "ḫāsiratun",
    "قَالُوا۟ تِلْكَ إِذًۭا كَرَّةٌ خَاسِرَةٌۭ": "qālū tilka iḏan karratun ḫāsiratun",
    "خَسِرُوٓا۟": "ḫasirū",
    "خَٰسِرُونَ": "ḫāsirūna",
    "خَٰسِرِينَ": "ḫāsirīna",
    "خَاسِئًۭا": "ḫāsiʾan",
    "خَاسِرَانِ": "ḫāsirāni",
    "خَسِئَانَ": "ḫasaʾāni",
    "خَٰلِدَيْنِ فِيهَا": "ḫālidayni fīhā",
    "خَٰلِدَيْنِ": "ḫālidayni",
    "فَكَانَ عَٰقِبَتَهُمَآ أَنَّهُمَا فِى ٱلنَّارِ خَٰلِدَيْنِ فِيهَا": "fa-kāna ʿāqibatahumā annahumā fī n-nāri ḫālidayni fīhā",
    "وَلَا تُخَٰطِبْنِى فِى ٱلَّذِينَ ظَلَمُوٓا۟ ۚ إِنَّهُم مُّغْرَقُونَ": "wa-lā tuḫāṭibnī fī llaḏīna ẓalamū innahum muġraqūna",
    "وَلَا تُخَٰطِبْنِى فِى ٱلَّذِينَ ظَلَمُوٓا۟": "wa-lā tuḫāṭibnī fī llaḏīna ẓalamū",
    "تُخَٰطِبْنِى": "tuḫāṭibnī",
    "تُخَافِتْ": "tuḫāfit",
    "وَلَا تُخَافِتْ بِهَا": "wa-lā tuḫāfit bihā",
    "يَتَخَٰفَتُونَ بَيْنَهُمْ إِن لَّبِثْتُمْ إِلَّا عَشْرًۭا": "yataḫāfatūna baynahum in labiṯtum illā ʿašran",
    "فَٱنطَلَقُوا۟ وَهُمْ يَتَخَٰفَتُونَ": "fa-nṭalaqū wa-hum yataḫāfatūna",
    "يَتَخَٰفَتُونَ": "yataḫāfatūna",
    "خَٰطِئِينَ": "ḫāṭiʾīna",
    "خَٰطِـِٔينَ": "ḫāṭiʾīna",
    "خَاطِئَةٌۢ": "ḫāṭiʾatun",
    "نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ": "nāṣiyatin kāḏibatin ḫāṭiʾatun",
    "بِٱلْخَاطِئَةِ": "bi-l-ḫāṭiʾati",
    "وَجَآءَ فِرْعَوْنُ وَمَن قَبْلَهُۥ وَٱلْمُؤْتَفِكَٰتُ بِٱلْخَاطِئَةِ": "wa-ǧāʾa firʿawnu wa-man qablahū wa-l-muʾtafikātu bi-l-ḫāṭiʾati",
    "إِنَّكِ كُنتِ مِنَ ٱلْخَاطِـِٔينَ": "inna ki kunti mina l-ḫāṭiʾīna",
    "لَخَٰطِـِٔينَ": "la-ḫāṭiʾīna",
    "أَحْسَنُ ٱلْخَٰلِقِينَ": "aḥsanu l-ḫāliqīna",
    "خَٰشِعُونَ": "ḫāšiʿūna",
    "خَٰشِعِينَ": "ḫāšiʿīna",
    "وَخَشَعَتِ": "wa-ḫašaʿati",
    "تَخْشَعَ": "taḫšaʿa",
    "خُشَّعًا": "ḫuššaʿan",
    "خَٰمِسَةُ": "ḫāmisatu",
    "خَٰمِسَةَ": "ḫāmisata",
    "وَمَا يَخْدَعُونَ إِلَّآ أَنفُسَهُمْ": "wa-mā yaḫdaʿūna illā anfusahum",
    "يُخَٰدِعُونَ": "yuḫādiʿūna",
    "خَٰدِعُهُمْ": "ḫādiʿuhum",
    "خَٰضِعِينَ": "ḫāḍiʿīna",
    "تَخْضَعْنَ": "taḫḍaʿna",
    "خَٰلِدٌۭ": "ḫālidun",
    "وَتَخَلَّتْ": "wa-taḫallat",
    "خَلَتْ": "ḫalat",
    "تُخَٰطِبْنِي": "tuḫāṭibnī",
    "الْخُلْدِ": "al-ḫuldi",
    "يَخْلُدْ": "yaḫlud",
    "تَخْلُدُونَ": "taḫludūna",
    "الْخَٰلِقِينَ": "al-ḫāliqīna",
    "الْخَٰلِقِينَ": "al-ḫāliqīna",
}

import glob
for f in sorted(glob.glob("/home/z/my-project/tr-tmp/fr19769_*.html")):
    h = open(f, encoding="utf-8").read()
    before = len(re.findall(r"[\u0600-\u06FF]", h))
    # tri par longueur décroissante pour éviter les remparts partiels
    for k in sorted(T, key=len, reverse=True):
        h = h.replace(k, T[k])
    after = len(re.findall(r"[\u0600-\u06FF]", h))
    open(f, "w", encoding="utf-8").write(h)
    print(f"{f}: {before} -> {after} arabes")

# --- passe 2 : résidus ---
T2 = {
    "أَنْ أَتَمَثَّلَ قِيمَةَ الْحِفَاظِ عَلَى رَسْمِ الْقُرْءَانِ الْكَرِيمِ": "an atamattala qīmata l-ḥifāẓi ʿalā rasmi l-Qurʾāni l-karīmi",
    "وَلَا تَخَفْ": "wa-lā taḫaf",
    "تَخَفْ": "taḫaf",
    "وَلَا مُثَنَّى هُنَا فِي بَابِ الْخَاءِ": "wa-lā muṯannā hunā fī bābi l-ḫāʾi",
    "بَابِ الْخَاءِ": "bābi l-ḫāʾi",
    "خَمْسَةٌۭ": "ḫamsatun",
    "خ‌ط‌ئ": "ḫ-ṭ-ʾ",
    "يَخْدَعُونَ": "yaḫdaʿūna",
    "سِوَى الَّذِي بِأَوَّلِ سُورَةِ يُوسُفَ": "siwā llaḏī bi-ʾawwali sūrati Yūsuf",
    "فَهُوَ بِالثَّبْتِ": "fa-huwa bi-ṯ-ṯubti",
    "لَيْسَ بِخَارِجٍ": "laysa bi-ḫāriǧin",
    "أَخْلَدَهُۥ": "ʾaḫladahū",
    "أَخْلَدَ": "ʾaḫlada",
    "مُّخَلَّدُونَ": "muḫalladūna",
    "تُخَطِبْـنِي": "tuḫaṭibnī",
    "خ‌ل‌د": "ḫ-l-d",
}
for f in sorted(glob.glob("/home/z/my-project/tr-tmp/fr19769_*.html")):
    h = open(f, encoding="utf-8").read()
    before = len(re.findall(r"[\u0600-\u06FF]", h))
    for k in sorted(T2, key=len, reverse=True):
        h = h.replace(k, T2[k])
    after = len(re.findall(r"[\u0600-\u06FF]", h))
    open(f, "w", encoding="utf-8").write(h)
    print(f"{f}: {before} -> {after} arabes")
