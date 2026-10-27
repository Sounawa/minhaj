#!/usr/bin/env python3
# build-13519.py — leçon 13519 « Sourate An-Nahl, versets 57-59 » (tafsir-tanawi-1, lessons[9], badge Leçon 11/32)
# Trame 13518 (R275). ZÉRO script arabe dans tout le htmlFr (auto-vérif). Apostrophes droites converties.
# VINGT restaurations coraniques (cache) + 1 candidat (az-Zukhruf 16) + en-tête « Premièrement » restauré.
import json, os, re

FR1 = '''<h1>La sourate an-Naḥl — <em>al-Muḥarrar al-wajīz</em> d'Ibn ʿAṭiyya, versets 57 à 59</h1>
<p>Leçon de tafsīr — sourate an-Naḥl, versets (57-59) — tirée du livre <em>al-Tafsīr min khilāl al-Muḥarrar al-wajīz fī tafsīr al-Kitāb al-ʿazīz</em> d'Ibn ʿAṭiyya, pour la première année de l'enseignement secondaire ancien, première étape (leçon 11 du manuel — la neuvième du fil consacré au Naḥl).</p>
<ol>
<li>Me familiariser avec le sens des mots des versets et en déterminer les contenus.</li>
<li>Déduire des versets la sanctification d'Allah, le Très-Haut, de ce qui ne Lui convient pas.</li>
<li>Rejeter la conduite des gens de la jāhiliyya dans le mépris qu'ils ont du féminin.</li>
</ol>
<h2>Introduction</h2>
<p>Les gens avaient atteint, avant la mission du Prophète (prière et salut d'Allah sur lui), le comble de l'égarement et du fourvoiement. La société arabe, en ce contexte, avait porté l'écart d'avec la <em>fitra</em> droite — la disposition naturelle — à un degré immense, tant du côté de la croyance et de la foi que dans les différents aspects de la vie, parmi lesquels l'aspect social : s'y était installée une vision dépréciative de la femme, établie dans les esprits et les cœurs, jusqu'à atteindre son sommet dans le fait que le père enterrât vivante sa fille, en réponse à une culture sociale dominante. Et de cette culture relevait, selon leur prétention, le fait de faire des anges des femelles et des filles d'Allah.</p>
<p>Comment les versets ont-ils traité la question de l'attribution des filles à Allah ? Et comment tirons-nous profit des versets pour édifier une conduite sociale qui rende à la femme sa place ?</p>
'''

FR2 = '''<h2>Les versets</h2>
<p>« (57) Et ils assignent à Allah des filles. Gloire et pureté à Lui ! Et à eux-mêmes, cependant, (ils assignent) ce qu'ils désirent (des fils). (58) Et lorsqu'on annonce à l'un d'eux une fille, son visage s'assombrit et une rage profonde (l'envahit). (59) Il se cache des gens, à cause du malheur qu'on lui a annoncé. Doit-il la garder malgré la honte ou l'enfouira-t-il dans la terre ? Combien est mauvais leur jugement ! » (an-Naḥl, 57-59)</p>
<p>[Citation coranique (an-Naḥl, 57-59 — le bloc entier des versets de la leçon) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la section imprimée « Les versets » est vide dans la source numérisée, le bloc versical tout entier ayant disparu à la numérisation — perte OCR.]</p>
'''

