# -*- coding: utf-8 -*-
"""Minhāj — Ré-extraction couche texte leçon 28 hadith-2es (slot pdf-29, R573).
Sortie : tr-tmp/hadith2-l29-readable.txt (pages 191-199, marqueurs de page)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l29-readable.txt"
FIRST, LAST = 191, 199  # bornes larges : fin l27 (191) + l28 (192-198) + tête annexe (199)

doc = fitz.open(PDF)
chunks = []
total = 0
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    total += len(txt)
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
open(OUT, "w", encoding="utf-8").write("\n".join(chunks))
print(f"OK {OUT} — {total} car, pages {FIRST}-{LAST}")
