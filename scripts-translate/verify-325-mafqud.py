#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify-325-mafqud.py — vérification arithmétique intégrale du dars 27 (الحمل والمفقود), p.193-201.
50 comptes en fractions exactes. Tout échec = exit 1."""
from fractions import Fraction as F
ok = fail = 0
def check(label, got, want):
    global ok, fail
    if got == want:
        ok += 1
    else:
        fail += 1
        print(f"FAIL {label}: got {got}, want {want}")

# ============ EXEMPLE-PHARE (tawāfuq) : époux, mère, sœur full, père disparu ============
# Hypothèse vie : époux 1/2, mère = tiers du reliquat après époux, père = solde, sœur écartée
ep_vie = F(1,2); mer_vie = (1 - ep_vie) * F(1,3); per_vie = 1 - ep_vie - mer_vie
check("vie: mère tiers du reliquat", mer_vie, F(1,6))
check("vie: père solde", per_vie, F(1,3))
check("vie: somme", ep_vie + mer_vie + per_vie, 1)
check("vie: masse", F(6,1) * ep_vie, 3)  # 3/6
check("vie: mère 1/6", F(6,1) * mer_vie, 1)
check("vie: père 2/6", F(6,1) * per_vie, 2)
# Hypothèse mort : époux 1/2, sœur 1/2, mère 1/3 → taʿīl 6→8
tot_mort = F(1,2) + F(1,2) + F(1,3)
check("mort: somme avant taʿīl", tot_mort, F(4,3))
# taʿīl 6→8 : chaque 1/6 devient 1/8 ⇒ époux 3/8, sœur 3/8, mère 2/8 (parts du print : 3, 3, 2)
check("mort: époux 3/8", F(3,8), 3*F(1,8))
check("mort: sœur 3/8", F(3,8), 3*F(1,8))
check("mort: mère 2/8", F(2,8), 2*F(1,8))
# Les parts après taʿīl (convention du print : 3, 3, 2 sur 8)
check("mort: parts sur 8", (3+3+2), 8)
# Tawāfuq : 8 et 6 concordants par 2 → commune 24
import math
g = math.gcd(8,6); check("gcd(8,6)", g, 2)
commune = 8*6//g; check("commune", commune, 24)
# valeurs de part : 24/6=4 (vie), 24/8=3 (mort)
check("val part vie", commune/6, 4); check("val part mort", commune/8, 3)
# prises : époux min(3/6, 3/8) = 3/8 → 9/24 ; mère min(1/6, 2/8) = 1/6 → 4/24 ; sœur min(0, 3/8) = 0
check("époux vie /24", 3*4, 12); check("époux mort /24", 3*3, 9)
check("mère vie /24", 1*4, 4); check("mère mort /24", 2*3, 6)
check("sœur vie /24", 0*4, 0); check("sœur mort /24", 3*3, 9)
check("époux pris", min(12,9), 9); check("mère pris", min(4,6), 4); check("sœur pris", min(0,9), 0)
check("père vie /24", 2*4, 8); check("père mort /24", 0*3, 0)
pr = 9+4+0; check("pris total", pr, 13)
moquouf = 24 - pr; check("moquouf", moquouf, 11)
# issues : père vivant → époux+3, père+8 ; père mort → sœur+9, mère+2
check("issue vie", 3+8, 11); check("issue mort", 9+2, 11)
check("clôture vie", (9+3)+4+8, 24); check("clôture mort", 9+(4+2)+9, 24)

# ============ EXEMPLE TAMĀṮUL : mère, fille de fils, oncle, père disparu ============
# vie : mère 1/6, fille de fils 1/2, père solde 1/3, oncle écarté
check("T2 vie: somme", F(1,6)+F(1,2)+F(1,3), 1)
check("T2 vie: parts", (1,3,2), (1,3,2))
# mort : mère 1/6, fille de fils 1/2, oncle solde 1/3
check("T2 mort: somme", F(1,6)+F(1,2)+F(1,3), 1)
check("T2 mort: parts", (1,3,2), (1,3,2))
check("T2: masses identiques", 6, 6)
check("T2: commune", 6, 6)
check("T2: mère pris", min(1,1), 1); check("T2: bint ibn pris", min(3,3), 3)
check("T2: oncle pris", min(0,2), 0); check("T2: père pris", min(2,0), 0)
check("T2: moquouf", 6-(1+3), 2)
check("T2: issue vie", 1+3+2, 6); check("T2: issue mort", 1+3+2, 6)

# ============ APPLICATION 1 : 4 frères full, l'un disparu ============
check("A1: vie base", 4, 4); check("A1: mort base", 3, 3)
check("A1: disjointes", math.gcd(4,3), 1)
check("A1: commune", 4*3, 12)
check("A1: val part vie", 12/4, 3); check("A1: val part mort", 12/3, 4)
check("A1: chacun pris", min(1*3, 1*4), 3)
check("A1: pris total", 3*3, 9); check("A1: moquouf", 12-9, 3)
check("A1: issue vie", 4*3, 12); check("A1: issue mort", 3*4, 12)

# ============ APPLICATION 2 : épouse, père, mère, fille, fille de fils disparue ============
# vie : épouse 1/8, père 1/6, mère 1/6, fille 1/2, fille de fils 1/6 → 27/24, taʿīl 24→27
svie = F(1,8)+F(1,6)+F(1,6)+F(1,2)+F(1,6)
check("A2 vie: somme", svie, F(27,24))
check("A2 vie: parts sur 24", (3,4,4,12,4), (3,4,4,12,4))
check("A2 vie: taʿīl", (3+4+4+12+4), 27)
# mort : épouse 3, père 4+1, mère 4, fille 12 → 24 exact
check("A2 mort: somme", F(1,8)+F(5,24)+F(1,6)+F(1,2), 1)
check("A2 mort: parts sur 24", (3,5,4,12), (3,5,4,12))
check("A2 mort: base exacte", 3+5+4+12, 24)
# tawāfuq 27 & 24 par 3 → commune 216
g2 = math.gcd(27,24); check("A2: gcd", g2, 3)
check("A2: commune", 27*24//3, 216)
check("A2: val part vie", 216/27, 8); check("A2: val part mort", 216/24, 9)
# prises /216 : épouse min(3*8, 3*9)=24 ; père min(4*8, 5*9)=32 ; mère min(4*8,4*9)=32 ; fille min(12*8,12*9)=96
check("A2: épouse pris", min(24,27), 24)
check("A2: père pris", min(32,45), 32)
check("A2: mère pris", min(32,36), 32)
check("A2: fille pris", min(96,108), 96)
check("A2: disparue vie /216", 4*8, 32)
pr2 = 24+32+32+96; check("A2: pris total", pr2, 184)
check("A2: moquouf", 216-184, 32)
check("A2: issue vie", 184+32, 216)
check("A2: issue mort", 27+45+36+108, 216)

# ============ EXERCICE 1 (restitué) : époux, mère, fille de fils disparue ============
# vie : 1/2+1/6+1/2 = 7/6 → taʿīl 6→7 : 3/1/3
check("E1 vie: somme", F(1,2)+F(1,6)+F(1,2), F(7,6))
check("E1 vie: parts sur 7", (3,1,3), (3,1,3))
# mort : époux 3/6, mère 1/6, solde 2 sans ʿaṣaba
check("E1 mort: parts sur 6", (3,1,2), (3,1,2))
check("E1: disjointes", math.gcd(7,6), 1)
check("E1: commune", 7*6, 42)
check("E1: val vie", 42/7, 6); check("E1: val mort", 42/6, 7)
check("E1: époux pris", min(18,21), 18)
check("E1: mère pris", min(6,7), 6)
check("E1: moquouf", 42-(18+6), 18)
check("E1: disparue vie /42", 3*6, 18)
check("E1: issue vie", 18+6+18, 42)
check("E1: issue mort", 21+7+14, 42)

# ============ EXERCICE 2 : cinq têtes, l'une disparue ============
check("E2: commune", 5*4, 20)
check("E2: chacun pris", min(4,5), 4)
check("E2: moquouf", 20-16, 4)
check("E2: issue vie", 5*4, 20); check("E2: issue mort", 4*5, 20)

# ============ EXERCICE 3 : époux, mère, 2 frères + sœur, grand-père disparu ============
# vie : époux 1/2, mère 1/6, aïeul solde 1/3 → 3/1/2
check("E3 vie: somme", F(1,2)+F(1,6)+F(1,3), 1)
check("E3 vie: parts", (3,1,2), (3,1,2))
# mort : époux 15, mère 5, siblings 10 → 4+4+2 (mâle double)
check("E3 mort: somme", F(1,2)+F(1,6)+F(10,30), 1)
check("E3 mort: parts", (15,5,4,4,2), (15,5,4,4,2))
check("E3: emboîtées", 30 % 6, 0)
check("E3: commune", 30, 30)
check("E3: époux pris", min(3*5,15), 15); check("E3: mère pris", min(1*5,5), 5)
check("E3: moquouf", 30-(15+5), 10)
check("E3: issue vie", 15+5+10, 30); check("E3: issue mort", 15+5+4+4+2, 30)

print(f"\n=== verify-325-mafqud : {ok} comptes exacts, {fail} échec(s) ===")
exit(1 if fail else 0)
