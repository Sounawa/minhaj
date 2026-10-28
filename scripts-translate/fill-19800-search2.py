# -*- coding: utf-8 -*-
"""R345 — Script 2 : comptes et textes complets pour 19800."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')

bc = [(s, a, bare(tx)) for (s, a, tx) in corpus]

def find_all(skel, limit=60):
    out = []
    for (sn, an, b) in bc:
        start = 0
        while True:
            i = b.find(skel, start)
            if i < 0:
                break
            lo = max(0, i-38); hi = min(len(b), i+len(skel)+38)
            out.append((sn, an, b[lo:hi]))
            start = i + 1
            if len(out) >= limit:
                return out
    return out

def boundary(skel, follow_ok=None):
    out = []
    for (sn, an, b) in bc:
        start = 0
        while True:
            i = b.find(skel, start)
            if i < 0: break
            j = i + len(skel)
            okl = (i == 0 or b[i-1] == ' ')
            okr = (j == len(b) or b[j] == ' ' or (follow_ok and j < len(b) and b[j] in follow_ok))
            if okl and okr:
                lo = max(0, i-38); hi = min(len(b), j+38)
                out.append((sn, an, b[lo:hi]))
            start = i + 1
    return out

def full(sn, an):
    for (s, a, tx) in corpus:
        if s == sn and a == an:
            return bare(tx)
    return "?"

print("===== COMPTES =====")
for skel in ["سلطن", "شيطن", "طغوت", "طغت", "ظلمين", "ظلمون", "طغين", "طيع", "طاع", "أطع", "اطع",
             "الصفت", "صافت", "تيب", "حفظى", "شركاء", "شركا", "عظم"]:
    r = find_all(skel, 10**6)
    print(f"[{skel}] : {len(r)} pos")

print("\n[عظم] frontière de mot :")
r = boundary("عظم")
for (sn, an, ctx) in r:
    print(f"   {sn}:{an}  {ctx}")

print("\n[طاع] frontière de mot :")
r = boundary("طاع")
for (sn, an, ctx) in r[:14]:
    print(f"   {sn}:{an}  {ctx}")

print("\n[ظلمي] non suivi de ن (construct élidé) :")
n = 0
for (sn, an, b) in bc:
    start = 0
    while True:
        i = b.find("ظلمي", start)
        if i < 0: break
        j = i + 4
        if j < len(b) and b[j] != 'ن':
            n += 1
            if n <= 10:
                lo = max(0, i-40); hi = min(len(b), j+40)
                print(f"   {sn}:{an}  {b[lo:hi]}")
        start = i + 1
print("   total:", n)

print("\n[طغوت] toutes positions :")
for (sn, an, ctx) in find_all("طغوت", 10**6):
    print(f"   {sn}:{an}  {ctx}")

print("\n[سلطن] positions :")
r = find_all("سلطن", 10**6)
for (sn, an, ctx) in r:
    print(f"   {sn}:{an}  {ctx}")
print("   total:", len(r))

print("\n===== TEXTES COMPLETS CLÉS =====")
for (sn, an) in [(18,97),(18,82),(3,97),(6,38),(7,131),(27,47),(36,19),(17,13),(7,201),
                 (39,21),(56,65),(57,20),(104,4),(104,5),(79,2),(51,53),(52,32),(2,238),
                 (20,123),(81,21),(12,64),(37,7),(30,7),(18,22),(28,48),(66,4),(2,259),
                 (75,3),(86,4),(3,57),(2,25),(4,34),(6,92),(23,9),(70,34)]:
    print(f"--- {sn}:{an} ---")
    print(full(sn, an))

print("\n===== RAW 12:64 et 37:7 (vérif حفظا/حفظى) =====")
raw = json.load(open(CACHE))
for (sn, an) in [(12,64),(37,7)]:
    t = raw[str(sn)]["ar"][an-1][1]
    print(f"--- {sn}:{an} RAW ---")
    print(repr(t[:200]))
