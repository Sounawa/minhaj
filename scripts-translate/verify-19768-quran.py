# -*- coding: utf-8 -*-
"""R336 — Vérification coranique étendue pour doc 19768 (chapitre du ḥāʾ).
Contrôle au muṣḥaf (quran-cache.json) :
  A. Inventaire systématique : ḥāʾ + alif SUSCRITE (حَٰ) vs ḥāʾ + alif PLEINE (حَا)
     vs ḥāʾ + alif à la MADDA (حَآ — alif porteuse de madda U+0653)
  B. Lexèmes de la leçon : išḥāq, le lexème ḥifẓ (ḥāfiẓ/yuḥāfiẓūn/ḥifẓ),
     les jamʿ mudakkar sālim (ḥākimūn/ḥāsibīn/ḥāširīn/ḥāmidūn),
     les jamʿ muʾannaṯ sālim (ṣāliḥāt/sāʾiḥāt/sābiḥāt/ḥāmilāt/musafiḥāt),
     maḥārīb, aṣḥāb, subḥāna, la racine ḥ-y-ǧ (tuḥāǧǧūnā), ḍuḥā (maqṣūr),
     le duel (y U+0648 + a alif pleine à l'extrémité)
  C. ISTITMĀR : تُحَآجُّونَ – إِسْحَاقَ – وَأَصْلَحَا – حَاجِزِينَ –
     يُحَافِظُونَ – حَافِّينَ – حَافِظُونَ – مَحَارِيبَ (thābit vs maḥḍūf)
  D. IʿDĀD en avance : chapitre du ḫāʾ — ḫāʾ + alif (خَٰ / خَا), ḫālid
Chaque sonde imprime : sūra:āya — rasm brut (contexte ± 25 car).
"""
import json, re
from collections import Counter

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = []  # (sura, aya, texte)
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1]))

def find(pat, label, note="", maxprint=60):
    rx = re.compile(pat)
    hits = []
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            st = max(0, m.start()-25); en = min(len(tx), m.end()+25)
            hits.append((sn, an, tx[st:en]))
    print(f"\n=== {label} — {len(hits)} occ. {note}")
    for (sn, an, ctx) in hits[:maxprint]:
        print(f"  {sn}:{an} | {ctx}")
    if len(hits) > maxprint:
        print(f"  ... +{len(hits)-maxprint} autres")
    return hits

def stat(pat, label):
    rx = re.compile(pat)
    full = sus = madda = 0
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            seg = m.group(0)
            if "\u0653" in seg: madda += 1
            elif "\u0670" in seg: sus += 1
            elif "ا" in seg: full += 1
    print(f"### {label}: pleine={full} suscrite={sus} madda={madda}")

print("■■■ R336 — VERIFICATIONS 19768 (chapitre du ḥāʾ) ■■■")

# ── A. INVENTAIRE SYSTÉMATIQUE ──────────────────────────────────────
print("\n────── A. INVENTAIRE ḥāʾ+alif ──────")
inv_sus = Counter(); inv_full = Counter(); inv_mad = Counter()
for (sn, an, tx) in corpus:
    for m in re.finditer(r"حَٰ(\S{0,10})", tx):
        inv_sus[m.group(0)[:8]] += 1
    for m in re.finditer(r"حَا(\S{0,10})", tx):
        if "\u0653" in m.group(0):
            inv_mad[m.group(0)[:8]] += 1
        else:
            inv_full[m.group(0)[:8]] += 1
print("— ḥāʾ+SUSCRITE (حَٰ) — lexèmes distincts:", len(inv_sus), "| occ:", sum(inv_sus.values()))
for w, c in inv_sus.most_common(40):
    print(f"   {w} ×{c}")
print("— ḥāʾ+PLEINE (حَا, sans madda) — lexèmes distincts:", len(inv_full), "| occ:", sum(inv_full.values()))
for w, c in inv_full.most_common(40):
    print(f"   {w} ×{c}")
print("— ḥāʾ+PLEINE à la MADDA (حَآ) — lexèmes distincts:", len(inv_mad), "| occ:", sum(inv_mad.values()))
for w, c in inv_mad.most_common(40):
    print(f"   {w} ×{c}")

# ── B. LEXÈMES DE LA LEÇON ──────────────────────────────────────────
print("\n────── B. LEXÈMES ──────")
# B1. išḥāq — « حَيْثُمَا ذُكِرَ فِي الْقُرْءَانِ »
find(r"سْحَق", "B1. IŠḤĀQ — les trois consonnes sans alif (rasm ḥaḏfiyya)", "attendu: partout suscrite")
stat(r"سْحَٰق|سْحَاق", "B1b. išḥāq alif suscrite vs pleine")
find(r"إِسْحَٰق", "B1c. IŠḤĀQ dessinée suscrite", "formes", maxprint=40)
find(r"إِسْحَاق", "B1d. IŠḤĀQ dessinée PLEINE (contrôle)", "attendu: 0", maxprint=10)

# B2. lexème ḥifẓ — la doctrine centrale de la leçon
find(r"حَٰفِظ", "B2a. ḤĀFIẒ à la suscrite (ḥaḏf)", "", maxprint=40)
find(r"حَافِظ", "B2b. ḤĀFIẒ à la PLEINE", "attendu: la seule 86:4", maxprint=20)
find(r"يُحَافِظ", "B2c. YUḤĀFIẒŪN — l'inaccompli du rubāʿī", "attendu: 3 — Anʿām/Muʾminūn/Maʿāriǧ, PLEINE")
find(r"حِفظ|حِفْظ", "B2d. ḤIFẒ squelette sans alif", "", maxprint=20)
find(r"حَفِظُونَ|حَٰفِظُونَ", "B2e. ḤĀFIẒŪN pluriel (jamʿ mudakkar sālim du taḥlīl)", "le « حَـِفظُونَ » de l'appareil", maxprint=10)

