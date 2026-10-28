# -*- coding: utf-8 -*-
"""R336 — Vérifications 19768, passe 3 : dernières sondes ciblées."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = []
for k in sorted(data, key=int):
    for a in data[k]["ar"]:
        corpus.append((int(k), a[0], a[1]))

def dump(sn, an, note=""):
    for (s, a, tx) in corpus:
        if s == sn and a == an:
            print(f"  [{sn}:{an}] {note}: {tx[:160]}")

def find(pat, label, maxprint=10):
    rx = re.compile(pat)
    hits = []
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            st = max(0, m.start()-30); en = min(len(tx), m.end()+30)
            hits.append((sn, an, tx[st:en]))
    print(f"=== {label} — {len(hits)} occ.")
    for (sn, an, ctx) in hits[:maxprint]:
        print(f"  {sn}:{an} | {ctx}")
    return hits

print("■■ R336 PASSE 3 ■■")
print("\n— Q1. 51:1 (sābiḥāt) + 9:112 + 66:5 (contextes complets) —")
dump(51, 1, "ḍ-ḏāriyāt")
dump(9, 112, "ṭawba")
dump(66, 5, "taḥrīm")

print("\n— Q2. sābiḥāt dessin (tolérant sur l'ordre) —")
find(r"س\S{0,3}ٰب\S{0,2}ح\S{0,3}ت", "Q2a. sābiḥāt (U+0670 avant le bāʾ)")

print("\n— Q3. حَآفِّي — localisation —")
find(r"ح\S{0,3}ف\S{0,3}ف|حَآف|حَٰٓف", "Q3a. ḥāffī (racine ḥ-f-f / madda)")

print("\n— Q4. خَٰفَتُو — localisation —")
find(r"خ\S{0,2}ٰف\S{0,3}ت", "Q4a. ḫāfatū suscrite")

print("\n— Q5. ṣāliḥāt — les DEUX alifs suscrites (radicale + terminale) —")
find(r"ٰل\S{0,2}ح\S{0,3}ٰت", "Q5a. ṣāliḥāt complet", maxprint=50)

print("\n— Q6. le bayt 4 du matn : « وَالْحِفْظُ إِلاَّ حَافِظٌ يُحَافِظُونْ » — rappel des positions —")
find(r"عَلَيْهَا حَافِظ", "Q6a. 86:4 an-nāziʿāt", maxprint=3)

print("\n■■ FIN PASSE 3 ■■")
