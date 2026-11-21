#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — assemblage + QA du htmlFr de la leçon 19 (hadith-tanawi-3, R778)."""
from pathlib import Path
import re, sys

REP = Path('/home/z/my-project/scripts-tmp/l19')
frag = ['f1-objectifs-tamhid.html', 'f2-textes.html', 'f3-tarjama-fahm.html',
        'f4-fiqh-istisna.html', 'f5-fiqh-himala-taqwim.html']
html = ''
for f in frag:
    html += (REP / f).read_text(encoding='utf-8').strip() + '\n'

erreurs = []
# 1) balises appariées
for tag in ('span', 'p', 'h1', 'h2'):
    o = len(re.findall(rf'<{tag}[ >]', html))
    c = html.count(f'</{tag}>')
    if o != c:
        erreurs.append(f'balise {tag}: {o} ouvrantes / {c} fermantes')
# 2) guillemets appariés
n_ouvre = html.count('«')
n_ferme = html.count('»')
if n_ouvre != n_ferme:
    erreurs.append(f'guillemets: {n_ouvre} « / {n_ferme} »')
# 3) 0 apostrophe droite
n_ap = html.count(chr(39))
if n_ap:
    erreurs.append(f'{n_ap} apostrophes droites (')
# 4) 0 ﷺ dans ce livre (les autres leçons n'en portent pas)
if 'ﷺ' in html:
    erreurs.append('le ﷺ présent (le livre n\'en porte pas)')
# 5) marqueurs interdits
for m in ('**', 'TODO', 'XXX', 'undefined', 'NaN'):
    if m in html:
        erreurs.append(f'marqueur {m!r} présent')
# 6) spans RTL non vides
vides = len(re.findall(r'<span dir="rtl" lang="ar">\s*</span>', html))
if vides:
    erreurs.append(f'{vides} spans arabes vides')

n_car = len(html)
print(f'htmlFr assemblé : {n_car} caractères')
print(f'guillemets « {n_ouvre} / » {n_ferme}')
print(f'spans arabes : {len(re.findall(chr(34)+"rtl", html))}')
print(f'?? séparateurs : {html.count(chr(63)*2)}')
if erreurs:
    print('QA ÉCHEC :')
    for e in erreurs:
        print(' -', e)
    sys.exit(1)
(REP / 'l19-htmlfr.html').write_text(html, encoding='utf-8')
print('QA PASS — écrit', REP / 'l19-htmlfr.html')
