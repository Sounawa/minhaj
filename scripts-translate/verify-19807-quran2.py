# -*- coding: utf-8 -*-
"""verify-19807-quran2.py — passe 2 : bare2 (آ→ا, ى→ي) + rasm exacts cibles."""
import json, re, unicodedata
from collections import Counter

data = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json', encoding='utf-8'))

def bare2(t):
    out = []
    for c in t:
        if unicodedata.category(c).startswith('M') or c == '\u0640':
            continue
        if c == '\u0622': c = '\u0627'
        if c == '\u0649': c = '\u064a'
        out.append(c)
    return ''.join(out).replace('\u0671', '\u0627')

corp = {}
for s in range(1, 115):
    corp[s] = [(i+1, bare2(p[1]), p[1]) for i, p in enumerate(data.get(str(s), {}).get('ar', []))]

W = lambda s: re.split(r'[\s\u00a0]+', s.strip())

def hunt(sk, show=7, whole=False):
    out = []
    for s in range(1, 115):
        for a, t, raw in corp[s]:
            hit = any(w == sk for w in W(t)) if whole else sk in t
            if hit:
                wraw = next((w for w in W(raw) if (bare2(w) == sk if whole else sk in bare2(w))), '')
                out.append((s, a, wraw))
    tag = 'WORD' if whole else 'SUB'
    print(f'\n== [{sk}] {tag} = {len(out)}')
    for s, a, w in out[:show]:
        print(f'   {s}:{a} «{w}»')
    if len(out) > show:
        cnt = Counter(x[0] for x in out)
        print(f'   …+{len(out)-show} ; sūras: {dict(sorted(cnt.items()))}')
    return out

# B. ālāna (le lexème élidé partout sauf al-Jinn constante)
hunt('الان'); hunt('الاان')
# hāʾulāʾi / ulāʾi sans kāf / conjoint au kāf
hunt('هولاء'); hunt('اولاء'); hunt('اولئ')
# balāʾ élidées 37/44
hunt('بلاء')
# jalāʾa / aḫillāʾu / lāta / les duels
hunt('جلااء'); hunt('الاخلا'); hunt('لاات'); hunt('رسولان'); hunt('سبيلا')
# kallā (كَلَّا) vs kullā (كُلَّا)
out = hunt('كلا', whole=True, show=0)
kalla = [x for x in out if x[2].startswith('كَلَّ')]
print('  → kallā (كَلَّا):', len(kalla), [f'{s}:{a}' for s, a, _ in kalla[:12]])
print('  → kullā (كُلَّا):', len(out) - len(kalla))
print('\nDONE verify-19807 pass2')
