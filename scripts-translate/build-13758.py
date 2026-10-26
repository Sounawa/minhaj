#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Concatène les 7 fragments de 13758 en tr-tmp/13758.html + retouches."""
import io, os

BASE = '/home/z/my-project/tr-tmp'
parts = []
for i in range(1, 8):
    p = os.path.join(BASE, f'13758.frag{i}.html')
    with io.open(p, encoding='utf-8') as f:
        parts.append(f.read())

html = '\n'.join(parts)

# --- retouches / corrections de style FR ---
fixes = [
    ("son architecture est celles des", "son architecture est celle des"),
    ("elle se lit comme la chaîne mālikī", "elle se lit comme la chaîne mālikite"),
    ("le patrimoine rendu accessible, chapitre par chapitre, avec ses arguments",
     "le patrimoine rendu accessible, chapitre par chapitre, avec ses arguments textuels"),
    ("c’est le droit vivant du royaume, dont le Livre du hadith pose les fondations scripturaires",
     "c’est le droit vivant du royaume, dont le Livre du hadith enseigne les fondations scripturaires"),
    ("et elle se lit comme la chaîne mālikite elle-même",
     "et elle se lit comme la chaîne mālikite déroulée"),
    ("dresse l’étage de l’explication, et son architecture est celle des leçons elles-mêmes",
     "dresse l’étage de l’explication, et son architecture épouse celle des leçons elles-mêmes"),
    ("quand une version du <em>Muwaṭṭaʾ</em> demandait appui ou éclairage",
     "quand une version du <em>Muwaṭṭaʾ</em> réclamait un appui ou un éclairage"),
    ("les deux <em>Ṣaḥīḥ</em> d’al-Bukhārī et de Muslim",
     "les deux <em>Ṣaḥīḥ</em>, d’al-Bukhārī et de Muslim"),
    ("l’instrument de travail des fuqahāʾ maghrébins",
     "l’instrument de travail des fuqahāʾ du Maghreb"),
    ("elle est la signature de la méthode", "elle est la signature même de la méthode"),
    ("rubrique par rubrique, édition par édition — c’est l’inventaire des instruments avec lesquels le maître a travaillé",
     "rubrique par rubrique, édition par édition : c’est l’inventaire des instruments avec lesquels le maître a travaillé"),
]
for a, b in fixes:
    if a in html:
        html = html.replace(a, b)

out = os.path.join(BASE, '13758.html')
with io.open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print('OK 13758.html :', len(html), 'caractères')
