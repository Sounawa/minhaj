# -*- coding: utf-8 -*-
"""verify-19335-quran.py — sondes coraniques pour 19335 (les heures, le ṭāliʿ, la manzila moyenne).
Horizon : al-Isrāʾ 17:12 — la nuit et le jour deux signes, le signe de la nuit effacé, celui du jour fait visible, pour connaître le nombre des années et le compte."""
import json, re, unicodedata

data = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json', encoding='utf-8'))

def bare2(t):
    out = []
    for c in t:
        if unicodedata.category(c).startswith('M') or c == '\u0640':
            continue
        if c == '\u0622': c = '\u0627'
        if c == '\u0623': c = '\u0627'
        if c == '\u0625': c = '\u0627'
        if c == '\u0671': c = '\u0627'
        if c == '\u0649': c = '\u064a'
        out.append(c)
    return ''.join(out)

W = lambda s: re.split(r'[\s\u00a0]+', s.strip())

def contient(seq, label, maxn=6):
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
    if n == 0:
        print('   ✗ AUCUNE position')
    elif n > maxn:
        print(f'   ... {n} positions')

def verse(s, i):
    p = data.get(str(s), {}).get('ar', [])
    if 0 < i <= len(p):
        print(f'\n>> {s}:{i} :: {p[i-1][1]}')
    else:
        print(f'\n>> {s}:{i} :: ✗ ABSENT')

# === Fente 1 — les deux signes (al-Isrāʾ 17:12) ===
contient(['جعلنا', 'الليل', 'النهار', 'ايتين'], 'F1. 17:12 ǧaʿalnā l-layla wa-n-nahāra āyatayn (les deux signes)')
contient(['محونا', 'اية', 'الليل'], 'F1b. 17:12 maḥawnā āyata l-layli (le signe de la nuit effacé)')
contient(['اية', 'النهار', 'مبصرة'], 'F1c. 17:12 āyata n-nahāri mubṣiratan (le signe du jour fait visible)')
contient(['لتعلموا', 'عدد', 'السينين', 'والحساب'], 'F1d. 17:12 li-taʿlamū ʿadada s-sinīna wa-l-ḥisāb (le nombre des années et le compte)')

# Impressions intégrales pour citation exacte
verse(17, 12)
