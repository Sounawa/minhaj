# -*- coding: utf-8 -*-
"""Minhāj — assemblage + normalisation du brouillon 409 (R687)."""
import re

PARTS = [
    "/home/z/my-project/tr-tmp/l409-part1.html",
    "/home/z/my-project/tr-tmp/l409-part2.html",
    "/home/z/my-project/tr-tmp/l409-part3.html",
]
OUT = "/home/z/my-project/tr-tmp/lesson-hadith3-409-fr.html"

h = "".join(open(p, encoding="utf-8").read() for p in PARTS)

# --- corrections manuelles ciblées (avant normalisation globale) ---
FIX = [
    ("(m-rfūʿ)", "(marfūʿ)"),
    ("(<em>ad-dā</em> 'an yaḥrim dā'a bi-l-Ǧalmayn)",
     "(kān idhā arād an yaḥrim dā bi-l-Ǧalmayn)"),
    ("min chu'ʾ ḥirm", "min chu' ḥirm"),
    ("al-muchqah", "al-machaqqah"),
    ("ach-chi'r", "ach-cha'r"),
    ("yutta-rak al-aḫdh", "yutta-rak al-aḫdh"),
]
for a, b in FIX:
    h = h.replace(a, b)

# --- normalisation des caractères hors convention (convention phonétique R685) ---
h = h.replace("Ǧ", "J")       # G caron -> J
h = h.replace("ǧ", "j")       # g caron -> j
h = h.replace("Ǧ", "J")
h = h.replace("ǧ", "j")
h = h.replace("ṯ", "th")      # t point souscrit -> th
h = h.replace("Ṯ", "TH")
h = h.replace("š", "ch")      # s caron -> ch
h = h.replace("Š", "CH")
h = h.replace("č", "ch")
h = h.replace("Č", "CH")
h = h.replace("ḫ", "kh")      # h point souscrit -> kh
h = h.replace("Ḫ", "KH")
h = h.replace("ʿ", "'")       # ayn U+02BF -> U+2019
h = h.replace("ʾ", "'")       # hamza U+02BE -> U+2019

# sécurité : aucun caractère restant hors convention
leftover = sorted(set(re.findall(r"[ǦǧṯṮšŠčČḫḪʿʾ]", h)))
assert not leftover, f"caractères non normalisés restants: {leftover}"

open(OUT, "w", encoding="utf-8").write(h)
print("OK", OUT, len(h), "car")
