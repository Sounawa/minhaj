#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sondes 2 — doc 19759 : patterns élargis (dagger \u0670, wasla \u0671) + contextes de versets pivots."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE, encoding="utf-8"))

HARAKAT = re.compile(r"[\u064B-\u0655\u0640]")
DAGGER = "\u0670"
ALIF = "ا"

def strip_h(s):
    return HARAKAT.sub("", s)

def form_of(w):
    sw = strip_h(w)
    if DAGGER in w:
        return "SUSCRITE"
    if ALIF in sw:
        return "PLEINE"
    return "absente"

def count_lexeme(label, pattern, limit=10):
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

def verse(label, sn, an):
    sd = data.get(str(sn))
    if not sd:
        print(f"\n--- {label} {sn}:{an} — sourate absente du cache")
        return
    for num, text in sd["ar"]:
        if num == an:
            print(f"\n--- {label} {sn}:{an} ---")
            print("   ", text)
            for w in text.split():
                print(f"      {form_of(w):8} {w}")
            return
    print(f"\n--- {label} {sn}:{an} — ayat non trouvée")

# 1. مِيثَاق — pattern élargi (dagger possible après ث)
count_lexeme("1. ميثاق élargi: م ي ث [ا/0670] ق", r"\u0645\u064A\u062B[\u0627\u0670]\u0642")

# 2. أَوْثَان — élargi
count_lexeme("2. أوثان élargi: [أو] و ث [ا/0670] ن", r"[\u0623\u0627]?\u0648\u062B[\u0627\u0670]\u0646")

# 3. نَفَّاثَات — élargi
count_lexeme("3. نفاثات élargi: ن ف [ا/0670]? ث", r"\u0646\u0641[\u0627\u0670]?\u062B")

# 4. أَثَرَة — élargi (ث ر ة/ت)
count_lexeme("4. أثرة élargi: [أا]? ث ر", r"[\u0623\u0627]?\u062B\u0631")

# 5. أَثَاث — élargi
count_lexeme("5. أثاث élargi: [أا] ث [ا/0670]? ث", r"[\u0623\u0627]\u062B[\u0627\u0670]?\u062B")

# 6. Contextes pivots
verse("6a. يَسْتَغِيثَانِ — lieu du duel", 46, 17)
verse("6b. خَبِيثَٰتُ — PFS", 24, 26)
verse("6c. أَمْثَلُهُمْ — DEPUIS Maryam", 20, 104)
verse("6d. ثُلُثَا — l'alif après thāʾ", 4, 11)
verse("6e. الثُّلُثَانِ — le duel", 4, 176)
verse("6f. أَثَرِ الرَّسُولِ", 20, 96)
verse("6g. أَثَرِ السُّجُودِ", 48, 29)
verse("6h. ءَاثَرَكَ", 12, 91)
verse("6i. وَءَاثَرَ", 79, 38)
verse("6j. 20:84 (أَثَرِى ?)", 20, 84)
