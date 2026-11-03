#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Preuve image leçon 7 hadith-2es (slot pdf-8, pages 53-59).
Crops fitz : pages entières ~160 dpi pour contexte + zones serrées 400 dpi
pour trancher numéros Muwaṭṭa, isnāds, lexies altérées (mécanique R535-R540).
Sortie : tr-tmp/qa-crops-r541/*.png
"""
import os
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r541"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)


def crop(page_no, x0f, y0f, x1f, y1f, dpi, name):
    """page_no = page imprimée (1-indexé) ; fractions du rect de la page."""
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    path = f"{OUT}/{name}.png"
    pix.save(path)
    print(f"{name}: {pix.width}x{pix.height}")


# Pages entières (contexte) 160 dpi
for p in range(53, 60):
    pg = doc[p - 1]
    pix = pg.get_pixmap(matrix=fitz.Matrix(160 / 72, 160 / 72))
    pix.save(f"{OUT}/p{p}-full.png")
    print(f"p{p}-full: {pix.width}x{pix.height}")

# Zones serrées 400 dpi — positions à ajuster après lecture des pages entières
# p.53 : objectifs (haut), renvoi āya, matn 1 (bas)
crop(53, 0.05, 0.05, 0.95, 0.40, 400, "p53-objectifs")
crop(53, 0.05, 0.33, 0.95, 0.62, 400, "p53-renvoi-aya")
crop(53, 0.05, 0.55, 0.95, 0.98, 400, "p53-matn1")
# p.54 : numéro matn 1 (haut), matn 2 + numéro, tarjama ʿĀʾiša (bas)
crop(54, 0.05, 0.03, 0.95, 0.30, 400, "p54-num506")
crop(54, 0.05, 0.25, 0.95, 0.72, 400, "p54-matn2-num509")
crop(54, 0.05, 0.62, 0.95, 1.00, 400, "p54-tarjama-aysha")
doc.close()
print("OK")
