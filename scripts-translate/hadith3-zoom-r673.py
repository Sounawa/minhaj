# -*- coding: utf-8 -*-
"""Minhāj — Rendus image leçon 406 hadith-3es (R673, slot pdf-mut23h2x-406).
Cours 17, bannière p.116, fenêtre sondée p.116-123 (fin de leçon p.123 :
istikhlass + iʿdād ; p.124 ouvre la leçon suivante ; bannière suivante p.129).
300 dpi pages pleines 116-123 + p.124/p.129 (contrôle bornes)
+ zooms 600 dpi des bandes discriminantes.
Sortie : tr-tmp/qa-crops-r673/."""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r673"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

# pages pleines 300 dpi
for p in list(range(116, 124)) + [124, 129]:
    pix = doc[p - 1].get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72), alpha=False)
    out = os.path.join(OUT, f"p-{p}.png")
    pix.save(out)
    print(f"OK {out} — {pix.width}x{pix.height}")

JOBS = [
    (116, 600, 0.04, 0.02, 0.96, 0.45, "zoom-p116-banner"),
    (117, 600, 0.04, 0.50, 0.96, 0.97, "zoom-p117-ayah"),
    (120, 600, 0.50, 0.45, 0.96, 0.75, "zoom-p120-maida"),
    (121, 600, 0.04, 0.02, 0.96, 0.30, "zoom-p121-top"),
    (124, 600, 0.04, 0.02, 0.96, 0.28, "zoom-p124-top"),
    (129, 600, 0.04, 0.02, 0.96, 0.45, "zoom-p129-banner"),
]
for page_no, dpi, x0, y0, x1, y1, name in JOBS:
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip, alpha=False)
    out = os.path.join(OUT, f"{name}.png")
    pix.save(out)
    print(f"OK {out} — {pix.width}x{pix.height}")
