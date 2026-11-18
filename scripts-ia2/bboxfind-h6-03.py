#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-37 — localisateur de mots dans le bbox (coordonnées pt) pour cadrer les zones VLM
import re, sys

BASE = '/home/z/my-project/scripts-ia2/tmp/h6-03'

def words_of(page_no):
    src = open(f'{BASE}/bbox-17-22.html').read() if page_no <= 22 else open(f'{BASE}/bbox-23.html').read()
    pages = re.split(r'<page ', src)
    # page section index: bbox-17-22 contains 17..22 ; bbox-23 contains 23
    pg = None
    for p in pages:
        m = re.search(r'width="([\d.]+)" height="([\d.]+)">(.*?)</page>', p, re.S)
        if not m: continue
        body = m.group(3)
        wm = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', body)
        # identify page by first strong marker? use order: collect all pages then pick
        pg = wm
        yield_page = None
    # fallback: rebuild ordered
    result = []
    for p in pages:
        m = re.search(r'>(.*?)</page>', p, re.S)
        if not m: continue
        body = m.group(1)
        wm = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', body)
        result.append(wm)
    if page_no <= 22:
        return result[page_no - 17]
    else:
        return result[0]

if __name__ == '__main__':
    page = int(sys.argv[1]); needle = sys.argv[2]
    for x0, y0, x1, y1, w in words_of(page):
        if needle in w:
            print(f'  p{page} "{w}" x[{float(x0):.0f}-{float(x1):.0f}] y[{float(y0):.0f}-{float(y1):.0f}]')
