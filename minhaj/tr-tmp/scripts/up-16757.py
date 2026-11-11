#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 16757 (tafsir-5ep, Sourate ʿAbasa 33-42, leçon 11).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : ʿAbasa 80:33-42 ; réponse du hadith Tirmidhī =
  80:37 (span « عبس: 37 ») ; conclusion du récit Ibn Kathīr = 80:34-37 (le
  récit ʿIkrima illustre précisément la fuite des proches) ; préparation =
  Takwīr 81:1-10 (leçon SUIVANTE 16767, 10 slots).
- Sharaḥ en <p> : gloses seules — termes restitués (الصاخة / مسفرة / غبرة /
  قترة / الفجرة).
- Garble de l'évaluation « ُوَضِّحُ » = أُوَضِّحُ (perte OCR de l'initiale).
- Hadith Tirmidhī (Ibn ʿAbbās) : « تُحْشَرُونَ حُفَاةً عُرَاةً غُرْلًا » +
  réponse « يا فلانة » + v37 — conservés avec référence de chapitre.
- Récit ʿIkrima [Ibn Kathīr 8/325] : dialogue épouse/fils + demande d'une
  seule ḥasana — traduit intégralement.
- FIX harmonisation 16751 : الصاخة rendue « la Clameur » (et non
  « Bourdonnement ») — up-16751.py corrigé et ré-exécuté au préalable.
- Harmonisation 13920 (ʿAbasa 38-39 citées) : « Des visages, ce jour-là,
  rayonnants, riant, réjouis » ; 16751 (préparation) : v33-37 et v40.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate ʿAbasa — le Tafsīr al-Jalālayn des versets 33 à 42</h1>
