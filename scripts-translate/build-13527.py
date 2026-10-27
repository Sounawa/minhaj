#!/usr/bin/env python3
# build-13527.py — leçon 13527 « Sourate An-Nahl, versets 41-44 » (tafsir-tanawi-1, lessons[10], badge Leçon 12/32)
# Trame 13519 (R276). ZÉRO script arabe dans tout le htmlFr (auto-vérif). Apostrophes droites converties.
# TREIZE restaurations coraniques (cache) dont 1 candidat (an-Naḥl 43, évaluation 4) ;
# tronçon « s'ils savaient » TRANCHÉ par le Muḥarrar original (« le pronom dans yaʿlamūn »).
import json, os, re

FR1 = '''<h1>La sourate an-Naḥl — <em>al-Muḥarrar al-wajīz</em> d'Ibn ʿAṭiyya, versets 41 à 44</h1>
<p>Leçon de tafsīr — sourate an-Naḥl, versets (41-44) — tirée du livre <em>al-Tafsīr min khilāl al-Muḥarrar al-wajīz fī tafsīr al-Kitāb al-ʿazīz</em> d'Ibn ʿAṭiyya, au profit des élèves de la première année de l'enseignement secondaire ancien, première étape (leçon 8 du manuel — la dixième du fil consacré au Naḥl).</p>
<ol>
<li>Me familiariser avec le sens des mots des versets et en déterminer les contenus.</li>
<li>Déduire des versets la récompense de l'émigration, en ce bas-monde et dans l'au-delà, ainsi que certaines des qualités des émigrants.</li>
<li>Ressentir la place de la Sunna prophétique.</li>
</ol>
<h2>Introduction</h2>
<p>Après que les versets de la leçon précédente ont fait allusion à la thèse des démenteurs de la Résurrection — ceux qui avaient juré par Allah de toute la force de leurs serments qu'Allah ne ressusciterait point celui qui meurt —, et après qu'Allah, le Très-Haut, les a réprimés en établissant que la Résurrection est vérité, vinrent ces versets, objet de la leçon, pour exposer la récompense de celui qui a cru au Jour dernier, tenu la révélation pour véridique, enduré pour sa foi le tort des associateurs, fait preuve de patience et espéré la rétribution, et émigré avec sa religion, craignant pour sa foi la séduction et pour son âme la perdition.</p>
<p>Quelle est donc l'émigration dont font mention les versets ? Et quelles sont les qualités par lesquelles les émigrants ont mérité les éloges et la récompense mentionnés ?</p>
'''

FR2 = '''<h2>Les versets</h2>
<p>« (41) Et ceux qui, pour (la cause d') Allah, ont émigré après avoir subi des injustices, Nous les installerons dans une situation agréable dans la vie d'ici-bas. Et le salaire de la vie dernière sera plus grand encore s'ils savaient. (42) Eux qui ont enduré et placé leur confiance en leur Seigneur. (43) Nous n'avons envoyé, avant toi, que des hommes auxquels Nous avons fait des révélations. Demandez donc aux gens du rappel si vous ne savez pas. (44) (Nous les avons envoyés) avec des preuves évidentes et des livres saints. Et vers toi, Nous avons fait descendre le Coran, pour que tu exposes clairement aux gens ce qu'on a fait descendre pour eux et afin qu'ils réfléchissent. » (an-Naḥl, 41-44)</p>
<p>[Citation coranique (an-Naḥl, 41-44 — le bloc entier des versets de la leçon) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la section imprimée « Les versets » est vide dans la source numérisée, le bloc versical tout entier ayant disparu à la numérisation — perte OCR.]</p>
'''

FR3 = '''<h3>L'explication des mots</h3>
<ul>
<li>« Ils ont émigré » (<em>hājarū</em>) : ils ont quitté leurs demeures. Le sens de l'émigration est de quitter les demeures et les proches, ou de délaisser les mauvaises actions et les péchés.</li>
<li>« pour les installer » (<em>li-nubawwiʾannahum</em>) : Nous les établirons en ce bas-monde dans une belle demeure, où réside leur gloire.</li>
<li>« avec les preuves évidentes » (<em>bi-l-bayyināt</em>) : par les miracles établissant la véracité du Messager.</li>
<li>« et les Psaumes » (<em>wa-z-zubur</em>) : leur singulier est <em>zabūr</em> ; ce sont les livres des législations et des obligations que les messagers transmettent aux serviteurs.</li>
<li>« le Rappel » (<em>adh-dhikr</em>) : le Coran noble.</li>
</ul>
<h3>L'extraction des contenus des versets</h3>
<ol>
<li>Quelle est la récompense de l'émigration pour Allah ?</li>
<li>Détermine certaines des qualités des émigrants.</li>
<li>Quelle est la qualité par laquelle Allah, le Très-Haut, a décrit Ses messagers ?</li>
</ol>
'''

