#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Livraison de la leçon 561 (سورة فاطر 15-18, الدرس 6, R102-WARSH).

Vérifications R102 (méthode Warsh e-verification + croisement CMS 16839 + GT) :
- BLOC v15-18 : squelette tanzil Warsh du quran-cache s35 (Fāṭir = 45 versets
  dans les deux comptages — confirmé R99→R101 pour v4-14, étendu v15-18).
  Mot-à-mot vérifié contre l'imprimé (probes tesseract 900-2400 dpi p1-p2 :
  يٰٓأيها الناس أنتم الفقراء إلى الله ۖ والله هو الغني الحميد / إن يشأ يذهبكم
  ويأت بخلق جديد / وما ذلك على الله بعزيز / ولا تزر وازرة وزر أخرى... إلى
  المصير). ۞ conservé (précédents 568/582).
- GLOSSAIRE 5 entrées (règle d'or 7/7 : idad 560 = الشرح 561) :
  «ٱلْفُقَرَآءُ إِلَىٰ ٱللَّهِ»=المحتاجون إليه في كل حال (le terme imprimé porte
  «إِلَىٰ ٱللَّهِ» — garble «الْجغْراءٌ إل وآللة» p2) / «ٱلْغَنِيُّ ٱلْحَمِيدُ»=الغني عن
  سائر خلقه، المحمود بأفعاله وأقواله وحسن تدبيره / «مُثْقَلَةٌ»=أي مثقلة بأوزارها
  حتى لم تقدر على المشي أو الحركة / «وَإِن تَدْعُ مُثْقَلَةٌ»=لا تجد من يستجيب لها
  ويحمل عنها بعض ذنبها (terme élargi au fragment verbal — VLM glyphique
  و+إن+تدع+مثقلة + largeur d'encre 981 px ≈ 11 glyphes + idad 560 «تَدْعُ»
  contenu) / «تَزَكَّىٰ»=طهر نفسه من الشرك والمعاصي.
- CITATIONS inter-sourates : [الأنعام: 166] contenu = Ḥafṣ 164 «وَلَا تَكْسِبُ
  كُلُّ نَفْسٍ إِلَّا عَلَيْهَا» (strips tesseract ×3 : وَلَا تَكْسِبُ كُلُّ نَفْسٍ إِلَّا
  عَلَيْهَا — la citation S'ARRÊTE à عليها, garble «إل عَلَيمًا» terminal ;
  numérotation médinoise transcrite telle qu'imprimée, directive R96) ;
  [المدثر: 38] = «كُلُّ نَفْسٍۢ بِمَا كَسَبَتْ رَهِينَةٌ» (garble «كتج رِمَاكَمثرَهيتةُ») ;
  [الإسراء: 15] = «وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ» (L13 p4 : «و ترز وازرة
  وزراتضى» + span CMS) ; [عبس: 34-35] = «يَوْمَ يَفِرُّ ٱلْمَرْءُ مِنْ أَخِيهِ ۝
  وَأُمِّهِۦ وَأَبِيهِ» (garble p6 «بكوم مز ماحد واف وَأيمة4» = يوم يفر المرء من
  أخيه وأمه وأبيه — croisé cache s80).
- TAG ÉGARÉ p6 : l'imprimé répète [عبس: 34-35] APRÈS «وَلَوْ كَانَ ذَا قُرْبَىٰ»
  (fragment de Fāṭir 18) — comparaison pixel des deux tags (encre 8311=8311,
  corr 0.959, 5 composants) = même mot typeset ; tag errant de composition,
  NON reproduit (structure Ibn ʿĀšūr + src.html 16839 = autorité, tag gardé
  à sa place légitime après «يَوْمَ يَفِرُّ...»).
- RÉFÉRENCES pixel-vérifiées : [التسهيل: 1/283 و 443] (strip p4 : «/283 و
  443») ; [التسهيل: 1/70] (CMS «07» = transposition ; imprimé ١/٧٠ double
  sonde tesseract+VLM) ; [التحرير والتنوير؛ لابن عاشور: 22/292] et [؛ للطاهر
  بن عاشور: 22/290 (بتصرف)] (ordre physique des groupes de chiffres : ٢٩٢
  à gauche de ٢٢ → logique vol/page).
- SLOTS grammaticaux p3 : «أَنتُمُ ٱلْفُقَرَآءُ» (L6 : قصر صفة على موصوف) ;
  «وفي إتباع صفة «ٱلْفَقْرِ» بـ«ٱلْحَمِيدِ»» (L8 TSV : slot1 695 px ≈ 5
  glyphes = الفقر [garbles لبر/لْبثرٌ ×3], slot2 819 px = الحميد [garbles
  أتْمِيذ/الْحمِيةٌ/الْحميةٌ]) ; «وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ» (L5) ; mafʿūl elided
  «يَشَأْ»→جواب «يُذْهِبْكُمْ» + «وَإِن تَدْعُ» (p3/p4 probes).
- IDAD 561 (pour 562, فاطر 19-26) VÉROUILLÉ ce tour : 4 termes «الْحَرُورُ» -
  «أُمَّةٍ» - «نَذِيرٌ» - «وَبِالزُّبُرِ» (règle d'or 7/7 : = le الشرح de 562 lu
  dans le CMS 16839 frais — 4 defs : شدة الحر بالنهار والليل / جماعة يجمعهم
  نسب واحد / منذر تخوف الناس من عذاب الله / الكتب المكتوبة كصحف إبراهيم
  وموسى ; garbles p7 : «قروز»=الحرور [ح→ق ر↔ر ز↔ر], «أمّةٍ» lu direct,
  «تويز/دوِيرٌ»=نذير, «وَبالزيْر/وَبِالزَّجْرِ»=وبالزبر [ج↔ب même point
  sous-basilaire] ; 3 tirets détectés par projection d'encre).
- SANITIZE : artefact CMS 16839 de l'iʿdād («أتأمل الآيية بين العباد يوم
  القيامة من خلال هذه الآيات.» = collant de l'idad 560) écarté ; «لله» des
  citations rendu au rasm Warsh du cache (ٱللَّهِ).
- Injection : AR ~9700 + FR ~13800 car. Registre hand +1 (480 main).
"""

import json
import sys

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"
TMP = "/home/z/my-project/tr-tmp/pdf-mut23h33-561.html"

HTML_AR = """<h1>سورة فاطر (الآيات: 15-18): كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي للسنة الثانية إعدادي الدرس 6</h1>
<p>درس في تفسير سورة فاطر الآيات (15-18)، كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي، للسنة الثانية من التعليم الإعدادي العتيق (الدرس 6).</p>
<ol>
<li>أن أتعرف مظاهر غنى الله تعالى وعدله المطلق بين عباده.</li>
<li>أن أستنتج أسباب الانتفاع برسالة النبي صلى الله عليه وسلم.</li>
<li>أن أستجيب لدعوة النبي صلى الله عليه وسلم لأحظى بصفات المؤمنين.</li>
</ol>
<h2>تمهيد</h2>
<p>لما توهم أصحاب الضلال بأنهم مرغوب في انضمامهم إلى المسلمين، وأحدث ذلك فيهم عزة وإعجابا بأنفسهم، ذكَّرهم الله سبحانه بحاجتهم إليه، واستغنائه جل وعلا عن جميع خلقه، مع استحقاق الطائعين لحمده سبحانه وإنعامه، ثم بين سبحانه عدله المطلق بين عباده يوم القيامة، فلا تتحمل النفوس المذنبة إلا مقدار ما ارتكبت من المعاصي، ليقرر في نهاية هذه الآيات أن المؤمنين هم الذين ينتفعون بدعوة الرسول صلى الله عليه وسلم.</p>
<p>فما هي مظاهر عدل الله تعالى بين عباده؟ وكيف أزكي نفسي من خلال هذه الآيات؟</p>
<h2>الآيات</h2>
<p>قال الله تعالى:</p>
<p><span>سورة فاطر: 15 - 18</span></p>
<p>«۞ يَٰٓأَيُّهَا ٱلنَّاسُ أَنتُمُ ٱلْفُقَرَآءُ إِلَىٰ ٱللَّهِ ۖ وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ» [فاطر: 15]</p>
<p>«إِن يَشَأْ يُذْهِبْكُمْ وَيَأْتِ بِخَلْقٍۢ جَدِيدٍۢ» [فاطر: 16]</p>
<p>«وَمَا ذَٰلِكَ عَلَىٰ ٱللَّهِ بِعَزِيزٍۢ» [فاطر: 17]</p>
<p>«وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۚ وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ ۗ إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ ۚ وَإِلَىٰ ٱللَّهِ ٱلْمَصِيرُ» [فاطر: 18]</p>
<h2>الفهم</h2>
<h3>الشرح:</h3>
<p>«ٱلْفُقَرَآءُ إِلَىٰ ٱللَّهِ»: المحتاجون إليه في كل حال.</p>
<p>«ٱلْغَنِيُّ ٱلْحَمِيدُ»: الغني عن سائر خلقه، المحمود بأفعاله وأقواله وحسن تدبيره.</p>
<p>«مُثْقَلَةٌ»: أي مثقلة بأوزارها حتى لم تقدر على المشي أو الحركة.</p>
<p>«وَإِن تَدْعُ مُثْقَلَةٌ»: لا تجد من يستجيب لها ويحمل عنها بعض ذنبها.</p>
<p>«تَزَكَّىٰ»: طهر نفسه من الشرك والمعاصي.</p>
<h3>استخلاص مضامين الآيات:</h3>
<ol>
<li>بم وصف الله تعالى نفسه في بداية الآيات؟</li>
<li>بماذا وعد الله عباده يوم القيامة في هذه الآيات؟</li>
<li>من ينتفع بإنذار الرسول صلى الله عليه وسلم؟</li>
</ol>
<h2>التفسير</h2>
<p>اشتملت هذه الآيات على ما يأتي:</p>
<h3>أولا: غنى الله تعالى عن خلقه غنى مطلقا:</h3>
<p>بعد عرض الأدلة والحجج التي تقرر تفرد الله تعالى بالعبادة، وأنه هو وحده المستحق لها، نادى سبحانه الناس بقوله: «يَٰٓأَيُّهَا ٱلنَّاسُ أَنتُمُ ٱلْفُقَرَآءُ إِلَىٰ ٱللَّهِ» وهو خطاب لجميع الناس، وإنما عرف الفقر بالألف واللام؛ ليدل على اختصاص الفقر بجنس الناس، وإن كان غيرهم فقراء، ولكن فقراء الناس أعظم.</p>
<p>ثم وصف نفسه بأنه الغني في مقابلة وصفهم بالفقر، ووصفه بأنه الحميد ليدل على وجوده وكرمه الذي يوجب أن يحمده عباده. فقال سبحانه: «وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ».</p>
<p>وقوله تعالى: «أَنتُمُ ٱلْفُقَرَآءُ» تفيد قصر صفة على موصوف، أي: قصر صفة الفقر على الناس، والمعنى: أن الناس مفتقرون إلى الله سبحانه، وهو غير مفتقر إليهم. وفي إتباع صفة «ٱلْفَقْرِ» بـ«ٱلْحَمِيدِ» دفع توهم الناس بأنهم غير مطالبين بعبادة الله تعالى بسبب كونه غنيا عنهم، إذ نبههم سبحانه بأنه يحمد من يجيب دعوته ويتوجه إليه بالعبادة.</p>
<p>ثم قرر سبحانه إمكانية استغنائه عن الخلق، بقوله: «إِن يَشَأْ يُذْهِبْكُمْ وَيَأْتِ بِخَلْقٍۢ جَدِيدٍۢ» أي: لو شاء تعالى لأفناكم وأتى بقومٍ آخرين يعبدونه وحده دون سواه.</p>
<p>«وَمَا ذَٰلِكَ عَلَىٰ ٱللَّهِ بِعَزِيزٍۢ» عزيز: ممتنع غالب، أي: لا يتعذر ولا يتعسر على الله سبحانه إهلاككم والإتيان بخلق سواكم، بل هو سهل يسير عليه سبحانه. وقد وقعت هاتان الآيتان موقع البيان لجملة «وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ» وحُذف مفعول «يَشَأْ» لدلالة جواب الشرط عليه، وهو «يُذْهِبْكُمْ» والتقدير: إن يشأ إذهابكم.</p>
<h3>ثانيا: وعد الله تعالى عباده بالعدل بينهم يوم القيامة:</h3>
<p>لما كان مقصد الآيات السابقة، تهديد الناس بالهلاك وتبديلهم بخلق جديد، طمأنهم سبحانه، بأنه سيحكم بينهم يوم القيامة بمنتهى العدل، فقال سبحانه: «وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ». «معنى تَزِرُ: تحمل، ومعنى وِزْرٍ: أي ذنب نفس أخرى. وأصل الوِزْر في اللغة: الثقل والحمل، ويراد به هنا الذنوب، والمعنى: لا يحمل أحد ذنوب أحد» [التسهيل: 1/283 و 443].</p>
<p>وجيء بالوازرة على التأنيث؛ لأن المقصود بها النفس المرتبطة باكتساب الأعمال كما يدل على ذلك قوله تعالى: «وَلَا تَكْسِبُ كُلُّ نَفْسٍ إِلَّا عَلَيْهَا» [الأنعام: 166] وقوله: «كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ رَهِينَةٌ» [المدثر: 38].</p>
<p>ثم بين سبحانه أن عدله هذا مستمر حتى لو استنجدت نفس مثقلة بالذنوب والمعاصي، وطالبت من يتحمل ذلك عنها، لم تجد من يحمل عنها شيئا، قال عز وجل: «وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ» الحمل: عبارة عن الذنوب، والمثقلة: الثقيلة الحمل أو النفس الكثيرة الذنوب، والمعنى: أنها لو دعت أحدا إلى أن يحمل عنها ذنوبها لم يحمل عنها. وحذف مفعول «وَإِن تَدْعُ» لدلالة المعنى وقصد العموم، وهذه الآية بيان وتكميل لمعنى قوله: «وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ» [الإسراء: 15].</p>
<p>وقوله سبحانه: «وَلَوْ كَانَ ذَا قُرْبَىٰٓ» المعنى: ولو كان المدعوّ ذا قرابة ممن دعاه إلى حمل ذنوبه لم يحمل عنه شيئا؛ لأن كل واحد يقول: نفسي نفسي.</p>
<h3>ثالثا: انتفاع المؤمنين بدعوة الرسول صلى الله عليه وسلم:</h3>
<p>بين الله سبحانه لرسوله صلى الله عليه وسلم من ينتفع بدعوته، فقال سبحانه: «إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ» المعنى: أن الإنذار لا ينفع إلا الذين يخشون ربهم، وليس المعنى اختصاصهم بالإنذار. وقوله: «بِٱلْغَيْبِ» في موضع حال من الفاعل في يخشون أي: يخشون ربهم في خلواتهم وهم غائبون عن الناس، فخشيتهم حق لا رياء.</p>
<p>وقوله تعالى: «وَأَقَامُوا۟ ٱلصَّلَوٰةَ» أي: «حافظوا عليها في أوقاتها، بالإخلاص لله في فعلها، وتوفية شروطها وأركانها وفضائلها وسننها وحضور القلب والخشوع فيها، وملازمة الجماعة في الفرائض والإكثار من النوافل» [التسهيل: 1/70].</p>
<p>«وَمَن تَزَكَّىٰ» أي: ومن تطهر من الشرك وأدناس المعاصي فإنما ثمرة ذلك التطهر عائدة على نفسه، وهذه جملة اعتراضية، تؤكد خشيتهم وإقامتهم الصلاة لأن إقامة الصلاة تزكي نفس الإنسان.</p>
<p>«وَإِلَىٰ ٱللَّهِ ٱلْمَصِيرُ» «التعريف في «ٱلْمَصِيرُ» للجنس، أي: المصير كله إلى الله، سواء فيه مصير المتزكي، ومصير غير المتزكي، أي: وكل يجازى بما يناسبه» [التحرير والتنوير؛ لابن عاشور: 22/292].</p>
<h3>رابعا: مقاصد الآيات:</h3>
<p>تقرر هذه الآيات مقاصد تربوية متعددة، منها:</p>
<ul>
<li>بيان اتصاف الله تعالى بصفات الكمال، ومنها صفة الغنى المطلق عن عباده.</li>
<li>وصف الله تعالى نفسه بأنه الحميد، يدل على أنه الغني النافع عباده بغناه؛ إذ الغني لا ينفع إلا إذا كان جوادا منعما. فإذا جاد على المنعَم عليهم حمدوه، وهذا يبين كرم الله تعالى وجوده على من عبده واستجاب لدعوته.</li>
<li>التأكيد على العدالة الإلهية المطلقة في القضاء بين العباد يوم القيامة، فلا يعاقب يومئذ إلا المذنبون.</li>
<li>خشية الله تعالى وإقامة الصلاة من أسباب الانتفاع بدعوة النبي صلى الله عليه وسلم، ونيل مرضاة الله تعالى.</li>
<li>تسلية النبي صلى الله عليه وسلم، والتأكيد على أن مهمته تقتصر على البلاغ. وهذا مما ينبغي أن يقتدي به العلماء والمرشدون والخطباء والوعاظ.</li>
</ul>
<h2>التقويم</h2>
<ul>
<li>ما الغاية من وصف الله تعالى نفسه بـ«ٱلْحَمِيدِ» بعد صفة «ٱلْفُقْرِ»؟</li>
<li>أستنتج من الآيات عدل الله تعالى بين عباده يوم القيامة.</li>
<li>هل الإنذار مقصور على المؤمنين في الآيات؟ ولماذا؟</li>
</ul>
<h2>الاستثمار</h2>
<p>«وَوَجْهُ مَا اقْتَضَتْهُ الْمُبَالَغَةُ مِنْ لَوْ الْوَصْلِيَّةِ فِي قَوْلِهِ سُبْحَانَهُ: «وَلَوْ كَانَ ذَا قُرْبَىٰٓ» أَنَّ ذَا الْقُرْبَى أَرَقُّ وَأَشْفَقُ عَلَى قَرِيبِهِ، فَقَدْ يَظُنُّ أَنَّهُ يُغْنِي عَنْهُ فِي الْآخِرَةِ بِأَنْ يُقَاسِمَهُ الثِّقَلَ الَّذِي يُؤَدِّي بِهِ إِلَى الْعَذَابِ فَيَخِفُّ عَنْهُ الْعَذَابُ بِالِاقْتِسَامِ. وَالْإِطْلَاقُ فِي الْقُرْبَى يَشْمَلُ قَرِيبَ الْقَرَابَةِ كَالْأَبَوَيْنِ وَالزَّوْجَيْنِ كَمَا قَالَ تَعَالَى: «يَوْمَ يَفِرُّ ٱلْمَرْءُ مِنْ أَخِيهِ ۝ وَأُمِّهِۦ وَأَبِيهِ» [عبس: 34-35]. وَهَذَا إِبْطَالٌ لِاعْتِقَادِ الْغَنَاءِ الذَّاتِيِّ بِالتَّضَامُنِ وَالتَّحَامُلِ فَقَدْ كَانَ الْمُشْرِكُونَ يَقِيسُونَ أُمُورَ الْآخِرَة على أُمُور الدُّنْيَا، فَيُعَلِّلُونَ أَنْفُسَهُمْ إِذَا هُدِّدُوا بِالْبَعْثِ بِأَنَّهُ إِنْ صَحَّ فَإِنَّ لَهُمْ يَوْمَئِذٍ شُفَعَاءَ وَأَنْصَارًا. فَهَذَا سِيَاقُ تَوْجِيهِ هَذَا إِلَى الْمُشْرِكِينَ، ثُمَّ هُوَ بِعُمُومِهِ يَنْسَحِبُ حُكْمُهُ عَلَى جَمِيعِ أَهْلِ الْمَحْشَرِ، فَلَا يَحْمِلُ أَحَدٌ عَنْ أَحَدٍ إِثْمَهُ. وَهَذَا لَا يُنَافِي الشَّفَاعَةَ الْوَارِدَةَ فِي الْحَدِيثِ (...) فَإِنَّهَا إِنَّمَا تَكُونُ بِإِذْنِ اللهِ تَعَالَى إِظْهَارًا لِكَرَامَةِ نَبِيئِهِ مُحَمَّدٍ صلى الله عليه وسلم، وَلَا يُنَافِي مَا جَعَلَهُ اللَّهُ لِلْمُؤْمِنِينَ مِنْ مَكَفِّرَاتٍ لِلذُّنُوبِ، كَمَا وَرَدَ أَنَّ أَفْرَاطَ الْمُؤْمِنِينَ يَشْفَعُونَ لِأُمَّهَاتِهِمْ، فَتِلْكَ شَفَاعَةٌ جَعْلِيَّةٌ جَعَلَهَا اللَّهُ كَرَامَةً لِلْأُمَّهَاتِ الْمُصَابَةِ مِنَ الْمُؤْمِنَاتِ». [التحرير والتنوير؛ للطاهر بن عاشور: 22/290 (بتصرف)]</p>
<p>أتأمل النص وأجيب عن الآتي:</p>
<ul>
<li>كيف يتم التوفيق بين عدم نفع القريب أقاربه يوم القيامة، وبين ما ورد في أدلة الشفاعة؟</li>
</ul>
<h2>الإعداد القبلي</h2>
<p>أتأمل الآيات: 19-26 من سورة فاطر وأجيب عن الآتي:</p>
<ul>
<li>أبحث عن مدلولات العبارات الآتية: «الْحَرُورُ» - «أُمَّةٍ» - «نَذِيرٌ» - «وَبِالزُّبُرِ».</li>
<li>أبحث عن أوجه المقارنة بين الفريقين الواردين في الآيات مع استحضار القواعد اللغوية.</li>
</ul>"""

HTML_FR = """<h1> Sourate Fāṭir, versets 15-18 : livre du Tafsīr à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy, deuxième année collégiale — leçon 6</h1>
<p>Leçon sur l’exégèse de la sourate Fāṭir, versets 15 à 18, du livre du Tafsīr fondé sur le <em>Tashīl li-ʿulūm al-tanzīl</em> d’Ibn Juzayy, pour la deuxième année de l’enseignement collégial traditionnel (leçon 6).</p>
<ol>
<li>Que je connaisse les manifestations de la richesse de Dieu — exalté soit-Il — et de Sa justice absolue entre Ses serviteurs.</li>
<li>Que je déduise les causes du profit tiré de la mission du Prophète — que Dieu le bénisse et lui accorde la paix.</li>
<li>Que je réponde à l’appel du Prophète — que Dieu le bénisse et lui accorde la paix — pour obtenir les caractères des croyants.</li>
</ol>
<h2>Introduction (tamhīd)</h2>
<p>Lorsque les gens de l’égarement se furent imaginé qu’ils étaient désirés dans leur adhésion aux musulmans, et que cela avait engendré en eux orgueil et complaisance envers eux-mêmes, Dieu — exalté soit-Il — leur rappela leur besoin de Lui et Son indépendance — gloire à Lui, le Très-Haut — à l’égard de toute Sa création, avec le mérite des obéissants à Le louer, Lui — exalté soit-Il — et à Sa grâce ; puis Il exposa — exalté soit-Il — Sa justice absolue entre Ses serviteurs au Jour de la résurrection : les âmes coupables ne supportent que l’étendue des péchés qu’elles ont commis — pour établir, à la fin de ces versets, que les croyants sont ceux qui profitent de l’appel du Messager — que Dieu le bénisse et lui accorde la paix.</p>
<p>Quelles sont les manifestations de la justice de Dieu — exalté soit-Il — entre Ses serviteurs ? Et comment purifierai-je mon âme à travers ces versets ?</p>
<h2>Les versets</h2>
<p>Allah — exalté soit-Il — a dit :</p>
<p><span>Sourate Fāṭir, versets 15 à 18</span></p>
<p>« Ô hommes ! Vous êtes les indigents envers Allah ; et Allah, c’est Lui le Riche, le Digne de louanges » (15).</p>
<p>« S’Il veut, Il vous fait disparaître et amène une création nouvelle » (16).</p>
<p>« Et cela n’est nullement ardu pour Allah » (17).</p>
<p>« Nul ne porte le fardeau d’un autre ; et si une âme surchargée appelle à porter sa charge, rien n’en sera porté, fût-ce par un proche. Tu n’avertis que ceux qui craignent leur Seigneur dans l’invisible et qui accomplissent la ṣalāt ; et quiconque se purifie ne le fait que pour lui-même ; et vers Allah est la destination » (18).</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>« al-fuqarāʾu ilā llāhi » (les indigents envers Allah) : ceux qui ont besoin de Lui en tout état.</p>
<p>« al-Ġanī al-Ḥamīd » (le Riche, le Digne de louanges) : Celui qui se passe de toute Sa création, le Loué pour Ses actes, Ses paroles et la bonté de Sa gestion.</p>
<p>« muṯqala » (surchargée) : c’est-à-dire accablée de ses charges au point de ne pouvoir marcher ni se mouvoir.</p>
<p>« wa-in tadʿu muṯqala » (et si une âme surchargée appelle) : elle ne trouve personne qui lui réponde et qui porte pour elle une part de son péché.</p>
<p>« tazakkā » (se purifie) : il a purifié son âme de l’association et des péchés.</p>
<h3>Extraction des contenus des versets</h3>
<ol>
<li>Par quoi Dieu — exalté soit-Il — S’est-Il décrit au début de ces versets ?</li>
<li>Qu’est-ce que Dieu a promis à Ses serviteurs au Jour de la résurrection dans ces versets ?</li>
<li>Qui profite de l’avertissement du Messager — que Dieu le bénisse et lui accorde la paix ?</li>
</ol>
<h2>Le Tafsīr</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la richesse de Dieu — exalté soit-Il — à l’égard de Sa création, une richesse absolue</h3>
<p>Après l’exposé des preuves et des arguments qui établissent l’exclusivité de Dieu — exalté soit-Il — en l’adoration, et que Lui seul y a droit, Il a appelé — exalté soit-Il — les hommes par Sa parole : « Ô hommes ! Vous êtes les indigents envers Allah » : c’est une adresse à la totalité des hommes ; et l’indigence n’a été définie par l’alif et le lām que pour indiquer que l’indigence est le propre du genre humain — quand bien même d’autres que les hommes seraient indigents, l’indigence des hommes est la plus grande.</p>
<p>Puis Il S’est décrit comme le Riche, en regard de Sa description d’eux comme indigents, et S’est décrit comme le Digne de louanges, pour marquer Son existence et Sa générosité, qui exigent que Ses serviteurs Le louent. Dieu — exalté soit-Il — a dit : « et Allah, c’est Lui le Riche, le Digne de louanges ».</p>
<p>Et Sa parole — exalté soit-Il : « Vous êtes les indigents » indique la restriction d’un attribut à son sujet (qaṣr ṣifa ʿalā mawṣūf) : c’est-à-dire la restriction de l’attribut d’indigence aux hommes. Le sens est que les hommes ont besoin de Dieu — exalté soit-Il — et qu’Il n’a pas besoin d’eux. Et dans la suite de l’attribut d’« indigence » (al-faqr) par « le Digne de louanges » (al-Ḥamīd) se trouve la levée du soupçon des gens qu’ils ne seraient pas tenus d’adorer Dieu — exalté soit-Il — du fait qu’Il se passe d’eux : car Il les a avertis — exalté soit-Il — qu’Il loue quiconque répond à Son appel et se tourne vers Lui par l’adoration.</p>
<p>Puis Il a établi — exalté soit-Il — la possibilité de Se passer de la création, par Sa parole : « S’Il veut, Il vous fait disparaître et amène une création nouvelle » : c’est-à-dire que s’Il voulait — exalté soit-Il —, Il vous anéantirait et ferait venir un peuple nouveau qui L’adorerait, Lui seul, à l’exclusion de tout autre.</p>
<p>« Et cela n’est nullement ardu pour Allah » : ʿazīz : invincible et prévalant (mumtaniʿ ġālib) — c’est-à-dire qu’il n’est ni impossible ni malaisé pour Dieu — exalté soit-Il — de vous anéantir et d’amener une création autre que vous : c’est au contraire chose aisée et légère pour Lui — exalté soit-Il. Et ces deux versets ont valu éclaircissement de la proposition « et Allah, c’est Lui le Riche, le Digne de louanges » ; l’objet (mafʿūl) de « veut » (yašaʾ) a été omis, l’indiquant par la réponse de la condition, à savoir « Il vous fait disparaître » — et l’estimation : s’Il veut, [c’est] votre disparition [qu’Il veut].</p>
<h3>Deuxièmement : la promesse de Dieu — exalté soit-Il — à Ses serviteurs de la justice entre eux au Jour de la résurrection</h3>
<p>Puisque la finalité des versets précédents était de menacer les hommes de l’anéantissement et de les remplacer par une création nouvelle, Il les a rassurés — exalté soit-Il — qu’Il jugera entre eux au Jour de la résurrection avec la justice extrême, disant — exalté soit-Il : « Nul ne porte le fardeau d’un autre ». « Le sens de taziru est : porte ; et le sens de wizrin est : le péché d’une autre âme. Et l’origine de wiẓr, en la langue, est le poids et la charge, et il vise ici les péchés ; et le sens est : nul ne porte les péchés d’autrui » [at-Tashīl : 1/283 et 443].</p>
<p>La wāzira est venue au féminin parce qu’elle vise, par elle, l’âme liée à l’acquisition des actes, comme l’indique Sa parole — exalté soit-Il : « Et nulle âme n’acquiert sinon contre elle-même » [al-Anʿām : 166], et Sa parole : « Toute âme est otage de ce qu’elle a acquise » [al-Muddaṯṯir : 38].</p>
<p>Puis Il a exposé — exalté soit-Il — que cette justice de Sien subsiste : quand même une âme surchargée de péchés et de désobéissances implorerait du secours et réclamerait que quelqu’un porte cela pour elle, elle ne trouverait personne qui porte quoi que ce soit pour elle. Le Puissant, le Majestueux a dit : « et si une âme surchargée appelle à porter sa charge, rien n’en sera porté » : la charge (ḥiml) désigne les péchés ; et la surchargée (muṯqala) : celle dont la charge est lourde, ou l’âme aux péchés nombreux ; le sens est que, si elle appelait quelqu’un à porter pour elle ses péchés, il ne les porterait pas pour elle. Et l’objet de « et si … appelle » a été omis, par indication du sens et en vue de la généralité ; et ce verset éclaire et complète le sens de Sa parole : « Nul ne porte le fardeau d’un autre » [al-Isrāʾ : 15].</p>
<p>Et Sa parole — exalté soit-Il : « fût-ce par un proche » : le sens est que, quand même celui qui est appelé serait un parent de celui qui l’a appelé à porter ses péchés, il ne porterait rien pour lui — car chacun dira : « mon âme, mon âme » (nafsī, nafsī).</p>
<h3>Troisièmement : le profit des croyants par l’appel du Messager — que Dieu le bénisse et lui accorde la paix</h3>
<p>Dieu — exalté soit-Il — a exposé à Son Messager — que Dieu le bénisse et lui accorde la paix — qui profite de son appel, disant — exalté soit-Il : « Tu n’avertis que ceux qui craignent leur Seigneur dans l’invisible » : le sens est que l’avertissement ne profite qu’à ceux qui craignent leur Seigneur — et non que l’avertissement leur serait réservé. Et Sa parole : « dans l’invisible » (bi-l-ġayb) est en position de circonstance (ḥāl) de l’agent de « ils craignent » : c’est-à-dire qu’ils craignent leur Seigneur dans leurs retraites, absents des regards des hommes — leur crainte est vérité, non ostentation.</p>
<p>Et Sa parole — exalté soit-Il : « et qui accomplissent la ṣalāt » : c’est-à-dire : « qu’ils la maintiennent en ses heures, par le dévouement exclusif (iḫlāṣ) à Dieu dans son accomplissement, la pleine exécution de ses conditions, de ses piliers, de ses mérites et de ses sunna, la présence du cœur et l’humilité en elle, la constance du groupe (ǧamāʿa) dans les prières obligatoires et l’abondance des surérogations » [at-Tashīl : 1/70].</p>
<p>« et quiconque se purifie » : c’est-à-dire : quiconque se purifie de l’association et des souillures des péchés, le fruit de cette purification ne revient qu’à lui-même ; et c’est une proposition d’incise, qui confirme leur crainte et leur accomplissement de la ṣalāt, car l’accomplissement de la ṣalāt purifie l’âme de l’homme.</p>
<p>« et vers Allah est la destination » : « la définition, dans al-maṣīr, vise le genre : c’est-à-dire que la destination tout entière est vers Dieu — qu’y soient compris pareillement le devenir de celui qui se purifie et le devenir de celui qui ne se purifie pas : chacun est rétribué selon ce qui lui convient » [at-Taḥrīr wa-t-tanwīr, d’Ibn ʿĀšūr : 22/292].</p>
<h3>Quatrièmement : les finalités (maqāṣid) des versets</h3>
<p>Ces versets établissent plusieurs finalités éducatives, parmi lesquelles :</p>
<ul>
<li>L’exposé que Dieu — exalté soit-Il — Se caractérise des attributs de perfection, parmi lesquels la richesse absolue à l’égard de Ses serviteurs.</li>
<li>Que Dieu — exalté soit-Il — Se décrive comme le Digne de louanges indique qu’Il est le Riche qui fait profiter Ses serviteurs par Sa richesse : le riche ne profite à autrui que s’il est généreux et bienfaiteur ; lorsqu’Il est généreux envers ceux qu’Il a comblés, ils Le louent — et cela montre la générosité de Dieu — exalté soit-Il — et Sa largesse envers quiconque L’adore et répond à Son appel.</li>
<li>L’affirmation de la justice divine absolue dans le jugement entre les serviteurs au Jour de la résurrection : seuls les coupables seront châtiés ce jour-là.</li>
<li>La crainte de Dieu — exalté soit-Il — et l’accomplissement de la ṣalāt comptent parmi les causes du profit de l’appel du Prophète — que Dieu le bénisse et lui accorde la paix — et de l’obtention de la satisfaction de Dieu — exalté soit-Il.</li>
<li>La consolation du Prophète — que Dieu le bénisse et lui accorde la paix — et l’affirmation que sa mission se limite à la transmission : chose dont les savants, les guides, les prédicateurs du vendredi et les exhortateurs doivent prendre modèle.</li>
</ul>
<h2>L’évaluation</h2>
<ul>
<li>Quelle est la finalité de la description, par Dieu — exalté soit-Il — de Soi-même comme « le Digne de louanges » (al-Ḥamīd), après l’attribut d’« indigence » (al-faqr) ?</li>
<li>Je déduis des versets la justice de Dieu — exalté soit-Il — entre Ses serviteurs au Jour de la résurrection.</li>
<li>L’avertissement est-il réservé aux croyants dans ces versets ? Et pourquoi ?</li>
</ul>
<h2>L’exploitation (istiṯmār)</h2>
<p>« Et le sens de ce qu’exigeait l’hyperbole de la conjonction conditionnelle lāw d’union (lāw al-waṣliyya) en Sa parole — exalté soit-Il : " fût-ce par un proche " : c’est que le parent est plus tendre et plus compatissant envers son parent — il peut penser qu’il le suppléera dans l’au-delà en partageant avec lui le poids qui le conduit au châtiment, et qu’allégera ainsi son châtiment par le partage. Et l’absolu du terme " parenté " (qurbā) embrasse le parent de proche parenté, comme les deux parents et les deux époux, comme Dieu — exalté soit-Il — a dit : " le jour où l’homme fuira son frère, sa mère et son père " [al-ʿAbasa : 34-35]. C’est là une invalidation de la croyance en l’autosuffisance par la solidarité et le port mutuel : les associationnistes comparaient les affaires de l’au-delà aux affaires de ce monde, et se donnaient pour excuse — quand ils étaient menacés de la résurrection — que, si c’était vrai, ils auraient ce jour-là des intercesseurs et des auxiliaires. C’est là le contexte qui oriente ceci vers les associationnistes ; puis, en sa généralité, sa règle s’étend à la totalité des gens du rassemblement : nul ne porte pour autrui son péché. Et cela ne contredit pas l’intercession rapportée dans le hadith (…), car elle n’a lieu que par la permission de Dieu — exalté soit-Il —, en manifestation de la dignité de Son prophète Muḥammad — que Dieu le bénisse et lui accorde la paix ; et cela ne contredit pas ce que Dieu a établi pour les croyants d’expiations (makaffirāt) des péchés, comme il est rapporté que les devanciers des croyants intercèdent pour leurs mères : c’est là une intercession institutionnelle (ǧaʿliyya), que Dieu a établie en honneur des mères éprouvées parmi les croyantes. » [at-Taḥrīr wa-t-tanwīr, d’aṭ-Ṭāhir Ibn ʿĀšūr : 22/290 (adapté)]</p>
<p>Je médite le texte et je réponds à ce qui suit :</p>
<ul>
<li>Comment concilier l’absence de profit du proche, pour ses proches, au Jour de la résurrection, avec ce qui est rapporté dans les preuves de l’intercession ?</li>
</ul>
<h2>La préparation préalable (iʿdād qablī)</h2>
<p>Je médite les versets 19 à 26 de la sourate Fāṭir et je réponds à ce qui suit :</p>
<ul>
<li>Je recherche la valeur des expressions suivantes : « al-ḥarūr » (chaleur accablante) — « ummatin » (une communauté) — « naḏīr » (avertisseur) — « wa-bi-z-zubur » (et par les Écritures).</li>
<li>Je recherche les termes de la comparaison entre les deux groupes figurant dans ces versets, en mobilisant les règles grammaticales.</li>
</ul>"""


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "--qa":
        with open(TMP, "w", encoding="utf-8") as fh:
            fh.write(HTML_FR)
        print(f"OK — tr-tmp écrit pour QA ({len(HTML_FR)} car)")
        return
    html_fr = HTML_FR
    if mode == "--from-tmp":
        with open(TMP, "r", encoding="utf-8") as fh:
            html_fr = fh.read()
        print(f"OK — FR relu depuis tr-tmp (auto-fix NNBSP) : {len(html_fr)} car")
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if str(l.get("docId", "")).endswith("-561"):
            l["html"] = HTML_AR
            l["htmlFr"] = html_fr
            l["pdfOnly"] = False
            # titre catalogue confirmé : «الآيات : 15 - 18» (citation imprimée
            # [سورة فاطر: 18-15] + CMS 16839 — convention RTL)
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 561 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 561 livrée: AR {len(HTML_AR)} car + FR {len(html_fr)} car")


if __name__ == "__main__":
    main()
