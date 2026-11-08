# -*- coding: utf-8 -*-
"""Minhāj — EXTRACTION leçon 12 hadith-3es (R656, slot pdf-mut23h2x-401,
أحكام السعي بين الصفا والمروة, p.84-89). Deux couches par page au patron
hadith3-l399-readable.txt : COUCHE FIX (mots réinversés via fix_line) et
COUCHE BRUTE (ordre natif d'extraction). Chiffres OCR inversés par paires —
jamais de borne devinée ; toute récusation tranchée par preuve image (VLM)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 84, 89  # bornes confirmées image R656 (médaillon « 12 » p.84 ; الإعداد القبلي p.89)

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
open("/home/z/my-project/tr-tmp/hadith3-l401-readable.txt", "w", encoding="utf-8").write(txt)
print(f"ÉCRIT tr-tmp/hadith3-l401-readable.txt ({len(txt)} car)")
