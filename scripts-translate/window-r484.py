#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R484 — fenêtres Muḥarrar pour le tafsīr 17:110-111 (leçon 736)."""
import re

SRC = "/home/z/my-project/tr-tmp/ibn-atiyya-isra17.md"
OUT = "/home/z/my-project/tr-tmp/muharrar-736-frag.txt"

MOTIFS = ["الآية 17:110", "الآية 17:111", "مفعولين", "التسمية", "البيضاوي", "عياشور",
          "تشهدهم", "أفذاذا", "مجاهد", "آية العز", "طلحة بن مصرف", "ابن سيرين",
          "أولياء الله", "لولن", "عقب ذلك", "أسمع أذنيه"]

txt = open(SRC, encoding="utf-8").read()
out = []
seen = set()
for m in MOTIFS:
    idxs = [x.start() for x in re.finditer(re.escape(m), txt)]
    out.append(f"\n{'='*70}\nMOTIF « {m} » — {len(idxs)} occurrence(s)")
    kept = 0
    for ix in idxs:
        if ix in seen:
            continue
        a, b = max(0, ix-500), min(len(txt), ix+700)
        for s in seen:
            if s-400 <= ix <= s+400:
                break
        else:
            out.append(f"\n--- occ @ {ix} ---\n{txt[a:b]}")
            seen.add(ix)
            kept += 1
        if kept >= 2:
            break
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("écrit:", OUT, len("\n".join(out)), "car")
