#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R588 — crops 1200 dpi (lecture image directe, chaîne R578-R587).
Leçon 11 ulum-hadith-tanawi-1 (pdf-mut23h2q-122, الحديث المبهم, p.59-62).
  V0  p59 bannière+objectifs (0.02-0.42) — الدرس 11 المبهم + objectifs L122
  V1  p59 fin تمهيد + bayt (0.40-1.00) — ligne garblée « جز لمتن ا هاا »
  V2  p60 أولا + bayt الناظم (0.02-0.32) — « مُبْهَمٌ مَا فِيهِ رَاوٍ لَمْ يُسَمَّ »
  V3  p60 définition + صيغ (0.30-0.64) — listes حدثني رجل … حدثني ناسٌ
  V4  p60 fin liste + ثانيا (0.62-1.00) — أنواع الإبهام وفائدة معرفة المبهم
  V5  p61 الإبهام في الإسناد (0.02-0.44) — مثال الموطأ زيد بن ثابت + شرحبيل
  V6  p61 المبهم في المتن (0.42-0.72) — فوائد + مثال البخاري فرصة من مسك
  V7  p61 مسلم أمة بنت شكل (0.70-1.00) — العراقي/النووي/الخطيب/ابن بشكوال
  V8  p62 top+التقويم+استثمار (0.02-0.42) — ligne décorative + 3 questions
  V9  p62 hadith fin+مالك (0.40-1.00) — رواية مالك + questions ×2
  V10 p63 إعداد قبلي (0.02-0.50) — preuve borne → العالي والنازل
  V11 p64 bannière الدرس 12 (0.02-0.32) — preuve borne L123 العالي والنازل
Sortie : tr-tmp/r588-uh1/crops/V*.png
Usage : python3 scripts-translate/crops-uh1-r588.py [tags...]
"""
import os
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r588-uh1/crops"

ZONES = [
    ("V0-p59-banniere-objectifs", 59, 0.02, 0.42),
    ("V1-p59-fin-tamhid-bayt", 59, 0.40, 1.00),
    ("V2-p60-awwal-bayt-nazim", 60, 0.02, 0.32),
    ("V3-p60-def-sighagh", 60, 0.30, 0.64),
    ("V4-p60-fin-liste-thaniya", 60, 0.62, 1.00),
    ("V5-p61-ibham-sanad-muwatta", 61, 0.02, 0.44),
    ("V6-p61-mubham-matn-bukhari", 61, 0.42, 0.72),
    ("V7-p61-muslim-ummah-bint", 61, 0.70, 1.00),
    ("V8-p62-taqwim-istithmar", 62, 0.02, 0.42),
    ("V9-p62-hadith-fin-malik", 62, 0.40, 1.00),
    ("V10-p63-idad-qibli", 63, 0.02, 0.50),
    ("V11-p64-banniere-d12", 64, 0.02, 0.32),
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
