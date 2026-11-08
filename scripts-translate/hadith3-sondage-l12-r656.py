# -*- coding: utf-8 -*-
"""Minhāj — SONDAGE BORNES leçon 12 hadith-3es (R656, slot pdf-mut23h2x-401,
أحكام السعي بين الصفا والمروة). Borne INFÉRIEURE = bannière « الدرس الثاني عشر ».
Borne SUPÉRIEURE = au SONDAGE des أهداف الدرس de la leçon 13 (الدرس الثالث عشر).
Mécanique hadith3-map-399.py / hadith3-sondage-r647.py : fix_line réinverse les
mots ; chiffres OCR inversés par paires — JAMAIS de borne devinée, toute borne
confirmée par sondage image si ambiguïté.
Source : content/textbooks-src/hadith-3-iadadi_text.pdf (196 p., version _text)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 76, 100

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
        if "الثاني عشر" in s or "ثاني عشر" in s or ("ثاني" in s and "عشر" in s):
            mark.append("THANI-ACHIR(12)")
        if "الثالث عشر" in s or "ثالث عشر" in s or ("ثالث" in s and "عشر" in s):
            mark.append("THALITH-ACHIR(13)")
        if "السعي" in s and len(s) < 90:
            mark.append("SA3Y")
        if "أهداف" in s:
            mark.append("AHDaf")
        if "الإعداد القبلي" in s or "الإعداد" in s:
            mark.append("I3dadQibli")
        if "الطواف" in s and len(s) < 80:
            mark.append("TAWAF")
        if "عرفة" in s and len(s) < 80:
            mark.append("ARAFA")
        if mark:
            hits.append((i, "•".join(mark), s[:95]))
    if hits:
        print(f"--- p.{p+1} (index {p}) ---")
        for i, m, s in hits:
            print(f"  [{i}] {m}: {s}")
