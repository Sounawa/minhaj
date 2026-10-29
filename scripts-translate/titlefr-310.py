#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R380 — harmonisation du titleFr de pdf-mut23h2v-310 au h1 interne."""
import json
import os

HOME = "/home/z/my-project"
PATH = f"{HOME}/content/books/faraid-tanawi-3.json"
H1 = "Les farāʾiḍ : le ḥaǧb (1)"

with open(PATH, "r", encoding="utf-8") as fh:
    data = json.load(fh)

hits = 0
before = []
for l in data.get("lessons", []):
    if str(l.get("docId")) == "pdf-mut23h2v-310":
        before.append(l.get("titleFr"))
        l["titleFr"] = H1
        hits += 1

tmp = PATH + ".tmp"
with open(tmp, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False)
os.replace(tmp, PATH)
print(f"titleFr harmonisé : {hits} emplacement(s)")
for b in before:
    print(f"  avant : {b}")
print(f"  après : {H1}")
