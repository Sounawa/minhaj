# -*- coding: utf-8 -*-
"""build-19295.py — assemblage de la leçon 19295 (la manzila du Soleil) + sondes."""
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
sonde('li total x27 (14 corps + 13 notes)', html.count('<li>') == 27, f"({html.count('<li>')})")
sonde('tables x4 (1 matn + 2 citations + 1 poème)', html.count('<table') == 4, f"({html.count('<table')})")
sonde('matn-table x3 (dir=ltr)', html.count('<table dir="ltr" class="matn-table">') == 3)
sonde('poème sans dir x1', html.count('<table>\n<tbody>') == 1 or re.search(r'<table>\s*<tbody>', html) is not None)
sonde('tr x9', html.count('<tr>') == 9, f"({html.count('<tr>')})")
sonde('td x27', html.count('<td>') == 27, f"({html.count('<td>')})")
sonde('1 fente <p></p> stricte (exemple a)', html.count('<p></p>') == 1, f"({html.count('<p></p>')})")
sonde('3 fentes <p><span></span></p>', html.count('<p><span></span></p>') == 3, f"({html.count('<p><span></span></p>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets appariés', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars ar-rābiʿ ʿašar', 'quatre-vingt-unième', 'Leçon 16 / 28',
              'al-iʿdād al-qiblī', 'Notes du traducteur',
              'manzila', 'manāzil', 'faṣl', 'burj', 'burūǧ', 'falak',
              'al-jabha', 'la Jabha', 'aṯ-ṯurayyā', 'les Pléiades', 'an-naʿāʾim',
              'al-ʿawwā', 'farġ al-muqaddam', 'farġ al-muʾaḫir', 'baṭn al-ḥūt',
              'an-naṭḥ', 'al-buṭayn', 'ad-dabarān', 'al-haqʿa', 'aš-šawla',
              'aṣ-ṣarfa', 'al-qalb', 'al-iklīl', 'al-balda', 'al-aḫbiya',
              'fabrāyir', 'mars', 'ibrīl', 'māyuh', 'gusht', 'nūnbar',
              'duǧanbar', 'šutanbar', 'falaḥī',
              '(jīm)', '(yajj)', '(yadd)', '(jīman)',
              '365', '364', '92', '91', 'soixante-quatorze', 'soixante-dix-sept',
              '15 fabrāyir', '12 fabrāyir', '17 māyuh', '17 gusht', '16 nūnbar',
              '29 ibrīl', '26 nūnbar', '29 gusht', '14 gusht', '13 nūnbar',
              'Idrīs al-ʿIrāqī', 'aṭ-Ṭāhirī', 'Muḥammad ibn ʿAbd as-Salām',
              'quatorzième grande fente', 'vingt-neuf documents consécutifs',
              'GT-isme', 'Sixième état', 'muṣḥaf', 'az-dilāf',
              'naẓm', 'iʿtidāl', 'inqilāb', 'ḥarakāt',
              'muqaddam al-farġayn', 'que Dieu le Très-Haut lui fasse miséricorde',
              'falāḥīn', 'ahl ar-raṣd']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td', 'span']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 5, f"({html.count('fente')})")
sonde('déroulés de la garde', html.count('déroulé') >= 4, f"({html.count('déroulé')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
