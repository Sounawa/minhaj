#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13525 (tafsir-tanawi-2, Sourate al-Isrāʾ
18-22, leçon 6 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions :
- Bloc d'ouverture (17:18-22) : <p> vide après « الآيات » → restauré du
  quran-cache (5 versets, numérotation entre parenthèses).
- Citations inline perdues par l'OCR, identifiées par l'exégèse qui suit :
  * v18 partie 1 après « فقال : » (glose « من كان يريد الدنيا العاجلة… » +
    discussion qirāʾique نشاء/يشاء) ;
  * v18 partie 2 après « ثم قال تعالى : » (glose « ثم يجعل الله جهنم… ») ;
  * les 3 aspects du châtiment (permanence/humiliation/bannissement) →
    3 citations partielles de v18 : « ثُمَّ جَعَلْنَا لَهُ جَهَنَّمَ يَصْلَاهَا »,
    « مَذْمُومًا », « مَدْحُورًا » (mapping exact sur l'énumération du manuel) ;
  * « دل عليه المقابل في قوله : » (Abū Ḥayyān) → le contre-terme de
    « كافر » dans l'estimation est « مُؤْمِنٌ » = v19 fin « … tout en étant
    croyants » ;
  * v19 en 2 citations (partie conditionnelle + « فأولئك كان سعيهم مشكورا »
    avant « أي : فأولئك يشكر الله سعيهم ») ;
  * v20 complet après « فقال : » ; note grammaticale : كلًّا au naṣb par
    نُّمِدُّ, tanwīn tenant lieu du mudāf ilayhi ; « هؤلاء وهؤلاء » badal de
    « كلًّا » (position naṣb) ; « من عطاء ربك » cité avant ses 2 taʾwīl ;
  * « وما كان عطاء ربك محظورا » après « يتناسب هذا المعنى مع قوله : » ;
  * v21 après « قال تعالى : » + répétition de « وللآخرة أكبر درجات وأكبر
    تفضيلا » avant « ليس في اللفظ من أي شيء هو أكبر » ;
  * parallèle « وكذلك الأمر في قوله : » → al-Anʿām 6:132 « وَلِكُلٍّ
    دَرَجَٰتٌ مِّمَّا عَمِلُوا » (réf restituée : le passage discute la
    graduation des gens en l'au-delà — darkāt/darajāt ; Anʿām 132 est le
    parallèle standard d'Ibn ʿAṭiyya) ;
  * v22 après « فقال : » (clôture des conditions des degrés).
- iʿdād (préparation leçon suivante 23-25 = docId 13534) : les 5 expressions
  vides restituées du lexique (الشرح) de 13534 : وقضى / أف / ولا تنهرهما /
  قولا كريما / للاوابين ; la citation « أوضح معنى قوله تعالى : » = Isrāʾ 17:24
  (l'istiʿāra de l'aile de l'humilité, traitée nommément dans le tafsīr de
  13534 — « نكتة بلاغية ») ; « مع بيان ما فيه من نكتة بلاغية » conserve
  l'interrogation imprimée.
- Heading « Les objectifs de la leçon » ajouté (le manuel papier le porte ;
  l'OCR l'a perdu — convention du corpus livré) ; titre h1 selon la convention
  du modèle 16767.
- Réf imprimée « مفاتيح الغيب 317/20 » = volume/page inversés → rendue
  « 20/317 » (doctrine R113 des réfs inversées).
- Anomalies source notées : « الاحتقتار » = احتقار (typo) ; 3e item مقاصد
  fusionné par <br> avec perte du « أن » connectif → « Que » restitué.
- GT non copié (GT-ismes « le bref éditeur » exclus) ; hadiths traduits
  intégralement, réfs fidèles.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 18 à 22</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 18 à 22, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> [« Le Concis établi, pour l’exégèse du Livre puissant »] du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 6).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Reconnaître les finalités que les gens poursuivent par leurs actions.</li>
<li>Saisir la rétribution de celui qui œuvre pour ce monde ou pour l’au-delà.</li>
<li>Être sincère en mes actes, pour qu’ils obtiennent l’agrément au Jour de la Résurrection.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Après que le Maître — gloire à Lui, le Très-Haut — eut mentionné que la destinée de l’homme est liée à son action, Il expose en ces versets que les gens sont, en ce monde, deux factions : une faction qui veut, par son action, ce monde — ses profits et ses plaisirs — et oublie l’au-delà ; et une faction qui veut, par son action, l’au-delà et sa béatitude, tenant ce monde pour un simple chemin vers elle : Dieu bénit alors pour elle son action et la fait action reconnue et rétribuée. C’est pourquoi, si la prééminence entre les gens se mesure, en ce monde, à l’argent et au rang, elle se mesure, en l’au-delà, aux degrés du Paradis — ce qui est plus grand et meilleur.</p>
<p>Quand l’action de l’homme se retourne-t-elle contre lui ? Et quelles sont les conditions de l’action qui sauve son auteur ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Quiconque désire [la vie] immédiate, (18) Nous nous hâtons de donner ce que Nous voulons, à qui Nous voulons. Puis, Nous lui assignons l’Enfer où il brûlera méprisé et repoussé. (19) Et ceux qui recherchent l’au-delà et fournissent les efforts qui y mènent, tout en étant croyants… alors l’effort de ceux-là sera reconnu. (20) Nous accordons abondamment à tous, ceux-ci comme ceux-là, des dons de ton Seigneur. Et les dons de ton Seigneur ne sont refusés [à personne]. (21) Regarde comment Nous favorisons certains sur d’autres. Et dans l’au-delà, il y a des rangs plus élevés et plus privilégiés. (22) N’assigne point à Allah d’autre divinité ; sinon tu te trouveras méprisé et abandonné. » (al-Isrāʾ, 18-22)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>al-ʿājila</em> (l’immédiate) : la demeure d’ici-bas.</li>
<li><em>yaṣlāhā</em> (il la brûlera) : il en subit l’ardeur.</li>
<li><em>madḥūran</em> (repoussé) : le banni humilié, écarté, rabaissé, couvert de blâme.</li>
<li><em>maḥẓūran</em> (refusé) : interdit à quiconque le souhaite.</li>
<li><em>makhdhūlan</em> (abandonné) : le délaissé que ne secourt pas même celui qui voudrait le secourir.</li>
</ul>
<h4>Extraction des idées des versets</h4>
<ul>
<li>Que poursuivent les gens par leurs actions ?</li>
<li>En quoi portait, dans ces versets, la comparaison entre les gens ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : les gens — entre qui veut par son action ce monde et qui veut l’au-delà</h3>
<p>Allah, Puissant et Majestueux, expose en ces versets que la rétribution des gens est liée à leurs intentions. Il dit :</p>
<p>« Quiconque désire [la vie] immédiate, Nous nous hâtons de donner ce que Nous voulons, à qui Nous voulons. »</p>
<p>c’est-à-dire : quiconque veut la vie immédiate, ne croit qu’en elle et ne croit pas en l’au-delà, et vide sur ce monde son espérance et sa croyance — eh bien, Dieu hâte à qui Il veut parmi ces gens ce qu’Il veut. Le sujet est alors Dieu selon la lecture de ceux qui lisent <em>nashāʾa</em> au <em>nūn</em> ; ou bien le sujet est le désirant, selon la lecture de <em>yashāʾa</em> au <em>yāʾ</em>. On a dit aussi : le pronom de <em>yashāʾa</em> renvoie à Dieu même selon la lecture au <em>yāʾ</em> — cela relève de l’<em>iltifāt</em> (la tournure) —, si bien que les lectures au <em>nūn</em> et au <em>yāʾ</em> se valent. Abū Ḥayyān — que Dieu lui fasse miséricorde — a dit : « Il faut nécessairement suppléer une élision qu’indique le terme opposé en Sa parole : [tout en étant croyants] — l’estimation est donc : quiconque veut l’immédiate et œuvre pour elle en son œuvre, tout en étant dénégateur. On a dit : il vise quiconque veut l’immédiate par l’œuvre de l’au-delà — tel l’hypocrite, celui qui agit par ostentation, celui qui émigre pour ce monde et celui qui combat pour le butin et la renommée —, comme le dit l’Envoyé de Dieu — paix sur lui : “ Celui dont l’émigration visait un acquis de ce monde qu’il atteigne, ou une femme qu’il épouse : son émigration est vers ce vers quoi il a émigré. ” [Ṣaḥīḥ al-Bukhārī, Livre du début de la révélation, chapitre : Comment débuta la révélation à l’Envoyé de Dieu — paix et bénédiction sur lui…] ; et il dit — prière et salut sur lui : “ Celui qui recherche l’œuvre de ce monde par l’œuvre de l’au-delà : il n’a point de part en l’au-delà. ” [Musnad al-Quḍāʿī : 1/293] ; on a dit : le verset descendit au sujet des hypocrites, qui combattaient aux côtés des musulmans pour le butin, non pour la récompense. ” [al-Baḥr al-Muḥīṭ, d’Abū Ḥayyān : 7/28]</p>
<p>[Citation coranique restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Puis le Très-Haut dit :</p>
<p>« Puis, Nous lui assignons l’Enfer où il brûlera méprisé et repoussé. »</p>
<p>c’est-à-dire : Dieu assigne alors la Géhenne à tous les désirants de l’immédiate qui sont dans l’incrédulité — à celui à qui Il y a donné ce qu’Il voulait comme à celui qui en fut frustré.</p>
<p>Ce châtiment embrasse trois choses : la permanence et l’éternité en Géhenne — à quoi renvoie Sa parole : « Puis, Nous lui assignons l’Enfer où il brûlera » ; l’humiliation et le mépris — à quoi renvoie Sa parole : « méprisé » ; et l’éloignement, le bannissement perpétuel de la miséricorde de Dieu — à quoi renvoie Sa parole : « repoussé ».</p>
<p>[Citations coraniques partielles (v. 18) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Puis le Très-Haut dit :</p>
<p>« Et ceux qui recherchent l’au-delà et fournissent les efforts qui y mènent, tout en étant croyants »</p>
<p>— le sens : quiconque veut l’au-delà d’une volonté qui s’en certifie, puis obéit à Dieu et recherche ce qui Lui plaît, croyant en Dieu, en Ses missions, en Sa récompense et en l’immensité de Sa rétribution de l’effort qu’il fournit pour elle.</p>
<p>« … alors l’effort de ceux-là sera reconnu. »</p>
<p>c’est-à-dire : ceux-là, Dieu reconnaît leur effort ; et Dieu ne reconnaît nulle action ni nul effort sans le rétribuer et lui pardonner à son sujet — à l’appui, la parole du Prophète — paix et bénédiction sur lui — dans le récit de l’homme qui abreuva le chien altéré : “ Dieu le lui reconnut et lui pardonna. ” [Muwaṭṭaʾ de l’imam Mālik, Livre du Jāmiʿ, chapitre : le Jāmiʿ de la nourriture et des boissons].</p>
<p>[Citations coraniques (v. 19) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Ainsi, trois conditions furent requises pour cette rétribution :</p>
<ul>
<li>Qu’il vise, par son action, la récompense de l’au-delà et sa béatitude : si cette intention ne survient pas, l’action n’en profite en rien — témoin le hadith : “ Les actions ne valent que par les intentions. ” [Ṣaḥīḥ al-Bukhārī, Livre du début de la révélation, chapitre : Comment débuta la révélation à l’Envoyé de Dieu — paix et bénédiction sur lui…] ; et parce que la finalité des actions est d’illuminer le cœur par la connaissance de Dieu, le Très-Haut, et par Son amour — ce qui n’advient que si l’agent se propose, en son action, l’adoration de Dieu, le Très-Haut, et la quête de Son obéissance.</li>
<li>Qu’il accomplisse l’action qui mène au succès de la récompense de l’au-delà — ce qui n’est qu’en fait de proximité et d’obéissances, non d’œuvres vaines ni d’actes interdits. Ibn ʿAṭiyya a dit : “ Il pose ensuite comme condition, à qui veut l’au-delà, d’œuvrer pour elle en son œuvre : c’est la constance en les œuvres du bien et en leurs paroles, selon le règle de la Loi et ses voies. ”</li>
<li>Qu’il agisse ainsi en croyant : car la condition pour que les œuvres de bien induisent la récompense est que la foi les précède — la condition absente, le conditionné n’a pas lieu. Et c’est là la plus grande des conditions du salut : nulle volonté ni nul effort ne profite sans elle. [Mafātīḥ al-ghayb, de Fakhr al-Dīn al-Rāzī : 20/317 (adapté) — réf. imprimée « 317/20 », ordre inversé]</li>
</ul>
<p>Puis le Glorifié expose que Son don et Sa subsistance d’ici-bas ne sont interdits à aucun des désirants de l’immédiate ni des désirants de l’au-delà. Il dit :</p>
<p>« Nous accordons abondamment à tous, ceux-ci comme ceux-là, des dons de ton Seigneur. Et les dons de ton Seigneur ne sont refusés [à personne]. »</p>
<p>[Citation coranique (v. 20) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>[<em>Kullan</em> (chacun)] prend le <em>naṣb</em> par “ <em>nūmidu</em> ” (Nous accordons), et son <em>tanwīn</em> tient lieu du nom annexé — c’est-à-dire : chacun des deux factions. J’ai <em>amdadtu</em> une chose quand je l’ai augmentée d’une autre que son espèce ; j’ai <em>madadtu</em> une chose quand je l’ai augmentée de son espèce. On a dit qu’ils sont synonymes : on dit <em>madadtu</em> et <em>amdadtu</em>. Et [“ ceux-ci comme ceux-là ” (<em>hāʾulāʾi wa-hāʾulāʾi</em>)] est en apposition (<em>badal</em>) de Sa parole : [“ chacun ” (<em>kullan</em>)] — il est donc en position de <em>naṣb</em>. Et Sa parole, le Très-Haut : [“ des dons de ton Seigneur ” (<em>min ʿaṭāʾi rabbika</em>)] peut viser les obéissances, pour les désirants de l’au-delà, et les désobéissances, pour les désirants de l’immédiate — interprétation rapportée d’Ibn ʿAbbās. Elle peut aussi, par “ don ” (<em>ʿaṭāʾ</em>), viser la subsistance de ce monde — c’est l’interprétation d’al-Ḥasan al-Baṣrī et de Qatāda : Dieu, le Très-Haut, subsiste en ce monde les désirants croyants de l’au-delà comme les désirants dénégateurs de l’immédiate, et les pourvoit de Son don — la prééminence et la divergence n’ont lieu qu’en l’au-delà. Ce sens s’accorde avec Sa parole :</p>
<p>« Et les dons de ton Seigneur ne sont refusés [à personne]. »</p>
<p>[Citations coraniques partielles (v. 20) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>c’est-à-dire : Sa subsistance en ce monde ne se resserre ni pour le croyant ni pour le dénégateur — et cette expression sied rarement à qui est comblé de désobéissances qui le perdent.</p>
<h3>Deuxièmement : le critère de la prééminence entre les gens en ce monde et en l’au-delà</h3>
<p>Le Très-Haut a dit :</p>
<p>« Regarde comment Nous favorisons certains sur d’autres. Et dans l’au-delà, il y a des rangs plus élevés et plus privilégiés. »</p>
<p>Elle comporte deux interprétations :</p>
<ul>
<li>On a dit : Regarde, ô Muḥammad, la faveur que Dieu accorde à certains sur d’autres en la subsistance et ce qui s’en approche — les figures, la noblesse, le rang et les fortunes. Sur ce pied, le “ don ” du verset précédent est la subsistance.</li>
<li>On a dit : Regarde, ô Muḥammad, la faveur que Dieu accorde à un peuple en leur donnant les obéissances qui mènent au Paradis, et à d’autres l’incrédulité qui mène au Feu — c’est la parole d’aṭ-Ṭabarī.</li>
</ul>
<p>Sur la première interprétation : le regard porte sur la faveur d’une personne sur une personne, parmi les croyants comme parmi les dénégateurs.</p>
<p>Sur la seconde : le regard porte sur la faveur d’une faction sur une faction.</p>
<p>[Citation coranique (v. 21) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Puis le Puissant et Majestueux informe que la faveur suprême n’a lieu qu’en l’au-delà. Le Très-Haut dit :</p>
<p>« Et dans l’au-delà, il y a des rangs plus élevés et plus privilégiés. »</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« … des rangs plus élevés et plus privilégiés »</p>
<p>— l’énoncé ne dit pas plus grands que quoi ; mais le sens et l’estimation le manifestent : des degrés plus grands que tout ce qui s’y ajoute, en existence ou par supposition. Tel est aussi le cas de Sa parole :</p>
<p>« A chacun des rangs (des récompenses) selon ses œuvres. » (al-Anʿām, 132)</p>
<p>car les gens sont gradués en l’au-delà : tel sera aux profondeurs (<em>darkāt</em>) de la Géhenne, en ses chaînes et ses carcans ; tel aux degrés supérieurs du Paradis, en sa béatitude et sa joie. Puis les gens des profondeurs sont gradués en leur état, comme le sont les gens des degrés — car le Paradis compte cent degrés, entre chaque couple de degrés comme entre le ciel et la terre. Témoin le hadith : “ Laisse les gens agir : au Paradis sont cent degrés, entre chaque deux degrés comme entre le ciel et la terre ; al-Firdaws est le sommet du Paradis et son milieu, au-dessus de lui est le Trône du Miséricordieux, et de lui jaillissent les rivières du Paradis : quand vous demandez à Dieu, demandez-Lui al-Firdaws. ” [Sunan at-Tirmidhī, chapitres de la description du Paradis, chapitre : ce qui est rapporté de la description des degrés du Paradis].</p>
<p>[Citations coraniques (v. 21 et parallèle al-Anʿām, 132) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR. La référence du parallèle suit l’usage d’Ibn ʿAṭiyya (al-Anʿām, 132) ; al-Aḥqāf, 19 porte le même début.]</p>
<p>Puis le Très-Haut indique ce par quoi se gagnent les degrés de l’au-delà : l’innocence du polythéisme et l’attache à la foi et à ses branches. Il dit :</p>
<p>« N’assigne point à Allah d’autre divinité ; sinon tu te trouveras méprisé et abandonné. »</p>
<p>L’interlocution du verset s’adresse à l’Envoyé de Dieu — paix et bénédiction sur lui —, et vaut pour toute la création. Le blâme échoit ici, de la part de Dieu, le Très-Haut, et des gens de raison, à ce que l’homme fasse d’un bâton ou d’une pierre mieux que lui-même, le voue à part à l’honneur, lui attribue la divinité et l’associe à Dieu qui l’a créé, subsisté et comblé de bienfaits. L’abandon, en cela, c’est que Dieu le livre à lui-même et cesse de le secourir.</p>
<p>[Citation coranique (v. 22) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Les versets visent la réalisation d’un ensemble de finalités éducatives, dont voici :</p>
<ul>
<li>L’affirmation de l’unicité de Dieu, Puissant et Majestueux, et l’interdit du polythéisme en Sa divinité et Son culte : car Dieu ne secourra pas qui Lui associe autre que Lui — Il l’abandonnera et le laissera à ce qu’il adore, qui ne profite ni ne nuit. Là est un appel à l’affranchissement de l’homme, que Dieu, le Très-Haut, a honoré et comblé de bienfaits nombreux, afin d’unifier la finalité en sa doctrine et son culte.</li>
<li>Que la subsistance et le don de Dieu en ce monde embrassent croyants et dénégateurs, obéissants et désobéissants — moyennant l’effort et l’action : Son don n’est ni retenu ni interdit à personne, fût-il dénégateur ou désobéissant, et la modulation de la subsistance n’a aucun lien avec la foi ou l’incrédulité. On n’infère donc pas de ce que l’homme acquiert ici-bas l’agrément de Dieu, le Très-Haut — car ce monde peut échoir à l’homme avec la pire des issues.<br>
[Que] la prééminence ne se mesure pas à ce que possèdent les gens en ce monde, d’argent ou de biens : la vraie prééminence tient à ce dont l’homme profite en son au-delà et par quoi il atteint les degrés supérieurs du Paradis — les œuvres pies qu’il avance pour son au-delà.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Quelle est la rétribution de celui qui borne son action à la quête de ce monde et oublie l’au-delà ?</li>
<li>Quel est le critère de la prééminence entre les gens en ce monde et en l’au-delà ?</li>
<li>Quel est le sort de celui qui associe à Dieu autre que Lui ?</li>
</ul>
<h3>L’investissement (istithmār)</h3>
<p>Ibn Māja rapporte en ses <em>Sunan</em> que le Prophète — paix et bénédiction sur lui — a dit : “ À qui ce monde était le souci, Dieu disperse son affaire, place sa pauvreté entre ses deux yeux, et il ne lui vient de ce monde que ce qui lui fut départi. Et à qui l’au-delà était l’intention, Dieu rassemble son affaire, place sa richesse en son cœur, et ce monde lui vient désarmé. ”<br>
[Sunan d’Ibn Māja, chapitres du renoncement (<em>zuhd</em>), chapitre : le souci de ce monde]<br>
Je contemple le texte et réponds à ce qui suit :</p>
<ul>
<li>J’explicite le rapport entre le contenu du hadith et les versets objet de la leçon.</li>
<li>Quand la quête de ce monde est-elle blâmable ?</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 23 à 25 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>wa-qāḍā</em> (وَقَضَىٰ).</p>
<p><em>uf</em> (أُفٍّ).</p>
<p><em>lā tanhurhumā</em> (وَلَا تَنْهَرْهُمَا).</p>
<p><em>qawlan karīman</em> (قَوْلًا كَرِيمًا).</p>
<p><em>li-l-awwābīna</em> (لِلْأَوَّابِينَ).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 23-25) : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Je recherche les manifestations de la piété filiale envers les parents durant leur vie et après leur mort.</li>
<li>J’explicite le sens de la parole du Très-Haut :</li>
</ul>
<p>« et par miséricorde, abaisse pour eux l’aile de l’humilité, et dis : “ Ô mon Seigneur, fais-leur, à tous deux, miséricorde comme ils m’ont élevé tout petit ”. » (al-Isrāʾ, 24)</p>
<ul>
<li>avec l’exposé de la finesse rhétorique qu’elle renferme ?</li>
</ul>
<p>[Citation coranique (v. 24 de la leçon suivante) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13525":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13525 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13525 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
