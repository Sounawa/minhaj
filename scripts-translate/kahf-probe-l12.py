#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Sonde de bornes Kahf leçon 12 (v36-43, ouvre p.87) : décharge les
lignes brutes des pages 87-99 du manuel miroir (tafsir-3-thanawi_text.pdf)
pour trancher la borne supérieure (début de la leçon 13 = « أهداف الدرس »)
— jamais devinée (doctrine R493+)."""
import re

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"
doc = fitz.open(PDF)
for p in range(87, 100):
    page = doc[p - 1]
    raw = page.get_text()
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    print(f"===== p{p} ({len(lines)} lignes) =====")
    # En-tête (5 premières) + queue (4 dernières) + lignes à NUM versets
    for l in lines[:5]:
        print("  T:", l[:90])
    for l in lines:
        if re.search(r"\d{1,3}\s*-\s*\d{1,3}", l) and (
                "آية" in l or "الكهف" in l or re.match(r"^[\d\s\-\[\]]+$", l)):
            print("  N:", l[:90])
    for l in lines[-4:]:
        print("  B:", l[:90])
