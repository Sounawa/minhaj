#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12885 (hadith-1es, l'essuyage sur la tête,
les oreilles et les chaussettes — Muwaṭṭaʾ n° 75, 79, 81, 85-89).

Conventions main (cf. 12875, 12881, 12883, 12884 du même livre) :
- h1 « L'essuyage sur la tête, les deux oreilles et les deux chaussettes
  (al-masḥ ʿalā al-raʾs wa-l-udhnayn wa-ʿalā al-khuffayn) ».
- Verset des ablutions cité « al-Māʾida (5) : 7 » — numérotation du manuel
  (maghrébine), EN COHÉRENCE avec la leçon 12875 du même livre qui cite ce
  même verset « (5) : 7 » (le décompte oriental standard l'imprime 6) ;
  restauré du canonique quran-cache.json aux DEUX emplacements (tamhīd +
  analyse) — paragraphes vides dans la source numérisée (perte OCR).
- Hadiths du Muwaṭṭaʾ 75 (Ibn ʿUmar, index aux oreilles), 79 (turban/voile),
  81 (al-Mughīra — Tabūk, jubba à manches étroites, rakʿa derrière
  ʿAbd al-Raḥmān b. ʿAwf, « aḥsantum »), 80, 85, 86, 87, 88, 89 : chaînes
  et textes intégraux.
- Écoles : masḥ ʿalā al-ʿimāma autorisé (Aḥmad, al-Awzāʿī, Dāwūd) vs interdit
  (Mālik, al-Shāfiʿī, Abū Ḥanīfa) ; al-Khaṭṭābī (certain vs susceptible) ;
  ʿAlī = Compagnon → « que Dieu soit satisfait de lui » (raḍiya).
- 12889 est la leçon SUIVANTE (épistaxis) — préparation = ses questions.
- Vocabulaire : khuff = chaussette de cuir (gloss manuel : جوربين من جلد
  مخروزين يغطيان الكعبين) ; jubba = vêtement taillé raccourci ; nāṣiya.
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

MAIDA = """<p>« Ô vous qui croyez ! Quand vous vous levez pour la prière, lavez vos visages et vos mains jusqu’aux coudes, et essuyez vos têtes, et [lavez] vos pieds jusqu’aux chevilles. Et si vous êtes en état d’impureté majeure, purifiez-vous. Et si vous êtes malades, ou en voyage, ou si l’un de vous revient de la selle, ou si vous avez touché des femmes et ne trouvez pas d’eau, alors recourez à une terre pure… » (al-Māʾida, 5 : 7, extrait)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>"""

HTML_FR = """<h1>L’essuyage sur la tête, les deux oreilles et les deux chaussettes (<em>al-masḥ ʿalā al-raʾs wa-l-udhnayn wa-ʿalā al-khuffayn</em>)</h1>
<p>Leçon sur l’essuyage sur la tête, les deux oreilles et les deux chaussettes, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la cinquième leçon.</p>
<ul>
<li>Connaître le statut de l’essuyage de la tête et des oreilles.</li>
<li>Saisir la preuve de la pérennité de l’essuyage sur les deux chaussettes.</li>
<li>Incarner la méthode requise pour l’essuyage sur les deux chaussettes.</li>
</ul>
<h2>Préambule</h2>
<p>Les ablutions sont lavage et essuyage : les [parties] essuyées sont les deux oreilles, la tête et les deux chaussettes. L’essuyage de la tête fait partie des obligations des ablutions — elles ne sont valables sans lui —, ce qu’atteste la parole de Dieu Très-Haut :</p>
""" + MAIDA + """
<p>Et dans le <em>Muwaṭṭaʾ</em> : « Yaḥyā a dit : on interrogea Mālik au sujet d’un homme qui fit ses ablutions et oublia d’essuyer sa tête, jusqu’à ce que ses ablutions eussent séché. Il dit : “J’estime qu’il essuie sa tête, et que, s’il a déjà prié, il refasse la prière.” » [Muwaṭṭaʾ, n° 80]</p>
<p>Quelle est l’origine de la méthode d’essuyage des deux oreilles ? Et est-il permis d’essuyer sur le turban (<em>ʿimāma</em>), le voile (<em>khimār</em>) et les deux chaussettes ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Nāfiʿ : « ʿAbd Allāh ibn ʿUmar prenait l’eau avec ses deux index pour ses deux oreilles. » [Muwaṭṭaʾ, n° 75]</li>
<li>Yaḥyā a dit : on interrogea Mālik au sujet de l’essuyage sur le turban et sur le voile ; il dit : « Il ne convient ni à l’homme ni à la femme d’essuyer sur un turban ou sur un voile : qu’ils essuient sur leurs têtes. » [Muwaṭṭaʾ, n° 79]</li>
<li>D’après Mālik, d’après Ibn Shihāb, d’après ʿIbād ibn Ziyād — qui est de la descendance d’al-Mughīra ibn Shuʿba —, d’après son père al-Mughīra ibn Shuʿba : « Le Messager de Dieu — paix et bénédiction sur lui — s’en fut, lors de l’expédition de Tabūk, pour son besoin. Al-Mughīra dit : je l’accompagnai avec de l’eau. Le Messager de Dieu — paix et bénédiction sur lui — vint, et je versai l’eau sur lui : il lava son visage ; puis il entreprit de tirer ses deux mains des manches de sa <em>jubba</em>, mais ne put y parvenir, vu l’étroitesse des manches de la <em>jubba</em> : il les fit donc sortir par-dessous la <em>jubba</em>, lava ses deux mains, essuya sa tête et essuya sur les deux chaussettes. Puis le Messager de Dieu — paix et bénédiction sur lui — arriva, alors que ʿAbd al-Raḥmān ibn ʿAwf les conduisait en prière, ayant déjà accompli pour eux une <em>rakʿa</em> ; le Messager de Dieu — paix et bénédiction sur lui — accomplit donc la <em>rakʿa</em> qui leur restait. Les gens s’alarmèrent ; et quand le Messager de Dieu — paix et bénédiction sur lui — eut achevé sa prière, il dit : “Vous avez bien fait.” » [Muwaṭṭaʾ, n° 81]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>Tabūk</em> : nom d’un lieu, appelé ʿAyn Tabūk (la source de Tabūk).</li>
<li><em>je versai</em> (<em>sakabtu</em>) : je répandis.</li>
<li><em>la jubba</em> (<em>al-jubba</em>) : ce qui, parmi les vêtements, est taillé [et porté] en raccourci.</li>
<li><em>les deux chaussettes</em> (<em>al-khuffān</em>) : deux chaussettes de cuir cousues, couvrant les deux chevilles.</li>
<li><em>les gens s’alarmèrent</em> (<em>faẓiʿa al-nās</em>) : ils craignirent d’être dans l’erreur, pour avoir devancé le Messager de Dieu — paix et bénédiction sur lui — dans la prière.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Quelle est l’origine de l’essuyage des deux oreilles, et quelle est sa méthode ?</li>
<li>Est-il permis d’essuyer sur le turban et le voile ?</li>
<li>Détermine le statut de l’essuyage sur les deux chaussettes et expose sa méthode.</li>
</ul>
<h2>L’analyse</h2>
<p>Les hadiths cités comportent trois règles parmi les actes des ablutions, à savoir :</p>
<h3>Premièrement : l’essuyage des deux oreilles</h3>
<p>L’essuyage des deux oreilles fait partie des sunna des ablutions, et le renouvellement de l’eau pour elles est recommandé — comme l’atteste le hadith du chapitre. La méthode de leur essuyage : que l’on replie les doigts de ses deux mains et fasse passer ses deux index, puis essuie avec eux ses deux oreilles, par-dedans et par-dehors. Al-Bājī a dit : il se peut aussi qu’il prenne l’eau avec deux doigts de chaque main, et essuie avec eux ses deux oreilles — sur le mode du hadith d’Ibn ʿAbbās : l’intérieur des deux oreilles s’essuie avec les index, et leur extérieur avec les pouces.</p>
<h3>Deuxièmement : l’essuyage de la tête</h3>
<p>L’essuyage de la tête fait partie des obligations des ablutions, sans lesquelles elles ne sont pas valables — du fait de la parole de Dieu Très-Haut :</p>
""" + MAIDA + """
<p>Le principe, dans le discours, est le sens propre, non le sens figuré : il n’est donc pas permis d’essuyer sur le turban. Al-Zarqānī a dit : Aḥmad, al-Awzāʿī, Dāwūd et d’autres l’y ont autorisé — en vertu des rapports (<em>āthār</em>), et par analogie avec les chaussettes — ; l’ont interdit Mālik, al-Shāfiʿī et Abū Ḥanīfa : car l’essuyage sur les chaussettes provient des rapports, non de l’analogie — et s’il provenait d’elle, l’essuyage sur les deux moufles (<em>qaffāzān</em>) serait permis.<br>
Et al-Khaṭṭābī a dit : Dieu a prescrit l’essuyage de la tête ; or le hadith de l’essuyage sur le turban est susceptible d’interprétation (<em>taʾwīl</em>) : on ne délaisse pas le certain pour le susceptible. Son analogie avec la chaussette est lointaine, vu la difficulté de l’ôter, à la différence de celle-ci ; ce qui a été transmis indiquant sa licéité est donc interprété selon les situations d’excuse (<em>ʿudhr</em>) — à preuve le hadith de l’essuyage sur le devant de la tête (<em>nāṣiya</em>) avec le turban.<br>
Et ce qui atteste la pratique continue d’ôter le turban — de même que le voile — est ce qui fut transmis dans le <em>Muwaṭṭaʾ</em> comme rapports, à savoir :<br>
D’après Mālik : « qu’il lui fut rapporté que Jābir ibn ʿAbd Allāh l’Anṣārite fut interrogé au sujet de l’essuyage sur le turban ; il dit : “Non — jusqu’à ce qu’il essuie les cheveux avec l’eau.” » [Muwaṭṭaʾ, n° 76]<br>
D’après Mālik, d’après Hishām ibn ʿUrwa : « que son père, ʿUrwa ibn al-Zubayr, ôtait le turban et essuyait sa tête avec l’eau. » [Muwaṭṭaʾ, n° 77]<br>
D’après Mālik, d’après Nāfiʿ : « qu’il vit Ṣafiyya bint Abī ʿUbayd — l’épouse de ʿAbd Allāh ibn ʿUmar — ôter son voile et essuyer sa tête avec l’eau — Nāfiʿ étant alors un enfant. » [Muwaṭṭaʾ, n° 78]</p>
<h3>Troisièmement : l’essuyage sur les deux chaussettes</h3>
<h4>Son statut</h4>
<p>L’essuyage sur les deux chaussettes est une dispense (<em>rukhṣa</em>) dans le fiqh mālikite ; un groupe de traditionalistes parmi les <em>ḥuffāẓ</em> a affirmé expressément qu’il est d’établissement massivement attesté (<em>mutawātir</em>), et certains en ont dénombré les rapporteurs : ils dépassent quatre-vingts. Ce qui atteste son établissement, entre autres, est le hadith d’al-Mughīra ibn Shuʿba — l’endroit probant étant sa parole : « et il essuya sur les deux chaussettes ». Al-Zarqānī a dit : il y a là une riposte à qui prétend que l’essuyage sur elles deux fut abrogé par le verset de <em>al-Māʾida</em> : car celui-ci fut révélé lors de l’expédition d’al-Muraysīʿ, tandis que ce récit [se situe] lors de l’expédition de Tabūk, postérieurement — d’un accord unanime, celle-ci étant la dernière des campagnes. En outre, l’essuyage sur les deux chaussettes est particulier aux ablutions : le lavage majeur (<em>ghusl</em>) n’y a point de part, de l’avis unanime.<br>
L’établissement de l’essuyage est encore confirmé par des rapports des Compagnons — dont Mālik en mentionne certains dans le <em>Muwaṭṭaʾ</em>, d’après Saʿd ibn Abī Waqqāṣ, ʿAbd Allāh ibn ʿUmar et Anas ibn Mālik. Et telle est la position authentique de l’imam Mālik — que Dieu lui fasse miséricorde. Et dans [le commentaire d’]al-Zarqānī : Ibn Wahb a dit : « C’est sur l’essuyage — en résidence comme en voyage — que je quittai Mālik en dernier lieu. » De même, la position répandue (<em>mashhūr</em>) dans l’école en autorise l’usage au voyageur comme au résident — mais on n’essuie qu’à la condition de les avoir chaussées sur une pureté hydrique complète, c’est-à-dire après l’achèvement de ses ablutions. Ainsi, dans le <em>Muwaṭṭaʾ</em> : « Yaḥyā a dit : on interrogea Mālik au sujet d’un homme qui fit les ablutions de la prière, puis chaussa ses deux chaussettes, puis urina, puis les ôta, puis les remit à ses pieds : doit-il reprendre les ablutions depuis le début ? Il dit : “Qu’il ôte ses deux chaussettes, puis qu’il fasse ses ablutions et lave ses deux pieds : car on n’essuie sur les deux chaussettes que celui qui introduit ses deux pieds dans les chaussettes alors qu’elles sont pures de la pureté des ablutions ; quant à celui qui introduit ses deux pieds dans les chaussettes alors qu’elles ne sont pas pures de la pureté des ablutions — il n’essuie pas sur les chaussettes.” » [Muwaṭṭaʾ, n° 85]</p>
<h4>La méthode de l’essuyage sur elles</h4>
<p>Cette méthode, l’expose ce que rapporta Mālik, d’après Hishām ibn ʿUrwa : « qu’il vit son père essuyer sur les deux chaussettes. Il dit : et il n’ajoutait rien, quand il essuyait sur les deux chaussettes, à l’essuyage de leurs dessus — et il n’essuyait pas leurs dessous. » [Muwaṭṭaʾ, n° 88]<br>
Al-Zarqānī a dit : « car le dessus de la chaussette est l’endroit où l’obligation de l’essuyage fait l’unanimité, et l’avis apparent de l’école (<em>ẓāhir al-madhhab</em>) est l’obligation de les couvrir intégralement, toutes deux : s’il essuie le dessus à l’exclusion du dessous, il refait [la prière] dans son temps ; et s’il fait l’inverse, il la refait en tout temps. ʿAlī — que Dieu soit satisfait de lui — a dit : “Si la religion relevait de l’opinion, le dessous de la chaussette mériterait plus l’essuyage que le dessus ! Et j’ai vu le Messager de Dieu — paix et bénédiction sur lui — essuyer sur le dessus de ses deux chaussettes.” Al-Mughīra transmit de même ; et l’original en est ce que l’imam transmit d’après Ibn Shihāb, à savoir : “Ibn Shihāb fut interrogé au sujet de l’essuyage sur les deux chaussettes : comment le fait-on ? Il introduisit alors l’une de ses deux mains sous la chaussette, et l’autre par-dessus, puis les fit passer [toutes deux]. Yaḥyā a dit : Mālik a dit : la parole d’Ibn Shihāb est ce que j’ai le plus aimé entendre en la matière.” » [Muwaṭṭaʾ, n° 89]<br>
Et dans le <em>Jāmiʿ</em> d’Ibn Yūnus : « Ibn al-Qāsim a dit : Mālik nous montra l’essuyage sur les deux chaussettes : il posa sa main droite sur les bouts de ses orteils, au-dessus de son pied droit, et posa la gauche sous les bouts des orteils de la plante de sa chaussette, puis les fit glisser jusqu’aux endroits de l’ablution — à savoir l’origine du tibia et l’alignement des deux chevilles. Abū Muḥammad a dit : de même, sa main gauche au-dessus de son pied gauche, et sa main droite au-dessous. Ibn Ḥabīb a dit : c’est ainsi que nous le montrèrent Muṭarrif et Ibn al-Mājishūn. »<br>
En somme : celui qui essuie, de quelque façon qu’il essuie, en est quitte, dès lors que son essuyage embrasse les deux chaussettes — ainsi parle al-Zarqānī.</p>
<h2>L’évaluation</h2>
<ol>
<li>Cite ce qui atteste l’interdiction de l’essuyage sur le turban et le voile.</li>
<li>Expose la méthode de l’essuyage des deux oreilles.</li>
<li>Expose la meilleure façon d’essuyer sur les deux chaussettes, et prouve qu’il n’est pas abrogé.</li>
</ol>
<h2>L’exploitation</h2>
<p>Yaḥyā a dit : on interrogea Mālik au sujet d’un homme qui fit ses ablutions, ses deux chaussettes étant [déjà] à ses pieds, et qui s’oublia sur l’essuyage des chaussettes, jusqu’à ce que ses ablutions eussent séché et qu’il eût prié. Il dit : « Qu’il essuie sur ses deux chaussettes, qu’il refasse la prière — et qu’il ne refasse pas les ablutions. » [Muwaṭṭaʾ, n° 86]<br>
Yaḥyā a dit : on interrogea Mālik au sujet d’un homme qui lava ses deux pieds, puis chaussa ses deux chaussettes, puis reprit les ablutions depuis le début. Il dit : « Qu’il ôte ses deux chaussettes, puis qu’il fasse ses ablutions et lave ses deux pieds. » [Muwaṭṭaʾ, n° 87]</p>
<ol>
<li>Tire du premier texte le statut de la continuité (<em>muwālāt</em>) entre l’essuyage sur les chaussettes et le reste des membres des ablutions.</li>
<li>Expose, au fil du second texte, le statut de celui qui inversa les actes des ablutions, puis chaussa ses chaussettes avant l’achèvement de ses ablutions.</li>
</ol>
<h2>La préparation préalable</h2>
<ol>
<li>Expose ce qu’on entend par épistaxis (<em>ruʿāf</em>) et son rapport avec les annulatifs des ablutions.</li>
<li>Qu’est-il obligatoire à celui dont le nez saigne pendant la prière ?</li>
<li>Médite les hadiths de la leçon à venir et détermine les règles qu’ils comportent.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12885":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12885 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12885 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
