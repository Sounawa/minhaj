# -*- coding: utf-8 -*-
"""R343 — Recherche des fentes vides de 19798 (chapitre du rāʾ -3-).
Restitution mot pour mot, ancrage cps, contre-vérification aux boundaries (règle ca)."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')

def find(skel, limit=16, boundary=False):
    out = []
    for (sn, an, tx) in corpus:
        b = bare(tx)
        start = 0
        while True:
            i = b.find(skel, start)
            if i < 0:
                break
            okb = True
            if boundary:
                okb = (i == 0 or b[i-1] == ' ') and (i+len(skel) == len(b) or b[i+len(skel)] == ' ')
            if okb:
                lo = max(0, i-30); hi = min(len(b), i+len(skel)+30)
                out.append((sn, an, b[lo:hi]))
            start = i + 1
    return out[:limit]

def count(skel, boundary=False):
    n = 0
    for (sn, an, tx) in corpus:
        b = bare(tx)
        start = 0
        while True:
            i = b.find(skel, start)
            if i < 0:
                break
            if boundary:
                if (i == 0 or b[i-1] == ' ') and (i+len(skel) == len(b) or b[i+len(skel)] == ' '):
                    n += 1
            else:
                n += 1
            start = i + 1
    return n

def full(sn, an):
    for (s, a, tx) in corpus:
        if s == sn and a == an:
            return bare(tx)
    return "?"

SECTIONS = [
    ("A1 المغيرت élidée (al-muğīrat, jamʿ muʾannaṯ)", "المغيرت", False),
    ("A2 CONTRE المغيرات pleine", "المغيرات", False),
    ("B1 فردى (élidée alif maqsura)", "فردي", False),
    ("B2 فرذى", "فرذى", False),
    ("B3 فرادى pleine", "فرادى", False),
    ("B4 فرادي pleine2", "فرادي", False),
    ("C1 رجعون élidée", "رجعون", True),
    ("C2 CONTRE راجعون pleine", "راجعون", True),
    ("D1 turab élidée تربا (boundary)", "تربا", True),
    ("D2 CONTRE turab pleine ترابا (boundary)", "ترابا", True),
    ("D3 CONTRE ترابين/اتراب", "اتراب", False),
    ("E1 سربيل élidée", "سربيل", False),
    ("E2 CONTRE سرابيل pleine", "سرابيل", False),
    ("F1 ترءا (une seule alif + hamza)", "ترءا", False),
    ("F2 ترء (sans alif finale)", "ترء", False),
    ("F3 تراء pleine", "تراء", False),
    ("F4 CONTRE-PT تراءت (8:48)", "تراءت", False),
    ("G1 تترى/تتري (le muʾannaṯ du duel)", "تتري", False),
    ("G2 تترا", "تترا", False),
    ("G3 تتراء", "تتراء", False),
    ("H1 مفتى élidée (muftan)", "مفتي", True),
    ("H2 CONTRE مفتيا pleine", "مفتيا", True),
    ("I1 قرى élidée (quran)", "قري", True),
    ("I2 CONTRE قريا pleine", "قريا", True),
    ("J1 بصرى (bušrā, ṣād)", "بصري", False),
    ("J2 بشرى (rasm b-s-r-ى)", "بشري", False),
    ("J3 بصر sans ى", "بصر", True),
    ("K1 هذين (le duel au yāʾ)", "هذين", True),
    ("K2 رجلين (duel au yāʾ)", "رجلين", True),
    ("K3 عينين (duel au yāʾ)", "عينين", True),
    ("K4 رجلان (duel PLEIN - exception)", "رجلان", True),
    ("K5 هذان (duel PLEIN - exception)", "هذان", True),
    ("L1 كتابين (duel au yāʾ)", "كتابين", True),
    ("M1 ساكين/ساقين (duel au yāʾ)", "ساقين", True),
    ("N1 ارداء (unrā?)", "ارداء", False),
]

for label, skel, bnd in SECTIONS:
    r = find(skel, 16, bnd)
    print(f"### {label} : {count(skel, bnd)} position(s)")
    for (sn, an, ctx) in r:
        print(f"  {sn}:{an}  {ctx}")

print()
print("=== TEXTES COMPLETS CIBLES ===")
for (sn, an) in [(100,3),(14,50),(16,81),(13,5),(27,67),(78,27),(78,33),(78,40),(8,48),(34,18)]:
    t = full(sn, an)
    print(f"--- {sn}:{an} : {t[:400]}")
