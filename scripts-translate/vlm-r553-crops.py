#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R553 — Générateur des crops ciblés haute résolution (fitz : pixmap + clip).

Conventions (identiques aux crops p105-h1-zone.png etc. produits à ~910 dpi,
zoom ≈ 12.6, pleine largeur de page) : page 637.2 × 807.1 pt ; un clip
(y0, y1) est donné en FRACTION de la hauteur de page ; sortie PNG niveau
gris→RGB pleine largeur dans tr-tmp/qa-crops-r553/.

Ce script documente ET régénère les crops de ciblage utilisés par les passes
VLM (le générateur de la passe interrompue 14:32-14:54Z n'avait pas été
consigné) ; les clips ci-dessous sont ceux des zones restées sans lecture
ciblée (passe 4)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r553"
ZOOM = 12.6  # ≈ 907 dpi

# (nom, page, y0, y1) — fractions de la hauteur de page (0 = haut)
CLIPS = [
    # p.109 bas : sous-section « ب- حول الفائدة والربح » + définition de la
    # fāʾida (couche texte corrompue, jamais lue par un crop dédié)
    ("p109-faida", 109, 0.72, 1.00),
    # p.110 haut : ligne d'ouverture « استفتى… 46 » + début du récit d'Abū Bakr
    ("p110-top", 110, 0.00, 0.20),
    # p.110 milieu : « حول الربح : من كان له مال… » + nombres de dinars +
    # renvoi [الموطأ رقم : 666] + nombre curieux de la couche (« 0035 »)
    ("p110-ribs", 110, 0.30, 0.62),
]

doc = fitz.open(PDF)
mat = fitz.Matrix(ZOOM, ZOOM)
for name, page_no, y0, y1 in CLIPS:
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.x0, r.y0 + y0 * r.height, r.x1, r.y0 + y1 * r.height)
    pix = pg.get_pixmap(matrix=mat, clip=clip, alpha=False)
    path = f"{OUT}/{name}.png"
    pix.save(path)
    print(path, pix.width, "x", pix.height)
print("DONE")
