#!/usr/bin/env python3
# build-13590.py — leçon 13590 « Sourate An-Nahl, versets 86-89 » (tafsir-tanawi-1, lessons[19], badge Leçon 21/32)
# Trame 13587 (R282). ZÉRO script arabe dans tout le htmlFr (auto-vérif ; U+FDFA exempté — convention du fil).
# VINGT-QUATRE restaurations coraniques (cache) : bloc principal 86-89 (section vide entière, 13ᵉ cas) + 23 emplacements
# vides du commentaire (DIX sans span, DOUZE avec span juste, DEUX spans erronés) ; DEUX spans subsistants ERRONÉS tranchés (al-Aʿrāf « 5 » → 6 ; al-Anʿām « 27 » → 26 — 4ᵉ et 5ᵉ cas
# du fil (aa)) ; DEUX emplacements confirmés MOT POUR MOT au Muḥarrar (الضمير في {ألقوا} عائد على المشركين ;
# الحكمة في قوله {من أنفسهم}) ; UN emplacement à caution (الضمير في قوله — {أقول} du Muḥarrar en ligne, lecture
# raisonnable {فألقوا إليهم القول}) ; EXCEPTION FAVORABLE : les 3 hadiths (Bukhārī, Aḥmad, Tirmidhī), la citation
# d'Ibn ʿAṭiyya et la longue citation du Qurṭubī (I/37-39, بتصرف) subsistent INTACTES ; gloses du الشرح AVEC leurs
# mots (aucune règle (y)) ; liste de mots de l'iʿdād perdue (11ᵉ occurrence) ; Muḥarrar original consulté en ligne
# (quran-tafsir.net/atia, sura16 aya86-89 — fetch 4/4 OK).
import json, os, re

FR1 = '''<h1>La sourate an-Naḥl — <em>al-Muḥarrar al-wajīz</em> d'Ibn ʿAṭiyya, versets 86 à 89</h1>
<p>Leçon de tafsīr — sourate an-Naḥl, versets (86-89) — tirée du livre <em>al-Tafsīr min khilāl al-Muḥarrar al-wajīz fī tafsīr al-Kitāb al-ʿazīz</em> d'Ibn ʿAṭiyya, au profit des élèves de la première année de l'enseignement secondaire ancien, première étape (leçon 19 du manuel — la dix-neuvième du fil consacré au Naḥl).</p>
<ol>
<li>Me familiariser avec le sens des mots des āyāt, et en déterminer les contenus.</li>
<li>Dégager des āyāt des scènes de l'état des associateurs au Jour de la Résurrection.</li>
<li>Tirer profit de la guidance du Coran et de son éclaircissement dans tous les domaines de la vie.</li>
</ol>
<h2>Introduction</h2>
<p>Après que la leçon précédente a exposé l'énumération qu'Allah, le Très-Haut, fit d'un ensemble de Ses graces envers Ses serviteurs, le démenti que les associateurs opposèrent à ces graces et leur reniement, ainsi que la menace d'Allah, le Très-Haut, aux associateurs pour cela, ces āyāt ont poursuivi l'exposé de quelques scènes de l'état des associateurs au Jour de la Résurrection, et de la manière dont ils se soumettront, une fois disparue l'égarément qui les voilait et manifestée la vérité. De même, les āyāt ont exposé le témoignage des prophètes contre leurs peuples, par leur transmission du message et leur éclaircissement du message d'Allah envers eux, ainsi que le témoignage du Prophète, que la bénédiction d'Allah et la paix soient sur lui, contre cette communauté. Les āyāt se sont closes sur l'exposé du dessein de la descente du noble Coran, par lequel Allah a établi la preuve contre les serviteurs.</p>
<p>Quelles sont donc les scènes que les āyāt ont peintes de l'état des associateurs au Jour de la Résurrection ? Et comment tirons-nous profit de la guidance du noble Coran dans notre conduite et notre vie quotidienne ?</p>
'''

