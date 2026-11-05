#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R587 — crops 1200 dpi (lecture image directe, chaîne R578-R586).
Leçon 10 ulum-hadith-tanawi-1 (pdf-mut23h2q-121, الحديث المعنعن, p.55-58).
  U0  p55 bannière+objectifs (0.02-0.40) — الدرس 10 المعنعن + objectifs L121
  U1  p55 متن bayt + الشرح (0.55-1.00) — vocalisation exacte du bayt + glose
  U2  p56 top questions (0.02-0.26) — section mystère (تذكير ?)
  U3  p56 bayt الناظم + définition (0.36-0.68) — « عرفه الناظم بقوله »
  U4  p56 citation الموطأ (0.58-0.92) — matn ghusl + référence kitāb/bāb
  U5  p57 top شروط (0.02-0.36) — التدليس + ملاقاة (شرط البخاري/مسلم)
  U6  p58 citation ابن عبد البر (0.02-0.45) — 3 شروط + ref التمهيد
  U7  p58 إعداد قبلي (0.55-1.00) — preuve borne → المبهم
  U8  p59 bannière+objectifs (0.02-0.35) — preuve borne → الدرس 11 المبهم L122
Sortie : tr-tmp/r587-uh1/crops/U*.png
Usage : python3 scripts-translate/crops-uh1-r587.py [tags...]
"""
import os
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r587-uh1/crops"

ZONES = [
    ("U0-p55-banniere-objectifs", 55, 0.02, 0.40),
    ("U1-p55-matn-bayt-sharh", 55, 0.55, 1.00),
    ("U2-p56-top-questions", 56, 0.02, 0.26),
    ("U3-p56-bayt-nazim-def", 56, 0.36, 0.68),
    ("U4-p56-muwatta-citation", 56, 0.58, 0.92),
    ("U5-p57-top-shurut", 57, 0.02, 0.36),
    ("U6-p58-ibn-abd-barr", 58, 0.02, 0.45),
    ("U7-p58-idad-qibli", 58, 0.55, 1.00),
    ("U8-p59-banniere-objectifs", 59, 0.02, 0.35),
]


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    tags = set(sys.argv[1:]) or {z[0].split("-")[0] for z in ZONES}
    doc = fitz.open(PDF)
    for tag, page, f0, f1 in ZONES:
        if tag.split("-")[0] not in tags:
            continue
        p = doc[page - 1]
        r = p.rect
        clip = fitz.Rect(r.x0, r.y0 + (r.y1 - r.y0) * f0, r.x1, r.y0 + (r.y1 - r.y0) * f1)
        out = f"{WORK}/{tag}.png"
        p.get_pixmap(dpi=1200, clip=clip).save(out)
        print(f"[ok] {tag}.png ({os.path.getsize(out)//1024} Ko)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
