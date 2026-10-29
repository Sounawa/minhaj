# -*- coding: utf-8 -*-
"""verify-19820-quran.py — sondes coraniques pour 19820 (faṣl al-mīm, bayts 113-117)."""
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

def lexemes(prefixes, label):
    print(f'\n== {label} ==')
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
        print(f'   «{b}» n={len(pos)} raws={dict(raws)} ex {ex[0]}:{ex[1]}')

def mots(label, *forms):
    """recherche de forms bare2 EXACTES, impression raw complète + citation"""
    print(f'\n## {label} — formes exactes {forms}')
    hits = []
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            for w in W(p[1]):
                if bare2(w) in forms:
                    hits.append((s, i+1, w, p[1]))
    for s, v, w, txt in hits[:8]:
        print(f'   {s}:{v} «{w}» :: {txt[:90]}')
    if len(hits) > 8: print(f'   ... {len(hits)} positions au total')

# --- I. Règles générales ---
lexemes(['يعلم', 'يقسم', 'يحكم'], 'I.1 LES DUELS : yuʿallimāni / yuqsimāni / yaḥkumāni (rasm nāni)')
lexemes(['كلمت', 'كلمات'], 'I.2 kalimāt (pluriel fém. sain)')
lexemes(['صايم', 'صائم', 'صييم'], 'I.2 ṣāʾimāt')
lexemes(['محكم'], 'I.2 muḥkamāt')
lexemes(['عمت', 'عما'], 'I.2 ʿammati')
lexemes(['مسلم'], 'I.2 muslimāt (et tout مسلم*)')
lexemes(['حرم', 'حرما'], 'I.2 ḥurumāt (et haram/ḥarām)')
lexemes(['ماكر', 'ماكرو'], 'I.3 al-mākirīn')
lexemes(['ماهد', 'مها'], 'I.3 māhidūn')
lexemes(['مكث', 'مي كث'], 'I.3 mākithūn/mākithīn')

# --- I.4 Noms aʿjamī ---
lexemes(['لقمن', 'لقمان'], 'I.4 Luqmān')
lexemes(['هامن', 'هامان'], 'I.4 Hāmān')
lexemes(['اسماعيل', 'اسمعيل'], 'I.4 Ismāʿīl')
lexemes(['سليمان', 'سليمن'], 'I.4 Sulaymān')

# --- II. Exceptionnelles sans règle ---
lexemes(['غمام', 'غمم'], 'II.1 al-ġamām')
lexemes(['علماء', 'علمائ', 'علمؤ'], 'II.1 ʿulamāʾ')
lexemes(['ايمان', 'ايمن'], 'II.1 īmān')
lexemes(['ايم'], 'II.1 aymān (tous)')
lexemes(['اعم'], 'II.1 aʿmal/aʿmāl (tous)')
lexemes(['سماوت', 'سموت', 'سمات'], 'II.1 samāwāt (rasm)')
lexemes(['عمام'], 'II.1 aʿmām')
lexemes(['رحمن', 'رحمان'], 'II.1 ar-Raḥmān')

# --- II.2 Avec istithnāʾ ---
lexemes(['امام'], 'II.2 imām')
lexemes(['اسما'], 'II.2 asmāʾ')
lexemes(['امان'], 'II.2 amāna/amānāt (et amān*)')

# --- Formes exactes ciblées ---
mots('malak fini (élidé ملك vs مالك)', 'ملك', 'مالك', 'ملٰك')
mots('yuʿallimāni exact', 'يعلمٰن', 'يعلمان', 'يعلمٰني', 'يعلماني')
mots('yuqsimāni exact', 'يقسمٰن', 'يقسمان', 'يقسمٰني', 'يقسماني')
mots('yaḥkumāni exact', 'يحكمٰن', 'يحكمان', 'يحكمٰني', 'يحكماني')

print('\nDONE verify-19820')
