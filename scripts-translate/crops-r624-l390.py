#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R624 — crops leçon 1 hadith-3es (p.10-16) : pages entières + bandes de
numéros de hadith (l'OCR inverse les chiffres par paires — jamais deviné)."""
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r624"

doc = fitz.open(PDF)


def full(p, zoom=220 / 72):
    pg = doc[p - 1]
    pix = pg.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
    pix.save(f"{OUT}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


def band(p, name, y0, y1, zoom=600 / 72):
    """Bande horizontale de la page p (y en fraction de hauteur)."""
    pg = doc[p - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * 0.05, r.height * y0, r.width * 0.95, r.height * y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    pix.save(f"{OUT}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


for p in (10, 11, 12, 13, 14, 15, 16):
    name = f"p{p}-full"
    full(p)

# bandes « numéro de hadith » : les crochets [الموطأ رقم] sont en marge gauche
band(10, "p10-nums", 0.55, 0.98)
band(14, "p14-nums", 0.10, 0.90)
band(11, "p11-bottom", 0.55, 1.00)
band(12, "p12-top", 0.00, 0.30)
band(12, "p12-full", 0.00, 1.00, zoom=260 / 72)
band(15, "p15-top", 0.00, 0.55)
band(15, "p15-bottom", 0.50, 1.00)
doc.close()
print("OK crops r624")
