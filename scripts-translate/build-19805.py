# -*- coding: utf-8 -*-
"""build-19805.py — assemble les 4 fragments en tr-tmp/19805.html + sondes."""
import re, sys

BASE = '/home/z/my-project/tr-tmp/'
parts = [open(f'{BASE}fr19805_{i}.html', encoding='utf-8').read() for i in (1, 2, 3, 4)]
html = '\n'.join(parts)
# auto-fix citations : (N :M) -> (N\u202f:M) espace fine
html, nfix = re.subn(r'\((\d{1,3}) :(\d{1,3})\)', lambda m: f'({m.group(1)}\u202f:{m.group(2)})', html)
print(f'citations normalisées : {nfix}')
open(f'{BASE}19805.html', 'w', encoding='utf-8').write(html)

probes = []
def probe(name, ok, detail=''):
    probes.append((name, ok, detail))

# 1. longueur
probe('longueur', len(html) >= 12000, f'{len(html)} car')

# 2. 0 caractère arabe (hors commentaires)
body = re.sub(r'<!--.*?-->', '', html, flags=re.S)
ar = re.findall(r'[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]', body)
probe('0 arabe', len(ar) == 0, f'{len(ar)} arabe(s)')

# 3. guillemets appariés
ng = body.count('«')
nd = body.count('»')
probe('guillemets', ng == nd, f'«={ng} »={nd}')

# 4. apostrophe droite
na = body.count("'")
probe('apostrophe droite=0', na == 0, f'{na}')

# 5. h1 unique
h1 = re.findall(r'<h1>(.*?)</h1>', body)
probe('h1 unique', len(h1) == 1, f'{len(h1)} : {h1}')

# 6. tables
tables = re.findall(r'<table[^>]*>', body)
closes = body.count('</table>')
probe('tables matn', len(tables) == 1 and closes == 1, f'{len(tables)} open / {closes} close')

# 7. citations format famille (N\u202f:M) — toutes précédées d'une parenthèse
cits = re.findall(r'\(\d{1,3}\u202f:\d{1,3}\)', body)
old = re.findall(r'\(\d{1,3} : ?\d{1,3}\)', body)
probe('citations espace fine', len(cits) >= 30 and len(old) == 0, f'{len(cits)} citations ok, {len(old)} anciens formats')

# 8. h2/h3/h1 arborescence
for tag in ('h2', 'h3'):
    n = len(re.findall(f'<{tag}>', body))
    probe(f'{tag}', n >= 4, f'{n}')

# 9. balises appariées (li, p, ul, ol, dl, dt, dd, em, span, strong)
for tag in ('li', 'p', 'ul', 'ol', 'dl', 'dt', 'dd', 'em', 'span', 'strong', 'tbody', 'tr', 'td'):
    o = len(re.findall(f'<{tag}[ >]', body))
    c = body.count(f'</{tag}>')
    if o != c:
        probe(f'balance {tag}', False, f'{o} open / {c} close')
probe('balance', all(p[1] for p in probes if p[0].startswith('balance')), 'vérifiée')

# 10. badge
probe('badge', 'Leçon 23 / 30' in body, '22/30')

# 11. pas de docId absurdes / pas de texte placeholder
for bad in ('TODO', 'FIXME', 'XXX', 'lorem'):
    if bad in body:
        probe('placeholder', False, bad)

bad = [p for p in probes if not p[1]]
for n, ok, d in probes:
    print(('OK ' if ok else '!! ') + n + (' — ' + d if d else ''))
print('TOTAL:', len(probes), 'sondes,', len(bad), 'échec(s)')
sys.exit(1 if bad else 0)
