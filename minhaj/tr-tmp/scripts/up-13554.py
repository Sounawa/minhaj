#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13554 (tafsir-tanawi-2, Sourate al-Isrāʾ
34-36, leçon 10 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions :
- Bloc d'ouverture (17:34-36) : <p> vide après « الآيات » → restauré du
  quran-cache.
- Citations inline perdues par l'OCR, identifiées par l'exégèse :
  * v34 p1 (bien de l'orphelin) après « فقال تعالى : » ; « إِلَّا بِٱلَّتِى
    هِىَ أَحْسَنُ » + mot « أَحْسَنُ » dans les gloses (iʿrāb du relatif,
    bāʾ de contact) ; « حَتَّىٰ يَبْلُغَ أَشُدَّهُۥ » (limite de
    l'abstention) ;
  * « فَإِذَا بَلَغُوا۟ النِّكَاحَ » (Nisāʾ 4:6 — réf imprimée
    « النساء: 6 » conservée) ;
  * hadith Ibn ʿAbbās (Abū Dāwūd) : Anʿām 153 (réf imprimée conservée) +
    Nisāʾ 10 début + Baqara — le manuel imprime « 218 », le contenu cité
    (ويسألونك عن اليتامى… فإخوانكم) = 2:220 canonique → numérotation
    MAGHRÉBINE (décalage -2, cohérence R118 « Baqara 220 imprimé = 222
    cache ») : canonique en principal + note ;
  * v34 p2 (الوفاء بالعهد) ; mot « الْعَهْدَ » + « إِنَّ ٱلْعَهْدَ كَانَ
    مَسْـُٔولًۭا » dans les gloses ; v35 p1 (أوفوا الكيل) ; v35 p2
    (القسطاس) ; « ذَٰلِكَ خَيْرٌۭ وَأَحْسَنُ تَأْوِيلًۭا » + « كِلْتُمْ » /
    « زِنُوا۟ » / « تَأْوِيلًا » / « التأويل » (discussion Qatāda) ;
  * v36 complet + « إِنَّ ٱلسَّمْعَ وَٱلْبَصَرَ وَٱلْفُؤَادَ… » +
    « كُلُّ أُولَٰٓئِكَ » / « أُولَٰٓئِكَ » (kunya du raisonnable,
    Sībawayh « raʾaytuhum fī nujūm ») + « عَنْهُ » (2e pronom) ;
  * Rāzī (istithmār) : 6 versets du dossier « الوفاء بالعهود » restitués —
    Māʾida 1 (أوفوا بالعقود), Naḥl 91, Raʿd 20, Aḥzāb 23, Baqara 177,
    + v34 p2 en exergue (ensemble standard du Mafātīḥ 20/337).
- Structure : le source porte <h2><span>الفهم</span></h2> + h3 الشرح/h3
  استخلاص (niveaux inhabituels) et le lexique en <p> à gloses séparées
  par <br> → conservés tels quels.
- Anomalie : DEUX headings « ثالثا » (نهي الناس… + مقاصد الآيات) —
  duplication OCR ; le second rendu « Quatrièmement » (pattern
  أولا/ثانيا/ثالثا/رابعا), noté.
- Réf Rāzī « 337/20 » inversée → 20/337 (doctrine R113).
- iʿdād (versets 37-40 = leçon suivante 13593) : 4 expressions restituées
  du lexique de 13593 — noter que sa 1re entrée imprimée « ملوما :
  مسرورا بدنياه… » est un MALLABELING OCR : la glose est celle de
  مَرَحًا (v37) ; expressions : مَرَحًا / لَن تَخْرُقَ الْأَرْضَ / مَلُومًا /
  مَدْحُورًا ; la citation à iʿrāb + qirāʾat = v38 (سَيِّئُهُ/سَيِّئَة,
  discussion iʿrāb de « مكروها » dans 13593).
- GT non copié ; hadiths (Abū Dāwūd Ibn ʿAbbās ; Bayhaqī ×2 ; Muslim)
  traduits intégralement, réfs fidèles.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 34 à 36</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 34 à 36, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 10).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Reconnaître ce que Dieu a ordonné ou interdit en ces versets.</li>
<li>Conclure des versets le caractère sacré du bien de l’orphelin et le danger de son exploitation.</li>
<li>Me conformer aux ordres et aux interdits légaux en obéissance à Dieu, le Très-Haut — recherchant le licite, m’écartant de l’illicite.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Après que le Vrai, glorifié soit-Il, eut interdit la destruction des personnes, Il y fit suivre l’interdit de la destruction des biens — car ils sont, après les personnes, ce qu’il y a de plus précieux —, et Il en particularisa les biens des orphelins, car ils sont, des gens, ceux qui ont le plus besoin de protection. Puis le Glorifié ordonna de remplir les engagements et de donner pleine mesure aux mesures et aux poids, et interdit à l’homme de suivre ce dont il n’a point science, en parole ou en action.</p>
<p>Comment les tuteurs géreront-ils les biens des orphelins sans tomber dans l’interdit ? Et comment l’homme recherchera-t-il la justice en mesures et poids ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et n’approchez les biens de l’orphelin que de la façon la meilleure, (34) jusqu’à ce qu’il atteigne sa majorité. Et remplissez l’engagement, car on sera interrogé au sujet des engagements. (35) Et donnez la pleine mesure quand vous mesurez, et pesez avec une balance exacte. C’est mieux [pour vous] et le résultat en sera meilleur. (36) Et ne poursuis pas ce dont tu n’as aucune connaissance. L’ouïe, la vue et le cœur : sur tout cela, en vérité, on sera interrogé. » (al-Isrāʾ, 34-36)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p><em>ashuddahu</em> (sa majorité) : sa force en raison, expérience et regard pour lui-même.<br>
<em>masʾūlan</em> (interrogé) : requis.<br>
<em>bi-l-qisṭāsi l-mustaqīm</em> (avec la balance exacte) : avec la balance équitable et réglée.<br>
<em>taʾwīlan</em> (issue) : dénouement et aboutissement.<br>
<em>wa-lā taqfu</em> (et ne poursuis pas) : et ne dis pas, et ne suis pas.</p>
<h3>Extraction des idées des versets</h3>
<ul>
<li>De quoi Dieu, Puissant et Majestueux, a-t-Il interdit au début des versets ?</li>
<li>Quels sont les trois ordres que Dieu, Puissant et Majestueux, a donnés ?</li>
<li>De quoi Dieu, Puissant et Majestueux, a-t-Il interdit à la fin des versets ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : l’interdit de manger le bien de l’orphelin, si ce n’est de la meilleure façon</h3>
<p>Après que Dieu, le Très-Haut, eut interdit la destruction des personnes, Il interdit ici celle des biens, et en particularisa le bien de l’orphelin. Le Très-Haut dit :</p>
<p>« Et n’approchez les biens de l’orphelin que de la façon la meilleure, »</p>
<p>[Citation coranique (v. 34, début) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>L’interlocution s’adresse aux tuteurs qui fréquentent le bien des orphelins, et pareillement à quiconque s’est mêlé de quelque bien d’orphelin hors les tuteurs. L’orphelin est l’individu des enfants ; l’orphelinat (<em>yutm</em>) est la solitude : on dit <em>yatima l-ṣabī yatīmu</em>, “ l’enfant devient orphelin ”, quand il perd son père. Ibn al-Sikkīt dit : l’orphelinat, chez les hommes, vient du côté du père ; chez les bêtes, du côté de la mère. D’al-Māwardī [on rapporte] que l’orphelinat, chez les hommes, vient aussi du côté de la mère. Son pluriel est <em>aytām</em>, comme <em>sharīf / ashrāf</em> et <em>shahīd / ashhād</em> ; il se plie aussi en <em>yanātī</em>, comme <em>asīr / asārā</em>.</p>
<p>Et Sa parole, glorifié soit-Il : “ … que de la façon la meilleure ” (<em>illā bi-llatī hiya aḥsan</em>) : sinon en l’état qui est le meilleur — le relatif est adjectif d’un sous-entendu, estimé conforme au relatif qui est nom de féminin : on l’estime par “ l’état ” ou “ la qualité ”. Le <em>bāʾ</em> est de contact : sinon en contact avec la qualité ou l’état qui est le meilleur des états de proximité. Et <em>aḥsan</em> (la meilleure) est un nom de préférence hors de sa voie — c’est-à-dire : la bonne (<em>ḥasana</em>) —, celle qui profite sans dommage pour l’orphelin ni pour son bien.</p>
<p>[Citation coranique partielle (v. 34) et mot « aḥsan » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>On divergea sur le visé par “ l’état le meilleur ”. On a dit : sinon par la gestion qui le fait croître et multiplie ; on a dit : le visé est que tu manges avec lui si tu en as besoin.</p>
<p>Mujāhid rapporta d’Ibn ʿAbbās qu’il dit : s’il est dans le besoin, qu’il mange convenablement ; s’il s’enrichit, qu’il le restitue ; s’il ne s’enrichit pas, rien ne pèse sur lui. Mālik — que Dieu lui fasse miséricorde — dit : qu’il en prenne un salaire à mesure de sa peine. Tout cela entre dans ce qui est meilleur.<br>
Et Sa parole, glorifié soit-Il : “ jusqu’à ce qu’il atteigne sa majorité ” (<em>ḥattā yablugha ashuddahu</em>) : la limite de l’abstention du bien de l’orphelin — car la tutelle du tuteur sur l’orphelin n’est que jusqu’à la limite du mariage, en vertu de Sa parole :</p>
<p>« jusqu’à ce qu’ils atteignent (l’aptitude) au mariage » (an-Nisāʾ, 6)</p>
<p>Au-delà de cette limite, [la chose] reste en suspens jusqu’à ce que s’y dresse une preuve légale, ou que le consensus en la circonstance l’exige.</p>
<p>[Citations coraniques (v. 34 et an-Nisāʾ, 6) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p><em>Ashudd</em> est pluriel de <em>shadd</em> selon Sībawayh ; Abū ʿUbayda dit qu’il n’a point de singulier de sa propre matière. Son sens : sa force en raison, expérience et regard pour lui-même — ce qui n’est qu’avec la majorité. <em>Ashudd</em>, en l’école de Mālik, est double : la majorité par la pollution (ou ce qui en tient lieu, selon la divergence en cela), et la maturité en fait de bien.</p>
<p>On divergea — en deux paroles — sur l’inclusion de la maturité religieuse parmi les conditions : Ibn al-Qāsim n’y a point égard dès lors qu’il gouverne son bien ; d’autres des compagnons de Mālik y ont égard. En l’école d’Abū Ḥanīfa, <em>ashudd</em> est la majorité seule : nulle interdiction ne frappe chez lui un majeur, sinon qu’on reconnaisse de lui la légèreté.</p>
<p>D’ʿAbd Allāh ibn ʿAbbās — qu’Allah l’agrée, lui et son père — : “ Quand Dieu, Puissant et Majestueux, fit descendre : “ Et voilà Mon chemin dans toute sa rectitude, suivez-le donc ; et ne suivez pas les sentiers qui vous écartent de Sa voie. ” (al-Anʿām, 153) et “ Ceux qui mangent [disposent] injustement des biens des orphelins… ” (an-Nisāʾ, 10 — début du verset), quiconque avait un orphelin chez lui partit séparer sa nourriture de la sienne, et sa boisson de la sienne ; il mettait à part l’excédent de sa nourriture et le réservait jusqu’à ce qu’il le mangeât ou qu’il se gâtât. Cela leur pesa fort ; ils en firent mention à l’Envoyé de Dieu — paix et bénédiction sur lui —, et Dieu, Puissant et Majestueux, fit descendre : “ Et ils t’interrogent au sujet des orphelins. Dis : “ Leur faire du bien est la meilleure action. Si vous vous mêlez à eux, ce sont alors vos frères. ” (al-Baqara, 220 — le manuel imprime « 218 », numérotation maghrébine) — ils mêlèrent alors leur nourriture à la sienne, et leur boisson à la sienne. ” [Sunan d’Abū Dāwūd, Livre des testaments, chapitre : du mélange de l’orphelin en la nourriture]</p>
<p>[Citations coraniques du hadith (al-Anʿām, 153 ; an-Nisāʾ, 10 ; al-Baqara, 220) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<h3>Deuxièmement : l’ordre de remplir l’engagement et de donner pleine mesure et juste poids</h3>
<p>Après que Dieu, glorifié soit-Il, eut interdit trois choses — la fornication, le meurtre et le manger du bien de l’orphelin —, Il y fit suivre l’ordre de trois choses :</p>
<ul>
<li>Le premier ordre est Sa parole, le Très-Haut :</li>
</ul>
<p>« Et remplissez l’engagement, car on sera interrogé au sujet des engagements. »</p>
<p>[Citation coranique (v. 34, fin) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Sa parole : “ l’engagement ” (<em>al-ʿahd</em>) est une locution générale pour tout engagement et tout contrat entre l’homme et son Seigneur, ou entre lui et les créatures, en fait d’obéissance — c’est-à-dire : remplissez tous les engagements par lesquels vous vous êtes engagés, qu’ils soient envers Dieu ou envers les gens, car vous en serez interrogés au Jour de la Résurrection. Et Sa parole, le Très-Haut : “ car on sera interrogé au sujet des engagements ” : c’est-à-dire requis de celui à qui fut promu comme de celui qui promit — a-t-il rempli, oui ou non ? C’est le motif de l’ordre de remplir l’engagement ; la reprise du mot “ engagement ” là où son pronom eût suffi marque l’importance qui s’y attache ; et le complément de “ interrogé ” est omis par évidence.</p>
<p>[Mots et citations coraniques (v. 34) restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Le second ordre est Sa parole, le Très-Haut : « Et donnez la pleine mesure quand vous mesurez, et pesez avec une balance exacte. » — Dieu, le Très-Haut, ordonne en ce verset aux gens du commerce, de la mesure et du poids, de donner le droit en leur mesure et leur poids. D’Ibn ʿAbbās fut rapporté qu’il s’arrêtait au marché et disait : “ ô communauté des <em>mawālī</em>, vous avez eu en charge deux choses par quoi périrent les peuples d’avant vous : cette mesure et ce poids. ” Ibn ʿAṭiyya [dit] : ce verset exige que la mesure incombe au vendeur — car on ne dit pas à l’acheteur : “ donne pleine mesure ” ; tel est l’apparent de l’énoncé et ce qui s’en offre d’abord.</li>
<li>Le troisième ordre est Sa parole, le Très-Haut : “ pesez avec la balance exacte ” (<em>bi-l-qisṭāsi l-mustaqīm</em>). Le <em>qisṭās</em> est la balance, et le visé est le genre des balances équitablement réglées, en quelque état que ce soit. Mujāhid dit : le <em>qisṭās</em> est “ la justice ” (<em>al-ʿadl</em>) en romain (<em>bir-rūmiyya</em>) ; on a dit : c’est une métaphore de la justice, non un instrument.</li>
</ul>
<p>[Citations coraniques (v. 35) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Ḥamza, al-Kisāʾī et Ḥafṣ lurent au <em>kasra</em> du <em>qāf</em> ; le reste des Sept, au <em>ḍamma</em> — deux langues. Une faction lut, par substitution de la première <em>sīn</em> en <em>ṣād</em> (<em>qiṣṭās</em>). Ibn ʿAṭiyya [dit] : il ne se peut pas qu’il vienne de <em>qisṭ</em> (la part), les deux matières différant — la matière de <em>qisṭ</em> est <em>q-s-ṭ</em>, celle-ci : <em>q-s-ṭ-s</em>.</p>
<p>Et Sa parole, le Très-Haut : “ C’est mieux [pour vous] et le résultat en sera meilleur ” — “ C’est mieux ” est une phrase reprise (<em>jumla mustaʾnafa</em>), et l’indexation porte sur le mentionné : la mesure et le poids, tirés des deux verbes [“ quand vous mesurez ” (<em>kiltum</em>)] et [“ pesez ” (<em>zinū</em>)]. [“ meilleur ” (<em>taʾwīlan</em>)] est un nom de préférence : c’est-à-dire que donner pleine mesure et établir le poids vaut mieux pour vous que le frauder. Le visé, en ce verset, par [“ l’issue ” (<em>taʾwīl</em>)] est le dénouement et l’aboutissement — parole de Qatāda. Il se peut aussi que <em>taʾwīl</em> soit l’infinitif de <em>taʾawwala</em> : le bien se dénouera pour vous en toutes vos affaires si vous avez bien fait en mesure et poids. L’obligation du sujet responsable est de rechercher le juste en mesure et poids : s’il survient à l’homme, après cette recherche, un peu de fraude qu’il n’a point visée, sa faute est levée — c’est là ce qu’il est impossible d’écarter en l’état du possible.</p>
<p>[Citations coraniques et mots (v. 35) restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<h3>Troisièmement : l’interdit fait aux gens de suivre ce dont ils n’ont pas science</h3>
<p>Après l’ordre de remplir l’engagement, de donner pleine mesure et la justice du poids, le Noble Coran revint à l’interdit de suivre ce dont on n’a point science. Le Très-Haut dit :</p>
<p>« Et ne poursuis pas ce dont tu n’as aucune connaissance. L’ouïe, la vue et le cœur : sur tout cela, en vérité, on sera interrogé. »</p>
<p>[Citation coranique (v. 36) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Son sens : et ne dis pas, et ne suis pas. Ibn ʿAṭiyya [dit] : mais c’est une locution employée pour l’accusation infondée et le soupçon — d’où la parole du Prophète — paix sur lui : “ Nous sommes les fils de an-Naḍḍār : nous ne soupçonnons point notre mère, ni ne nous désavouons de notre père. ” On dit : untel est mon <em>qafwā</em> — c’est-à-dire l’objet de mon soupçon. Les Arabes disent : “ Bien souvent qui entendit mon excuse n’entendit point mon accusation ” — c’est-à-dire ce dont on m’accusa ; c’est la parabole de qui divulgue son secret et s’excuse d’une faute que l’excusé n’a pas entendue. Ibn ʿAbbās dit aussi, et Mujāhid : “ et ne poursuis pas ” signifie : et n’accuse pas. L’origine de la locution est la poursuite de la trace : on dit <em>qafawtu l-athar</em>, “ j’ai suivi la trace ”. Il est vraisemblable qu’elle vienne de <em>qafā</em> (la nuque) — d’où la rime (<em>qāfiya</em>) du poème : elle suit le vers.</p>
<p>Le sens du verset est donc : ne suis pas de la parole, par ta langue, ce dont tu n’as point science. Mundhir ibn Saʿīd al-Ballūṭī al-Qurṭubī tint que <em>qafā</em> et <em>qāfa</em> sont comme <em>jabadha</em> et <em>jalaba</em> (variants d’un même radical). Ce verset, en somme, interdit le faux témoignage, l’accusation infondée et ce qui s’en approche des paroles mensongères et mauvaises.</p>
<p>Puis le Très-Haut dit : “ L’ouïe, la vue et le cœur : sur tout cela, en vérité, on sera interrogé. ” — motif de l’interdit précédent. Il exprima l’ouïe, la vue et le cœur par [“ tout cela ” (<em>kullu ulāʾika</em>)] car ce sont des sens doués de perception, et Il les fit, en ce verset, interrogés — ce qui est l’état de qui raisonne ; c’est pourquoi Il les exprima par [“ ceux-là ” (<em>ulāʾika</em>)].</p>
<p>Sībawayh — que Dieu lui fasse miséricorde — rapporta qu’il fut dit : “ Je les ai vus parmi les étoiles ” (<em>raʾaytuhum fī nujūm</em>) : car lorsqu’Il les décrivit par la prosternation — qui est l’acte de qui raisonne —, Il les exprima par la <em>kunya</em> du raisonnable.</p>
<p>Le pronom en [“ de cela ” (<em>ʿanhu</em>)] renvoie à ce dont l’homme n’a point science. Le sens est alors : Dieu, le Très-Haut, interroge l’ouïe de l’homme, sa vue et son cœur sur ce qu’il a dit sans science — et son démenti viendra de ses propres membres : c’est l’extrême de l’ignominie. Il se peut aussi que le pronom en “ de cela ” renvoie à [“ tout cela ” (<em>kullu ulāʾika</em>)], qui est pour l’ouïe, la vue et le cœur ; le sens : Dieu, le Très-Haut, interroge l’homme sur ce qu’ont contenu son ouïe, sa vue et son cœur — comme s’Il disait : de tout cela l’homme fut interrogé, c’est-à-dire sur les perceptions survenues à ceux-ci et les erreurs venues d’eux. L’estimation : “ il fut interrogé de leurs œuvres ” — le discours procède par omission de l’annexé.</p>
<p>[Citations coraniques et mots (v. 36) restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<h3>Quatrièmement : les finalités des versets</h3>
<p>[Le manuel imprime « ثالثا » une seconde fois — duplication OCR ; la numérotation logique est restituée.]</p>
<p>Ces versets orientent vers la réalisation d’un ensemble de finalités éducatives, dont :</p>
<ul>
<li>La préservation des droits des orphelins, l’audace niée sur leurs biens et l’exploitation de leur faiblesse — due à leur petitesse et à la perte de leurs pères : manifestation de l’entraide et de la solidarité entre les gens.</li>
<li>La préservation des droits des gens en les transactions, la justice en mesures et poids, l’absence de fraude, et le remplissement des engagements et obligations en général — qu’il s’agisse des droits de Dieu ou de ceux des serviteurs.</li>
<li>Le remplissement des droits et leur versement à leurs titulaires, entiers et non amoindris, et la présence de la surveillance divine en cela, concourent à la moralisation de la vie publique et privée, à la stabilité et à la confiance en les transactions entre les gens, et à la prospérité économique et commerciale du pays.</li>
<li>La vérification des nouvelles et l’évitement de toute espèce de tromperie, de mensonge, d’accusation infondée et d’imputation aux autres, affermit l’affection et l’harmonie entre les gens et les préserve des dommages et des ruines qui se bâtissent sur des paroles mensongères et des plaintes de malice.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Qu’est-il permis au tuteur de prendre du bien de l’orphelin ?</li>
<li>Que signifie la parole du Très-Haut : « Et ne poursuis pas ce dont tu n’as aucune connaissance » ?</li>
</ul>
<ul>
<li>Quel est le statut juridique du remplissement des engagements ? Et la justice contraint-elle l’homme à remplir l’obligation qu’il a contractée sur lui-même ?</li>
<li>Que peux-tu conclure de la parole du Très-Haut : « L’ouïe, la vue et le cœur : sur tout cela, en vérité, on sera interrogé » ?</li>
</ul>
<h3>L’investissement (istithmār)</h3>
<p>Fakhr al-Dīn al-Rāzī dit, en son commentaire de la parole du Très-Haut : « Et remplissez l’engagement, car on sera interrogé au sujet des engagements. » : “ Le résumé du dire en ce verset : ce qu’exige ce verset, c’est que tout contrat et tout engagement conclu entre deux hommes, il leur est obligatoire d’en remplir la teneur — sauf si une preuve détachée indique qu’il n’est pas obligatoire de le remplir. Il exige donc de juger valide toute vente qui s’est faite par consentement, et valide toute société qui s’est faite par consentement. Ce texte est affermi par le reste des versets indiquant le remplissement des engagements et des contrats, comme Sa parole : “ O les croyants ! Remplissez fidèlement vos engagements. ” (al-Māʾida, 1)</p>
<p>et Sa parole : “ Soyez fidèles au pacte d’Allah après l’avoir contracté ” (an-Naḥl, 91), et Sa parole : “ ceux qui remplissent leur engagement envers Allah et ne violent pas le pacte ” (ar-Raʿd, 20), et Sa parole : “ Il est, parmi les croyants, des hommes qui ont été sincères dans leur engagement envers Allah ” (al-Aḥzāb, 23)</p>
<p>et Sa parole : “ … ceux qui remplissent leurs engagements lorsqu’ils se sont engagés ” (al-Baqara, 177) — et sa parole sur lui le salut : “ Le bien d’un homme musulman n’est licite que de son entier gré. ” [as-Sunan al-kubrā d’al-Bayhaqī : Livre de l’usurpation, chapitre : de qui usurpa une planche et l’intégra à un navire, ou bâtit sur elle un mur], et sa parole : “ Quand les deux espèces diffèrent, vendez comme vous voulez, de main en main. ” [Ṣaḥīḥ Muslim, Livre de l’affermage, chapitre : du change et de la vente de l’or contre l’argent au comptant], et sa parole : “ Quiconque achète une chose sans l’avoir vue a le choix quand il la voit. ” [as-Sunan al-kubrā d’al-Bayhaqī : Livre des ventes, chapitre : de qui dit permise la vente de la chose absente].</p>
<p>Tous ces versets et ces reports indiquent que le fondement, en ventes, engagements et contrats, est la validité et l’obligation de s’y tenir. Cela posé, nous disons : si nous trouvons un texte plus particulier que ces textes, indiquant nullité et corruption, nous jugeons par lui — primauté du particulier sur le général ; sinon, nous jugeons de la validité en tout. Quant à la particularisation du texte par l’analogie, nous l’avons invalidée. Par cette voie, les chapitres des transactions, en leur longueur et leur ampleur, se trouvent réglés et connus par ce seul verset ; et le sujet responsable est cœur en paix, âme rassurée en son action — car puisque ces textes ont indiqué leur validité, il n’est plus d’exposé après l’exposé de Dieu ; et la Loi se trouve réglée et connue. ” [Mafātīḥ al-ghayb, de Fakhr al-Dīn al-Rāzī : 20/337 — réf. imprimée « 337/20 », ordre inversé]</p>
<p>[Citations coraniques du dossier « le remplissement des engagements » (al-Māʾida, 1 ; an-Naḥl, 91 ; ar-Raʿd, 20 ; al-Aḥzāb, 23 ; al-Baqara, 177) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<ul>
<li>Comment le texte a-t-il argumenté que le fondement des contrats est la validité ?</li>
<li>En quoi tient la mise au point de tous les chapitres des transactions par un seul verset ?</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 37 à 40 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>marḥan</em> (مَرَحًا — l’enjouement orgueilleux).</p>
<p><em>lan takhruqa l-arḍa</em> (لَن تَخْرُقَ الْأَرْضَ — tu ne fendras point la terre).</p>
<p><em>malūman</em> (مَلُومًا — blâmé).</p>
<p><em>madḥūran</em> (مَدْحُورًا — repoussé).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 37-40) : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Je recherche la vision de l’islam des deux qualités de l’orgueil (<em>kibr</em>) et de l’humilité (<em>tawāḍuʿ</em>), et leurs effets sur les rapports sociaux.</li>
<li>J’explicite le sens de la parole du Très-Haut :</li>
</ul>
<p>« Ce qui est mauvais en tout cela est détesté de ton Seigneur. » (al-Isrāʾ, 38)</p>
<p>— en exposant son <em>iʿrāb</em> et ses lectures.</p>
<p>[Citation coranique (v. 38, de la leçon suivante) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13554":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13554 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13554 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
