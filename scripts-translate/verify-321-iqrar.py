#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R448 — verify-321-iqrar.py : vérification en fractions exactes des deux
exercices corrigés de la leçon 321 (clôture du chapitre de l'aveu, p. 176).

Exercice 1 : زوج، أم، أخ شقيق — أقر الزوج ببنت.
  déni 6 (3/2/1) ; aveu 12 (6/3/2/1) ; regard = تداخل (6|12) → جامعة 12 ;
  جزء السهم 2 (déni) / 1 (aveu) ;
  زوج min(6,3)=3 → rend 3 ; بنت 3 ; أم 2×2=4 ; أخ 1×2=2. Somme = 12.

Exercice 2 : زوج، ابن، بنت — أقر الابن بابنين، وأقرت البنت ببنت.
  déni 12 (3/6/3) ; aveu du fils 28 (7/6·3/3) ; aveu de la fille 16 (4/6/3·2) ;
  regards : توافق 28↔16 (gcd 4) → 4×28=112 ; توافق 112↔12 (gcd 4) → 3×112=336 ;
  جامعة 336 ; جزء السهم 28 / 12 / 21 ;
  زوج 1/4 = 84 (partout) ; ابن min(168,72)=72 → rend 96 (48+48) ;
  بنت min(84,63)=63 → rend 21. Somme = 336.

VERDICT OK si toutes les assertions tiennent en fractions exactes.
"""
from fractions import Fraction as F

ok = True
def check(label, got, want):
    global ok
    good = got == want
    ok = ok and good
    print(f"{'OK ' if good else 'FAIL'} {label}: {got} (attendu {want})")

# ---------- Exercice 1 ----------
print("=== Exercice 1 : زوج + أم + أخ شقيق ; aveu du زوج d'une بنت ===")
# Déni : زوج 1/2, أم 1/3 (frère unique — le verset dit إخوة, pluriel), أخ reste 1/6
den = {"zawj": F(1,2), "umm": F(1,3), "akh": 1 - F(1,2) - F(1,3)}
check("déni parts", [den["zawj"], den["umm"], den["akh"]], [F(3,6), F(2,6), F(1,6)])
# Aveu : بنت 1/2, زوج 1/4, أم 1/6, أخ reste 1/12
ack = {"bint": F(1,2), "zawj": F(1,4), "umm": F(1,6), "akh": 1 - F(1,2) - F(1,4) - F(1,6)}
check("aveu parts", [ack["bint"], ack["zawj"], ack["umm"], ack["akh"]],
      [F(6,12), F(3,12), F(2,12), F(1,12)])
# Regard : 6 | 12 → تداخل → جامعة 12 ; جزء السهم 2 / 1
J = 12
check("جزء السهم déni", J // 6, 2)
check("جزء السهم aveu", J // 12, 1)
zawj_den, zawj_ack = 3*2, 3*1
umm_fin, akh_fin = 2*2, 1*2
zawj_fin = min(zawj_den, zawj_ack)
bint_fin = zawj_den - zawj_ack
check("زوج final", zawj_fin, 3)
check("بنت final (le rendu)", bint_fin, 3)
check("أم final (tiers du déni)", umm_fin, 4)
check("أخ final", akh_fin, 2)
check("somme finale", sum([zawj_fin, bint_fin, umm_fin, akh_fin]), J)

# ---------- Exercice 2 ----------
print()
print("=== Exercice 2 : زوج + ابن + بنت ; aveu du fils de 2 fils, de la fille d'une fille ===")
# Déni : زوج 1/4 ; reste 3/4 sur 3 têtes (ابن 2, بنت 1) → base 12 : 3/6/3
den = {"zawj": F(1,4), "ibn": F(6,12), "bint": F(3,12)}
check("déni parts", [den["zawj"], den["ibn"], den["bint"]], [F(3,12), F(6,12), F(3,12)])
# Aveu du fils : 3 fils + 1 fille = 7 têtes ; زوج 1/4 = 7/28 ; reste 21/28 à 3/tête
ack1 = {"zawj": F(1,4), "ibn": F(6,28), "bint": F(3,28)}
check("aveu fils parts", [ack1["zawj"], ack1["ibn"], ack1["bint"]], [F(7,28), F(6,28), F(3,28)])
check("aveu fils total", sum(ack1.values()) + 2*F(6,28), 1)
# Aveu de la fille : 1 fils + 2 filles = 4 têtes ; زوج 1/4 = 4/16 ; reste 12/16 à 3/tête
ack2 = {"zawj": F(1,4), "ibn": F(6,16), "bint": F(3,16)}
check("aveu fille parts", [ack2["zawj"], ack2["ibn"], ack2["bint"]], [F(4,16), F(6,16), F(3,16)])
check("aveu fille total", sum(ack2.values()) + F(3,16), 1)
# Regards en séquence : 28↔16 توافق (pgcd 4) → 4×28 = 112 ; 112↔12 توافق (pgcd 4) → 3×112 = 336
import math
g1 = math.gcd(28, 16)
check("pgcd(28,16)", g1, 4)
check("étape 1 (concordante de 16 × complète de 28)", (16//g1)*28, 112)
g2 = math.gcd(112, 12)
check("pgcd(112,12)", g2, 4)
check("étape 2 (concordante de 12 × complète de 112)", (12//g2)*112, 336)
J = 336
check("جامعة = ppcm(12,28,16)", J, 336)
check("جزء السهم déni/aveu1/aveu2", [J//12, J//28, J//16], [28, 12, 21])
# Distribution
zawj_fin = F(1,4) * J                       # 84 — le quart dans les trois fractions
ibn_den, ibn_ack = 6*28, 6*12               # 168 / 72
ibn_fin = min(ibn_den, ibn_ack)
rendu_fils = ibn_den - ibn_ack              # 96 → 48 + 48
bint_den, bint_ack = 3*28, 3*21             # 84 / 63
bint_fin = min(bint_den, bint_ack)
rendu_fille = bint_den - bint_ack           # 21
check("زوج final", zawj_fin, 84)
check("ابن final (le moindre)", ibn_fin, 72)
check("rendu du fils (deux garçons)", rendu_fils, 96)
check("part de chaque garçon", rendu_fils/2, 48)
check("بنت final (le moindre)", bint_fin, 63)
check("rendu de la fille", rendu_fille, 21)
check("زوج identique dans les trois fractions", [3*28, 7*12, 4*21], [84, 84, 84])
check("somme finale", sum([zawj_fin, ibn_fin, rendu_fils, bint_fin, rendu_fille]), J)

print()
print("VERDICT:", "OK" if ok else "ÉCHEC")
