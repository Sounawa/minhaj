#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-30 — extraction word-level (x,y) du html bbox pp.138-143 (méthode Z2-28) — sortie TSV triée page/y/x
import re, sys

SRC = '/home/z/my-project/scripts-ia2/tmp/h5-25/bbox-138-146.html'
pages = {}
cur = None
for line in open(SRC, encoding='utf-8'):
    m = re.search(r'<page width="([\d.]+)" height="([\d.]+)"', line)
    if m:
        cur = {'w': float(m.group(1)), 'h': float(m.group(2)), 'words': []}
        continue
    if cur is not None:
        m = re.search(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', line)
        if m:
            cur['words'].append({
                'x0': float(m.group(1)), 'y0': float(m.group(2)),
                'x1': float(m.group(3)), 'y1': float(m.group(4)),
                't': m.group(5)})
    m2 = re.search(r'</page>', line)
    if m2 and cur:
        pages[len(pages) + 138] = cur
        cur = None

out = open('/home/z/my-project/scripts-ia2/tmp/h5-25/bbox-words.tsv', 'w', encoding='utf-8')
out.write('page\tx0\ty0\tx1\ty1\tword\n')
for pno in sorted(pages):
    p = pages[pno]
    ws = sorted(p['words'], key=lambda w: (round(w['y0']), -w['x0']))
    for w in ws:
        out.write(f"{pno}\t{w['x0']:.0f}\t{w['y0']:.0f}\t{w['x1']:.0f}\t{w['y1']:.0f}\t{w['t']}\n")
out.close()
print('pages:', sorted(pages), '| total words:', sum(len(p['words']) for p in pages.values()))
