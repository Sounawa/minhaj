#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-10 — vérification de la livraison hadith-5ep / pdf-9 (les innovations dans la religion)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-9.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-9']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-9 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon 4 pages)', 9000 <= len(src) <= 17000, f'({len(src)} car)')
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
# — matière adjudiquée du manuel (Z2-10, planches p56-59 + couche) —
for kw in ['<h1>Les innovations (bid’a) dans la religion</h1>',
           'al-iḥdāṯ wa-l-ibtidā’ fī d-dīn', '(الْإِحْدَاثُ وَالِابْتِدَاعُ فِي الدِّينِ)',
           'Neuvième leçon (9) du manuel', 'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'tamhīd', 'an-naṣṣ', 'tarǧamat ar-rāwī',
           'al-fahm', 'istikhlāṣ al-maḍāmīn', 'at-taḥlīl', 'at-taqwīm',
           'al-istiṯmār', 'al-a’dād al-qabliyya',
           'la mère des croyants', '’Ā’iša',
           'la Véridique, fille du Véridique', 'aṣ-ṣiddīqa bint aṣ-ṣiddīq',
           'parts successorales',
           'an 57 ou en l’an 58 de l’Hégire',
           'Quiconque introduit dans notre affaire présente ce qui n’en fait pas partie',
           'Ṣaḥīḥ de al-Buḫārī et Muslim',
           'Quiconque accomplit une œuvre qui ne relève pas de notre ordre',
           'il a créé et forgé', 'anša’a wa-ḫtara’a',
           'notre Loi et notre religion', 'šar’unā wa-dīnunā',
           'repoussé', 'mardūd',
           'une voie inventée dans la religion, qui ressemble à la Loi',
           'se rapprocher d’Allah', 'al-I’tiṣām',
           'rien n’en est accepté en droit',
           'elle ne comporte aucune récompense',
           'formelle', 'ṣarīḥa',
           'instituée de lui-même', 'qu’un précédent y ait pourvu',
           'fondement authentique', 'aṣl ṣaḥīḥ',
           'règle générale', 'qā’ida ’āmma',
           'il est pécheur',
           'nullité de tous les contrats', '’uqūd',
           'absence d’obligation des fruits', 'ṯamarāt',
           'l’intérêt', 'maṣlaḥa',
           'finalités générales', 'maqāṣid',
           'la transcription du Coran dans les muṣḥafs',
           'ramenant les branches du <em>fiqh</em> à leurs principes',
           'en grammaire, en calcul, en parts successorales',
           'la sincérité exclusive', 'iḫlāṣ',
           'la conformité au modèle du Messager', 'mutāba’a',
           'Ǧāmi’ al-’Ulūm wa-l-Ḥikam, avec adaptations',
           'Sourate al-An’ām — verset 154',
           'Voici Mon chemin, qui est droit',
           'ne suivez pas les autres chemins',
           'L’incitation à la conformité au modèle', 'ittibā’',
           'mise en garde contre l’innovation',
           'toute œuvre qui la contredit est rejetée',
           'Se tenir aux limites des enseignements du Livre et de la Sunna',
           'l’exposé des savants et les règles de la Loi',
           'Qu’entend-on par le mot',
           'l’œuvre acceptée auprès d’Allah le Très-Haut',
           "l’apport de la seconde version",
           'Prenez ce que le Messager vous a donné',
           'Sourate al-Bayyina — verset 5',
           'Allah observera votre œuvre, de même que Son Messager et les croyants',
           'Sourate an-Naml — verset 19',
           'fa-ḫuḏūhu', 'muḫtala’a', 'ṣāliḥan', 'tarḍīhi',
           'lexique', 'al-mu’ǧam',
           'Nu’mān ibn Bašīr',
           'choses ambiguës', 'muštabahāt']:
    check(f'kw: {kw[:52]}', kw in src)
# — récusions (hallucinations VLM adjudiquées sur les planches) —
check('récusé: ʿUṯmān ibn ʿAffān (VLM) hors livr.',
      'ʿUṯmān' not in src and 'ʿAffān' not in src and 'Uthman' not in src)
check('récusé: muštarakāt (VLM) hors livr.', 'muštarakāt' not in src and 'choses communes' not in src)
check('récusé: «quatrième hadīth» (copie pdf-8)', 'quatrième hadīth' not in src)
check('récusé: la ḫabīr (leçon 8)', 'al-ḫabīr' not in src and 'al-’alīm al-ḫabīr' not in src)
# — garde cohérence titleFr pré-existant (non écrasé par la pose) —
check('titleFr slot cohérent', 'innovation' in (l.get('titleFr') or '').lower(),
      f"({(l.get('titleFr') or '')[:46]})")
check('titleFr inchangé', (l.get('titleFr') or '') == 'Les innovations (bidʿa) dans la religion',
      f"({(l.get('titleFr') or '')[:46]})")
# — garde-doublon : htmlFr du JSON == fichier (après pose uniquement) —
if fr:
    check('htmlFr posé == fichier', fr.strip() == src.strip(),
          f'(json={len(fr)} / fichier={len(src)})')

print(f'OK {len(ok)} contrôles' if not fail else 'FAIL:')
for f_ in fail:
    print('  ✗', f_)
if not fail:
    print(f'\nVERIF PASS — {len(ok)} contrôles OK / 0 échec — pdf-9 → {len(src)} car')
    sys.exit(0)
sys.exit(1)
