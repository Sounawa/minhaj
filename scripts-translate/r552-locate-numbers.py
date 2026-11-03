# -*- coding: utf-8 -*-
"""R552 — localisation des tokens numériques suspects sur pages 79-86 (leçon 11 hadith-2es).
Sortie : liste bbox par token ; alimente les crops 600-1200 dpi."""
import fitz, re

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
doc = fitz.open(PDF)
for pno in range(78, 86):  # pages 79-86 (0-based 78-85)
    page = doc[pno]
    print(f"===== PAGE {pno+1} (rect {page.rect.width:.0f}x{page.rect.height:.0f}) =====")
    for w in page.get_text("words"):
        x0, y0, x1, y1, word = w[0], w[1], w[2], w[3], w[4]
        # tokens numériques ou référentiels موطأ
        if re.search(r"[0-9٠-٩]{2,}", word) or "موطأ" in word or "موط" in word:
            print(f"  [{x0:6.1f},{y0:6.1f},{x1:6.1f},{y1:6.1f}] {word!r}")
