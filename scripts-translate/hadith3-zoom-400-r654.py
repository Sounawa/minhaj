# -*- coding: utf-8 -*-
"""Minhāj — Zooms haute résolution des blocs calligraphiques coraniques R654
(slot pdf-mut23h2x-400) : le commentaire de Mālik sur le hadith dʿʿUmar porte
DEUX citations de Sūrat al-Ḥaǧǧ en calligraphie t̲ulut̲ avec étiquettes bleues
[سورة الحج الآية N] — contenu et chiffres à trancher par lecture VLM à 600 dpi
(les lectures 300 dpi divergent sur le texte calligraphique ; chiffres OCR
inversés par paires, JAMAIS deviner). Sortie : tr-tmp/qa-crops-r654/zoom-*.png."""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r654"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
JOBS = [
    # (page 1-based, zoom dpi, rect fractions x0,y0,x1,y1, name)
    (79, 600, 0.04, 0.06, 0.96, 0.46, "zoom-p79-comment"),   # bande du commentaire de Mālik + 2 citations
    (80, 600, 0.04, 0.52, 0.96, 0.97, "zoom-p80-fiqh"),      # bande فقه : citations calligraphiques + étiquettes + gloss
    (78, 600, 0.04, 0.02, 0.96, 0.42, "zoom-p78-banner"),    # bannière médaillon + objectifs + tamhīd haut
]

for page_no, dpi, x0, y0, x1, y1, name in JOBS:
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip, alpha=False)
    out = os.path.join(OUT, f"{name}.png")
    pix.save(out)
    print(f"OK {out} — {pix.width}x{pix.height}")
