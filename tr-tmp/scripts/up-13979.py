#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 13979 (tafsir-5ep, Sourate al-Inshiqāq 10-15, leçon 22).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : Inshiqāq 84:10-15 ; citation de corroboration =
  Ḥāqqah 69:25-29 (le manuel imprime « 24-29 » — v24 concerne les gens de la
  droite, la lamentation « yā thubūrāh » est v25-29 : convention cache en
  principal + note imprimée) ; istithmār = Ḥadīd 57:20 (le manuel imprime
  « 19 » — v20 est le verset du متاع الغرور, thème exact des questions ;
  même convention note imprimée) ; préparation = 84:16-25 (leçon SUIVANTE
  13983, déjà main — rendu harmonisé sur elle).
- TABLE شرح dégradée : gloses seules — termes restitués des versets (ثبورًا /
  سعيرًا / يحور / بصيرًا).
- Lecture qirāʾique de v12 conservée : yuṣallā (ḍamma du yāʾ, fatha du ṣād,
  lām redoublée — forme passive).
- Note grammaticale v14 conservée : أنْ légère de أنَّ, nom élidé (taqdīr
  أَنَّهُ) ; بَلَى répond à la négation.
- Gloss v10 : main droite ligotée à la nuque + contrepartie avec « بيمينه »
  restaurée.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Inshiqāq — le Tafsīr al-Jalālayn des versets 10 à 15</h1>
