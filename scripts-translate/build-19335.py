# -*- coding: utf-8 -*-
"""build-19335.py — assemblage de la leçon 19335 (les heures, le ṭāliʿ, la manzila moyenne) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19335_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19335.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : la connaissance des heures, du ṭāliʿ et de la manzila moyenne du ciel au maġrib, à lʿišāʾ, au saḥūr et au faǧr' in html, f"(h1={html.count('<h1>')})")
sonde('badge Leçon 22 / 28', 'Leçon 22 / 28' in html)
sonde('dl 4 dt / 4 dd', html.count('<dt>') == 4 and html.count('<dd>') == 4, f"({html.count('<dt>')}/{html.count('<dd>')})")
sonde('champ date vide porté', 'Sans date' in html)
sonde('h2 x7', html.count('<h2>') == 7, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x4', html.count('<h4>') == 4, f"({html.count('<h4>')})")
sonde('h5 x1 (exemple illustratif)', html.count('<h5>') == 1, f"({html.count('<h5>')})")
sonde('ul x5', html.count('<ul>') == 5, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('tables matn x5', html.count('<table') == 5, f"({html.count('<table')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets appariés', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars al-ʿišrūn', 'quatre-vingt-septième', 'Leçon 22 / 28',
              'al-iʿdād al-qiblī', 'Notes du traducteur',
              'aš-šarḫ', 'istiḫlāṣ maḍāmīn', 'al-matn', 'al-fahm',
              'at-taḥlīl', 'at-taqwīm', 'al-istitmār',
              '(mab)', 'ṭāliʿ', 'manzila moyenne', 'saḥūr', 'ḍiyāʾ al-faǧr', 'zamāniyya',
              'naẓīr', 'maḍā', 'baqī', 'manzilin wa-s-sudsi', 'wa-l-«hāʾ» minhā maġriban wasaṭan',
              'an-naṭḥ', 'al-buṭayn', 'aṯ-ṯurayyā', 'ad-dabarān', 'al-haqʿa', 'al-hanaʿa', 'aḏ-ḏirāʿ',
              'as-simāk', 'al-ġafr', 'baṭn al-ḥūt',
              'Coup de corne', 'Petit Ventre', 'Pléiades', 'Suiveur', 'Tache blanche', 'Marque au cou', 'Bras',
              'Pilier', 'Couverture', 'abǧad', 'ḥāʾ', 'yāʾ', '(ḥayy)', '(kāf)',
              '14/12 = 7/6', 'quarante-deux', 'sept fois six',
              'Abū Maqriʿ', 'p. 202, annexe 1', 'al-ġazāl al-lāmiʿ', 'gazelle rayonnante',
              'vingt-et-unième grande fente', 'la garde', 'ne reconstruit pas',
              'al-Isrāʾ 17:12', 'mubṣiratan', 'maḥawnā', 'cache du Qorʾān', 'Yūnus 10:5',
              'Lundi 15 janvier 2024', 'al-maǧmūʿa aš-šamsiyya', 'astronomie contemporaine',
              'ar-raqīb', 'GT-isme', 'les manāzil du Soleil']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td', 'span']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 3, f"({html.count('fente')})")
sonde('déroulés de la garde', html.count('déroule') >= 2, f"({html.count('déroule')})")
sonde('GT-ismes cités en N.d.T.', all(t in html for t in ['« Timing »', '« l’horoscope »', '« le grammairien »', '« foin »', '« assez »', '« iḥfaẓhu imāman »', '« Al-Muqinʿ »']))
sonde('non-reconstruction affichée', 'ne reconstruit pas' in html)
sonde('déroulé étiqueté de la garde', 'Le déroulé est de la garde, les codes sont du livre' in html)

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