<p>Leçon de tafsīr de la sourate ʿAbasa (versets 33 à 42) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 11.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître un aspect du dogme de la résurrection et de la rétribution.</li>
<li>Distinguer entre la rétribution des bienheureux et celle des malheureux au Jour de la Résurrection.</li>
<li>Œuvrer à la purification de mon âme, pour être parmi les bienheureux au Jour de la Résurrection.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>Après qu'Allah, le Très-Haut, a exposé le commencement de l'affaire de l'homme — sa vie et sa subsistance —, Il clarifie en ces versets l'affaire de son retour [vers l'au-delà], pour qu'il veille à affermir sa foi et multiplier les œuvres justes. Il l'y a stimulé par la mention de scènes des terreurs du Jour de la Résurrection — le jour où le plus proche et le plus cher des gens ne lui servira de rien : seuls sa foi et son œuvre juste lui profiteront.<br>
Quelle sera la relation de l'homme à ses proches au Jour de la Résurrection ? Et sur quelle base les gens se diviseront-ils ce jour-là ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Mais non ! Quand viendra la Clameur, (33) le jour où l'homme fuira son frère, (34) et sa mère et son père, (35) et sa compagne et ses enfants : (36) ce jour-là, chacun aura son affaire qui l'occupera. (37) Des visages, ce jour-là, seront rayonnants, (38) riant, réjouis ; (39) et des visages, ce jour-là, couverts de poussière, (40) que couvrira une noirceur : (41) voilà les infidèles, les dévergondés. (42) » (ʿAbasa, 33-42)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Gloses imprimées seules, sans leurs termes — ceux-ci ont été restitués d'après les versets.]</p>
<ul>
<li>al-ṣākha (la Clameur) : le second soufflement.</li>
<li>musfira (rayonnants) : lumineux.</li>
<li>ghabara (poussière) : poussière.</li>
<li>qatara (noirceur) : que couvrent ténèbres et noirceur.</li>
<li>al-fajara (les dévergondés) : ceux qui joignent mécréance et dévergondage.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>De qui l'homme fuira-t-il au Jour de la Résurrection ?</li>
<li>Quelles sont les catégories des gens au Jour de la Résurrection ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la fuite des gens d'auprès de leurs proches au Jour de la Résurrection</h3>
<p>Après les faveurs qu'Allah, le Très-Haut, a rappelées à Ses serviteurs, et Son argumentation de la résurrection, le Glorifié mentionne les terreurs du Jour de la Résurrection, qui font oublier les liens familiaux. Le Glorifié dit :</p>
<p>« Mais non ! Quand viendra la Clameur, »</p>
<p>c'est-à-dire : quand viendra le cri du Jour de la Résurrection, au second soufflement ;</p>
<p>« le jour où l'homme fuira son frère, et sa mère et son père, »</p>
<p>c'est-à-dire : ce cri viendra en un jour où l'homme fuira son frère, sa mère et son père ;</p>
<p>« et sa compagne »</p>
<p>c'est-à-dire : son épouse ;</p>
<p>« et ses enfants : »</p>
<p>— ceux qui sont issus de lui.</p>
<p>Puis le Glorifié exposa la cause de sa fuite d'eux, et dit :</p>
<p>« ce jour-là, chacun aura son affaire qui l'occupera. »</p>
<p>c'est-à-dire : chaque homme, en ce jour, a un état qui l'occupe de l'affaire d'autrui — il n'est occupé que de lui-même.</p>
<p>Et de par l'intensité de l'occupation de l'homme par son état, il ne regarde pas la nudité de qui est à son côté. D'après Ibn ʿAbbās — qu'Allah les agrée —, d'après le Prophète — paix et bénédiction sur lui — : « Vous serez rassemblés pieds nus, nus, non circoncis. » Une femme dit : verrons-nous, certains d'entre nous, la nudité des autres ? Il dit : « Ô telle femme —</p>
<p>ce jour-là, chacun aura son affaire qui l'occupera ! » (ʿAbasa, 37)</p>
<p>[Sunan al-Tirmidhī, chapitres de l'exégèse du Coran, chapitre « et de la sourate ʿAbasa »]</p>
<h3>Deuxièmement : les bienheureux et les malheureux au Jour de la Résurrection</h3>
<p>Allah, glorifié soit-Il, mentionne en ces versets la division des gens en deux factions — bienheureux et malheureux —, et commence par les bienheureux. Le Glorifié dit :</p>
<p>« Des visages, ce jour-là, seront rayonnants, »</p>
<p>c'est-à-dire : illuminés, lumineux ;</p>
<p>« riant, réjouis ; »</p>
<p>c'est-à-dire : joyeux — ce sont les croyants.</p>
<p>Puis Allah, le Très-Haut, mentionna la catégorie opposée — les malheureux —, et le Glorifié dit :</p>
<p>« et des visages, ce jour-là, couverts de poussière, »</p>
<p>c'est-à-dire : en ce jour, les visages des malheureux seront couverts de poussière ;</p>
<p>« que couvrira une noirceur : »</p>
<p>— que couvriront ténèbres et noirceur, de par l'intensité de la honte et de la perte qui les auront frappés ;</p>
<p>« voilà les infidèles, les dévergondés. »</p>
<p>c'est-à-dire : les gens de cet état sont ceux qui joignent la mécréance et le dévergondage.</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation d'un ensemble de finalités éducatives, parmi lesquelles :</p>
<ul>
<li>la purification de l'âme et son nettoiement des fautes et désobéissances, par ce qu'elle a connu des terreurs du Jour de la Résurrection ;</li>
<li>l'exposé que les droits des gens sont garantis au Jour de la Résurrection, car Allah, le Très-Haut, rétribuera Ses serviteurs de la justice et de l'équité extrêmes ;</li>
<li>la foi et l'œuvre juste feront éclore des visages rayonnants, par ce qu'ils trouvèrent auprès de leur Seigneur de libéralité et de générosité ;</li>
<li>la mécréance et le dévergondage produiront ténèbres et noirceur sur les visages de qui s'en sera qualifié.</li>
</ul>
<h2>L'évaluation</h2>
<ol>
<li>J'expose des scènes de la résurrection et de la rétribution que renferment les versets.</li>
<li>Je distingue entre les attributs des bienheureux et des malheureux au Jour de la Résurrection.</li>
<li>Quelles sont les œuvres qui font éclore la félicité au Jour de la Résurrection ?</li>
</ol>
<h3>L'enrichissement (istithmār)</h3>
<p>L'imam Ibn Kathīr — qu'Allah lui fasse miséricorde — rapporte dans son exégèse, d'après ʿIkrima — qu'Allah l'agrée — : « L'homme rencontrera son épouse et lui dira : "Ô toi, quel époux fus-je pour toi ?" Elle dira : "Quel bon époux tu fus !" — et elle le louera de son mieux. Il lui dira : "Je te demande aujourd'hui une seule bonne œuvre : offre-la-moi, peut-être échapperai-je à ce que tu vois." Elle lui dira : "Que ce que tu demandes est peu de chose ! Mais je ne puis te rien donner : je redoute ce que tu redoutes." Et l'homme rencontrera son fils, qui s'attachera à lui et dira : "Ô mon fils, quel père fus-je pour toi ?" — et il le louera de son mieux. Il lui dira : "Ô mon fils, j'ai besoin du poids d'un grain de moutarde de tes bonnes œuvres, peut-être en serai-je sauvé de ce que tu vois." Son fils dira : "Ô mon père, que ce que tu demandes est peu de chose ! Mais je redoute ce que tu redoutes : je ne puis te rien donner." Allah, le Très-Haut, dit :</p>
<p>« le jour où l'homme fuira son frère, et sa mère et son père, et sa compagne et ses enfants — ce jour-là, chacun aura son affaire qui l'occupera. » (ʿAbasa, 34-37)</p>
<p>[Tafsīr al-Qurʾān al-ʿaẓīm (L'Exégèse du noble Coran), d'Ibn Kathīr : 8/325]</p>
<ul>
<li>Pourquoi les proches se démettent-ils les uns des autres au Jour de la Résurrection ?</li>
</ul>
<h2>La préparation préalable</h2>
<p>Je lis les versets 1 à 14 de la sourate al-Takwīr et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Quand le soleil sera replié » (al-Takwīr, 1) ;</p>
<p>« et que les étoiles s'obscurciront » (al-Takwīr, 2) ;</p>
<p>« et que les montagnes seront mises en marche » (al-Takwīr, 3) ;</p>
<p>« et que les chamelles pleines seront délaissées » (al-Takwīr, 4) ;</p>
<p>« et que les bêtes seront rassemblées » (al-Takwīr, 5) ;</p>
<p>« et que les mers seront embrasées » (al-Takwīr, 6) ;</p>
<p>« et que les âmes seront appareillées » (al-Takwīr, 7) ;</p>
<p>« et que la petite enterrée sera interrogée » (al-Takwīr, 8) ;</p>
<p>« pour quel péché elle fut tuée » (al-Takwīr, 9) ;</p>
<p>« et que les feuillets seront déployés » (al-Takwīr, 10).</p>
<p>[Expressions restituées d'après les versets 1 à 14 de la sourate al-Takwīr (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>Je recherche les scènes des terreurs du Jour de la Résurrection que renferment les versets.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16757":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16757 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16757 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
