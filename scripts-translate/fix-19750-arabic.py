#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translittération des citations arabes des fragments fr19750_* (convention :
0 caractère arabe résiduel dans la leçon livrée)."""
import re

MAP = [
    # 4. chaîne de Warš et pluriels
    ("وَلَا مُسْتَـْٔنِسِينَ لِحَدِيثٍ", "wa-lā mustaʾnisīna li-ḥadīṯin"),
    ("مُسْتَـْٔنِسِينَ", "mustaʾnisīna"),
    ("مُسْتَانِسِينَ", "mustānisīna"),
    ("مُسْتَنِسِينَ", "mustanisīna"),
    ("مُّؤْمِنَٰتٍۢ قَٰنِتَٰتٍۢ تَٰٓئِبَٰتٍ", "muʾminātin qānitātin tāʾibātin"),
    ("قَٰنِتَٰتٍ", "qānitātin"),
    ("تَٰٓئِبَٰتٍ", "tāʾibātin"),
    ("قَٰنِتًا", "qānitan"),
    ("ٱلتَّائِبُونَ", "at-tāʾibūna"),
    ("تَّائِبُونَ", "tāʾibūna"),
    ("تَـئِبُونَ", "tāʾibūna"),
    ("مُتَتَابِعِينَ", "mutatābiʿīna"),
    # 2. kitāb — formes pleines (15:4, 18:27, 13:38, 27:1)
    ("وَلَهَا كِتَابٌۭ مَّعْلُومٌۭ", "wa-lahā kitābun maʿlūm"),
    ("مِن كِتَابِ رَبِّكَ", "min kitābi rabbika"),
    ("لِكُلِّ أَجَلٍۢ كِتَابٌۭ", "li-kulli aǧalin kitābun"),
    ("وَكِتَابٍۢ مُّبِينٍ", "wa-kitābin mubīn"),
    # kitāb — suscrites et générique
    ("كِتَٰبٍۢ", "kitābin"),
    ("كِتَٰب", "kitāb"),
    ("كِتَب", "kitāb"),
    ("ٱلْكِتَٰبِ 2:2", "al-kitābi 2:2"),
    ("كِتَٰبٍ 2:89", "kitābin 2:89"),
    # 1. ḫitām / matāʿ / ḫatama
    ("خِتَٰمُهُۥ مِسْكٌ", "ḫitāmuhu misK"),
    ("خِتَٰمُهُ", "ḫitāmuhu"),
    ("مَتَٰعًا/مَتَٰعٌ", "matāʿan/matāʿun"),
    ("مَتَٰعًا", "matāʿan"),
    ("مَتَٰعٌ", "matāʿun"),
    ("مَتَاعَانِ", "matāʿāni"),
    ("خَتَمَ", "ḫatama"),
    ("نَخْتِمُ", "naḫtimu"),
    ("يَخْتِمْ", "yaḫtimu"),
    # duels
    ("جَنَّتَانِ", "ǧannatāni"),
    ("مَبْسُوطَتَانِ", "mabsūṭatāni"),
    ("فَخَانَتَاهُمَا", "fa-ḫānatāhumā"),
    ("طَائِفَتَانِ", "ṭāʾifatāni"),
    # morphologie
    ("تَائِبُونَ", "tāʾibūna"),
    ("مُسْتَأْنِسِينَ", "mustaʾnisīna"),
    ("فَعَالَة", "faʿāla"),
]

import io
total = 0
for i in range(1, 6):
    p = f"/home/z/my-project/tr-tmp/fr19750_{i}.html"
    h = open(p, encoding="utf-8").read()
    n = 0
    for ar, tr in MAP:
        if ar in h:
            n += h.count(ar)
            h = h.replace(ar, tr)
    open(p, "w", encoding="utf-8").write(h)
    ar_left = len(re.findall(r"[\u0600-\u06FF]", h))
    print(f"fr19750_{i}.html : {n} remplacements, AR restants = {ar_left}")
    total += n
print("TOTAL remplacements:", total)
