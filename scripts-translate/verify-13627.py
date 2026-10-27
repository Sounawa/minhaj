#!/usr/bin/env python3
# verify-13627.py — vérification systématique des versets au quran-cache
# Leçon 13627 « Sourate An-Nahl, versets 94-97 » (tafsir-tanawi-1, lessons[22])
# Bloc principal : Naḥl 94-97 — + Naḥl 92 (contexte du دَخَل, cité dans la discussion)
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

# Bloc principal — les quatre āyāt
show(16, 94, 97, 'an-Nahl (bloc principal 94-97)')

# Contexte du دَخَل (Naḥl 92 — تَتَّخِذُونَ أَيْمَانَكُمْ دَخَلًا)
show(16, 92, 92, 'an-Nahl 92 (contexte دخل)')

# Troncs attendus pour les emplacements tronqués du commentaire
print('### Troncs de fin de 94 et 95 et 96')
s = c['16']
for k in s.keys():
    if k in ('number', 'englishName', 'nAyahs'):
        continue
    for n, txt in s[k]:
        if n in (94, 95, 96):
            tail = txt[-160:] if len(txt) > 160 else txt
            print(f'[16:{k}:{n}:TAIL] …{tail}')
print('--- OK verify-13627 ---')
