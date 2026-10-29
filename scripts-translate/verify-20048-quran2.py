# -*- coding: utf-8 -*-
"""verify-20048-quran2.py — sondes 2 pour 20048 (recensements fins)."""
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

def sous(chaine, label):
    print(f'\n## {label} — sous-chaîne «{chaine}» (bare2 du mot)')
    n = 0
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            for w in W(p[1]):
                if chaine in bare2(w):
                    n += 1
                    print(f'   {s}:{i+1} «{w}» :: {p[1][:100]}')
    if n == 0: print('   (aucune)')

def seq_mots(seq, label):
    print(f'\n## {label} — séquence adjacente {[bare2(x) for x in seq]}')
    n = 0
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            bs = [bare2(w) for w in W(p[1])]
            for j in range(len(bs)-len(seq)+1):
                if bs[j:j+len(seq)] == [bare2(x) for x in seq]:
                    n += 1
                    print(f'   {s}:{i+1} :: {p[1][:110]}')
    if n == 0: print('   (aucune)')

def mots_exact(*forms, label=''):
    print(f'\n## {label} — formes exactes {list(forms)}')
    n = 0
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            for w in W(p[1]):
                if bare2(w) in [bare2(f) for f in forms]:
                    n += 1
                    print(f'   {s}:{i+1} «{w}» :: {p[1][:100]}')
    if n == 0: print('   (aucune)')

# 1. Le recensement complet de sīmāhum (sous-chaîne, capture بسيماهم inclus)
sous('سيماهم', '1. sīmāhum — recensement intégral')

# 2. ʿimāra — sous-chaînes (عمارت, عماره, عمرت)
sous('عمارت', '2a. ʿimāra (عمارت)')
sous('عماره', '2b. ʿimāra (عماره)')

# 3. law mā — séquence لو ما
seq_mots(['لو', 'ما'], '3. law mā (لو + ما adjacents)')

# 4. wa-immā nuriyannaka
mots_exact('نريانك', label='4a. nuriyannaka (نريانك)')
seq_mots(['وإما', 'نريانك'], '4b. wa-immā nuriyannaka (وإما + نريانك)')

# 5. fa-ammā alladhīna
seq_mots(['فاما', 'الذين'], '5. fa-ammā alladhīna (فاما + الذين)')

# 6. annamā / innamā — premières positions
mots_exact('أنما', label='6a. annamā (أنما) — toutes')
mots_exact('انما', label='6b. innamā (انما) — premières')

# 7. thamānī — toutes positions brutes
mots_exact('ثمانية', 'ثمانين', 'ثماني', label='7. thamānī — lexème entier')

# 8. ẓulumāt — toutes
mots_exact('ظلمت', label='8. ẓulumāt — toutes positions')

# 9. samāʿūn — toutes
mots_exact('سماعون', label='9. samāʿūn — toutes positions')

# 10. Sulaymān — comptage
sous('سليمان', '10. Sulaymān — comptage')

# 11. tamurru (27:88) + confirmation
mots_exact('تمر', 'تمرون', label='11. tamurru (تمر)')

# 12. tusammā / yusammā
mots_exact('تسمى', 'يسمى', label='12. tusammā / yusammā')

# 13. jimalāt (77:33) confirmation du rasm
mots_exact('جملت', label='13. jimalāt — rasm sans alif ?')

# 14. maʿlūmāt — les 2 positions
mots_exact('معلومت', label='14. maʿlūmāt — les 2')

# 15. ayyimā (28:28)
mots_exact('ايما', label='15. ayyimā')

# 16. mahmā (مَهْمَا) — Quranic ?
mots_exact('مهما', label='16. mahmā (مهما)')

# 17. rabamā (رُبَمَا)
mots_exact('ربما', label='17. rabamā (ربما)')

# 18. ḫulfu (الخلْف du Raḥḥālī) — inline check
mots_exact('الخل', label='18. ḫulfa')

print('\n== FIN DES SONDES 2 ==')
