#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify-324-wasaya.py — vérification arithmétique du dars 26 (al-waṣāyā)
pour la leçon 324 (faraid-tanawi-3, pdf-mut23h2v-324).

La méthode du manuel (p. 186-190) :
  UN legs commun (جزء شائع واحد) :
    1. Dresser la fariḍa des héritiers SANS le legs (colonne 1).
    2. Le dénominateur du legs (makhraj) : au légataire sa part, le RESTE aux héritiers.
    3. Si le reste se divise sur les parts des héritiers : clair (jāmiʿa = makhraj).
    4. Sinon, deux regards entre le reste et la base des héritiers :
       - tawāfuq : jāmiʿa = wafq(base) × makhraj ; légataire part × wafq(base),
         héritiers parts × wafq(reste).
       - tabāyun : jāmiʿa = base × makhraj ; légataire part × base,
         héritiers parts × reste.
  DEUX legs communs (جزأين شائعين) :
    1. Fariḍa des héritiers.
    2. Entre les deux dénominateurs : tabāyun → produit plein ; tawāfuq →
       wafq × plein = aṣl al-waṣiyya.
    3. Les deux parts du legs sortent de l'aṣl ; le reste se divise sur les
       héritiers — sinon les deux regards comme ci-dessus (contre l'aṣl).

Cas vérifiés (fractions exactes) :
  E1 : 2 fils + tiers (matn, cas clair)        — jāmiʿa 3
  E2 : 4 fils + tiers (tawāfuq, matn)          — jāmiʿa 6
  E3 : 3 fils + tiers (tabāyun, matn)          — jāmiʿa 9
  E4 : 4 fils + sixième + septième (print)     — jāmiʿa 168 : 29×4, 28, 24
  E5 : 6 fils + sixième + douzième (print)     — jāmiʿa 24 : 3×6, 4, 2
  A1 : époux + 2 filles + frère + cinquième    — jāmiʿa 15 : 3, 4, 4, 1, 3
  A2 : 3 fils + sixième + douzième             — jāmiʿa 12 : 3×3, 2, 1
  T1 : épouse + frère pour père + 9e + 8e      — jāmiʿa 144 : 55, 55, 16, 18
  T2 : époux + père + mère + 8e + 7e           — jāmiʿa 336 : 123, 82, 41, 42, 48
  T3 : fille + épouse + oncle + tiers à trois  — jāmiʿa 36 : 12, 3, 9, 4×3
"""
from fractions import Fraction as F
from math import gcd

ok = fail = 0

def check(name, got, expected):
    global ok, fail
    if got == expected:
        ok += 1
        print(f"  ✓ {name}: {got}")
    else:
        fail += 1
        print(f"  ✗ {name}: {got} ≠ attendu {expected}")

def wafq(a, b):
    """Le conforme (wafq) : le facteur commun ôté (a / pgcd)."""
    return a // gcd(a, b)

print("=== E1 : deux fils, legs du tiers (le cas clair du matn) ===")
# fariḍa : 2 fils, base 2 (1, 1) ; makhraj 3 : légataire 1, reste 2
check("E1.reste se divise", F(2, 3) / 2, F(1, 3))          # chaque fils 1/3
check("E1.jāmiʿa", 3, 3)
check("E1.somme", F(1, 3) + 2 * F(1, 3), F(1))

print("=== E2 : quatre fils, legs du tiers (tawāfuq — l'exemple du print p.187) ===")
# fariḍa : 4 fils, base 4 ; makhraj 3 : légataire 1, reste 2 ; gcd(2,4)=2 → tawāfuq
check("E2.wafq base", wafq(4, 2), 2)
check("E2.wafq reste", wafq(2, 4), 1)
check("E2.jāmiʿa", 2 * 3, 6)
check("E2.légataire", 1 * 2, 2)                              # 2/6 = 1/3
check("E2.fils", 1 * 1, 1)                                  # 1/6 chacun
check("E2.somme", F(2, 6) + 4 * F(1, 6), F(1))
check("E2.net fils", F(1, 6) / F(4, 6), F(1, 4))            # chaque fils 1/4 du net

print("=== E3 : trois fils, legs du tiers (tabāyun — l'exemple du print p.188) ===")
# fariḍa : 3 fils, base 3 ; makhraj 3 : légataire 1, reste 2 ; gcd(2,3)=1 → tabāyun
check("E3.tabāyun", gcd(2, 3), 1)
check("E3.jāmiʿa", 3 * 3, 9)
check("E3.légataire", 1 * 3, 3)                              # 3/9 = 1/3
check("E3.fils", 1 * 2, 2)                                  # 2/9 chacun
check("E3.somme", F(3, 9) + 3 * F(2, 9), F(1))

print("=== E4 : quatre fils, sixième + septième (l'exemple du print p.189) ===")
# aṣl al-waṣiyya : 6×7 = 42 (tabāyun) ; sixième 7, septième 6, total 13, reste 29
check("E4.aṣl", 6 * 7, 42)
check("E4.parts", (7, 6, 42 - 13), (7, 6, 29))
# reste 29 vs base 4 : gcd = 1 → tabāyun → jāmiʿa = 42 × 4 = 168
check("E4.tabāyun", gcd(29, 4), 1)
check("E4.jāmiʿa", 42 * 4, 168)
check("E4.sixième", 7 * 4, 28)
check("E4.septième", 6 * 4, 24)
check("E4.fils", 1 * 29, 29)
check("E4.somme", F(28, 168) + F(24, 168) + 4 * F(29, 168), F(1))
check("E4.sixième exact", F(28, 168), F(1, 6))
check("E4.septième exact", F(24, 168), F(1, 7))
check("E4.net", F(29 * 4, 168), F(29, 42))

print("=== E5 : six fils, sixième + douzième (le cas tawāfuq du print p.189-190) ===")
# dénominateurs 6 et 12 : gcd = 6 → tawāfuq : wafq(6)=1 × 12 = 12 = aṣl
check("E5.tawāfuq", gcd(6, 12), 6)
check("E5.aṣl", wafq(6, 12) * 12, 12)
check("E5.parts", (2, 1, 12 - 3), (2, 1, 9))
# reste 9 vs base 6 : gcd = 3 → tawāfuq : jāmiʿa = wafq(6) × 12 = 2 × 12 = 24
check("E5.wafq base", wafq(6, 9), 2)
check("E5.wafq reste", wafq(9, 6), 3)
check("E5.jāmiʿa", 2 * 12, 24)
check("E5.sixième", 2 * 2, 4)
check("E5.douzième", 1 * 2, 2)
check("E5.fils", 1 * 3, 3)
check("E5.somme", F(4, 24) + F(2, 24) + 6 * F(3, 24), F(1))
check("E5.sixième exact", F(4, 24), F(1, 6))
check("E5.douzième exact", F(2, 24), F(1, 12))
check("E5.net", F(18, 24), F(3, 4))

print("=== A1 : époux + 2 filles + frère germain, legs du cinquième (application p.191) ===")
# fariḍa : époux 1/4 (descendance), 2 filles 2/3, frère le reste 1/12 ; base 12 (3, 4, 4, 1)
check("A1.fariḍa", F(1, 4) + F(2, 3) + F(1, 12), F(1))
# makhraj 5 : légataire 1, reste 4 ; reste 4 vs base 12 : gcd = 4 → tawāfuq
check("A1.tawāfuq", gcd(4, 12), 4)
check("A1.wafq base", wafq(12, 4), 3)
check("A1.wafq reste", wafq(4, 12), 1)
check("A1.jāmiʿa", 3 * 5, 15)
check("A1.légataire", 1 * 3, 3)                              # 3/15 = 1/5
check("A1.époux", 3 * 1, 3)                                  # 3/15
check("A1.fille", 4 * 1, 4)                                  # 4/15 chacune
check("A1.frère", 1 * 1, 1)                                  # 1/15
check("A1.somme", F(3, 15) + F(3, 15) + 2 * F(4, 15) + F(1, 15), F(1))
check("A1.net époux", F(3, 15) / F(12, 15), F(1, 4))
check("A1.net filles", 2 * F(4, 15) / F(12, 15), F(2, 3))
check("A1.net frère", F(1, 15) / F(12, 15), F(1, 12))

print("=== A2 : trois fils, sixième + douzième (application p.191) ===")
# aṣl 12 (tawāfuq 6/12) ; sixième 2, douzième 1, reste 9 ; 9 se divise sur 3 têtes : clair
check("A2.aṣl", wafq(6, 12) * 12, 12)
check("A2.reste se divise", F(9, 12) / 3, F(1, 4))
check("A2.jāmiʿa", 12, 12)
check("A2.somme", 3 * F(3, 12) + F(2, 12) + F(1, 12), F(1))
check("A2.sixième exact", F(2, 12), F(1, 6))
check("A2.douzième exact", F(1, 12), F(1, 12))
check("A2.net", F(9, 12), F(3, 4))

print("=== T1 : épouse + frère pour père, legs du neuvième + du huitième (tamrīn 1) ===")
# fariḍa : épouse 1/2 (pas de descendance), frère pour père le reste 1/2 ; base 2 (1, 1)
check("T1.fariḍa", F(1, 2) + F(1, 2), F(1))
# aṣl : 9×8 = 72 (tabāyun) ; neuvième 8, huitième 9, total 17, reste 55
check("T1.aṣl", 9 * 8, 72)
check("T1.reste", 72 - 17, 55)
# reste 55 vs base 2 : gcd = 1 → tabāyun → jāmiʿa = 72 × 2 = 144
check("T1.jāmiʿa", 72 * 2, 144)
check("T1.neuvième", 8 * 2, 16)
check("T1.huitième", 9 * 2, 18)
check("T1.épouse", 1 * 55, 55)
check("T1.frère", 1 * 55, 55)
check("T1.somme", F(16, 144) + F(18, 144) + 2 * F(55, 144), F(1))
check("T1.neuvième exact", F(16, 144), F(1, 9))
check("T1.huitième exact", F(18, 144), F(1, 8))
check("T1.sous le tiers", F(1, 9) + F(1, 8) < F(1, 3), True)
check("T1.net épouse", F(55, 144) / F(55, 72), F(1, 2))

print("=== T2 : époux + père + mère, legs du huitième + du septième (tamrīn 2) ===")
# fariḍa : époux 1/2, mère 1/6, père 1/6 + reste 1/6 en agnat = 1/3 ; base 6 (3, 2, 1)
check("T2.fariḍa", F(1, 2) + F(1, 3) + F(1, 6), F(1))
# aṣl : 8×7 = 56 (tabāyun) ; huitième 7, septième 8, total 15, reste 41
check("T2.aṣl", 8 * 7, 56)
check("T2.reste", 56 - 15, 41)
# reste 41 vs base 6 : gcd = 1 → tabāyun → jāmiʿa = 56 × 6 = 336
check("T2.jāmiʿa", 56 * 6, 336)
check("T2.huitième", 7 * 6, 42)
check("T2.septième", 8 * 6, 48)
check("T2.époux", 3 * 41, 123)
check("T2.père", 2 * 41, 82)
check("T2.mère", 1 * 41, 41)
check("T2.somme", F(42, 336) + F(48, 336) + F(123, 336) + F(82, 336) + F(41, 336), F(1))
check("T2.huitième exact", F(42, 336), F(1, 8))
check("T2.septième exact", F(48, 336), F(1, 7))
check("T2.sous le tiers", F(1, 8) + F(1, 7) < F(1, 3), True)
check("T2.net", F(41, 56), F(41, 56))

print("=== T3 : fille + épouse + oncle, le tiers à trois légataires égaux (tamrīn 3) ===")
# fariḍa : fille 1/2, épouse 1/8, oncle le reste 3/8 ; base 8 (4, 1, 3)
check("T3.fariḍa", F(1, 2) + F(1, 8) + F(3, 8), F(1))
# le tiers à 3 têtes : makhraj 3, portion 1, mais 3 têtes sur 1 → منكسرة : base 9 (1×3), reste 6
check("T3.têtes", F(1, 3) / 3, F(1, 9))
# reste 6 vs base 8 : gcd = 2 → tawāfuq : wafq(8)=4, wafq(6)=3 ; jāmiʿa = 4 × 9 = 36
check("T3.tawāfuq", gcd(6, 8), 2)
check("T3.jāmiʿa", wafq(8, 6) * 9, 36)
check("T3.légataire", 1 * 4, 4)                              # 4/36 = 1/9 chacun
check("T3.fille", 4 * 3, 12)                                 # 12/36
check("T3.épouse", 1 * 3, 3)                                 # 3/36
check("T3.oncle", 3 * 3, 9)                                  # 9/36
check("T3.somme", 3 * F(4, 36) + F(12, 36) + F(3, 36) + F(9, 36), F(1))
check("T3.tiers exact", 3 * F(4, 36), F(1, 3))
check("T3.net fille", F(12, 36) / F(24, 36), F(1, 2))
check("T3.net épouse", F(3, 36) / F(24, 36), F(1, 8))
check("T3.net oncle", F(9, 36) / F(24, 36), F(3, 8))

print()
print(f"VERDICT : {ok} comptes exacts, {fail} échecs")
exit(1 if fail else 0)
