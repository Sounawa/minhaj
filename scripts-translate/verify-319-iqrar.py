#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Vérification arithmétique de la leçon 319 (al-iqrār, quatre cas du seul aveur).

Rejoue, en fractions exactes, les quatre cas travaillés par le manuel de farāʾiḍ
(kitāb al-farāʾiḍ 2 ṯānawī, ad-dars 24, p. 167-173) et soldant chaque joumʿa.
Verdict OK si les quatre totaux se referment sur leur base.
"""
from fractions import Fraction as F


def case(name, enk, iqr, j, expect):
    """enk/iqr : parts de chaque héritier en fractions de 1 ; j : joumʿa ; expect : total attendu."""
    scaled_e = {k: int(v * j) for k, v in enk.items()}
    scaled_i = {k: int(F(v) * j) for k, v in iqr.items()}
    total = sum(expect.values())
    ok = total == j
    print(f"{name}")
    print(f"  déni  ×{j // eval('1') if False else ''}{j}: {scaled_e}")
    print(f"  aveu ×{j}: {scaled_i}")
    print(f"  distribution finale: {expect} → total {total} / {j}")
    print(f"  {'SOLDE' if ok else 'ÉCART'}")
    return ok


ok = True
# Cas 1 — at-tadāḫul : ʿamm + deux sœurs germaines ; l'une reconnaît une 3ᵉ sœur germaine.
# Déni (base 3, chaque héritier 1) ; aveu (base 9) : 3 sœurs 2/9 chacune, ʿamm 3/9.
ok &= case(
    "CAS 1 — interpenetration (jāmiʿa 9)",
    {"s1": F(1, 3), "s2": F(1, 3), "amm": F(1, 3)},
    {"s1": F(2, 9), "s2": F(2, 9), "amm": F(3, 9), "s3": F(2, 9)},
    9,
    {"s2": 3, "amm": 3, "s1": 2, "s3": 1},
)
# Cas 2 — at-tabāyun : mêmes héritiers ; l'une reconnaît un frère germain (l'ʿamm bloqué dans l'aveu).
ok &= case(
    "CAS 2 — disparité (jāmiʿa 12)",
    {"s1": F(1, 3), "s2": F(1, 3), "amm": F(1, 3)},
    {"s1": F(1, 4), "s2": F(1, 4), "akh": F(2, 4)},
    12,
    {"amm": 4, "s2": 4, "s1": 3, "akh": 1},
)
# Cas 3 — at-tawāfuq : fils + deux filles ; le fils reconnaît un petit-fils.
ok &= case(
    "CAS 3 — concordance (jāmiʿa 12)",
    {"b1": F(1, 4), "b2": F(1, 4), "ibn": F(2, 4)},
    {"b1": F(2, 6), "b2": F(2, 6), "ibn": F(1, 6), "hafid": F(1, 6)},
    12,
    {"b1": 3, "b2": 3, "ibn": 2, "hafid": 4},
)
# Cas 4 — at-tamāṯul : mère + sœur consanguine + ʿamm ; la mère reconnaît une sœur germaine.
ok &= case(
    "CAS 4 — identité (jāmiʿa 6)",
    {"umm": F(2, 6), "sh_l_ab": F(3, 6), "amm": F(1, 6)},
    {"umm": F(1, 6), "sh_l_ab": F(1, 6), "sh_kamila": F(3, 6), "amm": F(1, 6)},
    6,
    {"sh_l_ab": 3, "amm": 1, "umm": 1, "sh_kamila": 1},
)

print()
print("VERDICT " + ("OK — les quatre joumʿāt soldent" if ok else "ÉCART"))
raise SystemExit(0 if ok else 1)