FR2 = '''<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Quand ceux qui associaient verront ceux qu'ils associaient [à Allah], ils diront : "Ô notre Seigneur, voilà nos associés, ceux que nous invoquions en dehors de Toi" — et [leurs associés] leur jetteront la parole : "Assurément, vous êtes des menteurs". Ils offriront ce jour-là à Allah la soumission, et s'évanouira d'eux ce qu'ils forgeaient. Ceux qui ont mécru et ont détourné du sentier d'Allah — Nous leur ajouterons un châtiment au-dessus du châtiment, pour ce qu'ils corrompaient. Et [rappelle] le jour où Nous susciterons, dans chaque communauté, un témoin contre eux, du milieu d'eux-mêmes ; et Nous t'amènerons comme témoin contre ceux-ci. Et Nous avons fait descendre sur toi le Livre, éclaircissement de toute chose, guidance, miséricorde et bonne annonce pour les soumis [à Allah]. » (an-Naḥl, 86-89)</p>
<p>[Citation coranique (an-Naḥl, 86-89 — le bloc entier des versets de la leçon) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la section imprimée « Les versets » est vide dans la source numérisée, le bloc versical tout entier ayant disparu à la numérisation — perte OCR — treizième cas consécutif du fil. Le muṣḥaf porte, à la fin de l'āya 86, la formule « assurément, vous êtes des menteurs » avec <em>inna</em> ; et, à l'āya 89, « Nous avons fait descendre » avec le renforcement <em>nassala</em>.]</p>
<p><span>an-Naḥl : 86 - 89</span></p>
<h3>L'explication des mots</h3>
<p>[Les six explications subsistantes de la source numérisée portaient TOUTES leurs mots-têtes — exception favorable du fil : à la différence des trois occurrences de la règle (y) (leçons 13537, 13585 et 13587), aucune tête ne manque ici ; les mots expliqués ont été reconstitués d'après l'ordre des versets et l'appariement mot pour mot au commentaire du manuel et au <em>Muḥarrar</em> original consulté en ligne.]</p>
<ul>
<li>« la soumission » (<em>as-salām</em>) : se livrer, s'humilier et obéir à Son jugement rendu parmi eux.</li>
<li>« et s'évanouit » (<em>wa-ḍalla</em>) : et cessa d'être.</li>
<li>« ils forgeaient » (<em>yaftarūna</em>) : ils fabriquaient le mensonge.</li>
<li>« et ont détourné du sentier d'Allah » (<em>wa-ṣaddū ʿan sabīli llāhi</em>) : ils ont empêché les gens d'obéir à Allah.</li>
<li>« un témoin » (<em>šahīdan</em>) : un messager, témoin contre sa communauté au Jour de la Résurrection, qu'il a bien transmis le message.</li>
<li>« un éclaircissement » (<em>tibyānan</em>) : un exposé clair des affaires de la religion.</li>
</ul>
<h3>L'extraction des contenus des versets</h3>
<ol>
<li>Dégage des āyāt les états des associateurs au Jour de la Résurrection.</li>
<li>De quoi les prophètes témoignent-ils contre leurs peuples au Jour de la Résurrection ?</li>
<li>Quelles sont les sagesses pour lesquelles Allah, le Très-Haut, a fait descendre le noble Coran ?</li>
</ol>
'''

