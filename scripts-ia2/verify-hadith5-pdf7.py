#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-7 — vérification de la livraison hadith-5ep / pdf-7 (renforcement et application)
import json, re, sys

PATH = '/home/z/my-project/minhaj/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/minhaj/scripts-ia2/livraisons/hadith-5ep/pdf-7.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-7']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-7 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon 3 pages)', 5000 <= len(src) <= 9000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 6, f'(h2={src.count("<h2>")})')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Le texte', 'La compréhension', 'L’analyse', 'L’application',
       'La préparation de la leçon suivante']))
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 demi-anneau ayn (U+02BF/02BE)', '\u02bf' not in src and '\u02be' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?', src))
# — matière adjudiquée du manuel (Z2-7) —
for kw in ['<h1>Renforcement et application</h1>', 'da’m wa-t-taṭbīq', '(دعم وتطبيق)',
           'Septième leçon (7) du manuel', 'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'Évaluer mes acquisitions de savoir',
           'Éprouver mes capacités', 'incarner' if 'incarner' in src else 'Incarner les valeurs',
           'al-mukallaf', 'aš-šarī’a al-islāmiyya',
           'Sourate al-Mā’ida — verset 91', 'Sourate al-Bayyina — verset 5',
           'Sourate Ṭāhā — verset 14', 'Sourate at-Tawba — verset 14',
           'Sourate al-Ḥuǧurāt — verset 14',
           'frivolité dans vos serments', 'monothéistes purs',
           'n’entretient les mosquées d’Allah', 'Sers-Moi donc',
           'qawā’id' if 'qawā’id' in src else 'règles de l’īmān',
           'ce ne sont pas les paroles, mais les intentions',
           '’aqqadtum al-aymāna', 'ḥunafā’', 'lā yultikum min a’mālikum šay’an',
           'al-lafẓ', 'āṯārun ḥamīda', 'an-nubuwwa aṣ-ṣādiqa',
           'la prophétie véridique', 'la foi en les anges et en les messagers',
           'preuve de la Loi appropriée', 'Ǧibrīl', 'al-’a’dād al-qabliyya' if
           'al-’a’dād' in src else 'al-a’dād al-qabliyya',
           'bi-kitbi rizqihi', 'faysbiqu ’alayhi al-kitāb',
           'le Livre le devance', 'quatre paroles',
           'maṭwiyya', 'Tandis que nous étions assis auprès du Messager d’Allah',
           'Les actes ne valent qu’aux intentions']:
    check(f'matière: {kw}', kw in src)
# — pose —
check('htmlFr posé non vide (garde-doublon)', len(fr) > 4000, f'({len(fr)} car)')
check('htmlFr posé == fichier source', fr.strip() == src.strip(),
      f'({len(fr)} car posés vs {len(src)} source)')
check('titleFr (pré-existant du dépôt, conservé)', (l.get('titleFr') or '').strip() == 'Consolidation et application',
      f"({l.get('titleFr')!r})")
# — registre IA-2 —
reg = json.load(open('/home/z/my-project/minhaj/scripts-ia2/savant-registry-ia2.json',
                     encoding='utf-8'))
check('registre IA-2 contient hadith-5ep/pdf-7', 'hadith-5ep/pdf-7' in reg.get('hand', []),
      f'({len(reg.get("hand", []))} savants)')

print('\n'.join('OK  ' + o for o in ok))
if fail:
    print('\n'.join('ECHEC  ' + f for f in fail))
    sys.exit(1)
print(f'\nVERIF PASS — {len(ok)} contrôles OK / 0 échec — pdf-7 → {len(src)} car')
