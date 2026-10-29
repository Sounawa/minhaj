# -*- coding: utf-8 -*-
"""build-19316.py — assemblage de la leçon 19316 (les activités d'exploitation des leçons 14 à 16) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19316_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19316.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : les activités d’exploitation des apprentissages et de leur soutien (des leçons 14 à 16)' in html)
sonde('badge Leçon 19 / 28', 'Leçon 19 / 28' in html)
sonde('dl 3 dt / 3 dd (pas de date)', html.count('<dt>') == 3 and html.count('<dd>') == 3, f"({html.count('<dt>')}/{html.count('<dd>')})")
sonde('h2 x10', html.count('<h2>') == 10, f"({html.count('<h2>')})")
sonde('h2 vides x4', html.count('<h2></h2>') == 4, f"({html.count('<h2></h2>')})")
sonde('h3/h4/h5 x0', html.count('<h3>') == 0 and html.count('<h4>') == 0 and html.count('<h5>') == 0)
sonde('ul x6', html.count('<ul>') == 6, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('li total x32 (19 corps + 13 notes)', html.count('<li>') == 32, f"({html.count('<li>')})")
sonde('tables x0', html.count('<table') == 0, f"({html.count('<table')})")
sonde('1 fente <p></p> (tableau perdu)', html.count('<p></p>') == 1, f"({html.count('<p></p>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets appariés', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars as-sābiʿ ʿašar', 'quatre-vingt-quatrième', 'Leçon 19 / 28',
              'al-iʿdād al-qiblī', 'Notes du traducteur',
              'an-našāṭ al-awwal', 'an-našāṭ aṯ-ṯānī', 'an-našāṭ aṯ-ṯāliṯ', 'an-našāṭ ar-rābiʿ',
              'manzila', 'manāzil', 'burj', 'burūǧ', 'faṣl', 'hilāl',
              'Al-azmān wa-l-anwāʾ', 'Ibn al-Aǧdābī', 'ʿIzzat Ḥasan',
              'muwaqqit', 'ar-raqīb', 'maġrib', 'mašriq', 'musayyir', 'muqarrir',
              'yulfā', 'yansalib', 'iqṭaʿā',
              'at-tawqīt', 'ʿaǧmiyya', 'istinbāṭ', 'azmān', 'anwāʾ',
              'dix-huitième grande fente', 'deuxième document consécutif',
              'Lundi 08 janvier 2024', '(x)', 'enseignant(e)', 'GT-isme',
              'quatre-vingt-quatrième fois', 'la garde']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 4, f"({html.count('fente')})")
sonde('déroulés de la garde', html.count('déroulé') >= 2, f"({html.count('déroulé')})")
sonde('pas de GT-isme « maisons » seul rendu', 'maisons du zodiaque' in html)
sonde('GT-ismes cités en N.d.T. (citations documentaires)', all(t in html for t in ['Calendrier', 'panneaux', 'Préparation tribale', 'un verset']))
sonde('calendrier absent du corps (hors N.d.T.)', html.replace('« Calendrier des activités', 'X').count('alendrier') <= 1)

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
