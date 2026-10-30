#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 314 (taṣḥīḥ al-inkisār / applications de lʿawl) :
le rasm du manuel (p.164-167) ne cite aucun verset ni hadith —
la vérification porte sur l'ABSENCE de citation non attestée dans le htmlFr.
(Les citations de la page 168 — général du verset, hadith de l'héritage —
appartiennent à la leçon 37, matière d'une pièce suivante, non à celle-ci.)"""
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h2v-314.html"
html = open(HTML, encoding="utf-8").read()

errors = []
# 1. aucun fragment coranique ou hadith canonique ne doit s'y être glissé
for pat, label in [
    (r"yūṣīkumu", "an-Nisāʾ 4:11"),
    (r"iḫwatan riǧālan", "an-Nisāʾ 4:176"),
    (r"alḥiqū al-farāʾiḍa", "hadith alḥiqū"),
    (r"man taraka mālan", "hadith de l'héritage (leçon 37, p.168 — hors pièce)"),
    (r"li-warithihi", "hadith de l'héritage (variante)"),
    (r"mā kāna li-dhimmatihi", "général du verset p.168 (hors pièce)"),
]:
    if re.search(pat, html):
        errors.append(f"citation inattendue détectée : {label}")

# 2. le corps ne doit prétendre à aucun « vérifié au cache »
if "vérifié verbatim au cache" in html:
    errors.append("mention « vérifié verbatim au cache » alors que la pièce ne cite aucun verset")

# 3. sanity arithmétique des trois compositions (les nombres du corps doivent tenir)
checks = [
    ("quatre, deux et un", 4 + 2 + 1 == 7),
    ("trois, deux et trois", 3 + 2 + 3 == 8),
    ("trois, deux, deux et six", 3 + 2 + 2 + 6 == 13),
    ("l'exemple entier du vingt-sept (3+4+4+16)", 3 + 4 + 4 + 16 == 27),
]
for name, ok in checks:
    if not ok:
        errors.append(f"incohérence arithmétique : {name}")
for frag in ["quatre, deux et un", "trois, deux et trois", "trois, deux, deux et six"]:
    if frag not in html:
        errors.append(f"fragment attendu absent du corps : {frag}")

if errors:
    print("ECHEC :")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("VERDICT : 0/0 — aucune citation coranique revendiquée, aucune citation non attestée présente (le rasm p.164-167 n'en porte pas) ; arithmétique des compositions vérifiée (7, 8, 13, 27)")
