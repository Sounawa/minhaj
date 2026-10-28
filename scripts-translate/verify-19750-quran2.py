#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Suivi des vérifications 19750 : متع, Kahf exact, 16:120, مستنس, ئب forms, طائف."""
import json
import re

C = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json"))
HARAKAT = re.compile(r"[\u064B-\u0652\u0653-\u0655\u0670\u06D6-\u06ED\u08F0-\u08F3]")

def strip(s):
    return HARAKAT.sub("", s).replace("\u0640", "")

def raw_hits(pat_harakat, pat_plain=None, limit=25):
    out = []
    for s, obj in C.items():
        for n, t in obj["ar"]:
            if pat_harakat in t:
                out.append((s, n, t))
    return out

print("=" * 70)
print("A. LEXÈME مَتَاع / مَتَّع — toutes formes (recherche HARAKATÉE)")
hits = raw_hits("مت")
for s, n, t in hits:
    st = strip(t)
    if re.search(r"مت", st):
        idx = st.find("مت")
        # ne garder que متع / متتن
        if re.search(r"مت", st) and ("متع" in st or "متن" in st):
            print(f"   [{s}:{n}] {t[:130]}")
print("   --- via stripped : مَتَاع (متاع) déjà = 0 ; chercher متع nu ---")
cnt = 0
for s, obj in C.items():
    for n, t in obj["ar"]:
        st = strip(t)
        for m in re.finditer("متع", st):
            print(f"   [stripped متع] [{s}:{n}] {st[max(0,m.start()-18):m.start()+20]}")
            cnt += 1
            break
print(f"   total stripped متع : {cnt}")

print("=" * 70)
print("B. KAHF — TOUTES les occurrences كِتَ+ (harakaté) sūra 18")
for s, obj in C.items():
    if s != "18":
        continue
    for n, t in obj["ar"]:
        if "كِتَ" in t or "كتب" in strip(t):
            print(f"   [18:{n}] {t[:110]}")

print("=" * 70)
print("C. 16:120 قَانِتًا — forme exacte")
obj = C["16"]
for n, t in obj["ar"]:
    if n == 120:
        print(f"   [16:120] {t}")

print("=" * 70)
print("D. مُسْتَنِس / أَسْتَأْنَس — recherche large")
for pat in ["مستنس", "أستأنس", "استأنس", "يستنس", "يستأنس"]:
    cnt = 0
    for s, obj in C.items():
        for n, t in obj["ar"]:
            if pat in strip(t):
                print(f"   [{pat}] [{s}:{n}] {strip(t)[:80]}")
                cnt += 1
    print(f"   → {pat} : {cnt}")

print("=" * 70)
print("E. Forms ء-ب (ئب) et ت-ب-و-ن : تَائِب lexical")
for pat in ["ئبت", "ئبون", "تبون", "ئبن"]:
    cnt = 0
    for s, obj in C.items():
        for n, t in obj["ar"]:
            if pat in strip(t):
                idx = strip(t).find(pat)
                print(f"   [{pat}] [{s}:{n}] {strip(t)[max(0,idx-20):idx+25]}")
                cnt += 1
    print(f"   → {pat} : {cnt}")

print("=" * 70)
print("F. طَائِف — lexème")
for pat in ["طائف", "طئف"]:
    cnt = 0
    for s, obj in C.items():
        for n, t in obj["ar"]:
            if pat in strip(t):
                idx = strip(t).find(pat)
                print(f"   [{pat}] [{s}:{n}] {strip(t)[max(0,idx-20):idx+28]}")
                cnt += 1
    print(f"   → {pat} : {cnt}")

print("=" * 70)
print("G. 34:15 جَنَّتَانِ — contexte (Saba)")
obj = C["34"]
for n, t in obj["ar"]:
    if n == 15:
        print(f"   [34:15] {t[:120]}")

print("=" * 70)
print("H. Élue التَّالِيَٰت 37:3 — forme exacte")
obj = C["37"]
for n, t in obj["ar"]:
    if n == 3:
        print(f"   [37:3] {t}")

print("=" * 70)
print("I. خَتَم/خِتَام — l'išāra : la lecture خَاتَمُهُ (fatha) n'est PAS au corpus ;")
print("   le rasm 83:26 = خِتَٰمُهُ (suscrite). Verbes ختم ci-dessus (2:7, 6:46, 36:65, 42:24, 45:23).")

print("=" * 70)
print("J. Recompte GLOBAL كِتَ+ par sourate (suscrite vs pleine) — sommet")
sus_by, full_by = {}, {}
for s, obj in C.items():
    for n, t in obj["ar"]:
        for m in re.finditer(r"كِتَ", t):
            j = m.end()
            ch = t[j] if j < len(t) else ""
            tail = t[j+1] if j+1 < len(t) else ""
            if ch == "\u0670" and tail == "ب":
                sus_by[s] = sus_by.get(s, 0) + 1
            elif ch in "\u0627\u0671" and tail == "ب":
                full_by[s] = full_by.get(s, 0) + 1
print(f"   total suscrite {sum(sus_by.values())} | pleine {sum(full_by.values())} : {full_by}")

print("=" * 70)
print("K. المُتَتَابِعين (4:92/58:4) — le seul « tābiʿīn » du corpus")
for s, n in (("4", 92), ("58", 4)):
    obj = C[s]
    for nn, t in obj["ar"]:
        if nn == n:
            idx = strip(t).find("تابعين")
            print(f"   [{s}:{n}] …{strip(t)[max(0,idx-30):idx+15]}…")
