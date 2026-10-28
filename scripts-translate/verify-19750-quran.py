#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérifications coraniques du doc 19750 (rasm-wa-dabt-4ep, chapitre du tāʾ).

Le doc enseigne (doctrine Wadghīrī / Dānī) :
  (1) bayt 1 : six mots élidées après le tāʾ — مَبْسُوطَتَـنِ التَّـلِيَـتِ مَرَّتَـنْ / خِتَـمُهُ مَتَعاً جَنَّتَـنْ
      + išāra ilā qirāʾa de « خَاتَمُهُ مِسْكٌ » ; mataʿān = duel ; 4 autres mots (images)
  (2) لفظ « الكِتَبِ » élidée DANS TOUT le Coran SAUF QUATRE positions (alif thābita) :
      a. 2e occurrence de sūrat al-Ḥiǧr    b. 2e occurrence de sūrat al-Kahf
      c. celle jointe à « أَجَلٍ » dans ar-Raʿd   d. 1re occurrence de sūrat an-Naml
  (3) مُسْتَـنِسِين — alif substituée à la hamza sākina chez Warš, puis élidée
  (4) pluriels salim : التَّـبِعِين / التَّـئِبُون / قَـنِتَـتْ (قَانِتَات) / تَـئِبَت (تَائِبَات)
  bayt 4 : فَخَانَتَـهُمَا (duel verbal) ; bayt 5 : طَآئِفَتَـنِ
