#!/usr/bin/env python3
"""verify-322.py — vérification arithmétique des 12 corrigés de la leçon 322
(أنشطة الدعم والتثبيت, faraid-tanawi-3, p.201-204).
Chaque fraction en valeurs exactes (Fraction), chaque distribution sommée à 1.
Règles mälikites (Mukhtaṣar Khalīl) : exclusions par degré/force, jadd
(meilleur du sixième / tiers du reliquat / muqāṣama), grand-mères (la proche
maternelle exclut la lointaine paternelle, sinon concours), tante paternelle
= parent allié (exclue par les ʿaṣaba), mushtaraka + radd, aveu (méthode
d'Asbagh du dars 25 : 3 farīḍa + jāmiʿa), legs plafonnés au tiers."""
from fractions import Fraction as F

ok = []
def check(name, total, expected=F(1)):
    good = (total == expected)
    ok.append(good)
    print(f"{'✓' if good else '✗ ÉCHEC'} {name}: somme = {total} (attendu {expected})")

# ─── ACTIVITÉ II ───────────────────────────────────────────────
# q1 : 2 petits-fils prennent tout ; exclus : 2 neveux لأب, 2 cousins germains, grand-père
check("II.1 deux petits-fils", F(1,2) + F(1,2))
# q2 : جدتان (أم الأب + أم أم الأم : concours, sixième partagé) ; 2 sœurs utérines (tiers) ;
#     3 frères لأب (reste) ; exclus : neveu germain + nièce germaine (par les frères لأب)
check("II.2 grand-mères concours + utérines + frères لأب",
      F(1,12) + F(1,12) + F(1,6) + F(1,6) + F(1,6)*3)
# q3 : épouse 1/4 ; أم الأم seule 1/6 (la proche maternelle exclut la lointaine
#     paternelle أم أم الأب) ; 5 utérines 1/3 ; jadd = sixième (meilleur que
#     muqāṣama 1/12 et tiers du reliquat 1/12) ; 2 germains partagent 1/12
check("II.3 épouse+أم الأم+5 utérines+jadd(6e)+2 germains",
      F(1,4) + F(1,6) + F(1,15)*5 + F(1,6) + F(1,24)*2)
# q4 : épouse 1/4 (cousine mais ʿaṣaba dominée par les oncles) ; 3 têtes utérines 1/3 ;
#     2 oncles لأب : reste 5/12 ; tante paternelle germaine EXCLUE (parent allié)
check("II.4 épouse-cousine+utérins+2 oncles (tante exclue)",
      F(1,4) + F(1,9)*3 + F(5,24)*2)
# q5 : 2 épouses 1/8 ; père 1/6 ; (grand-père + 2 utérins exclus par le père) ;
#     3 filles de fils + 2 fils de fils de fils : reste 17/24 en 7 parts (2:1)
check("II.5 2 épouses+père+3 filles de fils+2 arrière-petits-fils",
      F(1,16)*2 + F(1,6) + F(17,168)*3 + F(17,84)*2)
# q6 : épouse 1/4 ; 2 grand-mères directes (sixième partagé) ; MUSHTARAKA : les 2
#     germanes rejoignent les 3 utérins dans le tiers (1/15 chacune) ; reste 1/4 →
#     RADD sur les ayants-farḍ de parenté (facteur 3/2) ; exclus : 5 sœurs لأب,
#     2 nièces, 2 neveux, oncle (par les germanes)
check("II.6 mushtaraka + radd (base 40)",
      F(1,4) + F(1,8)*2 + F(1,10)*5)
#     détail : épouse 10/40 ; chaque grand-mère 5/40 ; chaque tête 4/40
assert F(1,4) == F(10,40) and F(1,8) == F(5,40) and F(1,10) == F(4,40)

# ─── ACTIVITÉ III ──────────────────────────────────────────────
# q1 : 1er décès — mère 1/6, épouse 1/4, frère+soeur germains 2:1 sur 7/12
check("III.1a premier décès (mère+épouse+germains 2:1)",
      F(1,6) + F(1,4) + F(7,18) + F(7,36))
