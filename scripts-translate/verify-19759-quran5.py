# -*- coding: utf-8 -*-
"""R334 — Passe 5 : résolution finale 19759.
(1) أَمْثَال/أَمْثَٰل — le mot de la règle « de Maryam au sceau » ;
(2) codepoints exacts 39:23 مَّثَانِىَ et 4:176 ٱلثُّلُثَانِ (ordre shadda) ;
(3) أُنثَى toutes formes ; (4) racine أ-ث-ب exhaustive ; (5) الْمَوْتَى ;
(6) contraste نَرَى/ذِكْرَى : dagger vs bare selon le contexte suivant.
"""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = []
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1]))
IDX = {(sn, an): tx for (sn, an, tx) in corpus}

D = "[َُِّْٰٰۭۣٓ۟ۨۖۗۘۚۛۜۢۖ۟۠ۥۦٰ'ʾ]*"

def find(pat, label, ctx=18):
    rx = re.compile(pat)
    hits = []
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            st = max(0, m.start()-ctx); en = min(len(tx), m.end()+ctx)
            hits.append((sn, an, m.group(0), tx[st:en]))
    print(f"\n=== {label} — {len(hits)} occ.")
    for (sn, an, g, c) in hits:
        print(f"  {sn}:{an} [{g}] | {c}")
    return hits

def cps(sura, aya, needle, n=12):
    tx = IDX.get((sura, aya), "")
    i = tx.find(needle)
    if i < 0:
        print(f"  {sura}:{aya} — '{needle}' ABSENT"); return None
    print(f"  {sura}:{aya} | {tx[max(0,i-10):i+n+6]}")
    print("    cps:", " ".join(f"{ord(c):04X}" for c in tx[i:i+n]))
    return i

print("■■■ PASSE 5 — 19759 ■■■")

# 1. أَمْثَال — toutes graphies (alif pleine OU suscrite entre م et ث... non : entre ث et ل)
print("\n--- 1. AMṮĀL أَمْثَال (alif entre ث et ل, toutes graphies) :")
find(f"أ{D}م{D}ث{D}[اٰ]{D}ل", "أَمْثَال/أَمْثَٰل")

# le mot الْأَمْثَٰل avec article
find(f"ٱ{D}ل{D}أ{D}م{D}ث{D}[اٰ]{D}ل", "ٱلْأَمْثَال (avec article)")

# 2. codepoints exacts — shadda ordre
print("\n--- 2. CODEPOINTS EXACTS ---")
tx = IDX[(39, 23)]
i = tx.find("مُّ")
# chercher le segment ث + [alif?] + ن dans 39:23
for m in re.finditer(f"ث{D}[اىٰ]?{D}ن", tx):
    seg = m.group(0)
    print(f"  39:23 match [{seg}] cps:", " ".join(f"{ord(c):04X}" for c in seg))
tx2 = IDX[(4, 176)]
for m in re.finditer(f"ث{D}[اىٰ]?{D}ن{D}ِ", tx2):
    seg = m.group(0)
    print(f"  4:176 match [{seg}] cps:", " ".join(f"{ord(c):04X}" for c in seg))
tx3 = IDX[(15, 87)]
for m in re.finditer(f"ث{D}[اىٰ]?{D}ن", tx3):
    seg = m.group(0)
    print(f"  15:87 match [{seg}] cps:", " ".join(f"{ord(c):04X}" for c in seg))

# 3. أُنثَى — toutes formes
print("\n--- 3. ANṮĀ أُنثَى (toutes formes, tolérant) :")
find(f"[اأٱ]?{D}ل?{D}[اأٱ]?{D}ن{D}ث{D}[اىٰي]", "أُنثَى/الْأُنثَى (tolérant)")

# 4. racine أ-ث-ب
print("\n--- 4. racine أ-ث-ب (exhaustif) :")
for init in "اأ":
    find(f"{init}{D}ث{D}ب", f"{init}-ث-ب")

# 5. الْمَوْتَى
print("\n--- 5. MAWTĀ الْمَوْتَى :")
find(f"ٱ{D}ل{D}م{D}و{D}ت{D}[ىٰي]", "ٱلْمَوْتَى")

# 6. contraste dagger/bare : نَرَى et ذِكْرَى selon contexte
print("\n--- 6. CONTRASTE نَرَى/ذِكْرَى (dagger vs bare) ---")
for pat, lbl in [(f"ن{D}ر{D}[ىٰ]", "نَرَى (toutes)"), (f"ذ{D}ك{D}ر{D}[ىٰي]", "ذِكْرَى (toutes)")]:
    rx = re.compile(pat)
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            seg = m.group(0)
            nxt = tx[m.end():m.end()+3]
            has_dagger = "ٰ" in seg
            print(f"  {sn}:{an} [{seg}] dagger={has_dagger} | next:'{nxt}'")
