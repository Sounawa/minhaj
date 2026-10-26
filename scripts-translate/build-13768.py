#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Concatène les 7 fragments de 13768 en tr-tmp/13768.html + retouches."""
import io, os

BASE = '/home/z/my-project/tr-tmp'
parts = []
for i in range(1, 8):
    p = os.path.join(BASE, f'13768.frag{i}.html')
    with io.open(p, encoding='utf-8') as f:
        parts.append(f.read())

html = '\n'.join(parts)

# --- retouches / corrections de style FR ---
fixes = [
    ("il est de ceux pour qui le sort fut tiré à Badr, et qui n’y assistèrent point",
     "il est de ceux pour qui le sort fut tiré à Badr — une part leur échut — sans qu’ils y assistassent"),
    ("l’homme au pied tordu, surnommé pour cela <em>al-Aʿraj</em>,",
     "surnommé <em>al-Aʿraj</em> pour le pied tordu,"),
    ("qui exigeait de ses élèves qu’ils vinssent porter la chaussure de leur maître avant d’apprendre d’eux une lettre",
     "qui exigeait de ses élèves de porter la chaussure de leur maître avant d’apprendre d’eux une lettre"),
    ("dont la maison accueillit le conseil de l’umma",
     "dans la maison de qui se réunit le conseil de l’umma"),
    ("les trois qui connaissent le mieux le hadith de ʿĀʾisha",
     "les trois qui connaissent le mieux le hadith de ʿĀʾisha"),
    ("des volumes entiers ont été consacrés à sa vie",
     "des volumes entiers ont été consacrés à sa biographie"),
    ("elle fut des premières émigrantes",
     "elle fut parmi les premières émigrantes"),
    ("le collège que la tradition médinoise compte —",
     "le collège que la tradition médinoise dénombre :"),
    ("c’est à ce collège que le commentaire renvoie quand il nomme « l’avis des gens de Médine »",
     "c’est à ce collège que le commentaire renvoie lorsqu’il nomme « l’avis des gens de Médine »"),
    ("L’islam a fait de la servitude une voie de science",
     "L’islam a fait de la servitude une voie vers la science"),
    ("L’index est ainsi une lecture du livre revenu à ses hommes : le plan des leçons, fait noms.",
     "L’index est ainsi une lecture du livre revenue à ses hommes : le plan des leçons fait noms."),
    ("l’élève qui apprend le hadith de Nāfiʿ apprend d’un affranchi devenu le premier maillon du livre",
     "l’élève qui apprend le hadith de Nāfiʿ apprend d’un affranchi devenu premier maillon des chaînes du livre"),
]
for a, b in fixes:
    if a in html:
        html = html.replace(a, b)

out = os.path.join(BASE, '13768.html')
with io.open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print('OK 13768.html :', len(html), 'caractères')
