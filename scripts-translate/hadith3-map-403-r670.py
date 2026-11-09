# -*- coding: utf-8 -*-
"""Minhāj — SONDAGE BORNES leçon 14 hadith-3es (R670, slot pdf-mut23h2x-403).
Borne INFÉRIEURE = bannière « الدرس الرابع عشر » (médaillon 14, أحكام مزدلفة).
Borne SUPÉRIEURE = bannière « الدرس الخامس عشر » (أعمال أيام منى (1)) — exclusive.
Attendu : leçon 13 (أعمال يوم عرفة) ouvre p.90 (R668) → leçon 14 ≈ p.94-96.
Mécanique hadith3-map-400.py : fix_line réinverse les mots ; chiffres OCR
inversés par paires — JAMAIS de borne devinée : toute borne confirmée par
sondage (couche texte + rendu image 300 dpi + lecture VLM).
Source : content/textbooks-src/hadith-3-iadadi_text.pdf (196 p., version _text)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 88, 110

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
        if "ثالث عشر" in s:
            mark.append("THALITH-ACHIR(13)")
        if "رابع عشر" in s:
            mark.append("RABI3-ACHIR(14)")
        if "خامس عشر" in s:
            mark.append("KHAMIS-ACHIR(15)")
        if "مزدلفة" in s:
            mark.append("MUZDALIFA")
        if "عرفة" in s:
            mark.append("ARAFAT")
        if "منى" in s:
            mark.append("MINA")
        if "أهداف" in s:
            mark.append("AHDAF")
        if "استخلاص" in s or "تقويم" in s:
            mark.append("ISTIHLAS/TAQWIM")
        if "الإعداد" in s:
            mark.append("I3DAD")
        if mark:
            hits.append((i, s[:160], "+".join(mark)))
    if hits:
        print(f"\n########## PAGE {p + 1} — {len(raw)} car bruts ##########")
        for i, l, m in hits:
            print(f"  [{i}] ({m}) {l}")