FR3 = '''<h2>Le commentaire</h2>
<p>Les āyāt ont comporté ce qui suit :</p>
<h3>Premièrement : l'évocation de scènes de l'état des associateurs au Jour de la Résurrection</h3>
<p>Les āyāt ont comporté l'exposé de deux scènes de l'état des associateurs au Jour de la Résurrection, lorsqu'ils comparaîtront devant Allah et découvriront la vérité qu'ils reniaient en ce bas monde. Ces deux scènes sont :</p>
<p><strong>L'incrimination de leurs divinités.</strong> Allah, le Très-Haut, a dit :</p>
<p>« Quand ceux qui associaient verront ceux qu'ils associaient [à Allah], ils diront : "Ô notre Seigneur, voilà nos associés, ceux que nous invoquions en dehors de Toi" — et [leurs associés] leur jetteront la parole : "Assurément, vous êtes des menteurs". » (an-Naḥl, 86)</p>
<p>[Citation coranique (an-Naḥl, 86 — l'āya de la scène d'incrimination) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Allah, le Très-Haut, a dit » est vide dans la source numérisée, SANS span subsistant — perte OCR ; le verset retenu est celui que l'āya-tête de la leçon et le commentaire subsistant du manuel (« quand ces associateurs verront de la vue d'œil… ») désignent.]</p>
<p>c'est-à-dire : lorsque ces associateurs d'Allah verront, au Jour de la Résurrection, de la vue d'œil, ce qu'ils adoraient en dehors d'Allah, des idoles et des divinités, ils leur feront signe et diront : ceux-ci sont nos associés dans la mécréance envers Toi, ceux que nous invoquions comme divinités en dehors de Toi. Il se peut qu'ils aient tenu ce propos dans l'espoir de faire répartir le châtiment entre eux, ou de renvoyer la faute sur eux — tout en sachant que le châtiment les atteindra fatalement. Mais tel est le cas du noyé : il s'accroche à tout ce que sa main peut saisir comme moyens, alors même qu'il sait qu'ils ne sauvent ni ne profitent.</p>
<p>Allah, le Très-Haut, a de même mentionné que leurs divinités se désavouent d'eux, alors qu'ils sont au plus grand besoin d'un appui en leur faveur. Il a dit :</p>
<p>« …et [leurs associés] leur jetteront la parole : "Assurément, vous êtes des menteurs". » (an-Naḥl, 86 — la fin)</p>
<p>[Citation coranique (an-Naḥl, 86 — le tronçon du désaveu des divinités) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Il a dit » est vide dans la source numérisée, SANS span subsistant ; le tronçon retenu est celui que la glose imprimée du manuel (« les divinités leur dirent : vous avez menti sur nous… ») et le <em>Muḥarrar</em> original (aṭ-Ṭabarī : « nous ne vous avons jamais appelés à notre adoration ») commentent mot pour mot.]</p>
<p>c'est-à-dire : les divinités leur dirent : vous avez menti sur nous ; nous ne vous avons jamais ordonné de nous adorer. Et une āya de même sens est la parole du Très-Haut :</p>
<p>« Dis : "Que pensez-vous de ceux que vous invoquez en dehors d'Allah ? Montrez-moi ce qu'ils ont créé de la terre ! Ou ont-ils dans les cieux une association [avec Dieu] ? Apportez-moi un Livre antérieur à celui-ci, ou un vestige d'une science, si vous êtes véridiques". — Et qui est plus égaré que celui qui invoque, en dehors d'Allah, celui qui ne lui répondra pas jusqu'au Jour de la Résurrection, alors qu'ils sont distraits de leur invocation ? » (al-Aḥqāf, 4-5)</p>
<p>[Citation coranique (al-Aḥqāf, 4-5) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « une āya de même sens est la parole du Très-Haut » est vide dans la source numérisée ; le span subsistant « al-Aḥqāf : 4 - 5 » est correct et a été suivi tel quel.]</p>
<p>et Sa parole :</p>
<p>« Bien au contraire ! Ces divinités renieront leur adoration, et seront contre eux des adversaires. — N'as-tu pas vu que Nous envoyons contre les mécréants des diables qui les excitent furieusement [à désobéir] ? » (Maryam, 82-83)</p>
<p>[Citation coranique (Maryam, 82-83) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « et Sa parole » est vide dans la source numérisée ; le span subsistant « Maryam : 82 - 83 » est correct et a été suivi tel quel.]</p>
<p>et le pronom dans Sa parole :</p>
<p>« …et [leurs associés] leur jetteront la parole… » (an-Naḥl, 86)</p>
<p>[Citation coranique (an-Naḥl, 86 — le tronçon du pronom) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « et le pronom dans Sa parole » est vide dans la source numérisée, SANS span subsistant ; identification raisonnable soumise à caution : l'édition en ligne du <em>Muḥarrar</em> porte « le pronom dans <em>aqūl</em> » — forme manifestement altérée à la collation — et enchaîne immédiatement la glose que le manuel reprend MOT POUR MOT (« celui des adorés qui était humain lança la parole habituelle de sa langue ; ce qui était inanimé parla par la puissance d'Allah ») ; le tronçon retenu est celui dont le sujet et le régime portent les pronoms renvoyant aux associés — l'āya 86, « et ils leur jetteront la parole ».]</p>
<p>renvoie aux associés. Celui, parmi les associés adorés, qui était humain, répondit de sa langue habituelle et démentit la forgery des associateurs ; et ce qui était inanimé parla par la puissance d'Allah, démentant la prétention des associateurs qui les décrivaient comme divinités et associés d'Allah.</p>
<p><strong>La manifestation de la soumission et de l'humilité.</strong> Allah, le Très-Haut, a dit :</p>
<p>« Ils offriront ce jour-là à Allah la soumission, et s'évanouira d'eux ce qu'ils forgeaient. » (an-Naḥl, 87)</p>
<p>[Citation coranique (an-Naḥl, 87) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Allah, le Très-Haut, a dit » est vide dans la source numérisée, SANS span subsistant ; l'āya retenu est celle que les gloses subsistantes du manuel (« la soumission », « et s'évanouit », « ils forgeaient ») désignent, appariées au <em>Muḥarrar</em>.]</p>
<p>c'est-à-dire : l'adorateur et l'adoré se soumirent à Allah. Nul, au Jour de la Résurrection, qui ne soit entendant et obéissant. Et une āya de même sens est la parole du Très-Haut :</p>
<p>« Les sectes divergèrent entre elles ; alors, malheur aux mécréants, du spectacle d'un jour terrible. » (Maryam, 37)</p>
<p>[Citation coranique (Maryam, 37) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « une āya de même sens est la parole du Très-Haut » est vide dans la source numérisée ; le span subsistant « Maryam : 37 » a été suivi tel quel ; remarque d'identification : la glose imprimée du manuel (« combien ils entendront et verront à ce moment-là ») s'accorde plus volontiers à la formule d'ouïe-et-de-vue de la citation suivante (as-Sajda, 12) qu'à la lettre de l'āya 37 — l'appariement suit l'ordre des étiquettes subsistantes.]</p>
<p>c'est-à-dire : combien ils entendront et verront à ce moment-là. Et Sa parole :</p>
<p>« Si tu voyais alors les criminels, têtes basses devant leur Seigneur : "Notre Seigneur, nous avons vu et entendu ; renvoie-nous donc, nous œuvrerons en bien ; assurément nous sommes convaincus". » (as-Sajda, 12)</p>
<p>[Citation coranique (as-Sajda, 12) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Et Sa parole » est vide dans la source numérisée ; le span subsistant « as-Sajda : 12 » est correct et a été suivi tel quel.]</p>
<p>et Sa parole :</p>
<p>« Ce jour-là, ils suivront le Convocateur, sans tortuosité ; et les voix s'humilieront devant le Tout Miséricordieux, si bien que tu n'entendras qu'un chuchotement. » (Ṭāhā, 108)</p>
<p>[Citation coranique (Ṭāhā, 108) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « et Sa parole » est vide dans la source numérisée ; le span subsistant « Ṭāhā : 108 » est correct et a été suivi tel quel.]</p>
<p>c'est-à-dire : elles s'humilièrent et se soumirent.</p>
<p>et le pronom dans :</p>
<p>« …et ils offriront à Allah ce jour-là la soumission… » (an-Naḥl, 87)</p>
<p>[Citation coranique (an-Naḥl, 87 — le tronçon du pronom) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « et le pronom dans » est vide dans la source numérisée, SANS span subsistant ; l'appariement est confirmé MOT POUR MOT au <em>Muḥarrar</em> original consulté en ligne : « le pronom dans <em>alqaw</em> renvoie aux associateurs, le sens étant : ils lui livrèrent la soumission, abandonnèrent ce qui était en leurs mains et s'humilièrent à Son jugement ».]</p>
<p>renvoie aux associateurs. Le sens : ils livrèrent à Lui la soumission, abandonnèrent ce qui était en leurs mains, s'humilièrent à Son jugement — sans ruse ni pouvoir de se défendre eux-mêmes.</p>
'''

