# -*- coding: utf-8 -*-
"""Fix final verify 275 + gabarit HTML tamhīd."""
# 1. HTML : ajouter la glose (al-muḍṭarab) après l'incohérent du tamhīd
f = 'tr-tmp/lesson-uh2-pdf-mut23h2u-275-fr.html'
h = open(f, encoding='utf-8').read()
old = 'l\u2019incoh\u00e9rent, et le d\u00e9sordonn\u00e9 (al-mu\u1e63\u1e25af)'
new = 'l\u2019incoh\u00e9rent (al-mu\u1e0d\u1e6darab), et le d\u00e9sordonn\u00e9 (al-mu\u1e63\u1e25af)'
assert old in h, 'HTML tamhīd : cible absente'
h = h.replace(old, new)
open(f, 'w', encoding='utf-8').write(h)
print('HTML tamhīd corrigé')

# 2. verify : cas 3 — le HTML porte l'ellipse « ... » avant la fermeture
f = 'scripts-translate/verify-ulumhadith2-pdf275.py'
v = open(f, encoding='utf-8').read()
old = ('ne vous ha\u00efssez pas, ne vous enviez pas, ne vous tournez pas le dos, '
       '(et ne vous faites pas concurrence) \u00bb')
new = ('ne vous ha\u00efssez pas, ne vous enviez pas, ne vous tournez pas le dos, '
       '(et ne vous faites pas concurrence)')
assert old in v, 'verify cas 3 : cible absente'
v = v.replace(old, new)
print('verify cas 3 corrigé')

# 3. verify : voie 2 — citer la séquence réelle du HTML
old = ('\u00ab une autre version que je dis sans l\u2019avoir entendue de lui : qui meurt sans faire de rival '
       '\u00e0 Dieu, Dieu le fait entrer dans le Paradis \u00bb')
new = ('qui a fait un rival \u00e0 Dieu, Dieu le met dans le Feu, et il a dit : '
       '\u00ab et une autre version que je dis sans l\u2019avoir entendue de lui : qui meurt sans faire de rival '
       '\u00e0 Dieu, Dieu le fait entrer dans le Paradis \u00bb')
if old in v:
    v = v.replace(old, new)
    print('verify voie 2 corrigé (compound)')
else:
    # vérifier l'état split déjà présent
    ok = '\u00ab et une autre version que je dis sans l\u2019avoir entendue de lui' in v
    print('verify voie 2 : forme split présente =', ok)
    assert ok, 'voie 2 : ni compound ni split'
open(f, 'w', encoding='utf-8').write(v)
print('verify écrit')
