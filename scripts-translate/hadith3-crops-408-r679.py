# -*- coding: utf-8 -*-
"""Minhāj — CROPS de preuve leçon 408 hadith-3es (R679, slot pdf-mut23h2x-408,
ما يفعله الحاج يوم النحر). Zones incertaines après OCR couches FIX/BRUTE —
tranchées par preuve image 900 dpi (protocole R535-R679 : jamais de numéro ni
de borne deviné). Sorties : tr-tmp/qa-crops-r679/x{N}-{nom}.png
Source : content/textbooks-src/hadith-3-iadadi_text.pdf — pages PDF 129-134."""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r679"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
DPI = 900

# (nom, page_pdf_1-indexée, y0_frac, y1_frac)
CROPS = [
    ("x0-p129-annonce",   129, 0.45, 0.98),
    ("x1-p130-aya",       130, 0.28, 0.52),
    ("x2-p130-h1173",     130, 0.52, 0.95),
    ("x3-p131-h1267",     131, 0.03, 0.40),
    ("x4-p131-hafsa",     131, 0.40, 0.72),
    ("x5-p131-notice",    131, 0.72, 0.98),
    ("x6-p132-gloses",    132, 0.03, 0.40),
    ("x7-p132-fiqh1",     132, 0.40, 0.70),
    ("x8-p132-amr",       132, 0.70, 0.98),
    ("x9-p133-taqdim",    133, 0.03, 0.30),
    ("x10-p133-makan",    133, 0.30, 0.52),
    ("x11-p133-mubashara",133, 0.52, 0.72),
    ("x12-p133-khutba",   133, 0.72, 0.98),
    ("x13-p134-khutba2",  134, 0.03, 0.30),
    ("x14-p134-aya",      134, 0.28, 0.46),
    ("x15-p134-tahlul2",  134, 0.46, 0.82),
    ("x16-p134-taqwim",   134, 0.82, 0.98),
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
