#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA structure des titres — suivi des métriques de l'audit R713.

Balaye les pages rendues (racine publiée ou site/) et vérifie :
  1. toute page de leçon/introduction porte exactement un <h1> ;
  2. les h1 vides (<h1></h1>) sont absents du rendu ;
  3. compte les leçons sans intertitre <h2> — chantier éditorial P1 de
     l'audit, exécuté par les zones propriétaires (IA-2 primaire,
     IA-3 collège/lycée) ; le rapport donne la liste par livre pour
     suivre la décroissance du reste à faire.

Usage : python3 scripts/qa-structure.py [RACINE]
        (RACINE par défaut : racine publiée si elle contient livres/,
         sinon site/)
Sortie : code 0 si aucune anomalie bloquante (h1), 1 sinon.
Les leçons sans h2 sont un indicateur, pas un échec.
"""

import re
import sys
from pathlib import Path

DEPOT = Path(__file__).resolve().parent.parent


def livres_disponibles(racine):
    return sorted(set(p.parent for p in racine.glob('livres/*/*.html')))


def principal():
    racine = Path(sys.argv[1]) if len(sys.argv) > 1 else DEPOT
    if not (racine / 'livres').is_dir():
        racine = DEPOT / 'site'
    if not (racine / 'livres').is_dir():
        print('!! ni', DEPOT, 'ni site/ ne contiennent livres/ — construire d\'abord')
        return 1

    n_pages = 0
    h1_pb = []          # (page, n_h1) — bloquant si h1 vide ou 0
    h1_vides = 0
    sans_h2 = {}        # livre -> [docId] — indicateur de chantier
    for rep in livres_disponibles(racine):
        livre = rep.name
        for page in sorted(rep.glob('*.html')):
            if page.name == 'index.html':
                continue
            n_pages += 1
            html = page.read_text(encoding='utf-8')
            if 'class="contenu"' not in html:
                continue  # hors-ligne/404 etc. ne sont pas sous livres/
            h1s = re.findall(r'<h1[^>]*>', html, re.I)
            corps_h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.S | re.I)
            if any(not re.sub(r'<[^>]+>', '', c).strip() for c in corps_h1):
                h1_vides += 1
                h1_pb.append((f'{livre}/{page.name}', 'h1 vide'))
            elif len(h1s) == 0:
                h1_pb.append((f'{livre}/{page.name}', '0 h1'))
            elif len(h1s) > 1:
                h1_pb.append((f'{livre}/{page.name}', f'{len(h1s)} h1'))
            article = html.split('class="contenu"', 1)[-1]
            article = article.split('</article>', 1)[0]
            if re.search(r'<h1[\s>]', article, re.I) and \
                    not re.search(r'<h2[\s>]', article, re.I):
                sans_h2.setdefault(livre, []).append(page.stem)

    print(f'pages de contenu balayées : {n_pages} ({racine})')
    if h1_pb:
        print(f'ÉCHEC — anomalies h1 : {len(h1_pb)}')
        for p, why in h1_pb[:12]:
            print('  -', p, why)
    else:
        print('h1 : PASS — exactement un h1 sur chaque page de contenu, aucun h1 vide')
    total_h2 = sum(len(v) for v in sans_h2.values())
    print(f'sans intertitre h2 (chantier éditorial P1 — zones IA-2/IA-3) : '
          f'{total_h2} leçons dans {len(sans_h2)} livres')
    for livre in sorted(sans_h2, key=lambda x: -len(sans_h2[x])):
        print(f'  - {livre} : {len(sans_h2[livre])} '
              f'({", ".join(sans_h2[livre][:5])}{"…" if len(sans_h2[livre]) > 5 else ""})')
    return 1 if h1_pb else 0


if __name__ == '__main__':
    raise SystemExit(principal())
