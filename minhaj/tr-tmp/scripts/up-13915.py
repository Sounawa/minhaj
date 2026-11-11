#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 13915 (tafsir-5ep, Sourate al-Muṭaffifīn 7-17, leçon 18).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : Muṭaffifīn 83:7-17 ; citation du hadith
  istithmār = 83:14 ; préparation = 83:18-27 (leçon SUIVANTE 13920).
- TABLE شرح dégradée : gloses seules — termes restitués des versets
  (كتاب الفجار / سجين / مرقوم / معت / أساطير الأولين / ران / لصالوا الجحيم).
- Harmonisation 13907 (leçon précédente, même sourate) : « le livre des
  libertins est certes dans le Sijjīn », « un livre inscrit », « Malheur, ce
  jour-là, aux négateurs », « ne le traite de mensonge que tout transgresseur,
  pécheur », « Des contes des anciens ! », « a couvert leurs cœurs ».
- Ibn Kathīr [Tafsīr 8/346] sur sijjīn/مرقوم conservé ; hadith Tirmidhī
  (Abū Hurayra, rān) restauré avec sa référence de chapitre.
- Note grammaticale OCR « وهو بدل من المكذبين أو بيان له » : le relatif
  « qui traitent de mensonge » est badal/bayān de « les négateurs » (v10-11).