FR4 = '''<p>et Sa parole :</p>
<p>« …et s'évanouira d'eux ce qu'ils forgeaient. » (an-Naḥl, 87 — la fin)</p>
<p>[Citation coranique (an-Naḥl, 87 — le tronçon de l'évanouissement) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « et Sa parole » est vide dans la source numérisée, SANS span subsistant ; le tronçon retenu est celui que la glose imprimée du manuel (« s'évanouit d'eux ce qu'ils adoraient en forgerie contre Allah, idoles et simulacres ») et le <em>Muḥarrar</em> (« s'évanouit d'eux leur mensonge contre Allah et leur forgery de la mécréance et de l'association ») commentent mot pour mot.]</p>
<p>c'est-à-dire : s'évanouit d'eux ce qu'ils adoraient en forgerie contre Allah, idoles et simulacres. Nul soutien pour eux, nul secours, nul intercesseur — de ce qu'ils prétendaient en ce bas monde —, comme le Très-Haut a dit, en rapportant leur parole :</p>
<p>« Et ils adorent, en dehors d'Allah, ce qui ne leur nuit ni ne leur profite, et disent : "Ceux-ci sont nos intercesseurs auprès d'Allah". Dis : "Informerez-vous Allah de ce qu'Il ne connaît pas, dans les cieux ni sur la terre ?" Pureté à Lui ! Il est Très-Élevé au-dessus de ce qu'Il associent. » (Yūnus, 18)</p>
<p>[Citation coranique (Yūnus, 18) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « en rapportant leur parole » est vide dans la source numérisée ; le span subsistant « Yūnus : 18 » est correct et a été suivi tel quel.]</p>
<p>et Sa parole :</p>
<p>« Ceux qui ont mécru et ont détourné du sentier d'Allah — Nous leur ajouterons un châtiment au-dessus du châtiment, pour ce qu'ils corrompaient. » (an-Naḥl, 88)</p>
<p>[Citation coranique (an-Naḥl, 88) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « et Sa parole » est vide dans la source numérisée, SANS span subsistant ; l'āya retenu est celle que le commentaire subsistant du manuel (« ceux qui ont nié ta prophétie… Il leur ajoute un châtiment au-dessus de leur châtiment ») désigne, apparié au <em>Muḥarrar</em>.]</p>
<p>Cette āya concerne celui qui a réuni l'égarement en lui-même et l'égarement d'autrui. Le sens : ceux qui ont nié ta prophétie, t'ont traité de menteur dans ce que tu leur as apporté de la part de ton Seigneur, et ont détourné de la foi en Allah et en Son messager — Il leur ajoute un châtiment au-dessus du châtiment qu'ils méritent pour leur mécréance, en raison de leur appel qui éloigne les gens du sentier d'Allah.</p>
<p>Ainsi, Allah châtie de tels gens d'un double châtiment : un châtiment pour la mécréance, et un châtiment pour l'égarement d'autrui et la déviation des gens du suivi de la vérité. Et une āya de même sens est la parole du Très-Haut :</p>
<p>« Et eux-mêmes, ils interdisent [aux gens de s'approcher] de lui et s'en écartent ; ils ne font périr qu'eux-mêmes, sans s'en rendre compte. » (al-Anʿām, 26)</p>
<p>[Citation coranique (al-Anʿām, 26) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « une āya de même sens est la parole du Très-Haut » est vide dans la source numérisée ; le span subsistant portait « al-Anʿām : 27 » — SPAN ERRONÉ, tranché d'après la formule glosée par le commentaire du manuel : « ils interdisent aux gens de le suivre, eux-mêmes s'en écartant aussi » est la lettre même de l'āya 26 (« et ils interdisent de lui et s'en écartent »), là où l'āya 27 porte le stationnement devant le Feu et le vœu de retour — quatrième leçon du fil où un span subsistant se révèle erroné (après le « 237/2 », le « la Vache, 252 » et le « az-Zalzala, 8-9 ») ; règle (aa) re-confirmée.]</p>
<p>c'est-à-dire : ils interdisent aux gens de le suivre, eux-mêmes s'en écartant aussi.</p>
<p>Et l'āya est une preuve de la gradation des mécréants dans leur châtiment, comme les croyants varient dans leurs demeures et leurs degrés au Paradis.</p>
<h3>Deuxièmement : le témoignage des prophètes contre leurs peuples au Jour de la Résurrection</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et [rappelle] le jour où Nous susciterons, dans chaque communauté, un témoin contre eux, du milieu d'eux-mêmes ; et Nous t'amènerons comme témoin contre ceux-ci. Et Nous avons fait descendre sur toi le Livre, éclaircissement de toute chose, guidance, miséricorde et bonne annonce pour les soumis [à Allah]. » (an-Naḥl, 89)</p>
<p>[Citation coranique (an-Naḥl, 89 — l'āya du témoignage) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Allah, le Très-Haut, a dit » est vide dans la source numérisée, SANS span subsistant ; l'āya retenu est celle que le commentaire subsistant du manuel (« rappelle la terreur de ce jour où Allah suscitera le prophète de chaque communauté, témoin contre son peuple ») désigne ; le muṣḥaf porte « Nous avons fait descendre » avec le renforcement <em>nassala</em>.]</p>
<p>Cette āya est une adresse au Messager, que la bénédiction d'Allah et la paix soient sur lui : rappelle la terreur de ce jour où Allah suscitera le prophète de chaque communauté, témoin contre son peuple ; et où tu viendras, ô Muhammad, témoin contre ta communauté, de leur réponse à ton appel et de leurs actes envers ton message. À ce stationnement, Allah coupe toute excuse à qui s'excuse, et y achève la preuve contre quiconque a traité de mensonge l'appel des prophètes et des messagers.</p>
<p>Cette āya ressemble à celle où parvint ʿAbdallāh b. Masʿūd, lorsqu'il récita devant le Messager d'Allah, que la bénédiction d'Allah et la paix soient sur lui, la sourate an-Nisāʾ. Lorsqu'il atteignit Sa parole :</p>
<p>« Comment seront-ils lorsque Nous amènerons, de chaque communauté, un témoin, et que Nous t'amènerons comme témoin contre ceux-ci ? » (an-Nisāʾ, 41)</p>
<p>[Citation coranique (an-Nisāʾ, 41) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « lorsqu'il atteignit Sa parole » est vide dans la source numérisée ; le span subsistant « an-Nisāʾ : 41 » est correct et a été suivi tel quel — l'āya 41 de la sourate an-Nisāʾ étant précisément celle où parvint Ibn Masʿūd, comme le hadith subsistant de la source l'atteste.]</p>
<p>le Messager d'Allah, que la bénédiction d'Allah et la paix soient sur lui, lui dit : « Cela te suffit maintenant » ; et Ibn Masʿūd dit : « Je me détournaïs — et voilà ses deux yeux qui laissaient couler des larmes ». [Ṣaḥīḥ al-Bukhārī, livre des mérites du Coran, chapitre de la parole du récitant « cela te suffit »]</p>
<p>Cette āya comporte une menace aux associateurs : Allah fait témoigner contre eux un messager du milieu d'eux-mêmes, dont ils connaissent la véracité et la fidélité, et qui a vu, en ce bas monde, leur reniement et leur mécréance. Ibn ʿAṭiyya, qu'Allah lui fasse miséricorde, a dit : il se peut qu'Allah suscite un témoin parmi les justes, avec les messagers. Et certains Compagnons ont dit : si tu vois quelqu'un en désobéissance, prohibe-la-lui ; s'il t'obéit — sinon, tu seras témoin contre lui au Jour de la Résurrection.</p>
<p>La sagesse dans Sa parole :</p>
<p>« …un témoin contre eux, du milieu d'eux-mêmes… » (an-Naḥl, 89)</p>
<p>[Citation coranique (an-Naḥl, 89 — le tronçon « du milieu d'eux-mêmes ») restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « La sagesse dans Sa parole » est vide dans la source numérisée, SANS span subsistant ; l'appariement est confirmé MOT POUR MOT au <em>Muḥarrar</em> original consulté en ligne : « <em>min anfusihim</em> — selon que la mission des messagers fut de même en ce bas monde : le messager qui est de la communauté même, quant à la langue, aux mœurs, à la compréhension des visées et des allusions… ».]</p>
<p>est que le messager suscité au sein même de la communauté — quant à la langue, aux mœurs, à la compréhension des visées et des allusions — est capable de leur faire comprendre et de répondre à leurs contradicteurs. Et n'y parvient pas celui qui est hors de la communauté. C'est pourquoi Allah n'a jamais suscité de prophète, sinon de la communauté à laquelle il était envoyé.</p>
'''

