# -*- coding: utf-8 -*-
"""verify-19333-quran.py — sondes coraniques pour 19333 (le ẓuhr et le ʿaṣr par le ẓill du Soleil).
Horizon : al-Furqān 25:45-46 — le ẓill étendu par le Seigneur, le Soleil fait dalīl."""
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

# === Fente 1 — le ẓill étendu (al-Furqān 25:45) ===
contient(['كيف', 'مد', 'الظل'], 'F1. 25:45 kayfa madda ẓ-ẓill (le ẓill étendu)')
contient(['لجعله', 'ساكنا'], 'F1b. 25:45 la-ǧaʿalahu sākinā (lʼombre faite immobile)')
contient(['جعلنا', 'الشمس', 'عليه', 'دليلا'], 'F1c. 25:45 ǧaʿalnāš-šamsa ʿalayhi dalīlā (le Soleil fait dalīl)')
contient(['قبضناه', 'الينا', 'قبضا', 'يسيرا'], 'F1d. 25:46 qabaḍnāhu ilaynā qabḍan yasīrā (la reprise aisée)')

# Impressions intégrales pour citation exacte
verse(25, 45)
verse(25, 46)

# === Fente 2 — contrôle : le ẓill et al-ʿaš (lʼaprès-midi) — an-Naḥl 16:12 ? non retenu ===
contient(['الليل', 'النهار', 'الشمس', 'القمر'], 'F2. contrôle 16:12 / 41:37 (la nuit, le jour, le Soleil, la Lune)')
