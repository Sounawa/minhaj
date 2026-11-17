#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rend scripts/og-image.source.html en og-image.png (1200×630) à la racine.

Image de partage sociale (og:image / twitter:image) recommandée par l'audit
R713 (P2). Polices chargées depuis content/fonts/ — aucun réseau utile.
Re-exécuter seulement si la charte change :
    python3 scripts/generer-og-image.py
"""

from pathlib import Path

from playwright.sync_api import sync_playwright

DEPOT = Path(__file__).resolve().parent.parent
SOURCE = DEPOT / 'scripts' / 'og-image.source.html'
CIBLE = DEPOT / 'og-image.png'


def main():
    with sync_playwright() as p:
        navigateur = p.chromium.launch()
        page = navigateur.new_page(viewport={'width': 1200, 'height': 630},
                                   device_scale_factor=2)
        page.goto(SOURCE.as_uri())
        page.wait_for_timeout(400)  # laisse les polices se charger
        page.screenshot(path=str(CIBLE), clip={'x': 0, 'y': 0,
                                               'width': 1200, 'height': 630})
        navigateur.close()
    # og:image : fichier 1200×630 exact — le rendu @2x est ré-échantillonné
    from PIL import Image
    im = Image.open(CIBLE).resize((1200, 630), Image.LANCZOS)
    im.save(CIBLE, optimize=True)
    taille = CIBLE.stat().st_size
    print(f'og-image.png : {taille / 1024:.0f} Ko (1200×630)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
