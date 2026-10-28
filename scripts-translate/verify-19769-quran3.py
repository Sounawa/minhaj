#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sonde 3 — doc 19769 : dessins bruts des lexèmes du chapitre du ḫāʾ + versets pivots."""
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
    if ALIF in w:
        return "PLEINE"
    return "absente"

def count_lexeme(label, pattern):
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
                    if len(ex[f]) < 6:
                        ex[f].append(f"{snum}:{aynum} {w}")
    for f in ("SUSCRITE", "PLEINE", "absente"):
        print(f"  {f}: {tally[f]}  ex: {' | '.join(ex[f][:4])}")
    print(f"  TOTAL: {sum(tally.values())}")

count_lexeme("خ-د-ع (خدع toutes formes)", r"خ.{0,2}دع")
count_lexeme("خ-ش-ع (خشع brut)", r"خ.{0,2}شع")
count_lexeme("خ-ل-ت (خلت, racine خ-ل-ا/خ-ل-و)", r"خ.{0,2}ل[ت]")
count_lexeme("خ-م-س (toutes sourates)", r"خ.{0,2}م[س]")
count_lexeme("خ-ض-ع (خضع)", r"خ.{0,2}ضع")
count_lexeme("خ-ز-ن (خزن)", r"خ.{0,2}زن")
count_lexeme("ش-م-خ (شمخ)", r"ش.{0,2}مخ")
count_lexeme("خ-ف-ت/خ-ف-ى hmm (خف hors خفف)", r"خف(?!ف)")

REFS = [(12, 29), (12, 91), (12, 97), (59, 17), (69, 9), (96, 16), (2, 167), (5, 37),
        (6, 122), (33, 32), (79, 12), (67, 4), (47, 15), (26, 129), (25, 69), (104, 3),
        (10, 52), (2, 134), (84, 4), (17, 110), (12, 75)]
for s, a in REFS:
    for aynum, aytext in data[str(s)]["ar"]:
        if aynum == a:
            print(f"\nRAW {s}:{a} — {aytext}")
