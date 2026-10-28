#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compléments 19750 : recherches par squelettes consonantiques (suscrites incluses)."""
import json
import re

C = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json"))
HARAKAT = re.compile(r"[\u064B-\u0652\u0653-\u0655\u06D6-\u06ED\u08F0-\u08F3]")

def light(s: str) -> str:
    """Strip harakat mais GARDE ٰ (suscrite) et les bases."""
    return HARAKAT.sub("", s).replace("\u0640", "")

def bare(s: str) -> str:
    """Strip tout (y compris ٰ et سuscrits) — squelette pur."""
    return HARAKAT.sub("", s).replace("\u0670", "").replace("\u0640", "").replace("\u0653", "")

def scan_raw(pat, label, maxp=15):
    rx = re.compile(pat)
    hits = []
    for s in range(1, 115):
        for n, t in C[str(s)]["ar"]:
            for m in rx.finditer(t):
                a, b = max(0, m.start() - 30), min(len(t), m.end() + 30)
                hits.append((f"{s}:{n}", t[a:b]))
    print(f"--- {label} : {len(hits)} occurrence(s)")
    for ref, ctx in hits[:maxp]:
        print(f"    {ref}  …{ctx}…")
    if len(hits) > maxp:
        print(f"    … +{len(hits)-maxp} autres")
    return hits

print("=== A. مَتَٰع / متاع (suscrites incluses) ===")
scan_raw(r"مَتَٰع|مَتَاع|مَتَٰٓع", "متاع raw (suscrite/madda)")
hits = []
for s in range(1, 115):
    for n, t in C[str(s)]["ar"]:
        for w in t.split():
            b = bare(w)
            if "متع" in b:
                hits.append((f"{s}:{n}", w))
print("--- squelette متع (mots entiers) :", len(hits))
for ref, w in hits[:15]:
    print(f"    {ref}  {w}")

print("")
print("=== B. مَرَّت dual de مَرَّة ===")
hits = []
for s in range(1, 115):
    for n, t in C[str(s)]["ar"]:
        for w in t.split():
            b = bare(w)
            if b.startswith("مرت") or "مرتين" in b or "مرتان" in b:
                hits.append((f"{s}:{n}", w))
print("--- squelette مرت* :", len(hits))
for ref, w in hits[:12]:
    print(f"    {ref}  {w}")

print("")
print("=== C. plurals du Dānī : تابعين / تائبون / قانتات / طائفات ===")
for sk, lab in (("تابعين", "تابعين"), ("تبعين", "تبعين"), ("تائبون", "تائبون"),
                ("تاوبون", "تاوبون"), ("قانيت", "قانيت(ت)"), ("قانتات", "قانتات"),
                ("طايف", "طايف"), ("طايفات", "طايفات")):
    hits = []
    for s in range(1, 115):
        for n, t in C[str(s)]["ar"]:
            for w in t.split():
                if sk in bare(w):
                    hits.append((f"{s}:{n}", w))
    print(f"--- {lab} : {len(hits)}")
    for ref, w in hits[:8]:
        print(f"    {ref}  {w}")

print("")
print("=== D. hamza warš : مستأخر / مستأنس / امتاز / استأنس ===")
for sk, lab in (("مستاىخر", "مستاىخر(suscrite)"), ("مستاخر", "مستاخر"), ("مستخر", "مستخر"),
                ("مستانيس", "مستانيس"), ("مستنيس", "مستنيس"), ("استانيس", "استانيس"),
                ("امتياز", "امتياز"), ("امتيز", "امتيز"), ("امتيزو", "امتيزو"), ("متيز", "متيز")):
    hits = []
    for s in range(1, 115):
        for n, t in C[str(s)]["ar"]:
            for w in t.split():
                if sk in bare(w):
                    hits.append((f"{s}:{n}", w))
    print(f"--- {lab} : {len(hits)}")
    for ref, w in hits[:8]:
        print(f"    {ref}  {w}")

print("")
print("=== E. يَتَمَى : squelettes تمي / تما / تتم ===")
for sk, lab in (("تمي", "تمي"), ("تماى", "تماى"), ("تمان", "تمان"), ("يتم", "يتم"), ("تتم", "تتم")):
    hits = []
    for s in range(1, 115):
        for n, t in C[str(s)]["ar"]:
            for w in t.split():
                if sk in bare(w):
                    hits.append((f"{s}:{n}", w))
    print(f"--- {lab} : {len(hits)}")
    for ref, w in hits[:10]:
        print(f"    {ref}  {w}")

print("")
print("=== F. خانتا (dual verbal bayt 4) ===")
hits = []
for s in range(1, 115):
    for n, t in C[str(s)]["ar"]:
        for w in t.split():
            if "خانتا" in bare(w) or "خانت" in bare(w):
                hits.append((f"{s}:{n}", w))
print("--- خانت* :", len(hits))
for ref, w in hits[:10]:
    print(f"    {ref}  {w}")
