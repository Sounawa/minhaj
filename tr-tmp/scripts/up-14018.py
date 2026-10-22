#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 14018 (tafsir-5ep, Sourate al-Burūj 17-22, leçon 26).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : Burūj 85:12-16 (rappel des attributs, leçon
  précédente) ; 85:17-22 ; citation introductive Rāzī = 85:20 ; trois preuves
  internes du Rāzī = al-Fatḥ 48:21, al-Isrāʾ 17:60, Yūnus 10:22 (citations
  partielles, refs imprimées conservées) ; préparation = Ṭāriq 86:1-7 (leçon
  14042, déjà main — versets 1-7 harmonisés sur son rendu).
- Garble d'ouverture « سورة اليروج » = البروج (h1 correct) — corrigé.
- TABLE شرح dégradée : gloses seules — termes restitués des versets (ثمود /
  محيط / مجيد / محفوظ).
- Grammaire v17-18 : فرعون وثمود بدل من الجنود + استغني بذكر فرعون عن
  أتباعه — conservées.
- Glose de la Table (lawḥ) : dans l'air au-dessus du 7e ciel, gardée des
  démons et de toute altération, dimensions ciel-terre/Orient-Occident,
  perle blanche — attribuée à Ibn ʿAbbās, conservée intégralement.
- Rāzī [Mafātīḥ 31/116] : les 3 exégèses de l'« enveloppement » conservées
  (puissance/prise, imminence de la perte, science des œuvres).
