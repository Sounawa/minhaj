# -*- coding: utf-8 -*-
"""Minhāj — Extraction couche texte leçon 2 hadith-3es (slot pdf-mut23h2x-391).
Mécanique hadith3-extract-392.py (R625) adaptée à la leçon 2 (R631).
Bornes larges : fin l1 (16) + l2 لباس المحرم (17-24) + tête l3 تطييب (25).
Sortie : tr-tmp/hadith3-l391-raw2.txt (marqueurs de page) — le WIP abandonné
tr-tmp/hadith3-l391-raw.txt (p.17-24) est réutilisable mais on ré-extrait avec
marge de contrôle pour tracer la borne inférieure (p.16 = iʿdād de fin l1)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith3-l391-raw2.txt"
FIRST, LAST = 16, 25  # bornes larges, sondage + double preuve

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
open(OUT, "w", encoding="utf-8").write("\n".join(chunks))
print(f"OK {OUT} — {sum(len(c) for c in chunks)} car, pages {FIRST}-{LAST}")
