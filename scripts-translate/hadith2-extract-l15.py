# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 15 hadith-2es (slot pdf-16, R553).
Bornes (hadith2-map.py) : l15 أهداف p.105 ; l16 أهداف p.112 → leçon = p.105-111.
Extraction large p.104-112 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l15-readable.txt"
FIRST, LAST = 104, 112

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