#     2e décès (tarka = 7/18) : épouse 1/8, mère 1/6, fils + 2 filles 2:1 sur 17/24
check("III.1b second décès (sur la tarka du frère)",
      F(1,8) + F(1,6) + F(17,48) + F(17,96)*2)
# q2 : sans le fils : mère 1/6, 4 têtes utérines 1/3 (1/12 chacune), frère لأب 1/2 ;
#     l'aveu d'une sœur : SA part (1/12) passe au fils avoué
check("III.2 aveu d'une cohéritière utérine",
      F(1,6) + F(1,12)*3 + F(1,2) + F(1,12))
# q3 : 60 000 dirhams — mère 1/6 (10 000), père 1/6 SEUL (les farḍ consument
#     tout : pas de reste de taʿṣīb — 10 000), 4 filles 2/3 (10 000 chacune) ;
#     la disparue : 10 000 suspendus
check("III.3 disparue (parts des présents)",
      F(1,6) + F(1,6) + F(1,6)*4)
assert 60000 * F(1,6) == 10000
assert 60000 * F(2,3) / 4 == 10000  # part suspendue de la disparue
#     si décès avéré AVANT sa mère : 3 filles 2/9 (13 333 1/3 chacune)
assert 60000 * F(2,3) / 3 == F(40000, 3)
# q4 : méthode d'Asbagh (dars 25) — 3 farīḍa + jāmiʿa 72 (CORRECTION R451 :
#     la mère de l'enfant prend le TIERS — l'enfant ne laisse ni descendant ni
#     fratrie — et les 3 oncles les deux tiers, 2/9 chacun : mināsakha base 9,
#     non 4 ; déni base 4 (épouse 1, chaque frère 1) ; aveu base 8 (épouse 1,
#     garçon 7) ; nieurs : 18/72 chacun (1/4), admettant : 14/72 (2×7),
#     épouse : 18/72 + 4/72 (résidu de l'admettant) = 22/72
check("III.4 aveu de l'istihlāl (jāmiʿa 72)",
      F(18,72)*2 + F(14,72) + F(22,72))
assert F(18,72) == F(1,4)      # chaque nieur : son quart exact
assert F(14,72) == F(7,36)     # l'avouant : deux neuvièmes portés par sept
assert F(22,72) == F(11,36)    # l'épouse : 18 + le reliquat 4 de l'avouant
#     la version erronée de R450 (base 4, jāmiʿa 32 : 8/8/7/9) posait la mère
#     de l'enfant au quart — fraction illicite ; corrigée au tour R451.
# q5 : legs 1/6 + 1/7 = 13/42 (< 1/3 ✓) ; net 29/42 ;
#     époux 1/2 du net, mère 1/6 du net, frère+soeur لأب 2:1 sur le tiers du net
check("III.5 deux legs (sixième+septième)",
      F(13,42) + F(29,84) + F(29,252) + F(29,378) + F(29,189))
#     vérif : parts du net = 29/42 × (1/2 + 1/6 + 1/3) = 29/42
assert F(29,42) * (F(1,2)+F(1,6)+F(1,3)) == F(29,42)
# q6 : 1er décès — legs 1/4 (> 1/3 : agrément des 3 fils requis ; sinon réduit
#     au tiers) ; avec agrément : net 3/4, chaque fils 1/4
check("III.6a premier décès (legs quart, avec agrément)",
      F(1,4) + F(1,4)*3)
#     2e décès (tarka du fils = 1/4 de la masse) : legs 1/6 (< 1/3 ✓) ;
#     net 5/24 de l'initiale ; ses 3 fils : 5/72 chacun
check("III.6b second décès (legs sixième, en cascade)",
      F(1,24) + F(5,72)*3, expected=F(1,4))  # = la tarka du fils prédécédé (1/4)
assert F(1,4) - F(1,4)*F(1,6) == F(5,24)

print()
print(f"═══ {sum(ok)}/{len(ok)} vérifications passées ═══")
exit(0 if all(ok) else 1)
