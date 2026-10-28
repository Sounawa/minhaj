#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérification coranique étendue — doc 19769 (rasm-wa-dabt-4ep, chapitre du ḫāʾ).
Sondes tolérantes (harakat ignorés, alif suscrite ٰ vs pleine ا conservées)."""
import json, re, unicodedata

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE, encoding="utf-8"))

HARAKAT = re.compile(r"[\u064B-\u0655\u0640]")  # tanwin, harakat, chadda, sukun, tatweel — GARDE U+0670 (suscrite) et ا (pleine)

def strip_h(s):
    return HARAKAT.sub("", s)

def words(s):
    return [w for w in strip_h(s).split() if w]

PROBES = {
    "خاطئ": ["خاطئ", "خئ"],
    "خالد": ["خلد"],
    "يَتَخَافَتُونَ": ["تخافت"],
    "خَافَ (peur)": ["خاف", "خف"],
    "خَشِعَ": ["خشع"],
    "خَمِدَ": ["خمد"],
    "خَلِقَ": ["خلق", "خَلِق"],
    "خَدَعَ": ["خدع"],
    "خَمْسَة/خامسة": ["خمس", "خامس"],
    "خَارِجَ": ["خرج"],
    "خَسِرَ/خَاسِر": ["خسر", "خاسر"],
    "خَسِئَ": ["خسئ"],
    "خَزَنَ": ["خزن", "خزر"],
    "خَضَعَ": ["خضع", "خاضع", "خاشع"],
    "تُخَاطِبْنِي": ["تخاتب", "تخطب"],
    "خَلَتْ": ["خلت"],
    "شَامِخَة": ["شامخ"],
}

for label, probes in PROBES.items():
    print(f"\n=== {label} ===")
    total = 0
    for snum, sdata in sorted(data.items(), key=lambda kv: int(kv[0])):
        for aynum, aytext in sdata["ar"]:
            t = strip_h(aytext)
            for p in probes:
                if p in t:
                    ws = [w for w in t.split() if p in w]
                    total += len(ws)
                    print(f"  {snum}:{aynum} — {' | '.join(ws[:4])}")
                    break
    if total == 0:
        print("  (aucune occurrence)")
    else:
        print(f"  → {total} occurrence(s)")
