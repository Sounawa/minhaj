# -*- coding: utf-8 -*-
"""Minhāj — Extraction couche texte leçon 7 hadith-3es (slot pdf-mut23h2x-396).
Mécanique hadith3-extract-395.py (R639) — leçon 7 « le muḥrim : نكاح المحرم,
الصيد, المضطر », ouverture l7 = p.52 (bannière + objectifs, R639-bis passation),
clôture l7 = p.57 (istiṯmār المضطر). Bornes 52-57 (passation R639-bis).
Sortie : tr-tmp/hadith3-l396-raw.txt — DEUX couches par page (fix + brute)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith3-l396-raw.txt"
FIRST, LAST = 52, 57

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
