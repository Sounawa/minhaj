#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13688 (tafsir-tanawi-2, Sourate al-Isrāʾ
86-89, leçon 22 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot ; corpus
canonique pour les versets) :
- Bloc d'ouverture (17:86-89) : <p> vide → 4 versets restaurés du
  quran-cache.
- Lexique (الشرح) : les 4 vedettes sont INTACTES dans la source
  (ẓahīran/wa-la-qad ṣarrafnā/min kulli mathalin/kafūran) — la prévision
  de l'iʿdād de 13681 confirmée par la source.
- Citations inline perdues :
  * v86 : citation perdue entre « فقال سبحانه » et la glose « أي: ولئن
    شاء » — restaurée du quran-cache ;
  * v87a : « إلا رحمة من ربك » après « وقاله: » — VÉRIFIÉ sur le texte
    d'Ibn ʿAṭiyya (« وقوله ﴿إلا رحمة﴾ استثناء منقطع ») ;
  * v87b : « إن فضله كان عليك كبيرا » après « فقال سبحانه: » —
    restitution (le manuel reprend la clausule du verset ; l'édition en
    ligne conclut le commentaire de v87 sans nouvelle citation, le manuel
    paraphrase en citation) ;
  * v88 : citation perdue — restaurée du quran-cache ;
  * « لئن » (le lām), « لا يأتون بمثله », « ولو كان بعضهم لبعض ظهيرا »,
    « الظهير », « وإن تظاهرا عليه » [التحريم: 4 — réf. CONFORME] —
    VÉRIFIÉS sur le texte d'Ibn ʿAṭiyya ;
  * « حتى زرتم المقابر » [التكاثر: 2 — réf. CONFORME] — VÉRIFIÉ ;
  * « إن كنتم في ريب » : citation perdue avant le span — VÉRIFIÉ sur le
    texte d'Ibn ʿAṭiyya ; le manuel imprime [البقرة: 22] — la référence
    canonique du verset cité est Baqara 2:23 (8e réf d'adjacence erronée
    notée) ;
  * v89 : citation perdue — restaurée du quran-cache ; « من كل مثل »,
    « فأبى », « كفورا », « يأبى », « أبى » — VÉRIFIÉS sur le texte
    d'Ibn ʿAṭiyya ;
  * « واتخذوا من مقام إبراهيم مصلى » : citation perdue avant le span —
    VÉRIFIÉ ; le manuel imprime [البقرة: 124] — la référence canonique est
    Baqara 2:125 (9e réf d'adjacence erronée notée) ;
  * al-Rāzī [Mafātīḥ 21/406] : la citation est INTACTE ; le «؟» final de
    l'imprimé est une coquille (l'énoncé est affirmatif — rendu par un
    point, noté) ;
  * l'istithmār : la phrase finale (« Et l'exception est épuisée… ») est
    d'Ibn ʿAjība [al-Baḥr al-madīd 3/230] ; ce qui précède est le texte
    d'Ibn ʿAṭiyya (vérifié) ;
  * iʿdād : 6 vedettes du lexique de la leçon suivante (13716 — v90-93)
    restituées du lexique imprimé de cette leçon (ينبوعا/جنة/كسفا/قبلا/
    زخرفا/سلما) + v90 restauré + la question qirāʾique (l'imprimé porte
    un wāw avant ﴿تفجر﴾ — trace probable de la paire تُفَجِّرَ/تَفْجُرَ,
    discutée dans la leçon suivante)."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 86 à 89</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 86 à 89, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 22).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Discerner le dessein de l’orientation de Dieu, le Très-Haut, à Son Messager — paix et bénédiction sur lui.</li>
