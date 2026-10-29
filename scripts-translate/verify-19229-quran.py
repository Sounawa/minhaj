# -*- coding: utf-8 -*-
"""verify-19229-quran.py — sondes coraniques pour 19229 (les jours importants de l'année arabe).
Fente formelle unique : l'āya du nombre des mois (9:36) — slot vide après « كما قال الله تعالى: ».
Écho identifié : « منها أربعة حرام » (les mois sacrés — la division de la Loi).
"""
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
                        print(f'   {s}:{i+1} :: {p[1][:130]}')
    if n == 0:
        print('   ✗ AUCUNE position')
    elif n > maxn:
        print(f'   ... {n} positions')

# === Fente formelle — le nombre des mois (le contexte : « عدد الشهور اثنا عشر كما قال الله تعالى ») ===
# Calibration du cache (cf. R354) : عدة avec ta marbuta ; كتب sans alif (dagger U+0670 strippé) ; ٱ → ا
contient(['ان', 'عدة', 'الشهور', 'عند', 'الله', 'اثنا', 'عشر', 'شهرا'], 'F1. 9:36a inna ʿiddaš-šuhūri ʿinda llāhi ṯna ʿašara šahran (nombre des mois)')

# === Écho — les quatre mois sacrés (la division selon la Loi) ===
contient(['منها', 'اربعة', 'حرم'], 'F2. 9:36b minhā arbaʿatun ḥurum (écho mois sacrés — hamza normalisée)')

# === Écho — le jour où Il créa les cieux et la terre (la continuation de la même āya) ===
contient(['يوم', 'خلق', 'السموت', 'والارض', 'منها'], 'F3. 9:36c yawma ḫalaqa s-samāwāti wa-l-arḍa minhā (continuité de lāya)')

# === Impression brute de 9:36 pour calibration du rasm ʿUṯmānī ===
print('\n## 9:36 rasm brut (cache)')
print(data['9']['ar'][35][1] if len(data['9']['ar']) > 35 else 'ABSENT')
print('\n## 9:37 rasm brut (l-année kabisa / an-nasīʾ, pour mémoire)')
print(data['9']['ar'][36][1] if len(data['9']['ar']) > 36 else 'ABSENT')
