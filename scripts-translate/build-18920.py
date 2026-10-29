# -*- coding: utf-8 -*-
"""build-18920.py — assemblage de la leçon 18920 (les jours de l'année arabe, fātiḥ muḥarram) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr18920_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/18920.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and "Le tawqīt : les jours de l'année arabe et le fātiḥ de muḥarram" in html)
sonde('badge Leçon 3 / 28', 'Leçon 3 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h2 N.d.T. présent', '<h2>Notes du traducteur</h2>' in html)
sonde('h2 tamhīd/matn/fahm/taḥlīl/taqwīm/istitmār/iʿdād',
      all(s in html for s in ['Le préambule (at-tamhīd)', '<h2>Le matn</h2>', 'La compréhension (al-fahm)',
                              "L'analyse (at-taḥlīl)", 'Le bilan (at-taqwīm)', "L'exploitation (al-istitmār)",
                              'La préparation (al-iʿdād al-qiblī)']))
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x7', html.count('<h4>') == 7, f"({html.count('<h4>')})")
sonde('h5 x4', html.count('<h5>') == 4, f"({html.count('<h5>')})")
sonde('tables x2', html.count('<table') == 2, f"({html.count('<table')})")
sonde('matn-table x2', html.count('class="matn-table"') == 2)
sonde('ul x9', html.count('<ul>') == 9, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1, f"({html.count('<ol>')})")
sonde('N.d.T. li<p> x9', html.count('<li><p>') == 9, f"({html.count('<li><p>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets apparies', g1 == g2, f'({g1}/{g2})')
sonde('fdfa présent (convention corpus)', '\uFDFA' in html)
sonde('0 marqueur TODO/TBD', 'TODO' not in html and 'XXX' not in html and '[?]' not in html)
# ancres de contenu
for ancre in ['sund', 'le kabs', '354', '355', 'ḥisāb al-ǧummal', 'dāʾira', 'al-ʿalāma',
              'ʿUmar b. al-Ḫaṭṭāb', '9 :36', '10 :5', '9 :37', '74 417', '64 140',
              'bahzay', 'kaww', 'kaṭṭ', 'aǧad, wazab, ǧahaw, abad', 'ḏū al-ḥiǧǧa',
              'ad-dars aṯ-ṯāliṯ', 'al-kalīm', 'arġab', 'arbaʿatun ḥurum', 'manāzila',
              'kinyāya', 'nasīʾ', 'rūʾyat' ]:
    sonde(f'ancre {ancre}', ancre in html)
sonde('ancre rūʾya du croissant', 'rūʾyat' in html or 'vision du croissant' in html)
# structure table matn : 1 tr x 3 td
matn_tbl = re.search(r'<table class="matn-table">.*?</table>', html, re.S)
sonde('matn table 1 tr x 3 td', matn_tbl and matn_tbl.group(0).count('<tr>') == 1 and matn_tbl.group(0).count('<td>') == 3)
# table poeme : 2 tr
poem_tbl = re.search(r'<table dir="ltr" class="matn-table">.*?</table>', html, re.S)
sonde('poeme table 2 tr x 6 td', poem_tbl and poem_tbl.group(0).count('<tr>') == 2 and poem_tbl.group(0).count('<td>') == 6)
sonde('translittération bayt matn', 'wa-s-sudsu minhumā yakūnu l-kabsu' in html and 'ayyāmuhu (sund) wa-zīda l-ḫumsu' in html)
sonde('onze positions kabis', '2, 5, 7, 10, 13, 15, 18, 21, 24, 26, 29' in html)
sonde('fentes portées (3 tableaux vides)', html.count('fente') >= 3 and 'sans reconstruction' in html)
sonde('reste 181 (exemple 1441)', '181' in html)
sonde('objectifs x3 en li', html.count('<li>1. Qu') == 1 and html.count('<li>3. Qu') == 1)
sonde('rang inclusif documenté', 'rang inclusif' in html)
print(f'\n== {ok} OK / {ko} FAIL == ({n} car)')
sys.exit(1 if ko else 0)
