#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : intro 11509 (fiqh-tanawi-1, Présentation du manuel).

Dernier doc LLM → 0 LLM restant au registre.

Vérifications :
- h1 enrichi sur le modèle des intros main (fiqh-6ep / tafsir-5ep) : « Le
  fiqh — le Mukhtaṣar du shaykh Khalīl avec le commentaire d'al-Dardīr et la
  ḥāshiya d'al-Dasūqī : première année… » (h1 source : double-point parasite
  « كتاب : الفقه… » corrigé).
- Sommaire numéroté (28 leçons + aʿlām + sources = 30) avec translittérations
  malikites exactes : bayʿ, ǧuzāf, ribā, muzābana, kāliʾ, ʿurbūn, ʿīna,
  khiyār al-sharṭ, tadlīs, ghalla ; « (suite) » pour تابع.
- FIX vs baseline : « la sensibilité juridique » → « l'habitus juridique
  (malaka fiqhiyya) » ; « religion bien guidée » → « religion pure »
  (al-ḥanīf) ; « arêtes » techniques du TOC traduites (la baseline coupait).
- Compétences : 7 items adjectivés (متمكنا/مستوعبا/قادرا) rendus par des
  participes, « il est attendu… que l'apprenant(e) soit » (يتوقع في نهاية
  السنة الدراسية).
