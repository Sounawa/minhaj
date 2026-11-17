#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IA-3 — sondage de précédents translittération dans tout le corpus."""
import json, glob, collections

A1, A2 = "\u02bf", "\u02be"   # ʿ ʾ
def bh(fn):
    b = json.load(open(fn))
    return "".join((d.get("htmlFr") or "") for d in ([b["intro"]] if b.get("intro") else []) + b.get("lessons", []) if isinstance(d, dict))

pats = ["Jāmi"+A1, "Jāmi"+A2, "Jāmi\u2019", "Jāmi'", "Gami"+A1,
        "rābi"+A1, "rābi"+A2, "juz"+A2, "juz"+A1,
        A1+"Umar", "\u2019Umar", A2+"Umar",
        "sharī"+A1, "charī"+A1, "charī\u2019", "shari"+A1,
        "qawā"+A2, "qawā'id", "raja"+A1, "raja"+A2,
        "wa"+A1+"ada", "wa"+A2+"ada", "malī"+A2, "malī"+A1, "mali"+A2,
        "ʿan", A2+"an ", A1+"ayn", A2+"ayn", "ustu"+A1, "ustu"+A2,
        "rābi'", "juz'", "Jāmi' al-Ummahāt"]
c = collections.Counter()
for fn in glob.glob("content/books/*.json"):
    h = bh(fn)
    for p in pats:
        n = h.count(p)
        if n:
            c[p] += n
for k, v in c.most_common():
    print(f"{v:>4}  {k!r}")
