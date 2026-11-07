# -*- coding: utf-8 -*-
# R639 — recadrages d'adjudication pour la leçon 14 (pdf-mut23h2u-268, p.74-77)
# Zones dégradées/à trancher, rendues à 432 dpi (zoom 6) pour lecture VLM/OCR.
import fitz, os

BOOK = "content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "tr-tmp/qa-crops-r639"
os.makedirs(OUT, exist_ok=True)

# (nom, page, x0, y0, x1, y1) en points PDF
ZONES = [
    ("p074-objectifs",   74,  35, 120, 560, 228),
    ("p074-gid",         74,  35, 225, 560, 395),
    ("p074-matn",        74,  35, 430, 560, 570),
    ("p074-istikhlas",   74,  35, 555, 560, 762),
    ("p075-tahlil-s1",   75,  35,  95, 560, 330),
    ("p075-sabab2",      75,  35, 325, 560, 402),
    ("p075-muallaq-def", 75,  35, 410, 560, 625),
    ("p075-farq",        75,  35, 618, 560, 742),
    ("p076-band",        76,  35,  55, 560, 108),
    ("p076-suwar",       76,  35, 100, 560, 292),
    ("p076-hukm",        76,  35, 290, 560, 542),
    ("p076-zuhri",       76,  35, 540, 560, 645),
    ("p077-taqwim",      77,  35,  55, 560, 185),
    ("p077-istithmar",   77,  35, 188, 560, 355),
    ("p077-ahtadi",      77,  35, 415, 560, 600),
]
doc = fitz.open(BOOK)
for name, p, x0, y0, x1, y1 in ZONES:
    pg = doc[p-1]
    clip = fitz.Rect(x0, y0, x1, y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(6, 6), clip=clip)
    path = f"{OUT}/{name}.png"
    pix.save(path)
    print(name, pix.width, "x", pix.height, os.path.getsize(path), "octets")
