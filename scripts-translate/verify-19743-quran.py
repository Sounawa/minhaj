#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérifications coraniques du doc 19743 (rasm-wa-dabt-4ep, chapitre du bāʾ, suite).

Le doc cite (dans le corps, en renvois d'appareil — pas de chips) :
  - لفظ « عِبَادَ » élidé : Maryam 65 / Ṣād (44?) / al-Fajr (32?) — le reste au thubūt
  - alif du duel fixe à l'extrémité + exception تُكَذِّبَانِ (al-Raḥmān)
  - أَبَا (al-Aḥzāb, qayd « aḥadin min ») vs أَبَى (maqṣūra)
  - maqṣūrāt élidées SANS yāʾ : mot en Ṭāhā 119 + Nūn (al-Qalam 50) / mot en al-Shams / أَدْبَرِ (mumāla)
  - ar-ribā : wāw à l'état défini (+ ilḥāq), alif à l'état indéfini (Rūm 39 رِبًا)
  - mots-rasm du Dānī : امرأتن / رجلتن / سحرتن (et أُدْخُلَا, وَقَالَا الْحَمْدُ لِلَّهِ illustratifs)
  - iʿdād (leçon suivante) : كِتَـبٍ, جَنَّتَـنِ, مَبْسُوطَتَنِ, التَّلِيَـتِ, التَّئِبُونَ
"""
import json
import re

C = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json"))
HARAKAT = re.compile(r"[\u064B-\u0652\u0653-\u0655\u0670\u06D6-\u06ED\u08F0-\u08F3]")

def strip(s: str) -> str:
    return HARAKAT.sub("", s).replace("\u0640", "")

def vref(s: int, i: int) -> str:
    return f"{s}:{i}"

def show(s: int, i: int, label: str) -> None:
    ar = C[str(s)]["ar"]
    for n, t in ar:
        if n == i:
            print(f"[{label}] {vref(s,i)} : {t}")
            return
    print(f"[{label}] {vref(s,i)} : ABSENT (sourate {s} a {len(ar)} versets)")

def scan_raw(pat: str, label: str, smin: int = 1, smax: int = 114) -> list:
    rx = re.compile(pat)
    hits = []
    for s in range(smin, smax + 1):
        for n, t in C[str(s)]["ar"]:
            for m in rx.finditer(t):
                a, b = max(0, m.start() - 30), min(len(t), m.end() + 30)
                hits.append((vref(s, n), t[a:b]))
    print(f"--- {label} : {len(hits)} occurrence(s)")
    for ref, ctx in hits:
        print(f"    {ref}  …{ctx}…")
    return hits

def scan_stripped(word: str, label: str, smin: int = 1, smax: int = 114) -> list:
    hits = []
    for s in range(smin, smax + 1):
        for n, t in C[str(s)]["ar"]:
            for w in t.split():
                if word in strip(w):
                    hits.append((vref(s, n), w))
    print(f"--- {label} (strip ≈ {word}) : {len(hits)} mot(s)")
    for ref, w in hits:
        print(f"    {ref}  {w}")
    return hits

print("========== 1. LEXÈME عِبَاد (élision de l'alif) ==========")
scan_raw(r"عِبَٰدَتِهِ", "لِعِبَدَتِهِ alif suscrite (élidée graphique)")
scan_raw(r"عِبَدَتِهِ", "عِبَدَتِهِ sans aucune alif")
scan_raw(r"عِبَادَتِهِ", "عِبَادَتِهِ alif pleine")
scan_raw(r"عِبَٰدِي", "عِبَدِي suscrite")
scan_raw(r"عِبَدِي", "عِبَدِي nue")
scan_raw(r"عِبَادِي", "عِبَادِي pleine")
scan_raw(r"عَبْدَنَا|عِبَٰدَنَا|عِبَدَنَا|عِبَادَنَا", "عبدنا toutes formes")
show(19, 65, "Maryam 65")
show(19, 93, "Maryam 93")
show(19, 98, "Maryam 98")
show(38, 41, "Ṣād 41")
show(38, 44, "Ṣād 44")
show(89, 29, "Fajr 29")
show(89, 32, "Fajr 32 (renvoi de l'appareil)")
print("    → tous les mots à عبد au strip (aperçu) :")
scan_stripped("عبد", "عبد générique")[:0]

print("")
print("========== 2. تُكَذِّبَانِ / الرَّحْمَن ==========")
scan_raw(r"تُكَذِّبَٰنِ", "تُكَذِّبَٰنِ alif suscrite (élidée graphique)")
scan_raw(r"تُكَذِّبَانِ", "تُكَذِّبَانِ alif pleine")

print("")
print("========== 3. أَبَا / أَبَى / أَبًى ==========")
scan_raw(r"أَبَا", "أَبَا (nom, alif pleine)")
scan_raw(r"أَبَٰى", "أَبَىٰ suscrite (verbe)")
scan_raw(r"أَبَى", "أَبَى nue")
scan_raw(r"أَبًى", "أَبًى (tanwīn)")
show(33, 40, "Aḥzāb 40")

print("")
print("========== 4. أَرْبًى / عُقْبَى / عُقْبَهَا ==========")
scan_raw(r"أَرْبًى|أَرْبَٰى|أَرْبَى|أَرْبِي", "أربى toutes formes")
scan_raw(r"عُقْبَى|عُقْبَٰى|عُقْبِي", "عُقْبَى formes")
scan_raw(r"عُقْبَهَا|عُقْبَاهَا|عُقْبَٰهَا", "عُقْبَاهَا formes")
show(91, 15, "al-Shams 15")

print("")
print("========== 5. X en Ṭāhā 119 / Qalam 50 (textes complets) ==========")
show(20, 119, "Ṭāhā 119")
show(68, 50, "Qalam 50")
show(68, 24, "Qalam 24 (الْبَاءَ?)")

print("")
print("========== 6. أَدْبَرِ (mumāla) ==========")
scan_raw(r"إِدْبَٰرَ|أَدْبَرِ|إِدْبَرَ|أَدْبَٰرِ", "أدبر/إدبار formes")

print("")
print("========== 7. ar-ribā (wāw défini vs alif indéfini) ==========")
scan_raw(r"رِبًا|رِبٰوا|رِبَوا|الرِّبَٰوا|الرِّبَوا|الرِّبَا", "ribā toutes graphies")
show(2, 275, "Baqara 275")
show(2, 276, "Baqara 276")
show(2, 278, "Baqara 278")
show(30, 39, "Rūm 39")

print("")
print("========== 8. mots-rasm du Dānī + duel marfūʿ médian ==========")
scan_raw(r"امْرَأَتَانِ|امْرَأَتَٰنِ|امْرَأَتَنِ", "امرأتان/امرأتن")
scan_raw(r"رَجُلَانِ|رَجُلَٰنِ|رَجُلَنِ", "رجلان/رجلتن")
scan_raw(r"سَحَرَانِ|سَحَرَٰنِ|سَحَرَنِ", "سحران/سحرتن")
scan_raw(r"آخَرَانِ|آخَرَٰنِ|آخَرَنِ", "آخَرَانِ formes")
show(5, 106, "Māʾida 106")
show(5, 107, "Māʾida 107")
scan_raw(r"كَانَا|قَالَا|عَمِلَا|جَاءَا", "duel verbal كَانَا etc. (aperçu 20)")
show(2, 246, "Baqara 246 (فَانْطَلَقَا?)")

print("")
print("========== 9. iʿdād (leçon suivante, chapitre du tāʾ) ==========")
scan_raw(r"كِتَبٍ|كِتَٰبٍ|كِتَابٍ", "كِتَابٍ formes")
scan_raw(r"جَنَّتَٰنِ|جَنَّتَانِ|جَنَّتَنِ", "جَنَّتَانِ formes")
show(55, 46, "Raḥmān 46")
show(55, 62, "Raḥmān 62")
scan_stripped("مبسوط", "مبسوط")
scan_stripped("تل", "تلي/اتل (aperçu)")
scan_stripped("تائب", "تائب/التائبون")
