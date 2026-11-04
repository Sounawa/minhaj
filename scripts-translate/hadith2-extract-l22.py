# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 22 hadith-2es (slot pdf-23, R567).
Bornes (hadith2-map.py) : l22 زكاة الفطر أهداف p.152 ;
l23 أحكام الصيام 1 أهداف p.158 → leçon = p.152-157.
Extraction large p.151-158 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l22-readable.txt"
FIRST, LAST = 151, 158

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
