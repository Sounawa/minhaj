#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-21 — positions bbox des mots-clés pp.108-110 (calibration géographique)
import re

html = open('scripts-ia2/tmp/h5-19/bbox-108-109.html').read()
pages = re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', html, re.S)
KEYS = ['مظاهر', 'ضياف', 'سُنَن', 'المُرْسَل', 'راهيم', 'ذاريات', 'يستفاد', 'يستف',
        'الفَقْه', 'الفقه', 'يبادر', 'كلفة', 'القاس', 'تقويم', 'ينفع', 'نفع', 'حث',
        'لماذا', 'نوع', 'جيران', 'حيوان', 'عمرو', 'عمر', 'زكاة', 'إعداد', 'الاغد',
        'الدعم', 'بقية', 'الجوارح', 'خصال', 'الإيمان', 'هَذَا ال', 'ضَيْف']
for idx, (w, h, body) in enumerate(pages):
    pno = 108 + idx
    words = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>', body)
    H = float(h)
    print(f'=== PAGE {pno} (H={H}, {len(words)} mots) ===')
    for x0, y0, x1, y1, txt in words:
        yf = float(y0) / H
        if any(k in txt for k in KEYS):
            print(f'  y={yf:.3f} [{float(y0):.0f}] {txt[:70]!r}')
