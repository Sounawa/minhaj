#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 13920 (tafsir-5ep, Sourate al-Muṭaffifīn 18-28, leçon 19).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : Muṭaffifīn 83:18-28 ; comparaison ʿAbasa 80:38-39
  (le span imprimé « عبس 39-38 » a l'ordre inversé — corrigé en 38-39) ;
  citation introductive Rāzī = 83:18 ; préparation = 83:29-36 (leçon SUIVANTE
  13931, déjà main — rendu des versets harmonisé sur elle).
- TABLE شرح dégradée : gloses seules — termes restitués des versets (كتاب
  الأبرار / عليين / على الأرائك / نضرة النعيم / رحيق / مزاجه).
- Ibn Ǧuzayy [Tashīl 2/462] sur la dérivation d'ʿIlliyyūn conservé ; Rāzī
  [Mafātīḥ 31/90] (hauteur/lumière = félicité vs bassesse/ténèbres = misère)
  conservé avec référence.
- Harmonisation 13915 (leçon précédente) : « le livre des bons est certes dans
  lʿIlliyyūn », « un livre inscrit », « que contemplent les rapprochés »,
  « Ils seront abreuvés d'un nectar cacheté », « Son mélange est de Tasnīm » ;
  harmonisation 13931 (leçon suivante) : « accoudés sur des lits »,
  « Ceux qui commettaient des crimes riaient de ceux qui avaient cru », etc.
- Note grammaticale v28 conservée : « ʿaynan » à l'accusatif d'un verbe élidé
  estimé « amdaḥu » (je célèbre) ; double exégèse de « يشرب بها » (boit d'elle
  / se délecte).
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Muṭaffifīn — le Tafsīr al-Jalālayn des versets 18 à 28</h1>
<p>Leçon de tafsīr de la sourate al-Muṭaffifīn (versets 18 à 28) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 19.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître la rétribution des bons et ce qu'Allah leur a préparé dans l'au-delà.</li>
<li>Dégager des versets le domaine de la compétition véritable entre les gens.</li>
<li>Incarner dans ma vie les valeurs d'obéissance et d'adoration, pour être parmi les bons.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>Après qu'Allah, le Très-Haut, a mentionné l'état des fraudeurs et des libertins, et la rétribution qu'Il leur a préparée dans l'au-delà, Il l'a fait suivre de la mention de l'état des bons et de la félicité durable que le Glorifié leur a préparée au Paradis — conformément au style du Noble Coran, qui joint l'incitation et l'intimidation.<br>
Comment les œuvres des bons sont-elles conservées ? Et qu'Allah a-t-Il préparé pour eux au Paradis ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Non ! Le livre des bons est certes dans lʿIlliyyūn. (18) Et qui te dira ce qu'est lʿIlliyyūn ? (19) Un livre inscrit, (20) que contemplent les rapprochés. (21) Les bons seront, certes, dans un jardin de délice, (22) accoudés sur des lits, ils regardent. (23) Tu reconnaîtras sur leurs visages la fraîcheur du délice. (24) Ils seront abreuvés d'un nectar cacheté (25) dont le sceau est de musc — et en cela, que compétitionnent les compétiteurs ! (26) Son mélange est de Tasnīm, (27) une source dont boivent les rapprochés. (28) » (al-Muṭaffifīn, 18-28)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Table imprimée dégradée : seules les gloses ont survécu à la numérisation ; les termes ont été restitués d'après les versets.]</p>
<ul>
<li>kitāb al-abrār (le livre des bons) : le livre des œuvres des croyants sincères dans leur foi.</li>
<li>ʿIlliyyūn : un livre qui rassemble les œuvres de bien des anges et des croyants des deux pesanteurs (hommes et djinns).</li>
<li>ʿalā al-arāʾik (accoudés sur des lits) : sur des lits sous dais — la chambre parée de tissus et de rideaux.</li>
<li>naḍrat al-naʿīm (la fraîcheur du délice) : la splendeur de la jouissance et sa beauté.</li>
<li>raḥīq (un nectar) : un vin pur de toute souillure.</li>
<li>mizājuhu (son mélange) : ce avec quoi il est mêlé.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>Comment les œuvres des bons leur seront-elles présentées dans l'au-delà ?</li>
<li>Quel est le rang des bons dans l'au-delà ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : les œuvres des bons sont conservées dans lʿIlliyyūn</h3>
<p>Après qu'Allah, Puissant et Majestueux, a mentionné l'état des fraudeurs et des libertins, Il mentionne ici l'état des bons, et dit :</p>
<p>« Non ! Le livre des bons est certes dans lʿIlliyyūn. »</p>
<p>« Non ! » (kalā) : certes.</p>
<p>« le livre des bons »</p>
<p>c'est-à-dire : le livre des œuvres des croyants sincères dans leur foi.</p>
<p>« est certes dans lʿIlliyyūn »</p>
<p>Il est dit : c'est un livre qui rassemble les œuvres de bien des anges et des croyants des deux pesanteurs ; et il est dit : c'est un lieu du septième ciel, sous le Trône — « [ʿIlliyyūn] est dérivé de la hauteur (ʿuluww), parce qu'il est cause de l'élévation des degrés au Paradis, ou parce qu'il est élevé en un lieu haut » [al-Tashīl li-ʿulūm al-tanzīl (La Facilitation des sciences de la Révélation), d'Ibn Ǧuzayy : 2/462].</p>
<p>« Et qui te dira ce qu'est lʿIlliyyūn ? »</p>
<p>c'est-à-dire : et qu'est-ce qui t'a informé de ce qu'est le livre de lʿIlliyyūn ?</p>
<p>« Un livre inscrit »</p>
<p>c'est-à-dire : scellé.</p>
<p>« que contemplent les rapprochés »</p>
<p>c'est-à-dire : d'entre les anges — ils le gardent et attestent de ce qu'il contient.</p>
<h3>Deuxièmement : la magnification du rang des bons et l'exposé de leur rétribution au Paradis</h3>
<p>Après qu'Allah, Puissant et Majestueux, a magnifié le livre des bons dans le verset précédent, Il expose dans ces versets leur rang, et dit :</p>
<p>« Les bons seront, certes, dans un jardin de délice »</p>
<p>c'est-à-dire : les pieux, obéissants à leur Seigneur, seront certes dans un jardin où ils jouiront de ce qu'il renferme.</p>
<p>Puis le Glorifié décrivit ce délice par trois choses. La première, Sa parole :</p>
<p>« accoudés sur des lits, ils regardent »</p>
<p>c'est-à-dire : sur les lits, dans les dais (ḥijāl) — la chambre parée de tissus et de rideaux —, regardant la félicité qui leur a été donnée. La deuxième, Sa parole, le Très-Haut :</p>
<p>« Tu reconnaîtras sur leurs visages la fraîcheur du délice »</p>
<p>c'est-à-dire : la splendeur de la jouissance et sa beauté — comme le Glorifié a dit :</p>
<p>« Des visages, ce jour-là, rayonnants, (38) riant, réjouis. (39) » (ʿAbasa, 38-39)</p>
<p>La troisième, Sa parole :</p>
<p>« Ils seront abreuvés d'un nectar cacheté »</p>
<p>c'est-à-dire : ils seront abreuvés d'un vin licite, non enivrant, pur de toute souillure, scellé sur son récipient — nul n'en rompt le sceau sinon les bons.</p>
<p>« dont le sceau est de musc »</p>
<p>c'est-à-dire : la dernière gorgée en exhale le parfum du musc.</p>
<p>« — et en cela, que compétitionnent les compétiteurs ! »</p>
<p>c'est-à-dire : en cela, que les coureurs aspirent, en s'empressant vers l'obéissance d'Allah.</p>
<p>« Son mélange est de Tasnīm »</p>
<p>c'est-à-dire : ce avec quoi il est mêlé — expliqué par Sa parole :</p>
<p>« une source dont boivent les rapprochés »</p>
<p>— il est dit que le sens en est : [les rapprochés] boivent d'elle ; et il est dit : [le verbe] a reçu le sens de « se délecter » (yaltafu) ; et Sa parole « ʿaynan » (une source) est à l'accusatif sous l'effet d'un verbe élidé, dont l'estimation est « amdaḥu » (je célèbre).</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont les plus importantes :</p>
<ol>
<li>la bonne nouvelle donnée aux croyants de la conservation de leurs œuvres en un livre de rang élevé auprès d'Allah, glorifié soit-Il ;</li>
<li>l'incitation des croyants à l'œuvre juste, pour obtenir ce qu'Allah a préparé de félicité durable aux gens du Paradis ;</li>
<li>l'exhortation par Allah, le Très-Haut, à la compétition dans les œuvres bonnes et à l'application dans les obéissances.</li>
</ol>
<h2>L'évaluation</h2>
<ol>
<li>Où sont conservées les œuvres des bons ?</li>
<li>Qu'Allah, le Très-Haut, a-t-Il préparé aux bons dans le Paradis ?</li>
<li>Que me faut-il faire en cette vie pour être parmi les bons ?</li>
</ol>
<h3>L'enrichissement (istithmār)</h3>
<p>Fakhr al-Dīn al-Rāzī — qu'Allah lui fasse miséricorde — a dit, en commentant la parole d'Allah, le Très-Haut :</p>
<p>« Non ! Le livre des bons est certes dans lʿIlliyyūn. » (al-Muṭaffifīn, 18)</p>
<p>« Sache que l'essentiel dans l'interprétation de ce verset est ce que nous avons exposé : la hauteur, l'espace, la lumière et la pureté sont des marques de la félicité ; la bassesse, l'étroitesse et les ténèbres sont des marques de la misère. Dès lors que le dessein du dépôt du livre des libertins au plus bas des bas, et dans le plus étroit des lieux, est l'humiliation des libertins et l'avilissement de leur rang, le dessein du dépôt du livre des bons au plus haut de lʿIlliyyūn, et du témoignage des anges en leur faveur, est leur magnification et l'exaltation de leur rang. » [Mafātīḥ al-ghayb (Les Clefs du mystère), de Fakhr al-Dīn al-Rāzī : 31/90]</p>
<ol>
<li>Je compare le rang du livre des libertins et la place du livre des bons à travers le texte.</li>
<li>Qu'est-ce qui indique l'exaltation du rang des bons ?</li>
</ol>
<h2>La préparation préalable</h2>
<p>Je lis les versets 29 à 36 de la sourate al-Muṭaffifīn et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Ceux qui commettaient des crimes riaient de ceux qui avaient cru » (al-Muṭaffifīn, 29) ;</p>
<p>« et lorsqu'ils passaient près d'eux, ils échangeaient des signes de l'œil et du sourcil » (al-Muṭaffifīn, 30) ;</p>
<p>« Et lorsqu'ils les voyaient, ils disaient : "Ceux-ci sont certes égarés" » (al-Muṭaffifīn, 32) ;</p>
<p>« Aujourd'hui, ceux qui ont cru riront des infidèles » (al-Muṭaffifīn, 34).</p>
<p>[Expressions restituées d'après les versets 29 à 36 de la sourate al-Muṭaffifīn (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>Je conclus des versets comment les criminels traitent les croyants en ce bas monde.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13920":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13920 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13920 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
