#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-2 — vérification de la livraison hadith-5ep / pdf-2
import json, re, sys

PATH = '/home/z/my-project/repo-minhaj/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/repo-minhaj/scripts-ia2/livraisons/hadith-5ep/pdf-2.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-2']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-2 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent', 8500 <= len(src) <= 15000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2/h3/h4', src.count('<h2>') == 9 and src.count('<h3>') == 5,
      f'(h2={src.count("<h2>")}, h3={src.count("<h3>")})')
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?', src))
for kw in ['’Umar ibn al-Khaṭṭāb', 'muttaqun ’alayhi', 'trois genres',
           'i’tikāf', 'ẓuhr', 'Umm Qays', 'Ṭabarānī', 'Abū Hurayra',
           'riyā’', 'aṭ-Ṭabarānī', 'Ṣaḥīḥ de Muslim', 'ṭala’a ’alaynā',
           'les piliers de la foi', 'Nufayl', '23 de l’Hégire']:
    check(f'matière: {kw}', kw in src)
# — pose —
check('htmlFr posé non vide (garde-doublon)', len(fr) > 5000, f'({len(fr)} car)')
check('htmlFr posé == fichier source', fr.strip() == src.strip(),
      f'({len(fr)} car posés vs {len(src)} source)')

print('\n'.join('OK  ' + o for o in ok))
if fail:
    print('\n'.join('ECHEC  ' + f for f in fail))
    sys.exit(1)
print(f'\nVERIF PASS — {len(ok)} contrôles OK / 0 échec — pdf-2 → {len(src)} car')
