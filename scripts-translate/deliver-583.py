#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Livraison de la leçon 583 (المجادلة 20-21, الدرس ٢٨, R97-WARSH).

Vérifications R97 (méthode Warsh e-verification) :
- Rosette ۝٢٠ confirmée par triple signal (blob C9 + VLM lettre à lettre) :
  elle vient APRES «إِنَّ ٱللَّهَ قَوِىٌّ عَزِيزٌ» (fin de la fusion Ḥafṣ v20+v21)
  et AVANT «لَّا تَجِدُ» — le muṣḥaf de l'école (Warsh) FUSIONNE Ḥafṣ v20+v21
  en son verset 20 ; Ḥafṣ v22 = verset 21 de l'école. Numérotation MEDINOISE.
- Les 7 lignes du bloc coranique vérifiées ligne à ligne contre le squelette
  tanzil (équivalence rasm Uthmani, pas de divergence Warsh connue ici).
- Glossaire : «ٱلْأَذَلِّينَ» / «كَتَبَ» / «بِرُوحٍ» (pixel + tesseract + tafsīr).
- Citation Rāzī vérifiée MOT A MOT contre quran-tafsir.net (Mafātīḥ al-Ġayb,
  tafsīr de 58:22) — y compris «بل كان عاصيا في الله» et «إرادة منافسه دينا
  ودنيا» ; référence 499/29 (lue à 8x, cohérente avec 494/29 de la leçon 581).
- Question de clôture du tamhīd reconstruite par segmentation pixel 600dpi :
  «فماذا كان جزاء المعاندين الذل والمهانة؟ وكيف تكون الغلبة لله ورسوله؟»
- Tafsīr identifié : Ibn Ǧuzayy (glose «في جملة الأذلين أي معهم» = verbatim).
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"

