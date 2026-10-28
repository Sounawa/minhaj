# -*- coding: utf-8 -*-
"""R340 — Vérification coranique 19774 (fascule du ḏāl muʿǧam).
Restitution des fentes vides : mulḥaq bil-muṯannā, jamʿ sālimān, aṭ-ḏāriyāt,
muttaḫiḏāt, ǧuḏḏan, aḏānu tawba, ḏālika élide, aḏā/aḏan, ḏā, iḏā/iḏan.
"""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]
def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')
def find(skel, limit=6, word=False):
    out = []
    for (sn, an, tx) in corpus:
        b = bare(tx)
        if skel in b:
            i = b.index(skel)
            out.append((sn, an, b[max(0,i-28):i+len(skel)+28]))
    return out[:limit]

QUERIES = [
    ("هذان/هذني (hāḏāni)", "هذان"),
    ("هذن élide", "هذن"),
    ("ذاكرات/ذاكرت", "ذاكرات"),
    ("متخذات/متخذت (muttaḫiḏāt)", "متخذات"),
    ("متخذ (racine)", "متخذ"),
    ("الذاريات (aṭ-ḏāriyāt)", "الذاريات"),
    ("جذذا/جذذ (ǧuḏḏ)", "جذذ"),
    ("اذن توبة (aḏānu tawba)", "اذن توبة"),
    ("اذن (racine aḏān)", "اذن"),
    ("ءاذان (adhan muḥtaraẓ)", "ءاذان"),
    ("كيف ذلك (ḏālik élide)", "كيف ذلك"),
    ("كيف ذلك (ḏālika)", "كيف ذلك"),
    ("ذلك élide", "ذلك"),
    ("اذى (aḏā)", "اذى"),
    ("اذي (aḏā yāʾ)", "اذي"),
    ("اذن/اذنً (iḏan)", "اذن"),
    ("اذا (iḏā/iḏan)", "اذا"),
    ("ذا (ḏā)", "ذا"),
    ("ذات (ḏāt)", "ذات"),
]
for label, skel in QUERIES:
    res = find(skel)
    print(f"== {label} : {len(res)}")
    for (sn, an, ctx) in res[:6]:
        print(f"   {sn}:{an}  …{ctx}…")

# textes diacrités complets des versets pivots
for (sn, an) in [(22,19), (51,1), (51,2), (2,229), (4,35), (3,102), (2,226),
                 (24,33), (2,229), (2,223), (9,127), (22,19), (2,229)]:
    pass
for (sn, an) in [(22,19), (51,1), (2,229)]:
    print(f"--- FULL {sn}:{an}")
    print(data[str(sn)]["ar"][an-1][1])
