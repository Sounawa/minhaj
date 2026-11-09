# -*- coding: utf-8 -*-
"""Minhāj R664 — crops par bande y (lignes du tableau تراجم الأعلام p.132-134).
Bandes dérivées des blocs texte (sondage fitz) ; rendu 1200 dpi."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r664"

BANDS = {
    131: [("r0-qari", 138, 217), ("r1-rajab", 217, 311), ("r2-shafii", 311, 408),
          ("r3-raz", 408, 482), ("r4-daraq", 482, 556), ("r5-zark", 556, 654)],
    132: [("r0-salah", 48, 209), ("r1-abd", 209, 344), ("r2-hakim", 344, 460),
          ("r3-iraqi", 460, 572), ("r4-khatib", 572, 690)],
    133: [("r0-dhahabi", 53, 144), ("r1-sakhawi", 144, 235), ("r2-suyuti", 235, 350),
          ("r3-iyad", 350, 507), ("r4-nawawi", 507, 620)],
}

doc = fitz.open(PDF)
for pno, rows in BANDS.items():
    page = doc[pno]
    rect = page.rect
    for name, y0, y1 in rows:
        clip = fitz.Rect(38, y0, 424, y1)  # table seule (marges blanches exclues)
        pix = page.get_pixmap(dpi=600, clip=clip)
        f = f"{OUT}/row-p{pno+1}-{name}.png"
        pix.save(f)
        print(f"row-p{pno+1}-{name}: y{y0}-{y1} → {pix.width}x{pix.height}")
