#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : intro muqaddima (tawhid-1es, Présentation du manuel).

Vérifications :
- Texte éditorial Minhāj (2 paragraphes) : registre savant, translittération
  systématique, parenthèses de traduction pour les titres arabes.
- FIX vs baseline GT : « ibn Abī Zayd » → « b. Abī Zayd » (convention corpus) ;
  « l'introduction de l'Épître » → « de la Risāla » (titre maintenu en arabe,
  convention des livres frères — hadith-1es Muwaṭṭaʾ, fiqh-tanawi Mudawwana) ;
  « gens de la Sunna et du Consensus » conservé (convention 12875).
- Injection : intro (d['intro']), pas une leçon — code dédié (pattern up-14604).
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd — présentation du manuel</h1>
<p>La matière du Tawḥīd s’ouvre, en la première année du cycle secondaire de l’enseignement traditionnel (<em>taʿlīm ʿatīq</em>), sur l’introduction de la <em>Risāla</em> de l’imam Abū Muḥammad ʿAbd Allāh b. Abī Zayd al-Qayrawānī (m. 386 H.) — le juriste du Maghreb et imam des mālikites de son époque —, avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> [« Le suffisant du disciple voué au Seigneur »] d’Abū l-Ḥasan, qui est le commentaire agréé dans l’enseignement traditionnel marocain.</p>
<p>La matière expose la doctrine des gens de la Sunna et du Consensus (<em>ahl al-sunna wa-l-jamāʿa</em>) selon l’école de l’imam Mālik, telle que l’introduction de la <em>Risāla</em> la fixe : les attributs de Dieu, Puissant et Majestueux, leur nécessité et l’impossibilité de leurs contraires ; le décret et la prédestination (<em>qaḍāʾ wa-l-qadar</em>) ; la foi en la totalité des réalités invisibles ; ce qui est dû aux envoyés et aux Compagnons — en une langue pédagogique simplifiée.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    intro = d.get("intro") or {}
    if str(intro.get("docId")) != "muqaddima":
        raise SystemExit("ERREUR: intro muqaddima introuvable dans tawhid-1es")
    intro["htmlFr"] = HTML_FR
    d["intro"] = intro
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — intro muqaddima upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
