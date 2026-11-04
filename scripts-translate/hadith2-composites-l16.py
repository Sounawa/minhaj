# -*- coding: utf-8 -*-
"""R560 — Composites de preuve leçon 16 (pdf-17).
Comp-300 : zones de wording (300 dpi, pleine largeur) — p112 objectifs+āya,
p113 citations+glossaire, p115 عمشر+citation 678, p117 Bukhārī.
Comp-600 : zones de NUMÉROS (600 dpi) — āya Tawba p112/p116, Muwaṭṭaʾ 680/684,
citation 678 p115, عمشر p115."""
import fitz
import os

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r560"
doc = fitz.open(PDF)
os.makedirs(OUT, exist_ok=True)

# (page, x0, y0, x1, y1, dpi, label)
STRIPS_300 = [
    (112, 20, 260, 620, 340, 300, "p112-objectifs"),
    (112, 20, 390, 620, 445, 300, "p112-aya"),
    (113, 20, 60, 620, 220, 300, "p113-citations"),
    (113, 20, 460, 620, 690, 300, "p113-glossaire"),
    (115, 20, 55, 620, 110, 300, "p115-3omshour"),
    (115, 20, 635, 620, 725, 300, "p115-citation678"),
    (117, 20, 100, 620, 225, 300, "p117-boukhari"),
]
STRIPS_600 = [
    (112, 20, 390, 620, 445, 600, "n-aya-p112"),
    (116, 20, 285, 620, 335, 600, "n-aya-p116"),
    (116, 20, 305, 620, 370, 600, "n-680-p116"),
    (116, 20, 485, 620, 555, 600, "n-684-p116"),
    (115, 20, 630, 620, 730, 600, "n-678-p115"),
    (115, 20, 50, 620, 115, 600, "n-3omshour-p115"),
]


def strip(spec):
    pg, x0, y0, x1, y1, dpi, label = spec
    pix = doc[pg - 1].get_pixmap(
        matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=fitz.Rect(x0, y0, x1, y1)
    )
    return pix, label


def composite(strips, path):
    pixes = [strip(s) for s in strips]
    w = max(p.width for p, _ in pixes) + 40
    h = sum(p.height for p, _ in pixes) + 30 * (len(pixes) + 1)
    canvas = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, w, h), False)
    canvas.set_rect(canvas.irect, (255, 255, 255))
    y = 30
    for p, _ in pixes:
        canvas.copy(p, fitz.IRect(20, y, 20 + p.width, y + p.height))
        y += p.height + 30
    canvas.save(path)
    print(f"{path}: {w}x{h}")


composite(STRIPS_300, f"{OUT}/comp-r560-300.png")
composite(STRIPS_600, f"{OUT}/comp-r560-600.png")
