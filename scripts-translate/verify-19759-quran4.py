# -*- coding: utf-8 -*-
"""R334 — Passe 4 : recensements restants 19759 (awthān, ṣalaw/zakaw iʿdād,
narā/ḏikrā istitmār, aṯāth, ṯāwiyān, bytes critiques duels/mumāl/maṯānī)."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = []
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1]))
IDX = {(sn, an): tx for (sn, an, tx) in corpus}

def find(pat, label, ctx=20):
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

def hexspan(sura, aya, needle, width=10):
    tx = IDX.get((sura, aya), "")
    i = tx.find(needle)
    if i < 0:
        print(f"  {sura}:{aya} — '{needle}' ABSENT"); return
    seg = tx[max(0,i-width):min(len(tx), i+len(needle)+width)]
    print(f"  {sura}:{aya} | {seg}")
    print("    cps:", " ".join(f"{ord(ch):04X}" for ch in tx[i:i+len(needle)]))

print("■■■ PASSE 4 — 19759 ■■■")

# 1. AWTHĀN — racine avec diacritiques entre lettres
D = "[َُِّْٰٰۭۣٓ۟ۨۖۗۘۚۛۜۢۖ۟۠ۥۦٰ'ʾ]*"
find(f"[اأٱ]{D}و{D}ث{D}ن", "AWTHĀN (racine أ-و-ث)")
find(f"[اأٱ]{D}و{D}ث{D}ي", "أ-و-ث-ي (أُوثِيَ ?)")

# 2. Bytes critiques
print("\n■■■ BYTES CRITIQUES ■■■")
print("18:6 ءَاثَٰرِهِمْ (le hāʾ) :"); hexspan(18, 6, "ءَاثَٰرِهِم")
print("37:70 ءَاثَٰرِهِمْ :"); hexspan(37, 70, "ءَاثَٰرِهِم")
print("36:12 ءَاثَٰرَهُمْ :"); hexspan(36, 12, "ءَاثَٰرَهُم")
print("20:84 أَثَرِى :"); hexspan(20, 84, "أَثَرِى")
print("20:96 أَثَرِ :"); hexspan(20, 96, "أَثَرِ")
print("48:29 أَثَرِ :"); hexspan(48, 29, "أَثَرِ")
print("46:4 أَثَٰرَةٍ :"); hexspan(46, 4, "أَثَٰرَة")
print("73:20 ثُلُثَىِ :"); hexspan(73, 20, "ثُلُثَى")
print("15:87 ٱلْمَثَانِى :"); hexspan(15, 87, "مَثَانِ")
print("39:23 مَّثَانِىَ :"); hexspan(39, 23, "مَّثَانِ")
print("2:55 نَرَى :"); hexspan(2, 55, "نَرَى")
print("11:114 ذِكْرَى :"); hexspan(11, 114, "ذِكْرَى")
print("4:176 ٱلثُّلُثَانِ :"); hexspan(4, 176, "ثُّلُثَٰ?نِ".replace("ٰ?",""))
print("46:17 يَسْتَغِيثَانِ (après ثَ) :")
tx = IDX[(46,17)]; i = tx.find("يَسْتَغِيثَانِ")
print("   ", tx[max(0,i-8):i+14], "| cps:", " ".join(f"{ord(c):04X}" for c in tx[i:i+14]))

# 3. AṮĀTH — racine أ-ث-ث
find(f"[اأٱ]{D}ث{D}ث", "AṮĀTH أَثَاث (racine أ-ث-ث)")

# 4. ṮĀWĪYĀN — ث-و-ي
find(f"ث{D}و{D}ي", "ṮĀWĪY ثَاوٍ (racine ث-و-ي)")

# 5. IʿDĀD — صَلَو et زَكَو (l'alif dessinée wāw)
find(f"ص{D}ل{D}و{D}[اأٱٰ]", "ṢALAW صَلَو (l'alif du wāw)")
find(f"ز{D}ك{D}و{D}[اأٱٰ]", "ZAKAW زَكَو")
find(f"د{D}ع{D}و{D}[اأٱٰ]", "DAʿAW دَعَو (témoin de la classe)")

# 6. ISTITIMĀR — نَرَى / ذِكْرَى (l'alif devant un sukūn)
find(f"ن{D}ر{D}ى", "NARĀ نَرَى (toutes)")
find(f"ذ{D}ك{D}ر{D}ى", "ḎIKRĀ ذِكْرَى (toutes)")

# 7. BIYĀ / RUWIYĀ — les mots incertains du bayt 3
find(f"ب{D}ي{D}ا", "B-Y-ā (biyā ?)")
find(f"ر{D}و{D}ي", "R-W-Y (ruwiyā ?)")
