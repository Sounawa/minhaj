#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA apparat de livraison — R719.

Vérifie trois choses après un build :
  1. AUCUN marqueur d’apparat de livraison dans les pages rendues (site/ et
     pages publiées à la racine : index.html, livres/**, hors-ligne.html) —
     ni bloc autonome, ni titre mixte, ni paragraphe d’entête de livraison,
     ni note « Points restés ouverts… », ni rubrique de sommaire ;
  2. les DONNÉES content/books/*.json portent toujours l’apparat (45
     documents attendus) — preuve que le filtre opère au rendu seul et que
     les données sources restent intouchées ;
  3. dans les 5 leçons à titre mixte (hadith-3es 390…394), les subtilités
     savantes réelles sont bien préservées dans les pages rendues.

Stdlib seule. Sortie : PASS/FAIL, code 0/1.
"""

import glob
import json
import re
import sys
from pathlib import Path

MARQUEURS = (
    'apparat de preuve de la livraison',
    'Chaîne de production de la passe',
    'Cette livraison a été faite',
    'Points restés ouverts consignés pour la reprise',
    'voir l’apparat',
    '<dt>Versets du cache</dt>',
    '<dt>Preuves de la passe</dt>',
    '<dt>État de la passe</dt>',
    '<dt>Statut de la livraison</dt>',
    '<dt>Trace de la passe</dt>',
)

# contenus RÉELS (subtilités savantes) qui doivent rester rendus
PRESERVES = {
    'pdf-mut23h2x-390': 'Subtilités tranchées sur l’image',
    'pdf-mut23h2x-391': 'Les treize numéros de hadiths imprimés entre crochets',
    'pdf-mut23h2x-392': 'Subtilités tranchées sur l’image',
    'pdf-mut23h2x-393': 'bornes tranchées par double sondage d’image',
    'pdf-mut23h2x-394': 'bornes tranchées par double preuve d’image',
}

# rubrique utile conservée dans le lesson-meta (401)
CONSERVES = {
    'pdf-mut23h2x-401': ('Plan du cours imprimé', 'Source du cours'),
}


def main():
    depot = Path(__file__).resolve().parent.parent
    echecs = []

    # ---- 1. pages rendues propres ------------------------------------------
    pages = sorted(glob.glob(str(depot / 'site' / '**' / '*.html'), recursive=True))
    pages += sorted(glob.glob(str(depot / 'site' / 'recherche' / '*.js'), recursive=True))
    pages += sorted(glob.glob(str(depot / '*.html')))          # racine publiée
    pages += sorted(glob.glob(str(depot / 'livres' / '**' / '*.html'), recursive=True))
    pages = [p for p in pages if Path(p).exists()]

    balayes = 0
    for p in pages:
        texte = Path(p).read_text(encoding='utf-8', errors='replace')
        balayes += 1
        for marqueur in MARQUEURS:
            if marqueur in texte:
                echecs.append(f'{p} : marqueur « {marqueur[:48]}… » encore rendu')

    # ---- 2. données intouchées (l’apparat reste dans les JSON) --------------
    docs_avec_apparat = set()
    for chemin in sorted(glob.glob(str(depot / 'content' / 'books' / '*.json'))):
        data = json.loads(Path(chemin).read_text(encoding='utf-8'))
        bid = data.get('id', chemin)
        lessons = list(data.get('lessons', []))
        for l in lessons:
            if 'apparat de preuve' in (l.get('htmlFr') or ''):
                docs_avec_apparat.add((bid, l.get('docId')))
    if len(docs_avec_apparat) != 45:
        echecs.append(f'données : {len(docs_avec_apparat)} docs avec apparat au lieu de 45 '
                      '(si le propriétaire de zone a nettoyé ses données, mettre à jour ce contrôle)')

    # ---- 3. subtilités préservées dans les 5 leçons mixtes ------------------
    for did, attendu in PRESERVES.items():
        page = depot / 'site' / 'livres' / 'hadith-3es' / f'{did}.html'
        if not page.exists():
            echecs.append(f'{did} : page rendue introuvable ({page})')
            continue
        texte = page.read_text(encoding='utf-8', errors='replace')
        if attendu not in texte:
            echecs.append(f'{did} : contenu réel perdu au rendu (attendu « {attendu[:44]}… »)')

    # ---- 4. rubriques utiles conservées dans le lesson-meta -----------------
    for did, labels in CONSERVES.items():
        page = depot / 'site' / 'livres' / 'hadith-3es' / f'{did}.html'
        if not page.exists():
            echecs.append(f'{did} : page rendue introuvable ({page})')
            continue
        texte = page.read_text(encoding='utf-8', errors='replace')
        for lab in labels:
            if f'<dt>{lab}</dt>' not in texte:
                echecs.append(f'{did} : rubrique utile perdue « {lab} »')

    # ---- bilan --------------------------------------------------------------
    print(f'qa-apparat : {balayes} pages balayées | '
          f'{len(docs_avec_apparat)} docs avec apparat dans les données (attendu 45) | '
          f'{len(PRESERVES)} leçons mixtes à contenu préservé')
    if echecs:
        print(f'FAIL ({len(echecs)} échecs) :')
        for e in echecs[:20]:
            print(f'  - {e}')
        return 1
    print('PASS — rendu propre, données intouchées, subtilités préservées')
    return 0


if __name__ == '__main__':
    sys.exit(main())
