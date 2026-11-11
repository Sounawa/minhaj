#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 13886 (tafsir-5ep, Sourate al-Infiṭār 1-8).

Conventions main (cf. 16711) :
- h1 « La sourate X — le Tafsīr al-Jalālayn des versets N à M ».
- Paragraphe d'ouverture : auteurs Jalāl al-Dīn al-Maḥallī (864 H) / Jalāl
  al-Dīn al-Suyūṭī (911 H), 5e année primaire traditionnel phase 2, leçon 15.
- « Objectifs de la leçon » en h2 + infinitifs.
- Versets : numérotation par verset (1)-(8) + référence (al-Infiṭār, 1-8).
- Qiyāma 13 RESTAURÉ canonique (le LLM confondait avec Infiṭār 5 :
  « L'homme sera, ce jour-là, informé de ce qu'il aura avancé et de ce
  qu'il aura remis » — cache يُنَبَّؤُا الْإِنسَانُ يَوْمَئِذٍ بِمَا قَدَّمَ وَأَخَّرَ).
- Préparation préalable : les 6 expressions vides du CMS restituées du
  canonique Infiṭār 9-14 (le LLM imprimait un fragment corrompu
  « Non...! algré tout] »).
- istithmār : تسويل = l'embellissement [du mal] (le LLM lisait « suave ») ;
  سُتُورُكَ الْمُرْخَاةُ = « Tes voiles déployés » (le LLM : « larges portes »).
