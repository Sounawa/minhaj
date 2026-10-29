# -*- coding: utf-8 -*-
"""verify-19263-quran.py — vérification de l'écho coranique final du document 19263.

La clôture du šarḫ pose la fāʾida de l'étude des jours importants :
« والاعتبار بآيات الله في الكون لمن أراد أن يذكر أو أراد شكورا »
— le document ne cite AUCUNE āya (0 ﴿﴾, 0 « قال الله ») : l'écho est
allusif. Le garde vérifie au quran-cache les candidats structurants :
  A. Q 50:37 — « لِمَن كَانَ ذَا قَلْبٍ أَوْ أَلْقَى السَّمْعَ وَهُوَ شَهِيدٌ » (l'auditoire du dhikr)
  B. Q 2:152 — « فَاذْكُرُونِي أَذْكُرْكُمْ وَاشْكُرُوا لِي » (le couple ḏikr/šukr)
  C. Q 3:191 — « يَتَفَكَّرُونَ فِي خَلْقِ السَّمَاوَاتِ وَالْأَرْضِ » (l'ibtilāʾ dans le cosmos)
  D. Q 14:7 — « لَئِن شَكَرْتُمْ لَأَزِيدَنَّكُمْ » (la promesse du šukr)
Recherche aussi par radical : شكور / ذكر en co-occurrence courte.
"""
import json, re

HOME = '/home/z/my-project'
quran = json.load(open(f'{HOME}/scripts-translate/quran-cache.json'))

def norm(t):
    if not isinstance(t, str):
        return ''
    t = t.replace('﴿', '').replace('﴾', '')
    t = t.replace('\u0671', '\u0627')          # alif wasla (rasm uthmanï) -> alif
    t = t.replace('\u0670', '')                 # alif superscript
    t = t.replace('\u06cc', '\u064a')           # farsi yeh
    t = re.sub(r'[\u064B-\u0652\u06D6-\u06ED\u08F0-\u08FF]', '', t)  # harakāt etc.
    return re.sub(r'\s+', ' ', t).strip()

# index des versets normalisés
ALL = {}
for s, rec in quran.items():
    for n, raw in rec.get('ar', []):
        ALL[(int(s), int(n))] = norm(raw)

def show(label, s, v, need, *any_of):
    t = ALL.get((s, v), '')
    flat = []
    for x in any_of:
        flat.extend(x) if isinstance(x, list) else flat.append(x)
    ok = need in t and any(x in t for x in flat)
    print(f'{label} Q {s}:{v} {"OK " if ok else "ABSENT"} — {t[:160]}')
    return ok

print('=== Candidats structurants ===')
show('A', 50, 37, 'لمن', ['قلب', 'سمع'])
show('B', 2, 152, 'اشكروا', ['اذكروني', 'اذكر'])
show('C', 3, 191, 'يتفكرون', ['خلق', 'سموات'])
show('D', 14, 7, 'لئن شكرتم', ['لأزيدنكم'])

print('\n=== Co-occurrence ذكر/شكور (radical) ===')
hits = []
for (s, n), t in ALL.items():
    if 'شكور' in t and 'ذكر' in t:
        hits.append((s, n, t))
print(f'{len(hits)} verset(s) avec شكور+ذكر :')
for s, i, t in hits[:8]:
    print(f'  Q {s}:{i} — {t[:140]}')
