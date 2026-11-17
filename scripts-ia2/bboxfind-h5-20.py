#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-22 — localiser les mots-clés dans la couche bbox pp.111-113 (pour crops calibrés)
import re, sys

html = open('scripts-ia2/tmp/h5-20/bbox-111-113.html').read()
pages = re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', html, re.S)

# cibles : (page, substring à chercher dans le mot, étiquette)
TARGETS = [
    (111, 'قو', 'obj1-verb'), (111, 'مكتسب', 'obj1-muktasab'),
    (111, 'قدر', 'obj2-qudrat'), (111, 'تخصيل', 'obj2-tahsil'), (111, 'تخصي', 'obj2-tahsil2'),
    (111, 'طق', 'obj3-tabbik'),
    (111, 'ولكي', 'walikay'), (111, 'تستمر', 'tastamir'),
    (111, 'يعيش', 'ya-ish'), (111, 'امن', 'aman'),
    (111, 'السام', 'islam-nazzama'), (111, 'لعلاقات', 'al-iqat'),
    (111, 'نواع', 'anwaiha'), (111, 'تنى', 'a'ana'),
    (111, 'عان', 'i'ana'), (111, 'الحدث', 'al-hath'), (111, 'حسن', 'husn'),
    (111, 'التق', 'taqwa'),
    (111, 'خلق', 'khalaqnakum'), (111, 'شعوبا', 'shuu'ban'), (111, 'كروا', 'shuu-garble'),
    (111, 'الدالة', 'ad-dalla'), (111, 'محب', 'yuhibb'),
    (111, 'سو', 'uswa'), (111, 'امل', 'al-mathal'), (111, 'حسان', 'ihsan'),
    (111, 'انه', 'laka-ine'), (111, 'حكيم', 'azim'),
    (112, 'خف', 'tuballif'), (112, 'اتخذت', 'ittakhadhat'), (112, 'شه', 'ishtahar'),
    (112, 'النبوة', 'nubuwwa'), (112, 'خزي', 'yukhzik'),
    (112, 'تص', 'litasil-qualifier'),
    (112, 'ضع', 'ada'-anwan'), (112, 'تاس', 'munasiban-garble'),
    (112, 'ش', 'ashrah'),
    (112, 'انكر', 'adhkur'), (112, 'اتدل', 'astadillu'), (112, 'ترجم', 'atarjim'),
    (112, 'نصوص', 'nusus'), (112, 'وضع', 'wadi-iyyat'),
    (113, 'اترص', 'yattasif'), (113, 'تدل', 'yustadall'),
    (113, 'جر', 'haththa-garble'), (113, 'سئ', 'yusiu'),
    (113, 'قنع', 'aqni'), (113, 'المحسن', 'al-muhsin'),
    (113, 'بين', 'ubayyin'), (113, 'ضب', 'dabt'), (113, 'تك', 'mustadillan'),
    (113, 'س', 'tayas-ara'), (113, 'حف', 'ahfaz'), (113, 'بحث', 'abhath'),
]

for idx, (w, h, body) in enumerate(pages):
    pno = 111 + idx
    words = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>', body)
    W, H = float(w), float(h)
    for (tp, sub, label) in TARGETS:
        if tp != pno:
            continue
        hits = [(float(x0), float(y0), float(x1), float(y1), txt) for x0, y0, x1, y1, txt in words if sub in txt]
        for x0, y0, x1, y1, txt in hits:
            print(f'p{pno} [{label}] x=[{x0/W:.3f},{x1/W:.3f}] y=[{y0/H:.3f},{y1/H:.3f}] «{txt[:40]}»')
