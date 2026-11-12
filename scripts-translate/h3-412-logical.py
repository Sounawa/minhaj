# -*- coding: utf-8 -*-
"""Reconstruction logique du texte PDF hadith-3, pages 152-158 (leçon 412).
Chaque ligne du layer PDF est en ordre VISUEL : mots inversés ET ordre de mots
inversé. Reconstruction : inverser chaque mot PUIS inverser la liste de mots.
Sortie : tr-tmp/h3-412-logical.txt"""
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/h3-412-logical.txt"
FIRST, LAST = 152, 158

doc = fitz.open(PDF)
out = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    out.append(f"===== PAGE {p + 1} — LOGIQUE =====")
    for line in doc[p].get_text("text").split("\n"):
        words = [w[::-1] for w in line.split(" ") if w.strip()]
        if words:
            out.append(" ".join(reversed(words)))
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print(f"OK {OUT} — {len(out)} lignes")
