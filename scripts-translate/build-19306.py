# -*- coding: utf-8 -*-
"""build-19306.py — assemblage de la leçon 19306 (le degré du Soleil dans son burj) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19306_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19306.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : le processus d’extraction du degré du Soleil dans son burj' in html)
sonde('badge Leçon 17 / 28', 'Leçon 17 / 28' in html)
sonde('dl 4 dt / 4 dd', html.count('<dt>') == 4 and html.count('<dd>') == 4)
sonde('date de séance (lundi 08 janvier 2024)', 'Lundi 08 janvier 2024' in html)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x6', html.count('<h4>') == 6, f"({html.count('<h4>')})")
sonde('h5 x3', html.count('<h5>') == 3, f"({html.count('<h5>')})")
sonde('ul x6', html.count('<ul>') == 6, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('li total x27 (14 corps + 13 notes)', html.count('<li>') == 27, f"({html.count('<li>')})")
sonde('tables x9 (1 matn + 7 citations + 1 poème)', html.count('<table') == 9, f"({html.count('<table')})")
sonde('matn-table x8 (dir=ltr)', html.count('<table dir="ltr" class="matn-table">') == 8)
sonde('poème sans dir x1', html.count('<table>\n<tbody>') == 1 or re.search(r'<table>\s*<tbody>', html) is not None)
sonde('tr x19', html.count('<tr>') == 19, f"({html.count('<tr>')})")
sonde('td x57', html.count('<td>') == 57, f"({html.count('<td>')})")
sonde('4 fentes <p></p> stricte', html.count('<p></p>') == 4, f"({html.count('<p></p>')})")
sonde('1 fente <p><span></span></p>', html.count('<p><span></span></p>') == 1, f"({html.count('<p><span></span></p>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets appariés', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars al-ḫāmis ʿašar', 'quatre-vingt-deuxième', 'Leçon 17 / 28',
              'al-iʿdād al-qiblī', 'Notes du traducteur',
              'burj', 'burūǧ', 'falak', 'usūs', 'ḥarakat al-iqbāl',
              'manzila', 'manāzil', 'la Jabha', 'an-naṭḥ',
              'al-ḥamal', 'aṯ-ṯawr', 'al-ǧawzāʾ', 'as-saraṭān', 'al-asad',
              'as-sunbula', 'al-mīzān', 'al-ʿaqrab', 'al-qaws', 'al-ǧadī',
              'ad-dalw', 'al-ḥūt', 'cercle des burūǧ', 'cercle écliptique',
              'yanāyir', 'fabrāyir', 'mars', 'ibrīl', 'māy', 'yūnyū',
              'yūlyūz', 'ġust', 'šutanbar', 'uktūbar', 'nūnbar', 'duǧanbar',
              'falaḥī', 'ʿaǧmī', 'yannayr', 'duǧanbir',
              '(yahh)', '(lāmā)', '(zaḥw)', '(zawaw)', '(dahah)', '(dahaw)',
              'Ibn Zākūr', 'Belmekkī', 'al-Baʿqīlī', 'al-Ǧādirī',
              'Rawḍat al-azhār', 'at-taʿdīl', 'Idrīs al-ʿIrāqī',
              'manzilat al-hilāl', 'tumsī', 'yuhil',
              'quinzième grande fente', 'vingt-neuf documents consécutifs',
              'Lundi 08 janvier 2024', 'GT-isme', 'Septième état', 'muṣḥaf',
              'az-dilāf', 'madḫal', 'naẓm', 'at-taqwīm', 'istitmār',
              'farattibannahā', 'yunqaṣu yawmāni']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td', 'span']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 5, f"({html.count('fente')})")
sonde('déroulés de la garde', html.count('déroulé') >= 4, f"({html.count('déroulé')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
