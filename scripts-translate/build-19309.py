# -*- coding: utf-8 -*-
"""build-19309.py — assemblage de la leçon 19309 (la manzila de la Lune et le garde-fou des manāzil du hilāl) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19309_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19309.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : le processus d’extraction de la manzila de la Lune et le garde-fou des manāzil dans lesquelles le hilāl apparaît' in html)
sonde('badge Leçon 18 / 28', 'Leçon 18 / 28' in html)
sonde('dl 3 dt / 3 dd (pas de date)', html.count('<dt>') == 3 and html.count('<dd>') == 3, f"({html.count('<dt>')}/{html.count('<dd>')})")
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x5 (dont 1 vide)', html.count('<h4>') == 5 and '<h4></h4>' in html, f"({html.count('<h4>')})")
sonde('h5 x0', html.count('<h5>') == 0)
sonde('ul x4', html.count('<ul>') == 4, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('li total x20 (13 corps + 7 notes)', html.count('<li>') == 20, f"({html.count('<li>')})")
sonde('tables x5 (1 matn sans dir + 4 citations dir=ltr)', html.count('<table') == 5, f"({html.count('<table')})")
sonde('matn-table dir=ltr x4', html.count('<table dir="ltr" class="matn-table">') == 4)
sonde('table poème sans dir x1', len(re.findall(r'<table class="matn-table">', html)) == 1)
sonde('tr x9', html.count('<tr>') == 9, f"({html.count('<tr>')})")
sonde('td x27', html.count('<td>') == 27, f"({html.count('<td>')})")
sonde('4 fentes <p></p> stricte', html.count('<p></p>') == 4, f"({html.count('<p></p>')})")
sonde('1 fente <p><span></span></p>', html.count('<p><span></span></p>') == 1, f"({html.count('<p><span></span></p>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets appariés', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars as-sādis ʿašar', 'quatre-vingt-troisième', 'Leçon 18 / 28',
              'al-iʿdād al-qiblī', 'Notes du traducteur',
              'manzila', 'manāzil', 'hilāl', 'manzilat al-hilāl', 'tumsī', 'yuhillu',
              'istihlāl', 'ḍābiṭ', 'naẓm', 'falak', 'faṣl ar-rabīʿī',
              'al-farġ al-muqaddam', 'al-farġ al-muʾaḫḫar', 'baṭn al-ḥūt', 'aṭ-ṭarf',
              'saʿd as-suʿūd', 'aṯ-ṯurayyā', 'an-naṯra', 'al-ġafr', 'al-qalb',
              'aṣ-ṣarfa', 'aḏ-ḏirāʿ', 'al-haqʿa', 'al-hanaʿa', 'naʿāim',
              '(luṭin)', '(ġuṣin)', '(šuġin)', '(kaqin)', '(nuʿin)', '(duḏ)',
              '(yasin)', '(famin)', '(manin)', '(iṯin)', '(mahin)', '(yuḏ)',
              'yanāyir', 'fabrāyir', 'mars', 'ibrīl', 'māy', 'yūnyū',
              'yūlyūz', 'ġušt', 'šutanbar', 'uktūbar', 'nūnbar', 'duǧanbar',
              'falaḥī', 'ʿaǧmī', 'ʿaǧamī', 'ḏū-l-qaʿda', 'ḏū-l-ḥiǧǧa',
              'muḥarram 1435', 'šaʿbān 1435', 'ramaḍān 1440',
              '30 nūnbar 2319 falaḥī', '22 uktūbar 2324', '16 māy 2325', '23 ibrīl 2330',
              '24 fabrāyir 2308', '15 fabrāyir', 'Lundi 08 janvier 2024',
              'Yūnus 10 : 5', 'Yā-Sīn 36 : 40', 'wa-qaddarahu manāzila',
              'seizième grande fente', 'dix-septième', 'huitième état de la doxologie',
              'rotation synchrone', '1417 h.', 'degré 13', 'GT-isme' if False else 'taqrīb',
              'quatre-vingt-troisième fois']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td', 'span']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 4, f"({html.count('fente')})")
sonde('déroulés de la garde', html.count('déroulé') >= 2, f"({html.count('déroulé')})")
sonde('pas de GT-isme « grégorien »', 'grégorien' not in html)
sonde('pas de GT-isme « calendrier » pour taqwīm', 'calendrier' not in html)
sonde('pas de « position » pour manzila', 'position de la Lune' not in html)

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
