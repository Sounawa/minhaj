#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Sonde de bornes Kahf leçons 21/22 (R522, slot 760) : scan p.158-180
du manuel miroir (tafsir-3-thanawi_text.pdf) pour trancher où ouvrent la leçon
22 (imprimé 82-84 = cache 83-85) et la leçon 23 (imprimé 85-91 = cache 86-92) :
« أهداف الدرس » aux ouvertures, إعداد قبلي (« أرجع تفسير ») aux clôtures.
NUM : chiffres OCR souvent INVERSÉS par paires (ex. « 94-25 » = 49-52) — jamais
deviné, chaque borne relue dans la couche texte brute puis sur image si doute."""
import re

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"
doc = fitz.open(PDF)
pat = re.compile(r"أهداف الدرس|إعداد|أرجع تفسير|الآيات|الكهف")
for p in range(158, 181):
    page = doc[p - 1]
    raw = page.get_text()
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    hits = [l for l in lines if pat.search(l)]
    print(f"===== p{p} ({len(lines)} lignes, {len(hits)} hits) =====")
    for l in hits[:10]:
        print(f"  > {l[:120]}")
    if not hits:
        for l in lines[:4]:
            print(f"  . {l[:110]}")
