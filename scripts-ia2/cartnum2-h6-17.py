#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — cartnum2-h6-17 : triangulation pixel v2 — le numéro du cartouche est
# en BLEU FONCÉ sur le losange JAUNE : extraire les pixels sombres du losange
# (droite du cartouche, sous الدرس) et comparer p.90 (١٥) / p.95 (?) / p.100 (?).
import numpy as np
from PIL import Image

DIR = "/home/z/my-project/pdf-work/h6-15/zoom"

def load_color(tag):
    # images couleur @1200 déjà rendues (z5-cart-bleu-XX.png = conversion ; il faut
    # les originaux couleur : z4-p95-cart-vlm.png etc. ou re-render z5 original)
    # les originaux : z5-cart-bleu-pXX.png est LA CONVERSION. On re-part des
    # rendus couleur : z4-p95-cart-vlm (p95 seulement). Pour p90/p100 : rendus
    # couleur refaits par zoom5 (cart_bleu n'a pas gardé le couleur) → on re-extrait
    # depuis les PNG gris 600dpi ? Non : re-render couleur @1200 via le PDF.
    return None

# Les rendus couleur complets du cartouche : p95 = z4-p95-cart-vlm.png (1200).
# p90/p100 : on re-rend la même zone (y300-1100 @1200 couleur) via pdftoppm.
import subprocess, os
PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"

def render(name, page):
    out = f"{DIR}/{name}"
    if not os.path.exists(out + ".png"):
        f = 1200 / 600.0
        W, H = int(5308 * f) + 40, int(6725 * f) + 40
        Y0, Y1 = int(300 * f), int(1100 * f)
        subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "1200",
                        "-png", "-singlefile", "-x", "0", "-y", str(Y0),
                        "-W", str(W), "-H", str(Y1 - Y0), PDF, out], check=True)
    return out + ".png"

pages = {"p90": 90, "p95": 95, "p100": 100}
for tag, pg in pages.items():
    render(f"z5-cartcol-{tag}", pg)
    print(tag, "rendu")

def num_layer(tag):
    """extrait le numéro : pixels sombres (encre bleu foncé) du losange jaune."""
    a = np.array(Image.open(f"{DIR}/z5-cartcol-{tag}.png").convert("RGB")).astype(int)
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    lum = (R + G + B) // 3
    dark = lum < 110   # encre sombre sur fond jaune clair
    H, W = dark.shape
    # losange = moitié droite ; numéro = bande basse du losange (sous الدرس)
    sub = dark[:, int(0.62 * W):int(0.98 * W)]
    cols = sub.sum(axis=0)
    groups, st = [], None
    for i, v in enumerate(cols > 1):
        if v and st is None: st = i
        if not v and st is not None:
            if i - st >= 6: groups.append((st, i))
            st = None
    if st is not None: groups.append((st, len(cols)))
    return dark, sub, groups

def norm(img):
    im = Image.fromarray((1 - img.astype(np.uint8)) * 255)
    im = im.resize((60, 60), Image.LANCZOS)
    return (np.array(im) < 128).astype(float)

def corr(a, b):
    av, bv = a - a.mean(), b - b.mean()
    d = np.sqrt((av**2).sum() * (bv**2).sum())
    return float((av * bv).sum() / d) if d else 0.0

zones = {}
for tag in pages:
    dark, sub, groups = num_layer(tag)
    # bande verticale du numéro : chercher les lignes occupées dans la moitié basse
    Hs, Ws = sub.shape
    band = sub[int(0.45 * Hs):, :]
    rows = band.sum(axis=1)
    nz = np.nonzero(rows > 0)[0]
    print(f"{tag}: groupes col = {groups}" + (f" ; lignes occupées y[{nz.min()}-{nz.max()}] (relatif)" if len(nz) else " ; RIEN"))
    zones[tag] = (sub, groups, nz if len(nz) else None)

# extraction des digits : dans la bande numéro, groupes de colonnes
digits = {}
for tag in pages:
    sub, groups, nz = zones[tag]
    if nz is None:
        continue
    Hs, Ws = sub.shape
    y0n = int(0.45 * Hs) + nz.min()
    y1n = int(0.45 * Hs) + nz.max() + 1
    band = sub[y0n:y1n, :]
    cols = band.sum(axis=0)
    gr, st = [], None
    for i, v in enumerate(cols > 0):
        if v and st is None: st = i
        if not v and st is not None:
            if i - st >= 4: gr.append((st, i))
            st = None
    if st is not None: gr.append((st, len(cols)))
    print(f"{tag}: DIGITS = {gr}")
    digits[tag] = [band[:, g[0]:g[1]] for g in gr]
    for di, g in enumerate(gr):
        Image.fromarray((1 - band[:, g[0]:g[1]].astype(np.uint8)) * 255).save(f"{DIR}/z5-digit-{tag}-{di}.png")

print()
for t1, t2 in [("p90","p95"), ("p90","p100"), ("p95","p100")]:
    if t1 in digits and t2 in digits:
        n = min(len(digits[t1]), len(digits[t2]))
        for di in range(n):
            c = corr(norm(digits[t1][di]), norm(digits[t2][di]))
            print(f"corr digit{di} {t1} vs {t2}: {c:.3f}")
