#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R92 — Injection du rendu savant faraid-tanawi-3 / pdf-mut23h2v-310.

- htmlFr de la leçon 310 remplacé depuis tr-tmp/pdf-mut23h2v-310.html
  (leçon pdfOnly : le src est l'OCR du scan habous, cf. content/ocr-cache/)
- titleFr INCHANGÉ (GT exact, non GT-isme)
- registre savant : pdf-mut23h2v-310 ajouté à « hand » (première leçon savante
  du book — le book passe de 1/27 à 2/27 savant, avec la leçon 335)
"""
import json

BOOK = "/home/z/my-project/content/books/faraid-tanawi-3.json"
TMP = "/home/z/my-project/tr-tmp/pdf-mut23h2v-310.html"
REG = "/home/z/my-project/scripts-translate/savant-registry.json"
DOC = "pdf-mut23h2v-310"


def main() -> None:
    book = json.load(open(BOOK, encoding="utf-8"))
    htmlFr = open(TMP, encoding="utf-8").read().strip()
    hit = 0
    for les in book["lessons"]:
        if str(les.get("docId")) == DOC:
            old = len(les.get("htmlFr") or "")
            les["htmlFr"] = htmlFr
            print(f"✓ {DOC} : htmlFr {old} → {len(htmlFr)} car")
            hit += 1
    if hit != 1:
        raise SystemExit(f"✗ {hit} leçon trouvée pour {DOC} — vérifier le docId")
    with open(BOOK, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)
        f.write("\n")

    reg = json.load(open(REG, encoding="utf-8"))
    if DOC not in reg["hand"]:
        reg["hand"].append(DOC)
        reg["hand"].sort()
        with open(REG, "w", encoding="utf-8") as f:
            json.dump(reg, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"✓ registre : {DOC} ajouté à hand ({len(reg['hand'])} hand + "
              f"{len(reg['llm'])} llm = {len(reg['hand']) + len(reg['llm'])}/950)")
    else:
        print(f"= registre : {DOC} déjà présent en hand")


if __name__ == "__main__":
    main()
