# -*- coding: utf-8 -*-
"""Minhāj — SONDAGE BORNES leçon 13 hadith-3es (R657, slot pdf-mut23h2x-402,
أعمال يوم عرفة). Borne INFÉRIEURE = bannière « الدرس الثالث عشر ».
Borne SUPÉRIEURE = au SONDAGE des أهداف الدرس de la leçon 14 (الدرس الرابع عشر,
المبيت بمزدلفة / أحكام المبيت بمزدلفة).
Mécanique hadith3-sondage-l12-r656.py (R656) : fix_line réinverse les mots ;
chiffres OCR inversés par paires — JAMAIS de borne devinée, toute borne
confirmée par sondage image si ambiguïté.
Source : content/textbooks-src/hadith-3-iadadi_text.pdf (196 p., version _text)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 80, 108

doc = fitz.open(PDF)
print(f"pages: {doc.page_count}")


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
        if "الثالث عشر" in s or "ثالث عشر" in s or ("ثالث" in s and "عشر" in s):
            mark.append("THALITH-ACHIR(13)")
        if "الرابع عشر" in s or "رابع عشر" in s or ("رابع" in s and "عشر" in s):
            mark.append("RABI3-ACHIR(14)")
        if "عرفة" in s and len(s) < 90:
            mark.append("ARAFA")
        if "أهداف" in s:
            mark.append("AHDaf")
        if "الإعداد القبلي" in s or "الإعداد" in s:
            mark.append("I3dadQibli")
        if "السعي" in s and len(s) < 80:
            mark.append("SA3Y")
        if "مزدلفة" in s or "المزدلفة" in s:
            mark.append("MUZDALIFA")
        if mark:
            hits.append((i, "•".join(mark), s[:95]))
    if hits:
        print(f"--- p.{p+1} ({len(raw)} car bruts) ---")
        for i, m, s in hits:
            print(f"  [{i}] {m}: {s}")
