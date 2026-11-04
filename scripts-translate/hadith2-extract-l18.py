# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 18 hadith-2es (slot pdf-19, R563).
Bornes (hadith2-map.py) : l18 زكاة الماشية أهداف p.125 ;
l19 زكاة خلطاء الماشية أهداف p.132 → leçon = p.125-131.
Extraction large p.124-132 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l18-readable.txt"
FIRST, LAST = 124, 132

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
