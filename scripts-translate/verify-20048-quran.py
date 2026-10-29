# -*- coding: utf-8 -*-
"""verify-20048-quran.py — sondes coraniques pour 20048 (faṣl al-mīm 2, bayts 118-123)."""
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

def lexemes(prefixes, label, maxn=14):
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
        n = len(pos)
        print(f'   «{b}» n={n} raws={dict(list(raws.items())[:4])} ex {ex[0]}:{ex[1]}' + (f' (+{n-1} autres)' if n > maxn else ''))

def mots(label, *forms, show=6):
    print(f'\n## {label} — formes exactes {forms}')
    hits = []
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            for w in W(p[1]):
                if bare2(w) in forms:
                    hits.append((s, i+1, w, p[1]))
    for s, v, w, txt in hits[:show]:
        print(f'   {s}:{v} «{w}» :: {txt[:90]}')
    if len(hits) > show: print(f'   ... {len(hits)} positions au total')

def contient(seq, label, maxn=10):
    """recherche d'une séquence de mots adjacents (bare2) dans un même aya"""
    print(f'\n## {label} — séquence {seq}')
    n = 0
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            bs = [bare2(w) for w in W(p[1])]
            for j in range(len(bs)-len(seq)+1):
                if bs[j:j+len(seq)] == list(seq):
                    n += 1
                    if n <= maxn:
                        print(f'   {s}:{i+1} :: {p[1][:110]}')
    if n > maxn: print(f'   ... {n} positions')

# === A. Le lexème tamr (F1-F4) ===
lexemes(['تمر', 'امر'], 'A. tamar / af-tamrūnah (F1-F3)')
mots('A2. exact temrūn', 'تمرونه', 'يتمرون', 'تمروا')

# === B. jimalāt (F5) ===
lexemes(['جملت', 'جملت', 'جمالت', 'جمل'], 'B. jimalāt (F5)')

# === C. les huit / الثامن (F6-F8) ===
lexemes(['ثمن', 'ثامن', 'ثمان'], 'C. th-thāmin / th-thamāniya')

# === D. kayfamā + les compositeurs de مā (F26-F33) ===
mots('D1. kayfamā', 'كيفما', 'كيفمهما')
mots('D2. annamā / innamā (avec hamza conservée)', 'أنما', 'انما', 'أنما', 'إانما')
mots('D3. lammā (l+mā)', 'لما')
mots('D4. rubamā / bimā / fīmā', 'ربما', 'بما', 'فيما')
mots('D5. ayyimā', 'ايما', 'أيما')
mots('D6. lawmā', 'لوما')
mots('D7. mā duels: ذلCOMEكم / تلكما / لكما / لهما / أنتما / دلّيهما',
     'ذلكما', 'تلكما', 'لكما', 'لهما', 'انتما', 'دليهما')

# === E. qūman / yaqūman (F19-F20) ===
lexemes(['قومن', 'قمن', 'يقوم'], 'E. yaqūmani (F19-F20) — rasm nāni')

# === F. plurals fém. sains (F21-F24) ===
lexemes(['علمت', 'علامت'], 'F1. ʿalamāt (F21)')
lexemes(['ظلمت'], 'F2. ẓulumāt (F22)')
lexemes(['معلومت'], 'F3. maʿlūmāt (F23)')
lexemes(['مقسمت'], 'F4. al-muqassimāt (F24)')
lexemes(['سمعون', 'سماعون'], 'F5. samʿūn (F25)')
lexemes(['خصمن', 'خصمان', 'خصم'], 'F6. khaṣmāni (bayt 1)')

# === G. tamthīl Saba (F9-F10) ===
lexemes(['تمثيل', 'مثيل'], 'G1. tamthīl (F9)')
contient(['سبا'], 'G2. sabaʾ (contexte)')

# === H. ʿimāra (F11) ===
lexemes(['عمارة', 'عمره', 'عامر', 'عمرو', 'يعمر', 'عمران', 'عمار'], 'H. ʿimāra / ʿāmir (F11)')

# === I. sīmāhum (F13-F18) — tout le lexème ===
lexemes(['سيم', 'سموا', 'وسم'], 'I. sīmāhum — lexème س-ي-م complet (F13-F18)')

# === J. tusammā (F34) ===
lexemes(['تسمي', 'تسمى', 'تسمم', 'مسما'], 'J. tusammā (F34) + musammā')

# === K. quoi d'autre — إمّا مشدّد ===
lexemes(['امّا', 'إما', 'اما'], 'K. innamā/ammā mušaddad (وَإِمَّا نُرِيَنَّكَ / فَأَمَّا الَّذِينَ)')

# === L. ما muǧarrad — le mot ʾayy / كم ===
mots('L. mā nue (forme كلمة وما)', 'ما', 'وما', 'فما')

print('\n== FIN DES SONDES ==')
