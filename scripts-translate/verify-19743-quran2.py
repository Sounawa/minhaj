#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compléments de vérification 19743 : tukadḏibāni (Raḥmān), igtibāʾ (hāwī + yāʾ),
التَّلِيَتِ/التَّئِبُونَ (iʿdād), ribā Nisāʾ/Āl ʿImrān."""
import json
import re

C = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json"))

def show(s, i, label):
    for n, t in C[str(s)]["ar"]:
        if n == i:
            print(f"[{label}] {s}:{i} : {t}")
            return
    print(f"[{label}] {s}:{i} ABSENT")

def scan(pat, label, smin=1, smax=114):
    rx = re.compile(pat)
    hits = []
    for s in range(smin, smax + 1):
        for n, t in C[str(s)]["ar"]:
            for m in rx.finditer(t):
                a, b = max(0, m.start() - 35), min(len(t), m.end() + 35)
                hits.append((f"{s}:{n}", t[a:b]))
    print(f"--- {label} : {len(hits)} occurrence(s)")
    for ref, ctx in hits:
        print(f"    {ref}  …{ctx}…")

print("=== 1. تُكَذِّبَانِ dans al-Raḥmān : quel rasm ? ===")
scan(r"كَذَّب", "كذّب tout (Raḥmān)", 55, 55)
show(55, 13, "Raḥmān 13")
show(55, 31, "Raḥmān 31")

print("")
print("=== 2. اِجْتَبَى (form VIII) : hāwī élidée sans yāʾ vs ailleurs ===")
scan(r"ٱجْتَبَ|اِجْتَبَ", "اجتبا toutes formes")
show(7, 144, "Aʿrāf 144 (ٱجْتَبَيْتُكَ?)")
show(20, 122, "Ṭāhā 122")

print("")
print("=== 3. hāwī avant suffixe hāʾ : دَعَٰهُ / عَادَا / غَوَا ===")
scan(r"دَعَٰهُ|دَعَاهُ|دَعَيْ", "دعا formes")
scan(r"رَانَ|عَادَ|غَوَى|نَوَى", "عادا/غوا/نوا aperçu")
scan(r"بَٰهُ|بَاهُ|بَيْهُ", "…باه (aperçu 15)")

print("")
print("=== 4. iʿdād : التَّلِيَتِ / التَّئِبُونَ ===")
scan(r"تَلِيَ|تَلْوَ|ٱتْلُ|تَتْلُو|تَتْلُوا|ٱتَّبَعْتُمْ|تَالِي", "تلي/تلو aperçu")
scan(r"تَائِب|تَائب|تَئِب|ٱلتَّئِب", "تائب/تئب")

print("")
print("=== 5. ribā : Nisāʾ 160-161, Āl ʿImrān 130, Rūm 39 (rasm complet) ===")
show(4, 160, "Nisāʾ 160")
show(4, 161, "Nisāʾ 161")
show(3, 130, "Āl ʿImrān 130")
scan(r"رِبَو|رِبًا|رِبٰا|رِبا", "ribā rasm (toutes)")

print("")
print("=== 6. عَلَيْهِ الْبَاءُ : bayt 4 الألف المتطرفة maqṣūra — جدول récap عُقْبَى/أَرْبَى ===")
scan(r"عُقْب", "عقب toutes")
scan(r"أَرْب", "أرب toutes")
