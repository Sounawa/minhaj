#!/usr/bin/env python3
"""R636 — recadrages des numéros de citation via recherche bbox fitz, méthode r634."""
import fitz, os

PDF = "content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "tr-tmp/r636"
doc = fitz.open(PDF)
os.makedirs(OUT, exist_ok=True)

found = 0
for pno in range(39, 45):
    pg = doc[pno - 1]
    hits = []
    for needle in ("رقم", "مقر"):
        try:
            hits = pg.search_for(needle)
        except Exception:
            hits = []
        if hits:
            break
    for i, rect in enumerate(hits):
        r = pg.rect
        clip = fitz.Rect(max(rect.x0 - 120, 0), max(rect.y0 - 12, 0),
                         min(rect.x1 + 60, r.width), min(rect.y1 + 12, r.height))
        pix = pg.get_pixmap(matrix=fitz.Matrix(10, 10), clip=clip)
        path = f"{OUT}/num-p{pno:03d}-{i}.png"
        pix.save(path)
        print(path, f"{pix.width}x{pix.height}")
        found += 1
print("citations localisées:", found)
