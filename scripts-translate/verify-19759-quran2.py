#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérifications coraniques du doc 19759 — passe 2 (patterns hamza + U+0671 corrigés)."""
import json
import re

C = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json"))
HARAKAT = re.compile(r"[\u064B-\u0652\u0653-\u0655\u0670\u06D6-\u06ED\u08F0-\u08F3]")

def strip(s):
    return HARAKAT.sub("", s).replace("\u0640", "")

def raw_verse(s, n, label):
    try:
        for nn, t in C[s]["ar"]:
            if nn == n:
                print(f"   [{label}] [{s}:{n}] {t}")
                return
    except KeyError:
        pass
    print(f"   [{label}] [{s}:{n}] — introuvable")

def plain_search(pat_plain, label, limit=15, ctx=30):
    hits = []
    for s, obj in C.items():
        for n, t in obj["ar"]:
            st = strip(t)
            if pat_plain in st:
                hits.append((s, n, t, st, st.find(pat_plain)))
    print(f"   [{label}] {len(hits)} hit(s) :")
    for s, n, t, st, idx in hits[:limit]:
        print(f"     [{s}:{n}] …{st[max(0,idx-ctx):idx+len(pat_plain)+ctx]}…")
    return hits

print("=" * 70)
print("A. Famille ءاثر — formes harakatées complètes (9 positions)")
for s, n in (("5", 46), ("12", 91), ("18", 6), ("30", 50), ("36", 12), ("37", 70),
             ("43", 22), ("43", 23), ("57", 27), ("79", 38)):
    raw_verse(s, n, "ءاثر")

print("=" * 70)
print("B. أمثل / أمثال — patterns à hamza (U+0623 / ء)")
plain_search("أمثل", "أَمْثَل (hamza, large)")
plain_search("ءمثل", "ءَمْثَل (hamza ض)")

print("=" * 70)
print("C. أَثَابَ — أثب du vers deux (patterns hamza)")
plain_search("أثاب", "أَثَابَ (hamza)")
plain_search("ءثاب", "ءَثَابَ (hamza ض)")
plain_search("ثاب", "…ثاب (large)")

print("=" * 70)
print("D. أَثَاث — toutes les positions (raw suscrite déjà : 16:80) + raws")
plain_search("أثاث", "أَثَاث (hamza)")
for s, n in (("16", 80),):
    raw_verse(s, n, "أثاث")

print("=" * 70)
print("E. النَّفَّٰثَٰتِ — 113:4 (alifs suscrites ?)")
plain_search("نفث", "نَفَّٰثَٰت (stripped)")
raw_verse("113", 4, "113:4")

print("=" * 70)
print("F. ثُلُثَا 4:11 / الثُّلُثَانِ 4:176 — raws")
raw_verse("4", 11, "4:11")
raw_verse("4", 176, "4:176")

print("=" * 70)
print("G. يَسْتَغِيثَانِ 46:17 + الْخَبِيثَٰتُ 24:26 — raws")
raw_verse("46", 17, "46:17")
raw_verse("24", 26, "24:26")

print("=" * 70)
print("H. نَرَى اللَّهَ 2:55 + نَحْوَ الْهُدَى — patterns larges")
plain_search("نرى", "…نرى (stripped)")
plain_search("الهدى", "…الهدى (stripped — contient نحو الهدى ?)")
plain_search("نحو", "…نحو (stripped)")

print("=" * 70)
print("I. 46:4 (أَثَٰرَةٍ) + 29:17 + 29:25 + 22:30 (أَوْثَٰن) — raws")
raw_verse("46", 4, "46:4")
raw_verse("29", 17, "29:17")
raw_verse("29", 25, "29:25")
raw_verse("22", 30, "22:30")

print("=" * 70)
print("J. ISTITIMĀR — ذِكْرَى ٱلدَّارِ 38:46 + les maqṣūrāt à sukūn suivant ?")
raw_verse("38", 46, "38:46")
