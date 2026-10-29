# -*- coding: utf-8 -*-
"""build-19277.py — assemblage de la leçon 19277 (l'as de l'année et l'entrée des mois ʿaǧmiyya) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19277_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19277.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : l’as de l’année et l’entrée des mois ʿaǧmiyya' in html)
sonde('badge Leçon 13 / 28', 'Leçon 13 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x4', html.count('<h4>') == 4, f"({html.count('<h4>')})")
sonde('h5 x5', html.count('<h5>') == 5, f"({html.count('<h5>')})")
sonde('ul x10', html.count('<ul>') == 10, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('N.d.T. li x15', html.count('<li><p>') == 15, f"({html.count('<li><p>')})")
sonde('li total x37', html.count('<li>') == 37, f"({html.count('<li>')})")
sonde('table x3', html.count('<table') == 3, f"({html.count('<table')})")
sonde('tr x9 / td x27', html.count('<tr>') == 9 and html.count('<td>') == 27, f"({html.count('<tr>')}/{html.count('<td>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets appariés', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
# pointillés de la source (rasm portés tels quels)
sonde('pointillés matn bayt 1 (29)', '.' * 29 in html)
sonde('pointillés citation bayt 1 (26)', '.' * 26 in html)
sonde('pelotons >= 20 exacts x2', len(re.findall(r'(?<!\.)\.{20,}(?!\.)', html)) == 2, f"({[len(m.group(0)) for m in re.finditer(r'(?<!\.)\.{20,}(?!\.)', html)]})")
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars al-ḥādī ʿašar', 'soixante-dix-huitième', 'Leçon 13 / 28',
              'at-tamhīd', 'al-fahm', 'at-taḥlīl', 'at-taqwīm', 'al-istitmār',
              'al-iʿdād al-qiblī', 'istiḫlāṣ maḍāmīn', 'aš-šarḫ', 'matn', 'naẓim',
              'bayt', 'ʿaǧmiyya', 'yanāyir', 'yannayr',
              'qalqalīs', 'qāʾid', 'madḫal', 'madāḫil', 'az-dilāf', 'kabīsa', 'asūs',
              'yannayrā', 'fabrīr', 'mars', 'ibrīl', 'māyy', 'yulyaza', 'gusht',
              'šutanbar', 'uktūbar', 'nūnbar', 'duǧanbar',
              'adad', 'zabah', 'zaǧaw', 'ḥadaw', 'fuh',
              'aṣl', 'asās', 'an-nuṭq',
              '653', '1395', '1419', '1460', '1441', '1420',
              'muharram', 'ramaḍān', 'ḏū-l-ḥiǧǧa', 'ǧumādā I',
              'samedi', 'vendredi', 'lundi', 'mercredi', 'dimanche', 'mardi',
              'onzième grande fente', 'sans reconstruction', 'garde du traducteur',
              'vingt-six documents consécutifs', 'GT-isme',
              'quinze leçons restent', 'milādī']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 8, f"({html.count('fente')})")
sonde('notes N.d.T. présentes', html.count('Notes du traducteur') == 1)

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
