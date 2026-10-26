#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Concatène les 5 fragments de 11798 en tr-tmp/11798.html + retouches."""
import io, os

BASE = '/home/z/my-project/tr-tmp'
parts = []
for i in range(1, 6):
    p = os.path.join(BASE, f'11798.frag{i}.html')
    with io.open(p, encoding='utf-8') as f:
        parts.append(f.read())

html = '\n'.join(parts)

# --- retouches / corrections de style FR ---
fixes = [
    ("pour vous deux une voie d’ascension",
     "pour vous deux, une voie d’ascension"),
    ("les plus importants termes uṣūlīs",
     "les plus importants des termes uṣūlīs"),
    ("l’élève et l’élève, que la série accompagne ensemble",
     "l’élève et l’élève que la série accompagne ensemble"),
]
for a, b in fixes:
    if a in html:
        html = html.replace(a, b)

out = os.path.join(BASE, '11798.html')
with io.open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print('OK 11798.html :', len(html), 'caractères')
