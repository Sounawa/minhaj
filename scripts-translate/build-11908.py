#!/usr/bin/env python3
"""Concatène les 5 fragments de 11908 en tr-tmp/11908.html + retouches."""
import io, os

BASE = '/home/z/my-project/tr-tmp'
parts = []
for i in range(1, 6):
    p = os.path.join(BASE, f'11908.frag{i}.html')
    with io.open(p, encoding='utf-8') as f:
        parts.append(f.read())

html = '\n'.join(parts)

# --- retouches / corrections de style FR ---
fixes = [
    ("c'est le vendeur qui en démolit le bâtiment ; de même",
     "et c'est le vendeur qui en démolit le bâtiment ; de même"),
    ("est réclamée par son ayant droit ; deux jarres",
     "est réclamée par son ayant droit ; deux jarres"),
]
for a, b in fixes:
    if a in html:
        html = html.replace(a, b)

out = os.path.join(BASE, '11908.html')
with io.open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print('OK 11908.html :', len(html), 'caractères')
