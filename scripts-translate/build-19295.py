# -*- coding: utf-8 -*-
"""build-19295.py — assemblage de la leçon 19295 (le processus d'extraction de la manzila du Soleil) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19295_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19295.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : le processus d’extraction de la manzila du Soleil pour toute date' in html)
sonde('badge Leçon 16 / 28', 'Leçon 16 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x5', html.count('<h4>') == 5, f"({html.count('<h4>')})")
sonde('h5 x2', html.count('<h5>') == 2, f"({html.count('<h5>')})")
sonde('ul x5', html.count('<ul>') == 5, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('li total x27 (15 corps + 12 notes)', html.count('<li>') == 27, f"({html.count('<li>')})")
sonde('table x2 (matn + poème)', html.count('<table') == 2, f"({html.count('<table')})")
sonde('fente <p></p> x2 (répartition + exemple a)', html.count('<p></p>') == 2, f"({html.count('<p></p>')})")
sonde('fente <p><span></span></p> x1 (exemple b)', html.count('<p><span></span></p>') == 1)
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets appariés', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars ar-rābiʿ ʿašar', 'quatre-vingt-unième', 'Leçon 16 / 28',
              'al-iʿdād al-qiblī', 'Notes du traducteur', 'at-tamhīd', 'al-matn',
              'al-fahm', 'aš-šarḫ', 'istiḫlāṣ maḍāmīn', 'at-taḥlīl', 'at-taqwīm',
              'al-istitmār', 'manzila', 'manāzil', 'faṣl', 'burj', 'burūj',
              'ǧummal', 'ǧīm', 'yaǧǧ', 'yadd', 'muntahā', 'taqaddamā',
              'an-naṭḥ', 'al-buṭayn', 'aṯ-ṯurayyā', 'ad-dabarān', 'al-haqʿa',
              'al-hanʿa', 'aḏ-ḏirāʿ', 'nathra', 'aṭ-ṭarf', 'al-ǧabha', 'az-zubra',
              'aṣ-ṣarfa', 'al-ʿawwā', 'as-simāk', 'al-ġafr', 'az-zabnān', 'al-iklīl',
              'al-qalb', 'aš-šawla', 'an-naʿāʾim', 'al-balda', 'ḏābiḥ', 'bulaʿ',
              'saʿūd', 'aḫbīya', 'farġ', 'baṭn al-ḥūt', 'fallāḥīn', 'raṣd',
              'kawākib siyāra', 'buyūt', 'aṭ-Ṭāhirī', 'al-ʿIrāqī',
              'rabīʿ', 'ṣayf', 'ḫarīf', 'aš-šitāʾ', 'falaḥī',
              'mars', 'ibrīl', 'māyy', 'yūnyū', 'yūlyūz', 'ġust',
              'šutanbir', 'uktūbar', 'nūnbar',
              'quatorzième grande fente', 'vingt-neuf documents consécutifs',
              'GT-isme', 'sixième état', 'déroulé de la garde', 'p. 102']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td', 'strong', 'em']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 5, f"({html.count('fente')})")
sonde('déroulés de la garde', html.count('déroulé') >= 4, f"({html.count('déroulé')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