FR3 = '''<p><span>La compréhension</span></p>
<h3>L'explication des mots</h3>
<p>L'exercice imprimé sous l'intitulé de l'explication juxtaposait aux tronçons coraniques une série d'interprétations ; les interprétations imprimées seules ont survécu à la numérisation, et les tronçons correspondants sont restaurés ci-dessous d'après le corpus canonique, chacun à sa place, l'identification s'appuyant sur le <em>Muḥarrar</em> original d'Ibn ʿAṭiyya consulté en ligne :</p>
<ul>
<li>« ce qu'ils désirent » (<em>mā yashtahūn</em>) (an-Naḥl, 57) : ils choisissent pour eux-mêmes les mâles et éprouvent du dégoût pour les femelles.</li>
<li>« une rage profonde » (<em>kazīm</em>) (an-Naḥl, 58) : silencieux, sous l'effet de l'intensité du chagrin qui l'emplit.</li>
<li>« Il se cache » (<em>yatawārā</em>) (an-Naḥl, 59) : il disparaît et s'absente, de peur que les gens ne le voient.</li>
<li>« à cause du malheur qu'on lui a annoncé » (<em>min sūʾ mā bushshira bih</em>) (an-Naḥl, 59) : le chagrin, l'opprobre et la pudeur mauvais qui s'abattent sur lui à cause de la fille.</li>
<li>« malgré la honte » (<em>ʿalā hūn</em>) (an-Naḥl, 59) : l'abjection et l'humiliation.</li>
<li>« l'enfouira-t-il » (<em>yadussuh</em>) (an-Naḥl, 59) : il l'ensevelit en cachette.</li>
<li>« Combien est mauvais leur jugement ! » (<em>alā sāʾ mā yaḥkumūn</em>) (an-Naḥl, 59) : c'est-à-dire qu'a péri leur prétention, qui consistait à attribuer les filles à Allah et à attribuer les garçons à eux-mêmes.</li>
</ul>
<h3>L'extraction des contenus des versets</h3>
<ol>
<li>Par quoi les associateurs ont-ils décrit les anges dans ces versets ?</li>
<li>Comment les versets ont-ils traité l'attitude des gens de la jāhiliyya envers la femelle ?</li>
</ol>
'''

FR4 = '''<h2>Le tafsīr</h2>
<h3>Premièrement : la sanctification d'Allah, le Très-Haut, de l'attribution des filles à Lui, et la réponse faite aux associateurs</h3>
<p>[En-tête « Premièrement » restauré avec adaptation : l'imprimé saute de l'ouverture du commentaire directement à l'en-tête « Deuxièmement », l'en-tête de la première section ayant disparu à la numérisation ; l'intitulé est reconstruit d'après le contenu conservé, en symétrie avec celui de la section suivante.]</p>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et ils assignent à Allah des filles. Gloire et pureté à Lui ! Et à eux-mêmes, cependant, (ils assignent) ce qu'ils désirent (des fils). » (an-Naḥl, 57)</p>
<p>[Citation coranique (an-Naḥl, 57 — l'ouverture du commentaire) restaurée d'après le corpus canonique : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>C'est-à-dire que l'ignorance de ces associateurs et l'énormité de leurs faux récits ont atteint un tel degré qu'ils assignent à Allah des filles, alors qu'Il est Celui qui dispose de leurs affaires et Celui à qui la gratitude est due ; ainsi qu'Allah, le Très-Haut, l'a dit :</p>
<p>« Ou bien Se serait-Il attribué des filles parmi ce qu'Il crée et accordé à vous par préférence des fils ? » (az-Zukhruf, 16)</p>
<p>[Citation coranique (az-Zukhruf, 16) restaurée d'après le corpus canonique à titre de candidat signalé : l'emplacement imprimé est un paragraphe vide ; le <em>Muḥarrar</em> original ne comporte pas, à cet endroit, d'appel de citation, et le verset retenu est le parallèle thématique le plus proche de la glose imprimée — l'identification demeure soumise à caution.]</p>
<p>Ils ont donc commis, en cela, une faute immense et se sont égarés d'un égarement lointain, du fait qu'ils ont attribué à Allah la descendance — en lui rapportant ce qu'ils n'auraient pas accepté pour eux-mêmes : la femelle.</p>
<p>Ainsi qu'Allah, le Très-Haut, l'a dit :</p>
<p>« Sera-ce à vous le garçon et à Lui la fille ? Que voilà donc un partage injuste ! » (an-Najm, 21-22)</p>
<p>[Citation coranique (an-Najm, 21-22) restaurée d'après le corpus canonique : la référence imprimée a subsisté dans la source numérisée, la citation qu'elle introduisait a disparu à la numérisation — perte OCR.]</p>
<p>Et Allah, le Très-Haut, a dit :</p>
<p>« Certes, ils disent dans leur mensonge : Allah a engendré. Mais ce sont certainement des menteurs ! » (aṣ-Ṣāffāt, 151-152)</p>
<p>[Citation coranique (aṣ-Ṣāffāt, 151-152) restaurée d'après le corpus canonique : la référence imprimée a subsisté dans la source numérisée, la citation qu'elle introduisait a disparu à la numérisation — perte OCR.]</p>
<p>Dans ce verset se trouve l'argument tiré de la faveur d'Allah envers eux — les garçons et les filles — qui est la faveur de la descendance ; et s'est trouvé fondu dans cet argument et dans cet acte de grâce le rappel d'une forme répugnante parmi les formes de leur mécréance : le fait d'inventer — de prétendre — que les anges seraient les filles d'Allah, glorifié soit-Il. La réponse à leur égard procède de deux voies :</p>
<ul>
<li>La première : attribuer une descendance à Allah, le Très-Haut, contredit l'attribut de l'unicité qui Lui est dû.</li>
<li>L'autre : ils ont attribué à Allah, parmi la descendance, la femelle — celle-là même qui leur était un objet de dégoût.</li>
</ul>
<p>Et Allah, le Très-Haut, a mis en évidence l'énormité de cette invention en disant, gloire à Lui :</p>
<p>« Vous avancez certes là une chose abominable ! Peu s'en faut que les cieux ne s'entrouvrent à ces mots, que la terre ne se fende et que les montagnes ne s'écroulent, du fait qu'ils ont attribué un enfant au Tout Miséricordieux, alors qu'il ne convient nullement au Tout Miséricordieux d'avoir un enfant ! Tous ceux qui sont dans les cieux et sur la terre se rendront auprès du Tout Miséricordieux, (sans exception), en serviteurs. Il les a certes dénombrés et bien comptés. » (Maryam, 89-94)</p>
<p>[Citation coranique (Maryam, 89-94 — six versets) restaurée d'après le corpus canonique : la référence imprimée a subsisté dans la source numérisée, la citation qu'elle introduisait a disparu à la numérisation — perte OCR.]</p>
'''

