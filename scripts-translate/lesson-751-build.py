#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — construction de la leçon 751 (tafsir-5ep, sūrat al-Kahf v44-45 de
l'imprimé warš = āyāt 45-46 du cache canonique ḥafṣ — treizième leçon du second
livre, pages 96-101 du manuel miroir tafsir-3-thanawi). Émet tr-tmp/lesson-751-fr.html.
Doctrine FR-seule : versets rendus mot pour mot du cache (apostrophes
typographiques), 0 arabe, guillemets « » appariés."""
import json

CACHE = "scripts-translate/quran-cache.json"
OUT = "tr-tmp/lesson-751-fr.html"

cache = json.load(open(CACHE, encoding="utf-8"))
fr = {n: t for n, t in cache["18"]["fr"]}


def v(n: int) -> str:
    """Rendu coranique du cache : apostrophe droite -> typographique."""
    return fr[n].replace("'", "\u2019")


html = f"""<h1>Sourate al-Kahf, versets 44 à 45&nbsp; : le livre du Tafsīr de troisième année de l’enseignement secondaire traditionnel — leçon 13</h1>
<dl class="lesson-meta">
<dt>Source du cours</dt>
<dd>Treizième leçon du second livre du parcours&nbsp; : le commentaire de sūrat al-Kahf (pages 96 à 101 de l’imprimé miroir), faisant suite à la muḥāwara des deux compagnons et à l’issue du propriétaire ingrat, et frappant l’exemple de la vie d’ici-bas. Le portail des Habous restant fermé (documents inaccessibles), la matière est portée par le manuel complet du miroir archive.org — collection «&nbsp;&nbsp;1_20220304_20220304_2251&nbsp;&nbsp;», version texte du fascicule, bornes de la leçon sondées par le mécanisme des en-têtes d’objectifs et des préparations préalables (p.96 ouvre la leçon 13&nbsp; ; les objectifs de la leçon 14 ouvrent p.102 — jamais devinées). Les versets sont rendus en français sur le rasm warš du cache de référence — la numérotation de l’imprimé suit le décompte warš&nbsp; : la plage imprimée (44-45) correspond aux āyāt 45 et 46 du cache canonique, décalage de un maintenu de la leçon 12 [tranché R511 sur le bloc coranique de p.87]&nbsp; ; les āyāt 1 à 44 du cache, livrées en les leçons 1 à 12, et les āyāt de la leçon suivante [cache 47-49], sont interdites de double rendu.</dd>
</dl>
<h2>Les objectifs de la leçon</h2>
<ol>
<li>Reconnaître la vérité de la duniyā, à travers l’exemple frappé dans l’āya.</li>
<li>Saisir l’importance des œuvres qui persistent, et leur mérite.</li>
<li>Ressentir la grandeur de la récompense de l’āḫira, et fortifier mon désir de ce qui est auprès de Dieu.</li>
</ol>
<h3>Le tamhīd</h3>
<p>Après que les āyāt précédentes ont exposé le débat qui courut entre le propriétaire des deux ǧannāt et son compagnon croyant, ce que le croyant avança de preuves et de rappel des bienfaits de Dieu, et l’avertissement de la ruine de l’injustice et de l’issue de l’orgueil, les āyāt de ce cours passèrent à une nouvelle frappe d’exemple, pour expliquer l’état de la duniyā, la promptitude de sa disparition, et la décrépitude de ses délices et de ses jouissances.</p>
<p>Quelle est donc la vérité de la duniyā&nbsp; ? Et quelle est la convenance de l’exemple frappé avec le récit du propriétaire des deux ǧannāt&nbsp; ?</p>
<h2>Le commentaire</h2>
<h3>La glose</h3>
<p>En le glosatoire du manuel&nbsp; : «&nbsp;se mélangea&nbsp;»&nbsp; : s’entremêla. «&nbsp;la végétation&nbsp;»&nbsp; : le poussement. «&nbsp;qu’Elle disperse&nbsp;»&nbsp; : le vent l’emporte et l’éparpille dans l’air [fragments imprimés altérés, déclarés].</p>
<h3>L’extraction des thèmes des āyāt</h3>
<p>Quel est l’exemple que Dieu — Très-Haut — frappa pour la vérité de la duniyā&nbsp; ?</p>
<p>Ces deux āyāt contiennent ce qui suit.</p>
<h3>Premièrement&nbsp; : l’exemple frappé de la vérité de la duniyā</h3>
<p>Sa parole, Très-Haut&nbsp; : «&nbsp;{v(45)} (45)&nbsp;»</p>
<p>C’est un autre exemple que Dieu — Très-Haut — frappa en cette sourate, après le récit des deux hommes auxquels Dieu avait donné à l’un des deux deux ǧannāt, et ce qui courut entre eux deux de débat, et comment s’acheva l’issue de l’ébloui par l’éclat de la duniyā et son ornement — en la perdition. Et en cet exemple&nbsp; : l’explication de la vérité de la duniyā qui poussa le propriétaire des deux ǧannāt au dédain et au déni — il fut donc un exemple pour l’homme ingrat. Et cette āya vint de plus assimiler la vie d’ici-bas en la promptitude de sa décrépitude et de sa disparition, par ce qui advient chaque année&nbsp; : la descente de la pluie et le verdissement de la terre, puis la conversion de sa végétation, après l’éclat et la joie, en fourrage effrité et débris.</p>
<p>Et «&nbsp;d’une eau&nbsp;»&nbsp; : il veut par cela «&nbsp;une eau&nbsp;» — et «&nbsp;du ciel&nbsp;»&nbsp; : c’est-à-dire de la nuée qui est au ciel [fragment imprimé altéré, déclaré] — et le terme de lieu y fut employé au sens du terme de circonstance.</p>
<p>Et «&nbsp;se mélange&nbsp;»&nbsp; : c’est-à-dire que la végétation se mêla, une part à une part.</p>
<p>Et la lettre de liaison en «&nbsp;...&nbsp;» est une lettre de causalité — l’expression dénote son passage [à l’herbe] par son effet [fragment imprimé altéré, déclaré].</p>
<p>Et «&nbsp;devient&nbsp;»&nbsp; : cela veut dire la spécialisation du moment du matin — c’est-à-dire&nbsp; : il devint, par la cessation de l’eau sur lui, un fourrage effrité. Et «&nbsp;le fourrage effrité&nbsp;»&nbsp; : le fritté et le brisé. Et «&nbsp;l’effritement&nbsp;»&nbsp; : la mouture de la chose sèche — dont l’émiettement du bouilli — et par cela fut nommé Hāšim b. ʿAbd Manāf, le ʿArabe de Qurayš, l’aïeul du Prophète — que la bénédiction et la paix de Dieu soient sur lui — et son nom est ʿAmr&nbsp; ; parce qu’il fut le premier à émietter le bouilli pour sa gens et pour les gens de la saison, en l’an de la famine.</p>
<p>Et les lectures alternent sur la lexie de la dispersion — et Ibn ʿAbbās l’a lue autrement [fragment imprimé altéré, déclaré]&nbsp; : le sens serait qu’Elle la broie et la lance.</p>
<p>Et «&nbsp;Dieu demeure&nbsp;»&nbsp; : une information que l’ordre fut ainsi, avant l’existence de l’homme — l’intellect de chacun en juge par son état — c’est le dire de Sībawayhi, et c’est un sens juste. Et al-Ḥasan a dit&nbsp; : «&nbsp;demeure&nbsp;» est une information sur l’état, avant la création des existants — c’est-à-dire&nbsp; : la puissance était. Et cela aussi est juste. Et le sens de «&nbsp;sans déclin&nbsp;»&nbsp; : le Puissant, le Créateur — Celui que rien ne contraint.</p>
<p>Et le sens de cette interprétation&nbsp; : l’assimilation de l’état de l’homme en sa vie, son bien, sa gloire, sa joie et son dédain, à la végétation qui gagna verdissement et éclat de la pluie descendante, puis redevint ensuite fourrage effrité et parvint au néant. Quiconque eut donc œuvre pure demeure en l’āḫira — il est le gagnant&nbsp; ; la vie fut comme l’eau, et le verdissement et l’éclat à la place des délices et de la gloire, et semblable.</p>
<h3>Deuxièmement&nbsp; : les biens et les enfants — l’ornement de la vie de ce monde</h3>
<p>Sa parole, Très-Haut&nbsp; : «&nbsp;{v(46)} (46)&nbsp;»</p>
<p>Dieu confirma Son Prophète — de l’accomplissement de l’exemple qu’Il avait amorcé en le fil du discours — le mérite, la rétribution, la belle espérance. C’est-à-dire&nbsp; : les biens et les enfants ne sont que l’ornement de cette vie humiliée — que vos âmes ne les poursuivent point. Et les biens et les enfants ne furent ornement de la vie d’ici-bas que parce qu’il y a dans le bien la beauté et l’effusion, et dans les enfants la force et la défense — ils furent donc tous deux l’ornement de la vie.</p>
<p>Et «&nbsp;l’ornement&nbsp;»&nbsp; : un nom verbal, et il en fit information sur des personnes — soit que cela se tienne sur un énoncé omis, son énoncé&nbsp; : [un ornement] établi de la vie d’ici-bas&nbsp; ; soit que nous mettions les biens et les enfants à la place de la richesse et de la multitude. [fragments imprimés altérés, déclarés]</p>
<p>Et l’on a divergé en «&nbsp;les œuvres qui persistent&nbsp;»&nbsp; : Ibn ʿAbbās, Ibn Ǧubayr, Abū ʿAmr, ʿAmr b. Mayšara et ʿAmr b. Šurayḥbīl ont dit&nbsp; : ce sont les cinq prières — et l’ʾimām Ibn al-ʿArabī l’a préféré en ses ʾaḥkām et a dit&nbsp; : «&nbsp;et c’est vers cela que va mon penchant&nbsp; ; et il n’est point en ce chapitre de ḥadīṯ juste&nbsp; ; or le mérite de la louange, de la magnification, de l’unification et de la formule de puissance est notoire en le Ṣaḥīḥ — et rien ne vaut les cinq prières à cet égard, ni par compte ni par estimation. Et Dieu est plus savant&nbsp;». [Aḥkām al-Qurʾān&nbsp; : 5/632 — chiffre imprimé tranché]</p>
<p>Et la masse a dit&nbsp; : ce sont les paroles transmises de mérite&nbsp; : Gloire à Dieu&nbsp; ; la louange à Dieu&nbsp; ; point de dieu que Dieu&nbsp; ; Dieu est plus grand&nbsp; ; il n’est de force ni de puissance qu’en Dieu, le Très-Haut, l’Immense — et il est rapporté en ce chapitre le ḥadīṯ&nbsp; : «&nbsp;Multipliez les œuvres qui persistent&nbsp;».</p>
<p>Et il est rapporté du Messager de Dieu — que la bénédiction et la paix de Dieu soient sur lui — par la voie d’Abū Hurayra — que Dieu l’agrée — et d’autres, que ces paroles sont les œuvres qui persistent. [Ṣaḥīḥ Ibn Ḥibbān&nbsp; ; Sunan an-Nasāʾī al-Kubrā, Kitāb de l’œuvre du jour et de la nuit — renvois imprimés altérés, déclarés]</p>
<p>Et Ibn ʿAbbās a dit&nbsp; : les œuvres qui persistent — toute œuvre pure, de propos ou d’acte, qui demeure pour l’āḫira — et al-Ṭabarī l’a préféré, et al-Qurṭubī l’a confirmé.</p>
<p>Et «&nbsp;la belle espérance&nbsp;»&nbsp; : c’est-à-dire l’espérance — car son détenteur espère, en la duniyā, la récompense de Dieu et sa part en l’āḫira. Et l’on dit&nbsp; : la meilleure rétribution [fragment imprimé altéré, déclaré] — la vérification, au-delà de ce que les ignorants en supposent.</p>
<h2>Les subtilités et les bienfaits</h2>
<p>En Sa parole — «&nbsp;Les biens et les enfants sont l’ornement de la vie de ce monde&nbsp;» — la réunion des deux termes sous un seul jugement est de la balāġa des ʿArabes [fragment imprimé altéré, déclaré]&nbsp; : le rassemblement rhétorique — le locuteur rassemble deux choses ou plus sous un seul jugement — et son contraire est la disjonction&nbsp; : séparer deux choses d’une même espèce en leurs jugements — comme en [renvoi imprimé altéré, déclaré].</p>
<p>Abū Bakr Ibn al-ʿArabī a dit — que Dieu lui fasse miséricorde — en la lexie des œuvres qui persistent&nbsp; : «&nbsp;Les principes, au Livre de Dieu&nbsp; : tout existant, hormis Dieu et Ses attributs sublimes, a un terme — tout existant hormis Dieu a un terme, et tout ce qui n’a point de terme — la ǧanna et ses gens, et l’orgueilleux? et les gens du Feu — et Celui qui demeure en vérité, c’est Dieu seul. Les œuvres donc, belles et laides, bonnes et mauvaises, sont périssables et se renouvellent — et les œuvres furent qualifiées de persistance de façon figurée, et la récompense et le châtiment demeurent sans interruption&nbsp; ; et «&nbsp;la belle espérance&nbsp;»&nbsp; : ce sont les délices — elles ne sont que des buts — qualifiées de persistance en ce sens que leurs semblables se succèdent sans interruption&nbsp;». [Aḥkām al-Qurʾān — renvois imprimés 332 et 432, chiffres partiellement altérés, déclarés]</p>
<p>Et l’ʾimām al-Qurṭubī a dit — que Dieu lui fasse miséricorde&nbsp; : «&nbsp;Les sages ont dit&nbsp; : Dieu assimila la duniyā à l’eau, car l’eau ne s’établit point en un lieu — ainsi la duniyā ne demeure point en un état&nbsp; ; et l’eau ne se tient point en un état unique — ainsi la duniyā&nbsp; ; et l’eau ne demeure point et s’en va — ainsi la duniyā périt&nbsp; ; et nul ne peut pénétrer l’eau sans s’y noyer — ainsi nul n’échappe qui entre dans la duniyā à ses épreuves et ses fléaux&nbsp; ; et l’eau, à la mesure juste, est profitable en germination — et passée la mesure, elle est nuisible et perditrice — ainsi la duniyā&nbsp; : la suffisance d’elle profite, et son excès nuit&nbsp;». [al-Ǧāmiʿ li-aḥkām al-Qurʾān&nbsp; : renvoi imprimé 862 — chiffre altéré, tranché]</p>
<h2>L’évaluation</h2>
<ol>
<li>Quelle est la convenance de l’exemple frappé dans l’āya avec le récit du propriétaire des deux ǧannāt&nbsp; ?</li>
<li>Par quoi Ibn ʿAbbās — que Dieu soit satisfait d’eux deux — interpréta-t-il [la lexie des œuvres qui persistent]&nbsp; ? Et quel est le guidage principiel de cette exégèse [fragments imprimés altérés, déclarés]&nbsp; ?</li>
<li>Pourquoi Dieu — Très-Haut — assimila-t-il la vie d’ici-bas à l’eau&nbsp; ?</li>
</ol>
<h2>L’exploitation</h2>
<p>L’exploitation imprimée porte l’orientation d’Ibn ʿĀšūr — que Dieu lui fasse miséricorde — en les lexies des biens et des enfants&nbsp; : les deux termes sont unis en un propos descriptif, sauf que la majorité de leurs occurrences exige un terme omis [passage imprimé altéré, déclaré en son entier]. Je contemple le texte, puis je réponds&nbsp; :</p>
<ol>
<li>Je cite un exemple du Noble Qurʾān où la description par «&nbsp;les œuvres&nbsp;» tient lieu de son décrit [fragment imprimé altéré, déclaré].</li>
<li>Quelle est la justification qu’Ibn ʿĀšūr — que Dieu lui fasse miséricorde — a donnée pour l’antéposition de la description «&nbsp;des œuvres qui persistent&nbsp;» sur la description de la seconde lexie [fragment imprimé altéré, déclaré]&nbsp; ?</li>
<li>Quelle est la sagesse qu’il a donnée à l’antéposition des biens sur les enfants&nbsp; ?</li>
</ol>
<p>La préparation préalable porte la révision de l’exégèse des āyāt 46-48 de sūrat al-Kahf [de l’imprimé — āyāt 47-49 du cache canonique&nbsp; ; consignes imprimées altérées, déclarées] et la réponse à ce qui suit&nbsp; : quelles sont les lectures venues en l’une des lexies de la parole divine [fragment imprimé altéré, déclaré]&nbsp; ? et qu’est-ce que l’ʾiʿrāb de la lexie demandée [fragment imprimé altéré, déclaré]&nbsp; ? et je cherche les sens des expressions suivantes, et j’en choisis les plus notables [fragment imprimé altéré, déclaré]. La leçon s’achève en la page imprimée 101&nbsp; ; la leçon suivante ouvre en la page 102 du même manuel — plage (46-48) à la grille du portail, rendue à sa livraison, précédent de la leçon 13 ici même. La borne de la leçon — p.96-101 — fut tranchée par le sondage textuel de la sonde&nbsp; : l’en-tête des objectifs du cours en p.102, aux objectifs «&nbsp;les scènes de la Résurrection&nbsp;» conformes au slot suivant — jamais devinée.</p>
"""

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(html)
print(f"OK {OUT} ({len(html)} car)")
