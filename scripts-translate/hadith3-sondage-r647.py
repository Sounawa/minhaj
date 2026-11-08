# -*- coding: utf-8 -*-
"""Minhāj — SONDAGE leçon 9 hadith-3es (R647, slot pdf-mut23h2x-398).
Ouverture l9 = p.65 (bannière الدرس التاسع, vue R643). Borne supérieure À TRANCHER
par sondage p.65-72 : chercher الدرس العاشر / أهداف الدرس. Mécanique hadith3-sondage.py
(R624) : fix_line réinverse les mots ; chiffres OCR inversés par paires — preuve texte."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 64, 73

doc = fitz.open(PDF)


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


for p in range(FIRST - 1, min(LAST, doc.page_count)):
    raw = doc[p].get_text("text")
    fixed = "\n".join(fix_line(l) for l in raw.split("\n"))
    print(f"\n########## PAGE {p + 1} — {len(raw)} car bruts ##########")
    for l in fixed.split("\n"):
        l = l.strip()
        if not l:
            continue
        mark = ""
        if "أهداف" in l:
            mark = "  <<< أهداف"
        if "الإعداد القبلي" in l:
            mark = "  <<< الإعداد القبلي"
        if "الدرس" in l:
            mark += "  <<< DARS"
        if mark or len(l) < 120:
            print(f"  | {l[:150]}{mark}")
