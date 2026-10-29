# -*- coding: utf-8 -*-
"""build-19219.py — assemblage de la leçon 19219 (ḥurūf al-ǧummal) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19219_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19219.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : les lettres-numérales (ḥurūf al-ǧummal)' in html)
sonde('badge Leçon 5 / 28', 'Leçon 5 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x6', html.count('<h4>') == 6, f"({html.count('<h4>')})")
sonde('ul x5', html.count('<ul>') == 5, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('N.d.T. li x8', html.count('<li><p>') == 8, f"({html.count('<li><p>')})")
sonde('table x2', html.count('<table') == 2, f"({html.count('<table')})")
sonde('tr x2 / td x2', html.count('<tr>') == 2 and html.count('<td>') == 2)
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets apparies', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
refs = re.findall(r'\((\d{1,3}):(\d{1,3})\)', html)
sonde('0 refs versets (doc sans āya)', len(refs) == 0, f'({len(refs)})')
for terme in ['ḥisāb al-ǧummal', 'ab-ǧad, ha-wwaz, ḥu-ṭī, ka-laman, ṣaʿ-faḍ, qa-rasat, ṯa-ḫiẓ, ẓa-ġš',
              'saʿ-faṣ, qu-rašat, ṯa-ḫiẓ, ḍaẓ-ġ', 'al-Būǧarfāwī', 'al-Badr aṭ-ṭāliʿ fī īḍāḥ maqāṣid al-Muqniʿ',
              'Bilmakkī', 'sund', '354', '365', 'bš', 'ǧš', 'yab : 12', 'kad : 24', 'kaḥ : 28', 'lah : 35',
              'qad : 104', 'ḫaṭ : 609', 'ġaṭ : 909', 'sad : 304', 'qal : 130', 'ram : 240', 'ḫaf : 680',
              'sak : 320', 'sahṣ : 365', 'ḫalṭ : 639', 'qayd : 114', 'samḥ : 348',
              'dix-neuvième document consécutif', 'soixante-dixième confirmation', 'ad-dars aṯ-ṯānī',
              'basīṭ', 'kabis', 'fātiḥ de muḥarram', 'ḥu-ṭī', 'ḍaẓ-ġ', 'ẓaḏ-ġ', 'dix-sept des vingt-huit',
              'sans reconstruction', 'Manẓūmat al-Muqniʿ', 'al-Marġatī', 'at-taḥlīl', 'al-iʿdād al-qiblī']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 6, f"({html.count('fente')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