FR4 = '''<h2>Le tafsīr</h2>
<p>Les versets ont comporté ce qui suit :</p>
<h3>Premièrement : l'exposé de la récompense des émigrants, en ce bas-monde et dans l'au-delà</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et ceux qui, pour (la cause d') Allah, ont émigré après avoir subi des injustices, Nous les installerons dans une situation agréable dans la vie d'ici-bas. Et le salaire de la vie dernière sera plus grand encore s'ils savaient. » (an-Naḥl, 41)</p>
<p>[Citation coranique (an-Naḥl, 41 — l'ouverture du commentaire) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>Ce verset fut révélé au sujet de l'émigration vers l'Abyssinie, selon l'avis de la majorité des savants — et c'est l'avis correct, car il fut révélé avant l'émigration vers Médine. En son sens, il s'adresse à quiconque a émigré, en général : celui qui a délaissé sa patrie et ses proches pour la cause d'Allah, en quête de Son agrément, qui a fait preuve de patience et placé sa confiance en Allah. C'est là, pour les autres, une incitation à l'émigration et à endurer tout tort dans la cause d'Allah, en espérant la rétribution.</p>
<p>Le bien promis en ce bas-monde — l'invisible l'a dévoilé : c'est Médine l'illuminée, dont Allah leur fit le don et qu'Il leur établit comme demeure d'émigration. Il a été dit aussi : ce bien est la langue de véracité qui demeure pour eux dans les générations à venir. Et il a été dit : le bien est général, en tout ce qu'il est bon que le fils d'Adam obtienne en ce bas-monde.</p>
<p>Il a été rapporté d'ʿUmar ibn al-Khaṭṭāb qu'il donnait, au moment du partage, des biens à l'un des émigrants, et lui disait : « Prends ce qu'Allah t'a promis en ce bas-monde, et le salaire de l'au-delà est plus grand. » [al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya, 4/169]</p>
<p>Et :</p>
<p>« Eux qui ont enduré et placé leur confiance en leur Seigneur. » (an-Naḥl, 42)</p>
<p>[Citation coranique (an-Naḥl, 42) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel orphelin « Et : » est vide dans la source numérisée — perte OCR.]</p>
<p>C'est ici une allusion au Paradis, car la récompense de l'au-delà est plus grande. Et le pronom dans la parole du Très-Haut :</p>
<p>« s'ils savaient » (<em>law kānū yaʿlamūn</em>)</p>
<p>[Citation coranique (an-Naḥl, 41 — le tronçon « s'ils savaient », la clôture du verset) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé est vide dans la source numérisée — perte OCR ; le tronçon retenu est celui que le <em>Muḥarrar</em> original désigne nommément pour ce commentaire — « le pronom dans <em>yaʿlamūn</em> ».]</p>
<p>revient sur quiconque doute de la Résurrection.</p>
'''

FR5 = '''<h3>Deuxièmement : certaines des qualités des émigrants qui ont appelé les égards à leur égard</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Eux qui ont enduré et placé leur confiance en leur Seigneur. » (an-Naḥl, 42)</p>
<p>[Citation coranique (an-Naḥl, 42 — l'ouverture de la deuxième section) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>Ce verset est venu exposer certaines des qualités des émigrants, celles par lesquelles Allah les a décrits afin qu'ils obtiennent la récompense de l'au-delà, et ce sont :</p>
<ul>
<li>La patience face au tort : Allah, le Très-Haut, les a décrits par cette vertu qui porte celui qui la détient à endurer les épreuves dans la cause d'Allah, à accomplir les actes d'obéissance et à s'abstenir de tomber dans les péchés et les passions. Ceux-ci ont fait preuve de patience face à ce qu'ils enduraient du tort de leur peuple, face au départ de la patrie, et face à l'étrangéité parmi des gens avec lesquels aucune familiarité ni protection commune ne les réunissait en une demeure.</li>
<li>La confiance en Allah : c'est s'appuyer sur Allah, le Très-Haut, et Lui confier l'affaire. Les gens, à ce sujet, se répartissent en degrés : l'un en fait la méthode même de sa vie — cela est licite et bon, tant qu'il ne se jette pas lui-même dans la ruine ; un autre place sa confiance en Allah tout en activant les moyens, et cela s'accorde à la parole du Prophète (prière et salut d'Allah sur lui) : « Entrave-la, puis place ta confiance. » [Ṣaḥīḥ d'Ibn Ḥibbān, livre des cœurs, chapitre de la piété et de la confiance] ; un autre encore est le négligent qui ne sait comment placer sa confiance en Allah.</li>
</ul>
<p>Les deux qualités de patience et de confiance comptent parmi les plus importantes qualités des émigrants — elles furent la cause de l'obtention de l'agrément d'Allah, en ce bas-monde et dans l'au-delà.</p>
'''

