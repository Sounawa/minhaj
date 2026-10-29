# -*- coding: utf-8 -*-
"""verify-19820-quran2.py — passe 2 : bare3 (aksár normalisés) + substrings + positions complètes."""
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

def cite(s, v):
    return data[str(s)]['ar'][v-1][1]

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

def positions(label, needles):
    print(f'\n## {label} — positions de {needles}')
    n = 0
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            for w in W(p[1]):
                b = bare3(w)
                if any(b == nd or b.startswith(nd) for nd in needles):
                    n += 1
                    if n <= 12:
                        print(f'   {s}:{i+1} «{w}» :: {p[1][:75]}')
    print(f'   total = {n}')

sub('māhidūn', 'اهد')
sub('Hāmān', 'هام')
sub('Ismāʿīl', 'اسماع')
sub('kalimāt (toutes formes)', 'كلم')
sub('ṣāʾimāt', 'صءمت')
sub('imām', 'امام')
sub('asmāʾ', 'اسما')
sub('amāna/amānāt', 'امان')
sub('īmān/aymān', 'ايمن')
sub('aʿmāl/aʿmal', 'اعم')
sub('samāwāt (avec article)', 'السموت')
sub('ġamām', 'غمام')
sub('ar-Raḥmān', 'الرحمن')
sub('aʿmām', 'عمام')
sub('mākirīn', 'ماكر')

positions('Luqmān (exact)', ['لقمن', 'لقمان'])
positions('ḥurumāt (élidée vs verbe)', ['حرمت', 'حرما'])
positions('Sulaymān (échantillon)', ['سليمن', 'سليمان'])
positions('malik/mulk bare3 «ملك» nu', ['ملك'])

# inspection codepoints — le duel et aʿmām
print('\n=== INSPECTION CODEPOINTS ===')
for s, v, wtxt in [(2,102,'yuʿallimāni'), (21,78,'yaḥkumāni'), (24,61,'aʿmāmikum ? / ʿammatikum'), (17,71,'bi-imāmihim'), (15,79,'labi-imāmin'), (33,72,'al-amāna (constante)'), (8,2,'īmānan'), (4,22,'aymānakum'), (31,12,'Luqmān')]:
    for w in W(cite(s, v)):
        b = bare3(w)
        if ('اعلم' in b or 'يعلمان' in b or 'يحكمان' in b or 'امام' in b or 'امان' in b or 'ايمن' in b or 'اعمام' in b or 'عمام' in b or 'لقمن' in b):
            codes = ' '.join(f'U+{ord(c):04X}({c})' for c in w if ord(c) > 0x600)
            print(f'   {s}:{v} «{w}» :: {codes}')

print('\nDONE verify-19820-quran2')
