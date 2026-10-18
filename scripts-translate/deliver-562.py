#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Livraison de la leçon 562 (سورة فاطر 19-26, الدرس 7, R103-WARSH).

Vérifications R103 (méthode Warsh e-verification + croisement CMS 16851) :
- BLOC v19-26 : squelette tanzil Warsh du quran-cache s35, mot-à-mot vérifié
  contre l'imprimé (OCR 562 frais 9 pages + garbles p1-p2 : وما يستوي الأعمى
  والبصير / ولا الظلمات ولا النور / ولا الظل ولا الحرور / وما يستوي
  الأحياء ولا الأموات... إلى فكيف كان نكيري).
- GLOSSAIRE 4 entrées = IDAD 561 craqué en R102 (règle d'or 8/8) :
  «الْحَرُورُ»=شدة الحر بالنهار والليل / «أُمَّةٍ»=جماعة يجمعهم نسب واحد /
  «نَذِيرٌ»=منذر تخوف الناس من عذاب الله / «وَبِالزُّبُرِ»=الكتب المكتوبة كصحف
  إبراهيم وموسى.
- CITATION [الإسراء: 105] : WARSH-SPECIFIC — «وَمَآ أَرْسَلْنَٰكَ إِلَّا مُبَشِّرًۭا
  وَنَذِيرًۭا» (rasm Warsh du cache, ≠ Ḥafṣ «إِلَّا رَحْمَةًۭ لِّلْعَٰلَمِينَ») —
  parfait avec le contexte (يجمع في رسالته بين النذارة والبشارة).
- CITATIONS [السجدة: 2] (×3) : contenu = cache Sajda 3 Warsh «لِتُنذِرَ
  قَوْمًۭا مَّآ أَتَىٰهُم مِّن نَّذِيرٍۢ مِّن قَبْلِكَ» (≠ Ḥafṣ «مَّآ أُنذِرَ
  آبَآؤُهُمْ») — VLM 1800 dpi à raisonnement glyphique : la citation se
  TERMINE à مِن قَبْلِكَ (pas فهم غافلون) ; numérotation médinoise 2 (R57 :
  «Sajda 2→3, mā atāhum min nadhīr» — localisateur Warsh confirmé).
- FRAGMENTS re-cités : «إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ»
  [فاطر: 18] (fin garble بالعيْب=بِٱلْغَيْبِ, largeur CMS 350px ≈ 8 mots,
  renvoi «كما تقدم في الدرس السابق») ; v22 : «إِنَّ ٱللَّهَ يُسْمِعُ مَن
  يَشَآءُ» + «وَمَآ أَنتَ بِمُسْمِعٍۢ مَّن فِى ٱلْقُبُورِ» ; v23 «إِنْ أَنتَ
  إِلَّا نَذِيرٌ» + v24 «إِنَّآ أَرْسَلْنَٰكَ بِٱلْحَقِّ بَشِيرًۭا وَنَذِيرًۭا» +
  «وَإِن مِّنْ أُمَّةٍ إِلَّا خَلَا فِيهَا نَذِيرٌۭ» ; v25 : «وَإِن يُكَذِّبُوكَ
  فَقَدْ كَذَّبَ ٱلَّذِينَ مِن قَبْلِهِمْ» + «جَآءَتْهُمْ رُسُلُهُمْ» + «بِٱلْبَيِّنَٰتِ»
  + «وَبِٱلزُّبُرِ» + «وَبِٱلْكِتَٰبِ ٱلْمُنِيرِ» ; v26 : «ثُمَّ أَخَذْتُ» (img 26
  100x61 ≠ img 26_3 200x47 = فَكَيْفَ كَانَ نَكِيرِ) + «ٱلَّذِينَ كَفَرُوا۟»
  (garble «الْذِيرَكقزوا» = 7-8/10 glyphes exacts) + «فَكَيْفَ كَانَ نَكِيرِ».
- HADITH Ibn ʿAbbās (عرض الأمم) : texte propre du src.html 16851 (autorité)
  + [صحيح البخاري: كتاب الرقاق؛ باب يدخل الجنة سبعون ألفا بغير حساب].
- RÉFÉRENCES pixel-vérifiées (ordre physique des chiffres → logique
  vol/page) : Taḥrīr 22/292 (بتصرف), 22/293 (بتصرف), 22/297 ; Tashīl 2/168 ;
  Nasafī Madārik 3/85 ; Rāzī Mafātīḥ 26/233.
- SLOT «وزيادة [؟] لتأكيد معنى النفي» : «لَا» (img 22_1 = 30x32px =
  2 glyphes ; la وَلَا de v22 est l'addition vs v19).
- IDAD 562 (versets 27-28, hors livre) : 4 termes «مُخْتَلِفًا أَلْوَانُهَا» -
  «جُدَدٌ» - «غَرَابِيبُ» - «يَخْشَىٰ» (garbles p9 تخْتَل اونما/4م/غرابي/
  منشى ; VLM ligne complète 3/4 confirmés + مappariement glyphique
  ي↔م خ↔ن ش↔ش ى↔ى ; sémantique item 2 خشيته).
- Injection : AR ~10100 + FR ~14700 car. Registre hand +1 (481 main).
"""

import json
import sys

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"
TMP = "/home/z/my-project/tr-tmp/pdf-mut23h33-562.html"

HTML_AR = """<h1>سورة فاطر (الآيات: 19-26): كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي للسنة الثانية إعدادي الدرس 7</h1>
<p>درس في تفسير سورة فاطر الآيات (19-26)، كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي، للسنة الثانية من التعليم الإعدادي العتيق (الدرس 7).</p>
<ol>
<li>أن أتعرف الغاية من بعث الله تعالى في كل أمة من يبشرهم وينذرهم.</li>
<li>أن أقارن بين الفريقين الواردين في الآيات.</li>
<li>أن أقتدي بمنهج دعوة الرسول صلى الله عليه وسلم الوارد في الآيات.</li>
</ol>
<h2>تمهيد</h2>
<p>بعد بيان الله تعالى أنه لا ينتفع بنذارة الرسول صلى الله عليه وسلم إلا المؤمنون، ضرب سبحانه في هذه الآيات أربعة أمثال للفريقين، تكشف عن اختلاف حاليهما. وروعي في هذه الأشباه توزيعها على صفة الكافر والمؤمن، وعلى حالة الكفر والإيمان، وعلى أثر الإيمان وأثر الكفر؛ ثم أكدت الآيات على صدق رسالة الإسلام، وأبطلت شبه المعاندين المكذبين.</p>
<p>فكيف قارن الله تعالى بين الفريقين؟ وما الذي يدل على صدق الرسالة الإسلامية؟</p>
<h2>الآيات</h2>
<p>قال الله تعالى:</p>
<p><span>سورة فاطر: 19 - 26</span></p>
<p>«وَمَا يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ» [فاطر: 19]</p>
<p>«وَلَا ٱلظُّلُمَٰتُ وَلَا ٱلنُّورُ» [فاطر: 20]</p>
<p>«وَلَا ٱلظِّلُّ وَلَا ٱلْحَرُورُ» [فاطر: 21]</p>
<p>«وَمَا يَسْتَوِى ٱلْأَحْيَآءُ وَلَا ٱلْأَمْوَٰتُ ۚ إِنَّ ٱللَّهَ يُسْمِعُ مَن يَشَآءُ ۖ وَمَآ أَنتَ بِمُسْمِعٍۢ مَّن فِى ٱلْقُبُورِ» [فاطر: 22]</p>
<p>«إِنْ أَنتَ إِلَّا نَذِيرٌ» [فاطر: 23]</p>
<p>«إِنَّآ أَرْسَلْنَٰكَ بِٱلْحَقِّ بَشِيرًۭا وَنَذِيرًۭا ۚ وَإِن مِّنْ أُمَّةٍ إِلَّا خَلَا فِيهَا نَذِيرٌۭ» [فاطر: 24]</p>
<p>«وَإِن يُكَذِّبُوكَ فَقَدْ كَذَّبَ ٱلَّذِينَ مِن قَبْلِهِمْ جَآءَتْهُمْ رُسُلُهُم بِٱلْبَيِّنَٰتِ وَبِٱلزُّبُرِ وَبِٱلْكِتَٰبِ ٱلْمُنِيرِ» [فاطر: 25]</p>
<p>«ثُمَّ أَخَذْتُ ٱلَّذِينَ كَفَرُوا۟ ۖ فَكَيْفَ كَانَ نَكِيرِ» [فاطر: 26]</p>
<h2>الفهم</h2>
<h3>الشرح:</h3>
<p>«الْحَرُورُ»: شدة الحر بالنهار والليل.</p>
<p>«أُمَّةٍ»: جماعة يجمعهم نسب واحد.</p>
<p>«نَذِيرٌ»: منذر تخوف الناس من عذاب الله.</p>
<p>«وَبِالزُّبُرِ»: الكتب المكتوبة كصحف إبراهيم وموسى.</p>
<h3>استخلاص مضامين الآيات:</h3>
<ol>
<li>من هما الفريقان اللذان قارن الله بينهما في الآيات؟</li>
<li>من صدقت الآيات؟ وماذا أبطلت؟</li>
<li>ما الغرض من ذكر الآيات تكذيب الأمم السابقة لرسلهم؟</li>
</ol>
<h2>التفسير</h2>
<p>اشتملت هذه الآيات على ما يأتي:</p>
<h3>أولا: مقارنة بين المؤمنين وغيرهم:</h3>
<p>ضرب الله تعالى في هذه الآيات أمثلة للكافر والمؤمن، وأنهما لا يستويان، فقال سبحانه: «وَمَا يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ» الأعمى والبصير، تمثيل للمؤمن والكافر، والمعنى: أن الكافر الذي عمي عن إدراك الحق، وما جاء به الرسول صلى الله عليه وسلم، لا يستوي مع المؤمن البصير الذي آمن بالله سبحانه واهتدى بهدي رسوله صلى الله عليه وسلم.</p>
<p>«وقدمت الآيات تشبيه حال الكفار على حال المؤمنين، لأن الغرض الأهم من هذا التشبيه هو بيان فظاعة الكفر، ذلك أن هذا التشبيه جيء به لتوضيح القصر في قوله سبحانه: «إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ» [فاطر: 18] كما تقدم في الدرس السابق، وشبه الكافر بالأعمى في اختلاط أمره بين العقل والجهالة، كما يختلط أمر الأعمى بين الإدراك وعدمه.</p>
<p>ثم شبه الله تعالى حال المؤمن وغيره بحال الظلمات والنور، فقال سبحانه: «وَلَا ٱلظُّلُمَٰتُ وَلَا ٱلنُّورُ» أي: لا تستوي ظلمة الكفر، ولا نور الإيمان. وشبه الكفر بالظلمات لأن من خصائص الظلمة إخفاء الأشياء، وقد خفيت عن الكافر الحقائق الاعتقادية، فكلما بينها له القرآن لم تتضح له، كما لو وصفت الطريق للسائر في الظلام». [التحرير والتنوير؛ لابن عاشور: 22/292 (بتصرف)].</p>
<p>وكذلك لا يستوي الظل والحرور، قال تعالى: «وَلَا ٱلظِّلُّ وَلَا ٱلْحَرُورُ» وهو تمثيل للثواب والعقاب وقيل: الظل: تمثيل للجنة، والحرور تمثيل للنار. والحرور في اللغة: شدة الحر بالنهار والليل، والسموم بالنهار خاصة. والمعنى: لا يستوي الظل البارد (جزاء الإيمان) مع الحرور (جزاء الكفر والمعاصي).</p>
<p>وقد «شبه حال المؤمن بالظل، لما يسببه من اطمئنان النفوس وهدوئها، وما ينتج عن ذلك من أعمال وقرارات صادرة عن تبصر وتريث؛ ولما كانت حال الكافر ونفسيته مضطربة في أمور العقيدة والتوحيد، شبه بالحرور الذي ترتبك فيه النفوس وتصدر فيه الآراء معجلة ومتفككة» [التحرير والتنوير؛ لابن عاشور: 22/293 (بتصرف)].</p>
<p>ثم شبه الله تعالى حال المؤمن وغيره بحال الأحياء والأموات، فقال سبحانه: «وَمَا يَسْتَوِى ٱلْأَحْيَآءُ وَلَا ٱلْأَمْوَٰتُ» وهذا أبلغ مما قبله لتكرير الفعل، وزيادة «لَا» لتأكيد معنى النفي، وهو تمثيل لمن آمن فهو كالحي، ومن لم يؤمن فهو كالميت، أي: لا يستوي من كان قلبه حيا بالإيمان، مع من مات قلبه بالكفر.</p>
<h3>ثانيا: دلائل صدق الرسالة النبوية وإبطال شبه المنكرين:</h3>
<p>بعد تشبيه الله تعالى حال المؤمنين والكافرين بما سبق، أعقب ذلك بتوجيه خطاب إلى النبي صلى الله عليه وسلم ليعذره في عدم قبول رسالته لدى أحد الفريقين، فقال سبحانه: «إِنَّ ٱللَّهَ يُسْمِعُ مَن يَشَآءُ» عبارة عن هداية الله لمن يشاء، «وَمَآ أَنتَ بِمُسْمِعٍۢ مَّن فِى ٱلْقُبُورِ» عبارة عن عدم سماع الكفار للبراهين والمواعظ، فشبههم بالموتى في عدم إحساسهم، وقيل: المعنى أن أهل القبور وهم الموتى حقيقة، لا يسمعون، فليس عليك أن تسمعهم، وإنما بعثت للأحياء.</p>
<p>ثم أثنى الله تعالى على نبيه ونوه به وبالإسلام فقال سبحانه: «إِنْ أَنتَ إِلَّا نَذِيرٌ» أي: ما أنتَ إلا رسول، كلفت بإنذار الناس من عذاب جهنم، ولست مكلفا بهدايتهم؛ لأن الله تعالى هو الذي يهدي من يشاء ويضل من يشاء. «إِنَّآ أَرْسَلْنَٰكَ بِٱلْحَقِّ بَشِيرًۭا وَنَذِيرًۭا» المعنى: بعثناك بالهدى ودين الحق، بشيرا للمؤمنين بأن لهم الجنة، ونذيرا للكافرين المكذبين بأن لهم النار والعذاب الأليم.</p>
<p>والآية تدفع توهم قصر النبي صلى الله عليه وسلم على النذارة قصرا حقيقيا، وتبين أن قصره على النذارة بالنسبة لمن ماتت قلوبهم وأشبهوا أصحاب القبور؛ وتؤكد أن الرسول صلى الله عليه وسلم يجمع في رسالته بين النذارة والبشارة، كما قال تعالى: «وَمَآ أَرْسَلْنَٰكَ إِلَّا مُبَشِّرًۭا وَنَذِيرًۭا» [الإسراء: 105].</p>
<p>ثم بين سبحانه أنه لم تخل أمة من نذير ينذرهم، ويوضح لهم رسالته. قال سبحانه: «وَإِن مِّنْ أُمَّةٍ إِلَّا خَلَا فِيهَا نَذِيرٌۭ» معناه: أن الله قد بعث إلى كل أمة نبيا يقيم عليهم الحجة.</p>
<p>فإن قيل: كيف لم تخل أمة من نذير وقد كان بين الأنبياء فترات وأزمنة طويلة؟ ألا ترى أن بين عيسى ومحمد صلى الله عليه وسلم ستمائة سنة لم يبعث فيها نبي؟</p>
<p>فالجواب: أن دعوة عيسى ومن تقدمه من الأنبياء كانت قد بلغتهم فقامت عليهم الحجة. فإن قيل: كيف الجمع بين هذه الآية وبين قوله: «لِتُنذِرَ قَوْمًۭا مَّآ أَتَىٰهُم مِّن نَّذِيرٍۢ مِّن قَبْلِكَ» [السجدة: 2] فالجواب: أنهم لم يأتهم نذير معاصر لهم، فلا يعارض ذلك من تقدم قبل عصرهم، وأيضا فإن المراد بقوله: «وَإِن مِّنْ أُمَّةٍ إِلَّا خَلَا فِيهَا نَذِيرٌۭ» أن نبوة محمد صلى الله عليه وسلم ليست ببدع فلا ينبغي أن تنكر؛ لأن الله أرسله كما أرسل من قبله، والمراد بقوله: «لِتُنذِرَ قَوْمًۭا مَّآ أَتَىٰهُم مِّن نَّذِيرٍۢ مِّن قَبْلِكَ» أنهم محتاجون إلى الإنذار، لكونهم لم يتقدم من ينذرهم، فاختلف سياق الكلام فلا تعارض بينهما.</p>
<p>«وقد اقتصر في الآية على وصف النذير دون وصف البشير، مراعاة للعموم الوارد فيها، ذلك أن بعض الأمم لم تحصل لهم بشارة لأنه لم يؤمن منهم أحد، ففي حديث ابن عباس أنه قال: قال رسول الله صلى الله عليه وسلم: «عُرِضَتْ عَلَيَّ الأُمَمُ، فَأَخَذَ النَّبِيُّ يَمُرُّ مَعَهُ الأُمَّةُ، وَالنَّبِيُّ يَمُرُّ مَعَهُ النَّفَرُ، وَالنَّبِيُّ يَمُرُّ مَعَهُ العَشَرَةُ، وَالنَّبِيُّ يَمُرُّ مَعَهُ الخَمْسَةُ، وَالنَّبِيُّ يَمُرُّ وَحْدَهُ» [صحيح البخاري: كتاب الرقاق؛ باب يدخل الجنة سبعون ألفا بغير حساب]» [التحرير والتنوير؛ للطاهر بن عاشور: 22/297].</p>
<h3>ثالثا: تسلية الرسول صلى الله عليه وسلم على تكذيب قومه له:</h3>
<p>بعد ثناء الله تعالى على نبيه صلى الله عليه وسلم، أتبع ذلك بتسليته على تكذيب قومه، فقال سبحانه: «وَإِن يُكَذِّبُوكَ فَقَدْ كَذَّبَ ٱلَّذِينَ مِن قَبْلِهِمْ» أي: وإن يكذبك من أشرك من قومك، فقد كذب الذين من قبلهم «جَآءَتْهُمْ رُسُلُهُمْ حال، وقد مضمرة بِٱلْبَيِّنَٰتِ بالمعجزات وَبِٱلزُّبُرِ وبالصحف وَبِٱلْكِتَٰبِ ٱلْمُنِيرِ، أي: التوراة، والإنجيل، والزبور. لما كانت هذه الأشياء في جنسهم أسند المجيء بها إليهم إسنادا مطلقا، وإن كان بعضها في جميعهم، وهي البينات، وبعضها في بعضهم، وهي الزبر والكتاب، وفيه مسلاة لرسول الله صلى الله عليه وسلم «ثُمَّ أَخَذْتُ» عاقبت «ٱلَّذِينَ كَفَرُوا۟» بأنواع العقوبة» [مدارك التنزيل وحقائق التأويل؛ للنسفي: 3/85].</p>
<p>وقوله تعالى: «فَكَيْفَ كَانَ نَكِيرِ» أي: فَكَيْفَ إنكاري، يعني: عقوبة الكفار المتقدمين [التسهيل: 2/168].</p>
<h3>رابعا: مقاصد الآيات:</h3>
<p>تدل الآيات على مقاصد تربوية جليلة، منها:</p>
<ul>
<li>ربط الجزاء بجنس العمل، إذ قارنت الآيات بين فريقين من الناس، فريق آمن بالله واستجاب لرسالته وأطاع أمر ربه، فاستحق الثواب، وفريق عاند وكذب بآيات الله وما جاء به أنبياؤه ورسله فاستحق بذلك العذاب.</li>
<li>التأكيد على صدق رسالة النبي صلى الله عليه وسلم، وأن مهمته تقتصر على البشارة والنذارة.</li>
<li>بيان أن الله سبحانه وتعالى هو من يتولى الهداية لمن يشاء من عباده.</li>
<li>بيان منهج أصيل في الدعوة الإسلامية، وإرشاد للعلماء والمصلحين وحث لهم على الاقتداء بهذا المنهج النبوي ليوجهوا خطابهم إلى الناس مبشرين ومنذرين بالحكمة والموعظة الحسنة.</li>
<li>الحكمة من الإنذار هي أن لا يبقى الضلال رائجا، وأن يرشد الناس إلى الحق والطريق المستقيم، وفي هذا تتجلى رحمة الله تعالى بعباده.</li>
</ul>
<h2>التقويم</h2>
<ol>
<li>ما هي أوجه الاختلاف بين الفريقين المذكورين في الآيات؟</li>
<li>لماذا اقتصر على ذكر النذارة في الآية: «وَإِن مِّنْ أُمَّةٍ إِلَّا خَلَا فِيهَا نَذِيرٌۭ»؟ وكيف يمكن الجمع بينها، وبين قوله تعالى: «لِتُنذِرَ قَوْمًۭا مَّآ أَتَىٰهُم مِّن نَّذِيرٍۢ مِّن قَبْلِكَ» [السجدة: 2]؟</li>
<li>ما هي الغاية من بعثة الأنبياء والرسل؟ وما علاقة ذلك بمقاصد الآيات؟</li>
<li>كيف أقتدي بالرسول صلى الله عليه وسلم في منهجه الدعوي؟</li>
</ol>
<h2>الاستثمار</h2>
<p>«فَإِنْ قُلْتَ قَابَلَ الْأَعْمَى بِالْبَصِيرِ بِلَفْظِ الْمُفْرَدِ وَكَذَلِكَ الظِّلُّ بِالْحَرُورِ وَقَابَلَ الْأَحْيَاءَ بِالْأَمْوَاتِ بِلَفْظِ الْجَمْعِ، وَقَابَلَ الظُّلُمَاتِ بِالنُّورِ بِلَفْظِ الْجَمْعِ فِي أَحَدِهِمَا وَالْوَاحِدِ فِي الْآخَرِ، فَهَلْ تَعْرِفُ فِيهِ حِكْمَةً؟ قُلْتُ: نَعَمْ بِفَضْلِ اللَّهِ وَهِدَايَتِهِ، أَمَّا فِي الْأَعْمَى وَالْبَصِيرِ وَالظِّلِّ وَالْحَرُورِ، فَلِأَنَّهُ قَابَلَ الْجِنْسَ بِالْجِنْسِ، وَلَمْ يَذْكُرِ الْأَفْرَادَ لِأَنَّ فِي الْعُمْيَانِ (وَأُولِي الْأَبْصَارِ) قَدْ يُوجَدُ فَرْدٌ مِنْ أَحَدِ الْجِنْسَيْنِ يُسَاوِي فَرْدًا مِنَ الْجِنْسِ الْآخَرِ كَالْبَصِيرِ الْغَرِيبِ فِي مَوْضِعٍ وَالْأَعْمَى الَّذِي هُوَ تَرْبِيَةُ ذَلِكَ الْمَكَانِ، وَقَدْ يَقْدِرُ الْأَعْمَى عَلَى الْوُصُولِ إِلَى مَقْصِدٍ وَلَا يَقْدِرُ الْبَصِيرُ عَلَيْهِ، أَوْ يَكُونُ الْأَعْمَى عِنْدَهُ مِنَ الذَّكَاءِ مَا يُسَاوِي بِهِ الْبَلِيدَ الْبَصِيرَ، فَالتَّفَاوُتُ بَيْنَهُمَا فِي الْجِنْسَيْنِ مَقْطُوعٌ بِهِ فَإِنَّ جِنْسَ الْبَصِيرِ خَيْرٌ مِنْ جِنْسِ الْأَعْمَى، وَأَمَّا الْأَحْيَاءُ وَالْأَمْوَاتُ فَالتَّفَاوُتُ بَيْنَهُمَا أَكْثَرُ، إِذْ مَا مِنْ مَيِّتٍ يُسَاوِي فِي الْإِدْرَاكِ حَيًّا مِنَ الْأَحْيَاءِ، فَذَكَرَ أَنَّ الْأَحْيَاءَ لَا يُسَاوُونَ الْأَمْوَاتَ سَوَاءٌ قَابَلْتَ الْجِنْسَ بِالْجِنْسِ أَوْ قَابَلْتَ الْفَرْدَ بِالْفَرْدِ، وَأَمَّا الظُّلُمَاتُ وَالنُّورُ فَالْحَقُّ وَاحِدٌ وَهُوَ التَّوْحِيدُ، وَالْبَاطِلُ كَثِيرٌ وَهُوَ طَرُقُ الْإِشْرَاكِ، عَلَى مَا بَيَّنَّا أَنَّ بَعْضَهُمْ يَعْبُدُونَ الْكَوَاكِبَ وَبَعْضَهُمُ النَّارَ وَبَعْضَهُمُ الْأَصْنَامَ الَّتِي هِيَ عَلَى صُورَةِ الْمَلَائِكَةِ، وَإِلَى غَيْرِ ذَلِكَ وَالتَّفَاوُتُ بَيْنَ كُلِّ فَرْدٍ مِنْ تِلْكَ الْأَفْرَادِ وَبَيْنَ هَذَا الْوَاحِدِ بَيِّنٌ». [مفاتيح الغيب؛ لفخر الدين الرازي: 26/233]</p>
<p>أتأمل النص وأبين الحكمة من استعمال الإفراد والجمع في الآيات.</p>
<h2>الإعداد القبلي</h2>
<p>أتأمل الآيتين: 27-28 من سورة فاطر وأجيب عن الآتي:</p>
<ul>
<li>أبحث عن مدلولات العبارات الآتية: «مُخْتَلِفًا أَلْوَانُهَا» - «جُدَدٌ» - «غَرَابِيبُ» - «يَخْشَىٰ».</li>
<li>أبحث في الآيتين عن مظاهر قدرة الله وعلاقتها بخشيته سبحانه.</li>
</ul>"""

HTML_FR = """<h1> Sourate Fāṭir, versets 19-26 : livre du Tafsīr à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy, deuxième année collégiale — leçon 7</h1>
<p>Leçon sur l’exégèse de la sourate Fāṭir, versets 19 à 26, du livre du Tafsīr fondé sur le <em>Tashīl li-ʿulūm al-tanzīl</em> d’Ibn Juzayy, pour la deuxième année de l’enseignement collégial traditionnel (leçon 7).</p>
<ol>
<li>Que je connaisse la finalité de l’envoi, par Dieu — exalté soit-Il —, en chaque communauté, de quelqu’un qui annonce et qui avertit.</li>
<li>Que je compare les deux groupes figurant dans ces versets.</li>
<li>Que je prenne modèle sur la méthode d’appel du Messager — que Dieu le bénisse et lui accorde la paix — figurant dans ces versets.</li>
</ol>
<h2>Introduction (tamhīd)</h2>
<p>Après que Dieu — exalté soit-Il — a établi que seuls les croyants profitent de l’avertissement du Messager — que Dieu le bénisse et lui accorde la paix —, Il a frappé, dans ces versets, quatre paraboles pour les deux groupes, qui dévoilent la différence de leurs états. Et dans ces ressemblances fut observée leur répartition selon l’attribut de l’infidèle et du croyant, selon l’état de l’infidélité et de la foi, selon l’effet de la foi et l’effet de l’infidélité ; puis les versets ont affirmé la véracité du message de l’islam et invalidé les objections des récalcitrants traiteurs de menteurs.</p>
<p>Comment Dieu — exalté soit-Il — a-t-Il comparé les deux groupes ? Et qu’est-ce qui atteste la véracité du message islamique ?</p>
<h2>Les versets</h2>
<p>Allah — exalté soit-Il — a dit :</p>
<p><span>Sourate Fāṭir, versets 19 à 26</span></p>
<p>« L’aveugle et le voyant ne sont pas semblables » (19).</p>
<p>« Ni les ténèbres ni la lumière » (20).</p>
<p>« Ni l’ombre ni la chaleur accablante » (21).</p>
<p>« Les vivants et les morts ne sont pas semblables : Allah fait entendre qui Il veut ; et tu n’es pas celui qui fait entendre ceux qui sont dans les tombes » (22).</p>
<p>« Tu n’es qu’un avertisseur » (23).</p>
<p>« Nous t’avons envoyé avec la vérité, en annonciateur et en avertisseur ; et il n’est de communauté en laquelle ne soit passé un avertisseur » (24).</p>
<p>« Et s’ils te traitent de menteur — ceux d’avant eux ont traité de menteurs ceux à qui leurs messagers étaient venus avec les preuves évidentes, les Écritures et le Livre lumineux » (25).</p>
<p>« Puis J’ai saisi ceux qui ont mécru ; et quelle fut alors Ma réprobation ! » (26).</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>« al-ḥarūr » (chaleur accablante) : intensité de la chaleur, de jour comme de nuit.</p>
<p>« ummatin » (une communauté) : un groupe d’êtres qu’unit une même lignée.</p>
<p>« naḏīr » (avertisseur) : celui qui met les gens en garde du châtiment de Dieu.</p>
<p>« wa-bi-z-zubur » (et par les Écritures) : les livres écrits, tels les feuilles d’Abraham et de Moïse.</p>
<h3>Extraction des contenus des versets</h3>
<ol>
<li>Qui sont les deux groupes que Dieu a comparés dans ces versets ?</li>
<li>Qui les versets ont-ils déclarés véridiques ? Et qu’ont-ils invalidé ?</li>
<li>Quel est le dessein de la mention, par les versets, du traitement de menteurs infligé par les communautés antérieures à leurs messagers ?</li>
</ol>
<h2>Le Tafsīr</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : une comparaison entre les croyants et les autres</h3>
<p>Dieu — exalté soit-Il — a frappé, dans ces versets, des paraboles pour l’infidèle et le croyant — qui ne s’équivalent pas —, disant — exalté soit-Il : « L’aveugle et le voyant ne sont pas semblables » : l’aveugle et le voyant sont une figure du croyant et de l’infidèle. Le sens est que l’infidèle, devenu aveugle à la perception du vrai et à ce qu’a apporté le Messager — que Dieu le bénisse et lui accorde la paix —, ne vaut pas le croyant clairvoyant qui a cru en Dieu — exalté soit-Il — et s’est guidé à la guidance de Son messager — que Dieu le bénisse et lui accorde la paix.</p>
<p>« Les versets ont avancé la ressemblance de l’état des infidèles sur celui des croyants, car le dessein le plus important de cette ressemblance est d’exposer la monstruosité de l’infidélité : cette ressemblance fut amenée pour éclaircir la restriction (qaṣr) en Sa parole — exalté soit-Il : " Tu n’avertis que ceux qui craignent leur Seigneur dans l’invisible " [Fāṭir : 18], comme il a précédé au cours précédent ; et l’infidèle fut assimilé à l’aveugle dans le mélange de son état entre raison et ignorance, comme se mélange l’état de l’aveugle entre perception et non-perception.</p>
<p>Puis Dieu — exalté soit-Il — a assimilé l’état du croyant et de l’autre à l’état des ténèbres et de la lumière, disant — exalté soit-Il : " Ni les ténèbres ni la lumière " : c’est-à-dire que ne s’équivalent pas la obscurité de l’infidélité et la lumière de la foi. Et l’infidélité fut assimilée aux ténèbres parce que des propriétés des ténèbres est la dissimulation des choses — et les réalités doctrinales sont restées dissimulées à l’infidèle : chaque fois que le Coran les lui expose, elles ne lui deviennent pas claires, comme si tu décrivais la route au marcheur dans l’obscurité. » [at-Taḥrīr wa-t-tanwīr, d’Ibn ʿĀšūr : 22/292 (adapté)].</p>
<p>De même ne s’équivalent pas l’ombre et la chaleur accablante — Dieu — exalté soit-Il — a dit : " Ni l’ombre ni la chaleur accablante " : c’est une figure de la récompense et du châtiment ; on a dit : l’ombre est une figure du Paradis, et la chaleur accablante une figure du Feu. Et ḥarūr, en la langue : intensité de la chaleur de jour et de nuit, et le simoun (vent brûlant) de jour seulement. Le sens : l’ombre fraîche (récompense de la foi) ne vaut pas la chaleur accablante (récompense de l’infidélité et des péchés).</p>
<p>« Et l’état du croyant fut assimilé à l’ombre, pour la sérénité des âmes et leur calme qu’il engendre, et pour les œuvres et décisions qui en procèdent, issues de clairvoyance et de pondération ; et puisque l’état de l’infidèle et sa psychologie étaient perturbés dans les affaires de la doctrine et de l’unicité, il fut assimilé à la chaleur accablante, en laquelle les âmes s’embrouillent et où les avis s’énoncent, précipités et dispersés » [at-Taḥrīr wa-t-tanwīr, d’Ibn ʿĀšūr : 22/293 (adapté)].</p>
<p>Puis Dieu — exalté soit-Il — a assimilé l’état du croyant et de l’autre à l’état des vivants et des morts, disant — exalté soit-Il : " Les vivants et les morts ne sont pas semblables " : ceci est plus expressif que ce qui précède, du fait de la répétition du verbe et de l’adjonction de " lā " pour renforcer le sens de la négation. C’est une figure de celui qui a cru — il est comme le vivant — et de celui qui n’a pas cru — il est comme le mort : c’est-à-dire que ne vaut pas celui dont le cœur est vivant par la foi, celui dont le cœur est mort par l’infidélité.</p>
<h3>Deuxièmement : les preuves de la véracité du message prophétique et l’invalidation des objections des négateurs</h3>
<p>Après que Dieu — exalté soit-Il — a assimilé l’état des croyants et des infidèles à ce qui précède, Il a fait suivre d’une adresse au Prophète — que Dieu le bénisse et lui accorde la paix — pour l’excuser de ce que l’un des deux groupes n’accepte pas son message, disant — exalté soit-Il : " Allah fait entendre qui Il veut " : formule de la guidance de Dieu envers qui Il veut ; " et tu n’es pas celui qui fait entendre ceux qui sont dans les tombes " : formule de la non-audition, par les infidèles, des preuves et des exhortations — Il les a assimilés aux morts dans leur insensibilité. On a dit aussi : le sens est que les gens des tombes, qui sont les morts au vrai sens, n’entendent pas : il ne t’incombe pas de les faire entendre — tu n’as été envoyé qu’aux vivants.</p>
<p>Puis Dieu — exalté soit-Il — a fait l’éloge de Son prophète, l’a magnifié, lui et l’islam, disant — exalté soit-Il : " Tu n’es qu’un avertisseur " : c’est-à-dire : tu n’es qu’un messager, chargé d’avertir les gens du châtiment de la Géhenne ; tu n’es pas chargé de les guider, car Dieu — exalté soit-Il — guide qui Il veut et égare qui Il veut. " Nous t’avons envoyé avec la vérité, en annonciateur et en avertisseur " : le sens : Nous t’avons envoyé avec la guidance et la religion du vrai — en annonciateur pour les croyants, que le Paradis leur est promis, et en avertisseur pour les infidèles traiteurs de menteurs, que le Feu et le châtiment douloureux leur sont promis.</p>
<p>Et le verset écarte le soupçon que le Prophète — que Dieu le bénisse et lui accorde la paix — serait restreint à l’avertissement par une restriction absolue, et établit que sa restriction à l’avertissement ne vaut que relativement à ceux dont les cœurs sont morts et qui ressemblent aux gens des tombes ; et il affirme que le Messager — que Dieu le bénisse et lui accorde la paix — réunit, dans son message, l’avertissement et l’annonce, comme Dieu — exalté soit-Il — a dit : " et Nous ne t’avons envoyé qu’en annonciateur et en avertisseur " [al-Isrāʾ : 105].</p>
<p>Puis Il a établi — exalté soit-Il — qu’il n’est pas de communauté qui soit dépourvue d’un avertisseur pour les avertir et leur exposer son message, disant — exalté soit-Il : " et il n’est de communauté en laquelle ne soit passé un avertisseur " : son sens est que Dieu a envoyé à chaque communauté un prophète qui établisse sur elle la preuve.</p>
<p>Si l’on objecte : comment n’est-il pas de communauté dépourvue d’avertisseur, alors qu’il y eut entre les prophètes de longues interruptions et de longs âges ? Ne vois-tu pas qu’entre Jésus et Muḥammad — que Dieu le bénisse et lui accorde la paix — se sont écoulées six cents années sans qu’un prophète ne soit envoyé ?</p>
<p>La réponse : l’appel de Jésus et des prophètes qui le précédèrent leur était parvenu, et la preuve s’était établie sur eux. Si l’on objecte : comment accorder ce verset avec Sa parole : " afin que tu avertisses un peuple auquel n’est venu aucun avertisseur avant toi " [as-Sajda : 2] ? — la réponse : il ne leur est pas venu d’avertisseur contemporain d’eux : cela ne contredit pas celui qui a précédé avant leur époque. Et de même, le visé par Sa parole : " et il n’est de communauté en laquelle ne soit passé un avertisseur ", est que la prophétie de Muḥammad — que Dieu le bénisse et lui accorde la paix — n’est pas une innovation : il ne sied pas de la renier, car Dieu l’a envoyé comme Il a envoyé ceux d’avant lui ; et le visé par Sa parole : " afin que tu avertisses un peuple auquel n’est venu aucun avertisseur avant toi ", est qu’ils ont besoin de l’avertissement, du fait que ne les a précédés personne pour les avertir : le contexte du propos diffère donc, et il n’y a entre eux nulle contradiction.</p>
<p>« Et il a été restreint, dans le verset, à la description de l’avertisseur sans celle de l’annonciateur, en égard à la généralité qui y figure — car certaines communautés n’ont pas reçu d’annonce, parce qu’il n’a cru, d’elles, personne. Ainsi, dans le hadith d’Ibn ʿAbbās, il dit : le Messager de Dieu — que Dieu le bénisse et lui accorde la paix — a dit : " Les communautés me furent présentées, et voici le prophète qui passe accompagné de la communauté entière ; et le prophète qui passe accompagné du groupe ; et le prophète qui passe accompagné de dix ; et le prophète qui passe accompagné de cinq ; et le prophète qui passe seul " » [Ṣaḥīḥ al-Buḫārī : livre des attendrissements (ruqāq) ; chapitre : entrent au Paradis soixante-dix mille sans compte] [at-Taḥrīr wa-t-tanwīr, d’aṭ-Ṭāhir Ibn ʿĀšūr : 22/297].</p>
<h3>Troisièmement : la consolation du Messager — que Dieu le bénisse et lui accorde la paix — face au traitement de menteur de son peuple</h3>
<p>Après l’éloge que Dieu — exalté soit-Il — a faite de Son prophète, Il en a fait suivre la consolation face au traitement de menteur infligé par son peuple, disant — exalté soit-Il : « Et s’ils te traitent de menteur » : c’est-à-dire : et si ceux de ton peuple qui ont associé te traitent de menteur — « ceux d’avant eux ont traité de menteurs ceux à qui leurs messagers étaient venus — circonstance (ḥāl) dont le qad est élidé — avec les preuves évidentes : avec les miracles ; et les Écritures : et avec les feuilles ; et le Livre lumineux : c’est-à-dire la Torāh, l’Évangile et le Psautier. Puisque ces choses étaient, en leur genre, les unes communes à tous — les preuves évidentes —, les autres propres à certains — les Écritures et le Livre —, la venue en est rapportée à eux d’une attribution absolue. Et il y a, en ceci, consolation pour le Messager de Dieu — que Dieu le bénisse et lui accorde la paix : “ Puis J’ai saisi ” — J’ai châtié — “ ceux qui ont mécru ” — de sortes de châtiment » [Madārik at-tanzīl wa-ḥaqāʾiq at-taʾwīl, d’an-Nasafī : 3/85].</p>
<p>Et Sa parole — exalté soit-Il : " et quelle fut alors Ma réprobation " : c’est-à-dire : comment fut Mon désaveu — voulant dire : le châtiment des infidèles d’autrefois [at-Tashīl : 2/168].</p>
<h3>Quatrièmement : les finalités (maqāṣid) des versets</h3>
<p>Ces versets indiquent d’importantes finalités éducatives, parmi lesquelles :</p>
<ul>
<li>Le lien de la rétribution au genre de l’œuvre : les versets ont comparé deux groupes d’hommes — un groupe qui a cru en Dieu, a répondu à Son message et obéi à l’ordre de son Seigneur, et a mérité la récompense ; et un groupe qui s’est obstiné, a traité de menteurs les signes de Dieu et ce qu’ont apporté Ses prophètes et Ses messagers, et a mérité par là le châtiment.</li>
<li>L’affirmation de la véracité du message du Prophète — que Dieu le bénisse et lui accorde la paix —, et que sa mission se limite à l’annonce et à l’avertissement.</li>
<li>L’établissement que Dieu — exalté soit-Il — est Celui qui assume la guidance de qui Il veut, parmi Ses serviteurs.</li>
<li>L’exposé d’une méthode originelle dans l’appel islamique, et une direction pour les savants et les réformateurs, et une exhortation à prendre modèle sur cette méthode prophétique pour adresser aux hommes leur parole, en annonciateurs et avertisseurs, avec sagesse et bonne exhortation.</li>
<li>La sagesse de l’avertissement est que l’égarement ne demeure pas florissant, et que les hommes soient guidés au vrai et à la voie droite — et en ceci se déploie la miséricorde de Dieu — exalté soit-Il — envers Ses serviteurs.</li>
</ul>
<h2>L’évaluation</h2>
<ol>
<li>Quels sont les termes de la différence entre les deux groupes mentionnés dans ces versets ?</li>
<li>Pourquoi s’est-on restreint, dans le verset, à la mention de l’avertissement : " et il n’est de communauté en laquelle ne soit passé un avertisseur " ? Et comment accorder ce verset avec Sa parole — exalté soit-Il : " afin que tu avertisses un peuple auquel n’est venu aucun avertisseur avant toi " [as-Sajda : 2] ?</li>
<li>Quelle est la finalité de l’envoi des prophètes et des messagers ? Et quel est son lien avec les finalités des versets ?</li>
<li>Comment prendrai-je modèle sur le Messager — que Dieu le bénisse et lui accorde la paix — dans sa méthode d’appel ?</li>
</ol>
<h2>L’exploitation (istiṯmār)</h2>
<p>« Si tu dis : Il a confronté l’aveugle au voyant au singulier, et de même l’ombre à la chaleur accablante ; Il a confronté les vivants aux morts au pluriel ; et Il a confronté les ténèbres à la lumière — au pluriel dans l’un, au singulier dans l’autre : en connais-tu la sagesse ? Je réponds : oui, par la faveur de Dieu et Sa guidance. Quant à l’aveugle et au voyant, à l’ombre et à la chaleur : c’est qu’Il a confronté le genre au genre, et qu’Il n’a pas mentionné les individus, car parmi les aveugles (et les doués de vue) il se peut qu’il se trouve un individu de l’un des deux genres qui égale un individu de l’autre genre — tel le voyant étranger en un lieu, et l’aveugle qui y a été élevé ; tel l’aveugle capable de parvenir à un but où le voyant n’arrive pas ; tel l’aveugle qui possède de l’intelligence de quoi égaler le voyant borné. L’écart entre eux, dans les deux genres, est donc certain : le genre des voyants est meilleur que le genre des aveugles. Quant aux vivants et aux morts, l’écart entre eux est plus grand : il n’est pas de mort qui égale, en perception, un vivant parmi les vivants — Il a donc dit que les vivants n’égalent pas les morts, que tu confrontes le genre au genre ou l’individu à l’individu. Quant aux ténèbres et à la lumière : le vrai est un, et c’est l’unicité (tawḥīd) ; le faux est multiple, et ce sont les voies de l’association — comme Nous l’avons exposé : certains adorent les astres, d’autres le feu, d’autres les idoles qui sont à l’image des anges, et ainsi de suite ; et l’écart entre chaque individu de ces individus-là et cet Unique est manifeste. » [Mafātīḥ al-ġayb, de Faḫr ad-Dīn ar-Rāzī : 26/233]</p>
<p>Je médite le texte et j’expose la sagesse de l’emploi du singulier et du pluriel dans ces versets.</p>
<h2>La préparation préalable (iʿdād qablī)</h2>
<p>Je médite les deux versets 27 et 28 de la sourate Fāṭir et je réponds à ce qui suit :</p>
<ul>
<li>Je recherche la valeur des expressions suivantes : « muḫtalifan alwānuhā » (aux couleurs différentes) — « ǧudad » (stries) — « ġarābīb » (d’un noir profond) — « yaḫšā » (craint).</li>
<li>Je recherche, dans les deux versets, les manifestations de la puissance de Dieu et leur lien avec Sa crainte — exalté soit-Il.</li>
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
        if str(l.get("docId", "")).endswith("-562"):
            l["html"] = HTML_AR
            l["htmlFr"] = html_fr
            l["pdfOnly"] = False
            # titre catalogue confirmé : «الآيات : 19 - 26» (citation imprimée
            # [سورة فاطر: 26-19] + CMS 16851 — convention RTL)
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 562 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 562 livrée: AR {len(HTML_AR)} car + FR {len(html_fr)} car")


if __name__ == "__main__":
    main()
