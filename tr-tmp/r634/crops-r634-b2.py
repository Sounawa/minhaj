#!/usr/bin/env python3
"""R634 — round 2 : bandes serrées 576-720 dpi pour zones divergentes."""
import fitz, os

PDF = "content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "tr-tmp/r634"
doc = fitz.open(PDF)

def crop(pno, y0f, y1f, name, x0f=0.04, x1f=0.98, zoom=8):
    pg = doc[pno-1]
    r = pg.rect
    clip = fitz.Rect(r.width*x0f, r.height*y0f, r.width*x1f, r.height*y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    pix.save(f"{OUT}/{name}.png")
    print(name, pix.width, "x", pix.height)

crop(33, 0.05, 0.32, "c2-p033-glosses")      # 4 gloses + استخلص heading
crop(34, 0.30, 0.62, "c2-p034-bukhari")      # أفضليّة + citation Buḫārī
crop(34, 0.60, 0.80, "c2-p034-fin-heading")  # ligne فكيف + heading ثانيا القران
crop(35, 0.56, 0.95, "c2-p035-fawaid")       # صنعهها + فوائد paragraph
crop(37, 0.28, 0.75, "c2-p037-tamattu")      # صنعت/صنعه + الشيباني + قول سعد
