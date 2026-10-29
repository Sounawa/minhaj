# -*- coding: utf-8 -*-
"""build-19257.py — assemblage de la leçon 19257 (iʿtidālān, inqilābān, ḥarakat al-iqbāl) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19257_{i}.html', encoding='utf-8').read() for i in range(1, 6)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19257.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : les deux iʿtidālān, les deux inqilābān et ḥarakat al-iqbāl' in html)
sonde('badge Leçon 10 / 28', 'Leçon 10 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x6', html.count('<h4>') == 6, f"({html.count('<h4>')})")
sonde('h5 x3', html.count('<h5>') == 3, f"({html.count('<h5>')})")
sonde('ul x12', html.count('<ul>') == 12, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('N.d.T. li x13', html.count('<li><p>') == 13, f"({html.count('<li><p>')})")
sonde('li total x38', html.count('<li>') == 38, f"({html.count('<li>')})")
sonde('table x10', html.count('<table') == 10, f"({html.count('<table')})")
sonde('tr x17 / td x51', html.count('<tr>') == 17 and html.count('<td>') == 51, f"({html.count('<tr>')}/{html.count('<td>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets apparies', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars aṯ-ṯāmin', 'soixante-quinzième', 'Leçon 10 / 28',
              'at-tamhīd', 'al-fahm', 'at-taḥlīl', 'at-taqwīm', 'al-istitmār',
              'al-iʿdād al-qiblī', 'istiḫlāṣ maḍāmīn al-matn', 'aš-šarḫ', 'matn', 'naẓim',
              'bayt', 'ʿaǧmiyya', 'falaḥī', 'faṣl',
              'iʿtidālān', 'inqilābān', 'al-iʿtidāl', 'al-inqilāb', 'ḥarakat al-iqbāl',
              'al-idbār', 'taʿdīl', 'raṣd',
              'māris', 'šutanbir', 'djanbir', 'yunyuh',
              'yaww', 'yawwi', 'yāʾi', 'iškāl', 'bulyā', 'taḫtabir',
              'Abū Maqrūf', 'falak', 'raʾs al-ḥamal', 'nuqtat', 'munṭabaʿ',
              'ḥaǧǧat al-wadāʿ', 'al-Buḫārī', 'Abū Bakra Nufayʿ b. al-Ḥāriṯ',
              'ḏū l-qaʿda', 'ḏū l-ḥiǧǧa', 'al-muḥarram', 'raǧabu muḍar', 'ǧumādā', 'šaʿbān',
              'Bil-ḥāǧǧ', 'Bil-makkī', 'al-Būǧarafāwī', 'ʿAbd ar-Razzāq', 'al-Badr aṭ-ṭāliʿ',
              'ʿIlm at-tawqīt wa-l-handasa al-falakiyya al-kurawiyya',
              'sāʿa', 'qiṭʿa', '2292 falaḥī', 'p. 68', 'p. 70', 'p. 91', 'p. 188',
              '1189', '1384', '1078', '706', '844', '1205', '1417',
              '1089', '717', '631', '1441', '1200', '1395', '855', '1216', '1428',
              'soixante-quatorze', 'vingt-trois documents consécutifs',
              'huitième grande fente', 'sans reconstruction', 'garde du traducteur',
              'mots-nombres', 'GT-isme', 'coups d’État',
              'rāʾ', 'ḫāʾ', 'ṣād', 'wāw', 'al-lyālī', 'as-samāʾim', 'ayyām muhimmāt',
              'lundi 25 décembre 2023', 'chaque degré un jour', '25 māris falaḥī',
              'dix-huit leçons restent']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 8, f"({html.count('fente')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
