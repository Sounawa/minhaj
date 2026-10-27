#!/usr/bin/env python3
# verify-13590.py — vérification systématique des versets au quran-cache
# Naḥl 86-89 (bloc principal + tous les emplacements vides du commentaire)
# + versets cités : Aḥqāf 4-5, Maryam 82-83, Maryam 37, Sajda 12, Ṭāhā 108,
#   Yūnus 18, Anʿām 26 ET 27 (span douteux), Nisāʾ 41, Aʿrāf 5 ET 6 (span douteux),
#   Ḥijr 92-93, Ḥashr 7, Naḥl 44
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

# Bloc principal — les quatre āyāt
show(16, 86, 89, 'an-Nahl (bloc principal 86-89)')

# Versets cités du commentaire
show(46, 4, 5, 'al-Ahqaf 4-5')
show(19, 82, 83, 'Maryam 82-83')
show(19, 37, 37, 'Maryam 37')
show(32, 12, 12, 'as-Sajda 12')
show(20, 108, 108, 'Ta-Ha 108')
show(10, 18, 18, 'Yunus 18')
show(6, 26, 27, 'al-Anam 26 ET 27 (span douteux 27 -> 26 ?)')
show(4, 41, 41, 'an-Nisa 41')
show(7, 5, 6, 'al-Araf 5 ET 6 (span douteux 5 -> 6 ?)')
show(15, 92, 93, 'al-Hijr 92-93')
show(59, 7, 7, 'al-Hashr 7')
show(16, 44, 44, 'an-Nahl 44')

# Tronc de la clôture de 86 (fin de sourate : vérifier que 86 finit bien par لكاذبون)
print('### fin an-Nahl 86 (tronc attendu : فألقوا إليهم القول أنكم لكاذبون)')
s = c['16']
for k in s.keys():
    if k in ('number', 'englishName', 'nAyahs'):
        continue
    for n, txt in s[k]:
        if n == 86:
            tail = txt[-120:] if len(txt) > 120 else txt
            print(f'[16:{k}:86:TAIL] …{tail}')
print('--- OK verify-13590 ---')
