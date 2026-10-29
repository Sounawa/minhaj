# -*- coding: utf-8 -*-
"""verify-19818-quran.py — sondes coraniques pour 19818 (le lām II, R349)."""
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

W = lambda s: re.split(r'[\s\u00a0]+', s.strip())

def lexemes(prefixes):
    """formes uniques (bare2 → raw + positions) commençant par l'un des préfixes"""
    seen = {}
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            for w in W(p[1]):
                b = bare2(w)
                if any(b.startswith(pr) for pr in prefixes):
                    seen.setdefault(b, []).append((s, i+1, w))
    for b, pos in sorted(seen.items(), key=lambda x: -len(x[1])):
        raws = Counter(w for _, _, w in pos)
        ex = pos[0]
        print(f'   «{b}» n={len(pos)} raws={dict(raws)} ex {ex[0]}:{ex[1]} «{ex[2]}»')

print('== صل* (le rasm de ṣalāt : wāw vs alif) ==')
lexemes(['صلو', 'صلات', 'صلوت', 'صلت'])
print('\n== زك* (bonus zakāt) ==')
lexemes(['زكو', 'زكات', 'زكوت', 'زكت'])
print('\n== مولى/تولى (muṭarrafa au yāʾ) ==')
lexemes(['مول', 'تول', 'لولي', 'ااولي'])
print('\n== في صلاتهم (bigramme) ==')
n = 0
for s in range(1, 115):
    if n > 3: break
    for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
        bars = [bare2(w) for w in W(p[1])]
        for k in range(len(bars)-1):
            if bars[k] == 'في' and bars[k+1].startswith('صلات'):
                print(f'   {s}:{i+1} «{W(p[1])[k]} {W(p[1])[k+1]}» :: {p[1][:70]}')
                n += 1
                break
print('\nDONE verify-19818')