FR6 = '''<h3>Troisièmement : l'humanité, l'une des qualités des prophètes et des messagers</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Nous n'avons envoyé, avant toi, que des hommes auxquels Nous avons fait des révélations. Demandez donc aux gens du rappel si vous ne savez pas. » (an-Naḥl, 43)</p>
<p>[Citation coranique (an-Naḥl, 43 — l'ouverture du commentaire) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>Ce verset fut révélé en réponse aux mécréants de Quraysh, qui trouvaient étrange qu'un être humain fût un messager d'Allah, le Très-Haut. Allah les informa donc — en s'adressant à Muḥammad (prière et salut d'Allah sur lui) — qu'Il n'avait envoyé aux communautés antérieures que des hommes, et n'avait envoyé à aucune communauté d'entre elles un ange. De cela relève la parole du Très-Haut :</p>
<p>« Est-il étonnant pour les gens, que Nous ayons révélé à un homme d'entre eux: "Avertis les gens, et annonce la bonne nouvelle aux croyants qu'ils ont auprès de leur Seigneur une présence méritée [pour leur loyauté antérieure]? Les mécréants dirent alors: "Celui-ci est certainement un magicien évident". » (Yūnus, 2)</p>
<p>[Citation coranique (Yūnus, 2) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la référence imprimée a subsisté dans la source numérisée, la citation qu'elle introduisait a disparu à la numérisation — perte OCR.]</p>
<p>Et parmi cela, la parole du Très-Haut :</p>
<p>« Les notables de son peuple qui avaient mécru et traité de mensonge la rencontre de l'au-delà, et auxquels Nous avions accordé le luxe dans la vie présente, dirent: "Celui-ci n'est qu'un être humain comme vous, mangeant de ce que vous mangez, et buvant de ce que vous buvez. Si vous obéissez à un homme comme vous, vous serez alors perdants." » (al-Muʾminūn, 33-34)</p>
<p>[Citation coranique (al-Muʾminūn, 33-34) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la référence imprimée a subsisté dans la source numérisée, la citation qu'elle introduisait a disparu à la numérisation — perte OCR.]</p>
<p>Et la parole du Très-Haut :</p>
<p>« Demandez donc aux gens du rappel si vous ne savez pas. » (an-Naḥl, 43 — la clôture)</p>
<p>[Citation coranique (an-Naḥl, 43 — le tronçon de la clôture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'appel de citation imprimé était suivi immédiatement du commentaire, sans emplacement versical subsistant — la virgule parasite qui ouvre le commentaire en témoigne ; perte OCR.]</p>
<p>— par « les gens du Rappel », on entend les rabbins des Juifs et des Nazaréens. Après avoir réprimandé les associateurs, Allah exigea d'eux l'argument et leur ordonna d'interroger les gens des législations célestes antérieures au sujet de leurs prophètes : étaient-ils des êtres humains, ou autre chose ? Lorsque ceux-ci — les gens du Rappel — les informèrent que leurs prophètes étaient des êtres humains, les mécréants et les associateurs ne le reconnurent pas, demeurèrent dans leur opposition et ne voulurent pas reconnaître l'humanité des messagers, dont Muḥammad (prière et salut d'Allah sur lui).</p>
<p>Lorsqu'Allah, dans ce verset, décrivit les messagers par la qualité qui leur est commune avec les autres hommes — l'humanité —, Il ajouta la qualité qui leur est propre, pour montrer leur rang et leur place : la réception de la révélation divine.</p>
<p>Allah, le Très-Haut, a dit :</p>
<p>« (Nous les avons envoyés) avec des preuves évidentes et des livres saints. Et vers toi, Nous avons fait descendre le Coran, pour que tu exposes clairement aux gens ce qu'on a fait descendre pour eux et afin qu'ils réfléchissent. » (an-Naḥl, 44)</p>
<p>[Citation coranique (an-Naḥl, 44 — l'ouverture du commentaire) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'appel de citation imprimé était suivi immédiatement du commentaire, sans emplacement versical subsistant — perte OCR.]</p>
<p>Allah, le Très-Haut, expose dans ce verset la vérité de ce qu'Il a révélé à ces messagers — à savoir : « Nous n'avons envoyé avant toi, avec les preuves évidentes et les Psaumes, que des hommes » —, par les preuves et les arguments qui témoignent pour eux de la véracité de leur prophétie, et par les livres qui englobent les obligations et les législations qu'ils transmettent d'Allah aux serviteurs.</p>
<p>Et la parole du Très-Haut :</p>
<p>« Et vers toi, Nous avons fait descendre le Coran, pour que tu exposes clairement aux gens ce qu'on a fait descendre pour eux » (an-Naḥl, 44)</p>
<p>[Citation coranique (an-Naḥl, 44 — le tronçon de l'exposition) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'appel de citation imprimé était suivi immédiatement du commentaire, sans emplacement versical subsistant — perte OCR.]</p>
<p>Il est possible qu'Il ait voulu dire : expose clairement, par le Coran, ce qu'Allah t'a révélé de la révélation ; et il est possible qu'Il ait voulu dire : expose clairement, par ton explication et ton commentaire, ce que du Coran est obscur — entrent en cela ce que la Sunna a explicité de l'ordre de la législation, et c'est l'avis de Mujāhid.</p>
<p>Le sens : et Nous fîmes descendre vers toi le Coran, rappel et exhortation pour les gens, afin qu'ils prennent connaissance de ce qui leur fut fait descendre d'ordres et de législations, et des situations des peuples qu'Allah périt en punition de leur entêtement.</p>
<p>Et la parole du Très-Haut :</p>
<p>« et afin qu'ils réfléchissent » (<em>wa-laʿallahum yatafakkarūn</em>)</p>
<p>[Citation coranique (an-Naḥl, 44 — le tronçon de la clôture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>— c'est-à-dire : peut-être réfléchiront-ils à ces secrets, et s'écarteront-ils alors de la voie suivie par les démenteurs d'autrefois.</p>
<p>Les versets objet de la leçon indiquent la réalisation du dessein de l'adoration totale d'Allah, le Très-Haut — adoration qui exige d'endurer le tort dans Sa cause, la confiance et l'appui en Lui, la délégation de l'affaire à Lui, et le suivi de ce qu'Allah a fait descendre de révélation sur Son messager (prière et salut d'Allah sur lui).</p>
<h2>L'évaluation</h2>
<ol>
<li>Déduis des versets la récompense de l'émigration pour Allah.</li>
<li>Quelles sont les qualités par lesquelles Allah, le Très-Haut, a loué les premiers émigrants ?</li>
<li>Extrais des versets la qualité commune aux prophètes et aux autres hommes, et la qualité qui leur est propre.</li>
<li>Que retires-tu de la parole du Très-Haut :</li>
</ol>
<p>« Nous n'avons envoyé, avant toi, que des hommes auxquels Nous avons fait des révélations. Demandez donc aux gens du rappel si vous ne savez pas. » (an-Naḥl, 43) ?</p>
<p>[Citation coranique (an-Naḥl, 43) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus à titre de candidat signalé : l'emplacement imprimé après l'appel de citation a disparu — un point d'interrogation orphelin subsiste après la position du verset ; le verset retenu est le parallèle thématique le plus proche des questions d'évaluation — l'identification demeure soumise à caution.]</p>
'''

