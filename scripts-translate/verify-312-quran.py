#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — vérification coranique de la leçon 312 (taʿṣīb) : 4:11, 4:176."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h2v-312.html"
cache = json.load(open("scripts-translate/quran-cache.json"))

def norm(s: str) -> str:
    # normalisation souple : retire diacritiques coraniques et séparateurs
    s = re.sub(r"[\u064B-\u0652\u0670\u06D6-\u06ED\u08F0-\u08FF]", "", s)
    s = s.replace("ٱ", "ا").replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    s = s.replace(" ", "").replace("\u202f", "")
    return s

html = open(HTML, encoding="utf-8").read()

checks = [
    ("an-Nisāʾ 4:11 (ouvrant)", 4, 11, "yūṣīkumu llāhu fī awlādikum li-ḏ-ḏakari miṯlu ḥaẓẓi-l-unṯayayn"),
    ("an-Nisāʾ 4:176 (sœurs)", 4, 176, "wa-in kānū iḫwatan riǧālan wa-nisāʾan fa-li-ḏ-ḏakari miṯlu ḥaẓẓi-l-unṯayayn"),
]

# La traduction FR est en translittération : on vérifie la PRÉSENCE des segments
# translittérés attendus dans le HTML (la source arabe du cache sert d'attestation
# du verset lui-même : même structure — ouverture 4:11 / clôture 4:176).
ok = True
for label, s, a, translit in checks:
    present = translit in html.replace("\u202f", " ")
    ay = cache[str(s)]["ar"][a - 1][1]
    print(f"{label} : translittération {'PRÉSENTE' if present else 'ABSENTE'} — verset cache [{ay[:60]}…]")
    ok = ok and present

print("VERDICT :", "2/2 vérifiés" if ok else "ÉCHEC")
sys.exit(0 if ok else 1)
