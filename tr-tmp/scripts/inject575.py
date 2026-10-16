#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Injection de la leçon 575 (pdf-only) + CORRECTION de la réf Bayḍāwī de 574.

575 = سورة الحديد (الآيات 19-23) = Ḥafṣ/Warš 20-24 (règle R84 : manual N = Ḥafṣ N+1
pour N≥15). Bloc = 5 versets Warš du cache, numérotation madrasa ١٩-٢٣, se terminant
à ٱلْغَنِىُّ ٱلْحَمِيدُ (label pixel-vérifié [سورة الحديد: ١٩-٢٣] + ۝٢٣).

Fix 574 : la réf [تفسير البيضاوي: 108/1] livrée en R84 était une méslecture —
pixel-vérification 600 dpi de ce tour : les 2e et 3e chiffres sont des «8» (anneau
à barre médiane), pas «0» (anneau vide). Print réel : [تفسير البيضاوي: 188/1]
(pages 188→189 consécutives avec la réf Bayḍāwī de 575 = 189/5 ; le «1» final est
vraisemblablement une coquille du manuel pour «5», transcrit tel quel).
"""
import json, os, re, tempfile

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"
AR575 = "/home/z/my-project/tr-tmp/575-ar.html"
FR575 = "/home/z/my-project/tr-tmp/575-fr.html"
DOCID = "pdf-mut23h33-575"
OLD574 = "pdf-mut23h33-574"

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

html575 = open(AR575, encoding="utf-8").read().strip()
fr575 = open(FR575, encoding="utf-8").read().strip()
assert html575.startswith("<h1>") and fr575.startswith("<h1>")
assert "{{" not in fr575 and "<img" not in fr575
assert "۞" not in html575

data = json.load(open(BOOK, encoding="utf-8"))
lessons = {les.get("docId"): les for les in data["lessons"]}

# ---------- 1) injection 575 ----------
les = lessons[DOCID]
assert "19 - 23" in les["titleAr"] or "19" in les["titleAr"], les["titleAr"]
les["html"] = html575
les["htmlFr"] = fix_fr(fr575)
les["pdfOnly"] = False

# ---------- 2) correction 574 — réf Bayḍāwï 108/1 -> 188/1 (pixel-vérifiée) ----------
old574 = lessons[OLD574]["html"]
anchor574 = "[تفسير البيضاوي: 108/1]"
assert old574.count(anchor574) == 1, old574.count(anchor574)
old574 = old574.replace(anchor574, "[تفسير البيضاوي: 188/1]")
assert old574.count("[تفسير البيضاوي: 188/1]") == 1
lessons[OLD574]["html"] = old574

# ---------- 3) écriture atomique ----------
d = os.path.dirname(BOOK)
fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
with os.fdopen(fd, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
os.replace(tmp, BOOK)

print(f"OK: {DOCID} injecté ({len(html575)} car AR, {len(fr575)} car FR)")
print(f"OK: {OLD574} corrigé — réf Bayḍāwī 108/1 → 188/1 (pixel-vérifiée 600 dpi)")
