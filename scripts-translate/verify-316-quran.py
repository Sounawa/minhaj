#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 316 (mafqūd) :
le rasm du chapitre (faraid-2 p.191-201) cite Khalīl et les articles 62/72
du Code de la famille — AUCUN verset ni hadith. Vérification : absence de
citation non attestée + arithmétique de l'exemple de Khalīl et de l'application."""
import re
import sys
from fractions import Fraction as F

HTML = "scripts-translate/tr-tmp/pdf-mut23h2v-316.html"
html = open(HTML, encoding="utf-8").read()

errors = []
for pat, label in [
    (r"yūṣīkumu", "an-Nisāʾ 4:11"),
    (r"iḫwatan riǧālan", "an-Nisāʾ 4:176"),
    (r"alḥiqū al-farāʾiḍa", "hadith alḥiqū (lointain, p.202 — hors pièce)"),
    (r"man taraka mālan", "hadith de l'héritage"),
    (r"la-dhakara|al-Farāʾiḍ al-muqaddara", "le texte aš-Šāṭibī (p.202 — hors pièce)"),
]:
    if re.search(pat, html):
        errors.append(f"citation inattendue détectée : {label}")

if "vérifié verbatim au cache" in html:
    errors.append("mention « vérifié verbatim au cache » alors que la pièce ne cite aucun verset")

# arithmétique de l'exemple de Khalīl (زوج+أم+أخت+أب مفقود)
vie = {'زوج': F(1,2), 'أم': F(1,6), 'أب': F(1,3), 'أخت': F(0)}          # أصل 6 عادلة
mort = {'زوج': F(3,8), 'أخت': F(3,8), 'أم': F(1,4)}                      # عائلة 6→8
assert sum(vie.values()) == 1 and sum(mort.values()) == 1
regle = {'زوج': min(F(12,24),F(9,24)), 'أم': min(F(4,24),F(6,24)), 'أخت': min(F(0),F(9,24))}
assert regle == {'زوج': F(9,24), 'أم': F(4,24), 'أخت': F(0)}             # les moindres
depot = 1 - sum(regle.values())
assert depot == F(11,24)
assert F(8,24)+F(3,24) == depot and F(9,24)+F(2,24) == depot             # les deux issues
# application des quatre frères germains (l'un disparu)
assert F(3,12) == F(1,4) and F(4,12) == F(1,3) and 3*F(3,12) + F(3,12) == 1

for frag in ["onze vingt-quatrièmes", "trois douzièmes", "vingt-quatre", "trois huitièmes"]:
    if frag not in html:
        errors.append(f"fragment attendu absent du corps : {frag}")

if errors:
    print("ECHEC :")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("VERDICT : 0/0 — aucune citation revendiquée, aucune citation non attestée (le chapitre cite Khalīl et la Mudawana 62/72, aucun verset ni hadith) ; exemple de Khalīl vérifié (6/8/24, moindres 9-4-0, dépôt 11/24, issues 8+3 et 9+2) ; application des quatre frères vérifiée (3/12)")
