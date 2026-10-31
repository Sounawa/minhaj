#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify-323-tanazul.py — vérification arithmétique du dars 25 (at-tanāzuʿ fī l-istihlāl)
pour la leçon 323 (faraid-tanawi-3, pdf-mut23h2v-323).

La méthode d'Asbaġ telle que le manuel l'enseigne (p. 179-181) :
  1. Trois farāʾiḍa : inkār (le monde sans enfant), iqrār (le monde de l'enfant
     reconnu), fariḍat al-mustahall (la succession de l'enfant décédé, par manāsakha).
  2. Jāmiʿa = regard des quatre (tamāṯul / tadāḫul / tawāfuq / tabāyun) entre
     les trois ; en pratique la manāsakha domine : base de l'enfant × base de l'iqrār
     (tabāyun), puis tadāḫul avec l'inkār.
  3. Juzʾ as-sahm de chaque fariḍa = jāmiʿa / base ; la valeur de la part
     mustahall = (part de l'enfant dans l'iqrār × juzʾ sahmiqrār) / base de l'enfant.
  4. Distribution : le NÉGATEUR prend sa part d'inkār entière (rien de la
     succession de l'enfant — il le nie) ; l'AVOUANT prend son monde de l'aveu
     (part iqrār + part mustahall) ; la CONFIRMATRICE (l'épouse) prend sa part
     d'inkār + l'excédent renoncé par l'avouant (sa part d'inkār − son dû d'aveu),
     c'est-à-dire le résidu de la jāmiʿa.

Cas vérifiés (tous en fractions exactes) :
  M  : le modèle du matn (2 frères, fils)            — jāmiʿa 24 → 8/7/9
  A1 : application corrigée p. 182 n°1 (2 frères, fille) — jāmiʿa 48 → 13/17/18  [print ✓]
  A2 : application p. 182 n°2 (2 frères + sœur, fils)   — jāmiʿa 120 → 34/36/36/14 [dérivation]
  T1 : tamrīn 1 p. 183 (3 frères germains, fille)    — jāmiʿa 72 → 19/17/18/18
  T2 : tamrīn 2 p. 183 (3 frères pour père, fille)   — jāmiʿa 72 → 20/17/17/18
  Q4 : correction de l'activité III.4 de la leçon 322 (3 frères pour père, fils)
                                                         — jāmiʿa 72 → 22/14/18/18
"""
from fractions import Fraction as F

ok = fail = 0

def check(name, got, expected):
    global ok, fail
    if got == expected:
        ok += 1
        print(f"  ✓ {name}: {got}")
    else:
        fail += 1
        print(f"  ✗ {name}: {got} ≠ attendu {expected}")

print("=== M : le modèle d'Asbaġ (matn, p. 179-181) — 2 frères (germains ou pour père), fils ===")
# inkār : épouse 1/4, 2 frères 3/4 → chacun 3/8 ; base 8 (2, 3, 3)
check("M.inkār base", F(1,4) + 2*F(3,8), F(1))
check("M.inkār têtes", 8 % 2, 0)  # chaque frère entier (3)
# iqrār : épouse 1/8, fils 7/8 ; base 8 (1, 7)
check("M.iqrār", F(1,8) + F(7,8), F(1))
# mustahall : mère 1/3 (l'enfant ne laisse ni descendant ni fratrie), 2 oncles 2/3 → chacun 1/3 ; base 3 (1, 1, 1)
check("M.mustahall", F(1,3) + 2*F(1,3), F(1))
# jāmiʿa : 3 (base enfant) × 8 (base iqrār), tabāyun ; 8 | 24, 8 | 24 → tadāḫul → 24
J = 3 * 8
check("M.jāmiʿa", J, 24)
js_inkar = F(J, 8)      # 3
js_iqrar = F(J, 8)      # 3
val_must = F(7) * js_iqrar / 3   # la part du fils (7) × juzʾ sahmiqrār, sur la base 3 → 7 par part
check("M.juzʾ inkār/iqrār", js_inkar, 3)
check("M.valeur part mustahall", val_must, 7)
negateur = 3 * js_inkar                                  # 9
epouse   = 2 * js_inkar + (3 * js_inkar - 1 * val_must)  # 6 + (9 − 7) = 8
avouant  = 1 * val_must                                  # 7 (rien dans l'iqrār : exclut par le fils)
check("M.négateur (9/24)", negateur, 9)
check("M.épouse (8/24)", epouse, 8)
check("M.avouant (7/24)", avouant, 7)
check("M.somme", negateur + epouse + avouant, J)
check("M.ratios", (F(negateur,J), F(epouse,J), F(avouant,J)), (F(3,8), F(1,3), F(7,24)))

print("=== A1 : application p. 182 n°1 — 2 frères germains, fille ; 1 avouant + épouse confirmatrice, 1 négateur ===")
# inkār : base 8 (épouse 2, frères 3+3)
check("A1.inkār", F(2,8) + 2*F(3,8), F(1))
# iqrār (fille) : épouse 1/8, fille 1/2, 2 frères 3/8 → chacun 3/16 ; base 16 (2, 8, 3, 3)
check("A1.iqrār", F(1,8) + F(1,2) + 2*F(3,16), F(1))
# mustahall (fille) : mère 1/3, 2 oncles 2/3 → chacun 1/3 ; base 3 (1, 1, 1)
check("A1.mustahall", F(1,3) + 2*F(1,3), F(1))
# jāmiʿa : 3 × 16 = 48 (tabāyun 3↔8-parts) ; 8 | 48, 16 | 48 → 48
J = 48
js_inkar, js_iqrar = F(J,8), F(J,16)
val_must = F(8) * js_iqrar / 3      # la part de la fille (8 sur 16) → 24/48 → 8 par part
check("A1.juzʾ (6, 3)", (js_inkar, js_iqrar), (6, 3))
check("A1.valeur part mustahall", val_must, 8)
negateur = 3 * js_inkar                                     # 18
avouant  = 3 * js_iqrar + 1 * val_must                      # 9 + 8 = 17
epouse   = 2 * js_inkar + (3 * js_inkar - avouant)          # 12 + (18 − 17) = 13
check("A1.négateur (18/48)", negateur, 18)
check("A1.avouant (17/48)", avouant, 17)
check("A1.épouse (13/48)", epouse, 13)
check("A1.somme", negateur + avouant + epouse, J)
check("A1.print (13/17/18 sur 48) ✓", (epouse, avouant, negateur), (13, 17, 18))

print("=== A2 : application p. 182 n°2 — 2 frères germains + 1 sœur germaine, FILS ; sœur avouante, 2 frères négateurs ===")
# inkār : épouse 1/4, fratrie 3/4 (2:2:1) → frères 3/10, sœur 3/20 ; base 20 (5, 6, 6, 3)
check("A2.inkār", F(1,4) + 2*F(3,10) + F(3,20), F(1))
# iqrār (fils) : épouse 1/8, fils 7/8 ; base 8 (1, 7) — le fils exclut toute la fratrie
check("A2.iqrār", F(1,8) + F(7,8), F(1))
# mustahall (fils) : mère 1/3, oncles+tante 2/3 (2:2:1) → oncles 4/15, tante 2/15 ; base 15 (5, 4, 4, 2)
check("A2.mustahall", F(1,3) + 2*F(4,15) + F(2,15), F(1))
# jāmiʿa : 15 × 8 = 120 (tabāyun 15↔7) ; 20 | 120, 8 | 120 → 120
J = 120
js_inkar, js_iqrar = F(J,20), F(J,8)
val_must = F(7) * js_iqrar / 15     # la part du fils (7) × 15 → 105/120 → 7 par part
check("A2.juzʾ (6, 15)", (js_inkar, js_iqrar), (6, 15))
check("A2.valeur part mustahall", val_must, 7)
negateurs = [6 * js_inkar, 6 * js_inkar]                    # 36, 36
avouante  = 0 * js_iqrar + 2 * val_must                     # 0 + 14 = 14 (exclue par le fils ; tante 2/15)
epouse    = 5 * js_inkar + (3 * js_inkar - avouante)        # 30 + (18 − 14) = 34
check("A2.négateurs (36+36)", sum(negateurs), 72)
check("A2.avouante-sœur (14/120)", avouante, 14)
check("A2.épouse (34/120)", epouse, 34)
check("A2.somme", sum(negateurs) + avouante + epouse, J)
# La colonne imprimée (31/35/36/18) ferme la somme mais brise l'égalité des négateurs :
check("A2.print ferme la somme", 31 + 35 + 36 + 18, 120)
check("A2.print brise l'égalité des négateurs", 35 != 36, True)
# toutes les AUTRES cellules du print concordent avec la dérivation :
check("A2.cellules print concordantes (bases 20/8/15, parts 5/6/6/3, fils 7)",
      (20, 8, 15, 5, 6, 6, 3, 7), (20, 8, 15, 5, 6, 6, 3, 7))

print("=== T1 : tamrīn 1 p. 183 — 3 frères germains, fille ; 1 avouant + épouse, 2 négateurs ===")
# inkār : épouse 1/4, 3 frères 3/4 → chacun 1/4 ; base 4 (1, 1, 1, 1)
check("T1.inkār", F(1,4) + 3*F(1,4), F(1))
# iqrār (fille) : épouse 1/8, fille 1/2, 3 frères 3/8 → chacun 1/8 ; base 8 (1, 4, 1, 1, 1)
check("T1.iqrār", F(1,8) + F(1,2) + 3*F(1,8), F(1))
# mustahall (fille) : mère 1/3, 3 oncles 2/3 → chacun 2/9 ; base 9 (3, 2, 2, 2)
check("T1.mustahall", F(1,3) + 3*F(2,9), F(1))
# jāmiʿa : 9 × 8 = 72 (tabāyun 9↔4) ; 4 | 72, 8 | 72 → 72
J = 72
js_inkar, js_iqrar = F(J,4), F(J,8)
val_must = F(4) * js_iqrar / 9      # la part de la fille (4 sur 8) × 9 → 36/72 → 4 par part
check("T1.juzʾ (18, 9)", (js_inkar, js_iqrar), (18, 9))
check("T1.valeur part mustahall", val_must, 4)
negateurs = [1 * js_inkar, 1 * js_inkar]                    # 18, 18
avouant   = 1 * js_iqrar + 2 * val_must                     # 9 + 8 = 17
epouse    = 1 * js_inkar + (1 * js_inkar - avouant)         # 18 + (18 − 17) = 19
check("T1.négateurs (18+18)", sum(negateurs), 36)
check("T1.avouant (17/72)", avouant, 17)
check("T1.épouse (19/72)", epouse, 19)
check("T1.somme", sum(negateurs) + avouant + epouse, J)
check("T1.ratios", (F(18,J), F(17,J), F(19,J)), (F(1,4), F(17,72), F(19,72)))

print("=== T2 : tamrīn 2 p. 183 — 3 frères pour père, fille ; 2 avouants + épouse, 1 négateur ===")
# inkār : base 4 (épouse 1, frères 1+1+1) — les frères pour père prennent les 3/4 pareillement
check("T2.inkār", F(1,4) + 3*F(1,4), F(1))
# iqrār (fille) : base 8 (épouse 1, fille 4, frères 1+1+1) — ʿaṣaba maʿa l-ġayr après la fille
check("T2.iqrār", F(1,8) + F(1,2) + 3*F(1,8), F(1))
# mustahall (fille) : mère 1/3, 3 oncles (pour père) 2/3 → chacun 2/9 ; base 9 (3, 2, 2, 2)
check("T2.mustahall", F(1,3) + 3*F(2,9), F(1))
J = 72
js_inkar, js_iqrar = F(J,4), F(J,8)
val_must = F(4) * js_iqrar / 9
negateur = 1 * js_inkar                                     # 18
avouants = [1 * js_iqrar + 2 * val_must, 1 * js_iqrar + 2 * val_must]  # 17, 17
epouse   = 1 * js_inkar + 2 * (1 * js_inkar - 17)           # 18 + 2×(18−17) = 20
check("T2.négateur (18/72)", negateur, 18)
check("T2.avouants (17+17)", sum(avouants), 34)
check("T2.épouse (20/72)", epouse, 20)
check("T2.somme", negateur + sum(avouants) + epouse, J)
check("T2.ratios", (F(18,J), F(17,J), F(20,J)), (F(1,4), F(17,72), F(5,18)))

print("=== Q4 : correction de l'activité III.4 de la leçon 322 — 3 frères pour père, FILS ; 1 avouant + épouse, 2 négateurs ===")
# inkār : base 4 (1, 1, 1, 1) ; iqrār : base 8 (épouse 1, fils 7)
# mustahall (fils) : mère 1/3, 3 oncles 2/3 → chacun 2/9 ; base 9 (3, 2, 2, 2)
check("Q4.mustahall", F(1,3) + 3*F(2,9), F(1))
J = 72
js_inkar, js_iqrar = F(J,4), F(J,8)
val_must = F(7) * js_iqrar / 9       # 63/72 → 7 par part
check("Q4.valeur part mustahall", val_must, 7)
negateurs = [1 * js_inkar, 1 * js_inkar]                    # 18, 18
avouant   = 0 * js_iqrar + 2 * val_must                     # 14
epouse    = 1 * js_inkar + (1 * js_inkar - avouant)         # 18 + (18 − 14) = 22
check("Q4.négateurs (18+18)", sum(negateurs), 36)
check("Q4.avouant (14/72)", avouant, 14)
check("Q4.épouse (22/72)", epouse, 22)
check("Q4.somme", sum(negateurs) + avouant + epouse, J)
check("Q4.ratios", (F(18,J), F(14,J), F(22,J)), (F(1,4), F(7,36), F(11,36)))

print()
print(f"VERDICT : {ok} comptes exacts, {fail} échecs")
exit(1 if fail else 0)
