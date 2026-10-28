# -*- coding: utf-8 -*-
"""R343 — Passe 2 : fentes restantes de 19798, avec normalisation yāʾ/alif-maqṣūra (Y unifié)."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')

def norm(t):
    """bare + unification ya/maqsura + hamza lignes/porteées optionnelle."""
    b = bare(t)
    return b.replace('\u064A', 'Y').replace('\u0649', 'Y')

def normH(t):
    """norm + unification hamza: ء أ إ آ ٱ أ→'"""
    n = norm(t)
    for h in '\u0621\u0623\u0625\u0622\u0671\u0624\u0626':
        n = n.replace(h, "'")
    return n

def find(skel, limit=20, boundary=False, hamza=False):
    out = []
    fn = normH if hamza else norm
    for (sn, an, tx) in corpus:
        b = fn(tx)
        start = 0
        while True:
            i = b.find(skel, start)
            if i < 0:
                break
            okb = True
            if boundary:
                okb = (i == 0 or b[i-1] == ' ') and (i+len(skel) == len(b) or b[i+len(skel)] == ' ')
            if okb:
                lo = max(0, i-36); hi = min(len(b), i+len(skel)+36)
                out.append((sn, an, b[lo:hi]))
            start = i + 1
    return out[:limit]

def count(skel, boundary=False, hamza=False):
    n = 0
    fn = normH if hamza else norm
    for (sn, an, tx) in corpus:
        b = fn(tx)
        start = 0
        while True:
            i = b.find(skel, start)
            if i < 0:
                break
            if not boundary or ((i == 0 or b[i-1] == ' ') and (i+len(skel) == len(b) or b[i+len(skel)] == ' ')):
                n += 1
            start = i + 1
    return n

# squelettes en Y (Y = ya OU maqsura), ' (hamza unifiée)
QUERIES = [
    ("P1 مفتري élidée (muftaran rasm-yāʾ)", "مفتري", True, False),
    ("P2 CONTRE مفترا pleine", "مفترا", True, False),
    ("P3 مفتر hamza-normalisé", "مفت'ر", False, True),
    ("Q1 قرى élidée (quran Y)", "قرY", True, False),
    ("Q2 CONTRE قرا pleine", "قرا", True, False),
    ("Q3 قرا hamza-norm", "قرا", False, True),
    ("R1 فرد TOUT (f-r-d)", "فرد", False, False),
    ("R2 فرد hamza-norm TOUT", "فرد", False, True),
    ("S1 بصر TOUT (bušrā hunt)", "بصر", False, False),
    ("S2 بصر hamza-norm TOUT", "بصر", False, True),
    ("S3 بشر TOUT", "بشر", False, False),
    ("T1 هذين (hamza-norm, duel)", "هذYن", True, False),
    ("T2 رجالين", "رجالYن", True, False),
    ("T3 كفين", "كفYن", True, False),
    ("T4 يدين", "يدYن", True, False),
    ("T5 ليالين", "لYالYن", True, False),
    ("U1 ترءا hamza-norm (toute forme)", "تر'ا", False, True),
    ("U2 اثبتن (le verbe du bayt)", "اثبتن", False, False),
]

for label, skel, bnd, hm in QUERIES:
    r = find(skel, 20, bnd, hm)
    print(f"### {label} : {count(skel, bnd, hm)} position(s)")
    for (sn, an, ctx) in r:
        print(f"  {sn}:{an}  {ctx}")