FR7 = '''<h2>L'exploitation</h2>
<p>Ibn Isḥāq a dit : « Lorsque le Messager d'Allah (prière et salut d'Allah sur lui) vit ce que ses compagnons subissaient comme épreuve, tandis que lui-même jouissait de la sécurité par sa position auprès d'Allah et auprès de son oncle Abū Ṭālib — et qu'il ne pouvait les préserver de l'épreuve où ils se trouvaient —, il leur dit : "Partez vers le pays d'Abyssinie : il s'y trouve un roi auprès duquel nul n'est lésé ; c'est une terre de véracité, jusqu'à ce qu'Allah vous accorde un dénouement de ce dans quoi vous êtes." Les musulmans, compagnons du Messager d'Allah (prière et salut d'Allah sur lui), partirent alors vers le pays d'Abyssinie, craignant la séduction et fuyant vers Allah avec leur religion. Ce fut la première émigration de l'islam. » [ar-Rawḍ al-anf d'as-Suhaylī, 2/202]</p>
<p>Examine le texte et réponds à ce qui suit :</p>
<ol>
<li>Quelles sont les raisons de l'émigration vers l'Abyssinie ?</li>
<li>Comment le Prophète (prière et salut d'Allah sur lui) et ses compagnons ont-ils traité ceux dont la religion différait de la leur ?</li>
</ol>
<h2>La préparation préalable</h2>
<p>Lis les versets (45 à 50) de la sourate an-Naḥl et réponds à ce qui suit :</p>
<ul>
<li>Explique les mots suivants :</li>
</ul>
<p>[La liste des mots imprimée a disparu à la numérisation : cinq emplacements vides subsistent dans la source ; les expressions relevaient des versets (45-50) de la sourate an-Naḥl, dont la leçon suivante du fil traite la suite — non reconstituée.]</p>
<ul>
<li>Montre le châtiment qu'Allah, le Très-Haut, inflige à ceux qui ont intrigé contre les prophètes et les messagers.</li>
<li>Montre le sens de la prosternation mentionnée dans les versets.</li>
</ul>
'''

