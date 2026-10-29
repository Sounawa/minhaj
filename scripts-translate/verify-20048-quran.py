# -*- coding: utf-8 -*-
"""verify-20048-quran.py — sondes coraniques pour 20048 (faṣl al-mīm 2, bayts 118-123)."""
import json, re, unicodedata
from collections import Counter

data = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json', encoding='utf-8'))

def bare3(t):
    out = []
    for c in t:
        if unicodedata.category(c).startswith('M') or c == '\u0640':
            continue
        if c in '\u0622\u0623\u0625\u0671': c = '\u0627'
        if c == '\u0649': c = '\u064a'
        out.append(c)
    return ''.join(out)

W = lambda s: re.split(r'[\s\u00a0]+', s.strip())
def cite(s, v): return data[str(s)]['ar'][v-1][1]

def sub(label, needle):
    print(f'\n== {label} — bare3 substring «{needle}» ==')
    seen = {}
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            for w in W(p[1]):
                b = bare3(w)
                if needle in b:
                    seen.setdefault(b, []).append((s, i+1, w))
    for b, pos in sorted(seen.items(), key=lambda x: -len(x[1])):
        raws = Counter(w for _, _, w in pos)
        ex = pos[0]
        print(f'   «{b}» n={len(pos)} raws={dict(raws)} ex {ex[0]}:{ex[1]}')
    if not seen: print('   (aucune)')

# le mot des six positions
sub('sīmāhum/sīmīhum', 'سيم')
sub('mahr (variante)', 'مهر')
sub('tumārūnahu', 'تمار')
sub('ǧimālāt', 'جمالت')
sub('ṯamānī/ṯamāniyāt', 'ثمن')
sub('tamāṯīl', 'تمث')
sub('ʿimāra', 'عمر')
sub('sammāʿūna', 'سمعون')
sub('ḫiṣmān', 'خصم')
sub('ʿalamāt', 'علمت')
sub('ẓulumāt', 'ظلمت')
sub('maʿlūmāt', 'معلومت')
sub('muqassimāt', 'قس')
sub('yaqūmāni', 'يقم')
sub('tussammā', 'تسمى')
sub('lawmā', 'لوما')
sub('ayyamā', 'أيما')
sub('bimā/rubamā', 'بما')
sub('pronoms duel (تما)', 'تما')
sub('maqṣūr aʿmā/ramā (ى)', 'عمى')

# positions complètes du mot central
print('\n## POSITIONS COMPLÈTES سيماهوم/سيميهم ##')
for s in range(1, 115):
    for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
        for w in W(p[1]):
            b = bare3(w)
            if 'سيم' in b or 'سيماهوم' in b:
                print(f'   {s}:{i+1} «{w}» :: {p[1][:70]}')

print('\nDONE verify-20048')
