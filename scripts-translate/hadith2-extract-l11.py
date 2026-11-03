# -*- coding: utf-8 -*-
"""Minhāj — Ré-extraction couche texte leçon 11 hadith-2es (slot pdf-12, R547).
Matière perdue au recyclage sandbox (fichiers non versionnés effacés).
Sortie : tr-tmp/hadith2-l11-readable.txt (pages 79-86, marqueurs de page)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l11-readable.txt"
FIRST, LAST = 79, 86  # bornes larges : fin l10 (79) + l11 (80-85) + tête l12 (86)

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
open(OUT, "w", encoding="utf-8").write("\n".join(chunks))
print(f"OK {OUT} — {len(chr(10).join(chunks))} car, pages {FIRST}-{LAST}")
