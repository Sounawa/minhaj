#!/usr/bin/env python3
# verify-13547.py — vérification systématique au quran-cache
# Naḥl 75-77 (ar + fr) + Baqara 3 & 254 (spans erronés 2/252) + Qamar 50 + Luqman 27 + Isra 70
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
                print(f'[{sura}:{k}:{n}] {txt[:420]}')
    print('-' * 50)

show(16, 75, 77, 'AN-NAHL')
show(2, 3, None, 'AL-BAQARA (span erroné "2" -> 3)')
show(2, 254, None, 'AL-BAQARA (span erroné "252" -> 254)')
show(2, 2, None, 'AL-BAQARA 2 (contenu réel du span "2")')
show(2, 252, None, 'AL-BAQARA 252 (contenu réel du span "252")')
show(54, 50, None, 'AL-QAMAR')
show(31, 27, None, 'LUQMAN')
show(17, 70, None, 'AL-ISRA')
show(16, 40, None, 'AN-NAHL 40 (كن فيكون — même sourate)')
