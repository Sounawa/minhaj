#!/usr/bin/env python3
# verify-13639.py — vérification systématique des versets au quran-cache
# Leçon 13639 « Sourate An-Nahl, versets 110-114 » (tafsir-tanawi-1, lessons[25])
# Bloc principal : Naḥl 110-114 — + ʿAbas 37 (span subsistant عبس: 37)
# + al-Isrāʾ 15 (span subsistant الإسراء: 15)
import json

c = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))

def show(sura, aya1, aya2=None, label=''):
    s = c[str(sura)]
    keys = [k for k in s.keys() if k not in ('number', 'englishName', 'nAyahs')]
    rng = range(aya1, (aya2 or aya1) + 1)
    print(f'### {label or sura} {aya1}' + (f'-{aya2}' if aya2 else ''))
    for k in keys:
        arr = s[k]
        for n, txt in arr:
            if n in rng:
                print(f'[{sura}:{k}:{n}] {txt[:900]}')
    print()

# Bloc principal — les cinq āyāt
show(16, 110, 114, 'an-Nahl (bloc principal 110-114)')

# Spans subsistants du commentaire
show(80, 37, 37, 'Abas 37 (span subsistant عبس: 37)')
show(17, 15, 15, 'al-Isra 15 (span subsistant الإسراء: 15)')

print('--- OK verify-13639 ---')
