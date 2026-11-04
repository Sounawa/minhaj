# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 24 hadith-2es (slot pdf-25, R569 subagent).
Bornes (hadith2-map.py) : l24 أحكام الصيام 2 أهداف p.165 ;
l25 أحكام الصيام 3 أهداف p.171 → leçon = p.165-170.
Extraction large p.164-171 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l24-readable.txt"
FIRST, LAST = 164, 171

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
