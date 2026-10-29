# -*- coding: utf-8 -*-
"""build-19281.py — assemblage de la leçon 19281 (l'écoulé du mois en absolu et les deux ères) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19281_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19281.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : l’écoulé du mois en absolu et l’extraction de l’année arabe depuis l’année milādī et l’inverse' in html)
sonde('badge Leçon 14 / 28', 'Leçon 14 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x5', html.count('<h4>') == 5, f"({html.count('<h4>')})")
sonde('h5 x8', html.count('<h5>') == 8, f"({html.count('<h5>')})")
sonde('ul x7', html.count('<ul>') == 7, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('N.d.T. li x15', html.count('<li><p>') == 15, f"({html.count('<li><p>')})")
sonde('li total x36', html.count('<li>') == 36, f"({html.count('<li>')})")
sonde('table x7', html.count('<table') == 7, f"({html.count('<table')})")
sonde('tr x15 / td x45', html.count('<tr>') == 15 and html.count('<td>') == 45, f"({html.count('<tr>')}/{html.count('<td>')})")
sonde('4 fentes <p></p>', html.count('<p></p>') == 4, f"({html.count('<p></p>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets appariés', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
# pointillés de la source (rasm portés tels quels)
sonde('pelotons 41 x5', html.count('.' * 41) == 5, f"({html.count('.' * 41)})")
sonde('pelotons >= 20 exacts x5', len(re.findall(r'(?<!\.)\.{20,}(?!\.)', html)) == 5, f"({[len(m.group(0)) for m in re.finditer(r'(?<!\.)\.{20,}(?!\.)', html)]})")
sonde('PRE18 wa-in lam yuʿlami', '.' * 18 + ' wa-in lam yuʿlami' in html)
sonde('POST16 ussaka wa-l-ayyāma', 'ussaka wa-l-ayyāma' + '.' * 16 in html)
sonde('PRE17 wa-z-zāʾida ʿan', '.' * 17 + ' wa-z-zāʾida ʿan' in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars aṯ-ṯānī ʿašar', 'soixante-dix-neuvième', 'Leçon 14 / 28',
              'at-tamhīd', 'al-fahm', 'at-taḥlīl', 'at-taqwīm', 'al-istitmār',
              'al-iʿdād al-qiblī', 'istiḫlāṣ maḍāmīn', 'aš-šarḫ', 'matn', 'naẓim',
              'bayt', 'ʿaǧmiyya', 'yanāyir', 'yannayrinā', 'ussunā',
              'ʿannā', 'rafaḍa', 'subāṭ', 'fabrāyir', 'fabrīr',
              'ibrīl', 'abrīl', 'māyuh', 'yūnyuh', 'yunīh', 'yanīh',
              'yūliyūz', 'aġušt', 'šutanbar', 'uktūbar', 'nūnbar', 'mars',
              'az-dilāf', 'az-dilāfāt', 'qāʾid', 'asūs', '653', '1395',
              '33', '32', '622', '1441', '2020', '1420', '1417', '1997',
              '1410', '1372', '1953', '1975', '1999', '2322', '2330', '1431', '1440',
              'muharram', 'ṣafar', 'ramaḍān', 'ḏū-l-ḥiǧǧa', 'ǧumādā I', 'rabīʿ II',
              'kaḥ', 'kāf', 'ḥāʾ', 'lām', 'abjad', 'ǧummal',
              'fāza raǧulun', 'tāba muqirrun', 'falaḥī', 'falaḥiyya', 'milādī',
              'hégirienne', 'iʿtidālān', 'inqilābān', 'mṭlq', 'qawluhum',
              'douzième grande fente', 'vingt-sept documents consécutifs', 'GT-isme',
              'quatorze leçons restent', 'sans unification']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 6, f"({html.count('fente')})")
sonde('notes N.d.T. présentes', html.count('Notes du traducteur') == 1)

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
