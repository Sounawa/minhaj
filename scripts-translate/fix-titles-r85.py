#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R85 — Correction des titleFr GT-ismes (12958/12961/12980/12985).

Convention R84 : le h1 du lecteur affiche titleFr (métadonnée) — les GT-ismes
y sont corrigés à l'image du titre savant rendu dans le corps.
"""
import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"
FIX = {
    "12958": "Les dispositions de la récitation dans la prière",
    "12961": "La vertu de la Fātiḥa et le statut de sa récitation",
    "12980": "L’āmīn et le taḥmīd dans la prière",
    "12985": "Les dispositions de l’assise et du tashahhud",
}

data = json.load(open(BOOK, encoding="utf-8"))
n = 0
for les in data.get("lessons", []):
    did = str(les.get("docId"))
    if did in FIX:
        old = les.get("titleFr")
        les["titleFr"] = FIX[did]
        n += 1
        print(f"{did} : « {old} » → « {FIX[did]} »")

tmp = BOOK + ".tmp"
with open(tmp, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
import os
os.replace(tmp, BOOK)
print(f"✓ {n} titleFr corrigés")
