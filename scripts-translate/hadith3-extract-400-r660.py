# -*- coding: utf-8 -*-
"""Minhāj — Extraction leçon 11 hadith-3es (R660, slot pdf-mut23h2x-400,
أحكام الطواف (2), p.78-83). Patron hadith3-extract-401-r656.py (R656) : deux
couches par page (FIX mots réinversés + BRUTE), fenêtre 77-86 pour sondage de
jonction (p.77 = clôture leçon 10 ; p.84 = ouverture leçon 12 à re-confirmer
image). Chiffres OCR inversés par paires — jamais de borne devinée."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 77, 86

doc = fitz.open(PDF)


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


out = []
for p in range(FIRST - 1, LAST):
    raw = doc[p].get_text("text")
    fixed = "\n".join(fix_line(l) for l in raw.split("\n"))
    out.append(f"===== PAGE {p+1} — COUCHE FIX (mots réinversés) =====")
    out.append(fixed.strip())
    out.append(f"===== PAGE {p+1} — COUCHE BRUTE =====")
    out.append(raw.strip())
    out.append("")
txt = "\n".join(out)
open("/home/z/my-project/tr-tmp/hadith3-l400-readable.txt", "w", encoding="utf-8").write(txt)
print(f"ÉCRIT tr-tmp/hadith3-l400-readable.txt ({len(txt)} car)")
