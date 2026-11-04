# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 25 hadith-2es (slot pdf-26, R571).
Bornes (hadith2-map.py + sondage OCR 300dpi) : l25 أهداف الدرس p.171 ;
l26 أهداف الدرس p.177 → leçon = p.171-176.
Extraction large p.170-177 pour preuve des bornes (jamais devinées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l25-readable.txt"
FIRST, LAST = 170, 177  # bornes larges : fin l24 (170) + l25 (171-176) + tête l26 (177)

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
