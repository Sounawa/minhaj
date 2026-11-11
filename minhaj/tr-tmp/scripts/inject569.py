#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Injection de la leçon 569 (pdf-only) + CORRECTION de la leçon 568.

Correction 568 (découverte R81) : le PDF 568 s'arrête à «…تحويلا ۝٤٤ [سورة فاطر: 44-41]»
(voirlet 44 du comptage manuel = la sunna «فهل ينظرون…تحويلا»). La livraison R80 avait :
  - fusionné la sunna dans [فاطر: 43] (cache v43),
  - ajouté à tort [فاطر: 44] = «أولم يسيروا…عليما قديرا» (cache v44) —
    ce verset appartient à la leçon 569 (v45 du comptage manuel,
    confirmé par l'استثمار [فاطر: 45] et la question [فاطر: 45] du PDF 569).
Fix : v43 = «استكبارًا…بأهله», v44 = «فهل ينظرون…تحويلا», suppression du verset en trop.
"""
import json, os, re, tempfile

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"
CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
AR569 = "/home/z/my-project/tr-tmp/569-ar.html"
FR569 = "/home/z/my-project/tr-tmp/569-fr.html"
DOCID = "pdf-mut23h33-569"
OLD568 = "pdf-mut23h33-568"

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

def para_around(hay: str, anchor: str):
    """Retourne (start, end) du <p>…</p> contenant anchor (première occurrence)."""
    i = hay.find(anchor)
    assert i >= 0, f"ancre introuvable: {anchor[:40]}"
    s = hay.rfind("<p>", 0, i)
    e = hay.find("</p>", i) + len("</p>")
    return s, e

cache = json.load(open(CACHE, encoding="utf-8"))
s35 = cache["35"]["ar"]
v43_full = [t for n, t in s35 if n == 43][0]      # استكبارًا…تحويلا (cache)
split_at = v43_full.find(" ۚ فَهَلْ")
assert split_at > 0
v43_new = v43_full[:split_at]                      # …بِأَهْلِهِۦ
v44_new = v43_full[split_at + len(" ۚ "):]         # فَهَلْ يَنظُرُونَ…تحويلا

html569 = open(AR569, encoding="utf-8").read().strip()
fr569 = open(FR569, encoding="utf-8").read().strip()
assert html569.startswith("<h1>") and fr569.startswith("<h1>")
assert "{{U" not in fr569 and "<img" not in fr569

data = json.load(open(BOOK, encoding="utf-8"))
lessons = {les.get("docId"): les for les in data["lessons"]}

# ---------- 1) injection 569 ----------
les = lessons[DOCID]
les["html"] = html569
les["htmlFr"] = fr569
les["pdfOnly"] = False

# ---------- 2) correction 568 — bloc الآيات AR ----------
old = lessons[OLD568]["html"]
# 2a. supprimer le verset en trop [فاطر: 44] = أولم يسيروا (identifier par «أَوَلَمْ يَسِيرُوا۟»)
s, e = para_around(old, "أَوَلَمْ يَسِيرُوا۟")
assert "[فاطر: 44]" in old[s:e], old[s:e][:80]
old = old[:s] + old[e:]
# 2b. scinder l'ancien [فاطر: 43] (استكبارًا + sunna fusionnés) en v43 + v44
s, e = para_around(old, "ٱسْتِكْبَارًۭا")
assert "[فاطر: 43]" in old[s:e]
new_pair = ('<p>«' + v43_new + '» [فاطر: 43]</p>\n'
            '<p>«' + v44_new + '» [فاطر: 44]</p>')
old = old[:s] + new_pair + old[e:]
assert old.count("[فاطر: 44]") == 1
assert "أَوَلَمْ يَسِيرُوا۟" not in old.replace("«أَوَلَمْ يَسِيرُوا۟", "@@@" + "أَوَلَمْ يَسِيرُوا۟") or True
assert "يَسِيرُوا۟ فِى ٱلْأَرْضِ فَيَنظُرُوا۟" not in old  # plus aucun أولم يسيروا dans 568
lessons[OLD568]["html"] = old

# ---------- 3) correction 568 — bloc Les versets FR ----------
oldf = lessons[OLD568]["htmlFr"]
# 3a. supprimer «N'ont-ils donc jamais parcouru…» (44-Ḥafṣ = premier م يسيروا)
s, e = para_around(oldf, "ont-ils donc jamais parcouru")
assert "(44)" in oldf[s:e]
oldf = oldf[:s] + oldf[e:]
# 3b. scinder le (43) en (43)+(44)
s, e = para_around(oldf, "par orgueil sur terre")
assert "(43)" in oldf[s:e]
p43 = fix_fr('<p>« par orgueil sur terre et par manœuvre perfide. Cependant, '
             'la manœuvre perfide n\'enveloppe que ses propres auteurs » (43)</p>')
p44 = fix_fr('<p>« Attendent-ils donc un autre sort que celui des Anciens ? '
             'Or, jamais tu ne trouveras de changement dans la règle d\'Allah et jamais '
             'tu ne trouveras de déviation dans la règle d\'Allah » (44)</p>')
oldf = oldf[:s] + p43 + "\n" + p44 + oldf[e:]
assert oldf.count("(44)") == 1
assert "donc jamais parcouru" not in oldf
lessons[OLD568]["htmlFr"] = oldf

# ---------- 4) écriture atomique ----------
d = os.path.dirname(BOOK)
fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
with os.fdopen(fd, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
os.replace(tmp, BOOK)

print(f"OK: {DOCID} injecté ({len(html569)} car AR, {len(fr569)} car FR)")
print(f"OK: {OLD568} corrigé — v43 scindée en v43+v44(sunna), verset أولم يسيروا retiré")
print(f"    568 AR: {len(old)} car | 568 FR: {len(oldf)} car")
