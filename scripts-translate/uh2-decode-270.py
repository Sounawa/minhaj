# -*- coding: utf-8 -*-
# R646 — décodeur lecture : les deux couches PyMuPDF sont en ordre visuel LTR ;
# le sens logique s'obtient en renversant chaque ligne caractère par caractère.
import re

TXT = "/home/z/my-project/tr-tmp/uh2-l270-raw.txt"


def dec(line: str) -> str:
    return line[::-1]


txt = open(TXT, encoding="utf-8").read()
for p in range(83, 88):
    m = re.search(rf"===== PAGE {p} — BRUTE =====\n(.*?)===== PAGE {p} — FIX", txt, re.S)
    if not m:
        continue
    lines = [l for l in m.group(1).strip().splitlines() if l.strip()]
    print(f"\n########## PAGE {p} — DECODE (renversé) ##########")
    for l in lines:
        d = dec(l)
        # marquer les lignes suspects (échange ط/ق documenté R645, jetons isolés)
        flag = "  [ Court/frag. ]" if len(d.strip()) < 12 else ""
        print(f"| {d}{flag}")
