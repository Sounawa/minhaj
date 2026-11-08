# -*- coding: utf-8 -*-
"""Minhāj — SONDAGE BANNIÈRES leçon 9 hadith-3es (R647) : chercher التاسع / العاشر
et درس sur p.60-74 (toutes lignes, sans filtre). Preuve texte obligée — jamais devinée."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 60, 74

doc = fitz.open(PDF)


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


for p in range(FIRST - 1, min(LAST, doc.page_count)):
    raw = doc[p].get_text("text")
    fixed = "\n".join(fix_line(l) for l in raw.split("\n"))
    hits = []
    for i, l in enumerate(fixed.split("\n")):
        if "تاسع" in l or "التاسع" in l or "عاشر" in l or "العاشر" in l or "أهداف" in l or "الإعداد القبلي" in l or ("الدرس" in l and len(l.strip()) < 60):
            hits.append((i, l.strip()[:140]))
    if hits:
        print(f"\n########## PAGE {p + 1} ##########")
        for i, l in hits:
            print(f"  [{i}] {l}")
