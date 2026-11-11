#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12987 (hadith-1es, les règles de
l'oubli dans la prière — suite — Muwaṭṭaʾ n° 254/258/260/261/263/265 +
Muslim + Bukhārī + Nasāʾī + Ibn Khuzayma).

Conventions main (cf. 12875-12986 du même livre) :
- h1 « Les règles de l'oubli dans la prière — suite (aḥkām al-sahw fī
  l-ṣalāh — tamām) », 22e leçon, 2e partie et suite de la 1ʳᵉ.
- Préambule : Muwaṭṭaʾ 265 (Abū Hurayra : « Satan vient à lui et
  l'embrouille... qu'il se prosterne de deux prosternations, assis »).
- Hadiths : 254 (Zayd b. Aslam/ʿAṭāʾ b. Yasār : doute 3 ou 4 → une
  rakʿa + 2 prosternations AVANT le salut ; 5e → shaffaʿahā ; 4e →
  targhīm de Satan) ; 258 (Ibn Shihāb/al-Aʿraj/ʿAbd Allāh b. Buḥayna :
  2 rakʿas, se leva sans s'asseoir, acheva, 2 prosternations avant le
  salut) ; 260 (Yaḥyā/Mālik : levé après l'achèvement, se souvint au
  rukūʿ → revient, s'assied, sans prosternation ; s'il s'est prosterné
  d'une, ne fait pas l'autre ; puis 2 prosternations APRÈS le salut).
- Lexique : shaffaʿahā (al-Bājī : la prière bâtie sur la parité),
  targhīm (courroux et abaissement), qaḍā ṣalātahu, naẋarnā
  taslīmahu.
