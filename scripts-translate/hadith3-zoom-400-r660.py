# -*- coding: utf-8 -*-
"""Minhāj — Rendus image leçon 11 hadith-3es (R660, slot pdf-mut23h2x-400).
300 dpi pages pleines 78-84 (p.84 = bannière leçon 12, borne sup à confirmer)
+ zooms 600 dpi des bandes discriminantes : bannière p.78 (médaillon 11,
objectifs, tamhīd), commentaire de Mālik p.79 (citations coraniques thuluth),
bande fiqh p.80 (citations + gloss), bloc الإعداد القبلي p.83 (mots glosés).
Sortie : tr-tmp/qa-crops-r660/."""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r660"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

# pages pleines 300 dpi
for p in range(78, 85):
    pix = doc[p - 1].get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72), alpha=False)
    out = os.path.join(OUT, f"hi-{p}-0{p}.png")
    pix.save(out)
    print(f"OK {out} — {pix.width}x{pix.height}")

JOBS = [
    (78, 600, 0.04, 0.02, 0.96, 0.42, "zoom-p78-banner"),
    (79, 600, 0.04, 0.04, 0.96, 0.50, "zoom-p79-comment"),
    (80, 600, 0.04, 0.50, 0.96, 0.97, "zoom-p80-fiqh"),
    (83, 600, 0.04, 0.55, 0.96, 0.97, "zoom-p83-idad"),
]
for page_no, dpi, x0, y0, x1, y1, name in JOBS:
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip, alpha=False)
    out = os.path.join(OUT, f"{name}.png")
    pix.save(out)
    print(f"OK {out} — {pix.width}x{pix.height}")
