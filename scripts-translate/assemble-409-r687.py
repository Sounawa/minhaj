# -*- coding: utf-8 -*-
"""Minhāj — assemblage + normalisation du brouillon 409 (R687)."""
import re

PARTS = [
    "/home/z/my-project/tr-tmp/l409-part1.html",
    "/home/z/my-project/tr-tmp/l409-part2.html",
    "/home/z/my-project/tr-tmp/l409-part3.html",
    "/home/z/my-project/tr-tmp/l409-part4.html",
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
    ("la lecture littérale du glyphe de bannière restant ambiguë à 1200 dpi (خ/ض), consignée",
     "la lecture littérale du glyphe de bannière restant ambiguë à 1200 dpi (le candidat dent et le candidat dad — deux glyphes d'un seul point), consignée"),
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
h = h.replace("ġ", "gh")      # g point suscrit -> gh
h = h.replace("Ġ", "GH")
h = h.replace("Ḫ", "KH")
h = h.replace("ʿ", "'")       # ayn U+02BF -> U+2019
h = h.replace("ʾ", "'")       # hamza U+02BE -> U+2019

# sécurité : aucun caractère restant hors convention
leftover = sorted(set(re.findall(r"[ǦǧṯṮšŠčČḫḪġĠʿʾ]", h)))
assert not leftover, f"caractères non normalisés restants: {leftover}"

open(OUT, "w", encoding="utf-8").write(h)
print("assemblé :", OUT, len(h), "car")

# injection du compte de caractères (avant le fix arabe résiduel, après normalisation)
import subprocess
qa_out = subprocess.run(
    ["python3", "/home/z/my-project/scripts-translate/qa-lesson.py", OUT],
    capture_output=True, text=True,
)
m = re.search(r"QA OK : (\d+) car", qa_out.stdout)
if m:
    h2 = open(OUT, encoding="utf-8").read()
    h2 = h2.replace("QA-COUNT car au brouillon", f"{int(m.group(1)):,}".replace(",", " ") + " car au brouillon")
    open(OUT, "w", encoding="utf-8").write(h2)
    print("QA-COUNT injecté :", m.group(1))
# re-passe QA après injection (le texte a changé de taille)
r2 = subprocess.run(
    ["python3", "/home/z/my-project/scripts-translate/qa-lesson.py", OUT],
    capture_output=True, text=True,
)
print(r2.stdout.strip() or r2.stderr.strip())

