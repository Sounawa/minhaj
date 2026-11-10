# -*- coding: utf-8 -*-
"""Minhāj — Mapping par texte des āyāt de la leçon 406 (R673) sur le cache ḥafṣ.
Normalisation robuste : hamza-alefs unifiés, maqsūra→yāʾ, alef suscrite→alef
(sauf après maqsūra), diacritiques et petit-vāw supprimés."""
import json
import re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"

def norm(t):
    t = t.replace("\u0640", "")                       # tatweel
    t = t.replace("ىٰ", "ى")                          # maqsūra + alef suscrite → maqsūra
    t = t.replace("\u0671", "ا").replace("\u0670", "ا")  # wasla / alef suscrite → alef
    t = re.sub(r"[\u064B-\u065F\u06D6-\u06ED\uFEFF]", "", t)  # diacritiques, signes coraniques
    t = re.sub(r"[إأآٱ]", "ا", t)                     # hamza-alefs → alef
    t = t.replace("ى", "ي")                           # maqsūra → yāʾ
    return t

def rm(t):
    return re.sub(r"\s+", "", norm(t))

cache = json.load(open(CACHE, encoding="utf-8"))

QUERIES = {
    "hadj-bayt": "ولله على الناس حج البيت من استطاع اليه سبيلا ومن كفر فان الله غني عن العالمين",
    "salati": "قل ان صلاتي ونسكي ومحياي ومماتي لله رب العالمين",
    "la-sharika": "لا شريك له وبذلك امرت وانا اول المسلمين",
    "ma-fi-samawat": "ولله ما في السماوات وما في الارض وكفى بالله وكيلًا",
    "istaysara": "فما استيسر من الهدي",
    "kacba": "جعل الله الكعبة البيت الحرام قياما للناس والشهر الحرام والهدي والقلايد",
    "yucamm-shaair": "ذلك ومن يعظم شعائر الله فانها من تقوى القلوب",
    "tukabbiru": "ليكبروا الله على ما هداكم",
    "lakum-fiha": "لكم فيها منافع الي اجل مسمى",
}

for label, q in QUERIES.items():
    qn = rm(q)
    hits = []
    for sn, sura in cache.items():
        for n, txt in sura["ar"]:
            if qn and qn in rm(txt):
                hits.append(f"{sura['number']}:{n}")
    print(f"{label:18s} → {' | '.join(hits) if hits else 'AUCUN'}")

print()
for sn, ay in [("3", 97), ("22", 30), ("22", 31), ("22", 32), ("22", 33),
               ("22", 36), ("22", 37), ("22", 162), ("22", 163), ("5", 97), ("2", 196)]:
    sura = cache[str(int(sn))] if str(int(sn)) in cache else cache[sn]
    for n, txt in sura["ar"]:
        if n == ay:
            print(f"=== sura {sura['number']} {sura['englishName']} āya {n} ===")
            print(txt[:400])
            print()
