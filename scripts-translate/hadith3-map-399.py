# -*- coding: utf-8 -*-
"""Minhāj — SONDAGE BORNES leçon 10 hadith-3es (R649, slot pdf-mut23h2x-399).
Borne INFÉRIEURE = bannière « الدرس العاشر » (leçon 9 commence p.65 vue R643).
Borne SUPÉRIEURE = bannière « الدرس الحادي عشر » (leçon 11 أحكام الطواف (2)).
Mécanique hadith3-sondage-r647.py : fix_line réinverse les mots ; chiffres OCR
inversés par paires — JAMAIS de borne devinée : toute borne confirmée par sondage.
Aussi : repérage des أهداف الدرس / الإعداد القبلي pour cadrer la leçon.
Source : content/textbooks-src/hadith-3-iadadi_text.pdf (196 p., version _text)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 64, 90

doc = fitz.open(PDF)


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


for p in range(FIRST - 1, min(LAST, doc.page_count)):
    raw = doc[p].get_text("text")
    fixed = "\n".join(fix_line(l) for l in raw.split("\n"))
    hits = []
    for i, l in enumerate(fixed.split("\n")):
        s = l.strip()
        if not s:
            continue
        mark = []
        if "عاشر" in s or "العاشر" in s:
            mark.append("ACHIR(10)")
        if "حادي عشر" in s or "الحادي عشر" in s or "حادي" in s:
            mark.append("HADI-ACHIR(11)")
        if "تاسع" in s or "التاسع" in s:
            mark.append("TASI(9)")
        if "أهداف" in s:
            mark.append("AHDaf")
        if "الإعداد القبلي" in s or "الإعداد" in s:
            mark.append("I3dadQibli")
        if "أحكام الطواف" in s or "الطواف" in s and len(s) < 70:
            mark.append("TAWAF")
        if mark:
            hits.append((i, s[:140], "+".join(mark)))
    if hits:
        print(f"\n########## PAGE {p + 1} — {len(raw)} car bruts ##########")
        for i, l, m in hits:
            print(f"  [{i}] ({m}) {l}")
