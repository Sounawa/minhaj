#!/usr/bin/env python3
"""Concatène les 5 fragments de 11922 en tr-tmp/11922.html + retouches."""
import io, os

BASE = '/home/z/my-project/tr-tmp'
parts = []
for i in range(1, 6):
    p = os.path.join(BASE, f'11922.frag{i}.html')
    with io.open(p, encoding='utf-8') as f:
        parts.append(f.read())

html = '\n'.join(parts)

# --- retouches / corrections de style FR ---
fixes = [
    ("la septième now traite d'un danger plus discret",
     "la septième traite d'un danger plus discret"),
    ("est un mot-madelest mnémotechnique",
     "est un mot mnémotechnique"),
    ("comme si l'on vendait un vêtement et des dollars pour mille dirhams marocains, par exemple.",
     "comme si l'on vendait un vêtement avec des dollars pour mille dirhams marocains, par exemple."),
    ("Cette leçon comporte des axes que l'imprimé annonce deux, et que sa structure déploie en trois :",
     "Cette leçon comporte des axes que l'imprimé annonce être deux, et que sa structure déploie en trois :"),
]
for a, b in fixes:
    if a in html:
        html = html.replace(a, b)

out = os.path.join(BASE, '11922.html')
with io.open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print('OK 11922.html :', len(html), 'caractères')
