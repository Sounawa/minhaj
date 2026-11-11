#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 16784 (tafsir-5ep, Sourate al-Takwīr 15-21, leçon 13).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : Takwīr 81:15-21 ; parallèle de la puissance =
  Najm 53:5 (« عَلَّمَهُ شَدِيدُ الْقُوَىٰ », la référence imprimée
  [النجم: 5] est correcte) ; préparation = 81:22-25+29 (leçon SUIVANTE
  16227, déjà main — versets harmonisés sur son rendu exact).
- Sharaḥ en <p> : 5 gloses seules — termes restitués (الخنس / الجوار الكنس /
  عسعس / تنفس / مكين) ; garble « قْبَلَ » = أَقْبَلَ (perte OCR initiale).
- Gloses astronomiques des 5 planètes (زحل/المشتري/المريخ/الزهراء/عطار) :
  takhnusu et taknusu « avec ḍamma du nūn » (notes vocaliques exactes) ;
  الْجَوَارِ الْكُنَّسِ glosé « les errantes qui se cachent sous la lumière
  du soleil » (table) et « les cinq planètes » (corps) — les deux conservées.
- ḍādd (contronyme) de عَسْعَسَ (avancer/se retirer) conservé ; ثمَّ =
  « avec fatha du thāʾ, adverbe du lieu éminent » (Jalālayn : obéi au ciel).
