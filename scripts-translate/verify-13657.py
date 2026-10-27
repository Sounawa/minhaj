#!/usr/bin/env python3
# verify-13657.py — vérification systématique des versets au quran-cache
# Leçon 13657 « Sourate An-Nahl, versets 125-128 » (tafsir-tanawi-1, lessons[28])
# Bloc principal : Naḥl 125-128 — spans subsistants à vérifier :
#   al-ʿAnkabūt 46 ; Ṭāhā 43 (cité en texte) ; al-Qaṣaṣ 56 ; an-Naḥl 37 ;
#   al-Baqara 271 (SUSPECT — « ليس عليك هداهم » = 272 ?) ;
#   az-Zumar 11 (SUSPECT — « أجر الصابرين بغير حساب » = 10 ?) ;
#   al-Aʿrāf 1 (SUSPECT — « لا يكن في صدرك حرج » = 2 ?) ; Hūd 12.
# Candidats de restitution : aš-Šūrā 40 ; al-Ḥiǧr 97 ; al-Aʿrāf 199 ; al-Ghāšiya 21-22 ; Yūnus 100.
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

# Bloc principal — les quatre āyāt
show(16, 125, 128, 'an-Nahl (bloc principal 125-128)')

# Spans subsistants du commentaire
show(29, 46, 46, 'al-Ankabut 46 (span subsistant العنكبوت:46)')
show(20, 43, 44, 'Taha 43-44 (cité en texte ﴿فقولا له قولا لينا﴾ [طه:43])')
show(28, 56, 56, 'al-Qasas 56 (span subsistant القصص:56)')
show(16, 37, 37, 'an-Nahl 37 (span subsistant النحل:37)')
show(2, 271, 272, 'al-Baqara 271-272 (span subsistant البقرة:271 — SUSPECT, ليس عليك هداهم = 272?)')
show(39, 10, 11, 'az-Zumar 10-11 (span الزمر:11 SUSPECT ×2 — أجر الصابرين بغير حساب = 10?)')
show(7, 1, 2, 'al-Araf 1-2 (span الأعراف:1 SUSPECT — لا يكن في صدرك حرج = 2?)')
show(11, 12, 12, 'Hud 12 (span subsistant هود:12)')

# Candidats de restitution (emplacements sans span / citation perdue)
show(42, 39, 40, 'aš-Šūrā 39-40 (candidat عفو منزلة عظيمة — فمن عفا وأصلح)')
show(15, 97, 97, 'al-Ḥiǧr 97 (candidat يضيق صدره بما يقولون)')
show(7, 199, 199, 'al-Aʿrāf 199 (candidat خذ العفو وأعرض عن الجاهلين)')
show(88, 21, 22, 'al-Ghāšiya 21-22 (candidat فذكر إنما أنت مذكر)')
show(10, 100, 100, 'Yūnus 100 (candidat ما كان لنفس أن تؤمن إلا بإذن الله)')
show(16, 93, 93, 'an-Naḥl 93 (candidat يضل من يشاء ويهدي من يشاء)')

print('--- OK verify-13657 ---')
