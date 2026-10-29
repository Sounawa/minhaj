# -*- coding: utf-8 -*-
"""build-19216.py — assemblage de la leçon 19216 (l'introduction à la science du tawqīt) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19216_{i}.html', encoding='utf-8').read() for i in range(1, 6)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19216.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and "Le tawqīt : l'introduction à la science des temps" in html)
sonde('badge Leçon 4 / 28', 'Leçon 4 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h2 N.d.T. présent', '<h2>Notes du traducteur</h2>' in html)
sonde('h2 tamhīd/matn/fahm/taḥlīl/taqwīm/istitmār/iʿdād',
      all(s in html for s in ['Le préambule (at-tamhīd)', '<h2>Le matn</h2>', 'La compréhension (al-fahm)',
                              "L'analyse (at-taḥlīl)", 'Le bilan (at-taqwīm)', "L'exploitation (al-istitmār)",
                              'La préparation (al-iʿdād al-qiblī)']))
sonde('h3 x5', html.count('<h3>') == 5, f"({html.count('<h3>')})")
sonde('h4 x6', html.count('<h4>') == 6, f"({html.count('<h4>')})")
sonde('tables x1 (ḫuṭba 9 tr)', html.count('<table') == 1 and html.count('<tr>') == 9, f"({html.count('<table')}, {html.count('<tr>')})")
sonde('matn-table x1', html.count('class="matn-table"') == 1)
sonde('18 td d\u2019hémistiches', html.count('<td></td>') == 9 and html.count('<td>') == 27, f"({html.count('<td>')})")
sonde('ul x11', html.count('<ul>') == 11, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1, f"({html.count('<ol>')})")
sonde('N.d.T. li<p> x9', html.count('<li><p>') == 9, f"({html.count('<li><p>')})")
sonde('ul imbriqué (dossier)', '<li>Je recherche une définition précise' in html)
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets apparies', g1 == g2, f'({g1}/{g2})')
sonde('salawat conforme à la source', ('\uFDFA' in html) == ('\uFDFA' in open(f'{HOME}/tr-tmp/19216.src.html', encoding='utf-8').read()))
sonde('0 marqueur TODO/TBD', 'TODO' not in html and 'XXX' not in html and '[?]' not in html)
# ancres de contenu
for ancre in ['al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ', 'Abū Miqraʿ', 'al-Firklī', 'al-Baṭīwī',
              'Saʿīdi s-Sūsī', 'sirra llāhi fī ṣidqi ṭ-ṭalab', 'ar-rubʿ al-muǧīb', 'astrolabe',
              'Ibn al-Hayṯam', 'al-Bīrūnī', 'al-Battānī', 'aṭ-Ṭūsī', 'al-Ḫwārazmī', 'Ibn aš-Šāṭir',
              'al-Marrākušī', 'Ukkāymadan', 'dār al-muwaqqit', 'Bagdad', '213 H / 829 M',
              'al-Qarāfī', 'al-Furūq', 'aš-šakāziyya', 'az-zarqāliyya', 'al-binqām', 'aṭ-ṭanǧahara',
              'at-taʿdīl', 'at-taqwīm', 'al-anwāʾ', 'al-hayʾa', 'mā lā yatimmu l-wāǧib',
              '2 :144', '6 :97', '17 :78', '3 :191', '10 :5', '17 :12', 'ǧummal',
              'Assyriens', 'Chaldéens', 'Babyloniens', 'Grecs', 'quatorze', 'vingt-huit manāzil']:
    sonde(f'ancre {ancre}', ancre in html)
sonde('translittération ḫuṭba (bayt 1)', 'yaqūlu, baʿda ḥamdi muǧrī l-falaki' in html and 'ṯumma ʿalā Muḥammadi l-hādī z-zakī' in html)
sonde('translittération ḫuṭba (bayt 9)', 'wa-asʾalu llaḏī bihī staʿantu' in html and 'ʿalayhi an yutimma mā aradtu' in html)
sonde('fentes d\u2019āya documentées (x5)', html.count('arrive vide') >= 5 and 'sans reconstruction' in html)
sonde('règle f documentée', 'soixante-neuvième confirmation' in html)
sonde('rangée : la première leçon vs Leçon 4', 'ad-dars al-awwal' in html)
print(f'\n== {ok} OK / {ko} FAIL == ({n} car)')
sys.exit(1 if ko else 0)
