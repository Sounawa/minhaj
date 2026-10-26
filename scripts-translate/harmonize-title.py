#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Harmonisation du titleFr d'une leçon avec le h1 savant du htmlFr.
Usage: python3 scripts-translate/harmonize-title.py <bookId> <docId> <nouveau titleFr>
Le h1 d'en-tête de la page rendue vient du champ titleFr du JSON (distinct du
h1 interne au htmlFr) — TOUJOURS harmoniser les DEUX (leçon R226).
"""
import json, os, sys

HOME = "/home/z/my-project"
book_id, doc_id, new_title = sys.argv[1], sys.argv[2], sys.argv[3]
path = f"{HOME}/content/books/{book_id}.json"

with open(path, "r", encoding="utf-8") as fh:
    data = json.load(fh)

changed = 0
for l in data.get("lessons", []):
    if str(l.get("docId")) == str(doc_id):
        old = l.get("titleFr")
        l["titleFr"] = new_title
        changed += 1
        print(f"✓ docId {doc_id} : titleFr « {old} » → « {new_title} »")
if "intro" in data and str(data["intro"].get("docId")) == str(doc_id):
    old = data["intro"].get("titleFr")
    data["intro"]["titleFr"] = new_title
    changed += 1
    print(f"✓ intro {doc_id} : titleFr « {old} » → « {new_title} »")

if not changed:
    print(f"⚠︎ docId {doc_id} introuvable dans {book_id} — aucun changement")
    sys.exit(1)

tmp = path + ".tmp"
with open(tmp, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False)
os.replace(tmp, path)
print(f"✓ {changed} emplacement(s) harmonisé(s) — {path}")
