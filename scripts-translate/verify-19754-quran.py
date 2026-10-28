#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérifications coraniques du doc 19754 (rasm-wa-dabt-4ep, chapitre du tāʾ, suite).

Le doc enseigne :
  (1) élidées restantes : بُهْتَان (3 cas), dérivés de اِسْتِيذَان (māḍin + muḍāriʿ)
  (2) DUEL MÉDIAL élidée : مُدْهَمَّتَانِ, نَضَّاخَتَانِ, وَامْرَأَتَانِ, الْفِئَتَانِ (4 mots en images)
  (3) THĀBITA à l'extrémité : كِلْتَا (le mot) + le duel à l'extrémité (l'aṣl — 2 exemples)
  (4) dessinées au YĀʾ : حَتَّى, مَتَى, أَتَى, ءَاتَى, شَتَّى, فَتَىً
  (5) ISTITIMĀR (al-Ḫabbāz) : l'alif maqṣūra MUNAWWANA — فَتىً ضُحىً غُزّىً مُفْتَرىً
      مَوْلىً هُدىً سِوىً سُدىً مُصَلّىً قُرىً أَذىً مُصَفّىً مَثْوىً عَمىً تَتْراً
"""
import json
import re

C = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json"))
HARAKAT = re.compile(r"[\u064B-\u0652\u0653-\u0655\u0670\u06D6-\u06ED\u08F0-\u08F3]")

def strip(s):
    return HARAKAT.sub("", s).replace("\u0640", "")

def raw_search(pat_harak, label):
    """Recherche dans le texte HARAKATÉ (formes exactes)."""
    hits = []
    for s, obj in C.items():
        for n, t in obj["ar"]:
            if pat_harak in t:
                idx = t.find(pat_harak)
                hits.append((s, n, t, idx))
    print(f"   [{label}] {len(hits)} hit(s) — formes harakatées :")
    shown = 0
    for s, n, t, idx in hits:
        if shown >= 8:
            break
        print(f"     [{s}:{n}] …{t[max(0,idx-30):idx+30]}…")
        shown += 1
    return hits

def plain_search(pat_plain, label, limit=8, ctx=25):
    hits = []
    for s, obj in C.items():
        for n, t in obj["ar"]:
            st = strip(t)
            if pat_plain in st:
                hits.append((s, n, t, st, st.find(pat_plain)))
    print(f"   [{label}] {len(hits)} hit(s) — textes :")
    for s, n, t, st, idx in hits[:limit]:
        print(f"     [{s}:{n}] …{st[max(0,idx-ctx):idx+len(pat_plain)+ctx]}…")
    return hits

print("=" * 70)
print("A. بُهْتَان — lexème ب-ه-ت (les 3 cas revendiqués)")
plain_search("بفتان", "بُهْتَان (PLEINE)")
raw_search("بُهْتَٰ", "بُهْتَٰ (susCRITE)")

print("=" * 70)
print("B. Famille اِسْتِيذَان / اِسْتِئْذَان et dérivés")
plain_search("استيذان", "اِسْتِيذَان (yāʾ)")
plain_search("استئذان", "اِسْتِئْذَان (hamza)")
plain_search("ستاذن", "استأذن (dérivés)")
plain_search("ستاذ", "…ستاذ (élidée ?)")
plain_search("فل يسن", "فَلْيَسْتَأْذِنُوا (24:59)")
raw_search("تَسْتَأْذِن", "تَسْتَأْذِن")
raw_search("يَسْتَأْذِن", "يَسْتَأْذِن")
raw_search("اسْتَأْذَنَ", "اسْتَأْذَنَ (māḍin)")

print("=" * 70)
print("C. DUEL MÉDIAL — les quatre mots revendiqués")
plain_search("مدهمتن", "مُدْهَمَّتَانِ")
plain_search("نداختن", "نَضَّاخَتَانِ")
plain_search("امرأتن", "امْرَأَتَانِ (stripped commun)")
raw_search("امْرَأَتَا", "امْرَأَتَا (PLEINE)")
raw_search("امْرَأَتَٰ", "امْرَأَتَٰ (susCRITE)")
plain_search("فئتا", "فِئَتَان (PLEINE, stripped)")
raw_search("فِئَتَا", "فِئَتَا harakaté")

print("=" * 70)
print("D. كِلْتَا — le mot (alif de l'extrémité MAINTENUE ?)")
plain_search("كلتا", "كِلْتَا (stripped)")
raw_search("كِلْتَا", "كِلْتَا (PLEINE)")

print("=" * 70)
print("E. Dessinées au YĀʾ — comptages")
for pat, label in [("حتم", "حَتَّى"), ("متى", "مَتَى"), ("شتم", "شَتَّى"),
                   ("اتى", "أَتَى / آتَى / ءَاتَى"), ("فتى", "فَتَى")]:
    cnt = 0
    for s, obj in C.items():
        for n, t in obj["ar"]:
            if pat in strip(t):
                cnt += 1
    print(f"   [{label}] stripped «{pat}» : {cnt} vers")

print("=" * 70)
print("F. ISTITIMĀR al-Ḫabbāz — l'alif maqṣūra MUNAWWANA au corpus")
for pat, label in [("فتى", "فَتًى ?"), ("ضحا", "ضُحًى ?"), ("ضحى", "ضُحًى (variant)"),
                   ("غزى", "غُزًّى ?"), ("مفتا", "مُفْتَرًى ?"), ("مفتى", "مُفْتَرًى (2)"),
                   ("مولى", "مَوْلًى ?"), ("مولا", "مَوْلًى (2)"), ("هدى", "هُدًى ?"),
                   ("هدا", "هُدًى (2)"), ("سوى", "سِوىً ?"), ("سوا", "سَوَاءً ?"),
                   ("سدى", "سُدًى ?"), ("سدا", "سُدًى (2)"), ("مصلى", "مُصَلًّى ?"),
                   ("مصلا", "مُصَلًّى (2)"), ("قرى", "قُرًى ?"), ("قرا", "قُرًى (2)"),
                   ("اذى", "أَذًى ?"), ("اذا", "أَذًى (2)"), ("مصفى", "مُصَفًّى ?"),
                   ("مثوى", "مَثْوًى ?"), ("مثوا", "مَثْوًى (2)"), ("عمى", "عَمًى ?"),
                   ("عما", "عَمًى (2)"), ("تترا", "تَتْرًا ?")]:
    cnt = 0
    samples = []
    for s, obj in C.items():
        for n, t in obj["ar"]:
            st = strip(t)
            if pat in st:
                cnt += 1
                if len(samples) < 3:
                    idx = st.find(pat)
                    samples.append(f"[{s}:{n}] …{st[max(0,idx-18):idx+20]}…")
    print(f"   [{label}] «{pat}» : {cnt} vers")
    for x in samples:
        print(f"      {x}")

print("=" * 70)
print("G. Duel à l'extrémité (l'aṣl) — les duels fin de vers (contexte جنتان déjà relevés R332)")
for s, n in (("55", 46), ("55", 62), ("34", 15), ("3", 122), ("49", 9), ("5", 64), ("18", 33)):
    obj = C[s]
    for nn, t in obj["ar"]:
        if nn == n:
            print(f"   [{s}:{n}] {t[-90:] if n in (46, 62) else t[:110]}")
