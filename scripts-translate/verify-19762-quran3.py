# -*- coding: utf-8 -*-
"""R335 — Vérification 19762 (3) — sondes sur squelette sans diacritiques
(shadda-order-proof) + reprise des graphies à l'article."""
import json, re
from collections import Counter

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))

def strip_diac(t):
    # retire harakat, tanwin, shadda, sukun, suscrite, petites marques, annotation mark-up
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0653-\u0655\u08F0-\u08FF]", "", t)

def codepoints(t):
    return " ".join(f"{ord(c):04X}" for c in t)

corpus = []
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1], a[1], strip_diac(a[1])))

def sfind(pat, label, maxprint=45):
    """pat est en squelette SANS diacritiques ; renvoie sūra:āya + rasm BRUT."""
    rx = re.compile(pat)
    hits = []
    for (sn, an, tx_raw, _, sx) in corpus:
        for m in rx.finditer(sx):
            hits.append((sn, an, m.group(0)))
    print(f"\n=== {label} — {len(hits)} occ.")
    seen = Counter(h[2] for h in hits)
    for w, c in seen.most_common(12):
        print(f"   {c:3d}× {w}")
    # contexte brut pour les 12 premières
    for (sn, an, w) in hits[:12]:
        for (s2, a2, tx_raw, _, sx) in corpus:
            if s2 == sn and a2 == an and w in sx:
                i = sx.find(w)
                print(f"  {sn}:{an} | {tx_raw[max(0,i-20):i+len(w)+14]}")
                break
    return hits

print("■■■ R335 — VERIFICATIONS 19762 (3) — squelette ■■■")

# 0. Codepoints du passage 6:96 (ordre des diacritiques de la shadda)
for (sn, an, tx_raw, _, sx) in corpus:
    if sn == 6 and an == 96:
        i = tx_raw.find("سَكَن")
        seg = tx_raw[max(0, i-16):i+6]
        print("SEG 6:96:", seg)
        print("CODEPOINTS:", codepoints(seg))

# 1. ṣalāt : article + wāw vs article + alif
sfind(r"[اأٱ]لصلو[^ ]{0,3}", "aṣ-ṣalāt WĀW (squelette الصلو)")
sfind(r"[اأٱ]لصلا[^و][^ ]{0,3}", "aṣ-ṣalāt ALIF (squelette الصلا)")

# 2. zakāt : toutes graphies
sfind(r"زكو[^ ]{0,3}", "zakāt WĀW (squelette زكو)")
sfind(r"زكا[^وو]", "zakāt ALIF (squelette زكا)")

# 3. ribā
sfind(r"ربو[^ ]{0,3}", "ribā WĀW (squelette ربو)")
sfind(r"ربا[^ ]{0,3}|رب[ًى]", "ribā ALIF (squelette ربا)")

# 4. al-ayl : وجعل + الليل
sfind(r"[اأٱ]?وجعل [اأٱ]?لليل[^ ]{0,2}|جعل [اأٱ]?لليل[^ ]{0,2}", "ǧaʿala + al-ayl (squelette)")

# 5. mutabarriǧat
sfind(r"متبرج[^ ]{0,4}", "mutabarriǧ (squelette)")

# 6. la phrase du iḥtirāz : ce qui N'EST PAS suivi de al-ayl — échantillon des ǧaʿala
sfind(r"[اأٱ]لليل[^ ]{0,2}", "al-ayl (toutes positions)", maxprint=20)

print("\n■■■ FIN (3) ■■■")
