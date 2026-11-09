# -*- coding: utf-8 -*-
"""Minhāj — SONDAGE BORNES leçon 15 hadith-3es (R670, slot pdf-mut23h2x-404,
أعمال أيام منى (1)). Borne INFÉRIEURE = bannière « الدرس الخامس عشر ».
Borne SUPÉRIEURE = bannière « الدرس السادس عشر » (exclusive) + sondage
أهداف الدرس de la leçon 16. Mécanique hadith3-map-403-r670.py : fix_line
réinverse les mots ; chiffres OCR inversés par paires — JAMAIS de borne
devinée : toute borne confirmée par sondage (couche texte + rendu image).
Contexte : leçon 13 ouvre p.90 (R668) ; leçon 14 ≈ p.94-96 (map-403 R670) ;
leçon 15 attendue ≈ p.96-100. Source : hadith-3-iadadi_text.pdf (196 p.)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 88, 118

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
        if "رابع عشر" in s:
            mark.append("RABI3-ACHIR(14)")
        if "خامس عشر" in s or "الخامس عشر" in s:
            mark.append("KHAMIS-ACHIR(15)")
        if "سادس عشر" in s or "السادس عشر" in s:
            mark.append("SADIS-ACHIR(16)")
        if "منى" in s:
            mark.append("MINA")
        if "مزدلفة" in s:
            mark.append("MUZDALIFA")
        if "أهداف" in s:
            mark.append("AHDAF")
        if "استخلاص" in s or "تقويم" in s:
            mark.append("ISTIHLAS/TAQWIM")
        if "الإعداد" in s:
            mark.append("I3DAD")
        if mark:
            hits.append((i, "+".join(mark), s[:160]))
    if hits:
        print(f"\n########## PAGE {p + 1} — {len(raw)} car bruts ##########")
        for i, m, s in hits:
            print(f"  [{i}] ({m}) {s}")
