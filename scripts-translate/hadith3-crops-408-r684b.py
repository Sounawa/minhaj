# -*- coding: utf-8 -*-
"""R684-bis — deux ultra-zooms décisifs p.135 : bandeau-titre de l'encadré
(الاستشهاد ? الاستثمار ?) et dernière ligne de l'athar 1183 (فَيُفِيض ?
فَيُطِيف ? إلى الذي قد أفاض ?). Protocole : jamais deviné, preuve image."""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r684"
doc = fitz.open(PDF)
DPI = 900

CROPS = [
    # (nom, page, x0, x1, y0, y1)
    ("t135-bandeau", 135, 0.30, 0.75, 0.015, 0.065),  # pastille + mot bleu seul
    ("t135-lastline", 135, 0.05, 0.95, 0.185, 0.27),   # dernière ligne complète
]
for nom, pg, fx0, fx1, fy0, fy1 in CROPS:
    page = doc[pg - 1]
    r = page.rect
    clip = fitz.Rect(r.width * fx0, r.height * fy0, r.width * fx1, r.height * fy1)
    pix = page.get_pixmap(matrix=fitz.Matrix(DPI / 72, DPI / 72), clip=clip)
    path = f"{OUT}/{nom}.png"
    pix.save(path)
    print(f"OK {path} {pix.width}x{pix.height}")
