#!/usr/bin/env python3
# verify-19354.py — vérification des emplacements coraniques au quran-cache
# Leçon 19354 « Jurisprudence : ce qu'il est interdit au failli… »
# (fiqh-tanawi-3, lessons[4]) — JUMELLE de 15355 (livrée R294).
#
# Particularité de la jumelle : les QUATRE emplacements coraniques sont VIDES
# (galle d'impression) — la source imprime les marqueurs de citation
# « فقال سبحانه: », « لقوله تعالى: », « قال تعالى: », « وقال تعالى: »
# immédiatement suivis de paragraphes vides, SANS texte de verset
# ET SANS référence entre crochets (la jumelle 15355 imprimait, elle,
# [البقرة: 279] / [النساء: 11]×2 / [البقرة: 281]).
#
# Résolution attendue (conforme au tranchage documenté de la jumelle) :
#   slot 1 — إنظار المعسر  → (2:280)  فنظرة إلى ميسرة   (13e cas du fil)
#   slot 2 — لقوله تعالى (succession/dette) → (4:11)  من بعد وصية أو دين (confirmée)
#   slot 3 — قال تعالى (Ibn Rushd, جواز التداين) → (2:282) إذا تداينتم (14e cas)
#   slot 4 — وقال تعالى (Ibn Rushd, suite) → (4:11)    (confirmée)
import json

c = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))

def show(sura, aya, label):
    s = c[str(sura)]
    for k, arr in s.items():
        if isinstance(arr, list):
            for n, txt in arr:
                if n == aya:
                    print(f'### {label} [{sura}:{k}]')
                    print(txt[:700])
                    print()

# --- slot 1 : إنظار المعسر (jumelle : [البقرة: 279] tranchée à 280) ---
show(2, 279, 'Baqara 279 (réf. imprimée de la JUMELLE, avertissement)')
show(2, 280, 'Baqara 280 (candidat إنظار المعسر — 19354 slot VIDÉ)')
# --- slot 2 : لقوله تعالى — succession/dette ---
show(4, 11, 'Nisaa 11 (candidat — succession subordonnée au testament et à la dette)')
# --- slot 3 : قال تعالى — التداين (jumelle : [البقرة: 281] tranchée à 282) ---
show(2, 281, 'Baqara 281 (réf. imprimée de la JUMELLE, jour du retour)')
show(2, 282, 'Baqara 282 (candidat التداين — 19354 slot VIDÉ)')