FR8 = '''<h2>Notes du traducteur</h2>
<p><em>N.d.T. —</em> Leçon du fil consacré au Naḥl dont le matériau versical a disparu à la numérisation. La section imprimée « Les versets » est vide en son entier — le bloc principal (an-Naḥl, 41-44) y a été restauré. Treize restaurations coraniques au total, d'après le corpus canonique et vérifiées au cache coranique du corpus : le bloc principal an-Naḥl 41-44 ; les huit emplacements coraniques vides du commentaire (an-Naḥl 41 l'ouverture, an-Naḥl 42 après l'appel orphelin « Et : », le tronçon « s'ils savaient » — la clôture du verset 41 —, an-Naḥl 42 l'ouverture de la deuxième section, an-Naḥl 43 l'ouverture de la troisième, Yūnus 2, al-Muʾminūn 33-34, le tronçon « afin qu'ils réfléchissent ») ; les trois appels de citation restés sans emplacement imprimé du tout (le tronçon « Demandez donc aux gens du rappel si vous ne savez pas » — la clôture du verset 43, appel suivi immédiatement de la virgule parasite qui ouvre le commentaire ; an-Naḥl 44 ; le tronçon « et vers toi, Nous avons fait descendre le Coran, pour que tu exposes clairement aux gens ») ; et un candidat signalé (an-Naḥl 43, quatrième question de l'évaluation).</p>
<p><em>N.d.T. —</em> Méthode : le <em>Muḥarrar al-wajīz</em> original d'Ibn ʿAṭiyya, consulté en ligne dans une édition numérique de référence (sourate 16, versets 41 à 44), a de nouveau servi d'autorité de tranchage. Le tronçon « s'ils savaient » est celui que le <em>Muḥarrar</em> désigne nommément pour le commentaire imprimé (« le pronom dans <em>yaʿlamūn</em> revient aux mécréants de Quraysh »), dont la glose scolaire est l'adaptation « revient sur quiconque doute de la Résurrection ». Les cinq gloses de l'explication des mots et les gloses lexicales du commentaire s'apparient mot pour mot aux tronçons que le <em>Muḥarrar</em> commente (« les Psaumes : les livres écrits » ; « le Rappel, en ce verset, est le Coran » ; « il est possible qu'Il ait voulu dire : expose clairement, par la lecture du texte du Coran, ce qui est descendu… et c'est l'avis de Mujāhid »). Le tronçon de la clôture du verset 43 est établi par le contexte : le commentaire imprimé porte nommément sur « les gens du Rappel », glose que le <em>Muḥarrar</em> rattache à l'appel « demande aux gens du Rappel ». La cause de la révélation imprimée — l'émigration vers l'Abyssinie, avis de la majorité, antérieure à l'émigration médinoise — est confirmée par le <em>Muḥarrar</em>, qui la rapporte des croyants de la Mecque contemporains des associateurs. Le candidat de la quatrième question de l'évaluation reste soumis à caution : l'emplacement imprimé est perdu, et le verset retenu est le pivot thématique de la troisième section du commentaire.</p>
<p><em>N.d.T. —</em> Les douze irrégularités de l'imprimé comptées : (1) la fente de définition vide sous le titre — neuvième occurrence ; (2) la section « Les versets » vide en son entier — septième cas consécutif du livre ; (3) les huit emplacements coraniques vides du commentaire ; (4) les trois appels de citation restés sans emplacement imprimé du tout ; (5) le candidat signalé de la quatrième question de l'évaluation, avec point d'interrogation orphelin ; (6) la liste de mots de la préparation préalable perdue — cinq emplacements ; (7) la virgule de collage orpheline en tête du commentaire des gens du Rappel ; (8) l'appel orphelin « Et : » après le récit de ʿUmar ; (9) le tatwīl médian parasite — septième leçon consécutive ; (10) l'écart de numérotation du manuel : l'imprimé porte « leçon 8 », la position au livre est la douzième leçon, et la leçon précédente du fil se disait « leçon 11 » — l'ordre de reliure du corpus numérique ne suit pas la numérotation du manuel ; (11) la tension d'attribution du hadith « Entrave-la, puis place ta confiance » : l'imprimé renvoie au Ṣaḥīḥ d'Ibn Ḥibbān, le <em>Muḥarrar</em> le rapporte d'al-Bayhaqī dans <em>Shuʿab al-īmān</em> avec le texte « Entrave et place ta confiance », auquel l'authenticité est accordée ; (12) les résidus de fermeture du corps et le paragraphe vide sous le titre. Signalés NON comptés : la lecture alternative <em>li-nuthwīannahum</em> (Ibn Masʿūd, Nuʿaym ibn Maysara, ar-Rabīʿ ibn Khuthaym, ʿAlī) et l'avis d'Abū l-Fatḥ sur le régime de <em>ḥasana</em>, attestés par le <em>Muḥarrar</em> et non reproduits par l'imprimé ; les autres avis sur les gens du Rappel rapportés par le <em>Muḥarrar</em> ; les causes alternatives de la révélation (Abū Jundal ibn Suhayl ; ʿAmmār, Ṣuhayb et Khabbāb) ; la glose des gens du Rappel tenue par az-Zajjāj — « les rabbins des Juifs et des Nazaréens qui n'ont pas embrassé l'islam » — sans être nommée par l'imprimé.</p>
<p><em>N.d.T. —</em> Les versions françaises des versets sont reprises du cache coranique du corpus ; les numéros de versets entre parenthèses ont été insérés au bloc principal selon la convention du fil ; les guillemets internes de la version du cache ont été conservés tels quels. La glose « dans une situation agréable dans la vie d'ici-bas » rend le terme coranique <em>ḥasana</em>, que l'explication des mots glose « une belle demeure, où réside leur gloire ». Le hadith aux deux attributions est rendu d'après le texte imprimé ; sa chaîne d'attribution est signalée au compte des irrégularités.</p>
'''

