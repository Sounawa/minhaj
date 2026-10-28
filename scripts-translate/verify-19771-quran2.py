# -*- coding: utf-8 -*-
"""R339 — Passe 2 : texte diacrité COMPLET des versets clés + squelettes manquants.
Objectif : rasm exact (alif pleine / suscrite / wāw / élidée) position par position.
"""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))

FULL = [
    (4, 7), (4, 33), (40, 60), (55, 6), (20, 63), (28, 23), (27, 66), (7, 38),
    (22, 38), (52, 8), (70, 2), (2, 197), (41, 34), (5, 64), (5, 91), (5, 82),
    (8, 42), (60, 4), (6, 52), (18, 28), (3, 26), (2, 237), (75, 36),
    (24, 35), (53, 20), (2, 276), (2, 3), (2, 43),
    (2, 38), (40, 18), (50, 23), (50, 28), (14, 41), (27, 10), (27, 19), (46, 15),
]
for (sn, an) in FULL:
    tx = data[str(sn)]["ar"][an-1][1]
    print(f"--- {sn}:{an}")
    print(tx)
    print()

def bare(t):
    t = re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t)
    return t.replace('\u0671', '\u0627')

corpus = []
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1]))

for label, skel in [
    ("تدارك/تدرك", "تدرك"), ("دارك", "دارك"), ("يدارك", "يدارك"),
    ("ادرا", "ادرا"), ("درأ", "درأ"), ("درء", "درء"),
    ("جاهد", "جاهد"), ("جهدك", "جهدك"), ("جاهدكم", "جاهدكم"),
    ("اتعد", "اتعد"), ("اعدني", "اعدني"), ("عذنني", "عذنني"),
    ("معدود", "معدود"), ("شاهد", "شاهد"), ("عابد", "عابد"),
    ("هداي", "هداي"), ("هدى", "هدى"), ("غدو", "غدو"),
    ("استبدال", "استبدال"), ("بدارا", "بدارا"),
]:
    res = []
    for (sn, an, tx) in corpus:
        b = bare(tx)
        if skel in b:
            i = b.index(skel)
            res.append((sn, an, b[max(0,i-20):i+len(skel)+20]))
    print(f"== {label} : {len(res)}")
    for (sn, an, ctx) in res[:6]:
        print(f"   {sn}:{an}  …{ctx}…")
