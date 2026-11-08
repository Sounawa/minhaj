# -*- coding: utf-8 -*-
"""Minhāj — Extraction couche texte leçon 9 hadith-3es (R647, slot pdf-mut23h2x-398).
Mécanique hadith3-extract-397.py (R643). Bornes provisoires tranchées par sondage
hadith3-sondage-r647.py : ouverture p.65 (objectifs + texte 1041), clôture p.70
(أسئلة) — p.71 = objectifs leçon 10 (الطواف/الحجر الأسود = registre 399).
Fenêtre élargie 64-72 pour preuves. Sortie : tr-tmp/hadith3-l398-readable.txt —
DEUX couches par page (fix + brute)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith3-l398-readable.txt"
FIRST, LAST = 64, 72

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
