#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R338 — Passe 7 : dernières sondes 19759 (113:4, 8:37 dual, 4:176 cps, صلو, أمثال corrigé)."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE, encoding="utf-8"))
corpus = []
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1]))
IDX = {(sn, an): tx for (sn, an, tx) in corpus}

def show(sn, an, needle, ctx=30):
    tx = IDX.get((sn, an), "")
    i = tx.find(needle)
    if i < 0:
        print(f"  {sn}:{an} — '{needle}' ABSENT"); return
    st = max(0, i - ctx); en = min(len(tx), i + len(needle) + ctx)
    print(f"  {sn}:{an} [{needle}] | …{tx[st:en]}…")
    seg = tx[i:i + len(needle) + 2]
    print("      cps:", " ".join(f"{ord(c):04X}" for c in seg))

print("=== 113:4 النَّفَّاثَات (verset entier) ===")
print("  " + IDX[(113, 4)])
print("      cps n-f-…:", " ".join(f"{ord(c):04X}" for c in IDX[(113, 4)][IDX[(113, 4)].find("نَّف"):IDX[(113, 4)].find("نَّف")+8]))

print("\n=== 8:37 verset entier (chercher le duel خبيثت) ===")
print("  " + IDX[(8, 37)])

print("\n=== 4:176 ثُلُثَانِ cps ===")
show(4, 176, "ثُلُثَانِ", 30)

print("\n=== صَلو (rasm wāw) toutes formes ===")
rx = re.compile(r"ص.{0,3}و[\u0670ٰ]?ة")
hits = 0
for (sn, an, tx) in corpus:
    for m in rx.finditer(tx):
        hits += 1
        if hits <= 8:
            st = max(0, m.start()-10); en = min(len(tx), m.end()+10)
            print(f"  {sn}:{an} [{m.group(0)}] | …{tx[st:en]}…")
print(f"  TOTAL صَلوة/صَلوات rasm wāw: {hits}")

print("\n=== أمثال position (corrigé) ===")
rx = re.compile(r"[أٱ]\u064E?مثَ?[اىٰ]?ال")
for (sn, an, tx) in corpus:
    m = rx.search(tx)
    if m:
        seg = m.group(0)
        print(f"  {sn}:{an} [{seg}] — cps:", " ".join(f"{ord(c):04X}" for c in seg))
