#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj R33 — Normalisation des titres FR de fiqh-tanawi-2
(fins des titres GT « vendre pacifiquement » [bayʿ salam ≠ paix],
« le musulman » [al-muslam = l'objet livrable du salam],
« hypothécaires » [rahn = gage] → convention savante gh/j alignée sur
tafsir-tanawi-2 ; DIN sans carons : Khalīl, al-Dardīr, al-Dasūqī).
"""

import json

PATH = "/home/z/my-project/content/books/fiqh-tanawi-2.json"

TITLES = {
    "12177": "Présentation du manuel",
    "12230": "Règles de la garantie du capital du salam",
    "12232": "Règles de la vente d’une marchandise contre une marchandise, en salam",
    "12239": "Détermination de l’objet du salam et clarification de ses qualités",
    "12241": "L’objet du salam, dette à la charge du vendeur, et son existence à l’échéance",
    "12242": "Règles du salam sur le fruit d’un verger déterminé",
    "12243": "Ce en quoi le salam est valable et ce en quoi il ne l’est pas",
    "12253": "Ce en quoi le salam n’est pas valable (suite)",
    "12261": "L’acceptation du semblable de l’objet du salam, en qualité et en espèce, avant l’échéance",
    "12498": "Règles du prêt (qarḍ)",
    "12499": "Règles de la compensation (muqāṣṣa)",
    "12500": "Règles du gage (rahn)",
    "12502": "Règles du gage (suite)",
    "12503": "Invalidateurs du gage",
    "12505": "Règles de la détention du gage",
    "12510": "Règles de la disposition du gage par le constituant",
    "12512": "Règles de la responsabilité du gage (ḍamān al-rahn)",
    "12517": "Règles du différend entre le constituant et le créancier gagistes",
    "12519": "Index des figures citées",
    "12522": "Liste des sources et références",
    "13349": "Index des figures citées",
    "13353": "Liste des sources et références",
}


def main() -> None:
    with open(PATH, encoding="utf-8") as fh:
        data = json.load(fh)
    n = 0
    for lesson in data.get("lessons", []):
        new = TITLES.get(str(lesson.get("docId")))
        if new and lesson.get("titleFr") != new:
            lesson["titleFr"] = new
            n += 1
    intro = data.get("intro")
    if intro and intro.get("docId") is not None:
        new = TITLES.get(str(intro["docId"]))
        if new and intro.get("titleFr") != new:
            intro["titleFr"] = new
            n += 1
    with open(PATH + ".tmp", "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    import os
    os.replace(PATH + ".tmp", PATH)
    print(f"✅ {n} titres normalisés dans fiqh-tanawi-2.json")


if __name__ == "__main__":
    main()
