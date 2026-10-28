#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sondes coraniques — doc 19759 : fasil al-thāʾ (l'alif après le thāʾ).
Cache : scripts-translate/quran-cache.json — convention des tours R335-R337."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE, encoding="utf-8"))

HARAKAT = re.compile(r"[\u064B-\u0655\u0640]")
DAGGER = "\u0670"
ALIF = "ا"
YAA = "ي"
THA = "ث"

def strip_h(s):
    return HARAKAT.sub("", s)

def form_of(w):
    sw = strip_h(w)
    if DAGGER in w:
        return "SUSCRITE"
    if ALIF in sw:
        return "PLEINE"
    return "absente"

def count_lexeme(label, pattern, limit=8):
    print(f"\n=== {label} ===")
    rx = re.compile(pattern)
    tally = {"SUSCRITE": 0, "PLEINE": 0, "absente": 0}
    ex = {"SUSCRITE": [], "PLEINE": [], "absente": []}
    for snum, sdata in sorted(data.items(), key=lambda kv: int(kv[0])):
        for aynum, aytext in sdata["ar"]:
            for w in aytext.split():
                if rx.search(strip_h(w)):
                    f = form_of(w)
                    tally[f] += 1
                    if len(ex[f]) < limit:
                        ex[f].append(f"{snum}:{aynum} {w}")
    for f in ("SUSCRITE", "PLEINE", "absente"):
        if tally[f]:
            print(f"  {f}: {tally[f]}  ex: {' | '.join(ex[f][:limit])}")
    print(f"  TOTAL: {sum(tally.values())}")
    return ex

# 1. أَثَرَة / أَثْرَة (bi-hadhf al-alif) — bayt 1 + appareil I
count_lexeme("1a. أثرة (tharata, hamza initial)", r"\u0623\u062B\u0631\u0629|\u0623\u062B\u0631\u062A|\u0623\u062B\u0631\u062A\u064A|\u0623\u062B\u0631\u062A\u0647")
count_lexeme("1b. بثرة/أثرة toute racine ATH-R", r"\u062B\u0631\u0629")

# 2. مِيثَاق (mīthāq) — bayt 1
count_lexeme("2. ميثاق (mīthāq, toutes formes)", r"\u0645\u064A\u062B\u0627\u0642|\u0645\u064A\u062B\u0642")

# 3. أَوْثَان (awthān, pl. waṯan) — bayt 1
count_lexeme("3. أوثان (awthān)", r"\u0623\u0648\u062B\u0627\u0646|\u0623\u0648\u062B\u0646|\u0648\u062B\u0627\u0646")

# 4. نَفَّاثَات (113:4) — bayt 1
count_lexeme("4. نفاثات (naffāthāt)", r"\u0646\u0641\u0627\u062B|\u0646\u0641\u062B\u0627")

# 5. خَبِيث (khabīth, toutes formes) — bayt 2 + appareil
count_lexeme("5. خبيث (khabīth)", r"\u062E\u0628\u064A\u062B|\u062E\u0628\u064A")

# 6. يَسْتَغِيث (istaghātha) — bayt 2 + appareil
count_lexeme("6. استغاث (istaghātha)", r"\u0633\u062A\u063A\u064A\u062B|\u0633\u062A\u063A\u0627\u062B|\u0633\u063A\u064A\u062B")

# 7. ثُلُث (thuluth) — bayt 3 + appareil
count_lexeme("7. ثلث (thuluth, toutes formes)", r"\u062B\u0644\u062B|\u062B\u0644\u064A\u062B")

# 8. أَثَاث (athāth) — bayt 3
count_lexeme("8. أثاث (athāth)", r"\u0623\u062B\u0627\u062B|\u0623\u062B\u062B")

# 9. أَمْثَال / أَمْثَل (amthāl) — bayt 2 + PARTITION Maryam
print("\n=== 9. أمثل/أمثال avec partition Maryam (19) ===")
rx = re.compile(r"\u0623\u0645\u062B\u0644|\u0623\u0645\u062B\u0627\u0644|\u0623\u0645\u062B\u0644")
rows = []
for snum, sdata in sorted(data.items(), key=lambda kv: int(kv[0])):
    for aynum, aytext in sdata["ar"]:
        for w in aytext.split():
            if rx.search(strip_h(w)):
                rows.append((int(snum), aynum, w, form_of(w)))
for snum, aynum, w, f in rows:
    side = "DEPUIS Maryam" if snum >= 19 else "AVANT Maryam"
    print(f"  {snum}:{aynum} {f:8} {side:12} {w}")

# 10. أَثَر (athara) — bayt 1 « ءَاثرَ مَعْ هُمُ » + appareil III « أَثَرِ » muḍāf ilā هِم bi-kasr
print("\n=== 10. أثر/اثر (athara, toutes formes) ===")
rx = re.compile(r"\u0623\u062B\u0631|\u0627\u062B\u0631")
for snum, sdata in sorted(data.items(), key=lambda kv: int(kv[0])):
    for aynum, aytext in sdata["ar"]:
        for w in aytext.split():
            if rx.search(strip_h(w)):
                print(f"  {snum}:{aynum} {form_of(w):8} {w}")

# 11. ذِكْرَى (alif maqmūra) — istitimār : نرى الله وذكرى الدار
count_lexeme("11a. ذكرى (dhikrā)", r"\u0630\u0643\u0631\u0649|\u0630\u0643\u0631\u064A")
count_lexeme("11b. نرى (narā)", r"\u0646\u0631\u0649")

# 12. أَثَبَ — bayt 2 « الْخَبيِثتُ أَثَبْ » + appareil « أَثَـــبَ »
count_lexeme("12. أثب/وثب (a-tha-ba)", r"\u0623\u062B\u0628|\u0648\u062B\u0628|\u0623\u062B\u0627\u0628|\u0648\u062B\u0627\u0628")

# 13. LE LIEU UNIQUE : thāʾ + muṭannā mutaṭarrif (mot en ث + alif finale + sens duel)
print("\n=== 13. mots finissant par ث + ا/alif ===")
rx = re.compile(r"\u062B[\u0627\u0649]$")
for snum, sdata in sorted(data.items(), key=lambda kv: int(kv[0])):
    for aynum, aytext in sdata["ar"]:
        for w in aytext.split():
            if rx.search(strip_h(w)):
                print(f"  {snum}:{aynum} {form_of(w):8} {w}")

# 14. lūbāb — glose 1 (اللُّبَاب)
count_lexeme("14. لباب (lubbāb)", r"\u0644\u0628\u0627\u0628|\u0644\u0628\u0628")
