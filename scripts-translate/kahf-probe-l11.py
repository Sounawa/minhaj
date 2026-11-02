#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Sonde de bornes Kahf : cherche les en-têtes « أهداف الدرس » et les
NUM de versets dans les pages du manuel miroir (tafsir-3-thanawi_text.pdf),
pour trancher la borne supérieure de la leçon 11 (v32-35) — jamais devinée."""
import re

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"
doc = fitz.open(PDF)
print("pages doc:", doc.page_count)
for p in range(80, 101):
    page = doc[p - 1]
    if p > doc.page_count:
        break
    raw = page.get_text()
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    hits = []
    for l in lines:
        if ("أهداف" in l or "اهداف" in l or ("الدرس" in l and len(l) < 40)
                or "الكهف" in l):
            hits.append(l[:80])
    nums = [l[:60] for l in lines if re.search(r"\d{1,3}\s*-\s*\d{1,3}", l)]
    if hits or nums:
        print(f"--- p{p} ---")
        for h in hits:
            print("  H:", h)
        for n in nums[:3]:
            print("  N:", n)
