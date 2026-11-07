# -*- coding: utf-8 -*-
"""Minhāj — Inspections image leçon 7 hadith-3es (slot pdf-mut23h2x-396).
Méthode R638 : bandes d'image localisées 600-900 dpi sur les zones incertaines
de p.52-57 (titres/bannière graphique absents de la couche texte, numéros de
référence à trancher par la loi d'inversion OCR, chaînes et matns corrompus).
Sortie : tr-tmp/qa-crops-r640/*.png — lecture sélective ensuite."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r640"

doc = fitz.open(PDF)

# (page 1-based, y0, y1 en points, dpi, suffixe)
CROPS = [
    # p.52 — bannière graphique + objectifs + tamhīd ; puis question + رقم 999/939
    (52, 0.00, 0.36, 600, "p52-a-banniere-objectifs"),
    (52, 0.30, 0.62, 600, "p52-b-question-num"),
    # p.53 — chaîne + matn corrompus (hadith أبو قتادة) + رقم 1007 ; bio + شرح
    (53, 0.05, 0.38, 700, "p53-a-isnad-matn"),
    (53, 0.34, 0.66, 700, "p53-b-matn-fin-num"),
    (53, 0.62, 0.86, 700, "p53-c-bio-charh"),
    # p.54 — règle + الخطابي + التحفة ; شواهد طريف/عفات + 1001/1002
    (54, 0.05, 0.38, 700, "p54-a-regle"),
    (54, 0.33, 0.64, 700, "p54-b-chawahid"),
    # p.55 — ثانيا + règle ; زيد بن أسلم + جابر + القديد ; 1008/1015
    (55, 0.22, 0.55, 700, "p55-b-zayd-jabir"),
    (55, 0.50, 0.80, 700, "p55-c-qadid-risala"),
    # p.56 — الصلْت بن جعدة + verset coranique ; عائشة + 1019/1020
    (56, 0.20, 0.52, 700, "p56-b-salt-verse"),
    (56, 0.48, 0.80, 700, "p56-c-aicha-num"),
    # p.57 — النص المضطر + رقم 1021 (convergence à confirmer)
    (57, 0.20, 0.50, 700, "p57-a-mudtarr-num"),
]

import os
os.makedirs(OUT, exist_ok=True)
for pg, f0, f1, dpi, name in CROPS:
    page = doc[pg - 1]
    r = page.rect
    clip = fitz.Rect(0, r.height * f0, r.width, r.height * f1)
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    p = f"{OUT}/{name}.png"
    pix.save(p)
    print(f"OK {p} {pix.width}x{pix.height}")
print(f"{len(CROPS)} bandes écrites dans {OUT}")
