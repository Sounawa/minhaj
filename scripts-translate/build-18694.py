# -*- coding: utf-8 -*-
"""build-18694.py — assemblage de la leçon 18694 (présentation du manuel de tawqīt) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr18694_{i}.html', encoding='utf-8').read() for i in range(1, 4)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/18694.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : la présentation du manuel' in html)
sonde('badge Leçon 2 / 28', 'Leçon 2 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x1 (N.d.T.)', html.count('<h2>') == 1, f"({html.count('<h2>')})")
sonde('ul x2 (compétences + fihrist)', html.count('<ul>') == 2, f"({html.count('<ul>')})")
sonde('compétences x7', html.count('<li>1.') == 1 and html.count('<li>7.') == 1)
sonde('fihrist x26 titres', html.count('<li>L’introduction à la science') + html.count('<li>Fihrist des sources') == 2)
sonde('N.d.T. ol x8 li', html.count('<li><p>') == 8, f"({html.count('<li><p>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets apparies', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
refs = [f'{a}:{b}' for a, b in re.findall(r'\((\d{1,3}):(\d{1,3})\)', html)]
sonde('refs scripturaires x4 (2:22, 10:5, 17:12, 71:16)',
      set(refs) == {'2:22', '10:5', '17:12', '71:16'}, f'({sorted(set(refs))})')
for terme in ['al-Marġatī', 'al-Muqniʿ', 'al-Malṭaʿ', 'tawqīt', 'manāzil', 'ḥifẓan mutqanan',
              'šarīʿa', 'ʿaǧamiyya', 'ǧummal', 'izdilāf', 'aṯ-ṯānawī al-ʿatīq', 'maghrébins',
              'firāšan', 'sirāǧan', 'première position du tableau', 'iqlāl']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('pas de iʿdād inventé', 'al-iʿdād al-qibliyy' not in html)
sonde('ﷺ absent (aucun hadith ici)', '\uFDFA' not in html)

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
