# -*- coding: utf-8 -*-
"""build-19237.py — assemblage de la leçon 19237 (les jours de l'année ʿaǧmiyya) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19237_{i}.html', encoding='utf-8').read() for i in range(1, 6)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19237.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : les jours de l\u2019année ʿaǧmiyya' in html)
sonde('badge Leçon 7 / 28', 'Leçon 7 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x5', html.count('<h4>') == 5, f"({html.count('<h4>')})")
sonde('h5 x4', html.count('<h5>') == 4, f"({html.count('<h5>')})")
sonde('ul x6', html.count('<ul>') == 6, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('N.d.T. li x11', html.count('<li><p>') == 11, f"({html.count('<li><p>')})")
sonde('table x5', html.count('<table') == 5, f"({html.count('<table')})")
sonde('tr x7 / td x21', html.count('<tr>') == 7 and html.count('<td>') == 21, f"({html.count('<tr>')}/{html.count('<td>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets apparies', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ayyāmuhā (sahṣ) wa-rubʿun kabsā', 'wa-zādahu r-Rūmu (subāṭa) ḥissā',
              'fa-l-faṣlu fī l-qawlayni (fayʾun) ʿadadā', 'wa-rubʿu yawmin muṭlaqan qad wuǧidā',
              'wa-zādahu fī ṣ-ṣayfi baʿḍun fa-aqāma', 'aš-šamsa fī l-Ǧabhati (yaddan) bi-l-iltizām',
              'kabāʾisu r-Rūmi turā fī ǧazzi', 'ya-ʾi, yahi, yaṭi, kaǧǧi, wa-kazzi',
              'ad-dars al-ḫāmis', 'vingt-et-unième document consécutif', 'soixante-douzième',
              'cinquième grande fente', 'ʿaǧmiyya', 'basīṭ', 'kabīs', 'kabīsa', 'basīṭa',
              'sabāṭ', 'al-ǧabha', 'al-Ǧabha', 'manāzil', 'manzila', 'ʿilm al-anwāʾ',
              'rūmiyya falaḥiyya', 'šamsiyya', 'falaḥiyya', 'al-Yūnāniyyūn', 'al-Iskandariyyūn',
              'dīsambil', 'uktūbar', 'yanāyir', 'fībrāyir', 'kalāʾ', 'ḥissā', 'kabsā',
              'kinyāya', 'sans reconstruction', 'al-iʿdād al-qiblī', 'at-taḥlīl', 'istiḫlāṣ',
              'at-taqwīm', 'al-istitmār', 'at-tamhīd', 'aš-šarḥ', 'Leçon 7 / 28',
              'vingt-et-une leçons restent', 'troisième démonstration', 'mots-sont-des-nombres',
              'quatre-vingt-onze', 'trois cent soixante-cinq', 'quatre-vingt-douze',
              'vingt-huit jours', 'vingt-neuf jours', 'trente-deux jours', 'quatorze jours',
              'onze jours', 'sund', 'fihrist', 'rubʿ al-muǧīb', 'tableau maître des ǧummal',
              'front du Lion', 'fārisiyya', 'Yūnāniyyūn', 'Iskandariyyūn']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 6, f"({html.count('fente')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
