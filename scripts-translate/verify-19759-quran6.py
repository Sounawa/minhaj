#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R338 — Passe 6 : sondes de POSITION EXACTE pour 19759 (fasil al-thāʾ).
Complète les passes 1-5 (instances parallèles) : ميثاق/أوثان/أثرة/نفاثات étaient
manquées par des patterns fautifs. Règle R337 : UNE SONDE DE POSITION EXACTE
> un comptage global."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE, encoding="utf-8"))
corpus = []
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1]))
IDX = {(sn, an): tx for (sn, an, tx) in corpus}

def show(sn, an, needle, ctx=34):
    tx = IDX.get((sn, aya := an), "")
    i = tx.find(needle)
    if i < 0:
        print(f"  {sn}:{an} — '{needle}' ABSENT"); return
    st = max(0, i - ctx); en = min(len(tx), i + len(needle) + ctx)
    print(f"  {sn}:{an} [{needle}] | …{tx[st:en]}…")
    seg = tx[i:i + len(needle) + 2]
    print("      cps:", " ".join(f"{ord(c):04X}" for c in seg))

def sweep(label, pattern):
    print(f"\n=== {label} ===")
    rx = re.compile(pattern)
    hits = []
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            st = max(0, m.start() - 16); en = min(len(tx), m.end() + 16)
            hits.append((sn, an, m.group(0), tx[st:en]))
    print(f"  {len(hits)} occ.")
    for (sn, an, g, c) in hits:
        print(f"  {sn}:{an} [{g}] | …{c}…")
    return hits

# 1. مِيثَاق — toutes formes (le probe 1 avait échoué : hamza forms)
sweep("مِيثَاق toutes formes", r"[مى]يثَ[اقت]")
sweep("ميث suite", r"يث")
# 2. أوثَان / وَثَن — toutes formes
sweep("وثَن racine w-ṯ-n (ثا)", r"وثَ[اىىٰ]")
sweep("وثَن racine w-ṯ-n", r"وثَ")
# 3. أَثَرَة — hamza initiale variantes
sweep("أَثَرَة toutes formes", r"[ءأٱ]ثَرَة")
# 4. نَفَّاثَات — le IIe affaibli
sweep("نَفَّاثَات", r"نف[َِّ]ثَات")
# 5. خَبِيثَت 8:37 — exact (position de l'alif après ث)
print("\n=== 8:37 الْخَبِيثَتِ exact ===")
show(8, 37, "خَبِيثَتِ")
# 6. 46:17 يَسْتَغِيثَانِ exact
print("\n=== 46:17 يَسْتَغِيثَانِ exact ===")
show(46, 17, "يَسْتَغِيثَانِ")
# 7. ثُلُث 4:11 / 4:12 / 4:176 / 73:20 — les quatre dessins
print("\n=== ثُلُث les quatre dessins ===")
show(4, 11, "ثُلُثَا", 26)
show(4, 11, "ٱلثُّلُثُ", 26)
show(4, 12, "ٱلثُّلُثِ", 26)
show(4, 176, "ٱلثُّلُثَانِ", 26)
show(73, 20, "ثُلُثَىِ", 26)
show(73, 20, "وَثُلُثَهُۥ", 26)
# 8. أَثَٰثًا 16:80 / 19:74 — position du dagger
print("\n=== أَثَٰثًا position exacte du dagger ===")
for (sn, an) in [(16, 80), (19, 74)]:
    tx = IDX[(sn, an)]
    i = tx.find("ثَٰث")
    if i >= 0:
        print(f"  {sn}:{an} [{tx[max(0,i-10):i+8]}]")
        print("      cps:", " ".join(f"{ord(c):04X}" for c in tx[i:i+8]))
# 9. إِنَٰثًا 17:40 / 43:19 — position du dagger (après nūn ?)
print("\n=== إِنَٰثًا position exacte du dagger ===")
for (sn, an) in [(17, 40), (43, 19)]:
    tx = IDX[(sn, an)]
    i = tx.find("نَٰث")
    if i >= 0:
        print(f"  {sn}:{an} [{tx[max(0,i-8):i+8]}]")
        print("      cps:", " ".join(f"{ord(c):04X}" for c in tx[i:i+8]))
# 10. أَثَٰبَ 3:153 / 5:85 / 48:18 — le verbe, dagger après ث
print("\n=== أَثَٰبَ les trois positions ===")
for (sn, an) in [(3, 153), (5, 85), (48, 18)]:
    tx = IDX[(sn, an)]
    i = tx.find("ثَٰب")
    if i >= 0:
        print(f"  {sn}:{an} [{tx[max(0,i-14):i+10]}]")
        print("      cps:", " ".join(f"{ord(c):04X}" for c in tx[i:i+8]))
# 11. أمثال — sonde de position : alif APRÈS ث (pas l'alif-hamza initiale)
print("\n=== أمثال position exacte (ث+ا) ===")
rx = re.compile(r"[أٱ]مثال")
for (sn, an, tx) in corpus:
    m = rx.search(tx)
    if m:
        seg = m.group(0)
        print(f"  {sn}:{an} [{seg}] — alif après ث ? {'ا' in seg[3:]}")
# 12. ذِكْرَى 38:46 + نَرَى 2:55 — les deux exemples de la Durra
print("\n=== نَرَى 2:55 / ذِكْرَى 38:46 — exemples de la Durra ===")
show(2, 55, "نَرَى", 22)
show(38, 46, "ذِكْرَى", 22)
# 13. صَلَوَة (iʿdād — الصَّلوة رasm wāw) — occurrence
print("\n=== الصَّلوة (iʿdād du chapitre) ===")
sweep("الصَّلوة rasm wāw", r"صَ?لَ?و[\u0670ٰ]?ة")
