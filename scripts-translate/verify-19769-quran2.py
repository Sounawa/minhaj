#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérification coranique 2 — doc 19769 (chapitre du ḫāʾ).
Sondes tolérantes à la position de l'alif : suscrite ٰ / pleine ا / élidée (absente).
Affiche le mot RAW (diacritiques conservés) pour classer suscrite/pleine/élidée."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE, encoding="utf-8"))

HARAKAT = re.compile(r"[\u064B-\u0655\u0640]")
DAGGER = "\u0670"

def strip_h(s):
    return HARAKAT.sub("", s)

def raw_words(s):
    return [w for w in s.split() if w]

def scan(label, pattern, sura_filter=None):
    print(f"\n=== {label} ===")
    rx = re.compile(pattern)
    hits = []
    for snum, sdata in sorted(data.items(), key=lambda kv: int(kv[0])):
        if sura_filter and int(snum) not in sura_filter:
            continue
        for aynum, aytext in sdata["ar"]:
            for w in raw_words(aytext):
                sw = strip_h(w)
                if rx.search(sw):
                    hits.append((snum, aynum, w))
    for snum, aynum, w in hits:
        form = "SUSCRITE(ٰ)" if DAGGER in w else ("PLEINE(ا)" if "ا" in w and strip_h(w) != w.replace("ا", "") else "absente/à voir")
        print(f"  {snum}:{aynum} — {w}   [{form}]")
    print(f"  → {len(hits)} mot(s)")
    return hits

# 1. خالد : participle خَٰلِد (dagger ou pleine) + façons dérivées
scan("خ-ل-د (toutes formes)", r"خ.{0,2}لد")
# 2. تخافت / يتخافتون (formes VI)
scan("ت-خ-ف-ت (form VI)", r"تخ.{0,2}فت")
# 3. Sourate 12 : tous mots contenant خ (trouver « le premier lieu de Yūsuf »)
scan("Sourate 12 : mots en خ", r"خ", sura_filter={12})
# 4. Sourate 11 : tous mots contenant خ (Hūd 37 et voisinage)
scan("Sourate 11 : mots en خ", r"خ", sura_filter={11})
# 5. Sourate 23 : tous mots contenant خ (al-Muʾminūn 27)
scan("Sourate 23 : mots en خ", r"خ", sura_filter={23})
# 6. خاسر / خسئ
scan("خ-س-ر (خاسر)", r"خ.{0,2}س[ر]")
scan("خ-س-ئ (خسئ)", r"خ.{0,2}سئ")
# 7. خَامِسَة (an-Nūr 7, 9) — formes خامس/خمس
scan("خ-م-س (خمس/خامس)", r"خ.{0,2}م[س]", sura_filter={24})
# 8. خَارِجَ (خرج)
scan("خ-ر-ج (خارج/خرج)", r"خ.{0,2}ر[ج]")
# 9. خَلَتْ / خلت (خَلَا «cesser de/imaginer»)
scan("خ-ل-ت (خلت)", r"خ.{0,2}ل[ت]")
# 10. شامخ
scan("ش-م-خ (شامخ/شمخ)", r"ش.{0,2}مخ")
# 11. خشع / خضع / خاشع
scan("خ-ش-ع (خشع/خاشع)", r"خ.{0,2}شع")
scan("خ-ض-ع (خضع/خاضع)", r"خ.{0,2}ضع")
# 12. خشى/خاف ذاكرة : 11:70 (قَالُوا لَا تَخَفْ)
for ref in [(11, 37), (11, 70), (23, 27), (24, 7), (24, 9), (20, 103), (68, 23), (12, 85), (12, 95), (11, 108)]:
    s, a = ref
    for aynum, aytext in data[str(s)]["ar"]:
        if aynum == a:
            print(f"\n=== TEXTE BRUT {s}:{a} ===\n  {aytext}")
