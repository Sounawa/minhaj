#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — adjudication finale par géométrie des points :
# (1) mot disputé du header p.47 : compter les points du 1er radical
#     (ح=0 pt → وأحللها ; غ=1 pt → ? ; ت=2 pts → وأتلواها?)
# (2) ligne «كل سلامى» p.46 : mesurer le vide entre الناس et les points de remplissage
#     (=> «عليه» imprimé ou non).
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-08'
S = 1200 / 72.0

def load(pg):
    # grayscale uint8 — 141 Mo seulement
    return np.array(Image.open(f'{DIR}/r1200/p{pg}.png').convert('L'))

def ink_profile(im, x0, y0, x1, y1, thr=130):
    g = im[int(y0*S):int(y1*S), int(x0*S):int(x1*S)].astype(int)
    return (g < thr), g

# ── (1) header p.47 : segments de mots avec leur hauteur d'encre ──
print('═══ (1) HEADER p.47 — profil de la ligne (y=495-522) ═══')
ink, g = ink_profile(load(47), 195, 495, 540, 522)
colprof = ink.sum(axis=0)
runs, inr = [], False
for x, v in enumerate(colprof):
    if v > 2 and not inr:
        inr, xa = True, x
    elif v <= 2 and inr:
        inr = False
        if x - xa > 6:
            runs.append((xa, x))
if inr: runs.append((xa, len(colprof)))
# grouper les runs proches (<6pt) en mots
words = []
for r in runs:
    if words and r[0] - words[-1][1] < 6*S/1.0/1.0:
        words[-1] = (words[-1][0], r[1])
    else:
        words.append(list(r))
print(f'{len(words)} groupes de mots (droite→gauche) :')
for xa, xb in reversed(words):
    seg = ink[:, xa:xb]
    # lignes d'encre : repérer les points ISOLÉS au-dessus du corps
    rowprof = seg.sum(axis=1)
    h = seg.shape[0]
    # corps du mot = bande contenant le plus d'encre
    core = np.argsort(rowprof)[-int(h*0.35):]
    core_top, core_bot = core.min(), core.max()
    dots_above = rowprof[:max(core_top-3, 0)].sum()
    dots_below = rowprof[min(core_bot+3, h):].sum()
    print(f'  x=[{195+xa/S:5.1f}-{195+xb/S:5.1f}]pt l={(xb-xa)/S:5.1f}pt '
          f'core=[{core_top/S:4.1f}-{core_bot/S:4.1f}] ink_above={dots_above} ink_below={dots_below}')

# ── (2) ligne كل سلامى p.46 : structure espace/points ──
print()
print('═══ (2) LIGNE «كل سلامى» p.46 (y=433-453) — profil ═══')
ink2, g2 = ink_profile(load(46), 240, 433, 530, 453)
colprof2 = ink2.sum(axis=0)
runs2, inr = [], False
for x, v in enumerate(colprof2):
    if v > 1 and not inr:
        inr, xa = True, x
    elif v <= 1 and inr:
        inr = False
        runs2.append((xa, x))
if inr: runs2.append((xa, len(colprof2)))
print(f'{len(runs2)} runs d\\u2019encre (gauche→droite) :')
for xa, xb in runs2:
    seg = ink2[:, xa:xb]
    dens = seg.mean()
    hh = (xb - xa) / S
    kind = 'POINT' if hh < 2.5 and dens > 0.15 else ('lettre' if hh < 12 else 'mot')
    print(f'  x=[{240+xa/S:5.1f}-{240+xb/S:5.1f}]pt l={hh:5.1f}pt dens={dens:.2f} {kind}')
