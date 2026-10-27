#!/usr/bin/env python3
# verify-13587.py — vérification systématique des versets au quran-cache
# Naḥl 68-70 (bloc principal + tous les emplacements vides du commentaire)
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
                print(f'[{sura}:{k}:{n}] {txt[:700]}')
    print()

# Bloc principal — les trois āyāt
show(16, 68, 70, 'an-Nahl (bloc principal 68-70)')