FR5 = '''<h3>Deuxièmement : l'exposé de la situation des gens de la jāhiliyya lorsqu'il naît à l'un d'eux une femelle</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et lorsqu'on annonce à l'un d'eux une fille, son visage s'assombrit et une rage profonde (l'envahit). » (an-Naḥl, 58)</p>
<p>[Citation coranique (an-Naḥl, 58) restaurée d'après le corpus canonique : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>La « bonne annonce » : dans la langue, à l'origine, le fait de transmettre une information réjouissante, celle qui agit sur le changement de l'éclat du visage. L'expression de l'information par l'augmentation de la femelle, de par son fait, vise deux bénéfices :</p>
<ul>
<li>Le premier : c'est une bonne annonce véritable, car l'augmentation du nouveau-né est une faveur pour le parent, vu ce qu'il attend de la compagnie de l'enfant, du bénéfice de son service et du fait d'accroître la descendance de la famille.</li>
<li>La seconde : elle vise à exprimer la moquerie à leur égard — et cela relève du sens figuré.</li>
</ul>
<p>Et la parole d'Allah, le Très-Haut :</p>
<p>« son visage s'assombrit » (<em>ẓalla wajhuhu muswaddan</em>)</p>
<p>[Citation coranique (an-Naḥl, 58 — le tronçon « son visage s'assombrit ») restaurée d'après le corpus canonique : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>— elle exprime le renfrognement et le froncement de sourcils qui saisissent l'homme accablé de chagrin. Le visage du chagriné peut parfois se couvrir de noirceur et perdre sa clarté ; c'est pourquoi on le décrit par la noirceur, et les Arabes disent de quiconque rencontre une chose pénible : son visage s'est assombri de tristesse et de chagrin.</p>
<p>Et</p>
<p>« la rage profonde » (<em>kazīm</em>)</p>
<p>[Citation coranique (an-Naḥl, 58 — le tronçon « la rage profonde ») restaurée d'après le corpus canonique : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>— c'est-à-dire empli de tristesse et de chagrin. Le <em>kazm</em> : l'issue du souffle ; on dit : il a saisi son <em>kazm</em>, lorsqu'il a saisi l'issue de son souffle ; et de là : il a contenu sa colère — c'est-à-dire qu'il l'a retenue de parvenir jusqu'à l'issue du souffle.</p>
<p>Et la parole d'Allah, le Très-Haut :</p>
<p>« Il se cache des gens, à cause du malheur qu'on lui a annoncé. » (an-Naḥl, 59)</p>
<p>[Citation coranique (an-Naḥl, 59 — l'ouverture) restaurée d'après le corpus canonique : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>Ce retrait dont Allah, le Très-Haut, fait mention n'intervient qu'après la bonne annonce de la femelle. L'homme, du temps de la jāhiliyya, lorsque sa femme lui donnait naissance à une fille, se retirait des regards sous l'effet de la honte qui s'emparait de lui, et demeurait tiraillé entre garder sa petite dans l'humiliation et la bassesse, ou l'enterrer vivante. Et Allah a considéré cet acte infâme comme un jugement injuste, en disant :</p>
<p>« Doit-il la garder malgré la honte ou l'enfouira-t-il dans la terre ? » (an-Naḥl, 59)</p>
<p>[Citation coranique (an-Naḥl, 59 — l'alternative) restaurée d'après le corpus canonique : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>Et Allah s'est adressé à eux en disant :</p>
<p>« Combien est mauvais leur jugement ! » (an-Naḥl, 59)</p>
<p>[Citation coranique (an-Naḥl, 59 — la clôture) restaurée d'après le corpus canonique : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>— en marque de réprobation envers cet injuste et immense forfait.</p>
<p>Le Coran généreux a honoré la femelle, lui a assigné des droits à l'égal des devoirs qui incombent sur elle, a rendu obligatoire son éducation, son instruction et le bienfait à son égard, et a rattaché à cela une récompense généreuse et une rétribution immense. D'après ʿĀʾisha, qu'Allah l'agrée : une femme démunie vint me trouver, portant ses deux filles ; je lui donnai trois dattes, et elle en donna une à chacune d'elles ; puis elle leva vers sa bouche une datte pour la manger, et ses deux filles la lui demandèrent ; elle rompit alors la datte qu'elle allait manger et la partagea entre elles. Son comportement m'admira, et je rapportai au Messager d'Allah (prière et salut d'Allah sur lui) ce qu'elle avait fait. Il dit :</p>
<p>« Allah lui a certes assigné, à cause d'elles, le Paradis — ou l'a affranchie, par elles, du Feu. »</p>
<p>[Recueil de Muslim, livre de la bonté, des liens de parenté et des bonnes manières, chapitre de l'excellence du bienfait envers les filles.]</p>
<p>Et Abū Nuʿaym, le <em>ḥāfiẓ</em>, a rapporté, dans un hadith d'Abū Wāʾil, d'après ʿAbdallāh — qu'Allah l'agrée — que le Messager d'Allah (prière et salut d'Allah sur lui) a dit :</p>
<p>« Quiconque a une fille, qu'il l'éduque en la bien éduquant, qu'il l'instruise en la bien enseignant, et qu'il répande sur elle des faveurs d'Allah dont Il l'a comblé, lui — elle lui sera une protection et un voile contre le Feu. »</p>
<p>[Sounan d'Ibn Mājah, livre du mariage, chapitre de l'homme qui affranchit sa servante puis l'épouse.]</p>
'''