FR5 = '''<h3>Troisièmement : l'exposé de la sagesse de la descente du noble Coran</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« …et Nous avons fait descendre sur toi le Livre, éclaircissement de toute chose, guidance, miséricorde et bonne annonce pour les soumis [à Allah]. » (an-Naḥl, 89 — la fin)</p>
<p>[Citation coranique (an-Naḥl, 89 — le tronçon de la descente du Livre) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Allah, le Très-Haut, a dit » est vide dans la source numérisée, SANS span subsistant ; le tronçon retenu est celui que la glose imprimée du manuel (« Nous avons fait descendre sur toi, ô Messager, ce Coran, éclaircissement de tout ce dont les gens ont besoin de connaître… une guidance, une miséricorde, une bonne annonce ») désigne — les trois derniers noms de l'āya s'y lisent un à un.]</p>
<p>c'est-à-dire : Nous avons fait descendre sur toi, ô Messager, ce Coran, éclaircissement de tout ce dont les gens ont besoin de connaître, du licite et de l'illicite, de la récompense et du châtiment, de la guidance et de l'égarement. Nous en fîmes de même une miséricorde pour qui croit en lui et œuvre selon les limites d'Allah qu'il contient, Son ordre et Son interdit ; Nous en fîmes une bonne annonce pour qui obéit à Allah et revient à Lui, de la généreuse récompense dans l'au-delà. Le lien de cette āya avec ce qui précède est l'exposé que Celui qui t'a imposé la transmission du Livre descendu t'interrogera, au Jour de la Résurrection, de cela — comme le Très-Haut a dit :</p>
<p>« Nous interrogerons ceux vers qui furent envoyés des messagers, et Nous interrogerons aussi les envoyés. » (al-Aʿrāf, 6)</p>
<p>[Citation coranique (al-Aʿrāf, 6) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « comme le Très-Haut a dit » est vide dans la source numérisée ; le span subsistant portait « al-Aʿrāf : 5 » — SPAN ERRONÉ, tranché d'après la formule glosée par le commentaire du manuel : « Celui qui t'a imposé la transmission… t'interrogera au Jour de la Résurrection » est la lettre même de l'āya 6 (« Nous interrogerons ceux vers qui furent envoyés des messagers, et Nous interrogerons aussi les envoyés »), là où l'āya 5 porte l'invocation des cités châtiées (« leur invocation, lorsque leur survint Notre rigueur… ») — cinquième leçon du fil où un span subsistant se révèle erroné ; règle (aa) re-confirmée une seconde fois dans la même leçon.]</p>
<p>et Il a dit :</p>
<p>« Par ton Seigneur ! Nous les interrogerons tous, de ce qu'ils œuvraient. » (al-Ḥijr, 92-93)</p>
<p>[Citation coranique (al-Ḥijr, 92-93) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « et Il a dit » est vide dans la source numérisée ; le span subsistant « al-Ḥijr : 92 - 93 » est correct et a été suivi tel quel.]</p>
<p>L'éclaircissement du Coran des affaires de la religion se fait soit immédiatement, soit par l'éclaircissement du Messager, que la bénédiction d'Allah et la paix soient sur lui. Le Transcendant nous a ordonné de suivre cet éclaircissement dans Sa parole :</p>
<p>« …et ce que le Messager vous donne, prenez-le ; et ce qu'il vous interdit, abstenez-vous en. Et craignez Allah — Allah est dur en châtiment. » (al-Ḥašr, 7 — la fin)</p>
<p>[Citation coranique (al-Ḥašr, 7 — le tronçon de l'obéissance au Messager) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « dans Sa parole » est vide dans la source numérisée ; le span subsistant « al-Ḥašr : 7 » est correct et a été suivi tel quel — le tronçon retenu est celui que le contexte de l'éclaircissement par le Messager appelle.]</p>
<p>et Sa parole :</p>
<p>« …et Nous avons fait descendre vers toi le Rappel, pour que tu éclaircisses aux gens ce qui est descendu vers eux, afin qu'ils réfléchissent. » (an-Naḥl, 44 — la fin)</p>
<p>[Citation coranique (an-Naḥl, 44 — le tronçon de l'éclaircissement par le Prophète) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « et Sa parole » est vide dans la source numérisée ; le span subsistant « an-Naḥl : 44 » est correct et a été suivi tel quel.]</p>
<p>et à Sa parole, que la bénédiction d'Allah et la paix soient sur lui : « Je reçus le Coran, et son pareil avec lui ». [Musnad de l'imam Aḥmad, musnad d'al-Miqdād b. Maʿdī-karib] — soit par l'éclaircissement des Compagnons et des savants qui s'efforcent [d'en déduire les règles]. Et le Prophète, que la bénédiction d'Allah et la paix soient sur lui, a dit : « Tenez-vous à ma sunna et à la sunna des califes bien guidés qui viendront après moi ; mordez-la avec vos molaires ». [Sunan at-Tirmidhī, chapitres de la science, chapitre de l'adhésion à la sunna et de l'évitement de l'innovation]</p>
<p>L'ordre fut comme le Messager, que la bénédiction d'Allah et la paix soient sur lui, l'a dit : les imams s'efforcèrent [d'en déduire les règles], préparèrent les voies de la recherche en affaires de religion pour ceux qui vinrent après eux, déduisirent du Livre et de la sunna des écoles et des opinions en matière d'adorations et de transactions des hommes entre eux, rédigèrent une législation dont s'abreuvent les musulmans à chaque génération, et à laquelle reviennent les juges pour trancher entre les gens avec justice. Ce fut la plus noble des législations sorties pour les hommes — comme les maîtres des autres religions l'ont eux-mêmes reconnu.</p>
<p>Ces āyāt généreuses établissent l'unicité d'Allah, le Très-Haut, et Sa transcendance au-dessus de tout associé qui ne profite ni ne nuit ; et elles orientent les hommes vers le danger de l'association à Allah, le Très-Haut, par l'exposé d'une scène des scènes des associateurs au Jour de la Résurrection, lorsque leurs adorés d'avec Allah se désavouent d'eux — le châtiment les cernera alors, salaire de ce qu'ils œuvraient en ce bas monde.</p>
<h2>L'évaluation</h2>
<p>Montre, à travers les āyāt, des scènes de l'état des associateurs au Jour de la Résurrection.</p>
<ol>
<li>Quel est le sens du témoignage des prophètes contre leurs peuples ?</li>
<li>Quelle est la sagesse de la descente du noble Coran ?</li>
</ol>
<h2>L'exploitation</h2>
<p>L'imam al-Qurṭubī, qu'Allah lui fasse miséricorde, a dit — « Chapitre de l'éclaircissement du Livre par la sunna, et de ce qui est venu à ce propos. Allah, le Très-Haut, a dit : »</p>
<p>« …et Nous avons fait descendre vers toi le Rappel, pour que tu éclaircisses aux gens ce qui est descendu vers eux, afin qu'ils réfléchissent. » (an-Naḥl, 44)</p>
<p>[Citation coranique (an-Naḥl, 44) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Allah, le Très-Haut, a dit » est vide dans la source numérisée ; l'étiquette subsistante porte « sourate an-Naḥl, āya 44 » — correcte, suivie telle quel ; c'est l'āya que la longue citation du Qurṭubī, subsistante entière, commente.]</p>
<p>« Puis l'éclaircissement [venant] de lui, que la bénédiction d'Allah et la paix soient sur lui, est de deux sortes : un éclaircissement de ce que le Livre résume — comme son éclaircissement des cinq prières dans leurs horaires, leurs prosternations, leurs inclinaisons et le reste de leurs règles ; comme son éclaircissement du montant de l'aumône, de son échéance et des biens dont elle se prélève ; comme son éclaircissement des rites du pèlerinage — il dit, que la bénédiction d'Allah et la paix soient sur lui, lorsqu'il pélerina avec les gens : "Prenez de moi vos rites" ; et il dit : "Priez comme vous m'avez vu prier" — al-Bukhārī l'a rapporté. — Et un second éclaircissement, qui est un ajout au jugement du Livre : l'interdiction d'épouser la femme à sa tante paternelle ou à sa tante maternelle ; l'interdiction des ânes domestiqués et de tout carnassier à crocs ; le jugement par le serment avec le témoin ; et autres que cela. » [al-Jāmiʿ li-aḥkām al-Qurʾān d'al-Qurṭubī, I/37-39, avec retouche]</p>
<ol>
<li>Éclaircis, à travers le texte, le lien de la sunna avec le noble Coran.</li>
</ol>
'''

