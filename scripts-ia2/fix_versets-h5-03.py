#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-3 — normalisation des citations coraniques de pdf-3 à la convention du corpus :
#   ﴿...﴾ [Sourate : N]  →  « ... » (Sourate X — verset N)
# (qa-lesson.py refuse les caractères arabes résiduels hors spans RTL ; U+FD3E/FD3F
#  sont dans la plage arabique. Convention observée : hadith-1ep/12797 etc.)
import re

P = '/home/z/my-project/repo-minhaj/scripts-ia2/livraisons/hadith-5ep/pdf-3.html'
src = open(P, encoding='utf-8').read()

# refs imprimées → sourate/verset
REFS = {
    "al-\u2019Anbiy\u0101\u2019": "Sourate al-\u2019Anbiy\u0101\u2019 — versets 26-27",
    "at-Ta\u1e25r\u012bm": "Sourate at-Ta\u1e25r\u012bm — verset 6",
    "al-Mudda\u1e6f\u1e6fir": "Sourate al-Mudda\u1e6f\u1e6fir — verset 31",
    "al-Baqara": "Sourate al-Baqara — verset 284",
    "a\u1e63-\u1e62\u0101ff\u0101t": "Sourate a\u1e63-\u1e62\u0101ff\u0101t — verset 96",
    "al-Qamar": "Sourate al-Qamar — verset 49",
    "al-\u1e24ad\u012bd": "Sourate al-\u1e24ad\u012bd — verset 22",
    "an-Na\u1e25l": "Sourate an-Na\u1e25l — verset 43",
    "al-\u2019Anf\u0101l": "Sourate al-\u2019Anf\u0101l — verset 2",
}

# 1) « ... » autour des ﴿﴾
src = src.replace('\ufd3f', '\u00ab\u00a0\u202f')
src = src.replace('\ufd3e', '\u00a0\u202f\u00bb')

# 2) refs : [Sourate&nbsp;\u202f: N] → (Sourate X — verset N)   (entité &nbsp; littérale)
_clean = lambda s: s.replace('&nbsp;', '').strip()
src = re.sub(
    r'\s*\[([^\[\]]+?)\u202f:\s*(\d+[\u2013-]\d*|\d+)\]',
    lambda m: ' (' + REFS.get(_clean(m.group(1)), _clean(m.group(1))) + ' — '
              + ('versets ' + m.group(2).replace('\u2013', '-') if '-' in m.group(2) or '\u2013' in m.group(2)
                 else 'verset ' + m.group(2)) + ')',
    src)

# 2-bis) dédoublonnage : « (Sourate X — verset N — verset N) » → « (Sourate X — verset N) »
src = re.sub(r'(\u2014 versets? [0-9\u2013-]+)\s*\u2014\s*versets? ([0-9\u2013-]+)\)',
             lambda m: m.group(1) + ')'
             if m.group(1).split()[-1].replace('\u2013', '-') == m.group(2).replace('\u2013', '-')
             else m.group(0), src)

# 3) la citation Investissement utilisait déjà « ... » + ref : uniformiser la sienne
src = re.sub(r'«\u00a0\u202fMais \[ne sont\] les croyants', '« Mais [ne sont] les croyants', src)
src = src.replace('à leur Seigneur.\u00a0\u202f» (Sourate al-\u2019Anf\u0101l — verset 2)',
                  'à leur Seigneur\u00a0\u202f» (Sourate al-\u2019Anf\u0101l — verset 2)')

open(P, 'w', encoding='utf-8').write(src)
print('OK — ﴿ restants :', src.count('\ufd3f') + src.count('\ufd3e'),
      '— [ refs restants :', len(re.findall(r'\[[^\]]*\u202f:', src)), ']')