<li>Conclure des versets l’inimitabilité du noble Coran.</li>
<li>M’enorgueillir du noble Coran et des versets inimitables qu’il renferme.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Après que Dieu, le Glorifié, eut gratifié Son Prophète — paix et bénédiction sur lui —, aux versets précédents, du noble Coran en le faisant guérison pour les gens, Il exposa en ces versets l’entier achèvement de Sa faveur sur Son Prophète — paix et bénédiction sur lui — par l’honneur sans interruption qu’Il lui fait du noble Coran, Lui en montrant l’inimitabilité et ce qu’il renferme des sagesses, des règles et des convenances dont l’homme a besoin en ce bas-monde et en la dernière vie.</p>
<p>En quoi Dieu, le Très-Haut, a-t-Il gratifié Son Messager — paix et bénédiction sur lui ? Et en quoi a-t-Il réduit les associateurs à l’impuissance ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et si Nous voulions, Nous emporterions certes ce que Nous t’avons révélé ; puis tu ne trouverais pas, à son sujet, de garant contre Nous. (87) Sauf une miséricorde de ton Seigneur : en vérité, Sa faveur sur toi a été immense. (88) Dis : “ Si les hommes et les djinns s’assemblaient pour venir avec la semblance de ce Coran, ils ne viendraient point avec sa semblance, quand même ils seraient les uns pour les autres auxiliaires. ” (89) Et certes, Nous avons exposé aux gens, en ce Coran, de toute parabole ; mais la plupart des gens n’ont persisté qu’en reniement. ” » (al-Isrāʾ, 86-89)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>ẓahīran</em> (ظَهِيرًا) : auxiliaire, secoureur.</li>
<li><em>wa-la-qad ṣarrafnā</em> (وَلَقَدْ صَرَّفْنَا) : Nous avons répété et renvoyé par des voies différentes, qui requièrent l’accroissement de la consolidation et de l’enracinement.</li>
<li><em>min kulli mathalin</em> (مِن كُلِّ مَثَلٍ) : de tout sens admirable en sa beauté, sa rareté et sa maestria, tel le proverbe.</li>
<li><em>kafūran</em> (كُفُورًا) : reniement et refus.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ul>
<li>En quoi Dieu, le Très-Haut, a-t-Il gratifié Son Messager — paix et bénédiction sur lui — en ces versets ?</li>
<li>Qui Dieu, le Très-Haut, a-t-Il défié en ces versets ? Et par quoi ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la grâce de Dieu, le Glorifié, sur Son Messager — paix et bénédiction sur lui</h3>
<p>Après la grâce de Dieu, le Très-Haut, à Son Messager — paix et bénédiction sur lui — au verset précédent, Il mentionne en ces versets une manifestation des manifestations de Sa puissance, après avoir exposé que l’Esprit relève de Son commandement. Le Glorifié dit :</p>
<p>« Et si Nous voulions, Nous emporterions certes ce que Nous t’avons révélé ; puis tu ne trouverais pas, à son sujet, de garant contre Nous. » (al-Isrāʾ, 86)</p>
<p>— c’est-à-dire : et si Dieu voulait, Il emporterait la révélation qu’Il t’a donnée, et tu n’aurais alors pour elle aucun secoureur : il n’est donc point chose grande qu’il ne te vînt point d’éclaircissement sur l’Esprit, dont tu voulus donner au peuple l’éclaircissement et que tu leur promis. Et Sa parole : <em>al-wakīl</em> (“ le garant ”) : celui qui se tient en l’affaire pour le secours ou la dispute, et pareil, des aspects du profit.</p>
<p>[Citation coranique (v. 86) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; le commentaire qui suit est conforme au texte d’Ibn ʿAṭiyya.]</p>
<p>Et Sa parole :</p>
<p>“ …sauf une miséricorde de ton Seigneur… ” (al-Isrāʾ, 87 — extrait)</p>
<p>— exception interrompue (<em>munqaṭiʿ</em>) : c’est-à-dire, mais une miséricorde de ton Seigneur la retient sur toi. Et cette exception interrompue particularise une particularisation quelconque, et n’est pas comme la continue (<em>muttaṣil</em>) : car la continue particularise du genre ou de la phrase totale, et l’interrompue particularise un étranger à cela. Et ne conteste la survenance de l’interrompue en le Coran qu’un non-Arabe (<em>aʿjamī</em>) ; et cela fut rapporté d’Ibn Khuyayz Mindād.</p>
<p>[Citation « illā raḥmatan min rabbik(a) » restaurée d’après le texte d’Ibn ʿAṭiyya (« وقوله ﴿إلا رحمة﴾ استثناء منقطع ») : l’emplacement imprimé est vide — perte OCR ; le commentaire est conforme.]</p>
<p>Puis le Puissant, le Majestueux, énuméra sur lui l’immensité de Sa faveur — en le particularisant par la prophétie, en le protégeant des associateurs, et le reste de ce qui ne se compte pas. Le Glorifié dit :</p>
<p>“ …en vérité, Sa faveur sur toi a été immense. ” (al-Isrāʾ, 87 — fin)</p>
<p>[Citation « inna faḍlaka kāna ʿalayka kabīrā » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; l’édition en ligne d’Ibn ʿAṭiyya conclut le commentaire du verset sans nouvelle citation — le manuel introduit la clausule du verset comme citation.]</p>
<h3>Deuxièmement : le défi lancé par Dieu, le Très-Haut, aux hommes et aux djinns par le noble Coran</h3>
<p>Après la grâce de Dieu, le Très-Haut, à Son Messager — paix et bénédiction sur lui — par le noble Coran, Il lui ordonna de défier les associateurs par ce Coran. Le Glorifié dit :</p>
<p>« Dis : “ Si les hommes et les djinns s’assemblaient pour venir avec la semblance de ce Coran, ils ne viendraient point avec sa semblance, quand même ils seraient les uns pour les autres auxiliaires. ” » (al-Isrāʾ, 88)</p>
<p>[Citation coranique (v. 88) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>La cause de la descente de ce verset : un groupe de Quraysh dit au Messager de Dieu — paix et bénédiction sur lui : “ Muḥammad, viens-nous-en avec un signe étranger, autre que ce Coran — car nous, nous pouvons venir avec la semblance de ceci. ” Ce verset descendit alors, proclamant expressément la réduction à l’impuissance, et enseignant que la totalité des créatures, si elles se prêtaient mutuel appui en cela, hommes et djinns, ne le pourraient point. Et l’impuissance en la rivalisation avec le Coran ne porta que sur la trame et l’assemblage de ses sens ; et la cause en est l’englobement (<em>iḥāṭa</em>) dont ne se qualifie que Dieu, le Puissant, le Majestueux — l’homme étant, de nécessité, défaillant par l’ignorance, l’oubli, l’insouciance et les espèces d’imperfection qui l’emportent sur lui.</p>
<p>Et le <em>lām</em> en Sa parole : <em>la-in</em> (“ et si ”) est annonceur sans être obligatoire : il est parfois élidé ; et ce <em>lām</em> peut venir purement intensif, et le verbe nié venir au jussif. Et Sa parole : <em>lā yaʾtūna bi-mithlihi</em> (“ ils ne viendront point avec sa semblance ”) est en position de nominatif, et <em>lā</em> reçoit le serment. Et Sa parole, le Glorifié : <em>wa-law kāna baʿḍuhum li-baʿḍin ẓahīrā</em> (“ quand même ils seraient les uns pour les autres auxiliaires ”) est coordonnée à un sous-entendu : c’est-à-dire qu’ils ne pourraient venir avec sa semblance si les uns n’étaient pour les autres auxiliaires et secoureurs — et quand même les uns seraient pour les autres auxiliaires et secoureurs, ils ne le pourraient pas davantage. Et le sens de <em>al-ẓahīr</em> : l’auxiliaire — et de lui la parole du Puissant, le Majestueux :</p>
<p>“ …et si toutes deux se liguent contre lui… ” (at-Taḥrīm, 66:4 — extrait)</p>
<p>Le visé : qu’ils ne peuvent, sur aucun état supposé, venir avec sa semblance.</p>
<p>[Citations « la-in », « lā yaʾtūna bi-mithlihi », « wa-law kāna baʿḍuhum li-baʿḍin ẓahīrā », « al-ẓahīr » et « wa-in taẓāharā ʿalayhi » restaurées d’après le texte d’Ibn ʿAṭiyya et le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la référence imprimée « at-Taḥrīm 66:4 » est conforme.]</p>
<p>Et les Arabes, par la pureté de leur entendement en la balance du discours et leur longue habitude de lui, comprirent ce que nous ne comprenons pas, nous, ni quiconque fut approché par la civilisation. Ils connurent donc par nécessité et constat immédiat l’impuissance à son égard ; et les gens après eux le connurent par inférence et examen : à chacun revint une science certaine — mais non en un même degré. De même que les Compagnons connurent, par constat immédiat, la Loi du Prophète et ses actes — science de nécessité — et que nous connaissons, nous, le massivement transmis de cela par la transmission massive : la certitude échut à tous, mais en deux degrés.</p>
<p>Et l’inimitabilité du Coran, la comprirent les maîtres de l’éloquence, ceux qui détiennent les merveilles en la balance du discours. Ne vois-tu pas la compréhension d’al-Farazdaq, saisissant le poème de Jarīr en plein poème de Dhū l-Rumma, en sa parole : “ Les généalogistes de Tamīm dénombrent… ” ? Et ne vois-tu pas l’histoire de Jarīr, en ses <em>Nawādir</em>, avec al-Farazdaq — en la parole d’al-Farazdaq : “ Pourquoi te retourner ? ”, et en sa parole : “ Elle se retourne : c’est qu’elle est sous le fils du forgeron ” ? Et ne vois-tu pas la parole du Bédouin : “ Il fut puissant — il jugea, il trancha ” ? Et ne vois-tu pas l’inférence de l’autre, pour la résurrection, de Sa parole :</p>
<p>“ …jusqu’à ce que vous visitiez les tombeaux. ” (at-Takāthur, 102:2 — extrait)</p>
<p>— il dit : la visite requiert le retour ? De là encore la science de Bishār en la parole d’Abū ʿAmr b. al-ʿAlāʾ sur le poème d’al-Aʿshā : “ Tu m’as méconnu — mais qu’était donc celui que tu as méconnu ? ”. De là la parole du Bédouin à al-Aṣmaʿī : “ Qui rend le généreux le plus grand besoin de jurer ? ”. De leur compréhension encore : qu’ils viennent, de leur premier jet, avec une parole en prose qui l’emporte sur le poème peaufiné — les exemples en sont conservés ; de là leurs réponses qui réduisent au silence, et le reste de leur maîtrise en l’éloquence, et le fait qu’ils en soient l’extrémité — comme était la magie au temps de Moïse, et la médecine au temps de Jésus. Eux, malgré ces entendements, reconnurent l’impuissance ; et celui d’entre eux qui tint tête eut recours à l’épée, s’accommoda du meurtre, de la captivité et de la mise à nu du sanctuaire — lui qui aurait trouvé échappatoire en cela par la seule rivalisation.</p>
<p>[Citation « ḥattā zurtumu l-maqābira » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée « at-Takāthur 102:2 » est conforme. Les trois anecdotes (al-Farazdaq ; “ ʿazza fa-ḥakama fa-qaṭaʿa ” ; le Bédouin et al-Aṣmaʿī) et le vers d’al-Aʿshā sont intacts dans la source — l’iʿdād de la leçon précédente les avait préparées.]</p>
<p>De même le défi par les dix sourates et le défi par la sourate : tout n’eut lieu que sur une seule limite, en la trame seule. Et les dix furent qualifiées par la forgerie, parce qu’ils avaient dit que le Coran était forgé : Il les appela, à la suite de cette mention, à venir avec dix sourates forgées ; et la forgerie ne fut pas mentionnée en la sourate, parce qu’il n’était pas venu d’eux, auparavant, mention de cela — mais Il dit :</p>
<p>“ …Si vous êtes en doute… ” (al-Baqara, 2:23 — extrait)</p>
<p>— bien qu’il soit advenu mention de la sourate avec leur mention de la forgerie, en la sourate Hūd.</p>
<p>[Citation « in kuntum fī rayb » restaurée d’après le texte d’Ibn ʿAṭiyya (« بل قال ﴿إن كنتم في ريب﴾ ») : l’emplacement imprimé est vide — perte OCR ; le manuel imprime la référence « al-Baqara 2:22 » — la référence canonique du verset cité est 2:23 (écart de numérotation noté, comme Baqara 124→125 ci-dessous).]</p>
<p>Et les gens divergèrent en cet endroit. Il fut dit : ils furent appelés à la sourate semblable en la trame, les mystères et le reste des attributs — et cela relevait de la charge de l’impossible ; puis, quand elle leur devint ardue, allègement par l’appel aux forgées. Et il fut dit autre chose, qui se dénoue à l’examen.</p>
<p>Et bien que les associateurs fussent impuissants à venir avec une sourate de la semblance du noble Coran, ils persistèrent en leur tyrannie et leur déni du noble Coran. Le Glorifié dit, en l’exposant :</p>
<p>« Et certes, Nous avons exposé aux gens, en ce Coran, de toute parabole ; mais la plupart des gens n’ont persisté qu’en reniement. » (al-Isrāʾ, 89)</p>
<p>— l’objet de <em>ṣarrafnā</em> (“ Nous avons exposé ”) est élidé, et la restitution : “ Et certes Nous avons exposé les guidances et les avertissements, en maintes voies. ” Et l’exposition réitérée du dire (<em>taṣrīf al-qawl</em>) est le renvoi de l’éclaircissement quant au sens.</p>
<p>[Citation coranique (v. 89) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Et Sa parole : <em>min kulli mathalin</em> (“ de toute parabole ”) — il est loisible que <em>min</em> soit du point de départ de la fin, l’objet de <em>ṣarrafnā</em> étant sous-entendu : restitution, “ Et certes Nous avons exposé, en ce Coran, les admonitions et les avertissements, de toute parabole que Nous avons frappée ” ; et il est loisible qu’elle soit intensive, de surcroît : restitution, “ Et certes Nous avons exposé toute parabole ”. Cela est comme Sa parole :</p>
<p>“ …Et prenez de la station d’Abraham un lieu de prière… ” (al-Baqara, 2:125 — extrait)</p>
<p>[Citation « wa-ttakhdhū min maqāmi Ibrāhīma muṣallan » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; le manuel imprime la référence « al-Baqara 2:124 » — la référence canonique est 2:125 (écart de numérotation noté ; l’édition en ligne d’Ibn ʿAṭiyya confirme « من الآية ١٢٥ »).]</p>
<p>Et Sa parole : <em>fa-abā</em> (“ mais il a refusé ”) est expression de l’acquisition de la dénégation par les dénégateurs, et de leur détournement de la foi ; et il y a, en l’expression par <em>yabā</em> (“ il refuse ”), intensification. La dénégation quant à la création et l’invention est œuvre de Dieu, le Très-Haut ; quant à l’acquisition et l’opiniâtreté, elle est de l’homme. Et Sa parole : <em>kufūran</em> (“ reniement ”) : un infinitif, comme <em>al-khurūj</em> (“ la sortie ”). Et l’exception est épuisée (<em>mufaragh</em>), mise à l’accusatif par <em>abā</em> — car il est au sens de la négation : c’est-à-dire : la plupart d’entre eux n’ont agréé que la dénégation de lui. ” [al-Baḥr al-madīd fī tafsīr al-Qurʾān al-majīd, d’Ibn ʿAjība : 3/230 — réf. imprimée « 3/230 », conforme]</p>
<p>[Mots « fa-abā », « yabā », « kufūran », « abā » restaurés d’après le texte d’Ibn ʿAṭiyya (« وقوله ﴿فأبى﴾… و﴿كفوراً﴾ مصدر كالخروج ») : les emplacements imprimés sont vides — perte OCR ; la phrase finale (« Et l’exception est épuisée… ») est l’investissement (<em>istithmār</em>) cité d’Ibn ʿAjība ; ce qui précède est le texte d’Ibn ʿAṭiyya, conforme.]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets établissent une somme de finalités éducatives, dont les plus importantes :</p>
<ul>
<li>L’honneur que Dieu, le Très-Haut, fait à Son Messager — paix et bénédiction sur lui — par ce qui affermit sa prophétie : le noble Coran, qui renferme les assises les plus affermies et les sagesses et règles les plus droites — le monde étant impuissant à venir avec sa semblance ; bien plus : les purs de la langue et leurs orateurs, en la langue de qui il est descendu, furent impuissants à venir avec une seule sourate sa semblance.</li>
</ul>
<ul>
<li>L’affermissement de la prophétie du Messager — paix et bénédiction sur lui —, et l’exposé de l’opiniâtreté des associateurs contre l’unicité de Dieu, le Très-Haut : ils agréent d’adorer la pierre, et renient la mission du Prophète — paix et bénédiction sur lui.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ol>
<li>Quel est le dessein de l’orientation de Dieu, le Très-Haut, à Son Messager — paix et bénédiction sur lui — en ces versets ?</li>
<li>J’expose les manifestations de l’inimitabilité du noble Coran advenues en ces versets.</li>
<li>Comment l’inimitabilité du noble Coran agit-elle en la réforme des âmes et leur discipline ?</li>
<li>J’explicite, à travers le commentaire, ce qui atteste la vive clairvoyance des Arabes et leur maîtrise de la compréhension du contexte.</li>
</ol>
<h3>L’investissement (istithmār)</h3>
<p>Al-Fakhr al-Rāzī dit, en commentant la parole de Dieu, le Très-Haut :</p>
<p>« Dis : “ Si les hommes et les djinns s’assemblaient pour venir avec la semblance de ce Coran, ils ne viendraient point avec sa semblance, quand même ils seraient les uns pour les autres auxiliaires. ” » (al-Isrāʾ, 88)</p>
<p>[Citation coranique (v. 88 — objet du commentaire d’al-Rāzī) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>“ Il est loisible à un contradicteur de dire : accorde qu’apparût l’impuissance de l’homme à le rivaliser — comment avez-vous connu l’impuissance des djinns à le rivaliser ? Et encore : pourquoi ne serait-il pas dit que ce discours est la trame des djinns, qu’ils auraient déversée sur Muḥammad — paix et bénédiction sur lui — et qu’ils lui auraient départie en propre, par voie d’effort à égarer la création ? Sur ce pied, vous ne connaîtriez la véracité de Muḥammad — paix et bénédiction sur lui — qu’après avoir connu que Muḥammad est véridique en sa parole : ‘ celui-ci n’est point du discours des djinns — il est du discours de Dieu, le Très-Haut ’ : alors s’ensuit le cercle. Et il n’est loisible à personne de dire : ‘ comment se conçoit-il que ceci soit du dire des djinns ? ’ — car nous disons : ce verset atteste la survenance du défi lancé aux djinns ; or ce défi n’est convenable que s’ils étaient purs de langue et orateurs ; et quand la chose est telle, la possibilité susdite demeure debout. ” [Mafātīḥ al-ghayb, d’al-Fakhr al-Dīn al-Rāzī : 21/406 — réf. imprimée « 21/406 », conforme]</p>
<p>[Citation d’al-Rāzī intégrale et conforme ; le point d’interrogation final de l’impression est une coquille — l’énoncé est affirmatif, rendu ici par un point.]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<ol>
<li>J’extrais la difficulté (<em>ishkāl</em>) advenue en le texte.</li>
<li>J’expose la réponse à cette difficulté.</li>
</ol>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 90 à 93 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>yanbūʿan</em> (يَنۢبُوعًا — une source dont l’eau ne s’épuise point).</p>
<p><em>jannatan</em> (جَنَّةٍ — un jardin d’arbres nombreux).</p>
<p><em>kisfan</em> (كِسَفًا — en morceaux : pluriel de <em>kusfa</em>, comme <em>qiṭʿa</em>).</p>
<p><em>qabīlan</em> (قَبِيلًا — face à face : pour les voir de leurs yeux).</p>
<p><em>min zukhrufin</em> (مِن زُخْرُفٍ — d’or).</p>
<p><em>sulāman</em> (سُلَّمًا — l’échelle : monter au ciel par l’échelle).</p>
<p>[Vedettes restituées du lexique de la leçon suivante (versets 90-93) : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Quel est le dessein du détournement de Dieu, le Très-Haut, des demandes des associateurs ?</li>
<li>Quel est l’effet de la lecture ﴿ tafjur ﴾ sur le sens de Sa parole, le Glorifié :</li>
</ul>
<p>“ …jusqu’à ce que tu fasses jaillir pour nous, de la terre, une source… ” (al-Isrāʾ, 90 — extrait)</p>
<p>[Citation coranique (v. 90) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la question prépare la divergence des lectures de 17:90 (تُفَجِّرَ / تَفْجُرَ) discutée dans la leçon suivante — l’imprimé porte un wāw avant ﴿تفجر﴾, trace probable de la paire de lectures.]"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13688":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13688 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13688 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
