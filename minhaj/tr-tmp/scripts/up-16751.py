#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 16751 (tafsir-5ep, Sourate ʿAbasa 24-32, leçon 10).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : ʿAbasa 80:24-32 ; istithmār Qurṭubī = 80:24 ;
  préparation = 80:33-37 + 40 (leçon SUIVANTE 16757).
- Sharaḥ en <p> : gloses seules — termes restitués (حبًّا / قضبًا / غلبًا /
  أبًّا) ; double glose d'أب (herbe pâture / paille) conservée.
- Garble du 3e مقصد « مْلُ الْإِنْسَانِ » = حَمْلُ (perte OCR de l'initiale)
  — rendu « porter l'homme à… », noté ici.
- Glosses v24-32 verset par verset (versé l'eau / fendu la terre / grains /
  raisin-qaḍḍ raṭb / olivier-palmier / jardins / fruits-dessert / herbages /
  jouissance) — toutes conservées.
- Qurṭubī [al-Ǧāmiʿ 19/220] : le regard du cœur par la réflexion, préparation
  au Maʿād — conservé avec référence.
- Harmonisation 16743 (leçon précédente, même sourate) : « Que l'homme
  considère donc sa nourriture », « c'est Nous qui avons versé l'eau,
  abondamment », « puis fendu la terre, entièrement », « et fait croître les
  grains » ; harmonisation 13920 (ʿAbasa 38-39 citées là) : « Des visages, ce
  jour-là, rayonnants, riant, réjouis » — même sourate, cohérence leçon 12.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate ʿAbasa — le Tafsīr al-Jalālayn des versets 24 à 32</h1>
<p>Leçon de tafsīr de la sourate ʿAbasa (versets 24 à 32) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 10.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître les faveurs dont Allah, le Très-Haut, a comblé l'homme.</li>
<li>Conclure l'indication de ces versets sur la réalité de la survenue de la résurrection.</li>
<li>Tirer leçon des manifestations de la puissance d'Allah, le Très-Haut, et de Sa grandeur.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>Après qu'Allah a rappelé à l'homme renieur et ingrat les faveurs de son Seigneur, ces versets viennent, dans le même contexte, éveiller l'homme à considérer et méditer les faveurs dont jouissent sa personne et ses troupeaux — peut-être reviendra-t-il de son égarement, de son déni et de sa négation.<br>
Quelles sont les faveurs rappelées à l'homme dans ces versets ? Et quelles finalités ce rappel vise-t-il ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Que l'homme considère donc sa nourriture : (24) c'est Nous qui avons versé l'eau, abondamment, (25) puis fendu la terre, entièrement, (26) et fait croître les grains, (27) la vigne et le fourrage frais, (28) l'olivier et le palmier, (29) des jardins aux arbres touffus, (30) et des fruits et des herbages — (31) une jouissance pour vous et pour vos bestiaux. (32) » (ʿAbasa, 24-32)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Gloses imprimées seules, sans leurs termes — ceux-ci ont été restitués d'après les versets.]</p>
<ul>
<li>ḥabban (les grains) : comme le blé et l'orge.</li>
<li>qaḍban (le fourrage frais) : le fourrage vert.</li>
<li>ghulban (touffus) : des jardins aux arbres nombreux.</li>
<li>abban (les herbages) : ce que paissent les bêtes.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>Sur quoi Allah, le Très-Haut, a-t-Il argumenté dans ces versets ?</li>
<li>Quelles sont les finalités que réalisent les versets ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la vie après la mort</h3>
<p>Après qu'Allah, le Très-Haut, a mentionné la création de l'homme dans les versets précédents, Il expose en ces versets ce qu'Il lui a facilité de sa subsistance, pour offrir un autre argument sur la manière de sa résurrection après sa mort. Le Glorifié dit :</p>
<p>« Que l'homme considère donc sa nourriture : »</p>
<p>c'est-à-dire : que cet homme regarde et médite l'affaire de sa nourriture — comment Allah l'a déterminée, disposée et préparée pour lui.</p>
<p>Puis le Glorifié exposa comment Il prépara la nourriture de l'homme, et le Puissant et Majestueux dit :</p>
<p>« c'est Nous qui avons versé l'eau, abondamment, »</p>
<p>c'est-à-dire : Nous avons fait descendre des nuées une eau sur la terre, en abondance ;</p>
<p>« puis fendu la terre, entièrement, »</p>
<p>c'est-à-dire : Nous avons fendu la terre par la végétation, d'une fente ;</p>
<p>« et fait croître les grains, »</p>
<p>c'est-à-dire : Nous avons fait sortir de la terre, après la descente de l'eau sur elle, une végétation — comme le blé et l'orge, et tout ce qui se moissonne et s'emmagasine ;</p>
<p>« la vigne et le fourrage frais, »</p>
<p>c'est-à-dire : et Nous avons fait sortir de la terre le raisin et les plantes mangées fraîches et tendres — c'est le fourrage vert (qaḍḍ raṭb) ;</p>
<p>« l'olivier et le palmier, »</p>
<p>c'est-à-dire : et Nous avons fait sortir de la terre les arbres de l'olivier et du palmier ;</p>
<p>« des jardins aux arbres touffus, »</p>
<p>— des jardins aux arbres nombreux ;</p>
<p>« et des fruits et des herbages — »</p>
<p>c'est-à-dire : et Nous avons fait sortir d'elle les sortes de fruits — nom des fruits que l'homme consomme à titre de dessert, comme la pomme et le raisin ; « des herbages » (abb) : ce que paissent les bêtes, de l'herbe et du gazon — et il est dit : c'est la paille ;</p>
<p>« une jouissance pour vous et pour vos bestiaux. »</p>
<p>c'est-à-dire : en jouissance, ou en jouissement, pour vous et pour vos bestiaux.</p>
<h3>Deuxièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation d'un ensemble de finalités éducatives, parmi lesquelles :</p>
<ul>
<li>l'exposé de la libéralité d'Allah, le Très-Haut, et de Sa faveur envers Ses serviteurs, par les biens qu'Il leur a assujettis ;</li>
<li>l'argumentation, à partir de la vivification de la végétation depuis la terre, de la vivification de l'homme après sa mort ;</li>
<li>porter l'homme à reconnaître l'existence d'Allah, le Très-Haut, et à ressentir Sa faveur et Sa puissance immense.</li>
</ul>
<h2>L'évaluation</h2>
<ol>
<li>Quelles sont les faveurs dont Allah, le Très-Haut, a comblé l'homme dans les versets ?</li>
<li>Comment argumentes-tu, à travers ces versets, de la survenue de la résurrection ?</li>
<li>Quels sont les effets de ces versets sur mon comportement et mes actes ?</li>
</ol>
<h3>L'enrichissement (istithmār)</h3>
<p>L'imam al-Qurṭubī — qu'Allah lui fasse miséricorde — a dit, en commentant la parole d'Allah, le Très-Haut :</p>
<p>« Que l'homme considère donc sa nourriture » (ʿAbasa, 24)</p>
<p>: « Après que le Glorifié — louange à Sa grandeur — a mentionné le commencement de la création de l'homme, Il mentionna ce qu'Il facilita de sa subsistance : c'est-à-dire : qu'il considère comment Allah a créé sa nourriture. Et ce regard est celui du cœur, par la réflexion : c'est-à-dire : qu'il médite comment Allah a créé sa nourriture — le soutien de sa vie —, et comment Il lui a préparé les moyens de la subsistance, pour s'en préparer au retour [vers l'au-delà]. » [al-Ǧāmiʿ li-aḥkām al-Qurʾān (Le Recueil des règles du Coran), d'al-Qurṭubī : 19/220]</p>
<ul>
<li>Quelle est la nature du regard mentionné dans le verset ? Et quelle est sa finalité ?</li>
</ul>
<h2>La préparation préalable</h2>
<p>Je lis les versets 33 à 42 de la sourate ʿAbasa et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Mais non ! Quand viendra la Clameur » (ʿAbasa, 33) ;</p>
<p>« le jour où l'homme fuira son frère » (ʿAbasa, 34) ;</p>
<p>« et sa mère et son père, » (ʿAbasa, 35) ;</p>
<p>« et sa compagne et ses enfants » (ʿAbasa, 36) ;</p>
<p>« ce jour-là, chacun aura son affaire qui l'occupera » (ʿAbasa, 37) ;</p>
<p>« Et des visages, ce jour-là, couverts de poussière » (ʿAbasa, 40).</p>
<p>[Expressions restituées d'après les versets 33 à 42 de la sourate ʿAbasa (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>Je recherche la cause de la fuite des gens d'auprès de leurs proches au Jour de la Résurrection.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16751":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16751 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16751 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
