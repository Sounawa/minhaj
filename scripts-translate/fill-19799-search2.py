# -*- coding: utf-8 -*-
"""R344 — Script 2 : compléter les fentes de 19799.
1) Toutes positions de جز en 12 et 39 (les 8 élidées de la leçon : Ḥašr/Zumar/Yūsuf×3/Šūrā/Māʾida×2)
2) Formes à hāʾ et hamza-ligne (جزاءه, جزؤه, جزءا, جزاوا...)
3) Maqṣūras unifiées U+0649 (règle ca) : عزى, عصى, انثى, تقوى, الشورى, الاولى, هذين
4) Textes complets des cibles."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')

def find_all(skel, limit=40):
    out = []
    for (sn, an, tx) in corpus:
        b = bare(tx)
        start = 0
        while True:
            i = b.find(skel, start)
            if i < 0:
                break
            lo = max(0, i-40); hi = min(len(b), i+len(skel)+40)
            out.append((sn, an, b[lo:hi]))
            start = i + 1
            if len(out) >= limit:
                return out
    return out

def in_sura(sn, ch):
    """Toutes positions du caractère ch dans la sūra sn."""
    out = []
    for (s, a, tx) in corpus:
        if s != sn: continue
        b = bare(tx)
        start = 0
        while True:
            i = b.find(ch, start)
            if i < 0: break
            lo = max(0, i-45); hi = min(len(b), i+55)
            out.append((s, a, b[lo:hi]))
            start = i + 1
    return out

def full(sn, an):
    for (s, a, tx) in corpus:
        if s == sn and a == an:
            return bare(tx)
    return "?"

print("=== 1) TOUTES POSITIONS جز EN SŪRA 12 (Yūsuf) ===")
for (s, a, ctx) in in_sura(12, "جز"):
    print(f"  {s}:{a}  {ctx}")

print("\n=== 2) TOUTES POSITIONS جز EN SŪRA 39 (az-Zumar) ===")
for (s, a, ctx) in in_sura(39, "جز"):
    print(f"  {s}:{a}  {ctx}")

print("\n=== 3) FORMES À HĀʾ ET HAMZA-LIGNE (corpus entier) ===")
for skel in ["جزاءه", "جزؤه", "جزءه", "جزاها", "جزاءهم", "جزؤهم", "جزءوا", "جزاوا", "جزىوا", "جزءا", "جزاءا"]:
    r = find_all(skel, 10)
    print(f"  [{skel}] : {len(r)}")
    for (sn, an, ctx) in r:
        print(f"     {sn}:{an}  {ctx}")

print("\n=== 4) MAQṢŪRAS U+0649 (règle ca) ===")
for skel, bnd in [("عزى", True), ("عصى", False), ("انثى", True), ("تقوى", True),
                  ("الشورى", True), ("الاولى", True), ("هذين", True), ("هدين", True),
                  ("غزى", False), ("غزي", False)]:
    # boundary simple
    n = 0; hits = []
    for (sn, an, tx) in corpus:
        b = bare(tx)
        start = 0
        while True:
            i = b.find(skel, start)
            if i < 0: break
            okb = (i == 0 or b[i-1] == ' ') and (i+len(skel) == len(b) or b[i+len(skel)] == ' ')
            if not bnd or okb:
                n += 1
                if len(hits) < 12:
                    lo = max(0, i-40); hi = min(len(b), i+len(skel)+40)
                    hits.append((sn, an, b[lo:hi]))
            start = i + 1
    print(f"  [{skel}] boundary={bnd} : {n}")
    for (sn, an, ctx) in hits:
        print(f"     {sn}:{an}  {ctx}")

print("\n=== 5) TEXTES COMPLETS CIBLES 2 ===")
for (sn, an) in [(39,24),(39,25),(2,62),(5,69),(22,17),(2,85),(20,66),(26,44),(26,45),(7,117),
                 (41,28),(18,80),(12,56),(12,60),(12,88),(12,25),(12,47),(5,95),(5,38),(5,85),
                 (9,26),(9,82),(9,95),(10,27),(17,63),(18,88),(20,76),(25,15),(32,17),(34,37),(3,87),(3,136),(4,93)]:
    print(f"--- {sn}:{an} ---")
    print(full(sn, an))
