# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 16 hadith-2es (slot pdf-17, R560).
Bornes (hadith2-map.py) : l16 أهداف p.112 ; l17 أهداف p.118 → leçon = p.112-117.
Extraction large p.111-118 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l16-readable.txt"
FIRST, LAST = 111, 118

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
