# -*- coding: utf-8 -*-
"""R560 — Crops individuels calibrés (pas de composite, bug canvas écarté)."""
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r560"
doc = fitz.open(PDF)

CROPS = [
    (112, 20, 385, 620, 560, 600, "z-p112-obj23-aya"),
    (113, 20, 683, 620, 806, 600, "z-p113-glossaire-suite"),
    (117, 20, 55, 620, 300, 300, "z-p117-boukhari"),
    (115, 20, 98, 620, 142, 600, "z-p115-673-3omshour"),
    (116, 20, 343, 620, 402, 600, "z-p116-680"),
    (115, 20, 686, 620, 744, 600, "z-p115-678-quote"),
]
for pg, x0, y0, x1, y1, dpi, name in CROPS:
    pix = doc[pg - 1].get_pixmap(
        matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=fitz.Rect(x0, y0, x1, y1)
    )
    pix.save(f"{OUT}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")
