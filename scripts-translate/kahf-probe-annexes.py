#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Sonde annexes (R529, slot 765) : scan p.202-224 du manuel miroir
(tafsir-3-thanawi_text.pdf) pour trancher les bornes des trois annexes :
  - أنشطة الإثراء والتعمق (activités d'enrichissement) — slot 765, ouvre p.202 ;
  - المعجم (glossaire/fihris des termes) — slot 766 ;
  - المصادر والمراجع (sources et références) — slot 767.
NUM : chiffres OCR parfois INVERSÉS par paires — jamais deviné, chaque borne
relue dans la couche texte brute + convergence double."""
import re

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"
doc = fitz.open(PDF)
pat = re.compile(
    r"أنشطة|الإثراء|التعمق|المعجم|المصادر|المراجع|أهداف|إعداد|التقويم|النهائي|"
    r"النشاط|النشاطات|الوحدة|الكهف|الدرس|فهرس|مصادر")
print(f"PDF pages: {doc.page_count}")
for p in range(200, 225):
    page = doc[p - 1]
    raw = page.get_text()
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    hits = [l for l in lines if pat.search(l)]
    print(f"===== p{p} ({len(lines)} lignes, {len(hits)} hits) =====")
    for l in hits[:14]:
        print(f"  > {l[:130]}")
    if not hits:
        for l in lines[:4]:
            print(f"  . {l[:130]}")