- Taḥlīl I : certitude vs prépondérant — Mālik/Shāfiʿī/Thawrī
  (certitude ; Muslim « rejette le doute et bâtis sur le certain »)
  vs Nakhaʿī/Abū Ḥanīfa/Awzāʿī (taḥarrī = prépondérant, preuve Ibn
  Masʿūd Bukhārī « recherche le juste et achève dessus » ; réponse
  mālikite : taḥarrī = viser le juste, retour au certain — Nasāʾī
  « que nul ne choisisse de prier au lever/coucher ») ; mustankiḥ
  (l'obsédé du doute : prosternation seule, 265) ; avant/après le
  salut : mashhūra = après (pure addition possible) + 2 réponses
  (salut du tashahhud — targhīm valable après l'achèvement ;
  prosternations de la rakʿa anti-doute ≠ prosternations de sahw).
- Taḥlīl II : Ibn Buḥayna — 6 règles : ne pas revenir à l'assise
  (Ibn Khuzayma « ils glorifièrent et il poursuivit » ; retour après
  station droite : valide au jumhūr/Mālik, invalide au Shāfiʿī) ;
  premier tashahhud = sunna ; prosternation du retranchement AVANT le
  salut ; 2 prosternations suffisent même répété ; prosternation
  propre à l'oubli (le volontaire ne se prosterne pas) ; le maʾmūm
  se prosterne avec l'imam (Ibn Ḥazm : consensus). Levé après
  l'achèvement : revenir en tout état, achever, 2 prosternations
  APRÈS le salut ; persistance = invalidation ; Ibn ʿAbd al-Barr
  (consensus : addition non-rappel = corruption) ; Ibn Masʿūd
  (Bukhārī : Ẓuhr à cinq, « j'oublie comme vous oubliez, quand
  j'oublie rappelez-le-moi »).
- Istimḥār : 261 (ʿAlqama b. Abī ʿAlqama/sa mère/ʿĀʾisha : le
  khumayṣa de Syrie d'Abū Jahm — « il faillit me tenter ») + 263
  (Abū Ṭalḥa : l'oiseau dubsī dans le jardin — « une tentation m'a
  atteint en ce bien ! » → aumône) + lexique (khumayṣa, yaftinunī,
  dubsī) + 3 questions.
- Préparation préalable : leçon SUIVANTE 12995 (vendredi —
  al-badna/al-dhikr/laghawt, glosses vérifiées sur le lexique de
  12995 même ; résumé des règles du vendredi).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Les règles de l’oubli dans la prière — suite (<em>aḥkām al-sahw fī l-ṣalāh — tamām</em>)</h1>
<p>Leçon sur les règles de l’oubli (<em>sahw</em>) dans la prière, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la vingt-deuxième leçon, deuxième partie et suite de la première.</p>
<ol>
<li>Connaître le statut de qui commit dans sa prière un oubli par addition ou par retranchement.</li>
<li>Distinguer le statut de l’oubli dans la prière selon l’addition et le retranchement.</li>
<li>Me conformer aux règles de l’oubli s’il se présente dans ma prière.</li>
</ol>
<h2>Préambule</h2>
<p>L’imam Mālik fit sortir dans le <em>Muwaṭṭaʾ</em>, d’après Abū Hurayra — que Dieu soit satisfait de lui —, que le Messager de Dieu — paix et bénédiction sur lui — dit : « Quand l’un de vous se met debout pour prier, Satan vient à lui et l’embrouille, au point qu’il ne sait combien il a prié. Quand l’un de vous trouve cela, qu’il se prosterne de deux prosternations, assis. » [Muwaṭṭaʾ, n° 265]</p>
<p>Quelle est la cause de l’oubli dans la prière ? Quel est son statut ? Et quelle est la différence entre l’oubli par addition et l’oubli par retranchement ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Zayd ibn Aslam, d’après ʿAṭāʾ ibn Yasār : « que le Messager de Dieu — paix et bénédiction sur lui — dit : Quand l’un de vous doute dans sa prière et ne sait combien il a prié — trois ou quatre —, qu’il prie une rakʿa et se prosterne de deux prosternations, assis, avant le salut : si la rakʿa qu’il pria était une cinquième, les deux prosternations la complètent paire (<em>shaffaʿahā</em>) ; et si elle était une quatrième, les deux prosternations sont une humiliation (<em>targhīm</em>) pour Satan. » [Muwaṭṭaʾ, n° 254]</li>
<li>D’après Mālik, d’après Ibn Shihāb, d’après al-Aʿraj, d’après ʿAbd Allāh ibn Buḥayna : « qu’il dit : Le Messager de Dieu — paix et bénédiction sur lui — pria pour nous deux rakʿas, puis se leva sans s’asseoir ; les gens se levèrent avec lui. Quand il eut accompli sa prière — et que nous attendions son salut —, il fit le takbīr, puis se prosterna de deux prosternations, assis, avant le salut, puis fit le salut. » [Muwaṭṭaʾ, n° 258]</li>
<li>Yaḥyā a dit : « Mālik dit, sur celui qui oublia dans sa prière, se leva pour l’addition après l’avoir achevée à quatre, récita puis s’inclina, et, relevant la tête de son inclinaison, se souvint qu’il avait achevé : “Il revient et s’assied, sans se prosterner — et s’il s’est prosterné de l’une des deux prosternations, je ne vois pas qu’il se prosterne de l’autre ; puis, quand il accomplit sa prière, qu’il se prosterne de deux prosternations, assis, après le salut.” » [Muwaṭṭaʾ, n° 260]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>shaffaʿahā</em> (« la complètent paire ») : il la rendit à la parité. Al-Bājī a dit : il se peut que la prière soit bâtie sur la parité ; s’il entre en elle ce qui la rend impaire par addition, il incombe de réparer cela par ce qui la fait paire.</li>
<li><em>targhīm</em> (« humiliation ») : courroux et abaissement.</li>
<li><em>qaḍā ṣalātahu</em> (« accomplit sa prière ») : il en fut quitte.</li>
<li><em>wa-naẓarnā taslīmahu</em> (« nous attendions son salut ») : nous attendîmes son salut.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Cite le statut de qui doute dans sa prière : a-t-il prié trois rakʿas ou quatre ?</li>
<li>Que fait celui qui s’est levé de deux rakʿas en délaissant l’assise du premier <em>tashahhud</em> ?</li>
<li>Explicite le statut de qui s’est levé après l’achèvement de sa prière, par addition.</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : le statut de qui doute dans sa prière</h3>
<h4>Qui doute dans sa prière : bâtit-il sur la certitude, ou sur le prépondérant de son opinion ?</h4>
<p>Mālik, al-Shāfiʿī, al-Thawrī et d’autres tinrent que le douteux bâtit sur la certitude, et que la recherche (<em>taḥarrī</em>) ne lui suffit pas — à cause du hadith du chapitre, d’après ʿAṭāʾ ibn Yasār, que le Messager de Dieu — paix et bénédiction sur lui — dit : « Quand l’un de vous doute dans sa prière et ne sait combien il a prié — trois ou quatre —, qu’il prie une rakʿa… » ; et dans une narration de Muslim : « qu’il rejette le doute et bâtisse sur ce dont il est certain ».</p>
<p>Une troupe de savants — al-Nakhaʿī, Abū Ḥanīfa, al-Awzāʿī — tinrent que le douteux recherche et bâtit sur le plus prépondérant de son opinion ; le sens, chez eux : s’il doute — a-t-il prié trois ou quatre ? — et le quatre prévaut à son avis, il bâtit dessus, salue et se prosterne ; et s’il doute sans savoir — trois ou quatre ? — sans que rien ne prévale à son avis, il bâtit sur le moindre et apporte une rakʿa. Leur preuve : le hadith d’Ibn Masʿūd : “Et quand l’un de vous doute dans sa prière, qu’il recherche le juste (<em>yataḥarra l-ṣawāb</em>) et l’achève dessus.” [Rapporté par al-Bukhārī dans son <em>Ṣaḥīḥ</em>] Et la recherche, chez eux : bâtir sur le plus prépondérant de l’opinion. Les Mālikites et leurs alliés y répondirent : le voulu par la recherche est l’intention du juste et le retour à la certitude — comme sa parole — paix et bénédiction sur lui — : « Que nul d’entre vous ne choisisse (<em>yataḥarra</em>) de prier au lever du soleil ni à son coucher. » [Rapporté par an-Nasāʾī dans la <em>Sunan al-ṣughrā</em>] Sur ce, le hadith d’Ibn Masʿūd explicite le hadith du chapitre.</p>
<p>Et cette règle vaut pour autre que l’obsédé du doute (<em>mustankiḥ</em>) — celui sur qui l’oubli abonde et dont il ne se défait guère ; quant au <em>mustankiḥ</em>, il ne lui incombe pas de réparer sa prière : il ne lui incombe que la prosternation — car l’imam Mālik rapporta dans le livre de l’oubli, d’après Abū Hurayra — que Dieu soit satisfait de lui — : « que le Messager de Dieu — paix et bénédiction sur lui — dit : Quand l’un de vous se met debout pour prier, Satan vient à lui et l’embrouille, au point qu’il ne sait combien il a prié. Quand l’un de vous trouve cela, qu’il se prosterne de deux prosternations, assis. » [Muwaṭṭaʾ, n° 265]</p>
<h4>Qui doute dans sa prière et bâtit sur la certitude : se prosterne-t-il avant le salut ou après ?</h4>
<p>Selon l’école connue, celui qui doute dans sa prière et bâtit sur la certitude se prosterne après le salut — car il se peut qu’il ait accompli ce en quoi il doutait : ce qu’il apporte alors est pure addition. Cela contredit l’apparent du hadith, car il y vient : « qu’il se prosterne de deux prosternations, assis, avant le salut » ; certains s’en servirent pour [tenir] que la prosternation de l’addition est avant le salut, comme le retranchement. On répondit au hadith par ce qui suit :</p>
<ul>
<li>a — Que le salut voulu en sa parole — paix et bénédiction sur lui — : « qu’il se prosterne de deux prosternations, assis, avant le salut » est le salut du <em>tashahhud</em> : le Prophète fut absolu dans [le terme] « salut », et on le porte sur lui, pour concilier les hadiths venus sur le sujet. L’indique ce qui vient à la fin du hadith : « les deux prosternations sont une humiliation pour Satan » : car l’humiliation de Satan n’est valable qu’après l’achèvement de l’adoration, et après qu’on est garanti de sa corruption par l’oubli ou autre.</li>
<li>b — Que les deux prosternations voulues en sa parole : « qu’il se prosterne de deux prosternations, assis, avant le salut » sont les deux prosternations de la rakʿa par laquelle il ôta le doute ; quant aux deux prosternations de l’oubli, il y fit allusion par sa parole : “si la rakʿa qu’il pria était une cinquième, les deux prosternations la complètent paire ; et si elle était une quatrième, les deux prosternations sont une humiliation pour Satan”.</li>
</ul>
<h3>Deuxièmement : le statut de qui s’est levé après les deux rakʿas ou après l’achèvement de la prière</h3>
<h4>Le statut de qui s’est levé après les deux rakʿas, délaissant l’assise du premier tashahhud</h4>
<p>L’imam Mālik mentionna en ce chapitre le hadith d’ʿAbd Allāh ibn Buḥayna : « qu’il dit : Le Messager de Dieu — paix et bénédiction sur lui — pria pour nous deux rakʿas, puis se leva sans s’asseoir ; les gens se levèrent avec lui. Quand il eut accompli sa prière — et que nous attendions son salut —, il fit le takbīr, puis se prosterna de deux prosternations, assis, avant le salut, puis fit le salut. » Ce hadith contient les règles suivantes :</p>
<ul>
<li>Que celui qui délaisse la première assise, une fois debout, n’y revient pas — comme il vient dans la narration d’Ibn Khuzayma et d’autres : “ils glorifièrent [Dieu] avec lui, et il poursuivit jusqu’à achever sa prière.” S’il revient après s’être tenu debout droit, sa prière n’en est pas invalidée selon le <em>jumhūr</em> des juristes, dont Mālik — car il revint à l’état originel sur lequel il était : qui ajoute dans sa prière par oubli, elle n’en est point invalidée — à plus forte raison qui vise l’acte qu’il en a délaissé. Il fut dit : elle est invalidée — et c’est l’école d’al-Shāfiʿī.</li>
<li>Que le premier <em>tashahhud</em> est une sunna : s’il était obligatoire, il serait revenu jusqu’à l’accomplir, comme en délaissant une rakʿa ou une prosternation — l’obligatoire égalise le délibéré et l’oublieux, sauf en la faute.</li>
<li>Que la prosternation de l’oubli est avant le salut quand elle est pour un retranchement, selon sa parole : “il se prosterna de deux prosternations, assis, avant le salut” — réfutation de qui a prétendu qu’elle est entièrement après le salut, ou avant lui.</li>
<li>Qu’on se contente des deux prosternations pour l’oubli, même répété — car celui qui a manqué le <em>tashahhud</em> et l’assise : chacun des deux, si l’orant l’oubliait isolément, il s’en prosternerait ; et il ne fut pas transmis qu’il — paix et bénédiction sur lui — se prosternât, en cette situation, d’autre chose que deux.</li>
<li>Que la prosternation est propre à l’oubli : qui délaisse délibérément quelque chose de ce qui se répare par la prosternation ne se prosterne pas, selon le <em>jumhūr</em>.</li>
<li>Que le suivi se prosterne avec l’imam quand l’imam oublie, même si le suivi n’oublie pas — Ibn Ḥazm y transmit le consensus.</li>
</ul>
<h4>Le statut de qui s’est levé après l’achèvement de sa prière</h4>
<p>L’imam Mālik [exposa] que celui qui oublia dans sa prière et se leva pour l’addition après l’avoir achevée revient chaque fois qu’il s’en souvient — avant l’inclinaison, après elle, entre les deux prosternations, et en quelque état qu’il s’en souvienne : il lui incombe de délaisser l’œuvre où il est et de prendre ce qui lui reste — assise, <em>tashahhud</em> et salut —, et il se prosterne après le salut pour l’addition. S’il s’en souvient et persiste dans sa prière sans revenir, sa prière est invalidée. C’est le sens de la parole de l’imam Mālik : “… il revient et s’assied, sans se prosterner — et s’il s’est prosterné de l’une des deux prosternations, je ne vois pas qu’il se prosterne de l’autre ; puis, quand il accomplit sa prière, qu’il se prosterne de deux prosternations, assis, après le salut.” La règle est générale en la prière de quatre comme en les autres. Ibn ʿAbd al-Barr a dit : “Ils furent d’accord que quiconque ajouta en sa prière quelque chose, si peu fût-ce, autre que le rappel permis — sa prière fut corrompue ; et leur consensus en cela valide la parole de Mālik.” L’origine en cela : le hadith d’Ibn Masʿūd — que Dieu soit satisfait de lui — : “qu’il — paix et bénédiction sur lui — pria le Ẓuhr à cinq. On lui dit : Faut-il ajouter à la prière ? Il dit : Qu’est-ce donc ? Ils dirent : Tu as prié cinq. Il se prosterna de deux prosternations après avoir salué, puis tourna son visage vers nous et dit : ‘Si quelque chose survenait dans la prière, je vous l’annoncerais — mais je ne suis qu’un homme comme vous : j’oublie comme vous oubliez ; quand j’oublie, rappelez-le-moi…’” [Rapporté par al-Bukhārī dans son <em>Ṣaḥīḥ</em>]</p>
<h2>L’évaluation</h2>
<ol>
<li>Qui doute dans sa prière : bâtit-il sur la certitude, ou sur le prépondérant de son opinion ?</li>
<li>Explicite le statut de qui commit dans sa prière un oubli par addition ou par retranchement.</li>
<li>Certains savants tinrent que la prosternation de l’oubli est avant le salut sans restriction, et s’appuyèrent du hadith d’ʿAṭāʾ ibn Yasār : « qu’il se prosterne de deux prosternations, assis, avant le salut » — lui qui concerne l’addition. Que réponds-tu à cela ?</li>
</ol>
<h2>L’exploitation</h2>
<p>L’imam Mālik fit sortir dans le <em>Muwaṭṭaʾ</em>, d’après ʿAlqama ibn Abī ʿAlqama, d’après sa mère : « que ʿĀʾisha, épouse du Prophète — paix et bénédiction sur lui —, dit : Abū Jahm ibn Ḥudhāfa offrit au Messager de Dieu — paix et bénédiction sur lui — un <em>khumayṣa</em> de Syrie portant des dessins ; il y pria. Quand il eut fini, il dit : Rends ce <em>khumayṣa</em> à Abū Jahm — car je regardai ses dessins dans la prière, et il faillit me tenter. » [Muwaṭṭaʾ, n° 261]</p>
<p>Et d’après ʿAbd Allāh ibn Abī Bakr : « qu’Abū Ṭalḥa al-Anṣārī priait dans son jardin ; un oiseau <em>dubsī</em> s’envola et se mit à voltiger, cherchant une issue ; cela lui plut, et il le suivit des yeux un moment ; puis il revint à sa prière — et voici qu’il ne savait plus combien il avait prié. Il dit : Une tentation m’a atteint en ce bien qui est mien ! Il vint au Messager de Dieu — paix et bénédiction sur lui —, lui mentionna la tentation qui l’avait atteint dans son jardin, et dit : Ô Messager de Dieu, il est une aumône pour Dieu : place-le où tu voudras. » [Muwaṭṭaʾ, n° 263]</p>
<p><em>khumayṣa</em> : un manteau fin, carré, de soie velours (<em>khazz</em>) ou de laine. <em>yaftinunī</em> (« il faillit me tenter ») : il me distraite de l’humilité de la prière. <em>dubsī</em> : un oiseau semblable à la tourterelle — on a dit : la tourterelle même.</p>
<ol>
<li>Pourquoi le Prophète — paix et bénédiction sur lui — ordonna-t-il de rendre le <em>khumayṣa</em> à son propriétaire ?</li>
<li>Quel est le statut si l’orant subit un oubli dans sa prière ?</li>
<li>Extrais des deux hadiths ce qui indique la légitimité de se prémunir de l’oubli dans la prière.</li>
</ol>
<h2>La préparation préalable</h2>
<p>Lis les hadiths de la prochaine leçon et réponds à ce qui suit :</p>
<ol>
<li>Explique ce qui suit : <em>al-badna</em> (le chameau, mâle ou femelle) – <em>al-dhikr</em> (le sermon du vendredi et les exhortations qu’il renferme) – <em>laghawt</em> (le parler vain).</li>
<li>Résume les principales règles touchant la prière du vendredi.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12987":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12987 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12987 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
