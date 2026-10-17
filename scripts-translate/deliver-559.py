#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Livraison de la leçon 559 (سورة فاطر 10-11, الدرس 4, R100-WARSH).

Vérifications R100 (méthode Warsh e-verification + croisement CMS 16812) :
- BLOC v10-11 : garbles 300/600 dpi conformes au squelette tanzil Warsh
  (مركا برط الل كااه الووجيعا = من كان يريد العزة فلله العزة جميعا / وزوز وال
  لفحم يى تل تور ثم جاح وا لماو تمان اتيى = والله خلقكم من تراب ثم من نطفة ثم
  جعلكم أزواجا / عَلو اتير = إن ذلك على الله يسير) — Fāṭir = 45 versets dans
  les deux comptages, AUCUN décalage (confirmé R99 pour v7-9).
- GLOSSAIRE 4 entrées (règle d'or 4/4 pour la 5e fois consécutive : idad de
  558 = الشرح de 559) : «ٱلْعِزَّةُ»=الشرف والمنعة / «مَكْرٌ»=ما عُمل على سبيل
  احتيال وخديعة / «يَبُورُ»=يهلك ويكسد / «أَزْوَاجًا»=أصنافا أو ذكرانا وإناثا.
- VERROU IDAD 559 (7 termes, croisés glossaire 560 PDF p2 600dpi + CMS 16823) :
  t1 «عَذْبٌ فُرَاتٌ» (runs 233+110+149 = e1 EXACT) - t2 «سَآئِغٌ شَرَابُهُ»
  (227+223 ≈ e2 228+223, 2e mot EXACT) - t3 «مِلْحٌ أُجَاجٌ» (250+151 = e3
  EXACT, ligne manquée par l'OCR 560 reconstituée) - t4 «لَحْمًا طَرِيًّا»
  (486 = e4 EXACT) - t5 «حِلْيَةً تَلْبَسُونَهَا» (OCR focal 5 pipelines :
  «حليةتَابَمُوتَها» = حِلْيَةً + تَلْبَسُونَهَا avec 3 confusions standard
  ل→ا/س→م/ن→ت ; corrélation pixel des 190px droits vs e5 «حِلْيَةً» = 0.541,
  contrôle t4/e4 = 0.526 ; sémantique : seule phrase حِلْيَةً de v12) -
  t6 «مَوَاخِرَ» (garbles وار/وخر + def 560 «جمع ماخرة وهي السفينة») -
  t7 «قِطْمِيرٍ» (garble فكصير = le garble du glossaire 560 lui-même «فكتمير»
  avec def «القشر الرقيق الأبيض الذي على نوى التمر»).
- Références : Ibn ʿAǧība [البحر المديد: 525/4] (continuité 558=520/4, format
  PAGE/VOL) ; Ibn ʿĀšūr [التحرير والتنوير: 274/22] (continuité 557=258-259/22) ;
  citation فاطر 43 = «وَلَا يَحِيقُ ٱلْمَكْرُ ٱلسَّيِّئُ إِلَّا بِأَهْلِهِ» (rasm
  Warsh du squelette — le CMS dégradé porte يُحِيق) ; citation الأنفال 30
  (fragment jusqu'à وَيُخْرِجُوكَ) ; hadith الطبراني [المعجم الأوسط، باب الألف،
  من اسمه أحمد] (CMS أحمد vs OCR أحسد = garble) ; vers Ǧarīr «بِظَهْرِ الْغَيْبِ»
  (CMS, OCR الْقَيْبِ = garble).
- Croisement CMS 16812 (2e canal, minhaj.ma) : tamhīd verbatim (أوهام قريش),
  citation Ibn ʿĀšūr verbatim (y compris «بِوَاسِطَةِ الْبَاءِ الَّتِي
  لِلْمُلَابَسَةِ» — l'OCR portait «اليَاء» = garble), 3 معان / 3 أقوال /
  3 أوجه de la structure Ibn Juzayy, 3 مقاصد, 2 questions d'istiṯmār.
- Honorifiques : aucun après ابن عباس/ابن عطية (CMS sans + psm4 600dpi sans +
  original Ibn Juzayy sans — les petites marques = ponctuation/tashkīl).
- Injection : AR 8406 + FR ~12700 car. Registre hand +1 (478 main).
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"

HTML_AR = """<h1>سورة فاطر (الآيتان: 10-11): كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي للسنة الثانية إعدادي الدرس 4</h1>
<p>درس في تفسير سورة فاطر الآيتين (10-11)، كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي، للسنة الثانية من التعليم الإعدادي العتيق (الدرس 4).</p>
<ol>
<li>أن أتبين أسباب حصول العزة للإنسان.</li>
<li>أن أستنتج عاقبة الماكرين بالإسلام والمسلمين.</li>
<li>أن أزكي نفسي باستشعار دلائل القدرة الإلهية الواردة في الآيتين.</li>
</ol>
<h2>تمهيد</h2>
<p>بعد بيان الآيات السابقة قدرة الله سبحانه على البعث والنشور؛ أشارت هاتان الآيتان إلى أوهام قريش؛ الذين كانوا يرون في اتباع الرسول ﷺ مذلة ومهانة؛ وتنقيصا من عزتهم التي كانوا يتمتعون بها؛ فقررت الآيتان أن العزة الحقيقية تكون لله سبحانه؛ ثم استدلت على قدرة الله العظيمة على البعث.</p>
<p>فلمن تكون العزة الحقيقية؟ وكيف استدلت الآيتان على وقوع البعث؟</p>
<h2>الآيات</h2>
<p><span>سورة فاطر: 10-11</span></p>
<p>«مَن كَانَ يُرِيدُ ٱلْعِزَّةَ فَلِلَّهِ ٱلْعِزَّةُ جَمِيعًا ۚ إِلَيْهِ يَصْعَدُ ٱلْكَلِمُ ٱلطَّيِّبُ وَٱلْعَمَلُ ٱلصَّٰلِحُ يَرْفَعُهُۥ ۚ وَٱلَّذِينَ يَمْكُرُونَ ٱلسَّيِّـَٔاتِ لَهُمْ عَذَابٌۭ شَدِيدٌۭ ۖ وَمَكْرُ أُو۟لَٰٓئِكَ هُوَ يَبُورُ» [فاطر: 10]</p>
<p>«وَٱللَّهُ خَلَقَكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ جَعَلَكُمْ أَزْوَٰجًۭا ۚ وَمَا تَحْمِلُ مِنْ أُنثَىٰ وَلَا تَضَعُ إِلَّاٰ بِعِلْمِهِۦ ۚ وَمَا يُعَمَّرُ مِن مُّعَمَّرٍۢ وَلَا يُنقَصُ مِنْ عُمُرِهِۦٓ إِلَّاٰ فِىٰ كِتَٰبٍ ۚ إِنَّ ذَٰلِكَ عَلَىٰ ٱللَّهِ يَسِيرٌۭ» [فاطر: 11]</p>
<h2>الفهم</h2>
<h3>الشرح:</h3>
<p>«ٱلْعِزَّةُ»: الشرف والمنعة.</p>
<p>«مَكْرٌ»: ما عُمل على سبيل احتيال وخديعة.</p>
<p>«يَبُورُ»: يهلك ويكسد.</p>
<p>«أَزْوَاجًا»: أصنافا أو ذكرانا وإناثا.</p>
<h3>استخلاص مضامين الآيتين:</h3>
<ol>
<li>لمن تكون العزة الحقيقية؟</li>
<li>ما هي عاقبة من يمكر بالإسلام والمسلمين؟</li>
<li>على ماذا استدل الله تعالى في نهاية الآيتين؟</li>
</ol>
<h2>التفسير</h2>
<p>اشتملت الآيتان على ما يأتي:</p>
<h3>أولا: العزة الحقيقية لله سبحانه:</h3>
<p>بين الله تعالى أن العزة الحقيقية تكون له وحده؛ فقال: «مَن كَانَ يُرِيدُ ٱلْعِزَّةَ فَلِلَّهِ ٱلْعِزَّةُ جَمِيعًا» هذه الآية تحتمل ثلاثة معان:</p>
<p>أحدها: وهو الأظهر؛ من كان يريد نيل العزة فليطلبها من عند الله فإن العزة كلها لله.</p>
<p>والثاني: من كان يريد العزة بمغالبة الإسلام فلله العزة جميعا؛ فالمغالب له مغلوب.</p>
<p>والثالث: من كان يريد أن يعلم لمن العزة فليعلم أن العزة لله جميعا.</p>
<p>وقوله تعالى: «إِلَيْهِ يَصْعَدُ ٱلْكَلِمُ ٱلطَّيِّبُ» بيان لما تطلب به العزة؛ قيل: يعني لا إله إلا الله. واللفظ يعم ذلك وغيره من الذكر والدعاء وتلاوة القرآن وتعليم العلم؛ فالعموم أولى.</p>
<p>وقوله تعالى: «وَٱلْعَمَلُ ٱلصَّٰلِحُ يَرْفَعُهُۥ» فيه ثلاثة أقوال:</p>
<p>أحدها: أن ضمير الفاعل في «يَرْفَعُهُۥ» يعود على الله تعالى؛ وضمير المفعول للعمل الصالح؛ فالمعنى على هذا: أن الله يرفع العمل الصالح؛ أي: يتقبله ويثيب عليه.</p>
<p>والثاني: أن ضمير الفاعل للكلام الطيب؛ وضمير المفعول للعمل الصالح؛ والمعنى على هذا: لا يقبل عمل صالح إلا ممن له كلام طيب؛ وهذا يصح إن قلنا: إن الكلم الطيب هو: لا إله إلا الله؛ لأنه لا يقبل العمل إلا من موحد.</p>
<p>والثالث: أن ضمير الفاعل للعمل الصالح؛ وضمير المفعول للكلم الطيب؛ والمعنى على هذا: أن العمل الصالح هو الذي يرفع الكلم الطيب؛ فلا يقبل الكلم إلا ممن له عمل صالح. وروي هذا المعنى عن ابن عباس، واستبعده ابن عطية، وقال: لم يصح عنه؛ لأن اعتقاد أهل السنة؛ أن الله يتقبل من كل مسلم. قال: وقد يستقيم بأن يتأول أن الله يزيد في رفعه وحسن موقعه.</p>
<h3>ثانيا: تآمر قريش على المسلمين:</h3>
<p>بعد بيان الله تعالى الكلام الطيب؛ بين تآمر قريش على المسلمين؛ فقال سبحانه: «وَٱلَّذِينَ يَمْكُرُونَ ٱلسَّيِّـَٔاتِ لَهُمْ عَذَابٌۭ شَدِيدٌۭ» الإشارة هنا إلى مكر قريش برسول الله ﷺ حين اجتمعوا في دار الندوة وأرادوا أن يقتلوه أو يحبسوه أو يخرجوه. وفعل (مكر) لا يتعدى؛ فتأويله يمكرون المكرات السيئات؛ فتكون السيئات مصدرا؛ أو تضمن يمكرون معنى يكتسبون فتكون السيئات مفعولا.</p>
<p>والمعنى: والذين يمكرون المكرات السيئات بالمسلمين؛ ويتآمرون عليهم؛ لهم عذاب شديد يوم القيامة «وَمَكْرُ أُو۟لَٰٓئِكَ هُوَ يَبُورُ» البوار الهلاك أو الكساد؛ ومعناه هنا: أن مكرهم يبطل ولا ينفعهم.</p>
<h3>ثالثا: إقامة الدليل على البعث ببدء خلق الإنسان:</h3>
<p>في هاتين الآيتين؛ يقيم الحق سبحانه الدليل على البعث ببدء خلق الإنسان؛ فيقول: «وَٱللَّهُ خَلَقَكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ» أي: والله خلق أصلكم الذي هو آدم من تراب؛ ثم خلق ذريته من نطفة؛ وهو الماء الذي يلقى في رحم المرأة «ثُمَّ جَعَلَكُمْ أَزْوَٰجًۭا» أي: جعلكم أصنافا؛ وقيل: ذكرانا وإناثا؛ وهذا أظهر «وَمَا تَحْمِلُ مِنْ أُنثَىٰ وَلَا تَضَعُ إِلَّاٰ بِعِلْمِهِۦ» أي: وما تحمل أنثى؛ ولا تضع مولودها إلا بعلمه تعالى.</p>
<p>وتابع سبحانه ببيان قدرته العظيمة؛ فقال عز وجل: «وَمَا يُعَمَّرُ مِن مُّعَمَّرٍۢ وَلَا يُنقَصُ مِنْ عُمُرِهِۦٓ إِلَّاٰ فِىٰ كِتَٰبٍ» التعمير: طول العمر. والنقص: قصره. والكتاب: اللوح المحفوظ. فإن قيل: إن التعمير والنقص لا يجتمعان لشخص واحد فكيف أعاد الضمير في قوله: «وَلَا يُنقَصُ مِنْ عُمُرِهِۦٓ» على الشخص المعمر؟ فالجواب من ثلاثة أوجه:</p>
<p>الأول وهو الصحيح: أن المعنى ما يعمر من أحد ولا ينقص من عمره؛ إلا في كتاب؛ فوضع من معمر موضع من أحد؛ وليس المراد شخصا واحدا؛ وإنما ذلك كقولك: لا يعاقب الله عبدا ولا يثيبه إلا بحق.</p>
<p>والثاني: أن المعنى لا يزاد في عمر إنسان ولا ينقص من عمره إلا في كتاب؛ وذلك أن يكتب في اللوح المحفوظ؛ أن فلانا إن تصدق فعمره ستون سنة؛ وإن لم يتصدق فعمره أربعون؛ وهذا ظاهر قول رسول الله ﷺ: «وَإِنَّ صِلَةَ الرَّحِمِ تَزِيدُ فِي الْعُمُرِ» [المعجم الأوسط، للطبراني، باب الألف، من اسمه أحمد]؛ إلا أن ذلك مذهب المعتزلة القائلين بالأجلين؛ وليس مذهب الأشعرية؛ وقد قال كعب حين طعن عمر: لو دعا الله لزاد في أجله؛ فأنكر الناس عليه؛ فاحتج بهذه الآية.</p>
<p>والثالث: أن التعمير هو كتب ما يستقبل من العمر؛ والنقص هو كتب ما مضى منه في اللوح المحفوظ وذلك حق كل شخص.</p>
<p>ثم بين الله تعالى أن ذلك يسير عليه فقال: «إِنَّ ذَٰلِكَ عَلَىٰ ٱللَّهِ يَسِيرٌۭ» قال ابن عجيبة رحمه الله؛ في معنى هذه الآية: إن «إحصاء الأعمار؛ أو زيادتها ونقصانها؛ سهل على علم الله وقدرته» [البحر المديد لابن عجيبة: 525/4].</p>
<h3>رابعا: مقاصد الآيتين:</h3>
<p>تسعى الآيتان إلى تحقيق مقاصد تربوية؛ منها:</p>
<ul>
<li>تقرير الله تعالى انفراده بالعزة؛ فالعزيز هو الذي أعزه الله.</li>
<li>الدعوة إلى لزوم الحكمة في القول والعمل؛ ذلك أن الكلم الطيب والعمل الصالح هو الذي يقبل عنده سبحانه.</li>
<li>بيان قدرته عز وجل في ابتداء خلق الإنسان بمراحل مختلفة؛ ليستدل بذلك على وقوع البعث وما بعده يوم القيامة.</li>
</ul>
<h2>التقويم</h2>
<ol>
<li>ما علاقة الكلم الطيب والعمل الصالح بالعزة؟</li>
<li>هل أثر مكر قريش بالإسلام والمسلمين؟ ولماذا؟</li>
<li>أستدل من خلال آيات الأنفس على بعث الناس يوم القيامة؟</li>
</ol>
<h2>الاستثمار</h2>
<p>قال الطاهر بن عاشور في تفسير قوله تعالى: «وَٱلَّذِينَ يَمْكُرُونَ ٱلسَّيِّـَٔاتِ لَهُمْ عَذَابٌۭ شَدِيدٌۭ»: «وَالْمَكْرُ: تَدْبِيرُ إِلْحَاقِ الضَّرِّ بِالْغَيْرِ فِي خُفْيَةٍ لِئَلَّا يَأْخُذَ حِذْرَهُ، وَفِعْلُهُ قَاصِرٌ. وَهُوَ يَتَعَلَّقُ بِالْمَضْرُورِ بِوَاسِطَةِ الْبَاءِ الَّتِي لِلْمُلَابَسَةِ، يُقَالُ: مَكَرَ بِفُلَانٍ، وَيَتَعَلَّقُ بِوَسِيلَةِ الْمَكْرِ بِبَاءِ السَّبَبِيَّةِ يُقَالُ: مَكَرَ بِفُلَانٍ بِقَتْلِهِ فَانْتِصَابُ السَّيِّئَاتِ هُنَا عَلَى أَنَّهُ وَصْفٌ لِمَصْدَرِ الْمَكْرِ نَائِبًا مَنَابَ الْمَفْعُولِ الْمُطْلَقِ الْمُبَيِّنِ لِنَوْعِ الْفِعْلِ فَكَأَنَّهُ قِيلَ وَالَّذِينَ يمكرون الْمَكْر السيّء. وَكَانَ حَقُّ وَصْفِ الْمَصْدَرِ أَنْ يَكُونَ مُفْرَدًا كَقَوْلِهِ تَعَالَى: «وَلَا يَحِيقُ ٱلْمَكْرُ ٱلسَّيِّئُ إِلَّا بِأَهْلِهِۦ» [فاطر: 43] فَلَمَّا أُرِيدَ هُنَا التَّنْبِيهُ عَلَى أَنَّ أَوْلِيَاءَ الشَّيْطَانِ لَهُمْ أَنْوَاعٌ مِنَ الْمَكْرِ، عُدِلَ عَنِ الْإِفْرَادِ إِلَى الْجَمْعِ وَأُتِيَ بِهِ جَمْعَ مُؤَنَّثٍ لِلدَّلَالَةِ عَلَى مَعْنَى الْفَعَلَاتِ مِنَ الْمَكْرِ، فَكُلُّ وَاحِدَةٍ مِنْ مَكْرِهِمْ هِيَ سَيِّئَةٌ، كَمَا جَاءَ ذَلِكَ فِي لَفْظِ (صَالِحَةٍ) كَقَوْلِ جَرِيرٍ:</p>
<p>كَيْفَ الْهِجَاءُ وَمَا تَنْفَكُّ صَالِحَةٌ *** مِنْ آلِ لأْمٍ بِظَهْرِ الْغَيْبِ تَأْتِينِي</p>
<p>أَيْ صَالِحَاتٌ كَثِيرَةٌ. وَأَنْوَاعُ مَكَرَاتِهِمْ هِيَ مَا جَاءَ فِي قَوْلِهِ تَعَالَى: «وَإِذْ يَمْكُرُ بِكَ ٱلَّذِينَ كَفَرُوا۟ لِيُثْبِتُوكَ أَوْ يَقْتُلُوكَ أَوْ يُخْرِجُوكَ» [الأنفال: 30].</p>
<p>[التحرير والتنوير، للطاهر بن عاشور: 274/22].</p>
<p>أتأمل النص وأجيب عن الآتي:</p>
<ol>
<li>أوضح العلاقة بين الآيتين الواردتين في النص.</li>
<li>أبين سبب وصف المصدر المحذوف (المكر) بالجمع (السيئات).</li>
</ol>
<h2>الإعداد القبلي</h2>
<p>أتأمل الآيات: 12-14 من سورة فاطر وأجيب عن الآتي:</p>
<ol>
<li>أبحث عن مدلولات العبارات الآتية: «عَذْبٌ فُرَاتٌ» - «سَآئِغٌ شَرَابُهُ» - «مِلْحٌ أُجَاجٌ» - «لَحْمًا طَرِيًّا» - «حِلْيَةً تَلْبَسُونَهَا» - «مَوَاخِرَ» - «قِطْمِيرٍ».</li>
<li>أبحث في معاني الآيات عما يدل على استحقاق الله وحده للعبادة.</li>
</ol>"""

HTML_FR = """<h1> Sourate Fāṭir, versets 10-11 : livre du Tafsīr à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy, deuxième année collégiale — leçon 4</h1>
<p>Leçon sur l’exégèse de la sourate Fāṭir, versets 10 et 11, du livre du Tafsīr fondé sur le <em>Tashīl li-ʿulūm al-tanzīl</em> d’Ibn Juzayy, pour la deuxième année de l’enseignement collégial traditionnel (leçon 4).</p>
<ol>
<li>Que je distingue les causes de l’accession de l’homme à la gloire.</li>
<li>Que je déduise le sort de ceux qui trament des ruses contre l’islam et les musulmans.</li>
<li>Que je purifie mon âme par la conscience des indices de la puissance divine contenus dans les deux versets.</li>
</ol>
<h2>Introduction (tamhīd)</h2>
<p>Après que les versets précédents ont exposé la puissance d’Allah — exalté soit-Il — sur la résurrection et le rassemblement, ces deux versets font allusion aux illusions de Qurayš, qui voyaient dans la suite du Messager ﷺ une humiliation et un avilissement, et une atteinte à la gloire dont ils jouissaient ; les deux versets ont alors établi que la vraie gloire appartient à Allah — exalté soit-Il —, puis ont produit la preuve de l’immense puissance d’Allah sur la résurrection.</p>
<p>À qui appartient donc la vraie gloire ? Et comment les deux versets ont-ils établi la preuve de la survenance de la résurrection ?</p>
<h2>Les versets</h2>
<p><span>Sourate Fāṭir, versets 10 et 11</span></p>
<p>« Quiconque veut la gloire — qu’il la demande à Allah, car à Allah appartient la gloire tout entière. Vers Lui monte la bonne parole, et l’œuvre bonne, c’est Lui qui l’élève. Et ceux qui trament les mauvaises actions ont un châtiment dur ; et la ruse de ceux-là est vouée à périr » (10).</p>
<p>« Et Allah vous a créés de terre, puis d’une goutte de sperme ; puis Il vous a faits par couples. Aucune femelle ne conçoit ni ne met bas sans Sa science ; et nul n’est doté de longévité, ni rien retranché de son existence, sans que cela soit consigné dans un Livre. Cela est certes facile pour Allah » (11).</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>« al-ʿizza » (la gloire) : l’honneur et l’invulnérabilité.</p>
<p>« makr » (la ruse) : ce qui est ourdi par tromperie et fraude.</p>
<p>« yabūr » (il périt) : il s’anéantit et se déprécie.</p>
<p>« azwāǧan » (par couples) : par catégories, ou mâles et femelles.</p>
<h3>Extraction des contenus des deux versets</h3>
<ol>
<li>À qui appartient la vraie gloire ?</li>
<li>Quel est le sort de celui qui tracte contre l’islam et les musulmans ?</li>
<li>Sur quoi Allah — exalté soit-Il — a-t-Il produit la preuve à la fin des deux versets ?</li>
</ol>
<h2>Le Tafsīr</h2>
<p>Ces deux versets comprennent ce qui suit :</p>
<h3>Premièrement : la vraie gloire appartient à Allah — exalté soit-Il</h3>
<p>Allah — exalté soit-Il — a exposé que la vraie gloire Lui appartient à Lui seul, et a dit : « Quiconque veut la gloire — qu’il la demande à Allah, car à Allah appartient la gloire tout entière ». Ce verset comporte trois sens. Le premier — et c’est le plus apparent : quiconque veut obtenir la gloire, qu’il la demande auprès d’Allah, car la gloire tout entière est à Allah. Le deuxième : quiconque veut la gloire en combattant l’islam — à Allah appartient la gloire tout entière, et celui qui Le combat est vaincu. Le troisième : quiconque veut savoir à qui appartient la gloire, qu’il sache que la gloire appartient tout entière à Allah.</p>
<p>Et Sa parole — exalté soit-Il : « Vers Lui monte la bonne parole » explicite ce par quoi la gloire se demande ; on a dit : cela désigne l’ilāha illā llāh (il n’est de dieu qu’Allah). Et le vocable englobe cela et autre chose encore — le rappel, l’invocation, la récitation du Coran et l’enseignement de la science : la généralité est donc préférable.</p>
<p>Et Sa parole — exalté soit-Il : « et l’œuvre bonne, c’est Lui qui l’élève » comporte trois avis. Le premier : le pronom sujet de « Il l’élève » (yarfaʿuhū) renvoie à Allah — exalté soit-Il —, et le pronom objet à l’œuvre bonne ; le sens, dès lors, est qu’Allah élève l’œuvre bonne, c’est-à-dire l’agrée et la rétribue. Le deuxième : le pronom sujet renvoie à la bonne parole, et le pronom objet à l’œuvre bonne ; le sens, dès lors, est : nulle œuvre bonne n’est agréée sinon de celui dont la parole est bonne — ce qui vaut si nous posons que la bonne parole est l’ilāha illā llāh, car l’œuvre n’est agréée que de l’unitarien. Le troisième : le pronom sujet renvoie à l’œuvre bonne, et le pronom objet à la bonne parole ; le sens, dès lors, est que l’œuvre bonne est ce qui élève la bonne parole, et que la parole n’est agréée que de celui dont l’œuvre est bonne. Ce sens a été rapporté d’Ibn ʿAbbās ; Ibn ʿAṭiyya l’a jugé peu vraisemblable et a dit : il n’est pas authentique de lui, car le credo des gens de la Sunna est qu’Allah agrée [l’œuvre] de tout musulman. Il dit : et cela peut se tenir si l’on pose qu’Allah accroît son élévation et la beauté de sa réception.</p>
<h3>Deuxièmement : le complot de Qurayš contre les musulmans</h3>
<p>Après qu’Allah — exalté soit-Il — a exposé la bonne parole, Il a exposé le complot de Qurayš contre les musulmans, et a dit — exalté soit-Il : « Et ceux qui trament les mauvaises actions ont un châtiment dur » : l’allusion vise ici la ruse de Qurayš contre le Messager d’Allah ﷺ, lorsqu’ils se réunirent à Dār an-Nadwa (la maison du conseil) et voulurent le tuer, l’emprisonner ou le bannir. Le verbe makara est intransitif ; son interprétation est : « ils trament les ruses mauvaises », sayyiʾāt étant alors un nominal (maṣdar) ; ou bien yamkurūna a le sens de yaktasibūna (« ils acquièrent »), et sayyiʾāt est alors un objet.</p>
<p>Le sens est : ceux qui trament les ruses mauvaises contre les musulmans et conspirent contre eux ont, au Jour de la résurrection, un châtiment dur. « Et la ruse de ceux-là est vouée à périr » : le bawār est l’anéantissement ou la dépréciation ; son sens ici est que leur ruse s’annule et ne leur profite pas.</p>
<h3>Troisièmement : la production de la preuve de la résurrection par la création initiale de l’homme</h3>
<p>Dans ces deux versets, le Vrai — exalté soit-Il — produit la preuve de la résurrection par la création initiale de l’homme, disant : « Et Allah vous a créés de terre, puis d’une goutte de sperme » : c’est-à-dire qu’Allah a créé votre origine, qui est Adam, de terre, puis a créé sa descendance d’une goutte — l’eau qui est déposée dans la matrice de la femme. « Puis Il vous a faits par couples » : c’est-à-dire : Il vous a faits par catégories ; on a dit aussi : mâles et femelles — et c’est le plus apparent. « Aucune femelle ne conçoit ni ne met bas sans Sa science » : c’est-à-dire qu’aucune femelle ne conçoit et ne met au monde son enfant sans la science d’Allah — exalté soit-Il.</p>
<p>Et Il a poursuivi en exposant Sa puissance immense, disant — le Puissant, le Majestueux : « Et nul n’est doté de longévité, ni rien retranché de son existence, sans que cela soit consigné dans un Livre » : la longévité (taʿmīr) est la longueur de l’existence ; la diminution (naqṣ), sa brièveté ; et le Livre est la Tablette gardée. Si l’on objecte que la longévité et la diminution ne se rencontrent pas chez une même personne, comment a-t-il réintroduit le pronom dans Sa parole « ni rien retranché de son existence » sur la personne dotée de longévité ? La réponse se fait de trois manières.</p>
<p>La première — et c’est la correcte : le sens est : nul n’est doté de longévité, ni rien retranché de son existence, sans que cela soit dans un Livre ; on a mis muʿammar (« celui qui est doté de longévité ») à la place de aḥad (« quiconque »), et l’intention n’est pas une personne unique : cela est comme ton dire : Allah ne châtie ni ne rétribue un serviteur qu’à bon droit.</p>
<p>La deuxième : le sens est : rien n’est ajouté à l’existence d’un homme, ni retranché de son existence, sans que cela soit dans un Livre ; cela consiste à écrire sur la Tablette gardée : « un tel, s’il fait l’aumône, aura soixante ans ; s’il ne la fait pas, quarante » — et c’est le sens apparent de la parole du Messager d’Allah ﷺ : « Et certes, le maintien des liens de parenté accroît l’existence » [al-Muʿǧam al-awsaṭ, d’al-Ṭabarānī ; chapitre de l’alif — celui qui porte le nom d’Aḥmad] ; sauf que cela est l’école des muʿtazilites, tenants des deux termes (al-ğalayn), et non celle des ašʿarites ; et Kaʿb a dit, quand ʿUmar fut poignardé : « S’il invoquait Allah, Il accroîtrait son terme » — les gens le lui reprochèrent, et il fit valoir ce verset.</p>
<p>La troisième : la longévité est l’inscription de ce qui vient de l’existence, et la diminution l’inscription de ce qui en est déjà passé, sur la Tablette gardée — et cela vaut pour toute personne.</p>
<p>Puis Allah — exalté soit-Il — a exposé que cela Lui est aisé, disant : « Cela est certes facile pour Allah ». Ibn ʿAǧība — qu’Allah lui fasse miséricorde — a dit, sur le sens de ce verset : « Le décompte des existences, ou leur accroissement et leur diminution, est aisé à la science d’Allah et à Sa puissance » [al-Baḥr al-madīd, d’Ibn ʿAǧība : 525/4].</p>
<h3>Quatrièmement : les finalités des deux versets</h3>
<p>Les deux versets visent la réalisation de nombreuses finalités éducatives, parmi lesquelles :</p>
<ul>
<li>L’établissement par Allah — exalté soit-Il — de Son exclusivité dans la gloire : le glorieux est celui qu’Allah a rendu glorieux.</li>
<li>L’appel à s’en tenir à la sagesse dans la parole et l’action : c’est la bonne parole et l’œuvre bonne qui sont agréées auprès de Lui — exalté soit-Il.</li>
<li>L’exposé de Sa puissance — le Puissant, le Majestueux — dans la création initiale de l’homme par des étapes diverses, pour en produire la preuve de la survenance de la résurrection et de ce qui la suit au Jour de la résurrection.</li>
</ul>
<h2>L’évaluation</h2>
<ol>
<li>Quel est le lien de la bonne parole et de l’œuvre bonne avec la gloire ?</li>
<li>La ruse de Qurayš contre l’islam et les musulmans a-t-elle eu un effet ? Et pourquoi ?</li>
<li>Je produis la preuve, à partir des versets portant sur les personnes, de la résurrection des hommes au Jour de la résurrection.</li>
</ol>
<h2>L’exploitation (istiṯmār)</h2>
<p>Aṭ-Ṭāhir Ibn ʿĀšūr a dit, dans son exégèse de Sa parole — exalté soit-Il : « Et ceux qui trament les mauvaises actions ont un châtiment dur » : « La ruse (makr) est la combinaison visant à faire subir un dommage à autrui en secret, pour qu’il n’en prenne pas sa garde ; son verbe est intransitif. Il se rapporte à la personne lésée par l’intermédiaire du bāʾ de circumlocution : on dit makara bi-fulān ("il a rusé contre un tel") ; et il se rapporte au moyen de la ruse par le bāʾ de causalité : on dit makara bi-fulān bi-qatlihi ("il a rusé contre un tel en le tuant"). La mise à l’accusatif de as-sayyiʾāt, ici, tient à ce qu’il est une qualification du nominal (maṣdar) de makr, tenant lieu de complément d’objet absolu précisant l’espèce de l’action — c’est comme s’il avait été dit : "et ceux qui trament la ruse mauvaise". Or il revenait à la qualification du nominal d’être au singulier, selon Sa parole — exalté soit-Il : « et la ruse mauvaise ne rejaillit que sur ses auteurs » [Fāṭir : 43]. Mais lorsqu’on a voulu, ici, avertir que les alliés de Satan ont des espèces multiples de ruse, on a délaissé le singulier pour le pluriel, et on l’a amené au pluriel féminin pour marquer le sens des "actions" de la ruse : chacune de leurs ruses est une action mauvaise, comme il en est du vocable ṣāliḥa ("une bonne action"), selon la parole de Ǧarīr :</p>
<p>Comment le blâme (higāʾ), alors que ne cesse de me venir, en mon absence, une bienfaisante des gens de Laʾmm ?</p>
<p>— c’est-à-dire : des bienfaisances nombreuses. Et les espèces de leurs ruses sont ce qui est venu dans Sa parole — exalté soit-Il : « Et quand ceux qui ont mécru complotaient contre toi, pour t’emprisonner, te tuer ou te bannir » [al-Anfāl : 30]. » [at-Taḥrīr wa-t-tanwīr, d’Aṭ-Ṭāhir Ibn ʿĀšūr : 274/22].</p>
<p>Je médite le texte et je réponds à ce qui suit :</p>
<ol>
<li>J’explicite le rapport entre les deux versets cités dans le texte.</li>
<li>J’explicite la raison de la qualification du nominal sous-entendu (la ruse) par le pluriel (les mauvaises actions).</li>
</ol>
<h2>La préparation préalable (iʿdād qablī)</h2>
<p>Je médite les versets 12 à 14 de la sourate Fāṭir et je réponds à ce qui suit :</p>
<ol>
<li>Je recherche la valeur des expressions suivantes : « ʿaḏbun furātun » (douce et douceâtre) — « sāʾiġun šarābuhū » (dont la boisson descend aisément dans la gorge) — « milḥun uǧāǧun » (salée et âcre) — « laḥman ṭariyyan » (une chair fraîche) — « ḥil’yatan talbasūnahā » (une parure que vous portez) — « mawāḫira » (navires) — « qiṭmīr » (la pellicule fine qui enveloppe le noyau de datte).</li>
<li>Je recherche, dans les sens des versets, ce qui indique qu’Allah seul mérite l’adoration.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if str(l.get("docId", "")).endswith("-559"):
            l["html"] = HTML_AR
            l["htmlFr"] = HTML_FR
            l["pdfOnly"] = False
            # titre catalogue confirmé correct : «الآيتان : 10 - 11» (leçon de
            # 2 versets — citation imprimée [سورة فاطر: 11-10] + CMS 16812)
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 559 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 559 livrée: AR {len(HTML_AR)} car + FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
