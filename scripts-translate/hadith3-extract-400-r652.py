# -*- coding: utf-8 -*-
"""Minhāj — Extraction couche texte leçon 11 hadith-3es (R652, slot pdf-mut23h2x-400).
Mécanique hadith3-extract-399.py (R650). Bornes à trancher par sondage image :
ouverture p.78 attendue (bannière الدرس الحادي عشر, médaillon 11,
أحكام الطواف (2), أهداف الدرس) ; clôture = page avant la bannière du cours 12.
Fenêtre élargie 77-86 pour preuves de jonction. Sortie :
tr-tmp/hadith3-l400-raw.txt puis -readable.txt — DEUX couches par page."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith3-l400-raw.txt"
FIRST, LAST = 77, 86

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
