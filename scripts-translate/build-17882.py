#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Concatène les 4 fragments de 17882 en tr-tmp/17882.html + retouches."""
import io, os

BASE = '/home/z/my-project/tr-tmp'
parts = []
for i in range(1, 5):
    p = os.path.join(BASE, f'17882.frag{i}.html')
    with io.open(p, encoding='utf-8') as f:
        parts.append(f.read())

html = '\n'.join(parts)

# --- retouches / corrections de style FR ---
fixes = [
    ("Le manuel fait therefore une pédagogie comparative",
     "Le manuel fait ainsi une pédagogie comparative"),
    ("la seconde canonique au Maroc, le second en d’autres terres",
     "la première canonique au Maroc, le second en d’autres terres"),
    ("ce où les deux divergent", "là où les deux divergent"),
    ("le second degré de l’école traditionnelle, entre le primaire et le secondaire",
     "le degré moyen de l’école traditionnelle, entre le primaire et le secondaire"),
    ("dont le caractère fut le Coran — la récitation parfaite est celle qui devient manière d’être.",
     "dont le caractère fut le Coran : la récitation parfaite est celle qui devient manière d’être."),
    ("c’est une récitation réglée, dont la lettre a ses droits",
     "c’est une récitation réglée dont la lettre a ses droits"),
    ("qu’il ou qu’elle ait mémorisé", "qu’il ou qu’elle ait mémorisé"),
    ("s’habituent à la langue seule, elles s’habituent au cœur",
     "ne s’habituent pas à la langue seule : elles s’habituent au cœur"),
    ("et les six chapitres ;", "et des six chapitres ;"),
]
for a, b in fixes:
    if a in html:
        html = html.replace(a, b)

out = os.path.join(BASE, '17882.html')
with io.open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print('OK 17882.html :', len(html), 'caractères')
