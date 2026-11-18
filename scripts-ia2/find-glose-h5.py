#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-35 — localise la ligne de la glose أَرَأْيْتَ (p.151) et le bandeau p.158 dans le bbox,
# puis produit les recadrages 1200 dpi natifs pour relecture VLM.
import re, subprocess, os

BBOX = '/home/z/my-project/scripts-ia2/tmp/h5-rereads/bbox-150-158.html'
R1200 = '/home/z/my-project/scripts-ia2/tmp/h5-rereads/r1200'
CROPS = '/home/z/my-project/scripts-ia2/tmp/h5-rereads/crops'
os.makedirs(CROPS, exist_ok=True)

html = open(BBOX, encoding='utf-8').read()

# découpe par page ; pages[1] = page PDF 150
pages = re.split(r'<page width="([\d.]+)" height="([\d.]+)">', html)
# pages[0]=preamble, pages[1]=w150, pages[2]=body150, pages[3]=w151, pages[4]=body151 ...

def rows_of(pnum):
    idx = 2 * (pnum - 150 + 1) - 1
    body = pages[idx + 1]
    words = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', body)
    rows = {}
    for x0, y0, x1, y1, t in words:
        y = round(float(y0), 1)
        rows.setdefault(y, []).append((float(x0), float(x1), t))
    return rows

def dump_rows(pnum, ymin, ymax, label):
    print(f'===== p.{pnum} {label} (y {ymin}-{ymax}) =====')
    rows = rows_of(pnum)
    for y in sorted(rows):
        if ymin <= y <= ymax:
            items = sorted(rows[y], key=lambda w: -w[0])  # RTL : x décroissant
            txt = ''.join(w[2] for w in items)
            xs = [w[0] for w in items] + [w[1] for w in items]
            print(f'y={y:7.1f} x={min(xs):6.1f}-{max(xs):6.1f} | {txt[:110]}')

# p.151 : entre fin ترجمة (y~520?) et questions فهم — balyage large
dump_rows(151, 380, 700, 'zone glose présumée')
