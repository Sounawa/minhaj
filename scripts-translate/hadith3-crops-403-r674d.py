# -*- coding: utf-8 -*-
"""Minhāj — CROPS finaux leçon 14 hadith-3es (R674-d, slot pdf-mut23h2x-403, أحكام مزدلفة).
Zones restées incertaines après lecture VLM r675/r674 + OCR fix : tranchées par
preuve image 1000 dpi (protocole R535-R547 : jamais de borne/mot deviné).
Sorties : tr-tmp/qa-crops-r674d/x{N}-{nom}.png
Source : content/textbooks-src/hadith-3-iadadi_text.pdf — pages PDF 97-102."""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r674d"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
DPI = 1000

# (nom, page_pdf_1-indexée, y0_frac, y1_frac)
CROPS = [
    ("x0-p97-top",      97, 0.00, 0.32),
    ("x1a-p98-h1160",   98, 0.28, 0.52),
    ("x1b-p98-notice",  98, 0.55, 0.80),
    ("x2-p99-taakhir",  99, 0.28, 0.64),
    ("x3-p100-mawqif", 100, 0.03, 0.40),
    ("x4-p100-jamian", 100, 0.40, 0.76),
    ("x5-p101-adhan",  101, 0.03, 0.38),
    ("x6-p101-athar",  101, 0.55, 0.98),
    ("x7-p102-talil1", 102, 0.08, 0.46),
    ("x8-p102-talil2", 102, 0.46, 0.80),
]

mat = fitz.Matrix(DPI / 72, DPI / 72)
for nom, pg, f0, f1 in CROPS:
    page = doc[pg - 1]
    r = page.rect
    clip = fitz.Rect(r.width * 0.03, r.height * f0, r.width * 0.97, r.height * f1)
    pix = page.get_pixmap(matrix=mat, clip=clip)
    path = f"{OUT}/{nom}.png"
    pix.save(path)
    print(f"OK {path} {pix.width}x{pix.height}")
