# -*- coding: utf-8 -*-
"""R560 — Composites v2 calibrés (positions issues de hadith2-calibrate-l16.py).
Comp300 : wording — p112 objectifs+āya, p113 glossaire (suite), p117 box Bukhārī.
Comp600A : numéros — āya p112, 675/677/681 p113, 672 p114, 673+عمشر p115, 676 p115.
Comp600B : numéros — 678 p115, 679/āya104/680/684 p116, 674 p112."""
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r560"
doc = fitz.open(PDF)

C300 = [
    (112, 20, 160, 620, 560, 300, "p112-objectifs-tamhid-aya"),
    (113, 20, 683, 620, 806, 300, "p113-glossaire-suite"),
    (117, 20, 55, 620, 300, 300, "p117-boukhari-box"),
]
C600A = [
    (112, 20, 400, 620, 500, 600, "p112-aya-600"),
    (113, 20, 108, 620, 292, 600, "p113-675-677-681"),
    (114, 20, 578, 620, 622, 600, "p114-672"),
    (115, 20, 98, 620, 142, 600, "p115-673-3omshour"),
    (115, 20, 526, 620, 574, 600, "p115-676"),
]
C600B = [
    (115, 20, 686, 620, 744, 600, "p115-678-quote"),
    (116, 20, 128, 620, 174, 600, "p116-679"),
    (116, 20, 308, 620, 357, 600, "p116-aya104"),
    (116, 20, 343, 620, 402, 600, "p116-680"),
    (116, 20, 533, 620, 582, 600, "p116-684"),
    (112, 20, 598, 620, 647, 600, "p112-674"),
]


def composite(strips, path):
    pixes = []
    for pg, x0, y0, x1, y1, dpi, label in strips:
        pix = doc[pg - 1].get_pixmap(
            matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=fitz.Rect(x0, y0, x1, y1)
        )
        pixes.append(pix)
    w = max(p.width for p in pixes) + 40
    h = sum(p.height for p in pixes) + 30 * (len(pixes) + 1)
    canvas = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, w, h), False)
    canvas.set_rect(canvas.irect, (255, 255, 255))
    y = 30
    for p in pixes:
        canvas.copy(p, fitz.IRect(20, y, 20 + p.width, y + p.height))
        y += p.height + 30
    canvas.save(path)
    print(f"{path}: {w}x{h}")


composite(C300, f"{OUT}/comp-r560-w300.png")
composite(C600A, f"{OUT}/comp-r560-n600a.png")
composite(C600B, f"{OUT}/comp-r560-n600b.png")
