# -*- coding: utf-8 -*-
"""R334 — Passe 3 : bytes des rasm critiques, racines exhaustives, lacunes 19759."""
import json, re, unicodedata

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = []
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1]))
IDX = {(sn, an): tx for (sn, an, tx) in corpus}

def hexspan(sura, aya, needle, width=14):
    """Affiche le rasm et le codepoint de chaque char autour de needle."""
    tx = IDX[(sura, aya)]
    i = tx.find(needle)
    if i < 0:
        print(f"  {sura}:{aya} — '{needle}' ABSENT"); return
    lo = max(0, i-width); hi = min(len(tx), i+len(needle)+width)
    seg = tx[lo:hi]
    print(f"  {sura}:{aya} | {seg}")
    print("    cps:", " ".join(f"{ord(ch):04X}" for ch in tx[i:i+len(needle)]))

print("■■■ RASM BYTES CRITIQUES ■■■")
print("46:17 يَسْتَغِيثَانِ :"); hexspan(46, 17, "سْتَغِيثَ")
print("4:176 ٱلثُّلُثَانِ :"); hexspan(4, 176, "ثُّلُثَ")
print("4:11 ثُلُثَا :"); hexspan(4, 11, "ثُلُثَا")
print("73:20 ثُلُثَىِ :"); hexspan(73, 20, "ثُلُثَى")
print("22:30 أَوْثَٰنِ :"); hexspan(22, 30, "أَوْثَ")
print("113:4 نَّفَّٰثَٰتِ :"); hexspan(113, 4, "نَّفَّ")
print("24:26 خَبِيثَٰتُ :"); hexspan(24, 26, "خَبِيثَ")
print("2:27 مِيثَٰقِهِۦ :"); hexspan(2, 27, "مِيثَ")
print("12:91 ءَاثَرَكَ :"); hexspan(12, 91, "ءَاثَ")
print("79:38 ءَاثَرَ :"); hexspan(79, 38, "ءَاثَ")
print("20:104 أَمْثَلُهُمْ :"); hexspan(20, 104, "أَمْثَل")
print("4:11 أُنثَيَيْنِ :"); hexspan(4, 11, "أُنث")
print("4:176 أُنثَيَيْنِ :"); hexspan(4, 176, "أُنث")

print("\n■■■ RACINES EXHAUSTIVES (avec diacritiques entre lettres) ■■■")
def root(a, b, c, label, extra=""):
    """Cherche X ... Y ... Z avec 0-2 diacritiques entre chaque lettre racine."""
    D = "[َُِّْٰٰۭۣٓ۟ۨۖۗۘۚۛۜۢۖ۟۠ۥۦٰ'ʾ]*"
    pat = re.compile(f"{a}{D}{b}{D}{c}{D}{extra}")
    hits = []
    for (sn, an, tx) in corpus:
        for m in pat.finditer(tx):
            st = max(0, m.start()-18); en = min(len(tx), m.end()+18)
            hits.append((sn, an, m.group(0), tx[st:en]))
    print(f"\n=== racine {label} — {len(hits)} occ.")
    for (sn, an, g, ctx) in hits:
        print(f"  {sn}:{an} [{g}] | {ctx}")

# أ-ث-ر : toutes formes (آ أ ء initiales couvertes via a=أ? non — chercher 3 passes)
for init in "اأءآ":
    root(init, "ث", "ر", f"{init}-ث-ر")
# م-ث-ل
root("م", "ث", "ل", "م-ث-ل")
# أ-ن-ث / ا-ن-ث
for init in "اأ":
    root(init, "ن", "ث", f"{init}-ن-ث")
# أ-ث-ب / ا-ث-ب
for init in "اأ":
    root(init, "ث", "ب", f"{init}-ث-ب")
# أ-ث-ث / ا-ث-ث
for init in "اأ":
    root(init, "ث", "ث", f"{init}-ث-ث")

print("\n■■■ LACUNES DE 19759 (comptage des emplacements d'exemples) ■■■")
src = open("/home/z/my-project/tr-tmp/19759.src.html", encoding="utf-8").read()
print("img vides:", src.count("<img"))
print("مِثْلَ:", src.count("مِثْلَ") + src.count("مِثْلِ"))
print("تَعَالَى:", src.count("تَعَالَى"))
print("قَوْلِهِ تَعَالَى:", src.count("قَوْلِهِ تَعَالَى"))
print("وَكَذا:", src.count("وَكَذا") + src.count("وَكَذَا"))
print("الْقِيَاس (règle du qiyās):", src.count("الْقِيَا"))
# Position des trous : afficher chaque occurrence de مثلا/مثل avec 15 car après
for m in re.finditer(r".{0,30}مِثْل[َِ]?[:.]?\s*.{0,25}", src):
    print("  [مثل] …", m.group(0).replace("\n", " ")[:80])
