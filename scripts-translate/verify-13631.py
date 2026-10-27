#!/usr/bin/env python3
# verify-13631.py — vérification systématique des versets au quran-cache
# Leçon 13631 « Sourate An-Nahl, versets 98 103 » (tafsir-tanawi-1, lessons[23])
# Bloc principal : Naḥl 98-103 — + Aʿrāf 201, Māʾida 7, Ḥiǧr 42, Naḥl 68 (الاستثمار)
# + Qaṣaṣ 6 ET 7 (span « القصص:6 » douteux — le وحَيْنَا est en 7 ?) — Maryam 10 ET 11 (span « مريم:10 » douteux — le فأوحى est en 11 ?)
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
show(16, 98, 103, 'an-Nahl (bloc principal 98-103)')

# Versets cités du commentaire
show(7, 201, 201, 'al-Araf 201 (span subsistant)')
show(5, 7, 7, 'al-Ma-ida 7 (span subsistant)')
show(15, 42, 42, 'al-Hiǧr 42 (span subsistant)')

# الاستثمار — les trois sens du waḥy
show(16, 68, 68, 'an-Nahl 68 (span subsistant — النحل)')
show(28, 6, 7, 'al-Qasas 6 ET 7 (span « القصص:6 » douteux — auḥayna en 7 ?)')
show(19, 10, 11, 'Maryam 10 ET 11 (span « مريم:10 » douteux — fa-awḥa en 11 ?)')

print('--- OK verify-13631 ---')
