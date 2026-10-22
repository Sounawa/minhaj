#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 13992 (tafsir-5ep, Sourate al-Burūj 1-9, leçon 24).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : Burūj 85:1-9 ; préparation = 85:10-15 (leçon
  SUIVANTE 14005).
- Garble d'ouverture « سورة اليروج » = البروج (le h1 est correct) — rendu
  corrigé.
- TABLE شرح dégradée : gloses seules — termes restitués des versets (البروج /
  الشاهد / المشهود / قتل / الأخدود / شهود) ; gloses الشاهد=vendredi et
  المشهود=ʿArafa corroborées par le hadith Abū Mūsā al-Ashʿarī [Sunan
  al-Bayhaqī, kitāb al-jumua] conservé avec référence.
- Les 12 بروج énumérés (Bélier…Poissons) conservés intégralement.
- Récit al-Rabīʿ ibn Anas [Ṭabarī Jāmiʿ al-bayān 24/276] conservé + renvoi
  « l'histoire est détaillée dans le Ṣaḥīḥ de Muslim ».
- Grammaire : jawāb du serment élidé, taqdīr « laqad » ; النار بدل اشتمال
  من الأخدود ; gloss fragmentaire de v7 (« بالله… من تعذيبهم ») rendu avec
  minimal bracket [aux croyants] (fragments OCR).
- عزيز = dans Son royaume / حميد = le loué (gloses Jalālayn exactes).
- Istithmār : Muṣannaf Ibn Abī Shayba (kitāb al-zuhd) conservé avec sa
  chaîne Abū Usāma ← ʿAwf ← al-Ḥasan.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Burūj — le Tafsīr al-Jalālayn des versets 1 à 9</h1>
