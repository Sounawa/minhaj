#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R691 — rendus PDF leçon 413 hadith-3es (p.158-163, la uḍḥiya)
+ couche logique. Pages plein-cadre ~1500px pour lectures VLM."""
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/pages-413"
LOG = "/home/z/my-project/tr-tmp/h3-413-logical.txt"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
print("pages PDF:", doc.page_count)
for pno in range(158, 164):  # 158..163 inclus (1-based -> index pno-1)
    page = doc[pno - 1]
    w = page.rect.width
    zoom = 1500.0 / w
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
    f = f"{OUT}/p{pno}.png"
    pix.save(f)
    print(f, pix.width, "x", pix.height, "| rect", f"{page.rect.width:.0f}x{page.rect.height:.0f}")

# couche logique : inverser chaque mot PUIS inverser la liste de mots
out = []
for p in range(158 - 1, 163):
    out.append(f"===== PAGE {p + 1} — LOGIQUE =====")
    for line in doc[p].get_text("text").split("\n"):
        words = [w[::-1] for w in line.split(" ") if w.strip()]
        if words:
            out.append(" ".join(reversed(words)))
open(LOG, "w", encoding="utf-8").write("\n".join(out))
print("OK", LOG, "—", len(out), "lignes")
