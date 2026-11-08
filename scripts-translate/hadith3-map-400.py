# -*- coding: utf-8 -*-
"""Minhāj — SONDAGE BORNES leçon 11 hadith-3es (R654, slot pdf-mut23h2x-400).
Borne INFÉRIEURE = bannière « الدرس الحادي عشر » (médaillon 11, أحكام الطواف (2))
— p.78 attendue (399 clôt p.77, cf. hadith3-map-399.py R649).
Borne SUPÉRIEURE = bannière « الدرس الثاني عشر » + أهداف الدرس de la leçon 12
(أحكام السعي بين الصفا والمروة) — fenêtre 77-86 pour preuves de jonction.
Mécanique hadith3-sondage-r647.py : fix_line réinverse les mots ; chiffres OCR
inversés par paires — JAMAIS de borne devinée : toute borne confirmée par sondage
(couche texte + rendu image 300 dpi + lecture VLM).
Source : content/textbooks-src/hadith-3-iadadi_text.pdf (196 p., version _text)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 77, 88

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
        if "حادي عشر" in s or "الحادي عشر" in s:
            mark.append("HADI-ACHIR(11)")
        if "ثاني عشر" in s or "الثاني عشر" in s:
            mark.append("THANI-ACHIR(12)")
        if "أهداف" in s:
            mark.append("AHDaf")
        if "الإعداد القبلي" in s or "الإعداد" in s:
            mark.append("I3dadQibli")
        if "السعي" in s and ("الصفا" in s or "المروة" in s or "أحكام" in s):
            mark.append("SA3Y(lec12)")
        if "أحكام الطواف" in s:
            mark.append("TAWAF")
        if "استخلاص" in s or "التقويم" in s or "تقويم" in s:
            mark.append("ISTIHLAS/TAQWIM")
        if mark:
            hits.append((i, s[:150], "+".join(mark)))
    if hits:
        print(f"\n########## PAGE {p + 1} — {len(raw)} car bruts ##########")
        for i, l, m in hits:
            print(f"  [{i}] ({m}) {l}")
