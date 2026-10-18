#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : intro 14604 (tafsir-6ep, Présentation du manuel).

Vérifications :
- Structure harmonisée sur 12609 (intro main de tafsir-5ep, même série) :
  h1 « Le Tafsīr à travers le Tafsīr al-Jalālayn — sixième année… »,
  « Sommaire des leçons » numéroté (le <ul> brut de la source est anonyme —
  titre ajouté comme en 12609), compétences en h2 + infinitifs.
- FIX vs baseline LLM : « qu'Allah les agrée » (radiya Allāhu ʿanhum —
  réservé aux Compagnons !) → « qu'Allah leur fasse miséricorde » (رحمهما
  الله, correct pour Maḥallī et Suyūṭī) ; « Tafsīr al-Qur'ān al-ʿAẓīm » →
  « Tafsīr al-Qurʾān al-ʿAẓīm » (ʾ) ; « la troisième boucle » → « le
  troisième maillon » (حلقة ثالثة) ; « ḥizb (section) cinquante-huit » →
  « cinquante-huitième ḥizb » ; tiret et ʿaṭīq systématisés.
- Sommaire : 28 leçons (al-Jinn ×5, al-Muzzammil ×3, al-Muddaththir ×6,
  al-Qiyāmah ×5, al-Insān ×5, al-Mursalāt ×4) + aʿlām + sources = 30
  entrées ; « les deux versets 30-31 » → « versets 30 et 31 » ; « le
  verset 18 » (al-Muzzammil) ; artefacts &nbsp; nettoyés.
- h1 source « كتاب: التفسير… » (double-point parasite OCR) — corrigé.
- Injection : intro (d['intro']), pas une leçon — code dédié.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-6ep.json"

HTML_FR = """<h1>Le Tafsīr à travers le Tafsīr al-Jalālayn — sixième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq)</h1>
<p>Le livre de tafsīr de la sixième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq) constitue le troisième maillon de la série des livres de tafsīr composée pour ce cycle, conformément aux finalités qui encadrent le programme et aux orientations sur lesquelles se fondent les méthodes et les programmes de l'enseignement traditionnel — dans l'ouverture aux innovations pédagogiques contemporaines.</p>
<p>Nous avons pris pour source principale de la matière, pour l'approche des sens des sourates prescrites, le « Tafsīr al-Qurʾān al-ʿAẓīm » des deux Jalāl — Jalāl al-Dīn al-Maḥallī et Jalāl al-Dīn al-Suyūṭī, qu'Allah leur fasse miséricorde —, que nous avons enrichi des ajouts, emprunts et citations appropriés, en recourant aux ouvrages-mères de l'exégèse.</p>
<p>Le contenu du livre a été présenté en un style accessible et par des activités variées, qui aident l'apprenant(e) à comprendre les sens du cinquante-huitième ḥizb du Noble Coran, à enrichir ses connaissances et investir ses acquis, à développer ses compétences, à s'engager dans l'apprentissage autonome et la participation active à la construction du savoir, et à dégager les bénéfices et les valeurs qui le guident vers l'incarnation des valeurs optimales — fondées sur les principes du dogme sain et les règles des nobles mœurs et vertus — visant la purification de l'âme, le renforcement du lien avec le Livre d'Allah, le Très-Haut, l'ancrage des valeurs nationales, humaines, de droits et sociales, et la promotion de la tolérance et de la coexistence avec tous les hommes, en préservant les constantes faisant consensus parmi les Marocains.</p>
<p>Notre grand espoir est que ce livre réponde à vos besoins cognitifs et éducatifs.</p>
<h3>Sommaire des leçons</h3>
<ul>
<li>1. Sourate al-Jinn, versets 1 à 7</li>
<li>2. Sourate al-Jinn, versets 8 à 12</li>
<li>3. Sourate al-Jinn, versets 13 à 17</li>
<li>4. Sourate al-Jinn, versets 18 à 23</li>
<li>5. Sourate al-Jinn, versets 24 à 28</li>
<li>6. Sourate al-Muzzammil, versets 1 à 8</li>
<li>7. Sourate al-Muzzammil, versets 9 à 17</li>
<li>8. Sourate al-Muzzammil, verset 18</li>
<li>9. Sourate al-Muddaththir, versets 1 à 7</li>
<li>10. Sourate al-Muddaththir, versets 8 à 17</li>
<li>11. Sourate al-Muddaththir, versets 18 à 29</li>
<li>12. Sourate al-Muddaththir, versets 30 et 31</li>
<li>13. Sourate al-Muddaththir, versets 32 à 47</li>
<li>14. Sourate al-Muddaththir, versets 48 à 55</li>
<li>15. Sourate al-Qiyāmah, versets 1 à 12</li>
<li>16. Sourate al-Qiyāmah, versets 13 à 18</li>
<li>17. Sourate al-Qiyāmah, versets 19 à 24</li>
<li>18. Sourate al-Qiyāmah, versets 25 à 34</li>
<li>19. Sourate al-Qiyāmah, versets 35 à 39</li>
<li>20. Sourate al-Insān, versets 1 à 6</li>
<li>21. Sourate al-Insān, versets 7 à 14</li>
<li>22. Sourate al-Insān, versets 15 à 22</li>
<li>23. Sourate al-Insān, versets 23 à 28</li>
<li>24. Sourate al-Insān, versets 29 à 31</li>
<li>25. Sourate al-Mursalāt, versets 1 à 15</li>
<li>26. Sourate al-Mursalāt, versets 16 à 28</li>
<li>27. Sourate al-Mursalāt, versets 29 à 40</li>
<li>28. Sourate al-Mursalāt, versets 41 à 50</li>
<li>29. Personnalités citées (aʿlām)</li>
<li>30. Sources et références</li>
</ul>
<h2>Compétences visées par l'enseignement du tafsīr en sixième année de l'enseignement primaire traditionnel</h2>
<p>L'enseignement du tafsīr vise à rendre l'apprenant(e) capable d'acquérir les compétences suivantes :</p>
<ul>
<li>assimiler le vocabulaire des sourates prescrites du Noble Coran ainsi que leurs contenus ;</li>
<li>prendre conscience de l'importance du dogme de l'unicité (tawḥīd) et de son effet dans le renforcement de la foi et la consolidation du lien avec Allah, Puissant et Majestueux ;</li>
<li>renforcer le lien de l'apprenant(e) avec le Livre d'Allah, le Très-Haut, et se conformer à ses prescriptions et à ses orientations ;</li>
<li>ancrer chez l'apprenant(e) les constantes doctrinales, légales et morales de l'islam ;</li>
<li>se parer des valeurs islamiques de tolérance et adhérer aux constantes de l'authentique identité marocaine, qui appelle à la tolérance et à la coexistence entre les membres de la société humaine.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    intro = d.get("intro") or {}
    if str(intro.get("docId")) != "14604":
        raise SystemExit("ERREUR: intro 14604 introuvable dans tafsir-6ep")
    intro["htmlFr"] = HTML_FR
    d["intro"] = intro
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — intro 14604 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
