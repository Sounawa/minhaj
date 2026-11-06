# -*- coding: utf-8 -*-
"""Minhāj — Extraction multicouche leçon 4 hadith-3es (slot pdf-mut23h2x-393,
R628). Mécanique hadith3-extract-392.py (R624/R627) adaptée : bornes larges
fin l3 (30) + l4 أنواع الإحرام (31-38) + tête l5 (39).
Sortie : tr-tmp/hadith3-l393-raw.txt (couche miroir) + hadith3-l393-fixed.txt
(décode hadith3-l1-fixed : chaque mot retourné, ordre des mots inchangé —
la lecture vraie inverse AUSSI l'ordre des mots)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT_RAW = "/home/z/my-project/tr-tmp/hadith3-l393-raw.txt"
OUT_FIX = "/home/z/my-project/tr-tmp/hadith3-l393-fixed.txt"
FIRST, LAST = 30, 39  # bornes larges, tranchées par sondage + lecture directe


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


doc = fitz.open(PDF)
chunks_raw, chunks_fix = [], []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks_raw.append(f"===== PAGE {p + 1} =====\n{txt}")
    fixed = "\n".join(fix_line(l) for l in txt.split("\n"))
    chunks_fix.append(f"===== PAGE {p + 1} =====\n{fixed}")
open(OUT_RAW, "w", encoding="utf-8").write("\n".join(chunks_raw))
open(OUT_FIX, "w", encoding="utf-8").write("\n".join(chunks_fix))
print(f"OK {OUT_RAW} — {sum(len(c) for c in chunks_raw)} car, pages {FIRST}-{LAST}")
print(f"OK {OUT_FIX} — {sum(len(c) for c in chunks_fix)} car")
