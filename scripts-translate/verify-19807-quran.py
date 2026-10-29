#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérification quran-cache 19807 — v2 (sondes calibrées sur le DESSIN).
bare(): dépouille diacritiques + khanjariyya + tatweel ; normalise أ/إ/آ/ٱ -> ا
 mais garde ء/ؤ/ئ (dessins distincts)."""
import json, re

CACHE = '/home/z/my-project/scripts-translate/quran-cache.json'
with open(CACHE, encoding='utf-8') as f:
    Q = json.load(f)

def bare(s):
    s = re.sub(r'[\u064B-\u0652\u0670\u0640\u0653-\u0655\u08F0-\u08F3\u06D6-\u06ED]', '', s)
    s = s.replace('\u0671', '\u0627').replace('\u0623', '\u0627').replace('\u0625', '\u0627').replace('\u0622', '\u0627')
    return s

def find(pat, exact=True, suras=None):
    hits = []
    sk = [str(s) for s in suras] if suras else [str(i) for i in range(1, 115)]
    for sk1 in sk:
        if sk1 not in Q: continue
        for a in Q[sk1]['ar']:
            for w in a[1].split():
                b = bare(w)
                if (b == pat) if exact else (pat in b):
                    hits.append((int(sk1), a[0], w))
    return hits

def show(label, hits, lim=16):
    print(f'== {label} : {len(hits)} positions')
    for s, a, w in hits[:lim]:
        print(f'   {s}:{a}  {w}')
    if len(hits) > lim:
        print(f'   ... (+{len(hits)-lim})')

print('====== SECTION I : WASATAN ======')
show('ءالاء (fente 1)', find('ءالاء'))
show('جلاء (fente 2)', find('جلاء'))
show('هؤلاء (fente 3, hāʾ tanbīh)', find('هؤلاء'))
show('اولاء (fente 4, مجرد)', find('اولاء'))
show('اولئكم (fente 5, kāf -> ḥaḏf)', find('اولئكم'))
show('هانتم (glose اولاء)', find('هانتم'))
print('--- al-Ǧinn (72) : tout mot avec ان/لان ---')
for a in Q['72']['ar']:
    for w in a[1].split():
        b = bare(w)
        if 'لان' in b or b == 'ان' or b == 'الان':
            print(f'   72:{a[0]}  {w}  (bare={b})')
show('الان (constant, tout muṣḥaf)', find('الان'))
show('بل : sūras 2,7,8,14,37,44', find('بل', exact=False, suras=[2,7,8,14,37,44]))
show('لات (al-Lāt)', find('لات', exact=False))
show('اخلا (aḫillāʾ)', find('اخلا', exact=False))
show('بلغا (constante بلاغ?)', find('بلغا', exact=False))
show('خلا exact', find('خلا'))
show('خلاا contains (خلئف?)', find('خلاا', exact=False))
show('خئف contains', find('خئف', exact=False))

print()
print('====== SECTION II : TARAFAN ======')
show('الا nu (إلا+ألا+ألا un dessin)', find('الا'), lim=45)
show('لولا', find('لولا'), lim=6)
show('رسول + fin ا (duel?)', [(s,a,w) for s,a,w in find('رسول', exact=False) if bare(w).endswith('ا')])
show('سبيل + fin ا (duel?)', [(s,a,w) for s,a,w in find('سبيل', exact=False) if bare(w).endswith('ا')])
show('علا exact', find('علا'))
print('--- 18:61 (duel) ---')
print('   ', Q['18']['ar'][60][1][:130])
show('على (particule, yāʾ) ex.', find('على'), lim=3)