- اغترار rendu « illusion » partout (cohérence avec l'objectif 2).
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Infiṭār — le Tafsīr al-Jalālayn des versets 1 à 8</h1>
<p>Leçon de tafsīr de la sourate al-Infiṭār (versets 1 à 8) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 15.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître certains signes précurseurs et certaines terreurs du Jour de la Résurrection.</li>
<li>Dégager des versets l'illusion de l'homme à l'égard de son Seigneur et son insouciance de l'au-delà.</li>
<li>Prendre conscience des nombreuses faveurs d'Allah envers moi, et Lui répondre par la gratitude et l'obéissance.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>La sourate al-Infiṭār est mecquoise et compte dix-neuf versets. Elle a apporté les annonces de la résurrection et des terreurs qui la précèdent ; elle a invité les associateurs à considérer les affaires qui les ont détournés de la reconnaissance de l'unicité d'Allah, et à méditer les preuves de la survenue de la résurrection et de la rétribution ; elle a enfin rappelé aux croyants que les œuvres sont dénombrées et qu'ils en seront rétribués.<br>
Quelles sont les marques précurseurs du Jour de la Résurrection ? Et quelle est la voie du salut face aux terreurs de ce Jour ?</p>
<h2>Les versets</h2>
<p>« Quand le ciel se fendra, (1) et que les étoiles se disperseront, (2) et que les mers seront faites jaillir, (3) et que les tombeaux seront éventrés, (4) toute âme saura alors ce qu'elle aura avancé et ce qu'elle aura remis. (5) Ô homme ! Qu'est-ce qui t'a illusionné au sujet de ton Seigneur, le Noble, (6) qui t'a créé, puis formé et constitué harmonieusement, (7) te composant en la forme qu'Il a voulue ! (8) » (al-Infiṭār, 1-8)</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<ul>
<li>infaṭarat (se fendra) : se déchirera.</li>
<li>intatharat (se disperseront) : s'effondreront et tomberont éparses.</li>
<li>fujjirat (seront faites jaillir) : l'une sera ouverte vers une autre, et elles deviendront une seule mer.</li>
<li>buʿthirat (seront éventrés) : leur terre sera retournée et leurs morts ressuscités.</li>
<li>gharraka (t'a illusionné) : t'a trompé et t'a porté à désobéir à Allah.</li>
<li>sawwāka (t'a formé) : t'a fait droit de constitution, indemne de tout défaut dans les membres.</li>
<li>ʿadalaka (t'a constitué harmonieusement) : t'a fait de constitution équilibrée, aux membres proportionnés.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>De quoi Allah, Puissant et Majestueux, nous a-t-Il rappelés à l'ouverture de cette sourate ?</li>
<li>En quoi Allah, le Très-Haut, a-t-Il blâmé l'homme dans ces versets ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : certains signes précurseurs du Jour de la Résurrection</h3>
<p>L'ouverture de cette sourate comporte le rappel de certains signes précurseurs du Jour de la Résurrection et des terreurs qu'il renferme. Allah, le Très-Haut, a dit :</p>
<p>« Quand le ciel se fendra, »</p>
<p>c'est-à-dire : le ciel se déchirera.</p>
<p>« et que les étoiles se disperseront, »</p>
<p>c'est-à-dire : elles s'effondreront et tomberont éparses.</p>
<p>« et que les mers seront faites jaillir, »</p>
<p>c'est-à-dire : l'une sera ouverte vers une autre, et l'eau douce se mêlera à l'eau salée.</p>
<p>« et que les tombeaux seront éventrés. »</p>
<p>c'est-à-dire : la terre des tombeaux sera retournée et leurs morts ressuscités.</p>
<p>Et la réponse [aux « Quand… »] et à ce qui leur est coordonné est Sa parole, le Très-Haut :</p>
<p>« toute âme saura alors ce qu'elle aura avancé et ce qu'elle aura remis »</p>
<p>c'est-à-dire : toute âme connaîtra le moment de ces événements mentionnés, qui est le Jour de la Résurrection ; « ce qu'elle aura avancé » : d'œuvres, « et ce qu'elle aura remis » d'elles, sans les avoir accomplies. « Le sens de l'avance (taqdīm) est l'empressement à l'œuvre, et le sens du remis (taʾkhīr) est son contraire, à savoir l'abandon de l'œuvre… » — et de même Sa parole, le Très-Haut :</p>
<p>« L'homme sera, ce jour-là, informé de ce qu'il aura avancé et de ce qu'il aura remis. » (al-Qiyāma, 13)</p>
<p>[al-Taḥrīr wa-l-Tanwīr, de al-Ṭāhir ibn ʿĀshūr : 30/173]</p>
<h3>Deuxièmement : l'illusion de l'homme à l'égard de son Seigneur</h3>
<p>Ces versets sont venus adresser un blâme à cet homme pour son illusion et son déni de son Seigneur, malgré les nombreuses faveurs qu'Il a répandues sur lui. Allah, le Très-Haut, a dit :</p>
<p>« Ô homme ! Qu'est-ce qui t'a illusionné au sujet de ton Seigneur, le Noble, »</p>
<p>— c'est un discours adressé aux négateurs de la résurrection.</p>
<p>« Qu'est-ce qui t'a illusionné »</p>
<p>c'est-à-dire : qu'est-ce qui t'a donné l'audace envers Allah, le Très-Haut, au point de Lui désobéir,</p>
<p>« qui t'a créé, puis formé »</p>
<p>c'est-à-dire : Il t'a fait droit de constitution, indemne de tout défaut dans les membres.</p>
<p>« et constitué harmonieusement »</p>
<p>— lu avec allègement et renforcement (takhfīf et tashdīd) : Il t'a fait de constitution équilibrée, aux membres proportionnés : tu n'as ni main ni pied plus long que l'autre.</p>
<p>« te composant en la forme qu'Il a voulue ! »</p>
<p>c'est-à-dire : Il t'a composé en quelque forme qu'Il a voulue — et [« qu'Il a voulue »] est un relatif : le sens est qu'Allah, le Très-Haut, t'a composé en la plus belle des formes, selon Sa parole, le Très-Haut :</p>
<p>« Nous avons certes créé l'homme dans la plus belle constitution. » (al-Tīn, 4)</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont les plus importantes :</p>
<ul>
<li>rappeler à l'homme les terreurs de la Résurrection, afin qu'il soit en préparation constante pour cet immense Jour ;</li>
<li>informer l'homme qu'il sera rétribué des œuvres qu'il aura avancées et remises ;</li>
<li>éveiller l'homme à son déni de son Seigneur, et lui rappeler les faveurs d'Allah, Puissant et Majestueux, envers lui ;</li>
<li>la puissance d'Allah sur la création, la mort et l'anéantissement du monde.</li>
</ul>
<h2>L'évaluation</h2>
<ul>
<li>Quelles sont les marques de l'avènement de l'Heure mentionnées dans les versets ?</li>
<li>Quel est le sens de la parole d'Allah, Puissant et Majestueux :</li>
</ul>
<p>« Ô homme ! Qu'est-ce qui t'a illusionné au sujet de ton Seigneur, le Noble ? » (al-Infiṭār, 6)</p>
<ul>
<li>Pourquoi Allah, Puissant et Majestueux, a-t-Il blâmé l'homme pour son déni de son Seigneur ?</li>
</ul>
<h3>L'enrichissement (istithmār)</h3>
<p>Les exégètes ont mentionné, au sujet de la cause de l'illusion de l'homme, plusieurs aspects : « L'un d'eux : Qatāda a dit : la cause de l'illusion du fils d'Adam est l'embellissement [du mal] par le Diable. Le deuxième : al-Ḥasan a dit : l'ont illusionné sa sottise et son ignorance. Le troisième : Muqātil a dit : l'a illusionné la clémence d'Allah envers lui, lorsqu'Il ne l'a pas châti au début de son affaire. Et on demanda à al-Fuḍayl ibn ʿIyāḍ : "Lorsqu'Allah te fera comparaître au Jour de la Résurrection et te dira : Qu'est-ce qui t'a illusionné au sujet de ton Seigneur, le Noble ?, que répondras-tu ?" Il répondit : "Je dirai : m'ont illusionné Tes voiles déployés." »</p>
<p>[Mafātīḥ al-ghayb (Les Clefs du mystère), de Fakhr al-Dīn al-Rāzī : 31/75]</p>
<ol>
<li>Les causes de l'illusion mentionnées dans le texte justifient-elles le déni et l'ingratitude de l'homme ? Et pourquoi ?</li>
<li>Comment l'homme devrait-il répondre aux faveurs d'Allah envers lui ?</li>
</ol>
<h2>La préparation préalable</h2>
<p>Je lis les versets 9 à 19 de la sourate al-Infiṭār et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Non ! Vous traitez la Rétribution de mensonge » (al-Infiṭār, 9) ;</p>
<p>« alors que veillent sur vous des gardiens » (al-Infiṭār, 10) ;</p>
<p>« de nobles scribes » (al-Infiṭār, 11) ;</p>
<p>« qui savent ce que vous faites » (al-Infiṭār, 12) ;</p>
<p>« Les bons seront, certes, dans un jardin de délice » (al-Infiṭār, 13) ;</p>
<p>« et les libertins seront, certes, dans une fournaise » (al-Infiṭār, 14).</p>
<ul>
<li>Je compare la rétribution des gens de bien et celle des pervers dans l'au-delà.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13886":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13886 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13886 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
