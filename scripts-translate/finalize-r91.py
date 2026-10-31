#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R91 — Ré-injection des 4 leçons corrigées dans hadith-1es.json.

Titres et registre INCHANGÉS (leçons déjà savantes « hand ») : seul htmlFr est
mis à jour depuis tr-tmp/<id>.html après fix-versets-r91.py.
"""
import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"
TMP = "/home/z/my-project/tr-tmp"
IDS = ["12875", "12885", "12908", "12953"]


def main() -> None:
    book = json.load(open(BOOK, encoding="utf-8"))
    done = 0
    for les in book["lessons"]:
        did = str(les.get("docId"))
        if did in IDS:
            htmlFr = open(f"{TMP}/{did}.html", encoding="utf-8").read().strip()
            old = len(les.get("htmlFr") or "")
            les["htmlFr"] = htmlFr
            print(f"✓ {did} : htmlFr {old} → {len(htmlFr)} car")
            done += 1
    if done != len(IDS):
        raise SystemExit(f"✗ {done}/{len(IDS)} leçons seulement — vérifier les docIds")
    with open(BOOK, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"→ hadith-1es.json réécrit ({done} htmlFr mis à jour)")


if __name__ == "__main__":
    main()
