# -*- coding: utf-8 -*-
"""Minhāj — Extraction couche texte annexe 29 hadith-2es (slot pdf-30, R574).
Sortie : tr-tmp/hadith2-l30-readable.txt (pages 198-203, marqueurs de page).
Bornes larges : p.198 (blanche, preuve R573) + annexe فهرس الأعلام (199-202) + tête annexe 30 (203)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l30-readable.txt"
FIRST, LAST = 198, 203

doc = fitz.open(PDF)
chunks = []
total = 0
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    total += len(txt)
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
open(OUT, "w", encoding="utf-8").write("\n".join(chunks))
print(f"OK {OUT} — {total} car, pages {FIRST}-{LAST}")
