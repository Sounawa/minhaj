# -*- coding: utf-8 -*-
"""build-19292.py — assemblage de la leçon 19292 (les activités des leçons 7 à 12) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19292_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19292.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : les activités d’exploitation des apprentissages et de leur soutien (des leçons 7 à 12)' in html)
sonde('badge Leçon 15 / 28', 'Leçon 15 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x5', html.count('<h2>') == 5, f"({html.count('<h2>')})")
sonde('h3/h4/h5 x0', html.count('<h3>') == 0 and html.count('<h4>') == 0 and html.count('<h5>') == 0)
sonde('ul x5', html.count('<ul>') == 5, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('li total x27 (14 corps + 13 notes)', html.count('<li>') == 27, f"({html.count('<li>')})")
sonde('1 fente <p></p> (table)', html.count('<p></p>') == 1, f"({html.count('<p></p>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets appariés', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars aṯ-ṯāliṯ ʿašar', 'quatre-vingtième', 'Leçon 15 / 28',
              'al-iʿdād al-qiblī', 'an-našāṭ', 'Notes du traducteur',
              'ḥarakat al-iqbāl', 'iʿtidāl rabīʿī', 'sept cents', '653',
              'kabīsa', 'madḫal', 'madāḫil', 'qāʾid', 'as de l’année arabe',
              'yanāyir', 'fabrīr', 'mars', 'ibrīl', 'māyy', 'yunīh', 'yulyaza',
              'gusht', 'šutanbar', 'uktūbar', 'nūnbar', 'duǧanbar',
              'mercredi', 'mardi', 'dimanche', 'vendredi', 'samedi', 'jeudi', 'lundi',
              '2331', '1441', '1398', '1395', '1300', '1433', '1944', '179', '1373',
              '1363', '796', '1954', '74', '622', 'az-dilāfāt', 'falaḥī', 'milādī',
              'hégirienne', 'manzila', 'manāzil', 'faṣl', 'Mālik', 'al-ʿAlamī',
              'muwaqqit', 'muʿaddil', 'Taqrīb al-baʿīd min al-ǧāmiʿ al-mufīd',
              'treizième grande fente', 'vingt-huit documents consécutifs',
              'GT-isme', 'enseignant(e)', 'Raḥim'.lower()]:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 5, f"({html.count('fente')})")
sonde('déroulés de la garde', html.count('déroulé') >= 4, f"({html.count('déroulé')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
