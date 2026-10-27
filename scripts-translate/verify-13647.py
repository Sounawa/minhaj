#!/usr/bin/env python3
# verify-13647.py — vérification systématique des versets au quran-cache
# Leçon 13647 « Sourate An-Nahl, versets 115-119 » (tafsir-tanawi-1, lessons[26])
# Bloc principal : Naḥl 115-119 — spans subsistants : al-Anʿām 146, 140, 147 ; al-Māʾida 4
# + Naḥl 120 (citation ḥanīfiyya perdue de l'iʿdād — restauration d'après la logique)
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
                print(f'[{sura}:{k}:{n}] {txt[:1100]}')
    print()

# Bloc principal — les cinq āyāt
show(16, 115, 119, 'an-Nahl (bloc principal 115-119)')

# Spans subsistants du commentaire
show(6, 146, 146, 'al-Anam 146 (span subsistant الأنعام:146)')
show(6, 140, 140, 'al-Anam 140 (span subsistant الأنعام:140)')
show(6, 147, 147, 'al-Anam 147 (span subsistant الأنعام: 147)')
show(5, 4, 4, 'al-Maida 4 (span subsistant المائدة:4)')

# Référence croisée — la citation ḥanīfiyya perdue de l'iʿdād
show(16, 120, 120, 'an-Nahl 120 (iʿdād — الحنيفية, citation perdue)')

print('--- OK verify-13647 ---')
