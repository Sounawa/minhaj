#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Sonde de borne SUPÉRIEURE Kahf leçon 19 (R519) : re-sonde p.149-150
du manuel miroir (tafsir-3-thanawi_text.pdf) pour trancher : est-ce que p.150
ouvre la leçon 20 (« أهداف الدرس » / « إعداد قبلي ») et p.149 clos l'exégèse
de la lexie de la retenue (« lā tuʾāḫiḏnī », imprimé 72 = cache 73) ?
NUM : chiffres OCR inversés par paires (ex. « 94-25 » = 49-52) — jamais deviné."""
import re

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"
doc = fitz.open(PDF)
for p in (149, 150):
    page = doc[p - 1]
    raw = page.get_text()
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    print(f"===== p{p} ({len(lines)} lignes) =====")
    for i, l in enumerate(lines):
        print(f"  [{i}] {l[:110]}")
