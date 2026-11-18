#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-35 — debug + localisation glose p151 / bandeau p158 dans bbox-150-158.html
import re, sys

BBOX = '/home/z/my-project/scripts-ia2/tmp/h5-rereads/bbox-150-158.html'
html = open(BBOX, encoding='utf-8').read()

parts = re.split(r'<page width="([\d.]+)" height="([\d.]+)">', html)
print('segments:', len(parts), file=sys.stderr)
# parts[0]=pre ; parts[1]=w150, parts[2]=h150, parts[3]=body150 ; parts[4]=w151 ... parts[6]=body151 ; ...
print(f'segments: {len(parts)} (attendu 1+3*9=28)', file=sys.stderr)

def rows_of(pnum):
    idx = 3 * (pnum - 150) + 3   # parts[3]=body150, parts[6]=body151, ...
    body = parts[idx]
    words = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', body)
    # regroupe par bande y (tolérance 6 pt)
    rows = []
    for x0, y0, x1, y1, t in words:
        y0f, y1f = float(y0), float(y1)
        for r in rows:
            if abs(r['ymin'] - y0f) < 6:
                r['items'].append((float(x0), float(x1), t))
                r['ymin'] = min(r['ymin'], y0f); r['ymax'] = max(r['ymax'], y1f)
                break
        else:
            rows.append({'ymin': y0f, 'ymax': y1f, 'items': [(float(x0), float(x1), t)]})
    rows.sort(key=lambda r: r['ymin'])
    return rows

pnum = int(sys.argv[1]) if len(sys.argv) > 1 else 151
lo = float(sys.argv[2]) if len(sys.argv) > 2 else 0
hi = float(sys.argv[3]) if len(sys.argv) > 3 else 900
for r in rows_of(pnum):
    if lo <= r['ymin'] <= hi:
        items = sorted(r['items'], key=lambda w: -w[0])  # RTL
        txt = ''.join(w[2] for w in items)
        xs = [w[0] for w in r['items']] + [w[1] for w in r['items']]
        print(f"y={r['ymin']:7.1f}-{r['ymax']:6.1f} x={min(xs):6.1f}-{max(xs):6.1f} | {txt[:105]}")
