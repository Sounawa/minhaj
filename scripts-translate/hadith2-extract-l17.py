# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 17 hadith-2es (slot pdf-18, R562).
Bornes (hadith2-map.py) : l17 زكاة الميراث والدين والعروض أهداف p.118 ;
l18 زكاة الماشية أهداف p.125 → leçon = p.118-124.
Extraction large p.117-125 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l17-readable.txt"
FIRST, LAST = 117, 125

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
