#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — extraction des lignes bbox (pdftotext -bbox) pp.46-49, leçon 7 «دَعْمٌ وَتَطْبِيقٌ»
import re

src = '/home/z/my-project/scripts-ia2/tmp/h6-08/bbox-46-49.html'
t = open(src, encoding='utf-8').read()
pages = re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', t, re.S)
for idx, (w, h, body) in enumerate(pages):
    n = 46 + idx
    if n > 49:
        break
    words = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', body)
    # regrouper par ligne (yMin arrondi à 3pt)
    lines = {}
    for x0, y0, x1, y1, wtxt in words:
        key = round(float(y0) / 3) * 3
        lines.setdefault(key, []).append((float(x0), float(x1), wtxt))
    print(f'════════ PAGE {n} ({w}x{h}) — {len(words)} mots, {len(lines)} lignes ════════')
    for key in sorted(lines):
        ws = sorted(lines[key], key=lambda a: -a[0])  # droite→gauche
        y0 = key
        txt = ' '.join(w for _, _, w in ws)
        xR = max(x1 for _, x1, _ in ws)
        xL = min(x0 for x0, _, _ in ws)
        print(f'  y={key:>4} x=[{xL:>5.0f}-{xR:>5.0f}] {txt[:110]}')
