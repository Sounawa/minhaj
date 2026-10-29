# -*- coding: utf-8 -*-
"""verify-18920-quran.py — sondes coraniques pour 18920 (les jours de l'année arabe, fātiḥ muḥarram)."""
import json, re, unicodedata
from collections import Counter

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
                        print(f'   {s}:{i+1} :: {p[1][:120]}')
    if n == 0:
        print('   ✗ AUCUNE position')
    elif n > maxn:
        print(f'   ... {n} positions')

def mot(label, *forms, show=8):
    print(f'\n## {label} — formes exactes {forms}')
    hits = []
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            for w in W(p[1]):
                if bare2(w) in forms:
                    hits.append((s, i+1, w, p[1]))
    for s, v, w, txt in hits[:show]:
        print(f'   {s}:{v} «{w}» :: {txt[:100]}')
    if len(hits) > show: print(f'   ... {len(hits)} positions au total')

# === Sonde 1 — 10:5 le verset-programme (liminaire de la leçon, āya en fente) ===
contient(['منازل', 'لتعلموا', 'عدد', 'السنين'], 'S1. 10:5 manāzila li-taʿlamū ʿadada s-sinīna (U+06E5 dans وقدرهۥ)')
contient(['لعلموا', 'عدد', 'السنين', 'والحساب'], 'S1b. 10:5 li-taʿlamū ʿadada s-sinīna wa-l-ḥisāba (fin)')

# === Sonde 2 — 9:36 les douze mois (définition de l'année arabe, āya en fente) ===
contient(['ان', 'عدة', 'الشهور', 'عند', 'الله'], 'S2. 9:36 inna ʿiddaṫa š-šuhūri ʿinda llāhi')
contient(['اثنا', 'عشر', 'شهرا', 'في', 'كتب', 'الله'], 'S2b. 9:36 iṯnā ʿašara šahrān fī kitābi llāhi (cache : كتب sans alif)')
contient(['منها', 'اربعة', 'حرم'], 'S2c. 9:36 minhā arbaʿatun ḥurum (les mois sacrés — muḥarram)')

# === Sonde 3 — 2:189 la vision du croissant (rūʾyat al-hilāl de la définition) ===
contient(['هي', 'موقيت', 'للناس'], "S3. 2:189 hiya l-mawāqītu li-n-nāsi (l'hilāl)")
contient(['النسيء', 'زيادة', 'في', 'الكفر'], 'S3b. 9:37 an-nasīʾ (la ziyāda dans les années — le nasīʾ du calendrier)')
contient(['والشمس', 'والقمر', 'حسبان'], 'S6b. 6:96 wa-š-šamsa wa-l-qamara ḥusbān')

# === Sonde 4 — le lexique des années/lune (contexte de vocabulaire) ===
mot('S4. suns/sanat (les années)', 'سند', 'سنين', 'سنين', 'السنين', 'السنة', 'سنون', 'السنون')
mot('S5. al-qamar + š-šams jumeaux', 'والقمر', 'والشمس', 'الشمس', 'القمر')

# === Sonde 6 — 17:12 la seconde occurrence (déjà calibrée à R353) ===
contient(['عدد', 'السنين', 'والحساب'], 'S6. occurrences « ʿadada s-sinīna wa-l-ḥisāba » (10:5 + 17:12)')

# === Sonde 7 — la fraction et le kabis : le lexique الزيادة ===
mot('S7. al-ziyāda (contexte du kabs)', 'زيده', 'الزيادة', 'يزيد', 'زيادة', 'كبس', 'الكبس')
mot('S8. al-ḫums (le quint du bayt)', 'الخمس', 'الخمسة', 'خمس')
mot('S9. as-suds (le six du bayt)', 'السدس', 'السادس', 'سدسه', 'السدسة')