FR6 = '''<h2>La préparation préalable</h2>
<p>Lis l'āya (90) de la sourate an-Naḥl et réponds à ce qui suit :</p>
<p>Explique les mots suivants :</p>
<p>[Liste de la préparation préalable perdue à la numérisation : les cinq emplacements imprimés sous « Explique les mots suivants » sont vides dans la source numérisée — onzième occurrence du fil ; d'après l'āya 90 du Naḥl — l'ordre de l'équité et de la bienfaisance, la donnée au proche, l'interdit de l'ignominie, du blâmable et de la transgression — la liste proposait vraisemblablement les mots de cette portion, mais aucun indice subsistant n'en permet le rétablissement.]</p>
<ul>
<li>Dégage de l'āya les mœurs nobles qu'Allah, le Très-Haut, a ordonnées à Ses serviteurs.</li>
<li>Montre dans l'āya les mœurs viles qu'Allah, le Très-Haut, a interdites.</li>
</ul>
<p>N.d.T. — Deux spans d'attribution subsistants se sont révélés ERRONÉS dans cette leçon, quatrième et cinquième cas du fil (après le « 237/2 » de la leçon 13537, le « la Vache, 252 » de la leçon 13547 et le « az-Zalzala, 8-9 » de la leçon 13584) : l'étiquette imprimée « al-Aʿrāf : 5 » introduisait une āya censée prouver que Allah interrogera le Prophète de sa transmission au Jour de la Résurrection — formule qui est celle de l'āya 6 de la même sourate, l'āya 5 portant tout autre chose ; et l'étiquette « al-Anʿām : 27 » introduisait une āya glosée « ils interdisent aux gens de le suivre, eux-mêmes s'en écartant aussi » — formule qui est celle de l'āya 26, l'āya 27 portant le stationnement devant le Feu. Les deux spans ont été tranchés au cache coranique contre la formule glosée par le commentaire, et signalés en note de restauration ; méthode re-confirmée : AUCUN span subsistant ne doit être suivi sans vérification, et l'écart est signalé, jamais corrigé dans le sens d'une lecture canonique inventée.</p>
<p>N.d.T. — Le <em>Muḥarrar</em> original d'Ibn ʿAṭiyya, consulté en ligne (collation des quatre āyāt 86-89, réussite quatre sur quatre), comporte pour ces versets des matières que le manuel n'a pas retenues, et qui complètent utilement la leçon. Pour l'āya 87, la glose de « la soumission » s'accompagne de lectures coraniques : la majorité lit « as-salām » avec ouverture du <em>lām</em>, Yaʿqūb a rapporté d'Abū ʿAmr le <em>sukūn</em> du <em>lām</em>, et Mujāhid lit avec élévation de la <em>sīn</em> et du <em>lām</em> (forme intensifiée de la soumission) ; la glose de « et s'évanouit » précise que c'est leur mensonge contre Allah, leur forgery de la mécréance et de l'association, qui s'évanouit. Pour l'āya 88, Ibn ʿAṭiyya discute le rapport grammatical de « ceux » et rapporte la description du châtiment accru : Ibn Masʿūd dit qu'Allah lâchera contre eux scorpions et serpents, aux crocs comme les palmiers les plus longs — ʿUbayd b. ʿUmayr ajoute : aux scorpions comme les mules noires — et ʿAbdallāh b. ʿAmr décrit les côtes de la Géhenne où ces bêtes refoulent le mécréant fuyant le Feu, jusqu'à ce qu'il retrouve sa chaleur. Pour l'āya 89, la glose de « ceux-ci » signale l'indication du doigt vers cette communauté ; celle de « éclaircissement » en fait un nom et non un infinitif, la <em>tāʾ</em> ouverte à la manière d'« itération » et de « répétition », à l'accusatif de circonstance — sans exclure l'accusatif de cause ; et la glose de « de toute chose » l'entend de ce dont la Loi a besoin, comme le licite et l'illicite, l'appel à Allah et la crainte de Son châtiment — l'auteur précisant que cette énumération est celle des formules des exégètes — puis rapporte d'Ibn Masʿūd la parole : est descendu dans ce Coran toute science ; toute chose nous a été éclaircie dans le Coran — avant de réciter cette āya même.</p>
<p>N.d.T. — État de la source numérisée de cette leçon : la section « Les versets » est vide entière — treizième cas consécutif du fil ; vingt-quatre emplacements coraniques du commentaire sont perdus — DIX sans aucun span subsistant (le bloc principal porte toutefois son étiquette « an-Naḥl : 86 - 89 »), DOUZE restitués d'après des étiquettes correctes vérifiées au cache (al-Aḥqāf 4-5, Maryam 82-83, Maryam 37, as-Sajda 12, Ṭāhā 108, Yūnus 18, an-Nisāʾ 41, al-Ḥijr 92-93, al-Ḥašr 7 et an-Naḥl 44 à deux reprises), deux SPANS ERRONÉS tranchés (al-Aʿrāf 5 vers 6 ; al-Anʿām 27 vers 26), et un emplacement à caution (le tronçon du pronom de l'āya 86, l'édition en ligne du <em>Muḥarrar</em> portant une forme altérée à la collation) ; deux emplacements sont confirmés MOT POUR MOT au <em>Muḥarrar</em> (le pronom de l'āya 87 renvoyant aux associateurs ; la sagesse de « du milieu d'eux-mêmes »). Exception favorable marquante du fil : les TROIS hadiths subsistent entiers et diacrités — le hadith d'Ibn Masʿūd (« cela te suffit maintenant » et les deux yeux laissant couler des larmes, rapporté par al-Bukhārī), le hadith « Je reçus le Coran et son pareil avec lui » (rapporté par Aḥmad d'al-Miqdād b. Maʿdī-karib) et le hadith de la sunna des califes bien guidés (rapporté par at-Tirmidhī) — ainsi que la parole d'Ibn ʿAṭiyya (« il se peut qu'Allah suscite un témoin parmi les justes ») et la longue citation du Qurṭubī sur les deux sortes d'éclaircissement (I/37-39, signalée « avec retouche » — adaptation pédagogique conservée telle quelle) ; les six gloses de l'explication des mots subsistaient TOUTES avec leurs mots-têtes — aucune occurrence de la règle (y) dans cette leçon. La liste des mots de la préparation préalable est perdue — onzième occurrence ; la fente liminaire <em>dl/dt/dd</em> est vide — quinzième ; le tatwīl du <em>fī</em> court à travers le titre — treizième leçon consécutive ; l'OCR altère le nom de l'enseignement secondaire ancien (« al-ʿatīq » porteur d'un alef dédoublé) — connu du fil et tranché d'après la collation des leçons précédentes ; et l'écart de numérotation persiste — leçon 19 au manuel, badge 21/32 du fil (quatorzième occurrence).</p>
'''

# === ASSEMBLAGE ===
html = FR1 + FR2 + FR3 + FR4 + FR5 + FR6

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
bal = ['h1', 'h2', 'h3', 'p', 'ol', 'ul', 'li', 'em', 'span']
types = sum(1 for b in bal if f'<{b}>' in html)
n_notes = html.count('[Citation coranique') + html.count('[Liste de la préparation')
n_ndt = html.count('N.d.T.')
print(f'caractères: {len(html)}')
print(f'types de balises: {types}/9')
print(f'notes de restauration: {n_notes}')
print(f'paragraphes N.d.T.: {n_ndt}')
print(f'guillemets: {html.count("«")}/{html.count("»")}')
if issues:
    print('PROBLÈMES:')
    for i in issues:
        print(' -', i)
    raise SystemExit(1)
if len(html) < 12000:
    print('TROP COURT (< 12 000 car) — rédaction insuffisante')
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/13590.html'
open(out, 'w').write(html)
print('écrit:', out)
