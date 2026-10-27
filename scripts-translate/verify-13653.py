#!/usr/bin/env python3
# verify-13653.py — vérification systématique des versets au quran-cache
# Leçon 13653 « Sourate An-Nahl, versets 120-124 » (tafsir-tanawi-1, lessons[27])
# Bloc principal : Naḥl 120-124 — spans subsistants à vérifier :
#   al-Baqara 123 ; an-Naǧm 36 (SUSPECT — « وَفَّى » = 37 ?) ; aš-Šuʿarāʾ 83 ;
#   Āl ʿImrān 19 ; Āl ʿImrān 66 (SUSPECT — fit?) ; al-Ḥaǧǧ 76 (SUSPECT — milla Ibrāhīm = 78 ?)
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
show(16, 120, 124, 'an-Nahl (bloc principal 120-124)')

# Spans subsistants du commentaire
show(2, 123, 123, 'al-Baqara 123 (span subsistant البقرة:123)')
show(53, 36, 37, 'an-Naǧm 36-37 (span subsistant النجم:36 — SUSPECT, وفّى = 37?)')
show(26, 83, 83, 'aš-Šuʿarāʾ 83 (span subsistant الشعراء:83 — invocation dʾIbrāhīm)')
show(3, 19, 19, 'Āl ʿImrān 19 (span subsistant آل عمران:19)')
show(3, 65, 66, 'Āl ʿImrān 65-66 (span subsistant آل عمران:66 — SUSPECT fit?)')
show(22, 76, 78, 'al-Ḥaǧǧ 76-78 (span subsistant الحج:76 — SUSPECT, milla Ibrāhīm = 78?)')

print('--- OK verify-13653 ---')
