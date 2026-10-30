#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 315 (activités de consolidation radd) :
le rasm de la pièce (p.171-173) ne cite aucun verset ni hadith — les preuves
textuelles du radd (p.168 verset + hadith, p.169 note) appartiennent au COURS,
non aux activités. La vérification porte sur l'ABSENCE de citation non attestée
+ l'arithmétique des corrigés savants (sommes = 1, taux uniformes)."""
import re
import sys
from fractions import Fraction as F

HTML = "scripts-translate/tr-tmp/pdf-mut23h2v-315.html"
html = open(HTML, encoding="utf-8").read()

errors = []
# 1. aucun fragment coranique ou hadith canonique ne doit s'y être glissé
#    (y compris les preuves du cours du radd, p.168-169 — matière d'un autre tour)
for pat, label in [
    (r"yūṣīkumu", "an-Nisāʾ 4:11"),
    (r"iḫwatan riǧālan", "an-Nisāʾ 4:176"),
    (r"alḥiqū al-farāʾiḍa", "hadith alḥiqū"),
    (r"man taraka mālan", "hadith de l'héritage (cours du radd, p.168 — hors pièce)"),
    (r"li-warithihi", "hadith de l'héritage (variante)"),
    (r"dhawī al-arḥām[aé]?\s*«", "citation vernaculaire inattendue"),
    (r"Anfāl|anfāl", "la note 8:75 du cours (p.169 — hors pièce)"),
]:
    if re.search(pat, html):
        errors.append(f"citation inattendue détectée : {label}")

# 2. le corps ne doit prétendre à aucun « vérifié au cache »
if "vérifié verbatim au cache" in html:
    errors.append("mention « vérifié verbatim au cache » alors que la pièce ne cite aucun verset")

# 3. arithmétique des corrigés savants (sommes = 1 ; taux uniformes)
cases = {
    "أ fille+mère":      ({'fille': F(3,4), 'mère': F(1,4)}, F(6,4)),
    "ب filles+mère":     ({'filles': F(4,5), 'mère': F(1,5)}, F(6,5)),
    "ج جدة+أخت+أخ":      ({'جدة': F(1,5), 'أخت': F(3,5), 'أخ': F(1,5)}, F(6,5)),
    "transformation":    ({'fille': F(3,4), 'جدة': F(1,4)}, F(6,4)),
}
for name, (parts, rate) in cases.items():
    if sum(parts.values()) != 1:
        errors.append(f"somme ≠ 1 : {name}")
# taux uniformes : chaque part / son farḍ = même rapport
farḍs = {
    "أ fille+mère":   ({'fille': F(1,2), 'mère': F(1,6)}, {'fille': F(3,4), 'mère': F(1,4)}, F(3,2)),
    "ب filles+mère":  ({'filles': F(2,3), 'mère': F(1,6)}, {'filles': F(4,5), 'mère': F(1,5)}, F(6,5)),
    "ج جدة+أخت+أخ":   ({'جدة': F(1,6), 'أخت': F(1,2), 'أخ': F(1,6)}, {'جدة': F(1,5), 'أخت': F(3,5), 'أخ': F(1,5)}, F(6,5)),
}
for name, (fards, radd, rate) in farḍs.items():
    for h in fards:
        if radd[h] / fards[h] != rate:
            errors.append(f"taux non uniforme pour {h} dans {name}")
# 4. fragments attendus dans le corps
for frag in ["trois quarts", "quatre cinquièmes", "un cinquième", "trois cinquièmes"]:
    if frag not in html:
        errors.append(f"fragment attendu absent du corps : {frag}")

if errors:
    print("ECHEC :")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("VERDICT : 0/0 — aucune citation revendiquée, aucune citation non attestée présente (le rasm p.171-173 n'en porte pas) ; corrigés vérifiés : sommes = 1, taux uniformes (3/2 ; 6/5 ; 6/5)")
