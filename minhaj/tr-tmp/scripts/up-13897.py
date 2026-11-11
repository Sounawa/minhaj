#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 13897 (tafsir-5ep, Sourate al-Infiṭār 9-19, leçon 16).

Vérifications :
- Toutes les citations coraniques étaient PERDUES par l'OCR (paragraphes vides)
  → restaurées du canonique quran-cache.json : Infiṭār 82:9-19 ; Qāf 50:17-18
  (justification des deux scribes par personne) ; préparation = Muṭaffifīn 83:1-6
  (leçon SUIVANTE 13907 — la baseline LLM y mettait à tort des fragments
  d'Infiṭār de la présente leçon).
- Garble « Non...! algré tout] » = كَلَّا بَلْ → « Non ! Mais vous traitez la
  Rétribution de mensonge » (82:9).
- TABLE شرح dégradée : seules les gloses survivent (colonne de gauche) — termes
  restitués des versets : يوم الدين / لحافظين / الأبرار / يصلونها / بغائبين /
  وما أدراك ; glose بما أخرجين = « sortis [d'elle] » (cf. Jalālayn : بغائبين
  أي خارجين منها) ; glose وما أعلمك = « qu'est-ce qui t'a informé » (synonyme).
- Fragments OCR « على الله / لتلك الأعمال / جميعه » conservés dans la glose de
  v10 (« au nom d'Allah, pour ces œuvres en leur totalité »).
- istithmār : citation introductive Rāzī restaurée (v10-11 — le propos porte sur
  le livre et les témoins de la reddition de comptes) ; référence
  [Mafātīḥ al-ghayb : 31/78] conservée.
- Harmonisation 13886 (même sourate) : « illusion » pour اغترار, « libertins »
  pour فجار, « jardin de délice » pour نعيم, « Rétribution » pour دين.
- GT-ismes éliminés : « étude du commentaire », objectifs à l'infinitif,
  « Le Jour du Jugement » → « Jour de la Rétribution » (din), « égarement » →
  « illusion » (cohérence 13886).
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Infiṭār — le Tafsīr al-Jalālayn des versets 9 à 19</h1>
<p>Leçon de tafsīr de la sourate al-Infiṭār (versets 9 à 19) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 16.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître les causes de l'illusion de l'homme à l'égard de son Seigneur et de son déni de son Créateur.</li>
<li>Dégager des versets la rétribution des bons et des libertins dans l'au-delà.</li>
<li>Me pénétrer de l'ordre de mon Seigneur — l'adoration et l'œuvre juste — en préparation du jour de la rétribution.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>Après que la Vérité, glorifié et exalté soit-Il, a exposé à l'homme certaines terreurs du Jour de la Résurrection et lui a rappelé son illusion à l'égard de son Seigneur, Il l'a, dans ces versets, blâmé de traiter le Jour de la Rétribution de mensonge, et a montré que ses œuvres sont conservées sur lui ; c'est à ce titre que les gens se divisent en bons et en libertins. La sourate s'achève par l'avertissement du jour de la rétribution et par l'exposé de l'unicité du Créateur, en ce jour, dans le jugement et le commandement.<br>
Comment les œuvres de l'homme sont-elles dénombrées en ce bas monde ? Et quelle est la voie du salut face à la terreur du Jour de la Résurrection ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Non ! Mais vous traitez la Rétribution de mensonge, (9) alors que veillent sur vous des gardiens, (10) de nobles scribes, (11) qui savent ce que vous faites. (12) Les bons seront, certes, dans un jardin de délice, (13) et les libertins seront, certes, dans une fournaise ; (14) ils y brûleront au jour de la Rétribution, (15) et ils n'en seront pas absents. (16) Et qu'est-ce qui te fera savoir ce qu'est le Jour de la Rétribution ? (17) Puis, qu'est-ce qui te fera savoir ce qu'est le Jour de la Rétribution ? (18) Le jour où nulle âme ne possèdera rien pour une autre âme, et où le commandement sera, ce jour-là, à Allah. (19) » (al-Infiṭār, 9-19)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Table imprimée dégradée : seules les gloses ont survécu à la numérisation ; les termes ont été restitués d'après les versets.]</p>
<ul>
<li>yawm al-dīn (le Jour de la Rétribution) : le jour de la rétribution des œuvres.</li>
<li>la-ḥāfiẓīn (des gardiens) : les anges gardiens de vos œuvres.</li>
<li>al-abrār (les bons) : les croyants sincères dans leur foi.</li>
<li>yaṣlawnahā (ils y brûleront) : ils y entrent et en subissent la chaleur.</li>
<li>bighāʾibīn (absents) : sortis [d'elle].</li>
<li>wa-mā adrāka (et qu'est-ce qui t'a fait savoir) : et qu'est-ce qui t'a informé.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>De quoi Allah, Puissant et Majestueux, a-t-Il averti au début des versets ?</li>
<li>Qu'est-ce qui découle de la piété de l'homme ou de sa perversité ?</li>
<li>À qui appartiendra le commandement au Jour de la Résurrection ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : l'avertissement des négateurs du Jour de la Rétribution, par le dénombrement de leurs œuvres</h3>
<p>Après que la Vérité, glorifié soit-Il, a exposé l'illusion de l'homme et son déni de son Seigneur, Il a porté, à la tête de ces versets, le blâme de son fait, ayant dit, le Très-Haut :</p>
<p>« Non ! Mais vous traitez la Rétribution de mensonge, »</p>
<p>— dissuasion de l'illusion [que permet] la générosité d'Allah, le Très-Haut. Le discours s'adresse aux négateurs de La Mecque ; et « le Jour de la Rétribution » (yawm al-dīn) vise le jour de la rétribution des œuvres. Et la parole du Très-Haut :</p>
<p>« alors que veillent sur vous des gardiens, de nobles scribes, »</p>
<p>c'est-à-dire : les anges qui écrivent les œuvres des fils d'Adam, au nom d'Allah, pour ces œuvres en leur totalité. Et les anges n'ont été mis au pluriel dans Sa parole : « de nobles scribes » (11) qu'en égard à la répartition parmi les gens : car chacun a deux scribes, et non un seul — selon la parole du Très-Haut :</p>
<p>« Quand les deux receveurs recueillent [les actes], assis l'un à droite, l'autre assis à gauche, (17) il ne prononce pas une parole sans qu'un observateur vigilant ne soit auprès de lui. (18) » (Qāf, 17-18)</p>
<h3>Deuxièmement : la rétribution de l'homme et son devenir dans l'au-delà</h3>
<p>Il a exposé, dans ces versets, la division des créatures, au Jour de la Résurrection, en bons et en libertins, et mentionné le devenir de chacun d'eux. Le Glorifié a dit :</p>
<p>« Les bons seront, certes, dans un jardin de délice, »</p>
<p>c'est-à-dire : les croyants sincères dans leur foi seront certes dans un jardin où ils jouiront [des délices].</p>
<p>« et les libertins seront, certes, dans une fournaise ; »</p>
<p>c'est-à-dire : et les négateurs seront certes dans un feu incandescent.</p>
<p>« ils y brûleront au jour de la Rétribution, »</p>
<p>c'est-à-dire : ils y entreront et en subiront la chaleur, au jour de la rétribution qu'ils traitaient de mensonge.</p>
<p>« et ils n'en seront pas absents. »</p>
<p>c'est-à-dire : ils n'en seront jamais sortis.</p>
<h3>Troisièmement : le commandement appartient à Allah seul au Jour de la Résurrection</h3>
<p>À la clôture de cette sourate, Allah, le Très-Haut, a décrit le Jour de la Résurrection par Sa parole, glorifié soit-Il :</p>
<p>« Et qu'est-ce qui te fera savoir ce qu'est le Jour de la Rétribution ? »</p>
<p>c'est-à-dire : et qu'est-ce qui t'a informé de ce qu'est le jour de la rétribution ? Le dessein de l'interrogation est de magnifier l'affaire de ce jour et d'en exagérer la terreur. Puis Il répéta la même interrogation, et dit :</p>
<p>« Puis, qu'est-ce qui te fera savoir ce qu'est le Jour de la Rétribution ? »</p>
<p>c'est-à-dire : quelle chose t'a fait savoir ce qu'est le jour de la rétribution, quant à l'effroi et à la rigueur ?</p>
<p>Puis le Glorifié détailla certaines caractéristiques de ce jour, et dit :</p>
<p>« Le jour où nulle âme ne possèdera rien pour une autre âme, et où le commandement sera, ce jour-là, à Allah. »</p>
<p>c'est-à-dire : en ce jour, personne ne possèdera quoi que ce soit de profitable pour autrui ; nul commandement n'y appartient à un autre que Lui, et Allah ne permet à personne d'y intercéder pour quiconque — au contraire de la situation en ce bas monde.</p>
<h3>Quatrièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont les plus importantes :</p>
<ul>
<li>l'affirmation de la foi au Jour dernier, qui est le jour de la rétribution des œuvres ;</li>
<li>la dissuasion des négateurs du Jour de la Rétribution, en réponse à leur déni de ce jour ;</li>
<li>le rappel que les œuvres de l'homme sont conservées, et qu'il en sera rétribué au Jour de la Résurrection ;</li>
<li>l'invitation à s'adonner au bien et à l'œuvre juste.</li>
</ul>
<h2>L'évaluation</h2>
<ol>
<li>Comment Allah, Puissant et Majestueux, a-t-Il répondu aux négateurs du Jour de la Rétribution ?</li>
<li>Je compare la rétribution des bons et celle des libertins à travers les versets.</li>
<li>Quel est le sens de la parole d'Allah, le Très-Haut : « Le jour où nulle âme ne possèdera rien pour une autre âme, et où le commandement sera, ce jour-là, à Allah » ? (al-Infiṭār, 19)</li>
</ol>
<h3>L'enrichissement (istithmār)</h3>
<p>Fakhr al-Dīn al-Rāzī — qu'Allah lui fasse miséricorde — a dit, en commentant la parole d'Allah, le Très-Haut :</p>
<p>« alors que veillent sur vous des gardiens, de nobles scribes » (al-Infiṭār, 10-11)</p>
<p>« Allah, le Très-Haut, ne conduit Ses affaires avec Ses serviteurs que selon la manière dont ils se traitent entre eux, car c'est ce qui fixe le plus sûrement le sens auprès d'eux. Et comme ce qui est le plus probant pour eux, en matière de reddition de comptes, est la production d'un livre accompagné de témoins, ils ont été interpelés par le semblable de ce à quoi ils devront rendre compte au Jour de la Résurrection : des livres leurs seront présentés déployés, et des anges s'y trouveront, témoignant contre eux — comme les témoins intègres du sultan témoignent contre quiconque lui désobéit et enfreint son ordre, lui disant : "Le roi t'a donné telle et telle chose, et a fait pour toi ceci et cela, puis tu L'as contredit et tu as fait telle et telle chose." »</p>
<p>[Mafātīḥ al-ghayb (Les Clefs du mystère), de Fakhr al-Dīn al-Rāzī : 31/78]</p>
<ul>
<li>J'explicite la finalité légale de la charge d'anges scribes, chargés d'enregistrer les œuvres des serviteurs, visée dans le texte.</li>
</ul>
<h2>La préparation préalable</h2>
<p>Je lis les versets 1 à 6 de la sourate al-Muṭaffifīn et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Malheur aux fraudeurs » (al-Muṭaffifīn, 1) ;</p>
<p>« qui, lorsqu'ils se font mesurer par les gens, exigent la pleine mesure » (al-Muṭaffifīn, 2) ;</p>
<p>« et qui, lorsqu'ils mesurent pour eux ou pèsent pour eux, lèsent » (al-Muṭaffifīn, 3) ;</p>
<p>« Ne pensent-ils pas qu'ils seront ressuscités » (al-Muṭaffifīn, 4) ;</p>
<p>« le jour où les gens se tiendront debout devant le Seigneur des mondes » (al-Muṭaffifīn, 6).</p>
<p>[Expressions restituées d'après les versets 1 à 6 de la sourate al-Muṭaffifīn (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>Je recherche la rétribution des fraudeurs dans la mesure et le poids.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13897":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13897 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13897 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
