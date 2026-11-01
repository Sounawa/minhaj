#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R93 — Injection du rendu savant tafsir-2es / pdf-mut23h33-563 + -564.

- htmlFr des leçons 563 et 564 remplacé depuis tr-tmp/pdf-mut23h33-56X.html
  (leçons pdfOnly : le src est l'OCR du manuel كتاب التفسير 2 إعدادي,
  cf. content/ocr-cache/)
- titleFr INCHANGÉS (GT, non réécrits)
- registre savant : les deux docIds ajoutés à « hand »
  (tafsir-2es passe de 7/37 à 9/37 savant)
"""
import json

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"
REG = "/home/z/my-project/scripts-translate/savant-registry.json"
DOCS = ["pdf-mut23h33-563", "pdf-mut23h33-564"]


def main() -> None:
    book = json.load(open(BOOK, encoding="utf-8"))
    hit = 0
    for doc in DOCS:
        htmlFr = open(f"/home/z/my-project/tr-tmp/{doc}.html", encoding="utf-8").read().strip()
        found = 0
        for les in book["lessons"]:
            if str(les.get("docId")) == doc:
                old = len(les.get("htmlFr") or "")
                les["htmlFr"] = htmlFr
                print(f"✓ {doc} : htmlFr {old} → {len(htmlFr)} car")
                found += 1
        if found != 1:
            raise SystemExit(f"✗ {found} leçon(s) trouvée(s) pour {doc}")
        hit += 1
    with open(BOOK, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)
        f.write("\n")

    reg = json.load(open(REG, encoding="utf-8"))
    added = []
    for doc in DOCS:
        if doc not in reg["hand"]:
            reg["hand"].append(doc)
            added.append(doc)
    reg["hand"].sort()
    with open(REG, "w", encoding="utf-8") as f:
        json.dump(reg, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"✓ registre : {added} ajoutés à hand ({len(reg['hand'])} hand + "
          f"{len(reg['llm'])} llm = {len(reg['hand']) + len(reg['llm'])}/950)")


if __name__ == "__main__":
    main()
