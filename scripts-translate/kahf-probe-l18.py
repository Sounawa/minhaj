#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Sonde de bornes Kahf leçon 17 (v56-58 imprimé = cache 57-59, ouvre
p.125) : décharge les lignes brutes des pages 125-137 du manuel miroir
(tafsir-3-thanawi_text.pdf) pour trancher la borne supérieure (début de la
leçon 18 = « أهداف الدرس ») — jamais devinée (doctrine R493+).
NUM : chiffres OCR inversés par paires (ex. « 85-65 » = (56-58))."""
import re

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"
doc = fitz.open(PDF)
for p in range(125, 138):
    page = doc[p - 1]
    raw = page.get_text()
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    print(f"===== p{p} ({len(lines)} lignes) =====")
    for l in lines[:5]:
        print("  T:", l[:90])
    for l in lines:
        if re.search(r"\d{1,3}\s*-\s*\d{1,3}", l) and (
                "آية" in l or "الكهف" in l or re.match(r"^[\d\s\-\[\]]+$", l)):
            print("  N:", l[:90])
        if "أهداف" in l or "الدرس" in l or "إعداد" in l:
            print("  H:", l[:90])
    for l in lines[-3:]:
        print("  B:", l[:90])
