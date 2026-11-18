#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-31 — auto-fix pdf-26.html : U+202F dans les guillemets, demi-anneaux -> ', coquilles
import re

P = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-26.html'
h = open(P, encoding='utf-8').read()

# 1) demi-anneaux -> U+2019 (convention série : ' pour hamza ET 'ayn)
h = h.replace('\u02bf', '\u2019').replace('\u02be', '\u2019')

# 2) coquilles
h = h.replace('L’maître Abū al-Qāsim al-Qushayrī', 'Le maître Abū al-Qāsim al-Qušayrī')
h = h.replace('al-Qushayrī', 'al-Qušayrī')
h = h.replace('ǧamī’il-muḫālafāt', 'ǧamī’i l-muḫālafāt')
h = h.replace('fī ǧamī’il-qur’āni', 'fī ǧamī’i l-qur’āni')
h = h.replace('’allim-nī', '’allimnī')
h = h.replace('ǧārahū', 'ǧārahu')

# 3) guillemets français : U+202F après « et avant » (sauf collés à la ponctuation)
h = re.sub(r'« +', '«\u202f', h)
h = re.sub(r' +»', '\u202f»', h)
# 3bis) U+202F avant toute ponctuation française double (; : ! ?) — convention pdf-25
h = re.sub(r' +([;:!?])', '\u202f\\1', h)

open(P, 'w', encoding='utf-8').write(h)
print('écrit', len(h), 'car')

# contrôles rapides
import sys
assert "'" not in h, 'apostrophe droite résiduelle'
assert '\u02bf' not in h and '\u02be' not in h
assert '\ufdfa' not in h and '﴿' not in h and '﴾' not in h
assert '\u00a0' not in h
print('«=', h.count('«'), ' »=', h.count('»'))
print('U+202F:', h.count('\u202f'))
print('h1:', h.count('<h1>'), 'h2:', h.count('<h2>'), 'h3:', h.count('<h3>'))
print('arabe hors spans:', re.findall(r'[\u0600-\u06FF]+', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', h))[:5])
print('OK')
