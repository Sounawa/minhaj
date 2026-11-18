#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sondage kahf — recherche des en-têtes de leçons dans le manuel miroir
(tafsir-3-thanawi_text.pdf) pour trancher la borne supérieure de la leçon 4
(p.29+) avant armement de la leçon 742. Même mécanique R458/R487 :
décode mot à mot (fix_line de kahf-map) puis cherche les marqueurs
« أهداف الدرس » et « الآيات » avec plages numériques."""
import importlib.util
import re

import fitz

_spec = importlib.util.spec_from_file_location(
    "kahf_map", "/home/z/my-project/scripts-translate/kahf-map.py")
km = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(km)

doc = fitz.open(km.PDF)
for p in range(29, 45):
    raw = doc[p - 1].get_text()
    fixed = "\n".join(km.fix_line(l) for l in raw.split("\n"))
    hits = []
    for ln in fixed.split("\n"):
        if ("أهداف" in ln or "الدرس" in ln or "الآيات" in ln) and len(ln.strip()) > 3:
            hits.append(ln.strip()[:110])
    # plages numériques visibles (les chiffres survivent à l'OCR)
    nums = re.findall(r"\d{1,3}[-–]\d{1,3}", fixed)
    print(f"--- p.{p} ---")
    if hits:
        for h in hits[:6]:
            print("  HDR:", h)
    if nums:
        print("  NUM:", sorted(set(nums))[:12])
