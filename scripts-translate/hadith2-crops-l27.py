# -*- coding: utf-8 -*-
"""R572 — micro-crops 900-2400 dpi pour adjudication À L'ŒIL (leçon 27, p.184-191).
Re-génération post-recyclage n°6 (lectures déjà tenues au journal de session —
8 pages 300 dpi + 6 chiffres serrés + 8 libellés, tranchés avant le recyclage)."""
import os
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r572"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

ZONES = [
    (184, 10, 592, 1880, 2380, 900, "w-tamhid-full"),
    (185, 10, 592, 240, 1210, 900, "w-umar-zayd"),
    (185, 10, 592, 1270, 2470, 900, "w-aicha-anas-malik"),
    (186, 10, 592, 2080, 2320, 900, "w-matn-l186"),
    (187, 10, 592, 890, 1500, 900, "w-846-nasiyan"),
    (187, 10, 592, 1780, 2660, 900, "w-aya-844-843"),
    (188, 10, 592, 940, 1140, 900, "w-hajj-aya"),
    (188, 10, 592, 2780, 3040, 900, "w-861"),
    (189, 10, 592, 950, 1130, 900, "w-854-855"),
    (189, 10, 592, 1880, 2410, 900, "w-856-857"),
    (190, 10, 592, 330, 440, 900, "w-858"),
    (190, 10, 592, 2360, 3000, 900, "w-istithmar-ayas"),
    (191, 10, 592, 380, 600, 900, "w-853-fin"),
    (185, 15, 225, 1080, 1230, 2400, "n-840"),
    (187, 96, 312, 1810, 1990, 2400, "n-aya184"),
    (188, 168, 264, 990, 1120, 2400, "n-hajj28"),
    (190, 432, 580, 2870, 2990, 2400, "n-195"),
    (184, 468, 596, 2060, 2220, 2400, "n-856"),
    (184, 84, 384, 2210, 2375, 2400, "n-183-857"),
]

for pno, x0, x1, y0, y1, dpi, tag in ZONES:
    page = doc[pno - 1]
    clip = fitz.Rect(x0, y0 * 72 / 300, x1, y1 * 72 / 300)
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{OUT}/{tag}.png")
print(f"DONE — {len(ZONES)} crops dans {OUT}")
