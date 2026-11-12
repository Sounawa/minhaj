#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-6 — vérification de la livraison hadith-5ep / pdf-6 (les phases de la création de l’homme)
import json, re, sys

PATH = '/home/z/my-project/repo-minhaj/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/repo-minhaj/scripts-ia2/livraisons/hadith-5ep/pdf-6.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-6']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-6 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent', 9000 <= len(src) <= 14000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2/h3', src.count('<h2>') == 9 and src.count('<h3>') == 5,
      f'(h2={src.count("<h2>")}, h3={src.count("<h3>")})')
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 demi-anneau ayn (U+02BF/02BE)', '\u02bf' not in src and '\u02be' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?', src))
for kw in ['’Abdullāh ibn Mas’ūd', '<h1>Les phases de la création de l’homme</h1>',
           'aṭwār ḫalq al-’insān', 'Sixième leçon (6) du manuel',
           'aṣ-ṣādiq al-maṣdūq', 'Ṣaḥīḥ de al-Buḫārī et Muslim',
           'quatre paroles', 'malheureux ou heureux', 'le Livre le devance',
           'Ibn Umm ’Abd', 'Musnad d’Ibn Abī Šayba', '32 ou 33 de l’Hégire',
           'al-Huḏalī', 'porteur de ses sandales',
           'Sourate Nūḥ — versets 17-18', 'Sourate al-Mu’minūn — versets 12-14',
           'Sourate al-Ḥaǧǧ — verset 5',
           'trois ténèbres', 'quarante jours', 'cent vingt jours',
           'an-nuṭfa', 'al-muḍġa', '’alaqa', 'ar-rūḥ',
           'l’unification du dispersé', 'la véracité de la Résurrection',
           'ad-da’m wa-t-taṭbīq',
           'Mémorise' if 'Mémorise' in src else 'Lis le texte du soutien']:
    check(f'matière: {kw}', kw in src)
# — pose —
check('htmlFr posé non vide (garde-doublon)', len(fr) > 5000, f'({len(fr)} car)')
check('htmlFr posé == fichier source', fr.strip() == src.strip(),
      f'({len(fr)} car posés vs {len(src)} source)')

print('\n'.join('OK  ' + o for o in ok))
if fail:
    print('\n'.join('ECHEC  ' + f for f in fail))
    sys.exit(1)
print(f'\nVERIF PASS — {len(ok)} contrôles OK / 0 échec — pdf-6 → {len(src)} car')
