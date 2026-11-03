# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 13 hadith-2es (slot pdf-14, R550).
Bornes (hadith2-map.py) : l13 أهداف p.91 ; l14 أهداف p.98 → leçon = p.91-97.
Extraction large p.90-98 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l13-readable.txt"
FIRST, LAST = 90, 98

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
