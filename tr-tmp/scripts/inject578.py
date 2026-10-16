#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Injection de la leçon 578 (pdf-only, 16e leçon tafsir-2es).

578 = سورة المجادلة (الآيات 1-4) = Ḥafṣ 1-4 (s58 : AUCUN offset ḥurūf —
marqueurs muṣḥaf ۝١-۝٤ pixel-vérifiés VLM+TSV = numérotation alignée). Le
tamhīd du manuel dénombre « إحدى وعشرون » (21 versets) = décompte marocain
Warš vs 22 Ḥafṣ — la fusion des versets est APRÈS v7 (à surveiller en 580+).
Basmala = ligne SÉPARÉE dans le cadre آيات (première sura du niveau 3 où
elle est détachée de v1 — v1 du cache débarrassé de son préfixe basmala).

Vérifications R91 (tesseract 300+600 dpi × multi-seuils + VLM sur chiffres/mots
candidats + web-search de l'original eshia du Tashīl) :
- Label [سورة المجادلة: 4-1] (tesseract+tesseract+VLM concordants).
- Réfs pixel-vérifiées : [تفسير البيضاوي: 193/5] (VLM+tesseract, = intel
  session perdue ✓) ; [المحرر الوجيز لابن عطية: 352/2] ; [أحكام القرآن لأبي
  بكر بن العربي: 185/4].
- Règle d'or idad→glose 9e fois, en REVERSE (pattern R89) : les gloses 578
  (سَمِعَ / تُجَادِلُكَ فِي زَوْجِهَا / مُنْكَرًا مِنَ الْقَوْلِ / وَزُورًا / يَتَمَاسَّا)
  ont tranché RÉTROACTIVEMENT les idad 577 mal transcrits → CORRECTION de
  577 injectée ce tour : «قَوْلَ»→«سَمِعَ» et «فِي زَوْجِهَا»→«تُجَادِلُكَ فِي
  زَوْجِهَا» (AR+FR) — vérifié par glyphes : lemma A 577 = س-م-ع identique au
  glose 578 (ASCII superposable), lemma B 577 = تُجَادِلُكَ (première lettre ت
  2 points + bol plat, pas de ٢ points sur bol plongeant = pas un ق).
- «يَتَمَاسَّا: يجتمعا» (tesseract ×3 psm8 crops ; VLM lisait يلتقيان — flag
  variante) ; «حاورت الرسول» (tesseract ×3 sur le titre de section ; VLM
  جادلت rejeté) ; «رِجَالَات قُرَيْش» (VLM + OCR ×3) ; «فقامت/لقمت» (600 dpi
  q3 ×2) ; «مرونته» (nūn vs hamza, 300 dpi ×2).
- Lignes FAIBLES (encre pâle du PDF, seuil <185) résolues : «الزوجة بمحارمه.»
  (fin du passage malikite — t200 sur crop serré + strokes ال/ز ; flag 10+
  tentatives) ; «يعجز عن الثاني.» (fin de la hiérarchie des kafārāt — VLM +
  contexte + ancrage droit court ✓).
- «وكانت «وَتَشْتَكِي إِلَى اللَّهِ» فتقول» — le fragment coranique en police
  muṣḥaf RÉSOLU par web-search de l'original (eshia.ir/41713/2/351) :
  l'édition porte «جدالها وَتَشْتَكِي إِلَى اللَّهِ كانت تقول» ; le manuel
  réarrange avec guillemets — 600 dpi t180 : «وكانت «إتشتكج إلواللة» فتقول».
- Requote muṣḥaf de la kafāra = v3 (وَٱلَّذِينَ…يَتَمَآسَّا) + v4 (فَمَن لَّمْ
  يَجِدْ…مِسْكِينًۭا), SANS ذَٰلِكُمْ تُوعَظُونَ (quoté séparément ensuite par
  Bayḍāwī) — confirmé par 300 dpi complet + VLM première ligne.
- Idad 579 (المجادلة 5-7) transcrits et VLM-vérifiés : «يُحَادُّونَ» -
  «كُبِتُوا» - «أَحْصَاهُ» - «شَهِيدٌ» + Q2 جزاء من يعاند الله ورسوله.
"""
import json, re

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"
AR578 = "/home/z/my-project/tr-tmp/578-ar.html"
FR578 = "/home/z/my-project/tr-tmp/578-fr.html"
DOCID = "pdf-mut23h33-578"

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

html578 = open(AR578, encoding="utf-8").read().strip()
fr578 = open(FR578, encoding="utf-8").read().strip()
assert html578.startswith("<h1>") and fr578.startswith("<h1>")
assert "{{" not in fr578 and "<img" not in fr578
assert "۞" not in html578
assert "regarding" not in fr578

data = json.load(open(BOOK, encoding="utf-8"))
lessons = {les.get("docId"): les for les in data["lessons"]}

les = lessons[DOCID]
assert "1" in les["titleAr"] and "4" in les["titleAr"], les["titleAr"]
les["html"] = html578
les["htmlFr"] = fix_fr(fr578)
les["pdfOnly"] = False

# Contrôle que la correction 577 est bien en place (règle d'or reverse)
l577 = lessons["pdf-mut23h33-577"]
assert "«سَمِعَ» - «تُجَادِلُكَ فِي زَوْجِهَا»" in l577["html"], "correction 577 AR absente"
assert "samiʿa" in l577["htmlFr"], "correction 577 FR absente"

json.dump(data, open(BOOK, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("OK — 578 injectée :", len(html578), "car AR,", len(fix_fr(fr578)), "car FR")
print("titleAr:", les["titleAr"], "| titleFr:", les["titleFr"])