# === ASSEMBLAGE ===
html = FR1 + FR2 + FR3 + FR4 + FR5 + FR6 + FR7 + FR8

# Post-traitement : apostrophes droites -> courbes (convention chantier)
html = html.replace("'", "\u2019")

# Auto-vérifs pré-QA
AR = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")
issues = []
if AR.search(html):
    issues.append('ARABE résiduel: ' + repr(AR.findall(html)[:5]))
if html.count('«') != html.count('»'):
    issues.append(f"guillemets non appariés: {html.count('«')}/{html.count('»')}")
if "'" in html:
    issues.append(f"apostrophes droites restantes: {html.count(chr(39))}")
for ch, name in [('\u0430', 'cyrillique'), ('\uFD3E', 'crochet ornement gauche'), ('\uFD3F', 'crochet ornement droit')]:
    if ch in html:
        issues.append(f'{name} présent')
bal = ['h1', 'h2', 'h3', 'p', 'ol', 'ul', 'li', 'em']
types = sum(1 for b in bal if f'<{b}>' in html)
n_notes = html.count('[Citation coranique')
print(f'caractères: {len(html)}')
print(f'types de balises: {types}/8')
print(f'notes de restauration: {n_notes}')
print(f'guillemets: {html.count("«")}/{html.count("»")}')
if issues:
    print('PROBLÈMES:')
    for i in issues:
        print(' -', i)
    raise SystemExit(1)
if len(html) < 12000:
    print('TROP COURT (< 12 000 car) — rédaction insuffisante')
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/13527.html'
open(out, 'w').write(html)
print('écrit:', out)
