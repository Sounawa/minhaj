# -*- coding: utf-8 -*-
"""verify-19807-quran3.py — passe 3 : formes uniques par lexème + versets pivots."""
import json, re, unicodedata

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

def forms(motif):
    """formes bare2 (dict) contenant le motif → liste (s:a, raw)"""
    seen = {}
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            for w in W(p[1]):
                b = bare2(w)
                if motif in b:
                    seen.setdefault(b, []).append((s, i+1, w))
    return seen

def show(label, motif, maxf=12):
    seen = forms(motif)
    print(f'\n-- {label} [{motif}] : {len(seen)} formes')
    for b, pos in sorted(seen.items(), key=lambda x: -len(x[1]))[:maxf]:
        print(f'   «{b}» n={len(pos)} ex: {pos[0][0]}:{pos[0][1]} «{pos[0][2]}»')

show('al-Jinn 72 ān ?', 'لان')
show('hāʾulāʾi', 'هول')
show('ulāʾi / ulālikum', 'اول')
show('jalāʾa', 'جلاء')
show('aḫillāʾu', 'اخلا')
show('lāta fin', 'لات')
show('duel rasūl', 'رسول')
show('al-Lāt', 'لاة')

print('\n== VERSETS PIVOTS (rasm exact) ==')
for (s, a) in [(37, 106), (44, 33), (2, 49), (38, 24), (16, 92), (106, 2), (53, 19), (28, 4), (2, 76)]:
    txt = data.get(str(s), {}).get('ar', [])[a-1][1]
    print(f'{s}:{a}  {txt[:110]}')
print('\nDONE pass3')
