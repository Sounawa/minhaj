# -*- coding: utf-8 -*-
"""build-19229.py — assemblage de la leçon 19229 (les jours importants de l'année arabe) + sondes."""
import re, sys

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr19229_{i}.html', encoding='utf-8').read() for i in range(1, 6)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/19229.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le tawqīt : les jours importants de l\u2019année arabe' in html)
sonde('badge Leçon 6 / 28', 'Leçon 6 / 28' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x8', html.count('<h2>') == 8, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('h4 x2', html.count('<h4>') == 2, f"({html.count('<h4>')})")
sonde('h5 x2', html.count('<h5>') == 2, f"({html.count('<h5>')})")
sonde('ul x13 (citations interrompues, fidèle à la source)', html.count('<ul>') == 13, f"({html.count('<ul>')})")
sonde('ol x1 (N.d.T.)', html.count('<ol>') == 1)
sonde('N.d.T. li x11', html.count('<li><p>') == 11, f"({html.count('<li><p>')})")
sonde('table x6', html.count('<table') == 6, f"({html.count('<table')})")
sonde('tr x19 / td x57', html.count('<tr>') == 19 and html.count('<td>') == 57, f"({html.count('<tr>')}/{html.count('<td>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets apparies', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
refs = re.findall(r'\(9\s?:36\)', html)
sonde('ref 9:36 x2 (flow + N.d.T.)', len(refs) == 2, f'({len(refs)})')
for terme in ['Manẓūmat al-Muqniʿ', 'al-Marġatī', 'al-Malṭaʿ ʿalā masāʾil al-Muqniʿ',
              'ṣallā ʿalayhi llāhu laylatan (ya-bī)', 'afḍalu mā fī l-ʿāmi mawlidu n-nabī',
              'fīhi atā Ṭaybata ḫayri mursalī', 'min yawmi ṯ-ṯanīni Rabīʿi l-awwal',
              'wa-(yā) muḥarramika ʿāšūrāʾ', 'wa-mawtuhu fīhi kaḏā l-isrāʾ',
              'fīhi tazīdu bi-himā l-arzāqu', 'aw tāsiʿun wa-ṣ-ṣawmu wa-l-infiqā',
              'fīhi l-Ḫalīla, wa-l-Kalīma Mūsā', 'wa-qā ilāhunā l-Karīmu būsā',
              'Ayyūba, Yūnusa wa-Nūḥan, ʿĪsā', 'Ādama, Dāwūda, bnahū, Idrīsā',
              'wa-(ḥāʾi) ḥiǧǧati wa-(kazzi) raǧabi', 'fī ṣawmi ṯāliṯi l-muḥarrami rġabi',
              'wa-niṣfi šaʿbāna rawā ḏū l-maʿrifah', 'wa-(kahhi) qiʿdatin wa-yawmi ʿarafah',
              'wa-Raǧabu l-fardu: šuhūrun ḥurum', 'ḏū qiʿdatin, ḏū ḥiǧǧatin, muḥarram',
              'lā yatawālā n-naqṣu fī akṭara min', 'ṯalāṯatin min aš-šuhūri yā faṭin',
              'kaḏā tawālī ḫamsatin mukammala', 'hāḏā ṣ-ṣawābu wa-siwāhu abṭalahu',
              'Inna ʿiddata š-šuhūri ʿinda llāhi iṯnā ʿašara šahrān', '(9 :36)',
              'ad-dars ar-rābiʿ', 'vingtième document consécutif', 'soixante-et-onzième',
              'quatrième grande fente', 'fihrist des œuvres', 'rubʿ al-muǧīb',
              'maḥāq', 'al-Badr aṭ-ṭāliʿ fī īḍāḥ maqāṣid al-Muqniʿ', 'Bilmakkī', 'p. 14',
              'sabāṭ', 'al-ǧabha', 'ʿaǧmiyya', 'basīṭ', 'kabīs', 'ṯāliṯāt',
              'al-ašhur al-ḥurum', 'al-ašhur al-ḥalāl', 'aš-šuhūr al-fardiyya', 'aš-šuhūr az-zawǧiyya',
              'sans reconstruction', 'al-iʿdād al-qiblī', 'at-taḥlīl', 'istiḫlāṣ',
              'Ṭayba', 'ʿĀšūrāʾ', 'mawlid', 'kabis de ḏū al-ḥiǧǧa', 'ʿArafa',
              'Leçon 6 / 28', 'vingt-deux leçons restent']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('fentes documentées', html.count('fente') >= 8, f"({html.count('fente')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
