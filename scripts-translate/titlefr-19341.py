#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R375 — harmonisation du titleFr de 19341 au h1 interne (convention espace régulière)."""
import json

HOME = "/home/z/my-project"
PATH = f"{HOME}/content/books/taqtit-tanawi-1.json"
H1 = "Le tawqīt : les activités d'exploitation des apprentissages et de leur soutien (des leçons 18 à 21)"

with open(PATH, "r", encoding="utf-8") as fh:
    data = json.load(fh)

hits = 0
before = []
for l in data.get("lessons", []):
    if str(l.get("docId")) == "19341":
        before.append(l.get("titleFr"))
        l["titleFr"] = H1
        hits += 1

tmp = PATH + ".tmp"
with open(tmp, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False)
import os
os.replace(tmp, PATH)
print(f"titleFr harmonisé : {hits} emplacement(s)")
for b in before:
    print(f"  avant : {b}")
print(f"  après : {H1}")
