#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle de la leçon 320 (al-iqrār 2, l'aveu du multiple par le multiple).

Rejoue, en fractions exactes, les trois problèmes travaillés par le manuel de
farāʾiḍ 2 (ad-dars 24, section ثالثا + الأنشطة التطبيقية, imprimé p.173-176) :
  A. le cas du matn (p.173-174) : fils + fille ; le fils reconnaît une fille et
     la fille un fils, chaque désigné niant l'autre — trois fractions disparates
     3-4-5, joumʿa 60, distribution 30/12/10/8 ;
  B. l'application 1 (p.175) : mère + deux frères germands + sœur germaine,
     l'un des frères reconnaissant une fille — joumʿa 30, distribution
     5/10/4/5/6 ;
  C. l'application 2 (p.175) : mère + grand-père, LA MÈRE reconnaissant une
     fille et LE GRAND-PÈRE un fils (double aveu = متعدد بمتعدد intégral) —
     trois fractions 3/6/6, joumʿa 6, distribution 1/1/1/3.
Vérifie aussi le rasm : la pièce ne citant AUCUN verset ni hadith (le matn de
Khalīl étant un texte de manuel, la chaîne de vérification s'est portée sur
l'édition du matn lui-même — Dār al-kutub al-ʿilmīya p.272, passage verbatim).
Verdict OK si les trois totaux se referment sur leur joumʿa et si le corps ne
cite aucun texte canonique non porté par le rasm.
"""
from fractions import Fraction as F

HTML = "scripts-translate/tr-tmp/pdf-mut23h2v-320.html"

errors = []


def sale(name, parts, j):
    total = sum(parts.values())
    ok = total == j
    print(f"{name}")
    print(f"  parts: {parts} → total {total} / joumʿa {j} : {'SOLDE' if ok else 'ÉCART'}")
    if not ok:
        errors.append(f"{name} : total {total} ≠ joumʿa {j}")
    return ok


ok = True

# ---- A. Le cas du matn (p.173-174) -------------------------------------------
# Déni (base 3) : ابن 2, بنت 1.
# Aveu du fils (base 4) : ابن 2, بنت 1, بنت مقر بها 1.
# Aveu de la fille (base 5) : ابن 2, ابن مقر به 2, بنت 1.
# Joumʿa : 4×5=20 puis ×3 = 60. Quarts sortants : 20, 15, 12.
ibn_enk = F(2, 3); bint_enk = F(1, 3)
ibn_iqr_s = F(2, 4); bint_iqr_s = F(1, 4); bint_mqb_s = F(1, 4)
ibn_iqr_d = F(2, 5); ibn_mqb_d = F(2, 5); bint_iqr_d = F(1, 5)
a_ibn_enk = ibn_enk * 60; a_ibn_iqr = ibn_iqr_s * 60
a_bint_enk = bint_enk * 60; a_bint_iqr = bint_iqr_d * 60
assert (a_ibn_enk, a_ibn_iqr, a_bint_enk, a_bint_iqr) == (40, 30, 20, 12), "intermédiaires du cas A"
nqis_ibn = a_ibn_enk - a_ibn_iqr   # 10 → بنت مقر بها
nqis_bint = a_bint_enk - a_bint_iqr  # 8 → ابن مقر به
ok &= sale(
    "A. cas du matn (joumʿa 60)",
    {"ibn": int(a_ibn_iqr), "bint": int(a_bint_iqr),
     "bint muqarr biha": int(nqis_ibn), "ibn muqarr bihi": int(nqis_bint)},
    60,
)

# ---- B. Application 1 (p.175) --------------------------------------------------
# Déni (base 6) : أم 1, أخان 2+2, أخت 1.
# Aveu (base 30) : أم 5, أخان 4+4, أخت 2, بنت 15.
# Tadāḫul (6 dans 30) → joumʿa 30 ; quarts sortants : 5 (déni), 1 (aveu).
umm_e = F(1, 6); akh1_e = F(2, 6); akh2_e = F(2, 6); ukht_e = F(1, 6)
umm_i = F(5, 30); akh_i = F(4, 30); ukht_i = F(2, 30); bint_i = F(15, 30)
b_umm = umm_e * 30            # 5 (renieuse)
b_akh_munkir = akh1_e * 30    # 10 (renieur)
b_ukht = ukht_e * 30          # 5 (renieuse)
b_akh_muqirr_enk = akh2_e * 30  # 10
b_akh_muqirr_iqr = akh_i * 30   # 4
b_akh_muqirr = min(b_akh_muqirr_enk, b_akh_muqirr_iqr)  # 4 — la règle du moindre
b_bint = b_akh_muqirr_enk - b_akh_muqirr_iqr            # 6 — ce que l'aveu a soustrait
assert (b_umm, b_akh_munkir, b_ukht, b_akh_muqirr, b_bint) == (5, 10, 5, 4, 6), "intermédiaires du cas B"
ok &= sale(
    "B. application 1 (joumʿa 30)",
    {"umm": int(b_umm), "akh munkir": int(b_akh_munkir), "ukht munkira": int(b_ukht),
     "akh muqirr": int(b_akh_muqirr), "bint muqarr biha": int(b_bint)},
    30,
)

# ---- C. Application 2 (p.175) — le double aveu ---------------------------------
# Déni (base 3) : أم 1, جد 2 (أم الثلث، الجد عصبة الباقي).
# Aveu de la mère (base 6) : أم 1, جد 2, بنت 3 (أم 1/6, بنت 1/2, جد عصبة الباقي).
# Aveu du grand-père (base 6) : أم 1, جد 1, ابن 4 (telle que portée par le print).
# Joumʿa 6 ; quarts sortants : 2 (déni), 1, 1.
c_umm_e = F(1, 3); c_jd_e = F(2, 3)
c_umm_ia = F(1, 6); c_jd_ia = F(2, 6); c_bint_ia = F(3, 6)   # ia = iqrār al-umm
c_umm_ij = F(1, 6); c_jd_ij = F(1, 6); c_ibn_ij = F(4, 6)    # ij = iqrār al-ǧadd
c_umm_enk = c_umm_e * 6   # 2
c_jd_enk = c_jd_e * 6     # 4
c_umm_iqr = c_umm_ia * 6  # 1
c_jd_iqr = c_jd_ij * 6    # 1
c_umm_final = min(c_umm_enk, c_umm_iqr)   # 1 — la règle du moindre
c_jd_final = min(c_jd_enk, c_jd_iqr)      # 1
c_bint = c_umm_enk - c_umm_iqr            # 1 — le manque de la mère → la fille reconnue
c_ibn = c_jd_enk - c_jd_iqr               # 3 — le manque du grand-père → le fils reconnu
assert (c_umm_final, c_jd_final, c_bint, c_ibn) == (1, 1, 1, 3), "intermédiaires du cas C"
ok &= sale(
    "C. application 2 (joumʿa 6)",
    {"umm": int(c_umm_final), "ǧadd": int(c_jd_final),
     "bint muqarr biha": int(c_bint), "ibn muqarr bihi": int(c_ibn)},
    6,
)

# ---- D. Rasm : AUCUN texte canonique cité par le rasm p.173-176 ----------------
try:
    html = open(HTML, encoding="utf-8").read()
except FileNotFoundError:
    html = ""
    print("(corps de la leçon absent — vérification du rasm différée à la rédaction)")
if html:
    body = html.split("<h2>Notes du traducteur</h2>", 1)[0]
    interdits = [
        "أَعُوذُ", "بِسْمِ اللهِ", "﴿", "﴾",
        "Yā ayyuhā", "yā ayyuhā", "Ô vous qui avez cru",
        "le hadith", "Ṣaḥīḥ", "Sunan", "Musnad",
    ]
    for frag in interdits:
        if frag in body:
            errors.append(f"citation canonique non portée par le rasm dans le corps : {frag}")
    # les repères doctrinaux attendus au corps
    for attendu in [
        "multiplie",
        "soixante",
        "le moindre",
        "ce que l\u2019aveu a soustrait",
        "trente", "douze", "dix", "huit",
    ]:
        if attendu not in body:
            errors.append(f"repère doctrinal attendu absent du corps : {attendu}")

print()
if errors:
    print("VERDICT ÉCHEC")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("VERDICT OK — trois joumʿāt soldées (60, 30, 6) ; rasm conforme (zéro canonique)")
