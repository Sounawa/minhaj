#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu des leçons 798 et 799 (tafsir-5ep,
sourate al-Shūrā — doublons relevés par renvoi de référence, slots 798 = 18-20
du manuel (= muṣḥaf 20-22) et 799 = 14-17 du manuel (= muṣḥaf 16-19), 3e année
de l'enseignement collégial traditionnel, Tashīl d'Ibn Juzayy).

Les leçons sont des COPIES fidèles des leçons jumelles tafsir-3es 16850 (798)
et 16833 (799), livrées R58 et vérifiées contre le quran-cache à leur livraison
(références corrigées, numérotation al-Shūrā à 50 versets documentée). Le
présent contrôle vérifie donc :
  1. la FIDÉLITÉ de la copie : le bloc des versets de la copie est identique,
     après normalisation typographique, au bloc de la jumelle en base ;
  2. la CONCORDANCE des numérotations : étiquettes (20)(21)(22) + « al-Shūrā,
     20-22 » pour 798 ; (16)(17)(18)(19) + « al-Shūrā, 16-19 » pour 799 ; note
     « cinquante versets » présente ;
  3. l'ABSENCE de rendu hors matière : le bloc de la jumelle SŒUR absent de
     chaque copie (798 ≠ 16-19, 799 ≠ 20-22) ; renders du cache des versets
     voisins (15, 23) absents ;
  4. 0 caractère arabe (FR-seule), 0 rasm nu ;
  5. le contenu du manuel (gloses, exégètes, hadīth) présent.
"""
import json
import re
import sys

ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')


def norm(s: str) -> str:
    s = s.replace('\u202f', ' ').replace('\u00a0', ' ').replace('&nbsp;', ' ')
    s = s.replace('’', "'")
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\s+', '', s)
    return s


def verse_block(html: str, first_words: str) -> str:
    """Le paragraphe du bloc des versets (de « first_words… » au » final)."""
    m = re.search(r'«\u202f?' + re.escape(first_words) + r'[\s\S]*?»', html)
    return m.group(0) if m else ''


def check(slot: str, twin_id: str, first_words: str, labels: list,
          ref_close: str, contenu: list, sister_words: str) -> list:
    errors = []
    html = open(f'tr-tmp/lesson-{slot}-fr.html', encoding='utf-8').read()
    n = norm(html)

    # 1. structure et note de renvoi
    for frag in [
        'Source du cours',
        'leçon jumelle (' + twin_id + ')',
        'deux entrées d' + '\u2019' + 'arborescence',
        'une seule et même arborescence',
        'concorde avec la matière du fascicule',
        'cinquante versets',
        'numérotation',
        'Introduction (tamhīd)',
        'Le commentaire (tafsīr)',
        'Explication des termes',
        'Extraction des idées des versets',
        "L'évaluation",
        'enrichissement (istithmār)',
        'La préparation préalable',
        'non reproduites dans le manuel',
        'Tashīl li-ʿulūm al-tanzīl',
        'Ibn Juzayy',
        'troisième année',
    ]:
        if norm(frag) not in n:
            errors.append(f'{slot} : fragment attendu absent : {frag[:55]}')

    # 2. fidélité au bloc des versets de la jumelle
    src = json.load(open('content/books/tafsir-3es.json', encoding='utf-8'))
    twin = next(l for l in src['lessons'] if str(l['docId']) == twin_id)
    twin_block = verse_block(twin.get('htmlFr') or '', first_words)
    copy_block = verse_block(html, first_words)
    if not twin_block:
        errors.append(f'{slot} : bloc des versets introuvable dans la jumelle {twin_id}')
    if not copy_block:
        errors.append(f'{slot} : bloc des versets introuvable dans la copie')
    if twin_block and copy_block and norm(twin_block) != norm(copy_block):
        errors.append(f'{slot} : bloc des versets DIVERGE de la jumelle {twin_id}')

    # 3. concordance des numérotations
    for lab in labels:
        if '(' + str(lab) + ')' not in norm(' '.join(re.findall(r'\(\d+\)', html))):
            errors.append(f'{slot} : étiquette de verset absente : ({lab})')
    if norm(ref_close) not in n:
        errors.append(f'{slot} : référence de fermeture absente : {ref_close}')

    # 4. absence de rendu hors matière
    sister = verse_block(html, sister_words)
    if sister:
        errors.append(f'{slot} : CONTAMINATION — bloc de la leçon sœur présent')
    cache = json.load(open('scripts-translate/quran-cache.json', encoding='utf-8'))
    fr42 = {num: t for num, t in cache['42']['fr']}
    for vois in (15, 23):
        t = norm(fr42[vois])[:60]
        if t in n:
            errors.append(f'{slot} : rendu du cache du verset voisin {vois} présent (hors matière)')

    # 5. 0 arabe
    if ARABIC.search(html):
        errors.append(f'{slot} : ARABE RÉSIDUEL')

    # 6. contenu du manuel
    for c in contenu:
        if norm(c) not in n:
            errors.append(f'{slot} : contenu attendu absent : {c[:55]}')

    return errors


def main() -> None:
    errors = []
    errors += check(
        '798', '16850', 'Quiconque désire le labeur', (20, 21, 22),
        '(al-Shūrā, 20-22 — numérotation du manuel : 18-20)',
        ['ḥarth al-ākhira', 'la bête bahīra', 'la bête sāʾiba', 'la bête waṣīla',
         'Ubayy b. Kaʿb', 'Musnad de l’imam Aḥmad', 'Tafsīr d’al-Bayḍāwī : 5/80',
         'Fāṭir, 30', 'Sunan de Tirmidhī', 'Anas b. Mālik',
         'jour de Sa rencontre', 'disjonctif'],
        'Et ceux qui disputent au sujet de Dieu')
    errors += check(
        '799', '16833', 'Et ceux qui disputent', (16, 17, 18, 19),
        '(al-Shūrā, 16-19 — le manuel compte al-Shūrā à cinquante versets et numérote ce passage 14-17)',
        ['Tafsīr d’Ibn Kathīr : 7/196', 'Tafsīr d’al-Nasafī : 3/250-251',
         'la Balance', 'Doux (laṭīf)', 'Hūd, 6', 'Sabaʾ, 29', 'Ṣād, 15', 'al-Ḥajj, 45',
         'jāhiliyya', 'les mécréants de Quraysh', 'égarement lointain'],
        'Quiconque désire le labeur')

    if errors:
        print(f'VERIFY 798/799 : ÉCHEC ({len(errors)})')
        for e in errors:
            print('  ✗', e)
        sys.exit(1)
    print('VERIFY 798/799 : PASS — fidélité jumelles, numérotations, plages, FR-seule, contenu')


if __name__ == '__main__':
    main()