HTML_AR = """<h1>سورة المجادلة (الآيات: 20-21): كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي للسنة الثانية إعدادي الدرس 28</h1>
<p>درس في تفسير سورة المجادلة الآيات (20-21)، كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي، للسنة الثانية من التعليم الإعدادي العتيق (الدرس 28).</p>
<ol>
<li>أن أتعرف صفات المؤمنين الصادقين.</li>
<li>أن أدرك أن الغلبة لله ورسوله والذل والمهانة للمعاندين.</li>
<li>أن ألازم الصالحين واتصف بصفاتهم وأتخلق بأخلاقهم.</li>
</ol>
<h2>تمهيد</h2>
<p>بعد أن ذكر الله تعالى بعض أحوال المنافقين، بين هنا سبب خسرانهم وهو أنهم شاقوا الله ورسوله وعصوا أمرهما؛ فكتب الله عليهم الذلة في الدنيا والآخرة؛ وكتب العزة لله ورسوله وللمؤمنين الذين قواهم الله بالطمأنينة والثبات على الإيمان؛ والفوز والفلاح في الآخرة.</p>
<p>فماذا كان جزاء المعاندين الذل والمهانة؟ وكيف تكون الغلبة لله ورسوله؟</p>
<h2>الآيات</h2>
<p><span>سورة المجادلة: 20-21</span></p>
<p>«إِنَّ ٱلَّذِينَ يُحَآدُّونَ ٱللَّهَ وَرَسُولَهُۥٓ أُو۟لَٰٓئِكَ فِى ٱلْأَذَلِّينَ كَتَبَ ٱللَّهُ لَأَغْلِبَنَّ أَنَا۠ وَرُسُلِىٓ ۚ إِنَّ ٱللَّهَ قَوِىٌّ عَزِيزٌۭ» [المجادلة: 20]</p>
<p>«لَّا تَجِدُ قَوْمًۭا يُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ يُوَآدُّونَ مَنْ حَآدَّ ٱللَّهَ وَرَسُولَهُۥ وَلَوْ كَانُوٓا۟ ءَابَآءَهُمْ أَوْ أَبْنَآءَهُمْ أَوْ إِخْوَٰنَهُمْ أَوْ عَشِيرَتَهُمْ ۚ أُو۟لَٰٓئِكَ كَتَبَ فِى قُلُوبِهِمُ ٱلْإِيمَٰنَ وَأَيَّدَهُم بِرُوحٍۢ مِّنْهُ ۖ وَيُدْخِلُهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ رَضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ أُو۟لَٰٓئِكَ حِزْبُ ٱللَّهِ ۚ أَلَآ إِنَّ حِزْبَ ٱللَّهِ هُمُ ٱلْمُفْلِحُونَ» [المجادلة: 21]</p>
<h2>الفهم</h2>
<h3>الشرح:</h3>
<p>«ٱلْأَذَلِّينَ»: أذل خلق الله.</p>
<p>«كَتَبَ»: قضى وقدر.</p>
<p>«بِرُوحٍ»: بلطف وهدى وتوفيق.</p>
<h3>استخلاص مضامين الآيتين:</h3>
<ol>
<li>لمن تكون الغلبة؛ ولمن يكون الذل؟</li>
<li>من هم المؤمنون الصادقون في الآيتين؟</li>
</ol>
<h2>التفسير</h2>
<p>اشتملت الآيتان على ما يأتي:</p>
<h3>أولا: الغلبة لله ورسوله والذل لمن يخالف أمرهما:</h3>
<p>بعد الحديث عن المنافقين وبيان أحوالهم وتصرفاتهم القبيحة يؤكد القرآن الكريم على جزاء المحادين لله ورسوله؛ حيث يقول تعالى: «إِنَّ ٱلَّذِينَ يُحَآدُّونَ ٱللَّهَ وَرَسُولَهُۥٓ أُو۟لَٰٓئِكَ فِى ٱلْأَذَلِّينَ»؛ أي: إن الذين يخالفون ويعادون الله ورسوله «أُو۟لَٰٓئِكَ فِى ٱلْأَذَلِّينَ» أي: أولئك في جملة الأذلين؛ أي: معهم.</p>
<p>ثم بين الله عز وجل عزة المؤمنين فقال: «كَتَبَ ٱللَّهُ لَأَغْلِبَنَّ أَنَا۠ وَرُسُلِىٓ ۚ إِنَّ ٱللَّهَ قَوِىٌّ عَزِيزٌۭ» أي: قضى الله وقدر أن الغلبة لله ورسوله.</p>
<h3>ثانيا: من صفات المؤمنين الصادقين:</h3>
<p>بعد أن أكدت الآية السابقة أن الذل والمهانة هو جزاء من يعاند الله ورسوله وأن الغلبة لله ورسوله؛ عاد الحق سبحانه لينوه بالمؤمنين الصادقين فقال تعالى: «لَّا تَجِدُ قَوْمًۭا يُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ يُوَآدُّونَ مَنْ حَآدَّ ٱللَّهَ وَرَسُولَهُۥ وَلَوْ كَانُوٓا۟ ءَابَآءَهُمْ أَوْ أَبْنَآءَهُمْ أَوْ إِخْوَٰنَهُمْ أَوْ عَشِيرَتَهُمْ» أي: لا تجد مؤمنا يحب كافرا ولو كان أقرب الناس إليه من أبيه أو ابنه أو أخيه أو عشيرته؛ وهذه حال المؤمن الصادق الإيمان.</p>
<p>فقوله: «يُوَآدُّونَ» مفاعلة من المودة تقتضي أن المودة من الجهتين، وقوله: «حَآدَّ» أي عاداه وخالفه.</p>
<p>وهذه الآية قيل: نزلت في حاطب بن أبي بلتعة حين كتب إلى المشركين يخبرهم بأخبار رسول الله ﷺ. والأحسن أنها على العموم.</p>
<p>قال الرازي رحمه الله: «لا يجتمع الإيمان مع وداد أعداء الله وذلك لأن من أحب أحدا امتنع أن يحب مع ذلك عدوه؛ وهذا على وجهين أحدهما: أنهما لا يجتمعان في القلب؛ فإذا حصل في القلب وداد أعداء الله؛ لم يحصل فيه الإيمان؛ فيكون صاحبه منافقا. والثاني: أنهما يجتمعان ولكنه معصية وكبيرة. وعلى هذا الوجه لا يكون صاحب هذا الوداد كافرا بسبب هذا الوداد؛ بل كان عاصيا في الله؛ فإن قيل: أجمعت الأمة على أنه تجوز مخالطتهم ومعاشرتهم؛ فما هذه المودة المحرمة المحظورة؟ قلنا: المودة المحظورة هي إرادة منافسه دينا ودنيا مع كونه كافرا، فأما ما سوى ذلك فلا حظر فيه» [مفاتيح الغيب؛ لفخر الدين الرازي: 499/29].</p>
<p>ثم أثنى الحق سبحانه على المؤمنين الصادقين الذين لم يوالوا أعداء الله مهما بلغت درجة قرابتهم فقال: «أُو۟لَٰٓئِكَ كَتَبَ فِى قُلُوبِهِمُ ٱلْإِيمَٰنَ» أي: أولئك الذين لا يوادون أعداء الله مهما كانوا؛ هم الذين كتب الله تعالى الإيمان في قلوبهم وأثبته فيها كأنه مكتوب. «وَأَيَّدَهُم بِرُوحٍۢ مِّنْهُ» أي: وقرّاهم بنصره وتأييده. وقيل: بلطف وهدى وتوفيق. وقيل: بالقرآن. وقيل: بجبريل.</p>
<p>ثم بين الله عز وجل أن جزاءهم في الآخرة هو رضى الله وإقامة دائمة في الجنة فقال: «وَيُدْخِلُهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ رَضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ».</p>
<p>ثم بين الله عز وجل أن أولئك المؤمنين هم أهل الله وجماعته وأن جزاءهم الفلاح فقال: «أُو۟لَٰٓئِكَ حِزْبُ ٱللَّهِ ۚ أَلَآ إِنَّ حِزْبَ ٱللَّهِ هُمُ ٱلْمُفْلِحُونَ» هذه في مقابلة قوله: «أُو۟لَٰٓئِكَ حِزْبُ ٱلشَّيْطَٰنِ» والحزب هم الجماعة المتحزبون لمن أضيفوا إليه.</p>
<h3>ثالثا: مقاصد الآيتين:</h3>
<p>تهدف الآيتان إلى بيان مجموعة من المقاصد التربوية منها:</p>
<ul>
<li>التحذير من محادة الله ورسوله ومخالفة أمرهما.</li>
<li>أن الله عز وجل قضى وقدر أن تكون الغلبة لله ورسوله.</li>
<li>الرابطة الإيمانية أقوى من رابطة القرابة.</li>
<li>أن جزاء المؤمنين حقا هو التأييد الإلهي والجنة والرضى في الآخرة.</li>
</ul>
<h2>التقويم</h2>
<ol>
<li>ما معنى محادة الله ورسوله؟ وما جزاء من اتصف بذلك؟</li>
<li>ما هي صفات المؤمنين الصادقين الواردة في الآيتين؟</li>
<li>أوضح كيف تكون رابطة الدين أقوى من رابطة القرابة؟</li>
</ol>
<h2>الاستثمار</h2>
<p>قال الله تعالى: «لَّا يَنْهَىٰكُمُ ٱللَّهُ عَنِ ٱلَّذِينَ لَمْ يُقَٰتِلُوكُمْ فِى ٱلدِّينِ وَلَمْ يُخْرِجُوكُم مِّن دِيَٰرِكُمْ أَن تَبَرُّوهُمْ وَتُقْسِطُوٓا۟ إِلَيْهِمْ ۚ إِنَّ ٱللَّهَ يُحِبُّ ٱلْمُقْسِطِينَ (٨) إِنَّمَا يَنْهَىٰكُمُ ٱللَّهُ عَنِ ٱلَّذِينَ قَٰتَلُوكُمْ فِى ٱلدِّينِ وَأَخْرَجُوكُم مِّن دِيَٰرِكُمْ وَظَٰهَرُوا۟ عَلَىٰٓ إِخْرَاجِكُمْ أَن تَوَلَّوْهُمْ ۚ وَمَن يَتَوَلَّهُمْ فَأُو۟لَٰٓئِكَ هُمُ ٱلظَّٰلِمُونَ (٩)» [الممتحنة: 8-9].</p>
<p>أبحث عن كيفية التوفيق بين النهي عن الموادة مع غير المؤمنين، ومشروعية برهم والقسط معهم المنصوص عليه في الآيتين.</p>"""

