#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 313 (ʿawl) :
le rasm du manuel (p.149-163) ne cite aucun verset ni hadith —
la vérification porte sur l'ABSENCE de citation non attestée dans le htmlFr."""
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h2v-313.html"
html = open(HTML, encoding="utf-8").read()

errors = []
# 1. aucun fragment coranique canonique ne doit s'y être glissé
for pat, label in [
    (r"yūṣīkumu", "an-Nisāʾ 4:11"),
    (r"iḫwatan riǧālan", "an-Nisāʾ 4:176"),
    (r"alḥiqū al-farāʾiḍa", "hadith alḥiqū"),
    (r"al-aṣl al-baḫīl", "note baḫīl (récit, non citation — si présent, c'est le rasm du livre)"),
]:
    if re.search(pat, html) and label.startswith(("an-", "hadith")):
        errors.append(f"citation inattendue détectée : {label}")

# 2. le corps ne doit prétendre à aucun « vérifié au cache »
if "vérifié verbatim au cache" in html:
    errors.append("mention « vérifié verbatim au cache » alors que la pièce ne cite aucun verset")

if errors:
    print("ECHEC :")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("VERDICT : 0/0 — aucune citation coranique revendiquée, aucune citation non attestée présente (le rasm p.149-163 n'en porte pas)")
