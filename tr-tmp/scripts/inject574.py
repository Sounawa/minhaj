#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Injection de la leçon 574 (pdf-only) + CORRECTION de la leçon 573.

Correction 573 (découverte R84) : le muṣḥaf madrasa FOND Ḥafṣ 14-15 en un seul
verset 14 (preuve triple : label 574 = [الحديد: ١٥-١٨] lu au pixel + bloc 574
commençant à «ألم يأن» (Ḥafṣ 16) + lemmes idad 574 tous dans Ḥafṣ 20/23 pour
la leçon 575 = manual 19-23). La livraison R83 avait coupé le v14 à «ٱلْغَرُورُ»
(bordure cache ḥafṣienne) — le bloc imprimé du PDF 573 continue jusqu'à
«وَبِئْسَ ٱلْمَصِيرُ» (fin de Ḥafṣ 15, lue sur p2 : b00/b01 + ۝١٤).
Fix : v14 (AR+FR) étendu du tail Ḥafṣ 15 ; note NdT ajoutée en FR.
"""
import json, os, re, tempfile

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"
CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
AR574 = "/home/z/my-project/tr-tmp/574-ar.html"
FR574 = "/home/z/my-project/tr-tmp/574-fr.html"
DOCID = "pdf-mut23h33-574"
OLD573 = "pdf-mut23h33-573"

NB = "\u202f"
def fix_fr(s: str) -> str:
    """Mêmes auto-fixes que scripts-translate/qa-lesson.py (nœuds texte uniquement)."""
    parts = re.split(r"(<[^>]+>)", s)
    for k, tok in enumerate(parts):
        if tok.startswith("<"):
            continue
        tok = tok.replace(" ;", NB + ";").replace(" :", NB + ":").replace(" !", NB + "!")
        tok = tok.replace(" ?", NB + "?").replace(" »", NB + "»").replace("« ", "«" + NB)
        tok = tok.replace("'", "\u2019")
        tok = re.sub(r"  +", " ", tok)
        parts[k] = tok
    return "".join(parts)

cache = json.load(open(CACHE, encoding="utf-8"))
s57 = cache["57"]["ar"]
v15h = [t for n, t in s57 if n == 15][0]      # فَٱلْيَوْمَ...ٱلْمَصِيرُ (Warš, Ḥafṣ 15)

html574 = open(AR574, encoding="utf-8").read().strip()
fr574 = open(FR574, encoding="utf-8").read().strip()
assert html574.startswith("<h1>") and fr574.startswith("<h1>")
assert "{{" not in fr574 and "<img" not in fr574
assert "۞" not in html574.split("</h1>")[1][:100]

data = json.load(open(BOOK, encoding="utf-8"))
lessons = {les.get("docId"): les for les in data["lessons"]}

# ---------- 1) injection 574 ----------
les = lessons[DOCID]
assert les["titleAr"].strip().endswith("15 - 18)") or "15" in les["titleAr"], les["titleAr"]
les["html"] = html574
les["htmlFr"] = fix_fr(fr574)
les["pdfOnly"] = False

# ---------- 2) correction 573 — bloc الآيات AR ----------
old = lessons[OLD573]["html"]
anchor_ar = "ٱلْغَرُورُ» [الحديد: 14]</p>"
assert old.count(anchor_ar) == 1, old.count(anchor_ar)
new_para_tail = ("ٱلْغَرُورُ " + v15h + "» [الحديد: 14]</p>")
old = old.replace(anchor_ar, new_para_tail)
assert old.count("[الحديد: 14]") == 1
assert "فَٱلْيَوْمَ لَا يُؤْخَذُ مِنكُمْ" in old
assert "وَبِئْسَ ٱلْمَصِيرُ" in old
lessons[OLD573]["html"] = old

# ---------- 3) correction 573 — bloc Les versets FR ----------
oldf = lessons[OLD573]["htmlFr"]
anchor_fr = "au sujet de Dieu”" + NB + "» (14)</p>"
assert oldf.count(anchor_fr) == 1, repr(oldf.count(anchor_fr))
append_fr = fix_fr(
    "au sujet de Dieu. Aujourd’hui donc, on n’acceptera de rançon ni de vous ni de "
    "ceux qui ont mécru. Votre asile est le Feu : c’est lui qui est votre compagnon "
    "inséparable. Et quelle mauvaise destination !”» (14) "
    "<em>(NdT — le muṣḥaf de l’école fond ici, en un seul verset 14, ce que le "
    "décompte ḥafṣien numérote 14-15.)</em></p>"
).replace("»»", "»")
oldf = oldf.replace(anchor_fr, append_fr)
assert oldf.count("(14)") == 1
assert "mauvaise destination" in oldf
lessons[OLD573]["htmlFr"] = oldf

# ---------- 4) écriture atomique ----------
d = os.path.dirname(BOOK)
fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
with os.fdopen(fd, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
os.replace(tmp, BOOK)

print(f"OK: {DOCID} injecté ({len(html574)} car AR, {len(fr574)} car FR)")
print(f"OK: {OLD573} corrigé — v14 étendu du tail Ḥafṣ 15 (فَٱلْيَوْمَ…ٱلْمَصِيرُ) + note NdT")
print(f"    573 AR: {len(old)} car | 573 FR: {len(oldf)} car")
