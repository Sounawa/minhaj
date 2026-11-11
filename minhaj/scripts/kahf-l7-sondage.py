#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sondage kahf leçon 7 (R500) — recherche de l'ouverture de la leçon 8 dans le
manuel miroir (tafsir-3-thanawi_text.pdf) pour trancher la borne supérieure de
la leçon 7 (p.50+) avant extraction. Même mécanique R458/R487/R492/R497 :
décode mot à mot (fix_line de kahf-map) puis cherche « أهداف الدرس » ; les
plages NUM survivent à l'OCR en chiffres inversés par paires (ex. p.51
« 12-42 » = 21-24)."""
import importlib.util

import fitz

_spec = importlib.util.spec_from_file_location(
    "kahf_map", "/home/z/my-project/scripts-translate/kahf-map.py")
km = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(km)

doc = fitz.open(km.PDF)
for p in range(50, 76):
    raw = doc[p - 1].get_text()
    fixed = "\n".join(km.fix_line(l) for l in raw.split("\n"))
    hdr = [ln.strip()[:110] for ln in fixed.split("\n")
           if ("أهداف" in ln or "الدرس" in ln) and len(ln.strip()) > 3]
    nums = sorted(set(__import__("re").findall(r"\d{1,3}[-–]\d{1,3}", fixed)))
    tete = " | ".join(fixed.strip().split("\n")[0:1])[:90]
    print(f"--- p.{p} --- {tete}")
    if hdr:
        for h in hdr[:4]:
            print("  HDR:", h)
    if nums:
        print("  NUM:", nums[:10])
