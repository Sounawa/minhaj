#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 16767 (tafsir-5ep, Sourate al-Takwīr 1-14, leçon 12).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : Takwīr 81:1-14 ; parallèle des montagnes =
  Kahf 18:47 (le manuel imprime « 46 » — v46 (المال والبنون) est hors sujet ;
  le parallèle exact de نسير الجبال→هباء est 18:47 : convention cache en
  principal + note imprimée) ; Nabaʾ 78:40 (le négateur « would I were dust ») ;
  Naḥl 16:58-59 (les filles enterrées vivantes) ; Isrāʾ 17:13-14 (le livre
  déployé) ; istithmār = Takwīr 81:1-13 + le jawāb 81:14 + hadiths Adī b.
  Ḥātim (Ṣaḥīḥayn) et Ibn ʿUmar (Tirmidhī : lire Takwīr/Infiṭār/Inshiqāq) ;
  préparation = 81:15-19 (leçon SUIVANTE 16784).
- Sharaḥ en <p> : 10 gloses seules — termes restitués (كورت/انكدرت/سيرت/
  العشار/عطلت/سجرت/الموءودة/كشطت/سعرت/أزلفت).
- Qurṭubī [19/229] sur les ʿishār (parabole de la chamelle pleine) et
  [19/236] sur la lecture d'Ibn ʿAbbās et ʿUmar — conservés avec références.
- Note qirāʾique v9 conservée : قُتِلَتْ / قُتِلْتِ (kasra du tāʾ, récit
  direct) ; v6 : سُجِّرَتْ lu avec takhfīf et tashdīd.
