#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 16743 (tafsir-5ep, Sourate ʿAbasa 11-23, leçon 9).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : ʿAbasa 80:11-23 ; istithmār Ibn ʿĀshūr = Aʿlā
  87:18-19, Shuʿarāʾ 26:196, Shūrā 42:3 (le manuel imprime « الشورى: 11 » —
  v11 (لَيْسَ كَمِثْلِهِۦ شَىْءٌ) est hors sujet ; le propos exige « ainsi
  Allah révèle à toi comme à ceux d'avant toi » = 42:3 : convention cache en
  principal + note imprimée) ; préparation = 80:24-27 (leçon SUIVANTE 16751).
- Sharaḥ en <p> (pas de table) : gloses seules — termes restitués (تذكرة /
  سفرة / بررة / قتل).
- Grammaire v13 : « في صحف مكرمة » = second prédicat de [تذكرة], le reste
  en parenthèse (Jalālayn exact) ; v17 : استفهام توبيخ ; v18 : استفهام
  تقرير — conservées.
- Glosses embryologiques v19 : نطفة → ʿalaqa (adhérence) → muḍgha (masse
  de chair) — la baseline LLM imprimait « masticule » (garble) et « une
  adhérence » sans suite : corrigé.
- Harmonisation 16739 (leçon 8, même sourate, main) : « kalā » = « Non ! »,
  style des gloses, « leçon 9 ».
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate ʿAbasa — le Tafsīr al-Jalālayn des versets 11 à 23</h1>
<p>Leçon de tafsīr de la sourate ʿAbasa (versets 11 à 23) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 9.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître les attributs du Noble Coran et son style exhortatif.</li>
<li>Employer ce style dans la réponse aux négateurs de la résurrection.</li>
<li>Tirer admonition du livre d'Allah et me guider à sa guidance.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>Après qu'Allah, le Très-Haut, a repris Son prophète — paix et bénédiction sur lui — pour son empressement à la prédication des associateurs de La Mecque et son occupation au détriment de l'aveugle, Il l'avertit que sa mission est la transmission et l'éveil des insouciants — la mission pour laquelle le Noble Coran fut révélé. Après cet exposé, Allah avertit l'homme ingrat des faveurs de son Seigneur, et le menace du châtiment qu'il encourra s'il persiste en cela.<br>
Quelles sont les finalités de la descente du Coran ? Et comment Allah, le Très-Haut, a-t-Il répondu aux négateurs de la résurrection au Jour de la Résurrection ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Non ! C'est certes une admonition : (11) quiconque veut, donc, s'en souvient — (12) [consignée] dans des feuillets honorés, (13) élevés, purifiés, (14) entre les mains de scribes, (15) nobles, vertueux. (16) Que périsse l'homme ! Qu'il est ingrat ! (17) De quoi l'a-t-Il créé ? (18) D'une goutte, Il l'a créé et l'a déterminé ; (19) puis Il lui a aplani la voie, (20) puis Il l'a fait mourir et lui a donné sépulture ; (21) puis, quand Il veut, Il le ressuscite. (22) Non ! Il n'accomplit point ce qu'Il lui ordonne. (23) » (ʿAbasa, 11-23)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Gloses imprimées seules, sans leurs termes — ceux-ci ont été restitués d'après les versets.]</p>
<ul>
<li>tadhkira (une admonition) : une exhortation pour la création.</li>
<li>safara (les scribes) : des copistes d'entre les anges.</li>
<li>barara (vertueux) : obéissants à Allah, le Très-Haut — ce sont les anges.</li>
<li>qutila (que périsse) : soit maudit.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>À quoi se rapportent les attributs mentionnés dans les versets ?</li>
<li>Par quoi Allah, le Très-Haut, a-t-Il rappelé [Ses faveurs] à l'homme dans ces versets ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : les attributs du Noble Coran</h3>
<p>Après qu'Allah, le Très-Haut, a repris Son prophète — paix et bénédiction sur lui —, Il l'avertit d'éviter ce qui précède, et le Glorifié dit :</p>
<p>« Non ! C'est certes une admonition : »</p>
<p>c'est-à-dire : il n'en est pas comme tu as fait à l'égard des deux factions — « Non ! » (kalā) : ici, annulation du discours précédent, signifiant : ne fais pas de même.</p>
<p>Puis Allah, le Très-Haut, exposa certains attributs du Coran, et le Très-Haut dit :</p>
<p>« une admonition » (tadhkira)</p>
<p>c'est-à-dire : cette sourate — ou les versets — est une exhortation et un rappel pour la création ;</p>
<p>« quiconque veut, donc, s'en souvient »</p>
<p>c'est-à-dire : quiconque veut la conserve et en tire admonition.</p>
<p>Après cet exposé, le Glorifié clarifia le rang du Noble Coran, et dit :</p>
<p>« [consignée] dans des feuillets honorés, élevés, purifiés, entre les mains de scribes, nobles, vertueux »</p>
<p>— [« dans des feuillets honorés »] est une seconde prédication de [« une admonition »], ce qui la précède étant une parenthèse. « honorés » : auprès d'Allah, le Très-Haut ; « élevés » : de rang élevé au ciel ; « purifiés » : préservés du contact des démons ; « scribes » (safara) : des copistes qui les transcrivent depuis la Table préservée ; « nobles, vertueux » : obéissants à Allah, le Très-Haut — ce sont les anges.</p>
<h3>Deuxièmement : les faveurs d'Allah, le Très-Haut, sur l'homme</h3>
<p>Après qu'Allah, le Très-Haut, a exposé aux gens la voie droite et facilité qu'ils l'empruntent, le Glorifié rappela à l'homme obstiné Ses faveurs envers lui, et dit :</p>
<p>« Que périsse l'homme ! Qu'il est ingrat ! »</p>
<p>— c'est une interrogation de blâme : que l'homme ingrat soit maudit — qu'est-ce qui l'a porté à la mécréance ?</p>
<p>« De quoi l'a-t-Il créé ? »</p>
<p>c'est-à-dire : de quelle chose l'a-t-Il créé ? — interrogation de confirmation, que le Glorifié expose par Sa parole :</p>
<p>« D'une goutte, Il l'a créé et l'a déterminé ; »</p>
<p>c'est-à-dire : Allah, le Très-Haut, le créa d'une goutte (nuṭfa), puis le détermina en adhérence (ʿalaqa), puis en masse de chair (muḍgha), jusqu'aux dernières étapes de sa création ;</p>
<p>« puis Il lui a aplani la voie, »</p>
<p>c'est-à-dire : puis Il lui facilita la voie de sa sortie du ventre de sa mère ;</p>
<p>« puis Il l'a fait mourir et lui a donné sépulture ; »</p>
<p>c'est-à-dire : Il le plaça en un tombeau qui le recouvre, en son honneur ;</p>
<p>« puis, quand Il veut, Il le ressuscite. »</p>
<p>c'est-à-dire : puis, quand Allah, le Très-Haut, veut, Il le ressuscite après sa mort ;</p>
<p>« Non ! Il n'accomplit point ce qu'Il lui ordonne. »</p>
<p>c'est-à-dire : en vérité, il ne s'est pas acquitté de ce qu'Allah, glorifié et exalté soit-Il, lui a ordonné d'obéissance et d'adoration.</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation d'un ensemble de finalités éducatives, parmi lesquelles :</p>
<ul>
<li>le Noble Coran est une exhortation et un rappel pour les gens ;</li>
<li>la purification de l'âme par la méditation des manifestations de la puissance d'Allah et de Sa grandeur ;</li>
<li>l'exposé de la faveur d'Allah, le Très-Haut, et de Sa libéralité envers Ses serviteurs, par les diverses sortes de bienfaits.</li>
</ul>
<h2>L'évaluation</h2>
<ol>
<li>Je conclus la finalité de la mention des attributs du Noble Coran renfermés dans les versets.</li>
<li>Qui est « l'homme » mentionné dans les versets ? Et pourquoi Allah a-t-Il blâmé son déni et sa mécréance ?</li>
<li>Quelles sont les finalités que renferment les versets ?</li>
</ol>
<h3>L'enrichissement (istithmār)</h3>
<p>Al-Ṭāhir ibn ʿĀshūr — qu'Allah lui fasse miséricorde — a dit : « Il se peut que par "les feuillets" (ṣuḥuf) on vise les livres des messagers antérieurs à notre maître Muḥammad — paix et bénédiction sur lui —, tels que la Torah, l'Évangile, le Zabūr et les feuillets d'Ibrāhīm — sur lui la paix : ces attributs seraient alors une confirmation du Coran, en ce que les livres divins antérieurs sont venus avec ce qu'il apporte. Et le sens de [l'inscription de] cet avertissement dans les livres des messagers antérieurs est que les pareils de ses sens et leurs principes [figurent] dans leurs livres — comme Allah, le Très-Haut, a dit :</p>
<p>« Ceci est bien dans les feuillets anciens, (18) les feuillets d'Ibrāhīm et de Mūsā. » (al-Aʿlā, 18-19)</p>
<p>et comme Il a dit :</p>
<p>« et il est, certes, dans les Écrits des anciens » (al-Shuʿarāʾ, 196)</p>
<p>et comme Il a dit :</p>
<p>« Ainsi Allah révèle-t-Il à toi comme à ceux d'avant toi — Allah le Puissant, le Sage. » (al-Shūrā, 3 — le manuel imprime « 11 »)</p>
<p>[al-Taḥrīr wa-l-Tanwīr, de al-Ṭāhir ibn ʿĀshūr : 30/117]</p>
<ul>
<li>Je conclus du texte ce qui indique le parachèvement de la loi islamique avec les lois antérieures.</li>
</ul>
<h2>La préparation préalable</h2>
<p>Je lis les versets 24 à 32 de la sourate ʿAbasa et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Que l'homme considère donc sa nourriture » (ʿAbasa, 24) ;</p>
<p>« c'est Nous qui avons versé l'eau, abondamment » (ʿAbasa, 25) ;</p>
<p>« puis fendu la terre, entièrement » (ʿAbasa, 26) ;</p>
<p>« et fait croître les grains » (ʿAbasa, 27).</p>
<p>[Expressions restituées d'après les versets 24 à 32 de la sourate ʿAbasa (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>Je recherche des preuves de l'existence d'une vie après la mort.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16743":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16743 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16743 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
