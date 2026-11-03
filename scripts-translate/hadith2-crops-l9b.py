#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Preuve image complémentaire leçon 9 hadith-2es (slot pdf-10).
Crops serrés 600 dpi pour trancher par image : (1) hadith 1 p67 isnād+matn
(lecture VLM 1546 manifestement hallucinée), (2) hadith 4 rawḍa p68 isnād
+ numéro Muwaṭṭaʾ (couche « 0:5 » vs VLM 419), (3) āya p67 (couche البقرة
vs VLM النور). Sortie : tr-tmp/qa-crops-r545b/"""
import os
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r545b"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)


def crop(page_no, x0f, y0f, x1f, y1f, dpi, name):
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{OUT}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


# (1) hadith 1 p67 : isnād puis matn, deux blocs 600 dpi
crop(67, 0.05, 0.42, 0.95, 0.72, 600, "p67-h1-isnad-600")
crop(67, 0.05, 0.70, 0.95, 1.00, 600, "p67-h1-matn-600")
# (2) hadith 4 p68 : isnād + matn + numéro
crop(68, 0.05, 0.52, 0.95, 0.78, 600, "p68-h4-isnad-600")
crop(68, 0.05, 0.74, 0.95, 1.00, 600, "p68-h4-matn-num-600")
# (3) āya d'ouverture p67 (fin d'intro + référence sourate)
crop(67, 0.05, 0.18, 0.95, 0.46, 600, "p67-aya-ref-600")
