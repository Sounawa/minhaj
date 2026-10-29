# -*- coding: utf-8 -*-
"""build-20048.py — assemblage de la leçon 20048 (faṣl al-mīm 2, bayts 118-123) + sondes."""
import re, sys, unicodedata

HOME = '/home/z/my-project'
parts = [open(f'{HOME}/tr-tmp/fr20048_{i}.html', encoding='utf-8').read() for i in range(1, 6)]
html = '\n'.join(p.strip() for p in parts) + '\n'
open(f'{HOME}/tr-tmp/20048.html', 'w', encoding='utf-8').write(html)

ok = 0; ko = 0
def sonde(label, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print(f'  OK   {label} {detail}')
    else: ko += 1; print(f'  FAIL {label} {detail}')

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')

n = len(html)
sonde('longueur >= 12000 car', n >= 12000, f'({n} car)')
sonde('h1 unique + titre', html.count('<h1>') == 1 and 'Le rasm et le ḍabṭ : le chapitre du mīm (2)' in html)
sonde('badge Leçon 28 / 30', 'Leçon 28 / 30' in html)
sonde('dl 3 dt / 3 dd', html.count('<dt>') == 3 and html.count('<dd>') == 3)
sonde('h2 x6', html.count('<h2>') == 6, f"({html.count('<h2>')})")
sonde('h3 x4', html.count('<h3>') == 4, f"({html.count('<h3>')})")
sonde('table x3', html.count('<table') == 3, f"({html.count('<table')})")
sonde('tr x11', html.count('<tr>') == 11, f"({html.count('<tr>')})")
sonde('td x22', html.count('<td>') == 22, f"({html.count('<td>')})")
sonde('N.d.T. ol x9 li', html.count('<li><p>') >= 9, f"({html.count('<li><p>')})")
sonde('0 arabe residuel', not ARABIC.search(html))
g1, g2 = html.count('«'), html.count('»')
sonde('guillemets apparies', g1 == g2, f'({g1}/{g2})')
sonde('0 apostrophe droite', "'" not in html)
refs = re.findall(r'\((\d{1,3}):(\d{1,3})\)', html)
sonde('refs versets >= 15', len(refs) >= 15, f'({len(refs)})')
sonde('refs uniques >= 20 (doublons legitimes texte+N.d.T.)', len(set(refs)) >= 20, f'({len(set(refs))} uniques / {len(refs)} totales)')
for terme in ['al-Waḏġīrī', 'ʿUmdat al-bayān', 'sīmāhum', 'ʿimāra', 'ṯamānī', 'yaqūmāni',
              'ar-Raḥḥālī', 'Tuhfat al-qurrāʾ', 'Tamhīd', 'Sijilmāsa', 'al-Muḥammadī',
              'al-Aʿrāf', 'al-Fatḥ', '(48:29)', '(5:107)', '(77:33)', '(27:30)', '(18:110)',
              'quinzième tour', 'bayts 118', 'iḥtirāzāt', 'ṯabt']:
    sonde(f'terme « {terme} »', terme in html)
for tag in ['h1', 'h2', 'h3', 'p', 'dl', 'dt', 'dd', 'ul', 'ol', 'li', 'table', 'tbody', 'tr', 'td']:
    o = len(re.findall(rf'<{tag}[ >]', html)); c = html.count(f'</{tag}>')
    sonde(f'balise {tag} appariée', o == c, f'({o}/{c})')
sonde('pas de descripteur inventé iʿdād', 'al-iʿdād al-qibliyy' not in html)
sonde('fentes marquées [', html.count('[la fente') + html.count('[fente') >= 6,
      f"({html.count('[la fente') + html.count('[fente')})")

print(f'\nSONDES: {ok} OK / {ko} FAIL — {n} car')
sys.exit(1 if ko else 0)
