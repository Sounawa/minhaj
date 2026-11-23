#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — cartnum-h6-17 : triangulation pixel du numéro du cartouche p.95
# contre p.90 (١٥ établi Z2-52) et p.100 (L18, attendu ١٧).
# Méthode : couche bleue @1200 → texte blanc→noir, extraction de la zone numéro,
# découpe des 2 ames de chiffres, corrélation croisée.
import numpy as np
from PIL import Image

DIR = "/home/z/my-project/pdf-work/h6-15/zoom"

def load_bleu(tag):
    im = Image.open(f"{DIR}/{tag}-bleu.png").convert("L")
    return np.array(im)

def digit_zone(a):
    # zone numéro : moitié droite du cartouche, sous الدرس (bande basse)
    H, W = a.shape
    ink = a < 120
    # chercher dans le quadrant droit-bas du cartouche (y 0.35-0.75 H, x 0.60-0.95 W)
    sub = ink[int(0.32*H):int(0.78*H), int(0.55*W):int(0.97*W)]
    # profil colonnes
    cols = sub.sum(axis=0)
    # groupes de colonnes occupées
    groups = []
    st = None
    for i, v in enumerate(cols > 0):
        if v and st is None: st = i
        if not v and st is not None:
            if i - st >= 8: groups.append((st, i))
            st = None
    if st is not None: groups.append((st, len(cols)))
    return sub, groups

def norm(img):
    h, w = img.shape
    out = np.zeros((80, 80))
    im = Image.fromarray((1 - img.astype(np.uint8)) * 255)
    im = im.resize((80, 80), Image.LANCZOS)
    a = np.array(im) < 128
    return a.astype(float)

def corr(a, b):
    av, bv = a - a.mean(), b - b.mean()
    d = np.sqrt((av**2).sum() * (bv**2).sum())
    return float((av * bv).sum() / d) if d else 0.0

tags = {"p90": "z5-cart-bleu-p90", "p95": "z5-cart-bleu-p95", "p100": "z5-cart-bleu-p100"}
zones = {}
for tag, base in tags.items():
    a = load_bleu(base)
    sub, groups = digit_zone(a)
    print(f"{tag}: {len(groups)} groupes de colonnes: {groups}")
    # sauvegarde visuelle de la sous-zone
    Image.fromarray(((1 - sub.astype(np.uint8)) * 255)).save(f"{DIR}/z5-numzone-{tag}.png")
    zones[tag] = (sub, groups)

# comparaison des groupes entre pages (alignement par ordre x)
print()
for tag in tags:
    sub, groups = zones[tag]
    for gi, (x0, x1) in enumerate(groups):
        g = sub[:, x0:x1]
        # lignes occupées
        rows = g.sum(axis=1)
        nz = np.nonzero(rows > 0)[0]
        if len(nz):
            print(f"{tag} grp{gi}: w={x1-x0}, y[{nz.min()}-{nz.max()}], ink={int(g.sum())}")

# corrélation croisée des groupes appariés (même index = même position physique)
print()
pairs = [("p90","p95"), ("p90","p100"), ("p95","p100")]
for t1, t2 in pairs:
    s1, g1 = zones[t1]; s2, g2 = zones[t2]
    for gi in range(min(len(g1), len(g2))):
        a1 = norm(s1[:, g1[gi][0]:g1[gi][1]])
        a2 = norm(s2[:, g2[gi][0]:g2[gi][1]])
        print(f"corr {t1}.g{gi} vs {t2}.g{gi} : {corr(a1, a2):.3f}")
