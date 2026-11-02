#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Sonde de borne leçon 26 (R527, slot 764) : scan p.195-212 du
manuel miroir (tafsir-3-thanawi_text.pdf) pour trancher où s'achève la leçon 26
(borne supérieure = ouverture de التقويم النهائي / annexe, la leçon 26 étant la
dernière leçon du tafsīr, grille VERSE_RANGE[26] « v102-105 »). NUM : chiffres
OCR souvent INVERSÉS par paires — jamais deviné, chaque borne relue dans la
couche texte brute + convergence double (badge + إعداد قبلي + contenu des āyāt).
NB R526 : le décalage imprimé→cache est passé à +4 (médaillon (98) = cache
102) — pour la leçon 26, le mapping (102)-(105) ↔ cache 106-110 à trancher par
le contenu (boîte des āyāt p.195 + gloses p.196-200)."""
import re

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"
doc = fitz.open(PDF)
pat = re.compile(r"أهداف الدرس|إعداد|أرجع|راجع|الآيات|الكهف|استثمار|التقويم|النهائي|أنشطة|المعجم|المصادر|102|103|104|105|106|١٠٢|١٠٣|١٠٤|١٠٥|١٠٦")
for p in range(195, 213):
    page = doc[p - 1]
    raw = page.get_text()
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    hits = [l for l in lines if pat.search(l)]
    print(f"===== p{p} ({len(lines)} lignes, {len(hits)} hits) =====")
    for l in hits[:16]:
        print(f"  > {l[:130]}")
    if not hits:
        for l in lines[:5]:
            print(f"  . {l[:130]}")
