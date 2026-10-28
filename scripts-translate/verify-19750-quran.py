#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérifications coraniques du doc 19750 (rasm-wa-dabt-4ep, chapitre du tāʾ).

L'élision de l'alif après le tāʾ : les six mots du bayt 1 (mabsūṭatāni, at-talīyati,
marratān, ḫitāmuhu, matāʿan, ǧannatān), les QUATRE exceptions de كِتَاب (Ḥiǧr 2,
Kahf 2, Raʿd avec ʾaǧal, Naml 1re), l'hamza warš (mustanisīn, mustaʾḫirīn, imtāzū),
les pluriels du Dānī (at-tābiʿīn, at-tāʾibūn, qānitāt, ṭāʾifāt, tāʾibat), le mot يَتَمَى.
"""
import json
import re

C = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json"))

def show(s, i, label):
    for n, t in C[str(s)]["ar"]:
        if n == i:
            print(f"[{label}] {s}:{i} : {t}")
            return
    print(f"[{label}] {s}:{i} ABSENT")

def scan(pat, label, smin=1, smax=114, maxp=25):
    rx = re.compile(pat)
    hits = []
    for s in range(smin, smax + 1):
        for n, t in C[str(s)]["ar"]:
            for m in rx.finditer(t):
                a, b = max(0, m.start() - 30), min(len(t), m.end() + 30)
                hits.append((f"{s}:{n}", t[a:b]))
    print(f"--- {label} : {len(hits)} occurrence(s)")
    for ref, ctx in hits[:maxp]:
        print(f"    {ref}  …{ctx}…")
    if len(hits) > maxp:
        print(f"    … +{len(hits)-maxp} autres")
    return hits

print("=== 1. كِتَاب / كِتَٰب : formes pleines vs suscrites (global) ===")
scan(r"كِتَاب", "كِتَاب alif PLEINE (toutes formes, aperçu 30)", 1, 114, 30)
print("    — décompte global :")
full_k = len(re.findall(r"كِتَاب", " ".join(t for s in range(1,115) for _, t in C[str(s)]["ar"])))
susk_k = len(re.findall(r"كِتَٰب", " ".join(t for s in range(1,115) for _, t in C[str(s)]["ar"])))
print(f"    كِتَاب (pleine) : {full_k} — كِتَٰب (suscrite) : {susk_k}")

print("")
print("=== 2. les quatre exceptions (per-sūra) ===")
for s, name in ((15, "Ḥiǧr"), (18, "Kahf"), (13, "Raʿd"), (27, "Naml")):
    scan(r"كِتَاب|كِتَٰب", f"كتاب en {name} ({s})", s, s, 12)

print("")
print("=== 3. أَجَل en ar-Raʿd ===")
scan(r"أَجَل", "أجل en Raʿd", 13, 13, 8)

print("")
print("=== 4. خِتَامُهُ / خِتَمُهُ (83:26 Muṭaffifīn) ===")
scan(r"خِتَٰم|خِتَام|خِتَم", "ختم formes (ختمām)", 1, 114, 8)
show(83, 26, "Muṭaffifīn 26")

print("")
print("=== 5. مَتَاع (dual?) ===")
scan(r"مَتَاع|مَتَع", "متاع toutes formes", 1, 114, 12)

print("")
print("=== 6. مَرَّتَان (dual de مَرَّة) ===")
scan(r"مَرَّتَٰنِ|مَرَّتَانِ|مَرَّتَيْ|مَرَّتَنِ", "مرة dual", 1, 114, 8)

print("")
print("=== 7. at-tābiʿīn (pluriel Dānī) ===")
scan(r"تَابِع|تَبِع", "تابع/تبع", 1, 114, 10)

print("")
print("=== 8. at-tāʾibūn (avec Ā composite?) ===")
scan(r"تَآئِب|تَائِب|تَئِب", "تائب toutes (avec آ)", 1, 114, 10)
scan(r"ٱلتَّآئ", "التّائ (آ)", 1, 114, 6)

print("")
print("=== 9. qānitāt / qānitat ===")
scan(r"قَانِت|قَنِت", "قانت/قنت", 1, 114, 12)

print("")
print("=== 10. ṭāʾifāt / ṭāʾifatāni ===")
scan(r"طَآئِف|طَائِف|طَيِّف", "طائف formes", 1, 114, 10)

print("")
print("=== 11. mustaʾḫirīn / mustanisīn / imtāzū (hamza warš) ===")
scan(r"مُسْتَأْخِر|مُسْتَخِر|مُسْتَأْنِس|مُسْتَنِس", "مستأخر/مستأنس", 1, 114, 10)
scan(r"امْتَزُوا|ٱمْتَزُوا|امْتَازُوا|ٱمْتَازُوا", "امتزوا/امتازوا", 1, 114, 8)

print("")
print("=== 12. yatamā (le mot mystère) ===")
scan(r"يَتَمَى|يَتَمَٰ|يَتَمَانِ|تَمَى|تَمَّى", "تمى/يتمى", 1, 114, 12)
scan(r"يَتِيم", "يتيم (dual? aperçu)", 1, 114, 6)

print("")
print("=== 13. جَنَّتَانِ (55:46/62, croisé R331) ===")
scan(r"جَنَّتَٰنِ|جَنَّتَانِ", "جنتان", 1, 114, 6)
