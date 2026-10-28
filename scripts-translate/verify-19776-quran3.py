# -*- coding: utf-8 -*-
"""R341 — Passe 3 finale : comptes exacts + CPS versets à citer."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

DIAC = r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]'
def bare(t): return re.sub(DIAC, '', t).replace('\u0671', '\u0627')
def hnorm(t):
    b = bare(t)
    for a, r in [('\u0623','\u0627'),('\u0625','\u0627'),('\u0622','\u0627'),('\u0626','\u064A'),('\u0621',''),('\u0654',''),('\u0655','')]:
        b = b.replace(a, r)
    return b
def wcps(sn, an): return data[str(sn)]["ar"][an-1][1]

# comptes exacts (sous-chaîne, sans limite)
for label, skel in [("صرط total", "صرط"), ("ثمرت total", "ثمرت"),
                    ("رعينا/رعنا", "رعنا"), ("رايت hamza-norm", "رايت"),
                    ("رایت pl", "رايتكم"), ("اكراهن", "اكراهن"),
                    ("تابون nú", "تابون"), ("ساحون nú", "ساحون"),
                    ("صامون nú", "صامون"), ("صبين nú", "صبين"),
                    ("طاغون nú", "طاغون"), ("خرصون nú", "خرصون"),
                    ("مدبرت nú", "مدبرت"), ("مقصورت nú", "مقصورت"),
                    ("رزقين nú", "رزقين"), ("صبرت nú", "صبرت")]:
    hits = [(sn, an) for (sn, an, tx) in corpus if skel in hnorm(tx)]
    print(f"== {label} : {len(hits)} -> {hits[:20]}")

print("\n##### A-RA-AYTA family #####")
for (sn, an, tx) in corpus:
    h = hnorm(tx)
    if "رايت" in h:
        i = h.index("رايت")
        print(f"   {sn}:{an}  …{bare(tx)[max(0,i-30):i+45]}…")

print("\n########## CPS À CITER ##########")
verses = [(2,104),(4,24),(3,180),(57,10),(2,22),(1,6),(2,142),(30,46),(24,31),(24,58),
          (79,5),(2,167),(35,8),(6,93),(77,3),(33,35),(55,72),(51,10),(9,112),(3,43),
          (20,63),(28,48),(5,106),(5,107),(5,55),(23,8),(70,32),(16,106),(20,73),
          (23,72),(15,20),(62,11),(5,114),(37,146),(51,53),(2,62),(6,142),(81,10)]
for (sn, an) in verses:
    print(f"--- {sn}:{an}")
    print(wcps(sn, an))