<p>Leçon de tafsīr de la sourate al-Inshiqāq (versets 10 à 15) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 22.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître la rétribution des négateurs et des auteurs de fautes au Jour de la Résurrection.</li>
<li>Dégager les causes de la persévérance dans la mécréance et la désobéissance.</li>
<li>Incarner les sens de la foi et de l'obéissance.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>Après que les versets précédents ont montré que l'homme rencontrera son œuvre — de bien ou de mal — et que les gens sont deux factions : une faction qui reçoit son livre en sa main droite — nous l'avons exposée dans la leçon précédente —, ces versets sont venus exposer la seconde faction : celle qui reçoit son livre derrière son dos.<br>
Qui est cette faction ? Et qu'est-ce qui l'a fait s'égarer du chemin ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Quant à celui qui recevra son livre derrière son dos, (10) il appellera bientôt la perdition [sur lui], (11) et il brûlera dans un feu ardent. (12) Il était, certes, parmi les siens, joyeux ; (13) il pensait qu'il ne retournerait jamais [vers Allah] ; (14) mais si ! Son Seigneur l'observait bien. (15) » (al-Inshiqāq, 10-15)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Table imprimée dégradée : seules les gloses ont survécu à la numérisation ; les termes ont été restitués d'après les versets.]</p>
<ul>
<li>thubūran (la perdition) : la perte [de soi].</li>
<li>saʿīran (un feu ardent) : le feu intense.</li>
<li>yaḥūra (retourner) : revenir.</li>
<li>baṣīran (observant) : connaissant.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>Comment sera le compte des gens de la mécréance et de la désobéissance dans l'au-delà ?</li>
<li>Quelle est la conséquence de la négation de la résurrection par l'homme ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la difficulté du compte des gens de la mécréance et de la désobéissance</h3>
<p>Après que la Vérité, glorifié soit-Il, a exposé la rétribution de celui qui reçoit son livre en sa main droite, Il l'a contrebalancée par la mention du devenir de celui qui reçoit son livre derrière son dos, et dit :</p>
<p>« Quant à celui qui recevra son livre derrière son dos, »</p>
<p>— c'est le négateur : sa main droite sera ligotée à sa nuque, et sa main gauche placée derrière son dos, et il prendra son livre avec elle — comme l'exige la contrepartie avec [« en sa main droite »].</p>
<p>« il appellera bientôt la perdition [sur lui] »</p>
<p>c'est-à-dire : il demandera la perte pour lui-même, lorsqu'il verra ce que renferme son livre, en disant : « Ô ma perdition (yā thubūrāh) ! » — et c'est ce qu'indique Sa parole, le Très-Haut :</p>
<p>« Quant à celui qui recevra son livre en sa main gauche, il dira : "Plût à Allah qu'on ne m'eût pas remis mon livre, (25) et que je n'eusse pas su mon compte ! (26) Plût au Ciel que cette [mort] eût été définitive ! (27) Ma fortune ne m'a servi à rien, (28) mon pouvoir m'a abandonné." (29) » (al-Ḥāqqah, 25-29 — le manuel imprime « 24-29 »)</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« et il brûlera dans un feu ardent. »</p>
<p>— lu (yuṣallā) avec ḍamma du yāʾ, fatha du ṣād et lām redoublée : c'est-à-dire, il entrera dans le feu intense, brûlera de sa flamme et subira la dureté de sa chaleur et de son ardeur.</p>
<h3>Deuxièmement : la cause du regret de l'homme dans l'au-delà</h3>
<p>Ces versets exposent les causes qui ont fait que l'homme emprunte la voie de la mécréance et de l'égarement, pour que son affaire aboutisse au regret et à la plainte. Allah, le Très-Haut, dit :</p>
<p>« Il était, certes, parmi les siens, joyeux ; »</p>
<p>c'est-à-dire : parce qu'il était, parmi les siens en ce bas monde, joyeux de suivre sa passion et oublieux des affaires de l'au-delà.</p>
<p>« il pensait qu'il ne retournerait jamais [vers Allah] ; »</p>
<p>c'est-à-dire : parce qu'il pensait qu'il ne retournerait pas à son Seigneur — car il traitait de mensonge la résurrection et le compte. Et [an] est la forme légère de la lourde, son nom étant élidé — c'est-à-dire : « qu'il [ne]... ».</p>
<p>Puis Allah lui répliqua par Sa parole :</p>
<p>« mais si ! » (balā)</p>
<p>— il répond à la négation : c'est-à-dire : mais oui — il retournera certes à son Seigneur, et il sera rétribué de son œuvre.</p>
<p>« Son Seigneur l'observait bien »</p>
<p>c'est-à-dire : connaissant son retour vers Lui.</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont les plus importantes :</p>
<ul>
<li>la joie en ce bas monde, qui mène à négliger les obligations légales, a pour rétribution le regret et la plainte dans l'au-delà ;</li>
<li>la négation de la résurrection pousse à commettre les désobéissances et les fautes ;</li>
<li>l'œuvre juste profite au serviteur lui-même, et à ceux qui l'entourent parmi les gens et l'univers entier.</li>
</ul>
<h2>L'évaluation</h2>
<ol>
<li>Pourquoi le négateur reçoit-il son livre derrière son dos ?</li>
<li>Quelles sont les causes du regret du négateur dans l'au-delà ?</li>
<li>Quelle est la réponse divine aux croyances corrompues des négateurs ?</li>
</ol>
<h3>L'enrichissement (istithmār)</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Sachez que la vie présente n'est qu'un jeu, une distraction, une parure, une vaine gloire entre vous, et une rivalité d'accroissement en biens et en enfants — telle une pluie dont la pousse émerveille les négateurs : puis elle sèche, et tu la vois jaunie, puis elle devient du chaume — et, dans l'au-delà, il y a un châtiment sévère, ainsi qu'un pardon d'Allah et un agrément ; et la vie présente n'est qu'une jouissance fallacieuse. » (al-Ḥadīd, 20 — le manuel imprime « 19 »)</p>
<ol>
<li>Pourquoi l'homme est-il illusionné par les plaisirs de la vie présente au point d'oublier l'au-delà ?</li>
<li>Quelle est la relation entre les œuvres de l'homme en ce bas monde et son devenir dans l'au-delà ?</li>
</ol>
<h2>La préparation préalable</h2>
<p>Je lis les versets 16 à 25 de la sourate al-Inshiqāq et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Non ! Je jure par le crépuscule » (al-Inshiqāq, 16) ;</p>
<p>« et par la nuit et ce qu'elle recueille » (al-Inshiqāq, 17) ;</p>
<p>« et par la lune lorsqu'elle se fait pleine » (al-Inshiqāq, 18) ;</p>
<p>« vous monterez, certes, d'un état à un autre état » (al-Inshiqāq, 19) ;</p>
<p>« Qu'ont-ils donc à ne pas croire » (al-Inshiqāq, 20) ;</p>
<p>« et, lorsque le Coran leur est récité, à ne pas se prosterner ? » (al-Inshiqāq, 21) ;</p>
<p>« Mais ceux qui ont mécru démentent » (al-Inshiqāq, 22) ;</p>
<p>« et Allah sait mieux ce qu'ils recueillent » (al-Inshiqāq, 23) ;</p>
<p>« Annonce-leur donc un châtiment douloureux » (al-Inshiqāq, 24) ;</p>
<p>« à l'exception de ceux qui croient et accomplissent les œuvres bonnes : à eux une récompense jamais interrompue » (al-Inshiqāq, 25).</p>
<p>[Expressions restituées d'après les versets 16 à 25 de la sourate al-Inshiqāq (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>Par quoi Allah, Puissant et Majestueux, a-t-Il menacé les négateurs de la résurrection ?</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13979":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13979 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13979 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
