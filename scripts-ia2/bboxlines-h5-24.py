#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-28 — réassemblage RTL des lignes pp.131-138 depuis la couche bbox glyphe (leçon 24)
import re, sys

PAGES = sys.argv[1:] or ['131', '132', '133', '134', '135', '136', '137', '138']
html = open('scripts-ia2/tmp/h5-24/bbox-131-138.html').read()
pages = re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', html, re.S)

for idx, (w, h, body) in enumerate(pages):
    pno = 131 + idx
    if str(pno) not in PAGES:
        continue
    words = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>', body)
    H = float(h)
    # cluster par y (tolérance 6 pt)
    lines = {}
    for x0, y0, x1, y1, txt in words:
        yc = round(float(y0) / 6) * 6
        lines.setdefault(yc, []).append((float(x0), float(y0), txt))
    print(f'═══════ PAGE {pno} ═══════')
    for yc in sorted(lines):
        glyphs = sorted(lines[yc], key=lambda t: -t[0])  # RTL : x décroissant
        yf = glyphs[0][1] / H
        line = ''.join(g[2] for g in glyphs)
        if len(line.strip()) < 2:
            continue
        print(f'y={yf:.3f} | {line[:170]}')
