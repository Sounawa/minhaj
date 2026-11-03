# -*- coding: utf-8 -*-
"""Minhāj — R555 (pdf-12, leçon 11) : localisation des renvois à trancher par image.
Cherche les jetons numériques (numéros Muwaṭṭaʾ rouges) et les renvois coraniques
sur les pages 79-85 du miroir, pour recadrage ciblé 600-900 dpi."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
doc = fitz.open(PDF)
TOKENS = ["562", "563", "564", "565", "566", "567", "568", "569", "570", "571",
          "572", "573", "574", "575", "576", "151", "152", "185", "60", "41", "06"]
for pno in range(78, 86):
    page = doc[pno]
    print(f"===== PAGE {pno+1} ===== {page.rect.width:.0f}x{page.rect.height:.0f}")
    for tok in TOKENS:
        for r in page.search_for(tok):
            print(f"  « {tok} » @ ({r.x0:.0f},{r.y0:.0f})-({r.x1:.0f},{r.y1:.0f})")
