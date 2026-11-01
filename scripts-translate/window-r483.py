#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R483 — fenêtres du Muḥarrar (ibn-atiyya-isra17.md, mono-ligne) pour trancher
les zones corrompues de la leçon 735 (Isrāʾ 105-108). Lecture Python obligatoire."""
import re

SRC = "/home/z/my-project/tr-tmp/ibn-atiyya-isra17.md"
OUT = "/home/z/my-project/tr-tmp/muharrar-735-frag.txt"

MOTIFS = [
    "لِلْأَذْقَان", "للأذقان", "أذقان",
    "سيبويه",
    "الفراء",
    "ورقة",
    "أوتوا العلم",
    "على مكث", "مكث",
    "فرقناه", "فَرَّقْنَاه", "فرّقناه",
    "ابن مسعود",
    "تساقط",
    "منجم", "مجموع",
    "لِتقرأه", "لتقرأه", "لِتَقْرَأَه",
    "التوراة والإنجيل",
    "الحسن البصري",
    "قتادة",
    "التميمي",
    "لمفعول",
    "سبحان ربنا",
    "آمنوا به أو",
    "بشيرا ونذيرا", "مبشرا",
    "بالحق نزل", "بالحق أنزلناه",
    "يخرون", "الخرور",
    "حواء", "لناحية",
]

txt = open(SRC, encoding="utf-8").read()
print(f"Muḥarrar: {len(txt)} car")
out = []
for m in MOTIFS:
    idxs = [x.start() for x in re.finditer(re.escape(m), txt)]
    out.append(f"\n{'='*70}\nMOTIF « {m} » — {len(idxs)} occurrence(s)")
    for i, ix in enumerate(idxs[:6]):
        a, b = max(0, ix-450), min(len(txt), ix+450)
        out.append(f"\n--- occ {i+1} @ {ix} ---\n{txt[a:b]}")
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("écrit:", OUT, len("\n".join(out)), "car")
