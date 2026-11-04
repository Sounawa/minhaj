# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 26 hadith-2es (slot pdf-27, R571).
Bornes (hadith2-map.py) : l26 p.177-183 ; l27 القضاء والفدية أهداف p.184.
Extraction large p.176-184 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l26-readable.txt"
FIRST, LAST = 176, 184

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
