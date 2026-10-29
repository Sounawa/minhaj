# -*- coding: utf-8 -*-
"""verify-19820-quran3.py — passe 3 : versets bruts suspects + codepoints ciblés + positions rares."""
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
def verse(s, v, label=''):
    t = data[str(s)]['ar'][v-1][1]
    print(f'\n== {s}:{v} {label} ==\n   {t}')

# versets suspects
verse(51, 48, 'māhidūn attendu (fa-niʿma l-māhidūn)')
verse(28, 38, 'Hāmān nidāʾ attendu')
verse(28, 6, 'Hāmān muǧarrad attendu')
verse(19, 54, 'Ismāʿīl attendu')
verse(2, 136, 'Ismāʿīl (liste) attendu')
verse(33, 35, 'ṣāʾimāt + muslimāt attendus')
verse(17, 71, 'bi-imāmihim attendu')
verse(3, 54, 'al-mākirīn attendu')
verse(2, 210, 'al-ġamām (2e position)')
verse(26, 197, 'ʿulamāʾu banī Isrāʾīl')
verse(5, 108, 'aymān nu ?')
verse(2, 33, 'samāwāt + asmāʾihim')

# positions rares à localiser
def positions(label, needles):
    print(f'\n## {label}')
    n = 0
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            for w in W(p[1]):
                b = bare3(w)
                if any(b == nd for nd in needles):
                    n += 1
                    if n <= 14: print(f'   {s}:{i+1} «{w}» :: {p[1][:75]}')
    print(f'   total = {n}')

positions('aʿmāl NU (اعمال)', ['اعمال'])
positions('kalimāt élidée PURE (كلمت bare3)', ['كلمت'])
positions('kalimāt khanjariyya (كلمت bare3 vs ٰ)', ['كلمت'])  # brute
positions('aymān/īmān NU (ايمن)', ['ايمن'])
positions('muḥkamāt (محكمت + محكمه)', ['محكمت', 'محكمه', 'محكما'])
positions('ṣāʾimāt — essai صايمت/صايمات', ['صايمت', 'صايمات', 'صءمات'])

# codepoints ciblés
print('\n=== CODEPOINTS CIBLÉS ===')
targets = {
    (2,57): 'al-ġamām (alif ?)', (2,210): 'al-ġamām 2e',
    (26,197): 'ʿulamāʾu', (3,7): 'muḥkamāt khanjariyya', (47,20): 'muḥkamāt élidée pure',
    (2,37): 'kalimātin', (8,7): 'bi-kalimātihi', (66,5): 'muslimātin', (33,35): 'ṣāʾimāt/muslimāt',
    (24,61): 'aʿmāmikum + ʿammatikum', (33,72): 'al-amāna CONST', (18,3): 'mākithīna', (43,77): 'mākithūna + yā māliku',
}
for (s, v), lab in targets.items():
    for w in W(data[str(s)]['ar'][v-1][1]):
        b = bare3(w)
        if any(nd in b for nd in ['غمام','علم','محكم','كلمت','مسلم','صءم','صايم','اعمم','عمت','امان','مكث','املك','مالك','امل']):
            codes = ' '.join(f'U+{ord(c):04X}' for c in w if ord(c) > 0x600 and unicodedata.category(c).startswith('L'))
            print(f'   {s}:{v} «{w}» lettres: {codes}')

print('\nDONE verify-19820-quran3')
