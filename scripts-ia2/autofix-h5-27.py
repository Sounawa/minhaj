#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-32 — auto-fix pdf-27.html : U+202F, demi-anneaux -> ', coquilles
import re

P = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-27.html'
h = open(P, encoding='utf-8').read()

h = h.replace('\u02bf', '\u2019').replace('\u02be', '\u2019')
h = h.replace('marbata-y ', 'marbata-y ')  # no-op garde
h = h.replace('’afḍala marbataw-wa-falāḥā', '’afḍala marbataw-wa-falāḥā')

h = re.sub(r'« +', '«\u202f', h)
h = re.sub(r' +»', '\u202f»', h)
h = re.sub(r' +([;:!?])', '\u202f\\1', h)

open(P, 'w', encoding='utf-8').write(h)
print('écrit', len(h), 'car')
assert "'" not in h, 'apostrophe droite résiduelle'
assert '\u02bf' not in h and '\u02be' not in h
assert '\ufdfa' not in h and '﴿' not in h and '﴾' not in h
assert '\u00a0' not in h
print('«=', h.count('«'), ' »=', h.count('»'))
print('U+202F:', h.count('\u202f'))
print('h1:', h.count('<h1>'), 'h2:', h.count('<h2>'), 'h3:', h.count('<h3>'))
print('arabe hors spans:', re.findall(r'[\u0600-\u06FF]+', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', h))[:5])
print('OK')
