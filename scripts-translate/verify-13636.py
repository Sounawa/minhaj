#!/usr/bin/env python3
# verify-13636.py — vérification systématique des versets au quran-cache
# Leçon 13636 « Sourate An-Nahl, versets 104 à 109 » (tafsir-tanawi-1, lessons[24])
# Bloc principal : Naḥl 104-109 — + Aṣ-Ṣaff 5 (span subsistant) + an-Nisāʾ 170 (span subsistant)
# + Naḥl 103 (accusation « إنما يعلمه بشر » possible pour « رد لقولهم في النبي »)
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

# Bloc principal — les six āyāt
show(16, 104, 109, 'an-Nahl (bloc principal 104-109)')

# Spans subsistants du commentaire
show(61, 5, 5, 'as-Saff 5 (span subsistant الصف: 5)')
show(4, 170, 170, 'an-Nisa 170 (span subsistant النساء: 170)')

# Référence croisée possible — la fausse accusation du Prophète
show(16, 103, 103, 'an-Nahl 103 (accusation « يعلمه بشر » — référence croisée)')

print('--- OK verify-13636 ---')
