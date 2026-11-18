#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inventaire formes apostrophe — usage: python3 w21-inventory.py <book.json> <ids virgules> <sortie.txt>

Collecte chaque ' hors spans RTL avec (mot_avant, mot_après) et un contexte
élargi — sortie triée par occurrences décroissantes → scripts-ia3/tmp/w-forms.txt
"""
import json, re, sys

import importlib.util
spec = importlib.util.spec_from_file_location("ft", "scripts-ia3/fix-typo.py")
ft = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ft)
word_before, word_after = ft.word_before, ft.word_after

import sys as _s
BOOK, IDLIST, OUT = _s.argv[1], _s.argv[2], _s.argv[3]
DOCS = [x.strip().rsplit("-", 1)[-1] for x in IDLIST.split(",")]

book = json.load(open(f"content/books/{BOOK}.json"))
docs = [book["intro"]] + book["lessons"]
pairs = {}
for d in docs:
    did = str(d.get("docId"))
    if did.rsplit("-", 1)[-1] not in DOCS:
        continue
    html = d["htmlFr"]
    segs = ft.tokenize(html)
    rendered, ctxmap = [], []
    for si, (kind, s) in enumerate(segs):
        if kind == "text":
            for off in range(len(s)):
                rendered.append(s[off])
                ctxmap.append(si)
    rendered = "".join(rendered)
    for m in re.finditer("'", rendered):
        p = m.start()
        pb, na = word_before(rendered, p), word_after(rendered, p)
        key = (pb.lower(), na.lower())
        pairs.setdefault(key, [0, pb + "'" + na, rendered[max(0, p - 45):p + 45]])
        pairs[key][0] += 1

rows = sorted(pairs.items(), key=lambda kv: -kv[1][0])
with open(OUT, "w", encoding="utf-8") as f:
    for (pb, na), (n, form, ctx) in rows:
        f.write(f"{n:>4}  {form!r}   ⟨{ctx}⟩\n")
print(f"{len(pairs)} formes uniques, {sum(v[0] for v in pairs.values())} apostrophes")
