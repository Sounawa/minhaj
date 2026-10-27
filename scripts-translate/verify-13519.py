#!/usr/bin/env python3
# Vérification quran-cache — leçon 13519 (an-Naḥl 57-59 + parallèles)
import json

cache = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))

def get(s, a):
    su = cache[str(s)]
    for row in su['ar']:
        if row[0] == a:
            for rf in su['fr']:
                if rf[0] == a:
                    return row[1], rf[1]
    return None, None

targets = [
    ('an-Naḥl 57', 16, 57), ('an-Naḥl 58', 16, 58), ('an-Naḥl 59', 16, 59),
    ('an-Najm 21', 53, 21), ('an-Najm 22', 53, 22),
    ('aṣ-Ṣāffāt 151', 37, 151), ('aṣ-Ṣāffāt 152', 37, 152),
    ('Maryam 89', 19, 89), ('Maryam 90', 19, 90), ('Maryam 91', 19, 91),
    ('Maryam 92', 19, 92), ('Maryam 93', 19, 93), ('Maryam 94', 19, 94),
    ('at-Takwīr 8', 81, 8), ('at-Takwīr 9', 81, 9),
]
out = {}
for label, s, a in targets:
    ar, fr = get(s, a)
    ok = 'OK' if ar and fr else 'MANQUANT'
    print(f'--- {label} [{ok}]')
    print('AR:', ar)
    print('FR:', fr)
    out[label] = {'ar': ar, 'fr': fr}

json.dump(out, open('/home/z/my-project/tr-tmp/13519-verses.json', 'w'), ensure_ascii=False, indent=1)
print('\nSauvé: tr-tmp/13519-verses.json')
