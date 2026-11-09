# -*- coding: utf-8 -*-
"""Minhāj — EXTRACTION leçon 13 hadith-3es (R667, slot pdf-mut23h2x-402,
أعمال يوم عرفة, p.90-96). Deux fichiers au patron R656/R666 :
  - tr-tmp/hadith3-l402-raw.txt     : couche texte BRUTE (ordre natif d'extraction)
  - tr-tmp/hadith3-l402-readable.txt: couche FIX (mots réinversés ligne à ligne) + BRUTE
Chiffres de la couche portés inversés par le miroir (ex. «1721» = 1271,
«7511» = 1157) — jamais devinés, tranchés par OCR micro-crops (script
hadith3-adjud-402-r667.py) + convergence lectures R657 en cache."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 90, 96  # bornes confirmées par sondage image R657 couché + OCR R667
                      # (médaillon «13» p.90, أعمال يوم عرفة ; الإعداد القبلي p.96 ;
                      # médaillon «14» p.97 = leçon 403, NON TOUCHÉE)

doc = fitz.open(PDF)


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


raw_all = []
readable = []
for p in range(FIRST - 1, LAST):
    raw = doc[p].get_text("text")
    fixed = "\n".join(fix_line(l) for l in raw.split("\n"))
    raw_all.append(f"===== PAGE {p+1} =====")
    raw_all.append(raw.strip())
    readable.append(f"===== PAGE {p+1} — COUCHE FIX (mots réinversés) =====")
    readable.append(fixed.strip())
    readable.append(f"===== PAGE {p+1} — COUCHE BRUTE =====")
    readable.append(raw.strip())
    readable.append("")

raw_txt = "\n".join(raw_all)
fix_txt = "\n".join(readable)
open("/home/z/my-project/tr-tmp/hadith3-l402-raw.txt", "w", encoding="utf-8").write(raw_txt)
open("/home/z/my-project/tr-tmp/hadith3-l402-readable.txt", "w", encoding="utf-8").write(fix_txt)
print(f"ÉCRIT tr-tmp/hadith3-l402-raw.txt ({len(raw_txt)} car)")
print(f"ÉCRIT tr-tmp/hadith3-l402-readable.txt ({len(fix_txt)} car)")