<p>Leçon de tafsīr de la sourate al-Burūj (versets 1 à 9) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 24.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître les principaux événements de l'histoire des gens de la fosse (aṣḥāb al-ukhdūd).</li>
<li>Dégager des versets les principales leçons et exhortations.</li>
<li>Incarner la valeur de la patience, de la quête de la récompense divine (iḥtisāb) et de la constance sur la vérité.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>La sourate al-Burūj est mecquoise et compte vingt-deux versets ; elle vient après la sourate al-Inshiqāq, toutes deux traitant de la rétribution des croyants et des négateurs, et célébrant le Noble Coran. Elle renferme l'histoire des gens de la fosse, et ce qu'on en tire : la patience des croyants dans l'épreuve, leur quête de la récompense divine et leur constance sur la vérité.<br>
Quels sont les principaux événements de l'histoire des gens de la fosse ? Et comment cette histoire m'aide-t-elle à demeurer constant sur la vérité ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Par le ciel aux constellations, (1) par le jour promis, (2) par le témoin et le contemplé : (3) périssent les gens de la fosse, (4) au feu plein de combustible, (5) alors qu'ils sont assis autour, (6) témoins de ce qu'ils font aux croyants — (7) eux qui ne leur ont reproché que d'avoir cru en Allah, le Puissant, le Louangé, (8) qui détient la royauté des cieux et de la terre. Allah est témoin de toute chose. (9) » (al-Burūj, 1-9)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Table imprimée dégradée : seules les gloses ont survécu à la numérisation ; les termes ont été restitués d'après les versets.]</p>
<ul>
<li>al-burūj (les constellations) : les astres.</li>
<li>al-shāhid (le témoin) : le vendredi.</li>
<li>al-mashhūd (le contemplé) : le jour de ʿArafa.</li>
<li>qutila (périssent) : soient maudits.</li>
<li>al-ukhdūd (la fosse) : le sillon creusé dans la terre.</li>
<li>shuhūd (témoins) : présents.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>Quelle est l'histoire que renferment les versets ?</li>
<li>Quel est l'objet du serment dans les versets ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : l'histoire des gens de la fosse</h3>
<p>D'après al-Rabīʿ ibn Anas — qu'Allah l'agrée — : « Les gens de la fosse étaient des croyants qui s'étaient retirés des gens durant l'interrègne (fatra). Un tyran parmi les idolâtres leur envoya [un émissaire] et leur proposa d'entrer dans sa religion ; ils refusèrent. Il creusa alors une fosse, y alluma un feu, puis leur donna le choix entre entrer dans sa religion et y être jetés. Ils choisirent d'être jetés au feu plutôt que de revenir de leur religion. On les y jeta ; et Allah sauva les croyants qu'on y avait jetés de la brûlure, en retirant leurs âmes avant que le feu ne les touchât ; et le feu s'échappa vers ceux qui se tenaient au bord de la fosse, parmi les négateurs, et les brûla. » [Jāmiʿ al-bayān, d'Ibn Ǧarīr al-Ṭabarī : 24/276] — et l'histoire est rapportée en détail dans le Ṣaḥīḥ de Muslim.</p>
<h3>Deuxièmement : la rétribution des gens de la fosse</h3>
<p>Le Très-Haut a dit :</p>
<p>« Par le ciel aux constellations, »</p>
<p>c'est-à-dire : Je jure par le ciel aux constellations (burūj) — et les burūj sont au nombre de douze : le Bélier, le Taureau, les Gémeaux, le Cancer, le Lion, la Vierge, la Balance, le Scorpion, le Sagittaire, le Capricorne, le Verseau et les Poissons.</p>
<p>« par le jour promis, »</p>
<p>— c'est le Jour de la Résurrection.</p>
<p>« par le témoin »</p>
<p>— le vendredi ;</p>
<p>« et le contemplé : »</p>
<p>— le jour de ʿArafa. Ainsi les trois ont-ils été interprétés dans le hadith : le premier est promis, le second est témoin par les œuvres qui y sont accomplies, et le troisième, les gens et les anges le contemplent. Abū Mūsā al-Ashʿarī — qu'Allah l'agrée — rapporte que le Prophète — paix et bénédiction sur lui — a dit : « Le jour promis est le Jour de la Résurrection ; le témoin, le vendredi ; le contemplé, le jour de ʿArafa ; et le vendredi est la réserve qu'Allah nous a destinée. » [Sunan al-Bayhaqī : Livre du vendredi]</p>
<p>Et la réponse du serment — son début est élidée, sa teneur estimée : « certes (laqad) » — est ce qui est estimé dans la parole du Très-Haut :</p>
<p>« périssent les gens de la fosse, »</p>
<p>c'est-à-dire : certes, les gens de la fosse ont péri — c'est-à-dire : ont été maudits. Et la parole du Très-Haut :</p>
<p>« au feu plein de combustible, »</p>
<p>c'est-à-dire : ce dont le feu est alimenté — c'est un complément d'inclusion (badal ishtimāl) de « la fosse ».</p>
<p>« alors qu'ils sont assis autour, »</p>
<p>c'est-à-dire : autour d'elle, au flanc de la fosse, assis sur des sièges.</p>
<p>« témoins de ce qu'ils font aux croyants — »</p>
<p>c'est-à-dire : du supplice qu'ils infligeaient [aux croyants] en les précipitant dans le feu, s'ils ne revenaient pas de leur foi.</p>
<p>« témoins » (shuhūd)</p>
<p>c'est-à-dire : présents. Et la parole du Très-Haut :</p>
<p>« eux qui ne leur ont reproché que d'avoir cru en Allah, le Puissant, le Louangé, »</p>
<p>« le Puissant » : dans Son royaume ; « le Louangé » : le loué.</p>
<p>« qui détient la royauté des cieux et de la terre. Allah est témoin de toute chose. »</p>
<p>— ce que les négateurs ont reproché aux croyants n'est rien d'autre que leur foi.</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>L'histoire des gens de la fosse rapportée dans ces versets oriente vers un ensemble de finalités éducatives, dont les plus importantes :</p>
<ul>
<li>l'épreuve (ibtilāʾ) est une loi d'Allah, Puissant et Majestueux, à laquelle les croyants sont exposés en tout temps ;</li>
<li>l'affermissement du cœur du Prophète — paix et bénédiction sur lui — et des croyants dans l'islam, par considération du secours d'Allah ;</li>
<li>la victoire véritable est le triomphe des principes et la constance sur eux.</li>
</ul>
<h2>L'évaluation</h2>
<ul>
<li>Quels sont les principaux événements de l'histoire des gens de la fosse ?</li>
<li>Quelle est la réponse au serment dans Sa parole : « Par le ciel aux constellations, par le jour promis, par le témoin et le contemplé » (al-Burūj, 1-3) — et ce qui la suit ?</li>
<li>Quelles sont les principales leçons à tirer de l'histoire des gens de la fosse ?</li>
</ul>
<h3>L'enrichissement (istithmār)</h3>
<p>D'après Abū Usāma, d'après ʿAwf, d'après al-Ḥasan : « Lorsque le Messager d'Allah — paix et bénédiction sur lui — mentionnait les gens de la fosse, il demandait refuge auprès d'Allah contre la rigueur de l'épreuve. »</p>
<p>[Muṣannaf Ibn Abī Shayba, Livre du renoncement (zuhd), chapitre de ce qui est rapporté de notre Prophète — paix et bénédiction sur lui — au sujet du renoncement]</p>
<ol>
<li>Pourquoi le Prophète — paix et bénédiction sur lui — demande-t-il refuge auprès d'Allah contre la rigueur de l'épreuve ?</li>
<li>Je passe en revue certaines épreuves subies par les musulmans aux débuts de l'islam.</li>
</ol>
<h2>La préparation préalable</h2>
<p>Je lis les versets 10 à 16 de la sourate al-Burūj et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Ceux qui ont éprouvé les croyants et les croyantes, puis ne se sont pas repentis : à eux le châtiment de la Géhenne, et le châtiment de la brûlure » (al-Burūj, 10) ;</p>
<p>« Ceux qui croient et accomplissent les œuvres bonnes ont des jardins sous lesquels coulent les ruisseaux : tel est l'immense succès » (al-Burūj, 11) ;</p>
<p>« Oui, la rigueur de ton Seigneur est terrible » (al-Burūj, 12) ;</p>
<p>« et c'est Lui le Pardonneur, le Tout-Affectueux » (al-Burūj, 14) ;</p>
<p>« le Maître du Trône, le Glorieux » (al-Burūj, 15).</p>
<p>[Expressions restituées d'après les versets 10 à 16 de la sourate al-Burūj (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>J'extrais des versets ce qui indique Sa puissance, glorifié soit-Il, à se venger des injustes.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13992":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13992 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13992 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
