#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérifications coraniques du doc 19759 — passe 3 (raws دقيقة)."""
import json
import re

C = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json"))
HARAKAT = re.compile(r"[\u064B-\u0652\u0653-\u0655\u0670\u06D6-\u06ED\u08F0-\u08F3]")

def strip(s):
    return HARAKAT.sub("", s).replace("\u0640", "")

print("=" * 70)
print("A. RAW des 12 positions أَمْثَل / أَمْثَال (dessins)")
pats = ("أمثل", "ءمثل")
for s, obj in C.items():
    for n, t in obj["ar"]:
        st = strip(t)
        if any(p in st for p in pats):
            # extraire le mot porteur
            idx = min((st.find(p) for p in pats if p in st), key=abs)
            print(f"   [{s}:{n}] …{st[max(0,idx-20):idx+24]}…")
            print(f"      RAW: …{t[max(0,idx-30):idx+40]}…")

print("=" * 70)
print("B. مِيثَاق — la LISTE COMPLÈTE des 16 (suscrites toutes ?)")
cnt = 0
for s, obj in C.items():
    for n, t in obj["ar"]:
        if "مِيثَٰق" in t:
            cnt += 1
            print(f"   {cnt:2d}. [{s}:{n}] مِيثَٰق présent — suscrite")
        elif strip(t).find("ميثاق") >= 0:
            cnt += 1
            print(f"   {cnt:2d}. [{s}:{n}] مِيثَاق — PLEINE ?! RAW: {t[:80]}")
print(f"   TOTAL: {cnt}")

print("=" * 70)
print("C. أثب — racine ء-ث-ب : zéro ancrage ? (patterns larges)")
pats2 = ("أتب", "ءتب", "أثب", "ءثب", "اثب", "يؤثب", "أتثب")
for s, obj in C.items():
    for n, t in obj["ar"]:
        st = strip(t)
        for p in pats2:
            if p in st:
                print(f"   [{s}:{n}] «{p}» — {st[max(0,st.find(p)-25):st.find(p)+25]}")
print("   (fin recherche أثب)")

print("=" * 70)
print("D. ثَاء + dual + extrémité — recontrôle complet des ثلث raws")
for s, obj in C.items():
    for n, t in obj["ar"]:
        st = strip(t)
        if "ثلث" in st and ("ثلثا" in st or "ثلثان" in st):
            idx = st.find("ثلث")
            print(f"   [{s}:{n}] …{st[max(0,idx-18):idx+22]}…")
            print(f"      RAW: …{t[max(0,idx-25):idx+35]}…")

print("=" * 70)
print("E. Les 6 positions kasra de ءَاثَٰرِهِم — dessin hamza-alif COMPLET partout ?")
for s, n in (("5", 46), ("18", 6), ("37", 70), ("43", 22), ("43", 23), ("57", 27)):
    for nn, t in C[s]["ar"]:
        if nn == n:
            seg = "ءاث" 
            i = t.find(seg)
            print(f"   [{s}:{n}] RAW word: {t[i:i+14]}")