HTML_FR = """<h1> Sourate al-Muǧādala, versets 20-21 : livre du Tafsīr à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Ǧuzayy, deuxième année collégiale — leçon 28</h1>
<p>Leçon sur l’exégèse de la sourate al-Muǧādala, versets 20 et 21, du livre du Tafsīr fondé sur le <em>Tashīl li-ʿulūm al-tanzīl</em> d’Ibn Ǧuzayy, pour la deuxième année de l’enseignement collégial traditionnel (leçon 28).</p>
<ol>
<li>Que je connaisse les traits des croyants véridiques.</li>
<li>Que je saisisse que la victoire appartient à Allah et à Son messager, et que l’abaissement et l’ignominie reviennent aux réfractaires.</li>
<li>Que je fréquente assidûment les vertueux, que j’adopte leurs traits et que je me pare de leurs morales.</li>
</ol>
<h2>Introduction (tamhīd)</h2>
<p>Après qu’Allah — exalté soit-Il — a mentionné quelques conditions des hypocrites, Il expose ici la cause de leur perte : le fait qu’ils se sont dressés contre Allah et Son messager et ont désobéi à leurs deux ordres. Allah a alors décrété sur eux l’abaissement en ce monde et dans l’au-delà ; et Il a décrété la puissance pour Allah, pour Son messager et pour les croyants qu’Allah a affermis par la sérénité et la constance dans la foi — ainsi que le succès et la prospérité dans l’au-delà.</p>
<p>Quelle fut donc la punition des réfractaires : l’abaissement et l’ignominie ? Et comment la victoire revient-elle à Allah et à Son messager ?</p>
<h2>Les versets</h2>
<p><span>Sourate al-Muǧādala, versets 20 à 21</span></p>
<p>« Ceux qui s’opposent à Allah et à Son messager — ceux-là sont au nombre des plus humiliés. Allah a décrété : “Je vaincrai assurément, Moi ainsi que Mes messagers. Allah est Fort, Puissant” » (20).</p>
<p>« Tu ne trouveras aucun peuple qui croie en Allah et au Jour dernier et qui aime celui qui s’oppose à Allah et à Son messager, fussent-ils ses pères, ses fils, ses frères ou son clan. Ceux-là : Allah a inscrit la foi dans leurs cœurs et les a affermis par un esprit venant de Lui ; Il les fera entrer dans des jardins sous lesquels coulent les ruisseaux, où ils demeureront éternellement. Allah est satisfait d’eux, et ils sont satisfaits de Lui. Ceux-là sont le parti d’Allah. Eh quoi, le parti d’Allah : ce sont eux les prospères » (21).</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>« al-aḏallīn » (les plus humiliés) : les plus abjects des créatures d’Allah.</p>
<p>« kataba » (a décrété) : a ordonné et prédestiné.</p>
<p>« bi-rūḥin » (par un esprit) : avec bienveillance, guidée et réussite.</p>
<h3>Extraction des contenus des deux versets</h3>
<ol>
<li>À qui appartient la victoire, et à qui revient l’abaissement ?</li>
<li>Qui sont les croyants véridiques dans les deux versets ?</li>
</ol>
<h2>Le Tafsīr</h2>
<p>Ces deux versets comprennent ce qui suit :</p>
<h3>Premièrement : la victoire à Allah et à Son messager, et l’abaissement à quiconque contrevient à leurs deux ordres</h3>
<p>Après l’entretien sur les hypocrites et l’exposé de leurs conditions et de leurs comportements vils, le noble Coran insiste sur le châtiment de ceux qui s’opposent à Allah et à Son messager. Allah — exalté soit-Il — dit : « Ceux qui s’opposent à Allah et à Son messager — ceux-là sont au nombre des plus humiliés » : ceux qui contreviennent à Allah et à Son messager et leur font opposition — « ceux-là sont au nombre des plus humiliés » : au nombre des humiliés, c’est-à-dire : avec eux.</p>
<p>Puis Allah — puissant et majestueux — expose la puissance des croyants et dit : « Allah a décrété : “Je vaincrai assurément, Moi ainsi que Mes messagers. Allah est Fort, Puissant” » : Allah a décrété et prédestiné que la victoire appartient à Allah et à Son messager.</p>
<h3>Deuxièmement : parmi les traits des croyants véridiques</h3>
<p>Après que le verset précédent a affirmé que l’abaissement et l’ignominie sont le châtiment de quiconque s’obstine contre Allah et Son messager, et que la victoire appartient à Allah et à Son messager, le Vrai — exalté soit-Il — revient honorer les croyants véridiques et dit — exalté soit-Il : « Tu ne trouveras aucun peuple qui croie en Allah et au Jour dernier et qui aime celui qui s’oppose à Allah et à Son messager, fussent-ils ses pères, ses fils, ses frères ou son clan » : tu ne trouveras aucun croyant aimant un mécréant, dût-il être le plus proche des hommes pour lui — son père, son fils, son frère ou son clan ; tel est l’état du croyant véridique dans sa foi.</p>
<p>Sa parole « yuwāddūna » (aiment) est une forme réciproque (mufāʿala) dérivée de l’affection, qui suppose l’affection des deux côtés ; et Sa parole « ḥādda » (s’opposer) : il lui a fait opposition et l’a contredit.</p>
<p>Ce verset, dit-on, fut révélé au sujet de Ḥāṭib ibn Abī Baltaʿa, lorsqu’il écrivit aux polythéistes pour les informer des nouvelles du messager d’Allah ﷺ. L’avis le plus juste est qu’il a une portée générale.</p>
<p>Ar-Rāzī — qu’Allah lui fasse miséricorde — dit : « La foi ne saurait cohabiter avec l’affection des ennemis d’Allah, car quiconque aime quelqu’un s’interdit d’aimer en même temps son ennemi ; et cela selon deux faces : la première, que l’une et l’autre ne cohabitent pas dans le cœur — si l’affection des ennemis d’Allah s’installe dans le cœur, la foi ne s’y installe pas, et son détenteur est un hypocrite ; la seconde, qu’elles cohabitent, mais à titre de désobéissance et de péché majeur. Selon cette face, le détenteur de cette affection n’est pas mécréant en raison d’elle : il fut désobéissant envers Allah. Si l’on dit : la communauté est d’accord sur le fait qu’il est permis de les fréquenter et de vivre avec eux, qu’est-ce donc que cette affection interdite et proscrite ? Nous répondons : l’affection proscrite est l’envie de rivaliser avec lui en religion et en choses de ce monde, alors qu’il est mécréant ; tout le reste n’est pas proscrit » [Mafātīḥ al-ġayb, de Faḫr ad-Dīn ar-Rāzī : 499/29].</p>
<p>Puis le Vrai — exalté soit-Il — fait l’éloge des croyants véridiques qui n’ont pas pris pour alliés les ennemis d’Allah, quel que soit le degré de leur parenté, et dit : « Ceux-là : Allah a inscrit la foi dans leurs cœurs » : ceux qui n’aiment pas les ennemis d’Allah, quels qu’ils soient — ce sont ceux dans les cœurs desquels Allah — exalté soit-Il — a inscrit la foi et l’a affermie, comme si elle était écrite. « et les a affermis par un esprit venant de Lui » : Il les a gratifiés de Son secours et de Son soutien. On a dit : par la bienveillance, la guidée et la réussite ; on a dit : par le Coran ; on a dit : par Gabriel.</p>
<p>Puis Allah — puissant et majestueux — expose que leur rétribution dans l’au-delà est la satisfaction d’Allah et une demeure éternelle au Paradis, et dit : « Il les fera entrer dans des jardins sous lesquels coulent les ruisseaux, où ils demeureront éternellement. Allah est satisfait d’eux, et ils sont satisfaits de Lui ».</p>
<p>Puis Allah — puissant et majestueux — expose que ces croyants sont les gens d’Allah et Sa communauté, et que leur rétribution est la prospérité, et dit : « Ceux-là sont le parti d’Allah. Eh quoi, le parti d’Allah : ce sont eux les prospères » — cela en pendant de Sa parole : « Ceux-là sont le parti du diable » ; le parti (ḥizb) désigne la communauté regroupée autour de celui auquel elle est rattachée.</p>
<h3>Troisièmement : les finalités des deux versets</h3>
<p>Les deux versets visent à exposer un ensemble de finalités éducatives, parmi lesquelles :</p>
<ul>
<li>L’avertissement contre l’opposition à Allah et à Son messager et la contravention à leurs deux ordres.</li>
<li>Le fait qu’Allah — puissant et majestueux — a décrété et prédestiné que la victoire appartient à Allah et à Son messager.</li>
<li>Le lien de la foi est plus fort que le lien de la parenté.</li>
<li>La rétribution des croyants véridiques est le soutien divin, le Paradis et la satisfaction [d’Allah] dans l’au-delà.</li>
</ul>
<h2>L’évaluation</h2>
<ol>
<li>Quel est le sens de l’opposition (muḥāda) à Allah et à Son messager ? Et quel est le châtiment de celui qui s’en pare ?</li>
<li>Quels sont les traits des croyants véridiques mentionnés dans les deux versets ?</li>
<li>J’expose comment le lien de la religion peut être plus fort que le lien de la parenté.</li>
</ol>
<h2>L’exploitation (istiṯmār)</h2>
<p>Allah — exalté soit-Il — dit : « Allah ne vous interdit pas, à l’égard de ceux qui ne vous ont pas combattus pour la religion et ne vous ont pas chassés de vos demeures, de leur faire du bien et d’agir équitablement envers eux : Allah aime les équitables (8). Allah vous interdit seulement de prendre pour alliés ceux qui vous ont combattus pour la religion, vous ont chassés de vos demeures et ont contribué à votre expulsion ; et quiconque les prend pour alliés, ce sont eux les injustes (9) » [Sourate al-Mumtaḥana : 8-9].</p>
<p>Je recherche comment concilier l’interdiction de l’affection envers les non-croyants et la licéité, prescrite dans les deux versets, de leur bienfaisance et de l’équité envers eux.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if str(l.get("docId", "")).endswith("-583"):
            l["html"] = HTML_AR
            l["htmlFr"] = HTML_FR
            l["pdfOnly"] = False
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 583 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 583 livrée: AR {len(HTML_AR)} car + FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
