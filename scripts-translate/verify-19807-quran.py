# -*- coding: utf-8 -*-
"""verify-19807-quran.py — sondes coraniques pour 19807 (le lām, R348)."""
import json, re, unicodedata
from collections import Counter

data = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json', encoding='utf-8'))

def bare(t):
    return ''.join(c for c in t if not unicodedata.category(c).startswith('M') and c != '\u0640').replace('\u0671', '\u0627')

corp = {}
for s in range(1, 115):
    corp[s] = [(i+1, bare(p[1]), p[1]) for i, p in enumerate(data.get(str(s), {}).get('ar', []))]

W = lambda s: re.split(r'[\s\u00a0]+', s.strip())

def hunt(sk, show=8, whole=False):
    out = []
    for s in range(1, 115):
        for a, t, raw in corp[s]:
            if whole:
                hit = any(w == sk for w in W(t))
            else:
                hit = sk in t
            if hit:
                wraw = next((w for w in W(raw) if (bare(w) == sk if whole else sk in bare(w))), '')
                out.append((s, a, wraw))
    tag = 'WORD' if whole else 'SUB'
    print(f'\n== [{sk}] {tag} = {len(out)}')
    for s, a, w in out[:show]:
        print(f'   {s}:{a} «{w}»')
    if len(out) > show:
        cnt = Counter(x[0] for x in out)
        print(f'   …+{len(out)-show} ; sūras: {dict(sorted(cnt.items()))}')
    return out

# A. mot du naẓīm kālān (élidé au milieu) — kāla, kālāt ?
hunt('كالن'); hunt('كالت'); hunt('كلت'); hunt('قالتا'); hunt('قالن')
# B. ālāna — le lexème élidé partout SAUF sūra al-Jinn (72) constante
hunt('الان'); hunt('الاا')
# C. balāʾ — constant hors 44, élidé ×2 (Ṣāffāt 37 + Ḫān 44) ?
hunt('بلاء'); hunt('بلء'); hunt('بلوا'); hunt('بلا')
# D. hāʾulāʾi élidée
hunt('هولاء'); hunt('هولء')
# E. ulālikum (conjoint au kāf élidé) / ūlāʾi sans kāf
hunt('اوللكم'); hunt('اولاء')
# G-H. ālāʾa / jalāʾa élidées
hunt('الاء'); hunt('الااء'); hunt('جلا')
# I. lāta constante
hunt('لات'); hunt('لاة'); hunt('لاات'); hunt('الاط')
# J. aḫillāʾu constante
hunt('اخلاا'); hunt('اخلا'); hunt('اخلاء')
# K-L. les deux duels constantes
hunt('رسولا'); hunt('رسولن'); hunt('سبيلن'); hunt('سبيلي')
# M. ʿalā verbale (word) — contrast sur ʿalā préposition
hunt('علا', whole=True, show=14); hunt('علي', whole=True, show=6)
# N. particules constantes (comptes)
hunt('لولا', whole=True, show=4); hunt('خلا', whole=True, show=4); hunt('كلا', whole=True, show=4)
hunt('الا', whole=True, show=5)
# O. iḥtirāz : إلا Allah / إلا الذين
hunt('الله', whole=True, show=0)
print('\nDONE verify-19807')