- Garble de la préparation « َقْرَأُ » = أَقْرَأُ (perte OCR de l'initiale).
- Harmonisation 16757 (leçon précédente, préparation = Takwīr 1-10) :
  « Quand le soleil sera replié », « les étoiles s'obscurciront », etc.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Takwīr — le Tafsīr al-Jalālayn des versets 1 à 14</h1>
<p>Leçon de tafsīr de la sourate al-Takwīr (versets 1 à 14) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 12.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître les signes du Jour de la Résurrection mentionnés dans ces versets.</li>
<li>Conclure des versets la finalité du serment d'Allah, le Très-Haut.</li>
<li>Obéir aux ordres d'Allah, glorifié soit-Il, et éviter Ses interdits, pour obtenir Son agrément à Sa rencontre.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>La sourate al-Takwīr est mecquoise et compte vingt-neuf versets. Ces versets traitent de la description par Allah, le Très-Haut, des états du Jour de la Résurrection et des changements qui atteindront le ciel et la terre — pour inciter l'homme au bien et le guider vers l'évitement du mal.<br>
Quels sont les changements qui atteindront le ciel et la terre ? Et quel est l'effet de ces versets sur la purification de mon âme ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Quand le soleil sera replié, (1) et que les étoiles s'obscurciront, (2) et que les montagnes seront mises en marche, (3) et que les chamelles pleines seront délaissées, (4) et que les bêtes seront rassemblées, (5) et que les mers seront embrasées, (6) et que les âmes seront appareillées, (7) et que la petite enterrée sera interrogée (8) — pour quel péché elle fut tuée ? — (9) et que les feuillets seront déployés, (10) et que le ciel sera écorché, (11) et que la Géhenne sera embrasée, (12) et que le Paradis sera approché : (13) alors, toute âme saura ce qu'elle a présenté. (14) » (al-Takwīr, 1-14)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Gloses imprimées seules, sans leurs termes — ceux-ci ont été restitués d'après les versets.]</p>
<ul>
<li>kuwwirat (replié) : enveloppé, et privé de sa lumière.</li>
<li>inkadarat (s'obscurciront) : s'effondreront et tomberont.</li>
<li>suyyirat (mises en marche) : emportées de la surface de la terre.</li>
<li>al-ʿishār (les chamelles pleines) : les chamelles gestantes.</li>
<li>ʿuṭṭilat (délaissées) : laissées sans berger ni traite.</li>
<li>sujjirat (embrasées) : allumées, devenues feu.</li>
<li>al-mawʾūda (l'enterrée) : la fille enterrée vivante.</li>
<li>kushiṭat (écorché) : retiré de ses places.</li>
<li>suʿʿirat (embrasée) : attisée.</li>
<li>uzlifat (approché) : rapproché de ses gens.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>Je dégage les signes du Jour de la Résurrection à travers les versets.</li>
<li>J'extrais des versets les finalités et les buts qu'ils visent.</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : les états du ciel et de la terre au Jour de la Résurrection</h3>
<p>Allah, le Très-Haut, expose en ces versets les terreurs du Jour de la Résurrection et les rigueurs qu'il renferme. Le Glorifié dit :</p>
<p>« Quand le soleil sera replié, »</p>
<p>c'est-à-dire : quand le soleil sera enveloppé et privé de sa lumière ;</p>
<p>« et que les étoiles s'obscurciront, »</p>
<p>c'est-à-dire : elles s'effondreront et tomberont de leurs places, éparses sur la terre ;</p>
<p>« et que les montagnes seront mises en marche, »</p>
<p>c'est-à-dire : les montagnes seront déplacées de leurs places et mises en marche dans l'air comme marche le nuage, emportées de la surface de la terre, faites poussière disséminée (habāʾ munbashir) — semblable à Sa parole, le Très-Haut :</p>
<p>« Et le jour où Nous mettrons les montagnes en marche, et tu verras la terre nivelée, et Nous les rassemblerons sans en laisser aucun. » (al-Kahf, 47 — le manuel imprime « 46 »)</p>
<p>« et que les chamelles pleines seront délaissées, »</p>
<p>c'est-à-dire : les chamelles gestantes — parvenues à dix mois de gestation, proches de la mise bas — seront laissées sans berger ni traite, leurs propriétaires étant occupés d'eux-mêmes par ce qui les a frappés, alors même qu'il n'est pas de bien plus cher à eux qu'elles.</p>
<p>« On n'a mentionné les ʿishār que parce qu'elles sont ce que les Arabes possèdent de plus précieux, et leurs propriétaires ne les abandonnent qu'au temps de la Résurrection. C'est à titre de parabole : à la Résurrection, il n'y aura pas de chamelle à dix mois — mais on a voulu par là l'image : le terror du Jour de la Résurrection est tel que, si un homme avait une chamelle à dix mois, il l'abandonnerait et serait occupé de lui-même. » [al-Ǧāmiʿ li-aḥkām al-Qurʾān, d'al-Qurṭubī : 19/229]</p>
<p>Puis le Très-Haut dit :</p>
<p>« et que les bêtes seront rassemblées, »</p>
<p>c'est-à-dire : rassemblées après la résurrection, pour que vengeance soit exercée de certaines sur d'autres ; puis elles deviendront poussière — alors le négateur souhaitera devenir poussière comme elles, selon Sa parole, le Très-Haut :</p>
<p>« Nous vous avons averti d'un châtiment proche, le jour où l'homme regardera ce que ses mains ont avancé, et où le négateur dira : "Plût à Allah que je fusse poussière !" » (al-Nabaʾ, 40)</p>
<p>« et que les mers seront embrasées, »</p>
<p>— lu avec allègement et renforcement (takhfīf et tashdīd) : c'est-à-dire : allumées, et devenues un feu qui flambe ;</p>
<p>« et que les âmes seront appareillées, »</p>
<p>c'est-à-dire : accouplées à leurs corps ;</p>
<p>« et que la petite enterrée sera interrogée »</p>
<p>c'est-à-dire : la fille enterrée vivante, par crainte du déshonneur et de l'indigence ;</p>
<p>« pour quel péché elle fut tuée ? »</p>
<p>c'est-à-dire : interrogée en blâme de son meurtrier — pour qu'elle dise qu'elle fut tuée sans aucun péché. Et on lit (qutilti) avec kasra du tāʾ, en citation de ce qui lui est adressé, sa réponse étant de dire : « J'ai été tuée sans péché. »</p>
<p>Des Arabes enterraient vivantes leurs filles, par crainte de la pauvreté et par peur de l'asservissement ; Allah, le Très-Haut, a blâmé leur fait en maints versets du Noble Coran, dont Sa parole :</p>
<p>« Et lorsqu'à l'un d'eux est annoncée la fille, son visage s'assombrit et il suffoque de chagrin : (58) il se dérobe aux gens, du mal de ce qui lui a été annoncé : le retient-il [avec honneur] malgré la honte, ou l'ensevelira-t-il dans la poussière ? Ah ! quelle condamnation que leur jugement ! » (al-Naḥl, 58-59)</p>
<p>Puis le Très-Haut dit :</p>
<p>« et que les feuillets seront déployés, »</p>
<p>c'est-à-dire : les feuillets seront ouverts et étendus — visant les feuillets des œuvres, roulés à la mort de l'homme et déployés au compte, pour que chaque homme lise son livre. Allah, le Très-Haut, a dit :</p>
<p>« À chaque homme, Nous avons attaché son oiseau [de destin] à son cou ; et Nous lui ferons sortir, au Jour de la Résurrection, un livre qu'il trouvera déployé : (13) "Lis ton livre : tu suffiras aujourd'hui à te tenir compte." (14) » (al-Isrāʾ, 13-14)</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« et que le ciel sera écorché, »</p>
<p>c'est-à-dire : le ciel sera retiré et arraché de ses places, comme on dépouille la peau du mouton ;</p>
<p>« et que la Géhenne sera embrasée, »</p>
<p>c'est-à-dire : le Feu sera attisé ;</p>
<p>« et que le Paradis sera approché : »</p>
<p>c'est-à-dire : approché et rapproché de ses gens, pour qu'ils y entrent.</p>
<p>Et la réponse [à « Quand… »] — elle et ce qui lui est coordonné — est Sa parole, le Très-Haut :</p>
<p>« alors, toute âme saura ce qu'elle a présenté. »</p>
<p>c'est-à-dire : quand surviendront tous les événements susdits, qui indiquent l'avènement de l'Heure, la sortie des gens de leurs tombes et leur rassemblement pour le compte — alors toute âme saura ce qu'elle a œuvré, et ce qui lui a été préparé de bien ou de mal.</p>
<h3>Deuxièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation d'un ensemble de finalités éducatives, parmi lesquelles :</p>
<ul>
<li>l'affirmation du dogme de la résurrection et de la rétribution, vu son effet sur la purification et l'éducation des âmes ;</li>
<li>la dénonciation des Arabes de la période idolâtre (jāhiliyya), qui enterraient vivantes leurs filles par crainte du déshonneur ;</li>
<li>l'affirmation du droit de l'homme à la vie.</li>
</ul>
<h2>L'évaluation</h2>
<ol>
<li>Quelle est la cause des changements qui atteindront le ciel et la terre, mentionnés dans les versets ?</li>
<li>Quelle est la finalité du serment d'Allah, le Très-Haut, dans ces versets ?</li>
<li>Je conclus des versets un droit de l'homme que l'islam garantit.</li>
</ol>
<h3>L'enrichissement (istithmār)</h3>
<p>L'imam al-Qurṭubī — qu'Allah lui fasse miséricorde — rapporte qu'Ibn ʿAbbās et ʿUmar ibn al-Khaṭṭāb — qu'Allah les agrée — lurent Sa parole, le Très-Haut :</p>
<p>« Quand le soleil sera replié, et que les étoiles s'obscurciront, et que les montagnes seront mises en marche, et que les chamelles pleines seront délaissées, et que les bêtes seront rassemblées, et que les mers seront embrasées, et que les âmes seront appareillées, et que la petite enterrée sera interrogée — pour quel péché elle fut tuée ? — et que les feuillets seront déployés, et que le ciel sera écorché, et que la Géhenne sera embrasée, et que le Paradis sera approché » (al-Takwīr, 1-13)</p>
<p>les versets ; « et lorsqu'ils atteignirent :</p>
<p>« alors, toute âme saura ce qu'elle a présenté » (al-Takwīr, 14)</p>
<p>ils dirent : c'est pour cela que le récit fut déroulé. Le sens est donc : quand le soleil sera replié et que ces choses seront, toute âme saura ce qu'elle aura présenté de son œuvre. Et dans les deux Ṣaḥīḥ, d'après ʿAdī ibn Ḥātim : le Messager d'Allah — paix et bénédiction sur lui — a dit : « Il n'est aucun d'entre vous dont Allah ne lui parlera, sans interprète entre Lui et lui : il regardera à sa droite et ne verra que ce qu'il a avancé, il regardera à sa gauche et ne verra que ce qu'il a préparé devant lui — et le Feu le fera face. Que quiconque d'entre vous le peut se garde du Feu, ne serait-ce qu'avec la moitié d'une datte ! » [al-Ǧāmiʿ li-aḥkām al-Qurʾān, d'al-Qurṭubī : 19/236]</p>
<p>Et al-Tirmidhī rapporte, dans le commentaire de cette sourate, un hadith d'après Ibn ʿUmar — qu'Allah les agrée : le Prophète — paix et bénédiction sur lui — a dit : « Quiconque souhaite regarder au Jour de la Résurrection comme s'il le voyait à l'œil nue, qu'il lise :</p>
<p>« Quand le soleil sera replié » (al-Takwīr, 1)</p>
<p>et :</p>
<p>« Quand le ciel se fendra » (al-Infiṭār, 1)</p>
<p>et :</p>
<p>« Quand le ciel se fendra » (al-Inshiqāq, 1)</p>
<p>[Sunan al-Tirmidhī, chapitres de l'exégèse du Coran, chapitre « et de la sourate "Quand le soleil sera replié" »]</p>
<ul>
<li>Comment bénéfice-je de ces textes pour la purification et l'éducation de mon âme ?</li>
</ul>
<h2>La préparation préalable</h2>
<p>Je lis les versets 15 à 21 de la sourate al-Takwīr et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Non ! Je jure par les [astres] qui se retirent » (al-Takwīr, 15) ;</p>
<p>« les [astres] qui circulent et se cachent » (al-Takwīr, 16) ;</p>
<p>« et par la nuit quand elle s'avance » (al-Takwīr, 17) ;</p>
<p>« et par l'aube quand elle exhale » (al-Takwīr, 18) ;</p>
<p>« c'est la parole d'un noble Messager » (al-Takwīr, 19).</p>
<p>[Expressions restituées d'après les versets 15 à 21 de la sourate al-Takwīr (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>Je recherche les attributs de Jibrīl — sur lui la paix — mentionnés dans ces versets.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16767":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16767 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16767 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