- Harmonisation 13992/14005 (même sourate) : « le récit des armées »,
  « Mais ceux qui ont mécru », « Coran glorieux », « Table bien gardée ».
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Burūj — le Tafsīr al-Jalālayn des versets 17 à 22</h1>
<p>Leçon de tafsīr de la sourate al-Burūj (versets 17 à 22) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 26.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître certains récits de Pharaon et de Thamūd, et leur déni de leurs prophètes.</li>
<li>Dégager des versets la véracité du Noble Coran et sa majesté.</li>
<li>Tirer admonition de la puissance d'Allah envers ceux qui traitent de mensonge les prophètes et messagers d'Allah.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>Après que le Noble Coran a parlé de l'histoire des gens de la fosse, exposé leur état et décrit les crimes qu'ils perpetrèrent, il montre ici que l'état des négateurs envers tout prophète et ceux qui crurent en lui suit ce même mode : ils ne cessent de nuire aux croyants et de les prendre en inimitié ; et Allah n'a envoyé aucun prophète sans qu'il ne rencontrât de son peuple une part de nuisance.<br>
Quels sont les récits de Pharaon et de Thamūd ? Et comment Allah a-t-Il répondu aux négateurs du Noble Coran ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« T'est-il parvenu le récit des armées (17) — de Pharaon et de Thamūd —, (18) alors que ceux qui ont mécru persistent dans la dénégation (19) qu'Allah, de derrière eux, enveloppe. (20) Non ! C'est un Coran glorieux (21) dans une Table bien gardée. (22) » (al-Burūj, 17-22)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Table imprimée dégradée : seules les gloses ont survécu à la numérisation ; les termes ont été restitués d'après les versets.]</p>
<ul>
<li>Thamūd : une tribu arabe.</li>
<li>muḥīṭ (enveloppe) : capable sur eux.</li>
<li>majīd (glorieux) : immense.</li>
<li>maḥfūẓ (bien gardée) : préservée.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>Quelles sont les communautés dont Allah, Puissant et Majestueux, a rapporté les récits dans ces versets ?</li>
<li>Par quoi Allah, Puissant et Majestueux, a-t-Il répondu aux négateurs du Noble Coran ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : les récits de Pharaon et de Thamūd</h3>
<p>Après qu'Allah, Puissant et Majestueux, nous a informés de certains de Ses attributs indiquant Sa grandeur, en Sa parole :</p>
<p>« Oui, la rigueur de ton Seigneur est terrible : c'est Lui qui commence et recommence ; et c'est Lui le Pardonneur, le Tout-Affectueux, le Maître du Trône, le Glorieux, l'Effecteur de ce qu'Il veut » (al-Burūj, 12-16)</p>
<p>Il expose ici ce qu'Il fit de Pharaon et de Thamūd, et le Très-Haut dit :</p>
<p>« T'est-il parvenu le récit des armées »</p>
<p>c'est-à-dire : T'est-il parvenu, ô Muḥammad, le récit des armées (al-junūd)</p>
<p>« — de Pharaon et de Thamūd — »</p>
<p>— substitut (badal) de « les armées » ; et la mention de Pharaon a dispensé de [citer] ses suites.</p>
<p>Et leur récit est qu'Allah les anéantit à cause de leur mécréance — avertissement adressé à quiconque a mécru au Prophète — paix et bénédiction sur lui — et au Coran, pour qu'ils s'amendent. Puis le Très-Haut dit :</p>
<p>« alors que ceux qui ont mécru persistent dans la dénégation »</p>
<p>c'est-à-dire : dans la dénégation du Prophète — paix et bénédiction sur lui — et du Noble Coran ;</p>
<p>« qu'Allah, de derrière eux, enveloppe. »</p>
<p>c'est-à-dire : Il est, glorifié soit-Il, capable sur eux — nul ne les protège de Lui.</p>
<h3>Deuxièmement : la préservation du Coran par Allah contre toute altération</h3>
<p>Après avoir parlé des négateurs du Prophète — paix et bénédiction sur lui — et de ce qu'il a apporté, Allah leur répond en ce verset, en exposant que ce livre est préservé par le Seigneur des mondes. Le Très-Haut a dit :</p>
<p>« Non ! C'est un Coran glorieux »</p>
<p>« glorieux » (majīd) : c'est-à-dire : immense ;</p>
<p>« dans une Table bien gardée. »</p>
<p>— la Table (lawḥ) est dans l'air, au-dessus du septième ciel ; « bien gardée » (maḥfūẓ) : des démons et de l'altération d'aucune de ses parties. Sa longueur va du ciel à la terre, sa largeur de l'Orient à l'Occident, et elle est d'une perle blanche. C'est ce qu'a dit Ibn ʿAbbās — qu'Allah les agrée.</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont les plus importantes :</p>
<ul>
<li>la consolation du Prophète — paix et bénédiction sur lui — et des croyants par les récits des communautés antérieures ;</li>
<li>l'exposé de la puissance d'Allah, le Très-Haut, et de l'immensité de Son autorité ;</li>
<li>l'affirmation que le Noble Coran est préservé de la falsification, du changement et de l'altération ;</li>
<li>l'obligation de se conformer aux règles du Noble Coran, de déclarer licite son licite et illicite son illicite.</li>
</ul>
<h2>L'évaluation</h2>
<ol>
<li>Pourquoi Allah a-t-Il rappelé à Son Prophète — paix et bénédiction sur lui — le récit de Pharaon et de Thamūd ?</li>
<li>Comment Allah a-t-Il répondu aux associateurs et à leurs imputations contre le Noble Coran ?</li>
<li>Comment Allah, Puissant et Majestueux, a-t-Il préservé Son livre puissant ?</li>
</ol>
<h3>L'enrichissement (istithmār)</h3>
<p>Fakhr al-Dīn al-Rāzī — qu'Allah lui fasse miséricorde — a dit, sur Sa parole, le Très-Haut :</p>
<p>« qu'Allah, de derrière eux, enveloppe » (al-Burūj, 20)</p>
<p>« Il y a en cela plusieurs aspects. Le premier : le sens visé est la description de Sa puissance sur eux, et [le fait qu']ils sont dans Sa poigne et Son domaine — comme l'encerclé que l'on ceint par derrière, dont la voie est barrée et qui ne trouve point d'issue. Allah, le Très-Haut, dit : ceux-ci sont ainsi dans Ma poigne ; Je suis capable de les anéantir et de les châtier promptement pour avoir traité [ton message] de mensonge : ne t'afflige donc pas de leur dénégation — ils ne M'échapperont pas si Je veux Me venger d'eux. Le deuxième : que cette enveloppe signifie la proximité de leur perte, selon Sa parole, le Très-Haut : "et une autre [conquête] que vous n'avez pu réaliser, dont Allah a déjà pris soin" (al-Fatḥ, 21) ; et Sa parole : "certes ton Seigneur enveloppe les gens" (al-Isrāʾ, 60) ; et Sa parole : "et ils crurent qu'ils étaient cernés" (Yūnus, 22) — tout cela exprime l'imminence de la perte. Il dit : ceux-ci, dans leur dénégation, ont touché à leur perte. Le troisième : que le sens soit "Allah enveloppe leurs œuvres", c'est-à-dire : les connaît — et les guette pour les en châtier. » [Mafātīḥ al-ghayb (Les Clefs du mystère), de Fakhr al-Dīn al-Rāzī : 31/116]</p>
<ul>
<li>Quelles sont les opinions auxquelles le texte a fait allusion au sujet du sens de la parole d'Allah, le Très-Haut : « qu'Allah, de derrière eux, enveloppe » (al-Burūj, 20) ?</li>
</ul>
<p>[La ligne imprimée correspondante est vide dans la source numérisée — perte OCR.]</p>
<ul>
<li>Où est la consolation du Prophète — paix et bénédiction sur lui — dans ce verset : « qu'Allah, de derrière eux, enveloppe » (al-Burūj, 20) ?</li>
</ul>
<p>[La ligne imprimée correspondante est vide dans la source numérisée — perte OCR.]</p>
<h2>La préparation préalable</h2>
<p>Je lis les versets 1 à 10 de la sourate al-Ṭāriq et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Par le ciel et par l'astre nocturne » (al-Ṭāriq, 1) ;</p>
<p>« et qui te dira ce qu'est l'astre nocturne ? » (al-Ṭāriq, 2) ;</p>
<p>« C'est l'étoile vivement brillante » (al-Ṭāriq, 3) ;</p>
<p>« Il n'est pas d'âme qui n'ait sur elle un gardien » (al-Ṭāriq, 4) ;</p>
<p>« Que l'homme considère donc de quoi il a été créé » (al-Ṭāriq, 5) ;</p>
<p>« Il a été créé d'une giclée d'eau » (al-Ṭāriq, 6) ;</p>
<p>« sortie d'entre les lombes et les côtes » (al-Ṭāriq, 7).</p>
<p>[Expressions restituées d'après les versets 1 à 10 de la sourate al-Ṭāriq (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>Je médite sur la création de l'homme, et sur la puissance d'Allah à le ressusciter après la mort.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "14018":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 14018 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 14018 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
