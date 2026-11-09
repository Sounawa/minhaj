# -*- coding: utf-8 -*-
"""Minhāj — EXTRACTION leçon 14 hadith-3es (R670, slot pdf-mut23h2x-403,
أحكام مزدلفة, p.97-103). Deux couches par page au patron hadith3-l401-readable.txt :
COUCHE FIX (mots réinversés via fix_line) et COUCHE BRUTE (ordre natif d'extraction).
Bornes confirmées sondage R670 (hadith3-map-403-r670.py) : ouverture p.97
(objectifs أحكام ليلة العاشر), évaluation p.102-103, préparation préalable p.103 ;
p.104 = objectifs leçon 15 (أعمال أيام منى) → borne supérieure exclusive.
Chiffres OCR inversés par paires — jamais de borne devinée ; toute récusation
tranchée par preuve image (VLM)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 97, 103  # bornes confirmées sondage R670

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
open("/home/z/my-project/tr-tmp/hadith3-l403-readable.txt", "w", encoding="utf-8").write(txt)
print(f"ÉCRIT tr-tmp/hadith3-l403-readable.txt ({len(txt)} car)")
