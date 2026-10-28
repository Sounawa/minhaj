# -*- coding: utf-8 -*-
"""R341 — Passe 2 corrigée : hamza normalisée + frontières de mots (règle ca) + CPS pivots."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

DIAC = r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]'

def bare(t):
    return re.sub(DIAC, '', t).replace('\u0671', '\u0627')

def hnorm(t):
    return bare(t).replace('\u0623', '\u0627').replace('\u0625', '\u0627').replace('\u0622', '\u0627').replace('\u0621', '')

def wcps(sn, an):
    return data[str(sn)]["ar"][an-1][1]

# ---------- Recherches frontières de mots (squelettes hamza-normalisés) ----------
QUERIES = [
    ("رعينا (rāʿinā/rаʿīnā)", "رعينا"),
    ("رعون au début de mot (rāʿūna)", "رعون"),
    ("رحمون (rāḥimūna)", "رحمون"),
    ("رحيمين (raḥimīn)", "رحيمين"),
    ("الركعون (al-rākiʿūna)", "الركعون"),
    ("ركعون début mot (munakkar)", "ركعون"),
    ("الركعين (al-rākiʿīna)", "الركعين"),
    ("ركعين début mot", "ركعين"),
    ("تابون (at-tāʾibūna)", "تابون"),
    ("ساحون (as-sāʾiḥūna)", "ساحون"),
    ("صامون (aṣ-ṣāʾimūna)", "صامون"),
    ("طاغون (aṭ-ṭāġūna)", "طاغون"),
    ("غاون (al-ġāwūna)", "غاون"),
    ("صبين (aṣ-ṣābiʾīna)", "صبين"),
    ("راعي (ar-rāʿī)", "راعي"),
    ("يا قطين (al-yaqṭīn)", "يقطين"),
    ("اكرهن hamza-norm (ukrihhunna)", "اكرهن"),
    ("كرهن nú", "كرهن"),
    ("ارايت hamza-norm (a-raʾayta/tum)", "ارايت"),
    ("ميرث (mīraṯ)", "ميرث"),
    ("ميراث (pleine)", "ميراث"),
    ("فرشا (firāšan)", "فرشا"),
    ("فراشا (pleine)", "فراشا"),
    ("صرط (ṣirāṭ ḥaḏf)", "صرط"),
    ("صراط (pleine)", "صراط"),
    ("ثمرت (ṯamarāt ḥaḏf)", "ثمرت"),
    ("ثمرات (pleine)", "ثمرات"),
    ("حسرت début mot (ḥasrāt)", "حسرت"),
    ("غمرت début mot", "غمرت"),
    ("نشرت (našrāt)", "نشرت"),
    ("صبرت (ṣabrāt)", "صبرت"),
    ("مبشرت (mubašširāt)", "مبشرت"),
    ("مبشرات (pleine)", "مبشرات"),
    ("عورت (ʿawrāt)", "عورت"),
    ("مدبرت (mudabbirāt)", "مدبرت"),
    ("مقصورت (maqṣūrāt)", "مقصورت"),
    ("رزقين (rizqīn)", "رزقين"),
    ("رازقين (pleine)", "رازقين"),
    ("خرصون (ḫarrāṣūna)", "خرصون"),
    ("خراصون (pleine)", "خراصون"),
    ("سحرن (saḥirān ḥaḏf)", "سحرن"),
    ("سحران (dual alif pleine)", "سحران"),
    ("ساحران (pleine totale)", "ساحران"),
    ("اخرن hamza-norm", "اخرن"),
    ("اخران hamza-norm (ʾāḫarān pleine)", "اخران"),
]
for label, skel in QUERIES:
    hits = []
    for (sn, an, tx) in corpus:
        h = hnorm(tx)
        for m in re.finditer(re.escape(skel), h):
            i = m.start()
            avant = h[i-1] if i > 0 else ' '
            apres = h[i+len(skel)] if i+len(skel) < len(h) else ' '
            # frontière de mot : début OU précédé d'espace
            if i == 0 or avant.isspace():
                hits.append((sn, an, bare(tx)[max(0,i-25):i+len(skel)+25]))
                break
    print(f"== {label} : {len(hits)}")
    for (sn, an, ctx) in hits[:8]:
        print(f"   {sn}:{an}  …{ctx}…")

print("\n########## CPS COMPLETS — PIVOTS ##########")
pivots = [(2,104),(4,24),(3,180),(57,10),(2,22),(1,6),(2,142),(30,46),(24,58),(79,5),
          (2,167),(35,8),(6,93),(77,3),(33,35),(55,72),(51,10),(9,112),(3,43),
          (20,63),(28,48),(5,106),(16,106),(20,73),(23,72),(15,20),(62,11),(5,114)]
for (sn, an) in pivots:
    print(f"--- {sn}:{an}")
    print(wcps(sn, an))