"""
import json
import re

C = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json"))
HARAKAT = re.compile(r"[\u064B-\u0652\u0653-\u0655\u0670\u06D6-\u06ED\u08F0-\u08F3]")

def strip(s: str) -> str:
    return HARAKAT.sub("", s).replace("\u0640", "")

SUP = "\u0670"   # alif suscrite
AL = "\u0627"    # alif pleine

def verses_with_pat(pat_plain: str):
    """pat_plain : motifs SANS harakat (déjà strippés). Retourne (s:i, texte, contexte)."""
    out = []
    for s, obj in C.items():
        for n, t in obj["ar"]:
            st = strip(t)
            if pat_plain in st:
                out.append((s, n, t, st))
    return out

def kitab_positions():
    """Compte le lexème كتب (racine, formes rasm ktAb) et sépare alif suscrite vs pleine."""
    res = []
    for s, obj in C.items():
        for n, t in obj["ar"]:
            st = strip(t)
            # forme كتب avec ou sans alif ; on capture la voyelle de fin approximative
            for m in re.finditer(r"كتب", st):
                i = m.start()
                # détecter la graphie réelle dans le texte harakaté
                res.append((s, n, t, i))
    return res

def classify_kitab():
    """Sépare كِتَٰب (suscrite) / كِتَاب (pleine) — le motif harakaté كِتَ+alif+ب."""
    sus, full, other = [], [], []
    for s, obj in C.items():
        for n, t in obj["ar"]:
            for m in re.finditer(r"كِتَ", t):
                j = m.end()
                ch = t[j] if j < len(t) else ""
                tail = t[j+1] if j+1 < len(t) else ""
                # كِتَٰب : suscrite ; كِتَاب / كِتَٱب : pleine
                if ch == SUP and tail in "ب":
                    sus.append((s, n))
                elif ch in (AL, "\u0671") and tail == "ب":
                    full.append((s, n))
                else:
                    other.append((s, n, ch, tail))
    return sus, full, other

print("=" * 70)
print("A. LEXÈME كِتَاب — suscrite vs pleine dans le corpus entier")
sus, full, other = classify_kitab()
print(f"   كِتَٰب  (alif SUSCRITE = élidée)      : {len(sus)} positions")
print(f"   كِتَاب  (alif PLEINE = thābita)      : {len(full)} positions")
if other:
    print(f"   autres graphies                     : {len(other)} — ex. {other[:3]}")
print("   --- positions à alif PLEINE (les exceptions revendiquées : 15/2e, 18/2e, 13 apr. aǧal, 27/1re) ---")
for s, n in full:
    print(f"     {s}:{n}")
print("   --- textes des positions pleines ---")
seen = set()
for s, n in full:
    if (s, n) in seen:
        continue
    seen.add((s, n))
    for ss, obj in C.items():
        if ss == s:
            for nn, t in obj["ar"]:
                if nn == n:
                    print(f"   [{s}:{n}] {t}")
print("   --- échantillon suscrite (10) ---")
cnt = 0
for s, n in sus:
    if cnt >= 10:
        break
    for ss, obj in C.items():
        if ss == s:
            for nn, t in obj["ar"]:
                if nn == n:
                    print(f"   [{s}:{n}] {t[:80]}")
                    cnt += 1

print("=" * 70)
print("B. Les QUATRE exceptions revendiquées — ordre dans chaque sourate")
for s in ("15", "18", "13", "27"):
    occ = [(n, t) for ss, obj in C.items() if ss == s for n, t in obj["ar"] if "كِتَ" in strip(t) or "كتب" in strip(t)]
    print(f"   --- sūra {s} : {len(occ)} occurrence(s) du lexème ---")
    for n, t in occ:
        st = strip(t)
        idx = st.find("كِتَ") if "كِتَ" in st else st.find("كتب")
        print(f"     {s}:{n} … {st[max(0,idx-25):idx+18]} …")

print("=" * 70)
print("C. DUEL مَتَاع — occurrences du lexème مَتَاع (toutes graphies)")
for s, n, t, st in verses_with_pat("متاع"):
    idx = st.find("متاع")
    print(f"   [{s}:{n}] {st[max(0,idx-20):idx+25]}")

print("=" * 70)
print("D. خِتَام — occurrences du lexème")
for s, n, t, st in verses_with_pat("ختم"):
    idx = st.find("ختم")
    print(f"   [{s}:{n}] {t}")

print("=" * 70)
print("E. DUELS nominaux et verbaux revendiqués (alif pleine dans le corpus ?)")
for pat, label in [("جنتان", "جَنَّتَانِ"), ("مبحوطتن", "?"), ("مبسوطتن", "مَبْسُوطَتَانِ élidée"),
                   ("مبسوطتن", "دuel مَبْسُوطَتَانِ"), ("فخانتم", "فَخَانَتَاهُمَا élidée"),
                   ("فخانتم", "فَخَانَتَاهُمَا"), ("طائفتن", "طَائِفَتَانِ élidée"),
                   ("مبتن", "?")]:
    hits = verses_with_pat(pat)
    if hits:
        print(f"   [{label}] {len(hits)} hit(s)")
        for s, n, t, st in hits[:6]:
            idx = st.find(pat)
            print(f"     [{s}:{n}] {st[max(0,idx-22):idx+25]}")
# formes pleines
for pat, label in [("فخانتم", "فَخَانَتَاهُمَا"), ("مبسوطتن", "مَبْسُوطَتَانِ")]:
    hits = verses_with_pat(pat)
    print(f"   [{label}] élidée-spelling hits : {len(hits)}")
print("   --- formule exacte 5:64 et 55:46/62 et 66:10 ---")
for s, i in (("5", 64), ("55", 46), ("55", 62), ("66", 10), ("83", 26), ("66", 5), ("13", 38)):
    obj = C[s]
    for n, t in obj["ar"]:
        if n == i:
            print(f"   [{s}:{i}] {t}")

print("=" * 70)
print("F. Pluriels salim et autres mots du matn — présence/absence")
for pat, label in [("تابعين", "التَّابِعِينَ"), ("تابعون", "تَابِعُونَ"),
                   ("تائبين", "التَّائِبِينَ"), ("تائبون", "التَّائِبُونَ"),
                   ("تائبت", "تَائِبَات / تَائِبَت"), ("قانت", "قَانِت"),
                   ("مستانس", "مُسْتَانِس (Warš)"), ("مستأنس", "مُسْتَأْنِس"),
                   ("يتمي", "يَتَمَّى ?"), ("تمي", "…تمي"), ("متم", "…تمم/تمم"),
                   ("تليت", "التَّالِيَتِ ?"), ("تليت", "التَّلِيَتِ"),
                   ("مبتن", "مَرَّتَنْ ?"), ("كيفم", "كَيْفَمَا ?"),
                   ("امتز", "امْتَزُوا ?"), ("المستخرين", "الْمُسْتَخِرِينَ ?"),
                   ("المتخرون", "الْمُتَخِرُونَ ?")]:
    hits = verses_with_pat(pat)
    print(f"   [{label}] : {len(hits)} hit(s)")
    for s, n, t, st in hits[:5]:
        idx = st.find(pat)
        print(f"     [{s}:{n}] {st[max(0,idx-25):idx+30]}")
