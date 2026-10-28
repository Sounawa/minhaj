# -*- coding: utf-8 -*-
"""R344 — Recherche des fentes vides de 19799 (chapitre du zāy).
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
                lo = max(0, i-35); hi = min(len(b), i+len(skel)+35)
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
    # — Taḥlīl II : ǧazāʾū (j-z-hamza) — les 8 positions
    ("A0 جزا (SQUELETTE, toutes positions)", "جزا", False),
    ("A1 جزؤا (rasm 4 lettres, hamza-porteuse)", "جزؤا", False),
    ("A2 جزا + hamza-ligne", "جزاء", False),
    ("A3 جزا + hamza + alif final", "جزاءا", False),
    ("A4 جزاء + wāw + alif (ǧazāʾū pleine)", "جزاءوا", False),
    ("A5 جزؤا + wāw + alif", "جزؤوا", False),
    ("A6 يجز (le présent du verbe)", "يجز", False),
    ("A7 وجزا + hāʾ (ǧazāhā?)", "جزها", False),
    # — Taḥlīl I : vedettes soumises aux règles
    ("B1 تزور (tazāwaru, ḥaḏf išāra)", "تزور", False),
    ("B2 زكية (zakātan/zakiyyatan)", "زكية", True),
    ("B3 زكيا contre-vérif", "زكيا", False),
    ("B4 الزجرت (az-zajarat 37:2)", "الزجرت", False),
    ("B5 الزاجرات pleine", "الزاجرات", False),
    ("B6 همزت (hamazat)", "همزت", False),
    ("B7 همزات pleine", "همزات", False),
    ("B8 زهدين (zāhidīna — vedette?)", "زهدين", False),
    ("B9 زهد racine", "زهد", False),
    ("B10 الزرعون (az-zāriʿūna)", "الزرعون", True),
    ("B11 زرعون sans article", "زرعون", True),
    ("B12 تزرعون (tazraʿūna)", "تزرعون", True),
    ("B13 الزرع (racine z-r-ʿ)", "الزرع", False),
    # — Taḥlīl III : alif au ṭarf
    ("C1 غزي (ġuzzan? vedette)", "غزي", True),
    ("C2 عزي (ʿUzzā 53:19)", "عزي", True),
    ("C3 هذان (dual à l'alif)", "هذان", True),
    ("C4 خصمان (dual à l'alif)", "خصمان", True),
    ("C5 رجلان (dual à l'alif)", "رجلان", True),
    ("C6 هذين (dual au yāʾ)", "هذين", True),
    ("C7 عص (l'ʿaṣā)", "عصا", False),
    ("C8 عصي (rasm yāʾ de ʿaṣā)", "عصي", True),
    ("C9 انثي (ʾunṯā maqṣūra)", "انثي", True),
    ("C10 تقوي (taqwā maqṣūra)", "تقوي", True),
    # — contexte sūras
    ("D1 الشوري (aš-Šūrā)", "الشوري", False),
    ("D2 عقود (al-ʿuqūd)", "عقود", False),
    ("D3 الاولي (al-ʾūlā?)", "الاولي", False),
]

for label, skel, bnd in SECTIONS:
    r = find(skel, 16, bnd)
    print(f"### {label} : {count(skel, bnd)} position(s)")
    for (sn, an, ctx) in r:
        print(f"  {sn}:{an}  {ctx}")

print()
print("=== TEXTES COMPLETS CIBLES (bare) ===")
for (sn, an) in [(5,29),(5,33),(5,95),(12,56),(12,60),(12,88),(18,17),(18,74),(18,80),
                 (23,97),(37,2),(41,28),(42,40),(53,19),(56,64),(59,17),(2,85),(20,66),
                 (22,19),(5,23),(7,117),(2,62),(5,69),(22,17),(26,44),(26,45)]:
    print(f"--- {sn}:{an} ---")
    print(full(sn, an))
