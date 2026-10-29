# -*- coding: utf-8 -*-
"""build-19333.py — assemblage de la leçon 19333 (le ẓuhr et le ʿaṣr par le ẓill du Soleil) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19333_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19333.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : la connaissance du temps du ẓuhr et du ʿaṣr par le ẓill du Soleil' in html, f"(h1={html.count('<h1>')})")
sonde('badge Leçon 21 / 28', 'Leçon 21 / 28' in html)
sonde('dl 4 dt / 4 dd (datée)', html.count('<dt>') == 4 and html.count('<dd>') == 4, f"({html.count('<dt>')}/{html.count('<dd>')})")
sonde('date de séance Lundi 15 janvier 2024', 'Lundi 15 janvier 2024' in html)
sonde('h2 x7', html.count('<h2>') == 7, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x2', html.count('<h4>') == 2, f"({html.count('<h4>')})")
sonde('ul x7', html.count('<ul>') == 7, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('tables matn x3', html.count('<table') == 3, f"({html.count('<table')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets appariés', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars at-tāsiʿ ʿašar', 'quatre-vingt-sixième', 'Leçon 21 / 28',
              'al-iʿdād al-qiblī', 'Notes du traducteur',
              'aš-šarḫ', 'istiḫlāṣ maḍāmīn', 'al-matn', 'al-fahm',
              'at-taḥlīl', 'at-taqwīm', 'al-istitmār',
              'ṣufūf', 'fardā', 'qāma', 'ašbār', 'aqdām', 'zawāl', 'mankūs', 'mabsūṭ', 'ǧummal',
              '(ṭazah, ǧabā, abdahu, ḥayy)', '(ḥawd, ǧabā, abǧad, waḥ)',
              'maʿa sabʿatin li-l-ʿaṣr', 'wa-kil', 'ʿallim', 'fī mustawin qif',
              'yanāyir', 'fabrāyir', 'māris', 'ibrīl', 'yūnyū', 'yūlyūz', 'ġušt', 'uktūbar', 'nūnbir', 'dganbir',
              'Ibn Ḥabīb', 'Ibn al-Bannā', 'ar-Rasmūkī', 'as-Samlālī', 'al-Ilġī',
              'Kifāyat ḏawī l-albāb', 'Rawḍat al-azhār', 'ibn al-Muwāṣṣī',
              'Balmakkī al-Būǧrafāwī', 'Al-Badr aṭ-ṭāliʿ fī īḍāḥ maqāṣid al-Muqniʿ',
              'al-Ḫaṭṭābī', 'ʿIlm al-mawāqīt', 'madhhab de Mālik',
              'vingtième grande fente', 'la garde', 'ne reconstruit pas',
              'al-Furqān 25:45', 'dalīl', 'sākinā', 'cache du Qorʾān',
              'deux documents d’une même séance', 'az-zawāl', 'ṭāliʿ al-layl', 'as-saḥūr',
              'al-manzil al-mutawassiṭ', 'GT-isme', 'logarithme', '9-7-5-3-2-1-1-2-4-5-8-10',
              '8-6-4-3-2-1-1-2-3-4-6-8', 'sept pieds', 'Les āyāt']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td', 'span']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 3, f"({html.count('fente')})")
sonde('déroulés de la garde', html.count('déroule') >= 2, f"({html.count('déroule')})")
sonde('GT-ismes cités en N.d.T.', all(t in html for t in ['« Timing »', '« midi »', '« Yunir »', '« un quart de la hauteur »', '« Al-Mu’tami']))
sonde('non-reconstruction affichée', 'ne reconstruit pas' in html)
sonde('le Maître (pas le Master)', 'Le Master' not in html and 'Master' not in html)

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
