#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-8 — vérification de la livraison hadith-5ep / pdf-8 (le décret et la prédestination)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-8.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-8']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-8 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon 6 pages)', 9000 <= len(src) <= 17000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 10, f'(h2={src.count("<h2>")})')
check('sous-sections h3', src.count('<h3>') == 5, f'(h3={src.count("<h3>")})')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Exorde', 'Le texte', 'Notice biographique du transmetteur',
       'La compréhension', 'Glossaire', 'Extraction des contenus', 'L’analyse',
       'Premièrement', 'Deuxièmement', 'Troisièmement',
       'Ce qu’il faut retirer du hadīth', 'L’évaluation', 'La valorisation',
       'La préparation de la leçon suivante']))
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 demi-anneau ayn (U+02BF/02BE)', '\u02bf' not in src and '\u02be' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?', src))
# — matière adjudiquée du manuel (Z2-8) —
for kw in ['<h1>Le décret et la prédestination (qaḍā’ et qadar)</h1>',
           'al-qaḍā’ wa-l-qadar', '(الْقَضَاءُ وَالْقَدَر)',
           'Huitième leçon (8) du manuel', 'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'tamhīd', 'an-naṣṣ', 'tarǧamat ar-rāwī',
           'al-fahm', 'istikhlāṣ al-maḍāmīn', 'at-taḥlīl', 'at-taqwīm',
           'al-istiṯmār', 'al-a’dād al-qabliyya',
           'fā’il muḫtār', 'aṣ-ṣādiq al-maṣdūq',
           'ḥattā mā yakūna baynahu wa-baynahā illā dirā’an',
           'faysbiqu ’alayhi al-kitāb',
           'quarante jours', 'goutte de semence', 'adhérence de sang', 'chair mâchée',
           'souffle vital', 'quatre paroles',
           "l’inscription de sa subsistance, son terme, son œuvre",
           'malheureux ou heureux',
           "l’œuvre des gens du Paradis", "l’œuvre des gens du Feu",
           "qu’une coudée", 'le Livre le devance',
           'Ṣaḥīḥ de al-Buḫārī et Muslim',
           'sa biographie (<em>tarǧama</em>) a précédé',
           'que son terme se rapproche',
           'l’inscription est arrêtée en sa faveur',
           'doctrine des gens de la Sunna',
           'Sourate al-Anbiyā’ — verset 23',
           'Il ne sera pas interrogé sur ce qu’Il fait',
           'L’imam al-Sam’ānī', 'tawaqquf', 'mers de l’égarement',
           'al-’alīm al-ḫabīr', 'Fatḥ al-Bārī',
           'aucun prophète envoyé ni ange rapproché',
           'charges religieuses', 'quintessence tient en ces quatre paroles',
           'La subsistance (<em>rizq</em>)', 'L’échéance (<em>aǧal</em>)',
           'L’œuvre (<em>’amal</em>)', 'Le malheur ou le bonheur',
           'l’islām et la mécréance', 'Ǧāmi’ al-’Ulūm wa-l-Ḥikam',
           'les actes et leurs ultimes aboutissements',
           'mauvaise fin', 'craintif et tremblant',
           'Sourate al-Mu’minūn — verset 61',
           'cœurs saisis de crainte',
           'grands péchés', 'interdits',
           'tant que paraît son apparence aux gens', '(al-Buḫārī et Muslim)',
           'L’absence de dépendance aux moyens', 'contentement',
           'la constance', 'belle fin',
           'l’inscription de la subsistance et de l’échéance',
           'La raison a-t-elle un rôle à jouer',
           'Est-il permis de délaisser l’œuvre',
           'D’après ’Alī', 'un bâton', 'la place n’ait été inscrite',
           'ne nous y fierons-nous donc pas', 'Agissez, car chacun est facilité',
           'Sourate al-Layl — versets 5 à 10', 'Ṣaḥīḥ de al-Buḫārī]',
           'la mère des croyants ’Ā’iša',
           '«\u202f&nbsp;ar-rad&nbsp;\u202f» (le rejet)']:
    check(f'kw: {kw[:52]}', kw in src)
# — garde cohérence titleFr pré-existant (non écrasé par la pose) —
check('titleFr slot cohérent', 'qaḍā' in (l.get('titleFr') or ''),
      f"({(l.get('titleFr') or '')[:46]})")

print(f'OK {len(ok)} contrôles' if not fail else 'FAIL:')
for f_ in fail:
    print('  ✗', f_)
if not fail:
    print(f'\nVERIF PASS — {len(ok)} contrôles OK / 0 échec — pdf-8 → {len(src)} car')
    sys.exit(0)
sys.exit(1)