- Injection : intro (d['intro']), pas une leçon — code dédié.
"""

import json

BOOK = "/home/z/my-project/content/books/fiqh-tanawi-1.json"

HTML_FR = """<h1>Le fiqh — le Mukhtaṣar du shaykh Khalīl avec le commentaire d'al-Dardīr et la ḥāshiya d'al-Dasūqī : première année de l'enseignement secondaire traditionnel (ʿatīq)</h1>
<p>Tandis que nous louons Allah, le Très-Haut, de nous avoir accordé d'élaborer le livre de fiqh de la première année de l'enseignement secondaire traditionnel (ʿatīq), c'est avec plaisir et joie que nous le mettons entre vos mains — en vue de consolider vos acquis antérieurs et d'ajouter des acquisitions nouvelles à votre capital cognitif, selon une méthodologie qui vise à unir le savoir à l'œuvre, la formation à l'application, et la compréhension à l'incorporation qui mène à l'engagement.</p>
<p>Ce livre est un moyen d'enseignement et un auxiliaire didactique : nous avons, en sa préparation, tenu compte du niveau intellectuel et cognitif de l'apprenant à cette étape, selon une approche pédagogique qui rend aisé pour vous le bénéfice de ses contenus, vous assiste dans votre formation, et vous stimule vers la réflexion, la recherche et l'apprentissage autonome.</p>
<p>Pour son élaboration, nous nous sommes appuyés sur l'un des livres de référence du fiqh malikite : le Mukhtaṣar du shaykh Khalīl — texte puissant dans sa langue, riche de ses concepts, qui exige présence d'esprit, force de pensée et application à l'étude avec les condisciples ; d'autant que le programme de cette année comprend des leçons sur les transactions financières, ce que nos jurisconsultes nomment les ventes (bayʿ). C'est un fiqh subtil en ses terminologies et ses questions, lié en ses affaires au vécu réel de l'homme ; c'est pourquoi nous nous sommes fondés, pour l'approche de ses contenus et l'analyse de ses sens, sur le commentaire d'al-Dardīr et la ḥāshiya d'al-Dasūqī sur le matn du Mukhtaṣar de Khalīl.</p>
<p>Nous avons également pris en compte, en élaborant ce livre, tout ce qui touche aux principes de notre religion pure (al-ḥanīfiyya) : l'affirmation des valeurs de fidélité (amāna), de justice, d'excellence (iḥsān) et de dignité, des valeurs de citoyenneté sincère, et des valeurs des droits de l'homme universellement reconnues.</p>
<p>On espère que ce livre, par le savoir jurisprudentiel qu'il porte, sera pour vous un moteur vers l'apprentissage autonome, un stimulant vers la recherche dans les sources jurisprudentielles faisant autorité — afin qu'il vous soit donné, à cette étape, de bâtir l'habitus juridique (malaka fiqhiyya) qui vous rendra aptes à poursuivre vos études dans les cycles suivants, avec aisance et facilité, et avec un empressement et un désir toujours renouvelés dans la quête du savoir.</p>
<h3>Sommaire des leçons</h3>
<ul>
<li>1. La vente (bayʿ) : ses piliers, ses conditions et ses divisions</li>
<li>2. Les conditions de la vente et leurs exigences (suite)</li>
<li>3. Les formes que frappent l'interdit et le permis</li>
<li>4. Les règles de la vente au forfait (ǧuzāf)</li>
<li>5. Les règles de la vente sur vision, sur programme et sur description</li>
<li>6. Les règles de l'usure (ribā) dans les monnaies et les aliments</li>
<li>7. La réunion de la vente et du change</li>
<li>8. L'effet du vice dans le change</li>
<li>9. Les règles de la vente du plaqué (muḥallā), de l'échange et de la vente au poids (murāṭala)</li>
<li>10. Les règles de l'acquittement de la dette</li>
<li>11. L'usure (ribā) dans les aliments</li>
<li>12. L'usure dans les accessoires des aliments</li>
<li>13. Les ventes viciées</li>
<li>14. Les ventes viciées (suite)</li>
<li>15. La vente en bloc (muzābana), la vente à terme (kāliʾ) et la vente avec arrhes (ʿurbūn)</li>
<li>16. Les ventes interdites</li>
<li>17. Les effets de la vente viciée et ses causes de déchéance</li>
<li>18. Les ventes à terme : leurs conditions, leurs formes et leur statut</li>
<li>19. Les ventes à terme : leurs formes et leurs règles (suite)</li>
<li>20. Les règles de la vente ʿīna</li>
<li>21. Les règles de la vente à option contractuelle (khiyār al-sharṭ)</li>
<li>22. Les annulatifs de l'option et ses empêchements</li>
<li>23. La propriété, la garantie et les modalités de choix dans l'option</li>
<li>24. Les causes de rétractation de la vente à option</li>
<li>25. Les empêchements de la rétractation par option</li>
<li>26. La dissimulation (tadlīs) dans la vente à option</li>
<li>27. Les règles de la restitution dans la vente</li>
<li>28. Les règles du fruit (ghalla) et de la garantie après restitution de l'objet vendu</li>
<li>29. Personnalités citées (aʿlām)</li>
<li>30. Sources et références</li>
</ul>
<h2>Compétences visées par l'enseignement du fiqh en première année de l'enseignement secondaire traditionnel</h2>
<p>Il est attendu, au terme de l'année scolaire, que l'apprenant(e) soit :</p>
<ul>
<li>1. capable de mémoriser à loisir le matn prescrit ;</li>
<li>2. capable de comprendre les termes du matn, la portée de ses expressions et ses terminologies ;</li>
<li>3. imprégné(e) des concepts et des sens contenus dans le matn ;</li>
<li>4. à même de manier les commentaires du matn, qui aident à décoder ses formules et éclaircir les visées de son auteur ;</li>
<li>5. imprégné(e) des règles légales universelles et des règles jurisprudentielles particulières liées aux ventes ;</li>
<li>6. détenteur d'un nombre de règles et de critères jurisprudentiels qui le rendent apte à acquérir l'habitus juridique (malaka) en droit des biens ;</li>
<li>7. capable de répondre aux questions nouvelles (nawāzil) soumises à la discussion et à l'analyse par une réponse jurisprudentielle.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    intro = d.get("intro") or {}
    if str(intro.get("docId")) != "11509":
        raise SystemExit("ERREUR: intro 11509 introuvable dans fiqh-tanawi-1")
    intro["htmlFr"] = HTML_FR
    d["intro"] = intro
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — intro 11509 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
