#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R339 — Sondes 19771 (faṣl ad-dāl). Position exacte + racines du chapitre."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE, encoding="utf-8"))
corpus = []
for k in sorted(data, key=int):
    for a in data[k]["ar"]:
        corpus.append((int(k), a[0], a[1]))
IDX = {(sn, an): tx for (sn, an, tx) in corpus}

def sweep(label, pattern, show_all=True, maxs=12):
    print(f"\n=== {label} ===")
    rx = re.compile(pattern)
    hits = []
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            st = max(0, m.start() - 14); en = min(len(tx), m.end() + 14)
            hits.append((sn, an, m.group(0), tx[st:en]))
    print(f"  {len(hits)} occ.")
    for (sn, an, g, c) in hits[:maxs]:
        print(f"  {sn}:{an} [{g}] | …{c}…")
    if len(hits) > maxs:
        print("  …")
    return hits

def show(sn, an, needle, ctx=28):
    tx = IDX.get((sn, an), "")
    i = tx.find(needle)
    if i < 0:
        print(f"  {sn}:{an} — '{needle}' ABSENT"); return
    st = max(0, i - ctx); en = min(len(tx), i + len(needle) + ctx)
    print(f"  {sn}:{an} [{needle}] | …{tx[st:en]}…")
    print("      cps:", " ".join(f"{ord(c):04X}" for c in tx[i:i+len(needle)+2]))

# 1. collectifs féminins du bayt
sweep("شهدت", r"شَ?هَ?[دذ]َ?ت")
sweep("عبدت", r"عَ?ابَ?دَ?ت")
sweep("ولدت", r"وَ?الِ?دَ?ت")
sweep("معدود", r"مَ?عْ?دُو?[دذ]")
# 2. داخِلون / داخِرون + le témoin de Ghāfir
sweep("دخلون/دخلين", r"د.{0,3}خ.{0,2}ل[وُىي]")
sweep("دخر", r"د.{0,3}خَ?ر")
sweep("dāl+ḫāʾ+ā en s40", r"دَ?[اى]?خَ?[رلد]")
for (sn, an) in [(40, x) for x in range(1, 86)]:
    tx = IDX.get((sn, an), "")
    for m in re.finditer(r"دَ?ا?خ", tx):
        st = max(0, m.start()-16); en = min(len(tx), m.end()+16)
        print(f"  s40:{an} [{tx[m.start():m.start()+6]}] | …{tx[st:en]}…")
# 3. يد formes (le duel)
sweep("يدا/يده/يدك/يديه", r"يَ?د[اىَ]", maxs=16)
# 4. racine د-ر-ك
sweep("درك/ادرك/ادارك", r"[اأ]?اد?َ?ر?َ?ك", maxs=6)
sweep("درک racine d-r-k", r"[اأٱ]دَ?رَ?ك", maxs=12)
# 5. racine د-ل-ج / ج-د-ل
sweep("جدل/جادل/جدال", r"ج.{0,3}د.{0,3}ل", maxs=10)
# 6. أتعِدنني 46:17 exact
show(46, 17, "أَتَعِدَ")
# 7. تذودن
sweep("تذو", r"تَ?ذُ?و", maxs=8)
# 8. دفع/دافع
sweep("دفع/دافع", r"[د]{1}.?ا?فَ?ع", maxs=10)
# 9. لدى/لدا + hanāǧir
sweep("لدى/لدا", r"لَ?د[اى]")
sweep("الحناجر", r"حَ?نَ?[اج]{1,2}ر")
# 10. بدأ (wāwiyy al-lām)
sweep("بدا", r"بَ?دَ?ا", maxs=10)
# 11. هداي / هدى / سدى
sweep("هداي", r"هُ?دَ?ا?ي", maxs=6)
sweep("سدى", r"سُ?د[اى]", maxs=6)
# 12. غدوة / غدو
sweep("غدو", r"غَ?دَ?و", maxs=10)
# 13. المقنع — الربا / مشكاة / نجوة / منوة
sweep("ربوا/ربا rasm wāw", r"ر.{0,3}ب[اى][وو]?[اىٰ]?", maxs=10)
show(2, 275, "رِبَو")
show(24, 35, "مِشْكَو")
sweep("نجوة", r"نَ?جَ?و[اى]ة")
show(53, 20, "مَنَو")
# 14. يسجدن / جهدك
sweep("سجد duals", r"س.{0,3}جُ?د[اىن]", maxs=8)
sweep("جهد", r"جَ?هَ?د", maxs=8)
