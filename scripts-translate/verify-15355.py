#!/usr/bin/env python3
# verify-15355.py — vérification des références coraniques au quran-cache
# Leçon 15355 « Ce qui est interdit au failli et ce qui lui demeure permis » (fiqh-tanawi-3, lessons[1])
# Références imprimées SANS texte de verset (crochets) :
#   [البقرة: 279] — contexte « أمر الله بإنظار المعسر فقال سبحانه » → SOUPÇON 280 (فنظرة إلى ميسرة)
#   [النساء: 11] ×2 — contexte succession/penas de la dette → à confirmer (من بعد وصية أو دين)
#   [البقرة: 281] — contexte « دل على جواز التداين » (Ibn Rushd) → SOUPÇON 282 (إذا تداينتم)
import json

c = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))

def show(sura, aya, label):
    s = c[str(sura)]
    for k, arr in s.items():
        if isinstance(arr, list):
            for n, txt in arr:
                if n == aya:
                    print(f'### {label} [{sura}:{k}]')
                    print(txt[:900])
                    print()

# --- Soupçon 1 : إنظار المعسر ---
show(2, 279, 'Baqara 279 (référence imprimée)')
show(2, 280, 'Baqara 280 (candidat إنظار المعسر)')
# --- Référence succession/dette ---
show(4, 11, 'Nisaa 11 (référence imprimée x2)')
# --- Soupçon 2 : التداين ---
show(2, 281, 'Baqara 281 (référence imprimée Ibn Rushd)')
show(2, 282, 'Baqara 282 (candidat التداين)')
