# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 14 hadith-2es (slot pdf-15, R552).
Bornes (hadith2-map.py) : l14 أهداف p.98 ; l15 أهداف p.105 → leçon = p.98-104.
Extraction large p.97-105 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l14-readable.txt"
FIRST, LAST = 97, 105

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
