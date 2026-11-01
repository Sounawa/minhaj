#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R483b — fenêtres ciblées : début du tafsīr 17:105 + en-têtes de versets du Muḥarrar."""
import re

SRC = "/home/z/my-project/tr-tmp/ibn-atiyya-isra17.md"
OUT = "/home/z/my-project/tr-tmp/muharrar-735b-frag.txt"

MOTIFS = ["مستأنف", "بالحق أنزلناه", "الزهراوي", "الآية 17:105", "الآية 17:106",
          "الآية 17:107", "الآية 17:108", "الآية 17:109", "الآية 17:110",
          "شهيدًا", "أسمعه من غيري", "ثمان عشرة"]

txt = open(SRC, encoding="utf-8").read()
out = []
for m in MOTIFS:
    idxs = [x.start() for x in re.finditer(re.escape(m), txt)]
    out.append(f"\n{'='*70}\nMOTIF « {m} » — {len(idxs)} occurrence(s)")
    for i, ix in enumerate(idxs[:4]):
        a, b = max(0, ix-700), min(len(txt), ix+700)
        out.append(f"\n--- occ {i+1} @ {ix} ---\n{txt[a:b]}")
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("écrit:", OUT, len("\n".join(out)), "car")