- Ibn Kathīr [8/338-339 بتصرف] : qualités de Jibrīl (constitution, rang,
  audition dans l'assemblée suprême, amāna) — conservées avec « (adapté) »
  imprimé.
- Harmonisation 16767 (leçon précédente, préparation = Takwīr 15-19) et
  16227 (leçon suivante, main).
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Takwīr — le Tafsīr al-Jalālayn des versets 15 à 21</h1>
<p>Leçon de tafsīr de la sourate al-Takwīr (versets 15 à 21) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 13.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître la finalité du serment d'Allah, le Très-Haut, dans ces versets.</li>
<li>Employer les attributs de Jibrīl — sur lui la paix — pour argumenter de la véracité du Coran.</li>
<li>Incarner les attributs de Jibrīl — sur lui la paix — pour affermir ma foi.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>Après qu'Allah, le Très-Haut, a affirmé le dogme de la résurrection et du compte dans les versets précédents, Il jure, en ces versets, par de grands témoignages cosmiques, que le Noble Coran est transmis par un messager noble, fidèle en ce qu'il transmet, puissant à porter le dépôt — qualified d'attributs qui le rendent apte à porter la révélation au Messager d'Allah — paix et bénédiction sur lui.<br>
Comment Allah, le Très-Haut, a-t-Il argumenté de la véracité du Noble Coran ? Et quelles finalités ces versets réalisent-ils ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Non ! Je jure par les [astres] qui se retirent, (15) les [astres] qui circulent et se cachent, (16) et par la nuit quand elle s'avance (17) et par l'aube quand elle exhale : (18) c'est la parole d'un noble Messager, (19) doué de force, établi auprès du Maître du Trône, (20) obéi là-haut, et digne de confiance. (21) » (al-Takwīr, 15-21)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Gloses imprimées seules, sans leurs termes — ceux-ci ont été restitués d'après les versets.]</p>
<ul>
<li>al-khunnas (les [astres] qui se retirent) : les astres qui reviennent sur leur cours, à vue d'œil.</li>
<li>al-jawārī al-kunnas (les [astres] qui circulent et se cachent) : les astres errants qui disparaissent sous la lumière du soleil.</li>
<li>ʿasʿasa (s'avance) : est venue avec ses ténèbres, ou s'en est retirée.</li>
<li>tanaffasa (exhale) : s'est étendue jusqu'à devenir un jour clair.</li>
<li>makīn (établi) : de standing.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>Par quoi Allah, le Très-Haut, a-t-Il juré dans ces versets ?</li>
<li>Qui Allah, le Très-Haut, a-t-Il décrit dans ces versets ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la véracité du Noble Coran</h3>
<p>Après qu'Allah, le Très-Haut, a affirmé que la résurrection est vérité, Il jure par les astres que le Noble Coran est vérité et véracité, et le Glorifié dit :</p>
<p>« Non ! Je jure par les [astres] qui se retirent, »</p>
<p>c'est-à-dire : Je jure — et [« lā »] est superflue, pour renforcer le serment ;</p>
<p>« les [astres] qui circulent et se cachent, »</p>
<p>— ce sont les cinq astres : Saturne, Jupiter, Mars, Vénus et Mercure. [Ils] « se retirent » (yakhunus, avec ḍamma du nūn) : reviennent sur leur orbite en retrait — tandis que nous voyons l'astre au bout du mansion, le voilà qui fait retour vers son début ; et « se cachent » (yaknus, avec ḍamma du nūn) : entrent en leur gîte (kinās), c'est-à-dire disparaissent aux lieux où ils disparaissent.</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« et par la nuit quand elle s'avance »</p>
<p>c'est-à-dire : vient avec ses ténèbres, ou s'en retire — [ʿasʿasa] est l'un des termes employés pour la chose et son contraire ;</p>
<p>« et par l'aube quand elle exhale : »</p>
<p>— elle s'étend jusqu'à devenir un jour clair et manifeste ; et [« l'aube »] est coordonnée à ce qui la précède, entrant dans le ressort du serment.</p>
<p>« c'est la parole d'un noble Messager, »</p>
<p>— c'est la réponse du serment : le Noble Coran est certes la parole d'un messager noble auprès d'Allah. Et le messager visé est Jibrīl — sur lui la paix — : le Coran lui est attribué parce qu'il est l'intermédiaire de la transmission de la révélation au Prophète — paix et bénédiction sur lui.</p>
<h3>Deuxièmement : parmi les attributs de Jibrīl — sur lui la paix</h3>
<p>Allah, le Très-Haut, décrivit Jibrīl — sur lui la paix — par cinq attributs. Il est :</p>
<p>« noble » (karīm)</p>
<ul>
<li>c'est-à-dire : noble auprès d'Allah, le Très-Haut.</li>
</ul>
<p>« doué de force » (dhū quwwa)</p>
<p>c'est-à-dire : d'une grande puissance, pour porter le dépôt — comme le Glorifié a dit :</p>
<p>« L'a enseigné [celui qui est] d'une force terrible » (al-Najm, 5)</p>
<p>« établi auprès du Maître du Trône » (makīn)</p>
<p>c'est-à-dire : Jibrīl — sur lui la paix — est titulaire d'un standing élevé et d'un rang immense auprès d'Allah, Puissant et Majestueux ;</p>
<p>« obéi là-haut » (muṭāʿ thumma)</p>
<p>c'est-à-dire : les anges lui obéissent aux cieux — « là-haut » (thumma), avec fatha du thāʾ : adverbe désignant le lieu éminent [et lointain] ;</p>
<p>« et digne de confiance » (amīn)</p>
<p>c'est-à-dire : chargé de la révélation qu'il apporte, et il s'acquitte de ce qu'Allah, le Très-Haut, lui a confié — sans addition ni diminution.</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation d'un ensemble de finalités éducatives, parmi lesquelles :</p>
<ul>
<li>l'affirmation que le Noble Coran est la parole d'Allah, descendue de auprès d'Allah, glorifié soit-Il ;</li>
<li>la qualification de Jibrīl — sur lui la paix — par la puissance et la fiabilité est une preuve de son rang auprès d'Allah, glorifié soit-Il, de la noblesse de sa station, et de la véracité de ce dont il fut envoyé porteur.</li>
</ul>
<h2>L'évaluation</h2>
<ol>
<li>Quelle est la finalité du serment divin dans ces versets ?</li>
<li>Comment argumenté-je de la véracité du Noble Coran ?</li>
<li>Quels sont les effets des attributs de Jibrīl — sur lui la paix — sur l'affermississement de ma foi au Noble Coran et l'éducation de mon comportement ?</li>
</ol>
<h3>L'enrichissement (istithmār)</h3>
<p>On lit dans l'exégèse d'Ibn Kathīr — qu'Allah lui fasse miséricorde — sur Sa parole, le Très-Haut :</p>
<p>« c'est la parole d'un noble Messager » (al-Takwīr, 19)</p>
<p>: « Il veut dire : ce Coran est transmis par un noble messager — un ange généreux, de belle constitution, magnifique d'aspect : c'est Jibrīl, sur lui la prière et la paix… d'une constitution puissante, d'une vigueur et d'une action fortes, ayant rang auprès d'Allah, Puissant et Majestueux, et station élevée… et ayant considération : sa parole est écoutée, il est obéi dans l'assemblée suprême… et Sa parole :</p>
<p>« digne de confiance » (al-Takwīr, 21)</p>
<p>: qualification de Jibrīl par la fiabilité… » [Tafsīr al-Qurʾān al-ʿaẓīm (L'Exégèse du noble Coran), d'Ibn Kathīr : 8/338-339 (adapté)]</p>
<ul>
<li>Le texte qualifie Jibrīl — sur lui la paix — de puissant et de digne de confiance. Quelle est l'importance de ces deux qualités dans la transmission du message ?</li>
</ul>
<h2>La préparation préalable</h2>
<p>Je lis les versets 22 à 29 de la sourate al-Takwīr et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Votre compagnon n'est nullement fou » (al-Takwīr, 22) ;</p>
<p>« il l'a effectivement vu au clair horizon » (al-Takwīr, 23) ;</p>
<p>« il ne garde pas avarement pour lui-même ce qui lui a été révélé » (al-Takwīr, 24) ;</p>
<p>« Et ceci [le Coran] n'est point la parole d'un diable banni » (al-Takwīr, 25) ;</p>
<p>« Mais vous ne pouvez vouloir que si Allah veut, [Lui,] le Seigneur de l'Univers » (al-Takwīr, 29).</p>
<p>[Expressions restituées d'après les versets 22 à 29 de la sourate al-Takwīr (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>Je recherche dans les versets ce qui indique la faveur du Messager — paix et bénédiction sur lui — et celle du Noble Coran.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16784":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16784 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16784 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
