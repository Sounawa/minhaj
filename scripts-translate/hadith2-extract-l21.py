# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 21 hadith-2es (slot pdf-22, R566).
Bornes (hadith2-map.py) : l21 ما لا زكاة فيه والمستحقون أهداف p.146 ;
l22 زكاة الفطر أهداف p.152 → leçon = p.146-151.
Extraction large p.145-152 pour preuve des bornes (jamais devinées).
Couche texte DÉGRADÉE : carte des sections seulement, jamais vérité de rendu."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l21-readable.txt"
FIRST, LAST = 145, 152

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")
