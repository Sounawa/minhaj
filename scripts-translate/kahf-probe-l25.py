#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Sonde de borne leçon 25 (R52x, slot 763) : scan p.188-210 du
manuel miroir (tafsir-3-thanawi_text.pdf) pour trancher où ouvre la leçon 26
(borne supérieure de la leçon 25, slot pdf-mut23h3c-763, p.188 ouverte R523,
directive R525 « cache depuis 100, décalage +2 » — v98+ imprimé). NUM :
chiffres OCR souvent INVERSÉS par paires — jamais deviné, chaque borne relue
dans la couche texte brute + convergence double (badge + إعداد قبلي + contenu
des āyāt)."""
import re

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"
doc = fitz.open(PDF)
pat = re.compile(r"أهداف الدرس|إعداد قبلي|الآيات|الكهف|استثمار|98|101|102|103|104|105|٩٨|١٠١|١٠٢|١٠٣|١٠٤|١٠٥")
for p in range(188, 211):
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
