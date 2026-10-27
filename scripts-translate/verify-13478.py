# -*- coding: utf-8 -*-
"""Vérification quran-cache pour 13478 (tafsir-tanawi-1, an-Naḥl 24-29)."""
import json

Q = json.load(open('scripts-translate/quran-cache.json'))

def verse(s, n):
    sura = Q[str(s)]
    for e in sura['ar']:
        if e[0] == n:
            return e[1]
    return None

print('=== AN-NAHL 24-29 (bloc principal + sous-quotes) ===')
for n in range(24, 30):
    print(f'[Naḥl {n}]', verse(16, n))

print()
print('=== SUPPORTS ===')
print('[Āl ʿImrān 192]', verse(3, 192))
print('[ad-Dukhān 46]', verse(44, 46))
print('[az-Zukhruf 48]', verse(43, 48))

print()
print('=== CONTEXTE Dukhān 41-50 ===')
for n in range(41, 51):
    print(f'[Dukhān {n}]', verse(44, n))

print()
print('=== CONTEXTE Zukhruf 45-49 ===')
for n in range(45, 50):
    print(f'[Zukhruf {n}]', verse(43, n))

print()
print('=== RECHERCHE شُرَكَائِي / شركاء dans tout le cache ===')
import re
for s in Q:
    sura = Q[s]
    for e in sura['ar']:
        if 'شُرَكَائِي' in e[1] or 'شُرَكَاء' in e[1] or 'شُرَكَائ' in e[1]:
            print(f'[{sura["englishName"]} {e[0]}]', e[1][:120])

print()
print('=== RECHERCHE تُشَاقُّونَ ===')
for s in Q:
    sura = Q[s]
    for e in sura['ar']:
        if 'شَاقُّونَ' in e[1] or 'شاقوا' in e[1] or 'شَاقُّوا' in e[1]:
            print(f'[{sura["englishName"]} {e[0]}]', e[1][:120])
