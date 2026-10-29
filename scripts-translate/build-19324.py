# -*- coding: utf-8 -*-
"""build-19324.py — assemblage de la leçon 19324 (la connaissance du burj de la Lune) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19324_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19324.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 2 and 'Le tawqīt : la connaissance du burj de la Lune' in html, f"(h1={html.count('<h1>')} dont 1 vide = fente)")
sonde('badge Leçon 20 / 28', 'Leçon 20 / 28' in html)
sonde('dl 4 dt / 4 dd (datée)', html.count('<dt>') == 4 and html.count('<dd>') == 4, f"({html.count('<dt>')}/{html.count('<dd>')})")
sonde('date de séance Lundi 15 janvier 2024', 'Lundi 15 janvier 2024' in html)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x4', html.count('<h4>') == 4, f"({html.count('<h4>')})")
sonde('h5 x2', html.count('<h5>') == 2, f"({html.count('<h5>')})")
sonde('h6 x2', html.count('<h6>') == 2, f"({html.count('<h6>')})")
sonde('ul x8', html.count('<ul>') == 8, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('tables matn x8', html.count('<table') == 8, f"({html.count('<table')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets appariés', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars aṯ-ṯāmin ʿašar', 'quatre-vingt-cinquième', 'Leçon 20 / 28',
              'al-iʿdād al-qiblī', 'Notes du traducteur',
              'aš-šarḫ', 'istiḫlāṣ maḍāmīn', 'at-tamhīd', 'al-matn', 'al-fahm',
              'at-taḥlīl', 'at-taqwīm', 'al-istitmār',
              'manzila', 'manāzil', 'burj', 'burūǧ', 'hilāl', 'yulfā', 'yansalib', 'iqṭaʿā',
              'sunnah', 'lāyat aš-šakk', 'ihlāl', 'istihlāl',
              '(yadd)', '(yahh)', '(kaḥ)', 'ǧummal',
              'baṭn al-ḥūt', 'aṭ-ṭarf', 'al-qalb', 'al-ḥūt', 'as-saraṭān', 'al-ʿaqrab',
              'ḏū-l-qaʿda 1417', 'muḥarram 1417', 'saʿd as-suʿūd', 'yanāyir', 'yūlyūz',
              'méridional montant', 'septentrional descendant', 'méridional descendant',
              'Balmakkī al-Būǧrafāwī', 'Al-Badr aṭ-ṭāliʿ fī īḍāḥ maqāṣid al-Muqniʿ',
              'badr', 'muḥāq', 'iǧtimāʿ', 'istiqbāl', 'šuʿāʿ', 'aḥwāl',
              'ẓill aẓ-ẓuhr', 'ẓill al-ʿaṣr', '(ṭazah)', '(ǧabā)', '(abdahu)', '(ḥayy)',
              'dix-neuvième grande fente', 'la garde', 'Maṭbaʿat al-Amniyya',
              'Yūnus 10:5', 'ḍiyāʾ', 'nūr', 'cache du Qorʾān',
              'Lundi 08 janvier 2024', 'deux documents d’une même séance',
              'GT-isme', 'quarante-huit minutes', 'deux manāzil et un tiers']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tr', 'td']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 3, f"({html.count('fente')})")
sonde('déroulés de la garde', html.count('déroule') >= 2, f"({html.count('déroule')})")
sonde('GT-ismes cités en N.d.T.', all(t in html for t in ['« un an »', '« son horoscope »', '« son statut »', '« Cela enlève »', '« Heure »']))
sonde('fente h1 vide portée', '<h1></h1>' in html)
sonde('non-reconstruction affichée', 'ne reconstruit pas' in html)

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
