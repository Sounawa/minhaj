#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R92 — Vérification du rendu savant faraid-tanawi-3 / pdf-mut23h2v-310.

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027 (nœuds texte)
  3. guillemets « » appariés
  4. verset-image : 0 attendu / 0 trouvé (leçon pdfOnly sans images)
  5. assertions ciblées : formules d'ouverture, les trois points, les vers clés,
     les 9 cas d'exercice, les notes de tableaux
  6. 0 résidu d'édition (XXX, TODO, 【】, doubles espaces)
"""
import json
import re
import sys

TMP = "/home/z/my-project/tr-tmp/pdf-mut23h2v-310.html"
BOOK = "/home/z/my-project/content/books/faraid-tanawi-3.json"
DOC = "pdf-mut23h2v-310"

ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")

PRESENT = [
    "La science de l’exclusion successorale (ḥaǧb) (1)",
    "manẓūma al-Rasmūkiyya avec le commentaire",
    "Īḍāḥ al-asrār al-maṣūna",
    "enseignement secondaire traditionnel",
    "la première leçon",
    "Les objectifs du cours",
    "Ouverture",
    "Analyse",
    "Premier point : ce qui atteint la fille et la fille du fils",
    "Deuxième point : l’exclusion de la sœur germaine",
    "Troisième point : l’exclusion des deux époux",
    "que Dieu lui fasse miséricorde",
    "abolition (<em>isqāṭ</em>) et par participation (<em>šarika</em>)",
    "deux exclusions s’envisagent, parmi les types de cette exclusion",
    "Pour la fille du fils, tous les types s’envisagent, sans réserve",
    "Le fils l’exclut, ainsi que deux filles par leur élévation",
    "partage avec lui les deux tiers de toute succession",
    "transfère sa pareille de la moitié du bien au sixième",
    "Pour la sœur germaine, trois exclusions",
    "proche ou lointaine",
    "sauf dans l’Akdariyya : un époux, un aïeul, une mère",
    "l’accroissement (<em>ʿawl</em>) se produit",
    "Pour la sœur consanguine, quatre [exclusions] se présentent d’abord",
    "la retranchent (<em>tašqīq</em>)",
    "deux sœurs germaines, là où nul mâle ne se trouve avec elle",
    "une séparation s’impose dans la totalité du bien",
    "L’époux passe de la moitié au quart par un enfant",
    "aucune exclusion de leur quart",
    "du quart au huitième",
    "une co-épouse partage avec elle le quart",
    "Je définis l’exclusion (<em>ḥaǧb</em>) dans la langue et dans l’usage",
    "qui ne sont jamais écartés de la succession",
    "figure de l’Akdariyya",
    "question anomale (<em>šādhdha</em>)",
    "un défunt laisse un fils, une fille et une épouse",
    "une femme décède laissant deux filles, une fille de fils, une mère et le fils d’un oncle paternel",
    "un homme décède laissant un fils, une fille de fils, un père et une mère",
    "le fils du fils du fils, une fille de fils et une épouse",
    "deux filles de fils, une aïeule maternelle et un frère germain",
    "des fils, des filles, une sœur germaine et une sœur consanguine",
    "une fille, une fille de fils, une sœur germaine et une sœur consanguine",
    "une sœur germaine, une sœur consanguine et le fils d’un oncle paternel",
    "deux filles, deux sœurs consanguines, un frère consanguin et une mère",
    "tableau à compléter par l’élève",
    "quatre lignes laissées vides dans le manuel",
    "cellule latérale « la fille »",
    "cellule latérale « la fille du fils »",
    "l’un pour la sœur germaine, l’autre pour la sœur consanguine",
]

ABSENT = ["XXX", "TODO", "【", "ṣanab", "مين", "undefined", "NaN", "à compléter — deux colonnes : « le type d’exclusion » et « sa définition » ; quatre lignes vides"]


def main() -> None:
    html = open(TMP, encoding="utf-8").read()
    errors = []

    # 1. arabe
    m = ARABIC.findall(html)
    if m:
        ctx = [html[max(0, x.start() - 40):x.start() + 40] for x in ARABIC.finditer(html)]
        errors.append(f"1. ARABE RESIDUEL ({len(m)} car) : " + " | ".join(ctx[:3]))

    # 2. apostrophe droite
    n_ap = html.count("'")
    if n_ap:
        errors.append(f"2. APOSTROPHE DROITE ({n_ap})")

    # 3. guillemets
    n_o, n_c = html.count("«"), html.count("»")
    if n_o != n_c:
        errors.append(f"3. GUILLEMETS non appariés : {n_o} vs {n_c}")

    # 4. verset-image : la leçon pdfOnly n'en a pas
    book = json.load(open(BOOK, encoding="utf-8"))
    les = next((l for l in book["lessons"] if str(l.get("docId")) == DOC), None)
    if les is None:
        errors.append("4. DOC ABSENT du book")
    else:
        src_img = (les.get("html") or "").count("<img")
        fr_img = (les.get("htmlFr") or "").count("<img") + html.count("<img")
        if src_img or fr_img:
            errors.append(f"4. VERSET-IMAGE inattendu : src={src_img} fr={fr_img}")

    # 5. assertions (normalisation des espaces fines/insécables insérées par qa-lesson)
    def _norm(t: str) -> str:
        return t.replace("\u202f", " ").replace("\u00a0", " ")

    hn = _norm(html)
    for s in PRESENT:
        if _norm(s) not in hn:
            errors.append(f"5. ABSENT ATTENDU : {s[:80]}")

    # 6. résidus
    for s in ABSENT:
        if _norm(s) in hn:
            errors.append(f"6. RÉSIDU INTERDIT : {s[:60]}")
    if re.search(r" {2,}", re.sub(r"<[^>]+>", "", html)):
        errors.append("6. DOUBLE ESPACE dans les nœuds texte")

    if errors:
        print("ECHEC verify-r92 :")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print(f"verify-r92 PASS : {len(html)} car — 0 arabe, 0 apostrophe droite, "
          f"guillemets appariés ({n_o}), 0 verset-image attendu/trouvé, "
          f"{len(PRESENT)} assertions OK, 0 résidu")


if __name__ == "__main__":
    main()
