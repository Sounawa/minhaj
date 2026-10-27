#!/usr/bin/env python3
# savant(fiqh-1es/11438) — Le déroulement de la prière : la récitation et les évocations
# Leçon 13 — Risāla d'Ibn Abī Zayd al-Qayrawānī, comm. Kifāyat aṭ-ṭālib ar-rabbānī (Abū al-Ḥasan), ḥāshiya al-ʿAdawī
#
# Vérifications dorar.net (sunnah.com bloqué Turnstile — cf. R82) :
#  - ʿUmar/Abū Rimtha « اجلس فإنه لم يهلك أهل الكتاب… أصاب الله بك يا ابن الخطاب » : Abū Dāwūd 1007 (اللفظ له),
#    Ṭabarānī Awsaṭ 728, Ḥākim 1011 — isnād ṣaḥīḥ (al-Albānī, Hidāyat ar-rāwātīn 932).
#  - Anas « من صلى الغداة في جماعة… كأجر حجة وعمرة » : Tirmidhī 586 (+ variantes « تامة تامة تامة » non imprimées
#    par le manuel), al-Albānī Silsila Ṣaḥīḥa 3403.
#  - Umm Ḥabība « من حافظ على أربع ركعات قبل الظهر وأربع بعدها حرمه الله على النار » : Abū Dāwūd 1269,
#    Tirmidhī 427, Nasāʾī 1816, Ibn Mājah 1160, Ibn Khuzayma 1190.
#  - Ibn ʿUmar « رحم الله امرأ صلى قبل العصر أربعا » : Abū Dāwūd 1271, Tirmidhī 430, Aḥmad 5980
#    (Ibn al-Qaṭṭān : ḍaʿīf — cité tel quel par le manuel).
#  - Ibn ʿUmar « صلاة الليل مثنى مثنى… » : Bukhārī 990, Muslim 749.
#  - Abū Umāma « عليكم بقيام الليل فإنه دأب الصالحين قبلكم… » : Tirmidhī après n° 3549, Ibn Khuzayma 1135,
#    Abū Nuʿaym (al-Mundhirī, at-Targhīb 1/291) — texte EXACT.
#  - Jābir « من خاف أن لا يقوم من آخر الليل فليوتر أوله… » : Muslim 755.
#  - Ṭalq b. ʿAlī « لا وتران في ليلة » : Abū Dāwūd 1439, Tirmidhī 470, Nasāʾī 1679.
#  - ʿĀʾisha/ʿAbd al-ʿAzīz b. Jurayj « سألنا عائشة بأي شيء كان يوتر… » : Tirmidhī 463, Ibn Mājah 1173,
#    Aḥmad 25906 — CONFIRME la doctrine des 3 zones-image (al-Aʿlā / al-Kāfirūn / al-Ikhlāṣ + muʿawwidhatayn).
#  - Abū Qatāda « إذا دخل أحدكم المسجد فليركع ركعتين قبل أن يجلس » : Bukhārī 444, Muslim 714.
#  - « قرأ في ركعتي الفجر قل يا أيها الكافرون وقل هو الله أحد » : Ibn Mājah 1148 (اللفظ له), Muslim 726 —
#    CONFIRME la 4e zone-image.
#  - Zarrūq (enrichissement) « أخذت بالعزم / أخذت بالحزم » : dorar = versions canoniques Abū Dāwūd 1434
#    (Abū Qatāda, Talkhīṣ al-Ḥabīr 2/502) et Ibn Khuzayma 1085/Ibn Ḥibbān 2446/Ḥākim 1121 (Ibn ʿUmar) —
#    attribuent à Abū Bakr al-ḤAZM et à ʿUmar al-QUWWA ; le manuel (via Zarrūq 1/273) imprime l'attribution
#    croisée ʿazm/ḥazm → traduit tel qu'imprimé + note N.d.T. documentant la variante canonique.
#
# Zones corrompues du CMS (noms de sourates en image dans le manuel) restaurées PAR DOCTRINE
# (matn du Risāla + hadith ʿĀʾisha Tirmidhī 463 + hadith fajr Muslim 726/Ibn Mājah 1148) :
#  1. shafʿ 1ʳᵉ rakʿa : al-Aʿlā (87) — 2. shafʿ 2ᵉ : al-Kāfirūn (109) — 3. witr : al-Ikhlāṣ (112)
#  4. rakʿatā al-fajr : al-Kāfirūn (109) + al-Ikhlāṣ (112)
#
# Fix 11437 : coquille « les pures ommages] à Dieu » → « les pures à Dieu » (الزَّاكِيَاتُ للهِ).
import json, re, sys

