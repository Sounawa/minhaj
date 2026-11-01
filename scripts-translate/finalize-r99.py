#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R99 — Injection du rendu savant tafsir-3es / pdf-mut23h36-601 + -602.

- htmlFr des leçons 599 et 600 remplacé depuis tr-tmp/pdf-mut23h36-5XX.html
  (leçons pdfOnly : le src est l'OCR du manuel كتاب التفسير 3 إعدادي,
  cf. content/ocr-cache/)
- titleFr INCHANGÉS (GT, non réécrits)
- registre savant : les deux docIds ajoutés à « hand »
  (tafsir-3es passe de 8/43 à 10/43 savant)
"""
import json

BOOK = "/home/z/my-project/content/books/tafsir-3es.json"
REG = "/home/z/my-project/scripts-translate/savant-registry.json"
DOCS = ["pdf-mut23h36-601", "pdf-mut23h36-602"]


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
