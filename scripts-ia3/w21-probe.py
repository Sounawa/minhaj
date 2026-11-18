#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""W21 — sonde : quelles formes sont résolues par la carte intégrée de
fix-typo.py, lesquelles exigent un arbitrage nouveau (→ W21 forms)."""
import importlib.util, re, collections

spec = importlib.util.spec_from_file_location("ft", "scripts-ia3/fix-typo.py")
ft = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ft)

rows = []
for line in open("scripts-ia3/tmp/w21-forms.txt", encoding="utf-8"):
    line = line.rstrip("\n")
    if not line.strip():
        continue
    try:
        head, rest = line.strip().split("  ", 1)
        form_repr, ctx = rest.split("   ⟨", 1)
        n = int(head.strip())
        form = eval(form_repr)
        ctx = ctx.rstrip("⟩")
    except Exception as e:
        print("SKIP:", repr(line[:60]), e)
        continue
    rows.append((n, form, ctx))

resolved, pending = [], collections.defaultdict(list)
for n, form, ctx in rows:
    ch, why = ft.classify(form, form.index("'"))
    if ch is None:
        pending[why].append((n, form, ctx))
    else:
        resolved.append((n, ch, form, why))

print(f"résolues par la carte intégrée : {sum(n for n, *_ in resolved)} / {sum(n for n,*_ in rows)}")
print(f"formes en attente d'arbitrage  : {len(pending)} raisons, {sum(n for v in pending.values() for n,*_ in v)} apostrophes")
with open("scripts-ia3/tmp/w21-pending.txt", "w", encoding="utf-8") as f:
    for why, items in sorted(pending.items(), key=lambda kv: -sum(n for n, *_ in kv[1])):
        f.write(f"### {why}  ({sum(n for n,*_ in items)} occ.)\n")
        for n, form, ctx in sorted(items, key=lambda x: -x[0]):
            f.write(f"{n:>4}  {form!r}   ⟨{ctx}⟩\n")
        f.write("\n")
for why, items in sorted(pending.items(), key=lambda kv: -sum(n for n, *_ in kv[1]))[:6]:
    print(f"  {sum(n for n,*_ in items):>5} occ | {why[:60]}")
