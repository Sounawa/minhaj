#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12579 (tafsir-tanawi-2, présentation
du manuel « Tafsīr — al-Muḥarrar al-Wajīz d'Ibn ʿAṭiyya », Sūrat al-Isrāʾ).

Vérifications et décisions :
- Aucun verset cité dans cette leçon (page de présentation) — rien à restaurer.
- Le <dl>/<dd> CMS vide et le <p>&nbsp;</p> de tête : métadonnées de page,
  non rendues (convention des présentations déjà livrées : 13360 tafsir-1es,
  18643 ulum-quran-2es).
- L'h1 AR porte le titre complet du manuel ; convention 13360 : h1 = « Présentation
  du manuel », le titre complet est rendu dans le premier paragraphe.
- La table des matières imprimée (28 leçons, al-Isrāʾ 1→110) rendue FIDÈLEMENT :
  elle documente que le manuel papier couvre la sourate entière — alors que le
  livre CMS ne porte que les leçons 6 à 25 (versets 18-100) ; les leçons 1-5
  (versets 1-17) et 26-28 (versets 101-110) existent dans le corpus sous
  tafsir-5ep (pdfOnly) — écart à consigner au worklog.
- منكما (duel) rendu par « vous » (convention des présentations livrées).
- ملتهم = « confession » (convention corpus).
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>Présentation du manuel</h1>
<p>Le livre du <em>Tafsīr</em> de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), consacré à l’exégèse de la sourate al-Isrāʾ sur la base du commentaire du cadi Abū Muḥammad Ibn ʿAṭiyya intitulé <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> [« Le Concis établi, pour l’exégèse du Livre puissant »] — à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel.</p>
<p>C’est avec joie que nous plaçons entre vos mains le livre du <em>Tafsīr</em> de la deuxième année de l’enseignement secondaire traditionnel, consacré à l’exégèse de la sourate al-Isrāʾ sur la base du commentaire du cadi Abū Muḥammad Ibn ʿAṭiyya intitulé <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em>, en profitant des ouvrages-mères de l’exégèse faisant autorité — le tout dans un style qui vous rapproche le sens des versets et vous en facilite l’intelligence.</p>
<p>Cette sourate renferme les fondements de la doctrine (<em>ʿaqīda</em>) qui établissent l’unicité de Dieu, le Très-Haut, et la constatation de la prophétie et de la mission de l’Envoyé de Dieu — paix et bénédiction sur lui — au moyen des miracles et des signes manifestes qu’elle contient ; s’y ajoute l’affirmation du Jour dernier et des événements qui s’y rattachent — à l’image des sourates mecquoises.</p>
<p>En composant ce livre, nous avons observé la spécificité de l’enseignement traditionnel, tout en nous ouvrant aux nouveautés pédagogiques qui font de vous le pivot du processus éducatif : vous voici associés à la construction de la leçon et à la réalisation d’activités diverses, qui visent la réalisation de ses objectifs et stimulent chez vous l’apprentissage autonome.</p>
<p>Dans l’élaboration de ce livre, nous avons suivi une méthode qui vous rend proches les finalités du Noble Coran et les bienfaits qu’il recèle, à travers les leçons et les enseignements que renferme la sourate al-Isrāʾ — leçons et enseignements qui affermissent les principes de la doctrine droite, les mœurs vertueuses et les valeurs nobles dont le musulman doit se parer en sa vie comme dans ses rapports avec autrui, quels que soient leur sexe ou leur confession.</p>
<h2>Le livre du <em>Tafsīr</em> à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> (l’exégèse de la sourate al-Isrāʾ)</h2>
<ul>
<li>La méthodologie de la composition.</li>
<li>Comment j’utilise mon livre.</li>
<li>Les compétences de l’enseignement de la matière d’exégèse.</li>
<li>La répartition par périodes et par semaines.</li>
<li>1. La sourate al-Isrāʾ (verset 1).</li>
<li>2. La sourate al-Isrāʾ (versets 2 à 4).</li>
<li>3. La sourate al-Isrāʾ (versets 5 à 8).</li>
<li>4. La sourate al-Isrāʾ (versets 9 à 12).</li>
<li>5. La sourate al-Isrāʾ (versets 13 à 17).</li>
<li>6. La sourate al-Isrāʾ (versets 18 à 22).</li>
<li>7. La sourate al-Isrāʾ (versets 23 à 25).</li>
<li>8. La sourate al-Isrāʾ (versets 26 à 30).</li>
<li>9. La sourate al-Isrāʾ (versets 31 à 33).</li>
<li>10. La sourate al-Isrāʾ (versets 34 à 36).</li>
<li>11. La sourate al-Isrāʾ (versets 37 à 40).</li>
<li>12. La sourate al-Isrāʾ (versets 41 à 44).</li>
<li>13. La sourate al-Isrāʾ (versets 45 à 48).</li>
<li>14. La sourate al-Isrāʾ (versets 49 à 55).</li>
<li>15. La sourate al-Isrāʾ (versets 56 à 60).</li>
<li>16. La sourate al-Isrāʾ (versets 61 à 65).</li>
<li>17. La sourate al-Isrāʾ (versets 66 à 69).</li>
<li>18. La sourate al-Isrāʾ (versets 70 à 72).</li>
<li>19. La sourate al-Isrāʾ (versets 73 à 77).</li>
<li>20. La sourate al-Isrāʾ (versets 78 à 81).</li>
<li>21. La sourate al-Isrāʾ (versets 82 à 85).</li>
<li>22. La sourate al-Isrāʾ (versets 86 à 89).</li>
<li>23. La sourate al-Isrāʾ (versets 90 à 93).</li>
<li>24. La sourate al-Isrāʾ (versets 94 à 98).</li>
<li>25. La sourate al-Isrāʾ (versets 99 à 100).</li>
<li>26. La sourate al-Isrāʾ (versets 101 à 104).</li>
<li>27. La sourate al-Isrāʾ (versets 105 à 108).</li>
<li>28. La sourate al-Isrāʾ (versets 109 et 110).</li>
<li>L’index des figures citées (<em>aʿlām</em>).</li>
<li>Les sources et références.</li>
<li>La couverture du livre.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12579":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12579 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12579 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
