# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 19 hadith-2es (slot pdf-20, R564).
Bornes (hadith2-map.py) : l19 زكاة خلطاء الماشية أهداف p.132 ;
l20 زكاة الثمار والحبوب أهداف p.139 → leçon = p.132-138.
Extraction large p.131-139 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l19-readable.txt"
FIRST, LAST = 131, 139

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
