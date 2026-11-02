#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Sonde de borne SUPÉRIEURE Kahf leçon 20 (R520, slot 758) :
scan p.150-164 du manuel miroir (tafsir-3-thanawi_text.pdf) pour trancher où
ouvre la leçon 21 (« أهداف الدرس » badge NUM, leçon 21 = v78-81 imprimé =
cache 79-82). NUM : chiffres OCR souvent INVERSÉS par paires (ex. « 94-25 » =
49-52) — jamais deviné, chaque borne relue dans la couche texte brute."""
import re

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"
doc = fitz.open(PDF)
pat = re.compile(r"أهداف الدرس|إعداد قبلي|الآيات|الكهف|78|81|87|18|٧٨|٨١")
for p in range(150, 165):
    page = doc[p - 1]
    raw = page.get_text()
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    hits = [l for l in lines if pat.search(l)]
    print(f"===== p{p} ({len(lines)} lignes, {len(hits)} hits) =====")
    for l in hits[:14]:
        print(f"  > {l[:120]}")
    if not hits:
        for l in lines[:6]:
            print(f"  . {l[:120]}")
