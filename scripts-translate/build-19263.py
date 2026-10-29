# -*- coding: utf-8 -*-
"""build-19263.py — assemblage de la leçon 19263 (lyālī, samāʾim, nīsān) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19263_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19263.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : connaître l' + "'" + 'entrée des lyālī, des samāʾim et du nīsān' in html)
sonde('badge Leçon 11 / 28', 'Leçon 11 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x6', html.count('<h4>') == 6, f"({html.count('<h4>')})")
sonde('ul x6', html.count('<ul>') == 6, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('N.d.T. li x13', html.count('<li><p>') == 13, f"({html.count('<li><p>')})")
sonde('li total x28', html.count('<li>') == 28, f"({html.count('<li>')})")
sonde('table x7', html.count('<table') == 7, f"({html.count('<table')})")
sonde('tr x17 / td x51', html.count('<tr>') == 17 and html.count('<td>') == 51, f"({html.count('<tr>')}/{html.count('<td>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets apparies', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars at-tāsiʿ', 'soixante-seizième', 'Leçon 11 / 28',
              'at-tamhīd', 'al-fahm', 'at-taḥlīl', 'at-taqwīm', 'al-istitmār',
              'al-iʿdād al-qiblī', 'istiḫlāṣ maḍāmīn', 'aš-šarḫ', 'matn', 'naẓim',
              'bayt', 'ʿaǧmiyya', 'falaḥī', 'muhimmāt',
              'al-lyālī', 'as-samāʾim', 'an-nīsān', 'al-ʿanṣara', 'al-ḥarṯ',
              'sumūm', 'al-ḥusūm', 'ibbāna',
              'yulyuh', 'yūliyūz', 'du-ǧanbira', 'djanbir', 'du-ǧanbrah', 'yanāyir',
              'yunyuh', 'yūnyuhin', 'aġušt', 'šutanbir', 'abrīl', 'māyuh', 'aktūbar',
              'fabrayr', 'šubāṭ', 'māris',
              'yab', 'mīma', 'kahh', 'dāl', 'kazz', 'kadd', 'yaz', 'ǧīm',
              'yā fahūm', 'yā fāhim', 'ḫalaqahū', 'rabbu-l-warā', 'ḥarṯu Ādama',
              'qīla', 'ṯamānūna', 'ḥusūm', 'ʿawnat aṭ-ṭullāb',
              'al-az-dilāf', 'iṭraḥna-hū sabʿan', 'al-ḥāǧūz',
              'ʿĪsā wulid', 'fa-stafid', 'sābiʿuhū', 'wulid',
              'vingt-quatre documents consécutifs', 'neuvième grande fente',
              'sans reconstruction', 'garde du traducteur', 'mots-nombres', 'GT-isme',
              'constante des treize', 'convention d\'inclusion',
              'Q 25', 'sourate 25', 'yattaḏakkar', 'yaḏkur', 'muṣḥaf du corpus',
              'p. 215', 'l\'annexe seconde',
              'dix-sept leçons restent']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 6, f"({html.count('fente')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
