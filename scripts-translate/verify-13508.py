# -*- coding: utf-8 -*-
"""Vérification quran-cache pour 13508 (tafsir-tanawi-1, an-Naḥl 36-40)."""
import json

Q = json.load(open('scripts-translate/quran-cache.json'))

def ar(s, n):
    for e in Q[str(s)]['ar']:
        if e[0] == n: return e[1]

def fr(s, n):
    for e in Q[str(s)]['fr']:
        if e[0] == n: return e[1]

print('=== AN-NAHL 36-40 (AR) ===')
for n in range(36, 41):
    print(f'[AR Naḥl {n}]', ar(16, n))
print()
print('=== AN-NAHL 36-40 (FR) ===')
for n in range(36, 41):
    print(f'[FR Naḥl {n}]', fr(16, n))
print()
print('=== SUPPORTS ===')
print('[AR Tawba 106]', ar(9, 106))
print('[FR Tawba 106]', fr(9, 106))
print()
print('[AR Āl ʿImrān 164]', ar(3, 164))
print('[FR Āl ʿImrān 164]', fr(3, 164))
print()
print('[AR Naḥl 64]', ar(16, 64))
print('[FR Naḥl 64]', fr(16, 64))
