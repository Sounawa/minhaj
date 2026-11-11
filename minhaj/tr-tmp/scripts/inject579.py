#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Injection de la leçon 579 (pdf-only, 17e leçon tafsir-2es). المجادلة 5-7.

579 = المجادلة (الآيات 5-7) = Ḥafṣ 5-7 (PAS de décalage : v5/v6/v7 du bloc
identifiés verbatim dans le cache Warš ; la fusion 21-vs-22 est donc APRÈS v7).
Label pixel-vérifié [سورة المجادلة: ٥-٧] (p2, 600dpi). Header الدرس ٢٤ (VLM).

Vérifications R89 :
- Gloses (5) : يُحَادُّونَ: يخالفون ويعادون ✓ / كُبِتُوا: هلكوا ولعنوا ✓ /
  أَحْصَاهُ: عَدَّهُ ✓ / شَهِيدٌ: مشاهد ✓ / نَّجْوَىٰ: الكلام الخفي (lemma
  flaggé — OCR يلي/لي résistant, sens certain par v7).
- RÈGLE D'OR 10e fois : idad 578 (يُحَادُّونَ/كُبِتُوا/أَحْصَاهُ/شَهِيدٌ) =
  gloses 1-4 de 579 ; la 5e (نَّجْوَىٰ) vient du verset 7 même.
- Réfs : [تفسير القرآن العظيم؛ لابن كثير: 72/8] ✓ (600dpi) ;
  [تفسير البيضاوي: 194/5] ✓ — CONSÉCUTIF avec 193/5 de la leçon 578 !
  [سنن ابن ماجه؛ أبواب الزهد؛ باب ذكر الذنوب] ✓ (×2 lectures).
- Édad 580 pré-validé par les gloses de 580 (PDF téléchargé ce tour) :
  النَّجْوَى: يتحدثون سرا / الإثم: المعصية / العدوان: الظلم /
  يَصْلَوْنَهَا: يقاسون حرها — lemmes idad 579 pixel-locked par analyse
  d'encre (3 tirets cachés détectés, 4 tokens : النَّجْوَى (315px, tall
  lam-alif initial, finale ى) - بالإثم - والعدوان - يَصْلَوْنَهَا (401px,
  ص→خ OCR, validé par glose 580 «يقاسون حرّها»)).
- Flags : «الدنيا» (OCR ×2 «الدنياء» — bruit probable) ; «بينهما» (OCR
  «بينهاً») ; تقويم Q3 «ما هي أثر» (grammaire, tel qu'imprimé ×2) ;
  hadith «لأعلمنَّ» (OCR لأعلمنٌ) ; أتأمل Q «في السر والعلانية» (×2
  concordants, cohérent avec l'objectif 3).
"""
import json, re

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"
AR579 = "/home/z/my-project/tr-tmp/579-ar.html"
FR579 = "/home/z/my-project/tr-tmp/579-fr.html"
DOCID = "pdf-mut23h33-579"

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

html579 = open(AR579, encoding="utf-8").read().strip()
fr579 = open(FR579, encoding="utf-8").read().strip()
assert html579.startswith("<h1>") and fr579.startswith("<h1>")
assert "{{" not in fr579 and "<img" not in fr579
assert "۞" not in html579
# cohérence bloc = cache
for frag in ["يُحَآدُّونَ", "كُبِتُوا۟", "أَحْصَىٰهُ", "نَّجْوَىٰ", "رَابِعُهُمْ", "سَادِسُهُمْ"]:
    assert frag in html579, frag
# cohérence idad ↔ gloses 580 (pré-validées)
for frag in ["النَّجْوَىٰ", "بِالْإِثْمِ", "وَالْعُدْوَانِ", "يَصْلَوْنَهَا"]:
    assert frag in html579, frag

data = json.load(open(BOOK, encoding="utf-8"))
lessons = {les.get("docId"): les for les in data["lessons"]}

les = lessons[DOCID]
assert "5 - 7" in les["titleAr"] or "5-7" in les["titleAr"], les["titleAr"]
les["html"] = html579
les["htmlFr"] = fix_fr(fr579)
les["pdfOnly"] = False

json.dump(data, open(BOOK, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("OK — 579 injectée :", len(html579), "car AR,", len(fix_fr(fr579)), "car FR")
print("titleAr:", les["titleAr"], "| titleFr:", les["titleFr"])
