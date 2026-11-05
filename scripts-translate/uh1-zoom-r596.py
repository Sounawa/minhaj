# -*- coding: utf-8 -*-
"""R596 — hyper-zooms 600 dpi des zones critiques restantes :
  1) bayt p96 (PDF 122) : 2 lignes du vers, zone 28-45 % hauteur, x 25-100 %
  2) p97 (PDF 123) top : 3e صورة « قلب سند بتمامه... », zone 5-25 % hauteur.
"""
import fitz
from PIL import Image

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r596"

doc = fitz.open(PDF)

# (idx_pdf_base1, y0 %, y1 %, x0 %, x1 %, nom)
# CALAGE PROUVÉ (R596) : docId = index PDF = numéro imprimé (offset 0) —
# footer «96» lu sur comp-D (PDF 96) et «97» sur comp-F (PDF 97) ;
# PDF 122 = المؤتلف والمختلف (lesson tardive) — l'hypothèse offset +26 était fausse.
ZONES = [
    (96, 0.26, 0.50, 0.22, 1.00, "zoom-p96-bayt-600"),
    (97, 0.04, 0.28, 0.05, 1.00, "zoom-p97-top-600"),
]

for idx1, y0, y1, x0, x1, name in ZONES:
    page = doc[idx1 - 1]
    pix = page.get_pixmap(dpi=600)
    png = f"{OUT}/{name}.png"
    pix.save(png)
    im = Image.open(png)
    w, h = im.size
    crop = im.crop((int(w * x0), int(h * y0), int(w * x1), int(h * y1)))
    crop.save(f"{OUT}/{name}-crop.png")
    print(name, "full", im.size, "-> crop", crop.size)
