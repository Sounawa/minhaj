#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R91 — Vérification des textes de versets du cache (hadith-1es, labels de versets-image)."""
import json

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
q = json.load(open(CACHE, encoding="utf-8"))

def verse(s: int, a: int, lang: str = "fr") -> str:
    sura = q[str(s)]
    arr = sura[lang]
    for num, txt in arr:
        if int(num) == a:
            return txt
    return f"[introuvable {s}:{a}]"

def show(label, s, a):
    try:
        t = verse(s, a)
        print(f"Q{s}:{a} [{label}] {t[:170]}")
    except Exception as e:
        print(f"Q{s}:{a} [{label}] ERREUR {e}")

print("=== Māʾida 6 vs 7 (ablutions — les 7 imprimés au manuel) ===")
show("wuḍūʾ attendu", 5, 6)
show("7", 5, 7)
print()
print("=== Nisāʾ 2 (ilā = maʿ) ===")
show("orphelins/avec", 4, 2)
print()
print("=== Baqara 220 vs 222 (ṭuhr — le 220 imprimé au manuel) ===")
show("220", 2, 220)
show("222 attendu", 2, 222)
print()
print("=== Tawba 109 (12884) ===")
show("édifice", 9, 109)
print()
print("=== Insān 6 (bāʾ du moyen — image 1 de 12953) ===")
show("76:5", 76, 5)
show("76:6", 76, 6)
print()
print("=== Nabaʾ 24-25 (le texte FR actuel du label « Insān 6 » correspond-il ?) ===")
show("78:24", 78, 24)
show("78:25", 78, 25)
print()
print("=== Ṭūr 33-35 (image 2 de 12953, cœur de Jubayr) ===")
for a in (33, 34, 35):
    show(f"52:{a}", 52, a)
print()
print("=== Najm 1-4 (le texte FR actuel du label « Ṭūr 33-35 » correspond-il ?) ===")
for a in (3, 4):
    show(f"53:{a}", 53, a)
print()
print("=== Les quatre labels prioritaires R90 (contrôle texte↔numéro) ===")
show("Jumuʿa 9 (12929/12995)", 62, 9)
show("Muḥammad 34 (12948)", 47, 34)
show("Wāqiʿa 77 (12985)", 56, 77)
show("Ṭāhā 131 (13001)", 20, 131)
print()
print("=== Divers autres labels vérifiés en passant ===")
show("Jumuʿa 9", 62, 9)
show("Māʾida 60 (12929)", 5, 60)
show("Baqara 105 (12961)", 2, 105)
show("Ḥijr 87 (12961)", 15, 87)
show("Anfāl 24 (12961)", 8, 24)
show("Aʿrāf 204 (12961)", 7, 204)
show("Yūnus 89 (12980)", 10, 89)
show("Dhāriyāt 17 (13002)", 51, 17)
show("Isrāʾ 79 (13002)", 17, 79)
show("Āl ʿImrān 8 (12953)", 3, 8)
show("Mursalāt 1 (12953)", 77, 1)
show("Inshiqāq 1 (12953)", 84, 1)
show("Nisāʾ 43 (12908)", 4, 43)
show("Nisāʾ 29 (12908)", 4, 29)
show("Tawba 109", 9, 109)