FR6 = '''<h2>L'évaluation</h2>
<ol>
<li>Décris la situation des gens de la jāhiliyya lorsqu'un homme est informé de la naissance d'une femelle.</li>
<li>Comment réponds-tu à celui qui attribue des filles à Allah, le Très-Haut ?</li>
<li>Comment Allah, le Très-Haut, a-t-il corrigé la vision des associateurs envers la femelle ?</li>
</ol>
<h2>L'exploitation</h2>
<p>ʿAlī Muḥammad ʿAlī aṣ-Ṣallābī écrit : « Les Arabes tournaient les filles en reproche ; car la fille ne part pas en campagne, ne défend pas le foyer contre les agresseurs, ne travaille pas pour rapporter des richesses à la manière des hommes ; et si elle est faite captive, elle devient un objet de bas service, que des mains se renvoient pour cela. Bien plus, on la contraint parfois à exercer la prostitution, afin que son maître joigne à sa richesse ce qui parvient à elle par la prostitution ; et les Arabes toléraient cela. Et cela engendrait pour le père l'angoisse, le chagrin et la honte lorsque lui naissait une fille… Aussi choisissaient-ils souvent de l'enfouir dans la poussière, de l'enterrer vivante — sans autre faute à sa charge que d'être une femelle. C'est pourquoi le Coran généreux a réprouvé à leur égard cet acte infâme, en disant : »</p>
<p>« Et qu'on demandera à la fillette enterrée vivante pour quel péché elle a été tuée. » (at-Takwīr, 8-9)</p>
<p>[Citation coranique (at-Takwīr, 8-9) restaurée d'après le corpus canonique : la référence imprimée a subsisté dans la source numérisée, la citation qu'elle introduisait a disparu à la numérisation — perte OCR.]</p>
<p>[La vie prophétique d'ʿAlī Muḥammad ʿAlī aṣ-Ṣallābī, p. 28 — cité avec adaptation.]</p>
<ul>
<li>Montre, à partir du texte et à partir de tes acquis, comment l'islam a traité l'attitude des gens de la jāhiliyya envers la femelle, et quels sont les droits qu'il lui a garantis.</li>
</ul>
'''

