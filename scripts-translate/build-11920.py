#!/usr/bin/env python3
"""Concatène les 5 fragments de 11920 en tr-tmp/11920.html + retouches."""
import io, os

BASE = '/home/z/my-project/tr-tmp'
parts = []
for i in range(1, 6):
    p = os.path.join(BASE, f'11920.frag{i}.html')
    with io.open(p, encoding='utf-8') as f:
        parts.append(f.read())

html = '\n'.join(parts)

# --- retouches / corrections de style FR ---
fixes = [
    ("La bénéfice de cela apparaît", "Le bénéfice de cela apparaît"),
    ("il n'est pas permis de vendre de l'or contre de l'or, pareil pour pareil, à terme ;",
     "il n'est pas permis de vendre de l'or contre de l'or, pareil pour pareil, à terme ;"),
    ("telle l'échange de deux", "tel l'échange de deux"),
]
for a, b in fixes:
    if a in html:
        html = html.replace(a, b)

out = os.path.join(BASE, '11920.html')
with io.open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print('OK 11920.html :', len(html), 'caractères')
