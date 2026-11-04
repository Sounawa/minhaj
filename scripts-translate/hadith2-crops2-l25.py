# -*- coding: utf-8 -*-
"""R571 — crops des zones de renvois Muwaṭṭaʾ (repérage par jetons numériques de la couche)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r571"
doc = fitz.open(PDF)

# (page, y du jeton, étiquette) — y issus du repérage hadith2-tokens-l25.py
ZONES = [
    (172, 129.2, "hadith1-818"),
    (172, 190.8, "hadith2-821"),
    (172, 315.6, "hadith3-826"),
    (173, 533.0, "desm-wasum-819"),
    (174, 307.9, "ata-819"),
    (174, 705.4, "hijama-822"),
    (175, 315.4, "aicha-825"),
    (176, 238.9, "istihlal-824"),
]

for pno, y, tag in ZONES:
    page = doc[pno - 1]
    clip = fitz.Rect(25, y - 16, 470, y + 26)
    for zoom, suf in ((10, "720"), (20, "1440")):
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
        pix.save(f"{OUT}/c-r571-{tag}-{suf}.png")
print("OK")
