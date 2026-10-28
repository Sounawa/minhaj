#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Suivi 19754 : أذن, maqṣūra brutes, istitmār restant, duel امرأة."""
import json
import re

C = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json"))
HARAKAT = re.compile(r"[\u064B-\u0652\u0653-\u0655\u0670\u06D6-\u06ED\u08F0-\u08F3]")

def strip(s):
    return HARAKAT.sub("", s).replace("\u0640", "")

def raw_search(pat, label, limit=10, ctx=32):
    hits = []
    for s, obj in C.items():
        for n, t in obj["ar"]:
            if pat in t:
                hits.append((s, n, t, t.find(pat)))
    print(f"   [{label}] {len(hits)} hit(s)")
    for s, n, t, idx in hits[:limit]:
        print(f"     [{s}:{n}] …{t[max(0,idx-ctx):idx+len(pat)+ctx]}…")
    return hits

print("=" * 70)
print("A. Racine أ-ذ-ن (استأذن/يستأذن/يؤذن) — formes HAMZA du corpus")
raw_search("تَأْذِن", "…تَأْذِن (استأذن family)")
raw_search("يُؤْذَن", "يُؤْذَن (passif)")
raw_search("أَذِنَ", "أَذِنَ (māḍin nu)")

print("=" * 70)
print("B. Maqṣūra brutes — أَتَى / ءَاتَى / آتَى / حَتَّى / شَتَّى / فَتًى")
raw_search("أَتَىٰ", "أَتَىٰ (suscr. après ى)")
raw_search("ءَاتَىٰ", "ءَاتَىٰ")
raw_search("ءَاتَى", "ءَاتَى (toutes)")
raw_search("آتَىٰ", "آتَىٰ")
raw_search("حَتَّىٰ", "حَتَّىٰ (exemples)")
raw_search("شَتَّىٰ", "شَتَّىٰ")
raw_search("فَتً", "فَتًى (tanwīn absolu)")

print("=" * 70)
print("C. ISTITIMĀR — mots restants")
raw_search("أَذً", "أَذًى (tanwīn)")
raw_search("مُصَفًّ", "مُصَفًّى")
raw_search("مَثْوً", "مَثْوًى")
raw_search("عَمً", "عَمًى (tanwīn)")
raw_search("تَتْرً", "تَتْرًا")
raw_search("مَوْلً", "مَوْلًى (tanwīn absolu)")
raw_search("ضُحً", "ضُحًى")
raw_search("هُدً", "هُدًى (tanwīn — échantillon)")
raw_search("قُرً", "قُرًى (tanwīn)")
raw_search("سَوَاءً", "سَوَاءً (tanwīn, dessin hamza)")

print("=" * 70)
print("D. Duel امرأة — toutes formes stripped")
hits = []
for s, obj in C.items():
    for n, t in obj["ar"]:
        st = strip(t)
        for m in re.finditer("امرأت", st):
            hits.append((s, n, st[max(0,m.start()-15):m.start()+18]))
print(f"   [امرأت stripped] {len(hits)} hit(s) — échantillon :")
seen = set()
for s, n, ctx in hits:
    key = ctx[-6:]
    if key not in seen:
        seen.add(key)
        print(f"     [{s}:{n}] …{ctx}…")
    if len(seen) > 10:
        break
print("   --- formes DUELLES (امرأتم / امرأتن / امرأتا) ---")
for pat, lab in [("امرأتم", "امْرَأَتَاهُ (duel+hu)"), ("امرأتن", "امْرَأَتَانِ absolu"),
                 ("امرأتين", "امْرَأَتَيْنِ"), ("امرأتا", "امْرَأَتَا nu")]:
    cnt = 0
    for s, obj in C.items():
        for n, t in obj["ar"]:
            if pat in strip(t):
                cnt += 1
    print(f"   [{lab}] : {cnt}")

print("=" * 70)
print("E. يَحَسْرَتَى et مُدْهَمَّتَانِ/نَضَّاخَتَانِ — absence confirmée")
for pat, lab in [("حسرتى", "يَحَسْرَتَى ?"), ("مدهمتن", "مُدْهَمَّتَانِ ?"),
                 ("نداختن", "نَضَّاخَتَانِ ?"), ("استيذان", "اِسْتِيذَان ?"),
                 ("مفتا", "مُفْتَرًى ?"), ("غزى", "غُزًّى 3:156 — texte"), ]:
    cnt = 0
    for s, obj in C.items():
        for n, t in obj["ar"]:
            if pat in strip(t):
                cnt += 1
                if lab.endswith("texte") or pat == "غزى":
                    idx = strip(t).find(pat)
                    print(f"     [{s}:{n}] …{strip(t)[max(0,idx-30):idx+25]}…")
    print(f"   [{lab}] : {cnt}")

print("=" * 70)
print("F. 24:59 et 24:62 — les dérivés d'استيذان (images de l'analyse)")
for s, n in (("24", 59), ("24", 62), ("24", 27)):
    obj = C[s]
    for nn, t in obj["ar"]:
        if nn == n:
            print(f"   [{s}:{n}] {t[:150]}")

print("=" * 70)
print("G. Les « ثَابِتَة » de l'extrémité — le duel fin de propos au corpus")
print("   (جَنَّتَانِ 55:46/62 et 34:15 déjà relevés — 55:46/62 en FIN de vers)")
obj = C["18"]
for nn, t in obj["ar"]:
    if nn == 33:
        print(f"   [18:33] {t[:120]}")
