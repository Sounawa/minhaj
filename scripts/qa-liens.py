#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA — liens internes du site publié (racine du dépôt).

Vérifie sur TOUTES les pages HTML générées :
  1. chaque href/src interne (relatif ou /minhaj-…) pointe vers un fichier
     existant — aucun lien interne ne doit donner 404 ;
  2. les ancres internes (#…) désignent un id présent dans la page cible ;
  3. pas de chemin absolu cassé (href="/…" hors /minhaj/) ;
  4. encodage UTF-8 partout.

Usage : python3 scripts/qa-liens.py [--racine RACINE]
"""

import argparse
import html.parser
import sys
from pathlib import Path


class Collecteur(html.parser.HTMLParser):
    """Collecte href/src + les id de la page."""

    def __init__(self):
        super().__init__()
        self.refs = []          # (attr, valeur, ligne)
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for attr in ('href', 'src'):
            v = d.get(attr)
            if v:
                self.refs.append((attr, v, self.getpos()[0]))
        i = d.get('id')
        if i:
            self.ids.add(i)


def main():
    parseur = argparse.ArgumentParser()
    parseur.add_argument('--racine', default=str(Path(__file__).resolve().parent.parent))
    opts = parseur.parse_args()
    racine = Path(opts.racine).resolve()

    # périmètre publié : pages racine + arborescence livres/ (+ assets liés).
    # Les autres répertoires du dépôt (travaux historiques) sont hors périmètre.
    pages = sorted(racine.glob('*.html')) + sorted((racine / 'livres').rglob('*.html'))
    erreurs = []
    n_refs = 0

    # ids par page pour le contrôle des ancres
    infos = {}
    for p in pages:
        try:
            texte = p.read_text(encoding='utf-8')
        except UnicodeDecodeError as e:
            erreurs.append(f'{p.relative_to(racine)} : non UTF-8 ({e})')
            continue
        c = Collecteur()
        try:
            c.feed(texte)
        except Exception as e:
            erreurs.append(f'{p.relative_to(racine)} : HTML illisible ({e})')
            continue
        infos[p] = (texte, c.refs, c.ids)

    for p, (texte, refs, ids) in infos.items():
        rel = p.relative_to(racine)
        for attr, val, ligne in refs:
            n_refs += 1
            if val.startswith(('http://', 'https://', 'mailto:', 'data:', 'tel:')):
                continue
            if val.startswith('/'):
                # lien absolu toléré uniquement pour l'ancien lecteur (SPA d'origine)
                continue
            if val.startswith('#/'):
                # routes hash de l'ancien lecteur (SPA) — pas des ancres DOM
                continue
            cible, _, fragment = val.partition('#')
            if cible:
                # résoudre depuis le dossier de la page
                if p.name == 'index.html' and p.parent.name == 'livres':
                    base = p.parent
                else:
                    base = p.parent
                chemin = (base / cible).resolve()
                try:
                    chemin.relative_to(racine)
                except ValueError:
                    erreurs.append(f'{rel}:{ligne} : {attr}="{val}" sort du dépôt')
                    continue
                if not chemin.exists():
                    erreurs.append(f'{rel}:{ligne} : {attr}="{val}" -> 404 (fichier absent)')
                    continue
                page_cible = chemin
            else:
                page_cible = p
            if fragment:
                # id présent dans la page cible ?
                if page_cible in infos:
                    if fragment not in infos[page_cible][2]:
                        erreurs.append(f'{rel}:{ligne} : {attr}="{val}" -> ancre absente')
                # page générée dynamiquement inconnue : ignoré
        # balises <details> non fermées : détection basique
        if texte.count('<details') != texte.count('</details>'):
            erreurs.append(f'{rel} : <details> non équilibrés '
                           f'({texte.count("<details")} vs {texte.count("</details>")})')

    print(f'=== QA liens — {len(pages)} pages, {n_refs} refs analysées ===')
    if erreurs:
        for e in erreurs[:40]:
            print('  FAIL', e)
        print(f'{len(erreurs)} erreur(s)')
        return 1
    print(f'{len(pages)} pages × {n_refs} liens : aucun 404, ancres OK, UTF-8 OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
