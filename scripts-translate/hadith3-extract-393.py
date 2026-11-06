# -*- coding: utf-8 -*-
"""Minhāj — Extraction couche texte leçon 3 hadith-3es (slot pdf-mut23h2x-393).
Mécanique hadith2-extract-l11.py (R535-R547) adaptée au front hadith-3es (R624).
Bornes larges : fin l3 (30) + l4 أنواع الإحرام (31-38) + tête l5 (39).
Sortie : tr-tmp/hadith3-l393-raw.txt (marqueurs de page)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith3-l393-raw.txt"
FIRST, LAST = 30, 39  # bornes larges : fin l3 (30) + l4 أنواع الإحرام (31-38?) + tête l5 (39?)

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
open(OUT, "w", encoding="utf-8").write("\n".join(chunks))
print(f"OK {OUT} — {sum(len(c) for c in chunks)} car, pages {FIRST}-{LAST}")
