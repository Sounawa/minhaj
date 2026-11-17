#!/usr/bin/env python3
# Z2-24 — clustering-y des lignes bbox pp.114-119 (calibrage des bandes r)
import re
html = open('scripts-ia2/tmp/h5-21/bbox-114-119.html').read()
pages = re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', html, re.S)
for idx, (w, h, body) in enumerate(pages):
    pno = 114 + idx
    words = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>', body)
    W, H = float(w), float(h)
    # ne garder que les mots avec au moins 2 lettres arabes (exclut debris)
    rows = []
    for x0, y0, x1, y1, txt in words:
        if len(re.findall(r'[\u0600-\u06FF]', txt)) >= 2:
            rows.append((float(y0), float(y1), float(x0), float(x1), txt))
    rows.sort()
    # cluster par yMin (tolérance 12pt)
    lines = []
    for y0, y1, x0, x1, txt in rows:
        if lines and abs(y0 - lines[-1]['y0']) < 12:
            L = lines[-1]
            L['y0'] = min(L['y0'], y0); L['y1'] = max(L['y1'], y1)
            L['x0'] = min(L['x0'], x0); L['x1'] = max(L['x1'], x1)
            L['n'] += 1; L['sample'] = (L['sample'] + ' ' + txt)[:70]
        else:
            lines.append({'y0': y0, 'y1': y1, 'x0': x0, 'x1': x1, 'n': 1, 'sample': txt[:60]})
    print(f'--- p{pno} ---')
    for L in lines:
        if L['n'] >= 3:
            print(f"  y[{L['y0']/H:.3f}-{L['y1']/H:.3f}] x[{L['x0']/W:.2f}-{L['x1']/W:.2f}] n={L['n']} «{L['sample'][:60]}»")