- Morphologie أساطير : pluriel d'usṭūra (ḍamm) ou d'iṣṭāra (kasr) conservée.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Muṭaffifīn — le Tafsīr al-Jalālayn des versets 7 à 17</h1>
<p>Leçon de tafsīr de la sourate al-Muṭaffifīn (versets 7 à 17) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 18.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître la rétribution des négateurs du Jour de la Rétribution.</li>
<li>Dégager des versets les causes du déni du Jour de la Rétribution par les négateurs.</li>
<li>Affermir ma foi au Livre d'Allah, véridique en tout ce qu'il apporte comme doctrines et règles.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>Après qu'Allah, le Très-Haut, a rappelé que le fait des fraudeurs est de nier ce qu'Il a promis à ce sujet — la présentation [des œuvres] et le compte —, Il leur a ordonné de s'abstenir de ce en quoi ils sont, et a mentionné que les libertins ont un livre préparé, où sont dénombrées toutes leurs œuvres ; de même qu'Il a préparé la ruine aux négateurs du jour de la rétribution, qui jettent le doute sur les versets du Noble Coran en disant : « Ce ne sont que des contes des anciens. »<br>
Comment les œuvres des libertins leur seront-elles présentées dans l'au-delà ? Et quelle est la rétribution des négateurs du Jour de la Rétribution ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Non ! Le livre des libertins est certes dans le Sijjīn. (7) Et qui te dira ce qu'est le Sijjīn ? (8) Un livre inscrit, (9) Malheur, ce jour-là, aux négateurs, (10) qui traitent de mensonge le Jour de la Rétribution : (11) ne le traite de mensonge que tout transgresseur, pécheur, (12) qui, lorsque Nos versets lui sont récités, dit : "Des contes des anciens !" (13) Non ! Mais ce qu'ils ont acquis a couvert leurs cœurs. (14) Non ! Ils seront, ce jour-là, voilés de leur Seigneur ; (15) puis ils seront, certes, introduits dans la Fournaise ; (16) puis il sera dit : "Voici ce que vous traitiez de mensonge !" (17) » (al-Muṭaffifīn, 7-17)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Table imprimée dégradée : seules les gloses ont survécu à la numérisation ; les termes ont été restitués d'après les versets.]</p>
<ul>
<li>kitāb al-fujjār (le livre des libertins) : le livre des œuvres des négateurs.</li>
<li>Sijjīn : un livre qui rassemble les œuvres des démons et des négateurs.</li>
<li>marqūm (inscrit) : scellé.</li>
<li>muʿtad (transgresseur) : qui outrepasse la limite.</li>
<li>asāṭīr al-awwalīn (contes des anciens) : les récits tracés jadis.</li>
<li>rāna (a couvert) : a vaincu.</li>
<li>la-ṣālū al-jahīm (introduits dans la Fournaise) : les entrants dans le feu incandescent.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>Comment les œuvres des libertins leur seront-elles présentées dans l'au-delà ?</li>
<li>Pour qui Allah a-t-Il préparé la rétribution mentionnée dans les versets ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la présentation des œuvres des libertins dans le Sijjīn</h3>
<p>Le contexte demeure dans l'avertissement contre l'injustice et la contravention aux ordres d'Allah, Puissant et Majestueux. Le Très-Haut a dit :</p>
<p>« Non ! Le livre des libertins est certes dans le Sijjīn. »</p>
<p>« Non ! » (kalā) : certes — il n'en est pas comme le prétendent ceux-ci, qui nient la résurrection et la rétribution.</p>
<p>« le livre des libertins »</p>
<p>c'est-à-dire : le livre des œuvres des négateurs.</p>
<p>« est certes dans le Sijjīn »</p>
<p>— c'est un livre qui rassemble les œuvres des démons et des négateurs.</p>
<p>« Et qui te dira ce qu'est le Sijjīn ? »</p>
<p>— une interrogation pour dramatiser (tahwīl), c'est-à-dire : et qu'est-ce qui t'a informé de ce qu'est le Sijjīn ? Et la parole du Très-Haut :</p>
<p>« Un livre inscrit »</p>
<p>— un exposé du livre des libertins, c'est-à-dire : qu'il est tracé et scellé. Ibn Kathīr a dit : « Sijjīn est dérivé de la prison (sijn), qui est l'étroitesse ; et comme la destination des libertins est la Géhenne, qui est le plus bas des bas et qui réunit l'étroitesse et la bassesse, le Très-Haut a informé que c'est un livre inscrit (marqūm), c'est-à-dire : écrit, achevé, auquel personne n'est ajouté et duquel personne n'est retranché. » [Tafsīr al-Qurʾān al-ʿaẓīm (L'Exégèse du noble Coran), d'Ibn Kathīr : 8/346]</p>
<h3>Deuxièmement : la rétribution des négateurs du Jour de la Rétribution</h3>
<p>Après l'exposé sur les feuillets des libertins, ces versets sont venus exposer la rétribution des négateurs de la résurrection et du renouvellement [de la vie]. Le Très-Haut a dit :</p>
<p>« Malheur, ce jour-là, aux négateurs, »</p>
<p>c'est-à-dire : la ruine, l'humiliation et la dureté du châtiment, en ce jour, pour les négateurs du Jour de la Rétribution ;</p>
<p>« qui traitent de mensonge le Jour de la Rétribution »</p>
<p>— le jour de la rétribution ; et [« qui traitent de mensonge »] est une substitution (badal) de « les négateurs », ou un explicatif (bayān) ;</p>
<p>« ne le traite de mensonge que tout transgresseur, pécheur »</p>
<p>c'est-à-dire : ne traite de mensonge ce jour-là qu'un outrepasseur des limites, excessif dans la perpétration des fautes.</p>
<p>Puis Allah, le Très-Haut, mentionna certaines caractéristiques des négateurs du Jour de la Rétribution, et le Glorifié dit :</p>
<p>« qui, lorsque Nos versets lui sont récités, dit : "Des contes des anciens !" »</p>
<p>c'est-à-dire : lorsque les versets du Noble Coran sont récités à ce négateur,</p>
<p>il dit : « Des contes des anciens ! »</p>
<p>— c'est-à-dire : des récits tracés jadis ; pluriel d'usṭūra (avec ḍamma) ou d'iṣṭāra (avec kasra).</p>
<p>Puis Allah, glorifié soit-Il, exposa ce qui les a portés à nier le Coran, et leur rétribution pour cela, et dit :</p>
<p>« Non ! Mais ce qu'ils ont acquis a couvert leurs cœurs. »</p>
<p>— « Non ! » (kalā) : une dissuasion et un blâme de leur parole : « Le Noble Coran [n'est que] des contes des anciens » ;</p>
<p>« a couvert leurs cœurs »</p>
<p>c'est-à-dire : a vaincu leurs cœurs ce qu'ils acquéraient comme désobéissances, l'a enveloppé et l'a voilé de la foi — tel la rouille.</p>
<p>« Non ! Ils seront, ce jour-là, voilés de leur Seigneur ; »</p>
<p>c'est-à-dire : certes, ces libertins seront voilés, au Jour de la Résurrection, de leur Seigneur, et ne Le verront pas ;</p>
<p>« puis ils seront, certes, introduits dans la Fournaise ; »</p>
<p>c'est-à-dire : les entrants dans le feu incandescent ;</p>
<p>« puis il sera dit : "Voici ce que vous traitiez de mensonge !" »</p>
<p>c'est-à-dire : puis il leur sera dit : voici le châtiment que vous traitiez de mensonge en ce bas monde.</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont les plus importantes :</p>
<ul>
<li>établir la preuve contre les libertins par la conservation de leurs œuvres et leur présentation au Jour de la Résurrection ;</li>
<li>parmi les causes du déni du Jour de la Rétribution par les libertins : l'abondance des fautes et des désobéissances ;</li>
<li>l'exposé de la rétribution des libertins au Jour de la Résurrection ;</li>
<li>l'invitation à purifier les âmes, à les porter vers les œuvres bonnes et à éviter les blâmables.</li>
</ul>
<h2>L'évaluation</h2>
<ol>
<li>Comment les œuvres des libertins sont-elles conservées ?</li>
<li>Quelles sont les caractéristiques des négateurs du Jour de la Rétribution auxquelles le Noble Coran a fait allusion ?</li>
<li>Quelle est la rétribution qu'Allah, Puissant et Majestueux, a préparée aux négateurs du Jour de la Rétribution ?</li>
</ol>
<h3>L'enrichissement (istithmār)</h3>
<p>D'après Abū Hurayra — qu'Allah l'agrée —, le Messager d'Allah — paix et bénédiction sur lui — a dit : « Lorsque le serviteur commet une faute, un point noir s'inscrit sur son cœur ; s'il s'en abstient, demande pardon et se repent, son cœur est poli ; mais s'il y revient, le point y est accru jusqu'à couvrir son cœur — et c'est là le voile (rān) qu'Allah a mentionné :</p>
<p>« Non ! Mais ce qu'ils ont acquis a couvert leurs cœurs. » (al-Muṭaffifīn, 14)</p>
<p>[Sunan al-Tirmidhī, Livre de l'exégèse, chapitre « et de la sourate "Malheur aux fraudeurs" »]</p>
<p>Quelles sont les causes de l'enfermement des cœurs et de leur voilement à l'égard de la foi ?<br>
Comment soigner les cœurs endurcis, insouciants de l'évocation d'Allah ?</p>
<h2>La préparation préalable</h2>
<p>Je lis les versets 18 à 28 de la sourate al-Muṭaffifīn et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Non ! Le livre des bons est certes dans lʿIlliyyūn » (al-Muṭaffifīn, 18) ;</p>
<p>« Et qui te dira ce qu'est lʿIlliyyūn ? » (al-Muṭaffifīn, 19) ;</p>
<p>« un livre inscrit » (al-Muṭaffifīn, 20) ;</p>
<p>« que contemplent les rapprochés » (al-Muṭaffifīn, 21) ;</p>
<p>« Ils seront abreuvés d'un nectar cacheté » (al-Muṭaffifīn, 25) ;</p>
<p>« et son mélange est de Tasnīm » (al-Muṭaffifīn, 27).</p>
<p>[Expressions restituées d'après les versets 18 à 28 de la sourate al-Muṭaffifīn (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>J'énumère certains des biens qu'Allah, le Très-Haut, a préparés aux bons dans le Paradis.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13915":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13915 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13915 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
