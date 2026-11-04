# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 20 hadith-2es (slot pdf-21, R565).
Bornes (hadith2-map.py) : l20 زكاة الثمار والحبوب أهداف الدرس p.139 ;
l21 ما لا زكاة فيه والمستحقون أهداف p.146 → leçon = p.139-145.
Extraction large p.138-146 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l20-readable.txt"
FIRST, LAST = 138, 146

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
