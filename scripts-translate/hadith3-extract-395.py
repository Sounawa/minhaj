# -*- coding: utf-8 -*-
"""Minhāj — Extraction couche texte leçon 6 hadith-3es (slot pdf-mut23h2x-395).
Mécanique hadith3-extract-393.py (R624) — leçon 6 « المواقيت الزمانية والمكانية
للإحرام بالحج », bannière p.45 (lue R636), clôture l5 = p.44 (iʿdād), ouverture
l7 = p.51 (objectifs المواقيت المكانية). Bornes larges 44-51 pour contexte.
Sortie : tr-tmp/hadith3-l395-raw.txt — DEUX couches par page (brute + fix_line)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith3-l395-raw.txt"
FIRST, LAST = 44, 51

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