BOOK = 'content/books/fiqh-1es.json'
DOC = '11438'

html_fr = """
<h1>Le déroulement de la prière : la récitation dans la prière et les évocations qui la suivent (al-qirāʾa fī aṣ-ṣalāh wa-dh-dhikr baʿdahā) — leçon de fiqh de la Risāla d'Ibn Abī Zayd al-Qayrawānī avec le commentaire Kifāyat aṭ-ṭālib ar-rabbānī</h1>
<p>Leçon sur la récitation dans la prière et l'évocation qui la suit, matière Fiqh, sur la base de la <em>Risāla</em> d'Ibn Abī Zayd al-Qayrawānī avec le commentaire d'Abū al-Ḥasan, <em>Kifāyat aṭ-ṭālib ar-rabbānī</em>, en marge de la <em>ḥāshiya</em> d'al-ʿAdawī — livre de l'élève (kitāb at-tilmīdh wa-t-talmīdha) de la première année de l'enseignement secondaire traditionnel (<em>ʿatīq</em>) — la treizième leçon.</p>
<p>Objectifs de la leçon :</p>
<ol>
<li>Connaître les règles de ce qui suit la prière.</li>
<li>Distinguer la quantité et la modalité de la récitation dans les prières.</li>
<li>Saisir les secrets de l'évocation et de l'invocation pendant la prière et après elle.</li>
<li>Connaître les prières surérogatoires et la modalité de leur récitation.</li>
</ol>
<p>La récitation du Coran rend la prière valide et l'achève, et l'évocation de Dieu l'embellit et la pare : aussi l'islam a-t-il institué la récitation dans la prière, et recommandé l'évocation en son cours et à sa suite.<br>
Quelle est la quantité dont il est demandé de réciter dans la prière ? Et quelle est la formule de l'évocation recommandée après la prière ?</p>
<h2>Le texte (matn)</h2>
<p>Ibn Abī Zayd — que Dieu lui fasse miséricorde — a dit :</p>
<p>« Il est recommandé de faire l'évocation à la suite des prières : glorifier Dieu trente-trois fois (<em>tasbīḥ</em>), louer Dieu trente-trois fois (<em>taḥmīd</em>), magnifier Dieu trente-trois fois (<em>takbīr</em>), et achever la centaine par : “Il n'est de divinité que Dieu, Lui seul, sans associé ; à Lui la royauté et à Lui la louange, et Il est capable de toute chose.” Il est recommandé, à la suite de la prière de l'aube (<em>ṣubḥ</em>), de persévérer dans l'évocation, la demande de pardon, la glorification et l'invocation jusqu'au lever du soleil ou peu avant — cela n'est pas une obligation. Il accomplit les deux rakʿa de l'aube avant la prière du ṣubḥ, après [l'apparition de] l'aube : il récite, dans chaque rakʿa, Umm al-Qurʾān (la Fātiḥa), en secret. »</p>
<p>« La récitation dans la prière du midi (<em>ẓuhr</em>) est comme la récitation du ṣubḥ, tirée des sourates longues (<em>aṭ-ṭiwāl</em>), ou un peu en deçà ; il ne récite à voix haute aucune partie de la récitation. Il récite, dans la première et la deuxième rakʿa, dans chacune, Umm al-Qurʾān et une sourate, en secret ; et dans les deux dernières, Umm al-Qurʾān seule, en secret. Il récite le tashahhud dans la première assise, jusqu'à : “et j'atteste que Muḥammad est Son serviteur et Son messager” ; puis il se lève — et ne dit le takbīr qu'une fois dressé debout. »</p>
<p>« Ainsi font l'imām et l'homme qui prie seul. Quant au suivi (<em>maʾmūm</em>), après que l'imām a dit le takbīr, il se lève à son tour ; et quand il est dressé debout, il dit le takbīr. Il en fait, pour le reste de la prière — description de l'inclinaison, des prosternations et de l'assise — selon ce qui a été exposé pour le ṣubḥ. Puis il prie surérogatoirement : il lui est recommandé de prier en surérogation quatre rakʿa, saluant à chaque deux ; et il lui est recommandé de même avant la prière de l'après-midi (<em>ʿaṣr</em>). Dans l'ʿaṣr il fait comme nous l'avons décrit pour le ẓuhr, exactement — sinon qu'il récite, dans les deux premières rakʿa, avec Umm al-Qurʾān, les sourates brèves (<em>al-qiṣār</em>) : telles aḍ-Ḍuḥā et Innā anzalnāhu, et leurs semblables. »</p>
<p>« Quant au coucher (<em>maghrib</em>), il récite à voix haute dans les deux premières rakʿa, récitant dans chacune Umm al-Qurʾān et une sourate parmi les sourates brèves ; dans la troisième, Umm al-Qurʾān seulement ; puis tashahhud et salutation. Il est recommandé de prier en surérogation, après elle, deux rakʿa — et ce qu'on y ajoute n'est que bien : s'il prie en surérogation six rakʿa, c'est bon. La surérogation entre le maghrib et la veillée (<em>ʿishāʾ</em>) y est vivement encouragée. Pour le reste de son affaire : comme ce qui a été exposé pour les autres. »</p>
<p>« Quant à la dernière veillée (<em>al-ʿishāʾ al-ākhira</em>) — c'est l'<em>ʿatama</em>, et le nom d'ʿishāʾ lui est plus particulier et plus propre —, il récite à voix haute dans les deux premières Umm al-Qurʾān et une sourate en chaque rakʿa, sa récitation étant un peu plus longue que celle de l'ʿaṣr ; dans les deux dernières, Umm al-Qurʾān en chaque rakʿa, en secret. Puis il fait, pour le reste, selon la description précédente. Dormir avant elle est blâmable, de même que parler après elle sans nécessité. La récitation qu'on fait en secret dans toute la prière consiste à mouvoir la langue en articulant le Coran ; quant à la voix haute (<em>jahr</em>), c'est se faire entendre soi-même et qui vous est proche, si l'on est seul. La femme est en deçà de l'homme quant à la voix haute ; et elle est, dans la configuration de la prière, comme lui — sinon qu'elle se tient serrée : elle n'écarte ni ses cuisses ni ses bras, et se tient resserrée, ramassée, dans son assise, ses prosternations et toute son affaire. »</p>
<p>« Puis il accomplit le shafʿ et le witr à voix haute. De même, il est recommandé, dans les surérogations de la nuit, de réciter à voix haute, et dans celles du jour, en secret ; s'il récite à voix haute de jour dans sa surérogation, c'est là une latitude. Le moindre shafʿ est de deux rakʿa : il est recommandé de réciter, dans la première, Umm al-Qurʾān et [sourate reproduite en image dans le manuel : « Proclame la transcendance du nom de ton Seigneur, le Très-Haut » — al-Aʿlā (87)], et dans la seconde, Umm al-Qurʾān et [sourate reproduite en image dans le manuel : « Dis : ô vous les négateurs » — al-Kāfirūn (109)] ; puis tashahhud et salutation. Puis il accomplit le witr en une rakʿa, où il récite Umm al-Qurʾān et [sourate reproduite en image dans le manuel : « Dis : Il est Dieu, Unique » — al-Ikhlāṣ (112)] et les deux protectrices (<em>al-muʿawwidhatayn</em>). S'il ajoute des shafʿ, il fait du dernier d'entre eux le witr. Le Messager de Dieu — paix et bénédiction sur lui — priait la nuit douze rakʿa, puis faisait le witr par une ; il a été dit : dix rakʿa, puis il fait le witr par une. »</p>
<p>« Le meilleur de la nuit, pour la station (<em>qiyām</em>), en est la fin : qui diffère sa surérogation et son witr jusqu'à sa fin, cela est meilleur — sauf celui que domine l'incapacité de s'éveiller : qu'il avance son witr, avec ce qu'il veut de surérogations, au début de la nuit ; puis, s'il veut, quand il s'éveille à sa fin, qu'il prie ce qu'il veut de surérogations, deux par deux (<em>mathnā mathnā</em>), sans refaire le witr. Celui dont les yeux ont eu raison — au détriment de sa part (<em>ḥizb</em>) — peut la prier entre le lever de l'aube et le premier grisonnement du jour (<em>isfār</em>) ; puis il fait le witr, puis prie le ṣubḥ. Nul ne rattrape le witr qui s'en souvient après avoir prié le ṣubḥ. »</p>
<p>« Quiconque entre à la mosquée en état de pureté ne s'assoit pas avant d'y prier deux rakʿa, s'il est en un temps où l'inclinaison est permise. Quiconque entre à la mosquée sans avoir accompli [les deux rakʿa] de l'aube : les deux rakʿa de l'aube lui en tiennent lieu. S'il a accompli [les deux rakʿa] de l'aube en sa demeure puis vient à la mosquée, on a divergé : il a été dit qu'il s'incline [en deux rakʿa] ; il a été dit qu'il ne s'incline pas. Nulle prière surérogatoire après l'aube, hormis les deux rakʿa de l'aube, jusqu'au lever du soleil. »</p>
<h2>La compréhension</h2>
<h3>Explication lexicale</h3>
<ul>
<li><em>at-tamādī</em> : persévérer en une chose — y persister et refuser de s'en détourner.</li>
<li><em>munzawiya</em> : resserrée, ramassée.</li>
<li><em>mathnā</em> : deux par deux — il salue à chaque deux rakʿa.</li>
<li><em>ḥizb</em> : sa part (<em>wird</em>) — la quantité qu'il prie chaque nuit.</li>
</ul>
<h3>Extraction des contenus du matn</h3>
<ul>
<li>Détermine, à partir du matn, la règle de l'évocation après la prière et sa formule.</li>
<li>Extrais du matn la quantité que récite le prieur dans chaque prière.</li>
<li>Extrais du matn la modalité de la récitation dans la prière surérogatoire, de nuit ou de jour.</li>
</ul>
<h2>L'analyse</h2>
<p>Cette leçon embrasse ce qui suit :</p>
<h3>Premièrement : la règle de l'évocation après la prière et sa formule</h3>
<h4>a. Sa règle</h4>
<p>Il est recommandé de faire l'évocation après les prières obligatoires, sans les séparer d'une surérogation — en vertu de ce qu'a rapporté Abū Dāwūd : « … L'homme qui avait rejoint [la prière commune] dès le premier takbīr se leva pour compléter [ce qui lui manquait] ; ʿUmar bondit vers lui, le prit par l'épaule et le secoua, puis dit : “Assieds-toi : les gens du Livre ne périrent que parce qu'entre leurs prières il n'y avait nul intervalle.” Le Prophète — paix et bénédiction sur lui — leva son regard et dit : “Dieu a visé juste par toi, ô fils d'al-Khaṭṭāb.” » [Sunan d'Abū Dāwūd, « chapitre de l'homme qui prie surérogatoirement à la place même où il a prié l'obligatoire ».]</p>
<p>Il est recommandé, après la prière de l'aube, de persévérer dans l'évocation, la demande de pardon, la glorification et l'invocation, jusqu'au lever du soleil ou peu avant ; la source en est sa parole — paix et bénédiction sur lui — : « Quiconque prie l'aube en commun, puis s'assoit évoquant Dieu jusqu'à ce que le soleil se lève, puis prie deux rakʿa, cela lui vaut la récompense d'un pèlerinage (<em>ḥajja</em>) et d'une ʿumra. » [Sunan at-Tirmidhī, « chapitre de ce qui est recommandé de s'asseoir à la mosquée après la prière de l'aube jusqu'au lever du soleil ».] En cela, parole de l'auteur : « Il est recommandé de faire l'évocation à la suite des prières : glorifier Dieu… jusqu'à : ou peu avant [son lever] — cela n'est pas une obligation. »</p>
<h4>b. Sa formule</h4>
<p>L'évocation après la prière est parvenue en des formules transmises du Prophète — paix et bénédiction sur lui —, parmi lesquelles : qu'il glorifie Dieu trente-trois fois, loue Dieu trente-trois fois, magnifie Dieu trente-trois fois, et achève la centaine par : “Il n'est de divinité que Dieu, Lui seul, sans associé ; à Lui la royauté et à Lui la louange, et Il est capable de toute chose.” Il est permis de les dire groupées ou séparées.</p>
<h3>Deuxièmement : la modalité de la récitation dans les prières</h3>
<h4>a. La longueur et la brièveté</h4>
<p>La récitation de la sourate diffère — en longueur et en brièveté comme en secret et en voix haute — d'une prière à l'autre, ainsi : la récitation du ẓuhr est comme celle du ṣubḥ — tirée des longues, ou un peu en deçà —, sinon qu'elle est en secret ; dans le maghrib, elle est tirée des sourates brèves ; dans l'ʿishāʾ, elle est un peu plus longue que la récitation de l'ʿaṣr. En cela, parole de l'auteur : « Dans l'ʿaṣr, il fait comme nous l'avons décrit pour le ẓuhr, sauf qu'il récite dans les deux premières rakʿa… jusqu'à la fin [du passage]. »</p>
<h4>b. Le secret et la voix haute</h4>
<p>Les prières où l'on récite en secret, et celles où l'on récite à voix haute, sont des choses sues. Le secret, dans la récitation, est de deux sortes : le moindre — mouvoir la langue seulement — et le plus haut : que l'homme se fasse entendre lui-même, seulement ; quiconque récite de son cœur, sa prière n'est pas valable. La voix haute de même est de deux sortes : la moindre — pour l'homme : se faire entendre soi-même et qui lui est proche — et la plus haute : rien ne la borne. Quant à la femme, secret et voix haute s'équivalent en son droit : qu'elle se fasse entendre elle-même, seulement. En cela, parole de l'auteur : « La récitation qu'on fait en secret dans toute la prière consiste à mouvoir la langue en articulant le Coran… jusqu'à : la femme est en deçà de l'homme quant à la voix haute. »</p>
<h3>Troisièmement : les surérogations — leur temps, leurs espèces et la modalité de leur récitation</h3>
<h4>a. Le temps des surérogations et leurs espèces</h4>
<p>Les surérogations (<em>nawāfil</em>) sont ce qui s'ajoute à l'obligatoire ; elles diffèrent, selon le moment où on les prie, en nom et en modalité de récitation. Ainsi :</p>
<ul>
<li>les <em>rawātib</em> (prières régulières) demandées avant ou après la prière, par recommandation : après le ẓuhr, quatre rakʿa en saluant à chaque deux, en vertu de sa parole — paix et bénédiction sur lui — : « Quiconque préserve quatre rakʿa avant le ẓuhr et quatre après, Dieu lui interdit le Feu. » [Sunan at-Tirmidhī, « chapitre de ce qui est rapporté des deux rakʿa après le ẓuhr »] ; avant l'ʿaṣr, quatre rakʿa, pour ce qui est parvenu : « Que Dieu fasse miséricorde à l'homme qui prie quatre [rakʿa] avant l'ʿaṣr. » [Sunan d'Abū Dāwūd, « chapitre de la prière avant l'ʿaṣr »] ; et après le maghrib, deux rakʿa une fois achevée l'évocation qui fait suite [à la prière] ;</li>
<li>le shafʿ et le witr, après la prière de l'ʿishāʾ, pour ce qui a été authentifié de sa parole — paix et bénédiction sur lui — : « La prière de la nuit se fait deux par deux ; quand l'un de vous craint l'aube, qu'il prie une rakʿa seule : elle fera le witr de ce qu'il a prié. » [Ṣaḥīḥ d'al-Bukhārī, « chapitre de ce qui est rapporté du witr »]. L'avis prévalent dans l'école est que le witr est une sunna instante, que le shafʿ est une condition de perfection, et qu'il est blâmable de s'en tenir à la seule rakʿa du witr ;</li>
<li>la station de la nuit (<em>qiyām al-layl</em>), recommandée en vertu de sa parole — paix et bénédiction sur lui — : « Attachez-vous à la station de la nuit : elle fut la coutume des vertueux avant vous, un moyen de se rapprocher de votre Seigneur, une expiation des mauvaises actions et un empêchement du péché. » [Sunan at-Tirmidhī, « chapitre de l'invocation du Prophète — paix et bénédiction sur lui »]. Le meilleur de la station est la fin de la nuit : qui diffère sa surérogation et son witr jusqu'à la fin [de la nuit], cela est meilleur ; et celui dont l'habitude est de ne pas s'éveiller, qu'il avance son witr, avec ce qu'il veut de surérogations, au début de la nuit — pour ce qui est parvenu : « Qui craint de ne pas se lever à la fin de la nuit, qu'il fasse le witr en son début ; et qui espère s'en lever, qu'il fasse le witr à la fin de la nuit : la prière de fin de nuit est attestée [des anges], et cela est meilleur. » [Ṣaḥīḥ de Muslim, « chapitre : qui craint de ne pas se lever à la fin de la nuit, qu'il fasse le witr en son début »]. S'il s'éveille à la fin de la nuit, il prie ce qu'il veut et ne refait pas le witr, en vertu de sa parole — paix et bénédiction sur lui — : « Pas deux witr en une même nuit. » [Sunan d'Abū Dāwūd, « chapitre de la rescision du witr »]. Nul ne rattrape le witr qui s'en souvient après avoir prié l'aube. Il est recommandé de réciter, dans le shafʿ, après la Fātiḥa, les sourates al-Aʿlā et al-Kāfirūn, comme il est recommandé, dans la rakʿa du witr, de réciter al-Ikhlāṣ et les deux protectrices, pour ce qui est parvenu de ʿAbd al-ʿAzīz b. Jurayj : « Nous demandâmes à ʿĀʾisha : en quoi le Messager de Dieu — paix et bénédiction sur lui — faisait-il le witr ? Elle dit : il récitait dans la première “Proclame la transcendance du nom de ton Seigneur, le Très-Haut” (al-Aʿlā), dans la seconde “Dis : ô vous les négateurs” (al-Kāfirūn), et dans la troisième “Dis : Il est Dieu, Unique” (al-Ikhlāṣ) et les deux protectrices. » [Sunan at-Tirmidhī, « chapitre de ce qui est rapporté de ce qu'on récite dans le witr »]. En cela, parole de l'auteur : « Puis il accomplit le shafʿ et le witr à voix haute… jusqu'à : nul ne rattrape le witr qui s'en souvient après avoir prié l'aube. »</li>
<li>la salutation de la mosquée (<em>taḥiyyat al-masjid</em>), pour qui entre à la mosquée en état de pureté : il ne s'assoit pas avant d'y prier deux rakʿa — sauf si le temps est un temps d'interdit, tel le lever du soleil, son coucher, la khutba du vendredi, après la prière de l'ʿaṣr et après le lever de l'aube. La source en est sa parole — paix et bénédiction sur lui — : « Quand l'un de vous entre à la mosquée, qu'il s'incline en deux rakʿa avant de s'asseoir. » [Ṣaḥīḥ d'al-Bukhārī, « chapitre : quand l'un de vous entre à la mosquée, qu'il s'incline en deux rakʿa »]. En cela, parole de l'auteur : « Quiconque entre à la mosquée en état de pureté ne s'assoit pas… jusqu'à : hormis les deux rakʿa de l'aube, jusqu'au lever du soleil. »</li>
<li>la faveur de l'aube (<em>raghībat al-fajr</em>), que l'on prie avant la prière du ṣubḥ, après l'adhān : elle n'est pas valable avant. Ibn al-Qāsim a rapporté de Mālik qu'on y récite Umm al-Qurʾān et une sourate, pour ce qui a été rapporté : « le Prophète — paix et bénédiction sur lui — récita, dans les deux rakʿa de l'aube, [sourates reproduites en image dans le manuel : « Dis : ô vous les négateurs » — al-Kāfirūn (109) — et « Dis : Il est Dieu, Unique » — al-Ikhlāṣ (112)] » [Sunan d'Abū Dāwūd, « chapitre des deux rakʿa de l'aube — chapitre de leur abrègement »]. Il est meilleur de les prier à la mosquée ; quiconque trouve l'imām dans l'obligatoire entre avec lui, puis les prie après le lever du soleil. Quiconque entre à la mosquée sans avoir prié l'aube : les deux rakʿa de l'aube lui suffisent pour la salutation de la mosquée. Quiconque prie l'aube en sa demeure puis vient à la mosquée et trouve la prière non encore dressée — il a été dit : il prie la salutation de la mosquée ; il a été dit : il s'assoit sans incliner : deux narrations prévalentes.</li>
</ul>
<h4>b. La modalité de la récitation</h4>
<p>La modalité de la récitation dans les surérogations de la nuit : la voix haute, par recommandation ; dans celles du jour : le secret, par recommandation. Qui récite à voix haute de jour, ou en secret de nuit, cela est permis. En cela, parole de l'auteur : « De même, il est recommandé, dans les surérogations de la nuit… jusqu'à : dans sa surérogation, c'est là une latitude. »</p>
<p>Parmi les visées de cette leçon : orienter le croyant vers le soin d'avoir une part des surérogations des prières — en accroissement de la purification de l'âme, en multiplication de la récompense, en gratitude au Créateur pour Ses bienfaits, et pour ce qui peut survenir de défaillance dans les obligations : elle est réparée par les surérogations, par la miséricorde de Dieu et Sa faveur.</p>
<h2>L'évaluation</h2>
<ul>
<li>Expose la règle de qui a oublié le witr jusqu'à avoir prié l'aube.</li>
<li>Donne la définition du moindre secret et de la moindre voix haute dans la récitation de la prière.</li>
<li>Mets en relief la modalité de la récitation dans la prière surérogatoire, de nuit ou de jour.</li>
</ul>
<h2>L'enrichissement</h2>
<p>Le cheikh Zarrūq — que Dieu lui fasse miséricorde — a dit :</p>
<p>« Abū Bakr — que Dieu l'agrée — avançait son witr au début de la nuit, hâtif vers l'adoration et avisé par le soin de sa famille ; le Prophète — paix et bénédiction sur lui — lui dit : “Tu as pris le parti de la ferme résolution (<em>al-ʿazm</em>).” ʿUmar — que Dieu l'agrée — le différait, confiant en la sunna de Dieu pour l'éveiller, et agissant selon son habitude avec Dieu Très-Haut ; le Prophète — paix et bénédiction sur lui — lui dit : “Tu as pris le parti de la sage prévoyance (<em>al-ḥazm</em>)” — le hadith. »</p>
<p>(<em>Sharḥ</em> de Zarrūq sur la <em>Risāla</em>, t. I, p. 273. — N.d.T. : les versions canoniques du hadith [Abū Dāwūd, n° 1434 ; Ibn Khuzayma, n° 1085 ; Ibn Ḥibbān, n° 2446] attribuent à Abū Bakr “la sage prévoyance” et à ʿUmar “la force”.)</p>
<p>Réfléchis à ces paroles et expose ce que tu en as retiré.</p>
<h2>La préparation préalable</h2>
<p>Lis le matn de la prochaine leçon et accomplis ce qui suit :</p>
<ul>
<li>Expose la règle de l'imāmat de la femme.</li>
<li>Mets en relief la condition d'atteinte de la prière en commun.</li>
<li>Où se tient le suivi (<em>maʾmūm</em>) — seul ou à plusieurs — auprès de l'imām ?</li>
</ul>
"""

