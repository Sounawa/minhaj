# -*- coding: utf-8 -*-
"""build-19248.py — assemblage de la leçon 19248 (jours de l'année ʿaǧmiyya 2) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19248_{i}.html', encoding='utf-8').read() for i in range(1, 6)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19248.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : quelques-uns des jours importants de l’année ʿaǧmiyya' in html)
sonde('badge Leçon 9 / 28', 'Leçon 9 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x2', html.count('<h4>') == 2, f"({html.count('<h4>')})")
sonde('ul x7', html.count('<ul>') == 7, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('N.d.T. li x11', html.count('<li><p>') == 11, f"({html.count('<li><p>')})")
sonde('li total x29', html.count('<li>') == 29, f"({html.count('<li>')})")
sonde('table x3', html.count('<table') == 3, f"({html.count('<table')})")
sonde('tr x8 / td x24', html.count('<tr>') == 8 and html.count('<td>') == 24, f"({html.count('<tr>')}/{html.count('<td>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets apparies', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars as-sābiʿ', 'soixante-quatorzième', 'Leçon 9 / 28',
              'at-tamhīd', 'al-fahm', 'at-taḥlīl', 'at-taqwīm', 'al-istitmār',
              'al-iʿdād al-qiblī', 'istiḫlāṣ maḍāmīn al-matn', 'aš-šarḫ', 'matn', 'naẓim',
              'faṣl', 'manāzil', 'burūǧ', 'ʿaǧmiyya', 'falaḥī',
              'yanāyir al-falaḥī', 'fabrāyir', 'māyuh', 'aġušt', 'nūnbir', 'al-ḥāǧūz',
              'al-farġ al-muqaddam', 'muqaddam al-farġayn', 'al-haqʿa', 'aṣ-ṣarfa', 'aš-šawla',
              'fahṣš', 'qawluhum', 'yahhin', 'yazzin', 'yaw', 'ad-dāl', 'hā',
              'ḥisāb s-sāʾir', 'ḥisāb', 'nuqtat',
              'al-Ilġī', 'ḥāšiyya', 'raṣd', 'marǧūḥa', 'aṣaḥḥ',
              'al-iʿtidāl', 'al-inqilāb', 'ḥarakat al-iqbāl', 'iʿtidālān', 'inqilābān',
              'al-ǧabha', 'yadd', 'sahṣ', 'kabīs', 'basīṭa', 'kabīsa', 'kinyāya',
              'lundi 25 décembre 2023', 'jeudi', 'vendredi', 'lundi',
              'quatre-vingt-onze', 'quatre-vingt-douze', 'trois cent soixante-cinq',
              '45', '136', '228', '319',
              'septième grande fente', 'sans reconstruction', 'garde du traducteur',
              'vingt-deux documents consécutifs', 'mots-nombres', 'GT-isme',
              'al-Ḫaṭṭābī', 'seconde autorité extérieure', 'dūna mayn', 'ḥissā',
              'rubʿ al-muǧīb', 'tableau maître des ǧummal', 'fihrist',
              'dix-neuf leçons restent', 'Neuf documents']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 8, f"({html.count('fente')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
