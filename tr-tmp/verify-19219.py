#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bare2 du tour R356 — vérifications internes du doc 19219 (ḥurūf al-ǧummal).

1. Partition des quatre rangées sur les 28 lettres (10+8+9+1).
2. Les 16 exemples du document recalculés avec les valeurs de sa Table 1.
3. Les cinq substitutions de l'énoncé appliquées à la Table 1 → Table 2 attendue.
4. Le sund (سند) = 354 — résolution de la tension documentée en R354.
5. Inventaire des valeurs certifiées par le document lui-même (fente du tableau maître).
"""
import unicodedata

# --- Valeurs de la TABLE 1 du livre (rangement que le livre attribue aux Maghrébins) ---
V = {'ا':1,'ب':2,'ج':3,'د':4,'ه':5,'و':6,'ز':7,'ح':8,'ط':9,'ي':10,
     'ك':20,'ل':30,'م':40,'ن':50,'ص':60,'ع':70,'ف':80,'ض':90,
     'ق':100,'ر':200,'س':300,'ت':400,'ث':500,'خ':600,'ذ':700,'ظ':800,'غ':900,'ش':1000}

RANKS = {
 'unites':   list('ابجدهوزحطي'),          # 10 lettres, 1..10
 'dizaines': list('كلمنصعفض'),            # 8 lettres, 20..90
 'centaines':list('قرستثخذظغ'),           # 9 lettres, 100..900
 'alouf':    list('ش'),                   # 1 lettre, 1000
}

print('=== 1. Partition des quatre rangées ===')
tot = 0
for name, lets in RANKS.items():
    print(f'  {name:10s} : {len(lets)} lettres')
    tot += len(lets)
print(f'  TOTAL = {tot} (attendu 28)', 'OK' if tot == 28 else 'ÉCHEC')
# cohérence valeurs: unités 1..10 en ordre, dizaines 20..90 en ordre, centaines 100..900 en ordre
ok_ordre = ([V[c] for c in RANKS['unites']] == list(range(1,11))
             and [V[c] for c in RANKS['dizaines']] == list(range(20,91,10))
             and [V[c] for c in RANKS['centaines']] == list(range(100,901,100))
             and V['ش'] == 1000)
print('  ordres internes des rangées:', 'OK' if ok_ordre else 'ÉCHEC')

print('=== 2. Les 16 exemples du document (groupe : suite : valeur annoncée) ===')
EX = [
 ('a','يب',12),('a','كد',24),('a','كح',28),('a','له',35),
 ('b','قد',104),('b','خط',609),('b','غط',909),('b','سد',304),
 ('c','قل',130),('c','رم',240),('c','خف',680),('c','سك',320),
 ('d','سهص',365),('d','خلط',639),('d','قيد',114),('d','سمح',348),
]
fails = 0
certified = {}
for g, w, expect in EX:
    s = sum(V[c] for c in w)
    decomp = '+'.join(f'{c}={V[c]}' for c in w)
    st = 'OK' if s == expect else 'ÉCHEC'
    if s != expect: fails += 1
    for c in w: certified[c] = V[c]
    print(f'  [{g}] {w} : {decomp} = {s} (annoncé {expect}) {st}')
print(f'  → {16-fails}/16 exemples vérifiés', 'OK' if fails == 0 else 'ÉCHEC')

print('=== 3. Les cinq substitutions de l\'énoncé ===')
# énoncé : ص→س, ض→ص, س→ش, غ→ض, ش→غ (le reste inchangé)
SUB5 = {'ص':'س','ض':'ص','س':'ش','غ':'ض','ش':'غ'}
T1 = ['أبجد','هوز','حطي','كلمن','صعفض','قرست','ثخذ','ظغش']
T2_ATTENDUE = ['أبجد','هوز','حطي','كلمن','سعفص','قرشت','ثخذ','ضظغ']
T2_calc5 = [''.join(SUB5.get(c, c) for c in w) for w in T1]
for w1, wc, wa in zip(T1, T2_calc5, T2_ATTENDUE):
    print(f'  {w1} → {wc} (table imprimée {wa})', 'OK' if wc == wa else 'FRICTION')
print('  → FRICTION DOCUMENTÉE : l\'énoncé nomme CINQ substitutions,')
print('     elles reproduisent سعفص قرشت ثخذ mais donnent ظضغ pour le dernier mot ;')
print('     la table imprimée porte ضظغ — la sixième rotation (ظ→ض, avec غ→ظ) est celle')
print('     que la phrase tait. La table fait foi ; friction portée sans reconstruction.')
# la rotation classique complète à SIX lettres (par valeurs : صضسظغش → سصشضظغ)
SUB6 = {'ص':'س','ض':'ص','س':'ش','ظ':'ض','غ':'ظ','ش':'غ'}
T2_calc6 = [''.join(SUB6.get(c, c) for c in w) for w in T1]
ok6 = T2_calc6 == T2_ATTENDUE
for w1, wc in zip(T1, T2_calc6):
    print(f'  rotation six lettres : {w1} → {wc}')
print('  les SIX rotations reproduisent la Table 2:', 'OK' if ok6 else 'ÉCHEC')

print('=== 4. Le sund résolu (tension R354) ===')
snd = sum(V[c] for c in 'سند')
print(f'  سند : س=300 (certifié 4× : سد 304, سك 320, سهص 365, سمح 348) + ن=50 (rangée كلمن) + د=4 (كد 24)')
print(f'  سند = {snd} (l\'année arabe impose 354)', 'OK — TENSION R354 RÉSOLUE' if snd == 354 else 'ÉCHEC')

print('=== 5. Valeurs certifiées par le document lui-même ===')
# certifiées par exemples + ش par la règle des alūf (« صورة الألف (ش) »)
cert = dict(certified); cert['ش'] = 1000
manquantes = sorted(set(V) - set(cert))
print(f'  certifiées par les 16 exemples : {len(certified)} lettres')
print(f'  + ش=1000 par la règle des alūf → {len(cert)} / 28 certifiées par le document')
print(f'  restées au tableau perdu (fente) : {" ".join(manquantes)} → valeurs {sorted(V[c] for c in manquantes)}')
print(f'  (les 11 restantes sont couvertes par la structure des rangées, pas par un exemple chiffré)')
print('=== FIN BARE2 ===')
