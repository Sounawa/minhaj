# -*- coding: utf-8 -*-
"""R334 — Vérification coranique 2ᵉ passe (patterns corrigés, segments bruts)."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = []
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1]))

def show(sura, aya, span=None):
    for (sn, an, tx) in corpus:
        if sn == sura and an == aya:
            if span is None:
                print(f"  {sura}:{aya} PLEIN | {tx}")
            else:
                print(f"  {sura}:{aya} | {tx[span[0]:span[1]]}")

def find(pat, label):
    rx = re.compile(pat)
    hits = []
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            st = max(0, m.start()-20); en = min(len(tx), m.end()+20)
            hits.append((sn, an, m.group(0), tx[st:en]))
    print(f"\n=== {label} — {len(hits)} occ.")
    for (sn, an, g, ctx) in hits:
        print(f"  {sn}:{an} [{g}] | {ctx}")
    return hits

print("■■■ PASSE 2 — 19759 ■■■")

print("\n--- AWTHĀN corrigé (alif suscrite possible) :")
find(r"[اأٱ]وْثَ[ٰ]?ن", "AWTHĀN")

print("\n--- NAFFĀṮĀT corrigé :")
find(r"نَفَّ[ٰ]?ث[^ ]{0,6}", "NAFFĀṮĀT")

print("\n--- ḪABĪṮ corrigé (alef wasla) :")
find(r"[اأٱ]لْخَبِيث[^ ]{0,5}", "ḪABĪṮ")

print("\n--- ṮULŪTH corrigé (shadda) :")
find(r"ثُّ?لُث[^ ]{0,5}", "ṮULŪTH")

print("\n--- AMṮAL large :")
find(r"[اأٱ]?مْثَل[^ ]{0,4}", "AMṮAL large")

print("\n--- ANṮĀ large :")
find(r"[اأٱ]نْ?ث[^ ]{0,6}", "ANṮĀ large")

print("\n--- ĀTHARA + HUM (verbe préférence + formes) :")
find(r"[اأآ]ث[َٰ]?ر[^ ]{0,10}", "ĀTHARA formes")

print("\n--- ITHR / إثْر :")
find(r"إِثْر[^ ]{0,8}", "IṮR")

print("\n■■■ SEGMENTS BRUTS DES ANCRAGES ■■■")
print("\n46:17 (يَسْتَغِيثَانِ + أَتَعِدَانِنِي) :")
show(46, 17)
print("\n4:176 (ٱلثُّلُثَانِ) :")
show(4, 176)
print("\n4:11 (ثُلُثَا + الْأُنْثَيَيْنِ) :")
show(4, 11)
print("\n73:20 (ثُلُثَىِ / ثُلُثَهُ) :")
show(73, 20)
print("\n22:30 (أَوْثَٰنِ) :")
show(22, 30)
print("\n113:4 (النَّفَّاثَاتِ) :")
show(113, 4)
print("\n8:9 (تَسْتَغِيثُونَ) :")
show(8, 9)
print("\n18:29 (يَسْتَغِيثُوا) :")
show(18, 29)
print("\n12:91 (ءَاثَرَكَ) :")
show(12, 91)
print("\n79:38 (ءَاثَرَ) :")
show(79, 38)
print("\n24:26 (الْخَبِيثَات) :")
show(24, 26)
print("\n8:37 (الْخَبِيثَ مِنَ الطَّيِّب) :")
show(8, 37)