FR7 = '''<h2>La préparation préalable</h2>
<p>Lis les versets (57-62) de la sourate an-Naḥl et réponds à ce qui suit :</p>
<ol>
<li>Explique les mots suivants :</li>
</ol>
<p>[La liste des mots imprimée a disparu à la numérisation : quatre emplacements vides subsistent dans la source ; les expressions relevaient des versets (57-62) de la sourate an-Naḥl, dont les leçons suivantes du fil traitent la suite — non reconstituée.]</p>
<ol>
<li>Montre, d'après les versets, la description qu'Allah, le Très-Haut, donne de ceux qui traitent de mensonge le Jour dernier.</li>
<li>Déduis des versets la sagesse d'Allah dans le sursis qu'Il accorde aux pécheurs.</li>
</ol>
<h2>Notes du traducteur</h2>
<p><em>N.d.T. —</em> Cas limite du chantier, sixième leçon consécutive du fil : leçon de tafsīr dont le matériau versical a disparu à la numérisation. La section imprimée « Les versets » est vide en son entier — le bloc principal (an-Naḥl, 57-59) y a été restauré. Vingt restaurations coraniques au total, d'après le corpus canonique et vérifiées au cache coranique du corpus : le bloc principal an-Naḥl 57-59 ; les sept tronçons coraniques du tableau de compréhension, dont les sept interprétations imprimées seules ont survécu (an-Naḥl 57 — <em>mā yashtahūn</em> ; an-Naḥl 58 — <em>kazīm</em> ; an-Naḥl 59 — <em>yatawārā</em>, <em>min sūʾ mā bushshira bih</em>, <em>ʿalā hūn</em>, <em>yadussuh</em>, <em>alā sāʾ mā yaḥkumūn</em>) ; les sept emplacements coraniques vides du commentaire (an-Naḥl 57 l'ouverture du commentaire, an-Naḥl 58, les deux tronçons de l'analyse lexicale — « son visage s'assombrit » et « la rage profonde » —, an-Naḥl 59 l'ouverture, l'alternative et la clôture) ; et les quatre citations disparues au sein de références imprimées subsistantes (an-Najm 21-22, aṣ-Ṣāffāt 151-152, Maryam 89-94, at-Takwīr 8-9 — classe 13478), soit un candidat signalé en sus (az-Zukhruf 16).</p>
<p><em>N.d.T. —</em> Méthode : le <em>Muḥarrar al-wajīz</em> original d'Ibn ʿAṭiyya, consulté en ligne dans une édition numérique de référence, a de nouveau servi d'autorité de tranchage : la glose orpheline « ils choisissent pour eux-mêmes les mâles » s'apparie au tronçon <em>mā yashtahūn</em> par le commentaire du <em>Muḥarrar</em> (« ce qu'ils désirent : les mâles parmi les enfants ») ; la glose « silencieux, sous l'effet de l'intensité du chagrin » au tronçon <em>kazīm</em> (« <em>kazīm</em> au sens de <em>kāzim</em>… il dissimule sa douleur ») ; les gloses « il disparaît », « l'abjection », « il l'ensevelit en cachette » aux tronçons <em>yatawārā</em>, <em>ʿalā hūn</em> et <em>yadussuh</em> (« le retrait… il disparaît », « l'humiliation », « il l'ensevelit et l'enterre vivante — tel est l'ensevelissement dans la poussière ») ; les tronçons lexicaux du commentaire (« son visage s'assombrit », « la rage profonde ») sont ceux que le <em>Muḥarrar</em> commente mot pour mot (« l'expression du renfrognement et du froncement de sourcils »). L'appel imprimé « ainsi qu'Allah l'a dit » resté sans objet identifiable (paragraphe vide) est pourvu d'un candidat signalé — az-Zukhruf 16, parallèle thématique le plus proche. L'en-tête « Premièrement » de la première section du commentaire est perdu (l'imprimé saute directement à « Deuxièmement ») ; l'intitulé est restauré avec adaptation, en symétrie avec celui de la section suivante, le contenu conservé intégralement.</p>
<p><em>N.d.T. —</em> Les douze irrégularités de l'imprimé comptées : (1) la fente de définition vide sous le titre — huitième occurrence ; (2) la section « Les versets » vide en son entier — sixième cas consécutif du livre ; (3) les sept gloses orphelines du tableau de compréhension — classe 13518 ; (4) l'en-tête « Premièrement » perdu — classe nouvelle ; (5) les huit emplacements coraniques vides du commentaire, dont un candidat ; (6) les quatre citations disparues au sein de références imprimées subsistantes — classe 13478 ; (7) la liste de mots de la préparation préalable perdue — quatre emplacements ; (8) la tension d'attribution du second hadith, imputé par l'imprimé à Abū Nuʿaym le <em>ḥāfiẓ</em> puis abrégé sous le Sounan d'Ibn Mājah ; (9) le tatwīl médian parasite — sixième leçon consécutive ; (10) le marqueur d'adresse genré entre parenthèses, retenu comme second intitulé de la première question de l'évaluation — deuxième leçon consécutive ; (11) les coquilles de collage ; (12) les résidus de fermeture et le paragraphe vide. Signalés NON comptés : l'ordre inversé de la référence an-Najm imprimée (22-21) ; la coïncidence numérique entre la leçon 11 du manuel et le badge de page ; la divergence de lecture <em>ʿalā hūn</em> / <em>ʿalā huwan</em> / <em>ʿalā sūʾ</em> attestée par le <em>Muḥarrar</em> et non reproduite par l'imprimé.</p>
<p><em>N.d.T. —</em> Les versions françaises des versets sont reprises du cache coranique du corpus ; le tronçon « Allah a engendré » conservait dans la version du cache des guillemets internes, reformattés pour l'appariement ; le verset 8 d'at-Takwīr, s'inscrivant dans la continuation du verset 7, a vu son initiale portée en majuscule. La glose orpheline « le chagrin, l'opprobre et la pudeur mauvais » a été rendue d'après le texte imprimé tel quel, l'ordre des termes étant celui de la source.</p>
'''

# === ASSEMBLAGE ===
html = FR1 + FR2 + FR3 + FR4 + FR5 + FR6 + FR7

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

out = '/home/z/my-project/tr-tmp/13519.html'
open(out, 'w').write(html)
print('écrit:', out)