# B3. jamʿ mudakkar sālim de l'arǧūza — existeraient-ils au corpus ?
for w, lab in [("حَٰكِمِين|حَاكِمِين|حَٰكِمُون|حَاكِمُون", "B3a. ḤĀKIMĪN/ŪN"),
               ("حَٰسِبِين|حَاسِبِين|حَٰسِبُون|حَاسِبُون", "B3b. ḤĀSIBĪN/ŪN"),
               ("حَٰشِرِين|حَاشِرِين|حَٰشِرُون|حَاشِرُون", "B3c. ḤĀŠIRĪN/ŪN"),
               ("حَٰمِدِين|حَامِدِين|حَٰمِدُون|حَامِدُون", "B3d. ḤĀMIDĪN/ŪN")]:
    find(w, lab, "attente ouverte — mots de l'arǧūza", maxprint=12)

# B4. jamʿ muʾannaṯ sālim de l'arǧūza
for w, lab in [("صَٰلِح", "B4a. ṢĀLIḤĀT (rasm ḥaḏfiyya)"),
               ("سَٰئِح|سَائِح|سٓئِح", "B4b. SĀʾIḤĀT"),
               ("مُسَفِح", "B4c. MUSAFAḤĀT"),
               ("سَٰبِح|سَابِح", "B4d. SĀBIḤĀT"),
               ("حَٰمِل|حَامِل", "B4e. ḤĀMILĀT")]:
    find(w, lab, "", maxprint=30)

# B5. maḥārīb + aṣḥāb + subḥāna
find(r"مَحَٰرِيب|مَحَارِيب", "B5a. MAḤĀRĪB", "attendu: Sabaʾ, suscrite", maxprint=10)
stat(r"أَصْحَٰب|أَصْحَاب", "B5b. AṢḤĀB alif suscrite vs pleine")
find(r"أَصْحَاب", "B5c. AṢḤĀB à la PLEINE (contrôle)", "attendu: 0", maxprint=10)
stat(r"سُبْحَٰن|سُبْحَان", "B5d. SUBḤĀNA alif suscrite vs pleine")
find(r"سُبْحَان", "B5e. SUBḤĀNA à la PLEINE (contrôle)", "attendu: 0", maxprint=10)

# B6. racine ḥ-y-ǧ : le muḍāriʿ au nūn al-wiqāya + la madda
find(r"تُحَا|تُحَٰ|أَتُحَا|أَتُحَٰ|تَحَا|تَحَٰ", "B6a. TUḤĀǦǦŪNA — la mādda ḥ-y-ǧ", "2:139 attendu — alif à la MADDA")
find(r"حَاجَج|حَٰجَج|تُحَجّ|تُحَجّ", "B6b. ḤĀǦA/ḤAǦǦ verbes", "", maxprint=20)

# B7. ḍuḥā le maqṣūr + le duel à l'extrémité
find(r"ضُحَى|ضُحى", "B7a. ḌUḤĀ — le maqṣūr à la yāʾ", "attendu: 93:1", maxprint=10)
find(r"يُصْلِحَا|أَصْلَحَا", "B7b. YUṢLIḤĀ/AṢLAḤĀ — le DUEL à l'extrémité PLEINE", "alif du duel = thābit", maxprint=10)

# ── C. ISTITMĀR — les huit mots ─────────────────────────────────────
print("\n────── C. ISTITMĀR (8 mots) ──────")
for w, lab in [("تُحَا", "C1. tuḥāǧǧūna (madda → thābit ?)"),
               ("إِسْحَٰق", "C2. išḥāq (maḥḍūf partout ?)"),
               ("أَصْلَحَا|يُصْلِحَا", "C3. aṣlaḥā/yuṣliḥā (duel → thābit ?)"),
               ("حَاجِزِين|حَٰجِزِين", "C4. ḥāǧizīn (Quranique ?)"),
               ("يُحَافِظ", "C5. yuḥāfiẓūn (exception thābit)"),
               ("حَافِّين|حَٰفِّين|حَافُّون|حَٰفُّون", "C6. ḥāffīn (Quranique ?)"),
               ("حَٰفِظُون|حَافِظُون", "C7. ḥāfiẓūn (maḥḍūf ?)"),
               ("مَحَٰرِيب|مَحَارِيب", "C8. maḥārīb (maḥḍūf ?)")]:
    find(w, lab, "", maxprint=8)

# ── D. IʿDĀD EN AVANCE — chapitre du ḫāʾ ────────────────────────────
print("\n────── D. IʿDĀD ḫāʾ (en avance) ──────")
inv_k = Counter()
for (sn, an, tx) in corpus:
    for m in re.finditer(r"خَٰ(\S{0,10})", tx):
        inv_k[m.group(0)[:8]] += 1
    for m in re.finditer(r"خَا(\S{0,10})", tx):
        inv_k["PLEINE:"+m.group(0)[:8]] += 1
print("— ḫāʾ+alif — lexèmes distincts:", len(inv_k), "| occ:", sum(inv_k.values()))
for w, c in inv_k.most_common(30):
    print(f"   {w} ×{c}")

print("\n■■■ FIN R336-A ────────────────────────────────")
