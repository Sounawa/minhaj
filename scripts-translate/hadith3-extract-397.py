# -*- coding: utf-8 -*-
"""Minhāj — Extraction couche texte leçon 8 hadith-3es (slot pdf-mut23h2x-397).
Mécanique hadith3-extract-396.py (R640) — leçon 8 « أحكام صيد المحرم والجزاء فيه »,
ouverture l8 = p.58 (bannière + objectifs, R640 passation), clôture l8 = À TRANCHER
PAR SONDAGE (bornes provisoires 58-70). Sortie : tr-tmp/hadith3-l397-raw.txt —
DEUX couches par page (fix + brute)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith3-l397-raw.txt"
FIRST, LAST = 58, 70

doc = fitz.open(PDF)


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    fixed = "\n".join(fix_line(l) for l in txt.split("\n"))
    chunks.append(f"===== PAGE {p + 1} — COUCHE FIX (mots réinversés) =====\n{fixed}")
    chunks.append(f"===== PAGE {p + 1} — COUCHE BRUTE =====\n{txt}")
open(OUT, "w", encoding="utf-8").write("\n\n".join(chunks))
print(f"OK {OUT} — {sum(len(c) for c in chunks)} car, pages {FIRST}-{LAST}")
