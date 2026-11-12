#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R690 — rendus PDF leçon 412 hadith-3es (p.152-158, la 'umra).
Pages plein-cadre ~1500px pour lectures VLM + planche de contact."""
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/pages-412"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
print("pages PDF:", doc.page_count)
for pno in range(152, 159):  # 152..158 inclus (1-based -> index pno-1)
    page = doc[pno - 1]
    # zoom pour largeur ~1500 px
    w = page.rect.width
    zoom = 1500.0 / w
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    f = f"{OUT}/p{pno}.png"
    pix.save(f)
    print(f, pix.width, "x", pix.height)

# planche de contact : coordonnées utiles pour microcrops ultérieurs
for pno in range(152, 159):
    page = doc[pno - 1]
    r = page.rect
    print(f"p{pno}: rect {r.width:.0f}x{r.height:.0f}")
