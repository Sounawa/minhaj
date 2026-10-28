# -*- coding: utf-8 -*-
"""R341 — Recherche des fentes vides de 19776 (chapitre du rāʾ).
Restitution mot pour mot, ancrage cps, contre-vérification aux boundaries (règle ca)."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')

def find(skel, limit=14, boundary=None):
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
                out.append((sn, an, b[max(0, i-28):i+len(skel)+28]))
            start = i + 1
    return out[:limit]

QUERIES = [
    ("taradaytum (ترضيتم)", "ترضيتم", False),
    ("taradaytum-alt (تـرضـيتم)", "رضيتم", False),
    ("mirath (ميرث)", "ميرث", True),
    ("ra'ina (رعنا)", "رعنا", False),
    ("furashan (فرشا)", "فرشا", True),
    ("sirat-mu'arraf (الصراط)", "الصراط", True),
    ("sirat-munakkar (صراطا)", "صراطا", False),
    ("sirat-munakkar2 (صراطن)", "صراطن", False),
    ("ikrihihinna (كرههن)", "كرههن", False),
    ("arayta-akila (أريت)", "أريت", True),
    ("arayta-akila2 (ءريت)", "ءريت", False),
    ("araytum (أريتم)", "أريتم", False),
    ("rahimin (الرحيمين)", "الرحيمين", False),
    ("rahimin2 (رحيمين)", "رحيمين", False),
    ("rizqin (رزقين)", "رزقين", False),
    ("ra'un (رعون)", "رعون", False),
    ("kharrassun (الخرصون)", "الخرصون", False),
    ("kharrassun2 (خرصون)", "خرصون", False),
    ("raki'un (وركعون)", "وركعون", True),
    ("raki'un2 (ركعون)", "ركعون", True),
    ("mubashshirat (مبشرات)", "مبشرات", False),
    ("'awrat (عورت)", "عورت", False),
    ("mudabbirat (مدبرات)", "مدبرات", False),
    ("hasirat (حسرت)", "حسرت", False),
    ("ghamirat (غمرت)", "غمرت", False),
    ("nashirat (النشرت)", "النشرت", False),
    ("thamarat (الثمرت)", "الثمرت", False),
    ("thamarat2 (ثمرت)", "ثمرت", False),
    ("sabirat (الصبرت)", "الصبرت", False),
    ("maqsurat (مقصورت)", "مقصورت", False),
    ("sahirani (سحرن)", "سحرن", False),
    ("akhirani (ءاخرن)", "ءاخرن", False),
    ("akhirani2 (اخران)", "اخران", False),
    ("akhirani3 (خران)", "خران", False),
]

for label, skel, strict in QUERIES:
    hits = find(skel, limit=14)
    print(f"== {label} : {len(hits)}")
    for (sn, an, ctx) in hits[:8]:
        print(f"   {sn}:{an}  …{ctx}…")
print("########## CPS COMPLETS DES VERSETS PIVOTS ##########")
for (sn, an) in [(3,180),(57,10),(2,104),(16,80),(4,146),(24,58),(33,35),(55,72),(20,63),(28,48),(5,106),(78,38)]:
    try:
        tx = data[str(sn)]["ar"][an-1][1]
        b = bare(tx)
        print(f"--- FULL {sn}:{an}")
        print(b)
    except Exception as e:
        print(f"--- {sn}:{an} ERR {e}")
