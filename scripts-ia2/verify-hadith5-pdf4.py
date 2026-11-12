#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-4 — vérification de la livraison hadith-5ep / pdf-4 (l’excellence et les signes de l’Heure)
import json, re, sys

PATH = '/home/z/my-project/repo-minhaj/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/repo-minhaj/scripts-ia2/livraisons/hadith-5ep/pdf-4.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-4']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-4 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent', 9000 <= len(src) <= 14000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2/h3', src.count('<h2>') == 9 and src.count('<h3>') == 9,
      f'(h2={src.count("<h2>")}, h3={src.count("<h3>")})')
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 demi-anneau ayn (U+02BF/02BE)', '\u02bf' not in src and '\u02be' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?', src))
for kw in ['Jibrīl', '’Umar ibn al-Khaṭṭāb', 'Ṣaḥīḥ de Muslim',
           '<h1>L’excellence et les signes de l’Heure</h1>', 'al-iḥsān',
           'Quatrième leçon (4) du manuel',
           'Sourate Luqmān — verset 33', 'Sourate an-Naḥl — verset 128',
           'Sourate al-Baqara — verset 194', 'Sourate Yūnus — verset 26',
           'Ikmāl ikmām al-mu’allim', 'qāḍī',
           'mušāhada', 'murāqaba', 'itqān', 'taǧawwud',
           'la servante enfante sa maîtresse',
           'ḥāfi’', '’ārī', '’ā’il', 'rā’ī', 'aš-šā’',
           'deux degrés', 'trois stations',
           'la fréquence de l’ingratitude filiale',
           'Mémorise le hadīth suivant',
           'sa notice biographique a été présentée']:
    check(f'matière: {kw}', kw in src)
# — pose —
check('htmlFr posé non vide (garde-doublon)', len(fr) > 5000, f'({len(fr)} car)')
check('htmlFr posé == fichier source', fr.strip() == src.strip(),
      f'({len(fr)} car posés vs {len(src)} source)')

print('\n'.join('OK  ' + o for o in ok))
if fail:
    print('\n'.join('ECHEC  ' + f for f in fail))
    sys.exit(1)
print(f'\nVERIF PASS — {len(ok)} contrôles OK / 0 échec — pdf-4 → {len(src)} car')