# Typographie française : espaces fines insécables (U+202F) dans les guillemets
# et avant : ; ? ! — convention du corpus (leçons récentes).
html_fr = html_fr.replace('« ', '«\u202f').replace(' »', '\u202f»')
html_fr = re.sub(r' ([;?!])', '\u202f\\1', html_fr)
html_fr = html_fr.replace(' :', '\u202f:')
html_fr = html_fr.strip()

book = json.load(open(BOOK))
found = False
for d in book['lessons']:
    if d['docId'] == DOC:
        d['htmlFr'] = html_fr
        found = True
        print(f"OK: {DOC} -> htmlFr ({len(html_fr)} car), titleFr conservé : {d.get('titleFr','')[:60]}")
if not found:
    sys.exit(f"ERREUR: {DOC} introuvable dans {BOOK}")

# Fix 11437 : coquille « les pures ommages] à Dieu » -> « les pures à Dieu » (الزاكيات لله)
fixed37 = 0
for d in book['lessons']:
    if d['docId'] == '11437':
        old = d['htmlFr']
        new = old.replace('les pures ommages] à Dieu', 'les pures à Dieu')
        if new != old:
            d['htmlFr'] = new
            fixed37 = 1
            print("OK: 11437 coquille « ommages] » corrigée")
        else:
            print("ATTENTION: coquille 11437 non trouvée — vérifier manuellement")
json.dump(book, open(BOOK, 'w'), ensure_ascii=False, indent=2)
print(f"{BOOK} réécrit.")

# Registre savant : ajout de 11438 à hand[]
REG = 'scripts-translate/savant-registry.json'
reg = json.load(open(REG))
if DOC not in reg['hand']:
    reg['hand'].append(DOC)
    json.dump(reg, open(REG, 'w'), ensure_ascii=False, indent=2)
    print(f"Registre: {DOC} ajouté à hand ({len(reg['hand'])} entrées)")
else:
    print(f"Registre: {DOC} déjà présent")

# Contrôle qualité immédiat : aucun caractère arabe ne doit rester dans la traduction
arabic = re.findall(r'[\u0600-\u06FF]+', html_fr)
print('Caractères arabes résiduels:', len(arabic), arabic[:5] if arabic else '')
print('Guillemets « :', html_fr.count('«'), '| » :', html_fr.count('»'))
