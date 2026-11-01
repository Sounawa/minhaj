#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R88 — Extraction des sources hadith-1es (13004/13005).

Pour chaque docId :
  - tr-tmp/<id>.src.html : la source arabe du CMS (lessons[].html)
  - tr-tmp/<id>.gt.html  : le htmlFr GT actuel (référence + garde-fou retour arrière)
  - affiche le rang de la leçon (n° officiel) + tailles.
"""
import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"
TMP = "/home/z/my-project/tr-tmp"
IDS = ["13004", "13005"]


def main() -> None:
    book = json.load(open(BOOK, encoding="utf-8"))
    lessons = book["lessons"]
    for pos, les in enumerate(lessons, start=1):
        did = str(les.get("docId"))
        if did not in IDS:
            continue
        src = (les.get("html") or "").strip()
        gt = (les.get("htmlFr") or "").strip()
        with open(f"{TMP}/{did}.src.html", "w", encoding="utf-8") as f:
            f.write(src)
        with open(f"{TMP}/{did}.gt.html", "w", encoding="utf-8") as f:
            f.write(gt)
        print(f"[R88] leçon {pos:02d} — {did} — src {len(src)} car | gt {len(gt)} car | titleFr: {les.get('titleFr')}")
    print("extraction terminée")


if __name__ == "__main__":
    main()
