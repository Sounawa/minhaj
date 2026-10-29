# -*- coding: utf-8 -*-
"""build-19238.py — assemblage de la leçon 19238 (activités d'exploitation leçons 1-5) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19238_{i}.html', encoding='utf-8').read() for i in range(1, 6)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19238.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : les activités d’exploitation des apprentissages et de leur soutien (des leçons 1 à 5)' in html)
sonde('badge Leçon 8 / 28', 'Leçon 8 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x5', html.count('<h2>') == 5, f"({html.count('<h2>')})")
sonde('ul x4', html.count('<ul>') == 4, f"({html.count('<ul>')})")
sonde('li x22 (12 consignes + 10 N.d.T.)', html.count('<li>') == 22, f"({html.count('<li>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('N.d.T. li x10', html.count('<li><p>') == 10, f"({html.count('<li><p>')})")
sonde('table x0', html.count('<table') == 0, f"({html.count('<table')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets apparies', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars as-sādis', 'soixante-treizième', 'Leçon 8 / 28',
              'an-našāṭ al-awwal', 'an-našāṭ aṯ-ṯānī', 'an-našāṭ aṯ-ṯāliṯ', 'al-iʿdād al-qiblī',
              'al-Ḫaṭṭābī', 'ʿilm al-mawāqīt : uṣūluhu wa-manāhiǧuh', 'al-kura', 'aṣ-ṣafīḥa',
              'rubʿ al-muǧīb', 'muqanṭarāt', 'ḏāt al-kursī', 'bayt al-ibra',
              'Ibn ʿAṭiyya', 'al-Muḥarrar al-waǧīz', 'an-Naqqāš', '18 :25',
              'wa-labiṯū fī kahfihim ṯalāṯa miʾatin sinīna wa-zdādū tisʿā',
              'gens de la caverne', 'muṣḥaf du corpus', 'fente formelle', '9 :36',
              '309', '109 575', '354,36667', 'sund', 'onze jours',
              'qayd', 'sahṣ', '114', '365', '43', '1008', '1000', 'millier',
              '1382 h. — 2237 f. — 1404 h. — 2325 f.',
              'š — m-ǧ — ḥ-š — q-y-d — s-h-ṣ',
              'basīṭ', 'kabīs', 'basīṭa', 'kabīsa', 'ʿaǧmiyya', 'faṣl', 'manāzil', 'burūǧ',
              'crible de trente', 'crible de vingt-huit', '2, 5, 7, 10, 13, 15, 18, 21, 24, 26, 29',
              '3, 7, 11, 15, 19, 23, 27', 'lagnat murāqabat al-hilāl',
              'sixième grande fente', 'sans reconstruction', 'vingt-deuxième document consécutif',
              'mūraṯ al-maġribī', 'Abū Miqraʿ', 'al-Firklī', 'arǧūza', 'šarḫ',
              'kinyāya',
              'istiṯmār', 'al-istitmār', 'mots-nombres', 'vingt leçons restent']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 8, f"({html.count('fente')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
