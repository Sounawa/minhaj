#!/usr/bin/env python3
# verify-13585.py — vérification systématique des versets au quran-cache
# Naḥl 60-62 (bloc principal) + Anfāl 25, Ṣād 32, Anʿām 137, Fāṭir 45, Kahf 57, Ibrāhīm 44, ʿAnkabūt 53 (citations perdues)
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
                print(f'[{sura}:{k}:{n}] {txt[:600]}')
    print()

# Bloc principal
show(16, 60, 62, 'an-Nahl (bloc principal)')
# Citations perdues du commentaire
show(8, 25, None, 'al-Anfal')
show(38, 32, None, 'Sad')
show(6, 137, None, 'al-Anam')
# Citations perdues de l exploitation (as-Sanqiti)
show(35, 45, None, 'al-Fatir')
show(18, 57, None, 'al-Kahf')
show(14, 44, None, 'Ibrahim')
show(29, 53, None, 'al-Ankabut')
