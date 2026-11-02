#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Sonde de borne leçon 24 (R52x, slot 762) : scan p.171-200 du
manuel miroir (tafsir-3-thanawi_text.pdf) pour trancher 1) où ouvre la leçon
24 (« أهداف الدرس » badge NUM, grille leçon 24 = v92-97 imprimé = cache 93-98,
épisode al-sadd/Yaʾǧūǧ-Maʾǧūǧ) et 2) où ouvre la leçon 25 (v98-101 imprimé =
cache 99-102, borne supérieure de la leçon 24). NUM : chiffres OCR souvent
INVERSÉS par paires (ex. « 94-25 » = 49-52) — jamais deviné, chaque borne
relue dans la couche texte brute + convergence double (badge + إعداد قبلي +
contenu des āyāt)."""
import re

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"
doc = fitz.open(PDF)
pat = re.compile(r"أهداف الدرس|إعداد قبلي|الآيات|الكهف|استثمار|92|97|98|101|٩٢|٩٧|٩٨|١٠١")
for p in range(171, 201):
    page = doc[p - 1]
    raw = page.get_text()
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    hits = [l for l in lines if pat.search(l)]
    print(f"===== p{p} ({len(lines)} lignes, {len(hits)} hits) =====")
    for l in hits[:14]:
        print(f"  > {l[:130]}")
    if not hits:
        for l in lines[:5]:
            print(f"  . {l[:130]}")
