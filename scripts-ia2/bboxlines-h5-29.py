#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-34 — reconstruction word-level du bbox pdftotext pp.159-166 (leçon 29, bibliographie)
# But : lignes ordonnées (y croissant) avec hauteurs de police, pour (a) détecter les
# bandeaux/rubriques décoratives (gaps + garbles), (b) calibrer les recadrages des
# points disputés (dates, nasab, entrée 37 manquante).
import re, sys
from html.parser import HTMLParser

SRC = '/home/z/my-project/scripts-ia2/tmp/h5-29/bbox-159-166.html'

class B(HTMLParser):
    def __init__(self):
        super().__init__()
        self.words = []          # (page, xmin, ymin, xmax, ymax, word)
        self.cur = None
        self.page = 158
        self.inword = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'page':
            self.page += 1        # pages en ordre d'apparition : 159..166
        elif tag == 'word':
            self.inword = True
            self.cur = [self.page, float(a['xmin']), float(a['ymin']),
                        float(a['xmax']), float(a['ymax']), '']
    def handle_endtag(self, tag):
        if tag == 'word' and self.cur is not None:
            self.words.append(tuple(self.cur)); self.cur = None; self.inword = False
    def handle_data(self, d):
        if self.inword:
            self.cur[5] += d

b = B()
b.feed(open(SRC, encoding='utf-8').read())

pages = {}
for w in b.words:
    pages.setdefault(w[0], []).append(w)

target = int(sys.argv[1]) if len(sys.argv) > 1 else 159
ymin_f = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
ymax_f = float(sys.argv[3]) if len(sys.argv) > 3 else 1e9

ws = sorted(pages.get(target, []), key=lambda w: (round(w[2], 0), -w[1]))
# regrouper par ligne (ymin proche)
lines = []
for w in ws:
    if w[2] < ymin_f or w[2] > ymax_f:
        continue
    placed = False
    for L in lines:
        if abs(L['y'] - w[2]) < 6.0:
            L['words'].append(w); placed = True
            break
    if not placed:
        lines.append({'y': w[2], 'words': [w]})
lines.sort(key=lambda L: L['y'])
prev = None
for L in lines:
    L['words'].sort(key=lambda w: -w[1])   # RTL : x décroissant
    hs = [w[4] - w[3] for w in L['words'] if w[5].strip()]
    hmed = sorted(hs)[len(hs)//2] if hs else 0
    gap = (L['y'] - prev) if prev is not None else 0.0
    txt = ' '.join(w[5] for w in L['words'])
    print(f"y={L['y']:7.1f} h={hmed:4.1f} gap={gap:5.1f} | {txt[:150]}")
    prev = L['y']
