# -*- coding: utf-8 -*-
# R648 — décodeur lecture leçon 17 (cf. uh2-decode-270.py) : renversement caractère par caractère.
import re

TXT = "/home/z/my-project/tr-tmp/uh2-l271-raw.txt"
FIRST, LAST = 88, 97

txt = open(TXT, encoding="utf-8").read()
for p in range(FIRST, LAST + 1):
    m = re.search(rf"===== PAGE {p} — BRUTE =====\n(.*?)===== PAGE {p} — FIX", txt, re.S)
    if not m:
        continue
    lines = [l for l in m.group(1).strip().splitlines() if l.strip()]
    print(f"\n########## PAGE {p} — DECODE (renversé) ##########")
    for l in lines:
        d = l[::-1]
        flag = "  [ Court/frag. ]" if len(d.strip()) < 12 else ""
        print(f"| {d}{flag}")
