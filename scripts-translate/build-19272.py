# -*- coding: utf-8 -*-
"""build-19272.py — assemblage de la leçon 19272 (l'entrée de yanāyir et l'az-dilāf) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19272_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19272.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : l’entrée de yanāyir et l’az-dilāf' in html)
sonde('badge Leçon 12 / 28', 'Leçon 12 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x4', html.count('<h4>') == 4, f"({html.count('<h4>')})")
sonde('h5 x2', html.count('<h5>') == 2, f"({html.count('<h5>')})")
sonde('ul x5', html.count('<ul>') == 5, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('N.d.T. li x15', html.count('<li><p>') == 15, f"({html.count('<li><p>')})")
sonde('li total x30', html.count('<li>') == 30, f"({html.count('<li>')})")
sonde('table x5', html.count('<table') == 5, f"({html.count('<table')})")
sonde('tr x17 / td x51', html.count('<tr>') == 17 and html.count('<td>') == 51, f"({html.count('<tr>')}/{html.count('<td>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets appariés', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
# pointillés de la source (rasm portés tels quels)
for dots, label in [(28, 'matn bayt 7'), (37, 'citation bayt 1 tr2'), (25, 'citation bayt 2 (après virgule)')]:
    sonde(f'pointillés {label} ({dots})', '.' * dots in html)
sonde('pelotons 36 exacts x4', len(re.findall(r'(?<!\.)\.{36}(?!\.)', html)) == 4, f"({len(re.findall(r'(?<!\\.)\\.{36}(?!\\.)', html))})")
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ad-dars al-ʿāšir', 'soixante-dix-septième', 'Leçon 12 / 28',
              'at-tamhīd', 'al-fahm', 'at-taḥlīl', 'at-taqwīm', 'al-istitmār',
              'al-iʿdād al-qiblī', 'istiḫlāṣ maḍāmīn', 'aš-šarḫ', 'matn', 'naẓim',
              'bayt', 'ʿaǧmiyya', 'falaḥī', 'yanāyir', 'yannayir',
              'al-az-dilāf', 'az-dilāfāt', 'iṭraḥna-hū sabʿan', 'al-ḥāǧūz',
              'muzdallaf', 'kabīs', 'Abū Maqrīʿ',
              'laǧǧ', 'šakh', 'sal wa-šid', 'muṭṭarid', 'maǧūz',
              'al-ʿIlmī', 'al-ʿIrāqī', 'manuscrites',
              'mā baʿda sabʿimiʾatin', 'wa-l-izdifāfa iṭraḥhu illā wāḥidā',
              'asqaṭahuš-šayḫu', 'wa-bdaʾ li-bāqin', 'taruk al-ḫāmisi al-maǧūzi',
              'bi-aḥadin taqif ʿalā-l-ḥāǧūzi', 'wa-l-izdifāfu kulla (laǧǧin) an yatimm',
              'taʿrifuhu min baʿdi tarḥi sal wa-šid', 'ḥaṭṭi-l-muzdallif',
              'dimanche', 'mardi', 'jeudi', 'vendredi',
              'dixième grande fente', 'sans reconstruction', 'garde du traducteur',
              'vingt-cinq documents consécutifs', 'GT-isme',
              'Q 21', 'Q 36', 'Q 10', 'sourate' if False else 'muṣḥaf du corpus',
              'kullun fī falakin yasbaḥūna', 'ʿadada-s-sinīna wa-l-ḥisāb',
              '717', '697', '871', '1040 h.', '1440 h.', '1417 h.', '2307 falaḥiyya',
              'seize leçons restent']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 4, f"({html.count('fente')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
