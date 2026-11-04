# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 27 hadith-2es (slot pdf-28, R573).
Bornes (hadith2-map.py + sondage) : l27 p.184-191 القضاء والفدية في الصيام ;
bannière أهداف leçon 27 = p.184 ; أهداف leçon 28 (فضل الصيام) = p.192.
Extraction large p.183-192 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l27-readable.txt"
FIRST, LAST = 183, 192

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
