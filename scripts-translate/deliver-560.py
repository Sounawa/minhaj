#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Livraison de la leçon 560 (سورة فاطر 12-14, الدرس 5, R101-WARSH).

Vérifications R101 (méthode Warsh e-verification + croisement CMS 16823 + GT) :
- BLOC v12-14 : squelette tanzil Warsh du quran-cache s35 (Fāṭir = 45 versets
  dans les deux comptages, aucun décalage — confirmé R99/R100 pour v4-11).
- GLOSSAIRE 7 entrées (règle d'or 6/6 : idad de 559 = الشرح de 560 — termes
  craqués en R100 par ink-runs + OCR focal) : «عَذْبٌ فُرَاتٌ»=شديد العذوبة /
  «سَآئِغٌ شَرَابُهُ»=مريء يسهل انحداره في الحلق / «مِلْحٌ أُجَاجٌ»=شديد الملوحة /
  «لَحْمًا طَرِيًّا»=السمك / «حِلْيَةً»=اللؤلؤ والمرجان / «مَوَاخِرَ»=جمع ماخرة وهي
  السفينة / «قِطْمِيرٍ»=القشر الرقيق الأبيض الذي على نوى التمر.
- IDAD 560 (pour 561, فاطر 15-18) VÉROUILLÉ ce tour par OCR 561 frais
  (615-11.PDF, 7 pages) : le الشرح de 561 imprimé p2 donne les 5 defs
  (المحتاجون إليه في كل حال / الغني عن سائر خلقه؛ المحمود... / مثقلة بأوزارها
  حتى لم تقدر على المشي / لا تجد من يستجيب لها ويحمل عنها بعض ذنبها / طهر
  نفسه من الشرك والمعاصي) = les 5 termes «ٱلْفُقَرَآءُ» - «ٱلْغَنِيُّ ٱلْحَمِيدُ» -
  «مُثْقَلَةٌ» - «تَدْعُ» - «تَزَكَّىٰ» (croisés CMS 16839 GT : Al-fuqarāʾ /
  Al-Ghanī al-Ḥamīd / Muthqala / Tadʿū / Tazakkā — garbles 560 p7
  «الْجْغْراء»=فقراء [ف→ج ق→غ] et «متْفْلَة»=مثقلة [ق→ف] conformes).
- CITATIONS inter-sourates : [الأنعام: 131] contenu = Ḥafṣ 130 «يَٰمَعْشَرَ
  ٱلْجِنِّ وَٱلْإِنسِ أَلَمْ يَأْتِكُمْ رُسُلٌۭ مِّنكُمْ» (garble «جِامَخَرَأ وإ نِمْيَابِكُم
  يلجم» = يَامَعْشَرَ + وَالْإِنسِ أَلَمْ يَأْتِكُمْ lettre à lettre ; numérotation
  médinoise du muṣḥaf scolaire — transcription TELLE QU'IMPRIMÉE, aucun NdT
  comparative, directive Warsh-only R96) ; [الأحقاف: 4-5] = les deux versets
  ENTIERS (garbles + GT-CMS concordants) ; [مريم: 82-83] contenu = Ḥafṣ 81-82
  «وَٱتَّخَذُوا۟ مِن دُونِ ٱللَّهِ ءَالِهَةًۭ...ضِدًّۭا» (garble «واقتذوايى حو الله
  #الهة ليضونرا نهم» = واتخذوا من دون الله آلهة ليكونوا لهم عزا + «كلك مكبر
  بجا ةتهة كرفو َلتِهِرضناً» = كلا سيكفرون بعبادتهم ويكونون عليهم ضدا).
- ALŪSĪ [روح المعاني: 353/11 بتصرف] : comparaison Naḥl 14 ↔ Fāṭir 12 —
  6 slots Quran reconstitués : (a) «وَتَرَى ٱلْفُلْكَ مَوَاخِرَ فِيهِ
  وَلِتَبْتَغُوا۟ مِن فَضْلِهِۦ» [النحل: 14] AVEC wāw (garbles «وكرى َلك
  مَوَأخِرَقةة» + «(َلتتتَكُوا») ; (b) «فِيهِ» après «وَتَأْخِيرِ» ; (c) «وَإِن
  تَعُدُّوا۟ نِعْمَةَ ٱللَّهِ لَا تُحْصُوهَا» [النحل: 18] (garble «ولى تَحْدٌواًنمْمة
  الل اتتُتْحُومَاً») ; (d) «فِيهِ» après «فَقَدَّمَ» (garble «(8ية» — la ﴿ du CMS
  est le crochet ouvrant, le «في» du CMS/OCR = le crochet mal lu) ; (e)
  «وَلِتَبْتَغُوا۟» بالواو ; (f) «لِتَبْتَغُوا۟ مِن فَضْلِهِۦ» SANS wāw (Fāṭir).
- Tashīl : [التسهيل: 1/423] (مواخر — «جمع ماخرة، يقال: مخرت السفينة...») ;
  [التسهيل: 2/140] (يولج — «يدخل كلا منهما في الآخر...»).
- Titre catalogue confirmé : «الآيات : 12 - 14» = citation imprimée
  [سورة فاطر: 14-12] (convention RTL, nombre de droite = début).
- Injection : AR ~7900 + FR ~12300 car. Registre hand +1 (479 main).
"""

import json
import sys

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"
TMP = "/home/z/my-project/tr-tmp/pdf-mut23h33-560.html"

HTML_AR = """<h1>سورة فاطر (الآيات: 12-14): كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي للسنة الثانية إعدادي الدرس 5</h1>
<p>درس في تفسير سورة فاطر الآيات (12-14)، كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي، للسنة الثانية من التعليم الإعدادي العتيق (الدرس 5).</p>
<ol>
<li>أن أتعرف على المظاهر الكونية المضمنة في الآيات.</li>
<li>أن أستدل على استحقاق الله تعالى وحده للعبادة.</li>
<li>أن أشكر الله تعالى على نعمه التي حبانا بها.</li>
</ol>
<h2>تمهيد</h2>
<p>بعد استدلال الآيات السابقة على تفرده سبحانه بالإلهية بآيات الأنفس؛ واصلت هذه الآيات استدلالها على ذلك بمظاهر أخرى من الظواهر الكونية، المتمثلة في البحار والليل والنهار والشمس والقمر، ثم أبطلت ما يعبده المشركون من دون الله، موضحة أن تلك المعبودات لا تنفع نفسها ولا غيرها.</p>
<p>فما هي مظاهر آيات الله الكونية الواردة في الآيات؟ وكيف أستدل من خلالها على استحقاق الله وحده للعبادة؟</p>
<h2>الآيات</h2>
<p>قال الله تعالى:</p>
<p><span>سورة فاطر: 12 - 14</span></p>
<p>«وَمَا يَسْتَوِى ٱلْبَحْرَانِ هَٰذَا عَذْبٌۭ فُرَاتٌۭ سَآئِغٌۭ شَرَابُهُۥ وَهَٰذَا مِلْحٌ أُجَاجٌۭ ۖ وَمِن كُلٍّۢ تَأْكُلُونَ لَحْمًۭا طَرِيًّۭا وَتَسْتَخْرِجُونَ حِلْيَةًۭ تَلْبَسُونَهَا ۖ وَتَرَى ٱلْفُلْكَ فِيهِ مَوَاخِرَ لِتَبْتَغُوا۟ مِن فَضْلِهِۦ وَلَعَلَّكُمْ تَشْكُرُونَ» [فاطر: 12]</p>
<p>«يُولِجُ ٱلَّيْلَ فِى ٱلنَّهَارِ وَيُولِجُ ٱلنَّهَارَ فِى ٱلَّيْلِ وَسَخَّرَ ٱلشَّمْسَ وَٱلْقَمَرَ كُلٌّۭ يَجْرِى لِأَجَلٍۢ مُّسَمًّۭى ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ لَهُ ٱلْمُلْكُ ۚ وَٱلَّذِينَ تَدْعُونَ مِن دُونِهِۦ مَا يَمْلِكُونَ مِن قِطْمِيرٍ» [فاطر: 13]</p>
<p>«إِن تَدْعُوهُمْ لَا يَسْمَعُوا۟ دُعَآءَكُمْ وَلَوْ سَمِعُوا۟ مَا ٱسْتَجَابُوا۟ لَكُمْ ۖ وَيَوْمَ ٱلْقِيَٰمَةِ يَكْفُرُونَ بِشِرْكِكُمْ ۚ وَلَا يُنَبِّئُكَ مِثْلُ خَبِيرٍۢ» [فاطر: 14]</p>
<h2>الفهم</h2>
<h3>الشرح:</h3>
<p>«عَذْبٌ فُرَاتٌ»: شديد العذوبة.</p>
<p>«سَآئِغٌ شَرَابُهُ»: مريء يسهل انحداره في الحلق.</p>
<p>«مِلْحٌ أُجَاجٌ»: شديد الملوحة.</p>
<p>«لَحْمًا طَرِيًّا»: السمك.</p>
<p>«حِلْيَةً»: اللؤلؤ والمرجان.</p>
<p>«مَوَاخِرَ»: جمع ماخرة وهي السفينة.</p>
<p>«قِطْمِيرٍ»: القشر الرقيق الأبيض الذي على نوى التمر.</p>
<h3>استخلاص مضامين الآيات:</h3>
<ol>
<li>ما هي الآيات الكونية الواردة في الآيات؟</li>
<li>علام استدل الله تعالى بتلك الآيات الكونية؟</li>
</ol>
<h2>التفسير</h2>
<p>اشتملت هذه الآيات على ما يأتي:</p>
<h3>أولا: بعض مظاهر آيات الله الكونية:</h3>
<p>بعد الاستدلال على وقوع البعث يوم القيامة؛ بين في هذه الآيات بعض الأدلة على قدرته وعظمته في خلقه الأشياء المختلفة مع اتحاد منفعتها للإنسان. فقال سبحانه: «وَمَا يَسْتَوِى ٱلْبَحْرَانِ هَٰذَا عَذْبٌۭ فُرَاتٌۭ سَآئِغٌۭ شَرَابُهُۥ وَهَٰذَا مِلْحٌ أُجَاجٌۭ» أي: هذان البحران لا يتعادلان؛ أحدهما: فرات بالغ العذوبة حتى يضرب إلى الحلاوة، والثاني: ملح يحرق بملوحته ويجمع إلى ذلك المرارة؛ والقصد بالآية: التنبيه على قدرة الله ووحدانيته وإنعامه على عباده.</p>
<p>ثم بين سبحانه وجوه انتفاع الناس بالبحرين العذب والملح؛ فقال عز وجل: «وَمِن كُلٍّۢ تَأْكُلُونَ لَحْمًۭا طَرِيًّۭا» هذا استطراد في صفة البحرين وما فيهما من النعم؛ أي: ومن كلا البحرين تأكلون سمكاً غضاً طرياً «وَتَسْتَخْرِجُونَ حِلْيَةًۭ تَلْبَسُونَهَا» أي: وتستخرجون منهما الجوهر والمرجان للزينة والتحلي. فإن قيل: إن الحلية لا تخرج إلا من البحر الملح دون العذب؛ فكيف قال: «وَمِن كُلٍّۢ» أي: من كل واحد منهما؟ فالجواب من ثلاثة أوجه:</p>
<p>الأول: أن ذلك تجوّز في العبارة كما قال: «يَٰمَعْشَرَ ٱلْجِنِّ وَٱلْإِنسِ أَلَمْ يَأْتِكُمْ رُسُلٌۭ مِّنكُمْ» [الأنعام: 131] والرسل إنما هي من الإنس.</p>
<p>الثاني: أن المرجان إنما يوجد في البحر الملح حيث تنصب أنهار الماء العذب، أو ينزل المطر فلما كانت الأنهار والمطر وهي البحر العذب تنصب في البحر الملح كان الإخراج منهما جميعا.</p>
<p>الثالث: زعم قوم أنه يخرج اللؤلؤ والمرجان من الملح والعذب، وهذا قول يبطله الحس، أي: الواقع.</p>
<p>وقوله تعالى: «وَتَرَى ٱلْفُلْكَ فِيهِ مَوَاخِرَ»: «جمع ماخرة، يقال: مخرت السفينة. والمخر: شق الماء، وقيل: صوت جري الفلك بالرياح» [التسهيل: 1/423]. «لِتَبْتَغُوا۟ مِن فَضْلِهِۦ وَلَعَلَّكُمْ تَشْكُرُونَ» أي: سخر لكم البحر لتبتغوا فضل الله بأنواع التجارات وغيرها، ولتشكروا ربكم على نعمه وفضله بأن سخر لكم ذلك.</p>
<p>ثم استمرت الآيات تعرض مظاهر قدرة الله تعالى في الآفاق؛ فقال سبحانه: «يُولِجُ ٱلَّيْلَ فِى ٱلنَّهَارِ وَيُولِجُ ٱلنَّهَارَ فِى ٱلَّيْلِ» أي: يدخل كلا منهما في الآخر بما يزيد في أحدهما وينقص من الآخر، أو بإدخال ظلمة الليل على ضوء النهار وإدخال ضوء النهار على ظلمة الليل. [التسهيل: 2/140].</p>
<p>ثم بين سبحانه أنه سخر الشمس والقمر بقدرته وإرادته؛ فقال عز وجل: «وَسَخَّرَ ٱلشَّمْسَ وَٱلْقَمَرَ» أي: ذلَّل الشمس والقمر لصالح العباد. فكل منهما يسير في فلكه إلى يوم القيامة.</p>
<h3>ثانيا: دليل استحقاق الله تعالى للعبادة دون غيره:</h3>
<p>بعد بيانه تعالى مشاهد من تجليات قدرته وعلمه وحكمته ولطفه ورحمته؛ خاطب الناس بقوله: «ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ لَهُ ٱلْمُلْكُ» أي: ذلكم الذي فعل الأمور المتقدمة، هو ربكم الذي لا رب سواه ولا معبود بحق إلا هو، له المُلك والعظمة والسلطان.</p>
<p>ثم بين سبحانه أن ما يعبده المشركون من دونه لا يستحق العبادة لأن تلك المعبودات فقيرة لا تملك شيئا، فقال سبحانه: «وَٱلَّذِينَ تَدْعُونَ مِن دُونِهِۦ مَا يَمْلِكُونَ مِن قِطْمِيرٍ» القطمير: هو القشر الرقيق الأبيض الذي على نوى التمر، والمعنى أن الأصنام لا يملكون أقل الأشياء كمقدار القطمير، فكيف أكثرها.</p>
<p>وقد عزز الله تعالى ضعف الأصنام وعجزها بقوله: «إِن تَدْعُوهُمْ لَا يَسْمَعُوا۟ دُعَآءَكُمْ» أي: إن تدعوا هذه المعبودات من دون الله، لا يسمعوا دعاءكم «وَلَوْ سَمِعُوا۟ مَا ٱسْتَجَابُوا۟ لَكُمْ» أي: ولو سمعوا على سبيل الفرض ما استجابوا لكم؛ لأنها جمادات لا حس لها، ولا قدرة لها على النفع «وَيَوْمَ ٱلْقِيَٰمَةِ يَكْفُرُونَ بِشِرْكِكُمْ» أي: بإشراككم؛ فالمصدر مضاف للفاعل.</p>
<p>ونظير هذا، قوله تعالى: «قُلْ أَرَءَيْتُم مَّا تَدْعُونَ مِن دُونِ ٱللَّهِ أَرُونِى مَاذَا خَلَقُوا۟ مِنَ ٱلْأَرْضِ أَمْ لَهُمْ شِرْكٌۭ فِى ٱلسَّمَٰوَٰتِ ۖ ٱتُونِى بِكِتَٰبٍۢ مِّن قَبْلِ هَٰذَآ أَوْ أَثَٰرَةٍۢ مِّنْ عِلْمٍ إِن كُنتُمْ صَٰدِقِينَ وَمَنْ أَضَلُّ مِمَّن يَدْعُوا۟ مِن دُونِ ٱللَّهِ مَن لَّا يَسْتَجِيبُ لَهُۥٓ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ وَهُمْ عَن دُعَآئِهِمْ غَٰفِلُونَ» [الأحقاف: 4-5]. وقوله سبحانه: «وَٱتَّخَذُوا۟ مِن دُونِ ٱللَّهِ ءَالِهَةًۭ لِّيَكُونُوا۟ لَهُمْ عِزًّۭا كَلَّا ۚ سَيَكْفُرُونَ بِعِبَادَتِهِمْ وَيَكُونُونَ عَلَيْهِمْ ضِدًّۭا» [مريم: 82-83]. «وَلَا يُنَبِّئُكَ مِثْلُ خَبِيرٍۢ» أي: لا يخبرك بالأمر مخبر مثل مخبر عالم به، يعني نفسه تعالى في إخباره أن الأصنام تكفر يوم القيامة بمن عبدها.</p>
<h3>ثالثا: مقاصد الآيات:</h3>
<p>ترشد هذه الآيات في عمومها إلى عدة مقاصد، منها:</p>
<ul>
<li>بيان فضل الله تعالى وإنعامه على عباده بمختلف أصناف النعم، فقد سخر سبحانه لعباده البحر وما يشتمل عليه من خيرات، وسخر لهم الليل والنهار، والشمس والقمر.</li>
<li>الحث على إخلاص العبادة لله تعالى وحده دون سواه، إذ هو المستحق للعبادة دون غيره من المعبودات الباطلة التي لا تملك لنفسها نفعا ولا ضرا، فضلا أن تملكه لغيرها.</li>
</ul>
<h2>التقويم</h2>
<ol>
<li>أستنتج الغاية من امتنان الله تعالى على عباده بالنعم الواردة في الآيات.</li>
<li>كيف أبطل الله تعالى عبادة المشركين لغيره؟</li>
<li>أربط بين الآيات ومقاصدها الواردة في العنصر الثالث.</li>
</ol>
<h2>الاستثمار</h2>
<p>قال الألوسي رحمه الله: «جَاءَ فِي سُورَةِ النَّحْلِ: «وَتَرَى ٱلْفُلْكَ مَوَاخِرَ فِيهِ وَلِتَبْتَغُوا۟ مِن فَضْلِهِۦ» [النحل: 14] بِتَقْدِيمِ مَوَاخِرَ وَتَأْخِيرِ «فِيهِ» وُعُكِسَ هَهُنَا(...) وَالَّذِي يَظْهَرُ لِي فِي ذَلِكَ أَنَّ آيَةَ النَّحْلِ سِيقَتْ لِتَعْدَادِ النِّعَمِ كَمَا يُؤْذِنُ بِذَاكَ سَوَابِقُهَا وَلَوَاحِقُهَا، وَتَعْقِيبُ الآيَاتِ بِقَوْلِهِ سُبْحَانَهُ: «وَإِن تَعُدُّوا۟ نِعْمَةَ ٱللَّهِ لَا تُحْصُوهَا» [النحل: 18] فَكَانَ الْأَهَمَّ هُنَاكَ تَقْدِيمَ مَا هُوَ نِعْمَةٌ وَهُوَ مَخْرُ الْفَلَكِ لِلْمَاءِ، بِخِلاَفِ مَا هُنَا، فَإِنَّه إِنَّمَا سِيقَ اِسْتِطْرادًا أَوْ تَتِمَّةً لِلتَّمْثيلِ (...) فَقَدَّمَ «فِيهِ» إِيذَانًا بِأَنَّهُ لَيْسَ الْمَقْصُودَ بِالذَّاتِ ذَلِكَ، وَكَأَنَّ الْاِهْتِمَامَ بِمَا هُنَاكَ اقْتَضَى أَنْ يُقَالَ فِي تِلْكَ الْآيَةِ «وَلِتَبْتَغُوا۟» بالواو، وَمُخَالَفَةُ مَا هُنَا لِذَلِكَ اقْتَضَتْ تَرْكَ الْوَاوِ فِي قَوْلِهِ سُبْحَانَهُ «لِتَبْتَغُوا۟ مِن فَضْلِهِۦ» أَيْ: مِنْ فَضْلِ اللهِ تَعَالَى بِالنَّقَلَةِ فِيهَا». [روح المعاني، الألوسي: 11/353 (بتصرف)]</p>
<p>أتأمل النص وأجيب عن الآتي:</p>
<ul>
<li>أقارن بين ما جاء في سورة النحل وسورة فاطر، بخصوص قوله تعالى: «وَتَرَى ٱلْفُلْكَ مَوَاخِرَ فِيهِ وَلِتَبْتَغُوا۟ مِن فَضْلِهِۦ وَلَعَلَّكُمْ تَشْكُرُونَ» مع التعليل.</li>
</ul>
<h2>الإعداد القبلي</h2>
<p>أتأمل الآيات: 15-18 من سورة فاطر وأجيب عن الآتي:</p>
<ul>
<li>أبحث عن مدلولات العبارات الآتية: «ٱلْفُقَرَآءُ» - «ٱلْغَنِيُّ ٱلْحَمِيدُ» - «مُثْقَلَةٌ» - «تَدْعُ» - «تَزَكَّىٰ».</li>
<li>أنجز بحثا يتضمن مظاهر العدالة الإلهية بين العباد يوم القيامة من خلال هذه الآيات.</li>
</ul>"""

HTML_FR = """<h1> Sourate Fāṭir, versets 12-14 : livre du Tafsīr à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy, deuxième année collégiale — leçon 5</h1>
<p>Leçon sur l’exégèse de la sourate Fāṭir, versets 12 à 14, du livre du Tafsīr fondé sur le <em>Tashīl li-ʿulūm al-tanzīl</em> d’Ibn Juzayy, pour la deuxième année de l’enseignement collégial traditionnel (leçon 5).</p>
<ol>
<li>Que je connaisse les phénomènes cosmiques contenus dans ces versets.</li>
<li>Que j’établisse la preuve qu’Allah — exalté soit-Il — seul mérite l’adoration.</li>
<li>Que je rende grâce à Allah — exalté soit-Il — pour les bienfaits dont Il nous a gratifiés.</li>
</ol>
<h2>Introduction (tamhīd)</h2>
<p>Après que les versets précédents ont établi, par les signes touchant les personnes humaines (āyāt al-anfus), Son exclusivité en la divinité, ces versets poursuivent l’argumentation par d’autres manifestations des phénomènes cosmiques : les mers, la nuit, le jour, le soleil et la lune ; puis ils invalident ce que les associationnistes adorent en dehors de Dieu, établissant que ces objets d’adoration ne profitent ni à eux-mêmes ni à autrui.</p>
<p>Quelles sont les manifestations des signes cosmiques de Dieu figurant dans ces versets ? Et comment en établirai-je la preuve qu’Allah seul mérite l’adoration ?</p>
<h2>Les versets</h2>
<p>Allah — exalté soit-Il — a dit :</p>
<p><span>Sourate Fāṭir, versets 12 à 14</span></p>
<p>« Les deux mers ne sont pas semblables : celle-ci est douce, désaltérante, agréable à boire ; celle-là salée, âcre. De chacune vous mangez une chair fraîche, et vous en extrayez une parure que vous portez ; et tu vois le navire y fendre l’eau — pour que vous recherchiez de Sa faveur, et peut-être rendrez-vous grâce » (12).</p>
<p>« Il fait entrer la nuit dans le jour, et fait entrer le jour dans la nuit ; et Il a assujetti le soleil et la lune : chacun coule vers un terme nommé. Tel est Allah, votre Seigneur : à Lui la royauté. Et ceux que vous invoquez en dehors de Lui ne possèdent pas même la pellicule d’un noyau de datte » (13).</p>
<p>« Si vous les invoquez, ils n’entendent pas votre invocation ; et quand même ils entendraient, ils ne vous répondraient pas. Au Jour de la résurrection, ils désavoueront votre association ; et nul ne t’informe comme Celui qui est parfaitement informé » (14).</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>« ʿaḏbun furātun » (douce, désaltérante) : d’une douceur extrême.</p>
<p>« sāʾiġun šarābuhū » (dont la boisson descend aisément) : agréable, qui descend aisément dans la gorge.</p>
<p>« milḥun uǧāǧun » (salée, âcre) : d’une salinité extrême.</p>
<p>« laḥman ṭariyyan » (une chair fraîche) : le poisson.</p>
<p>« ḥil’yatan » (une parure) : la perle et le corail.</p>
<p>« mawāḫira » (fendant l’eau) : pluriel de māḫira, qui est le navire.</p>
<p>« qiṭmīr » (pellicule) : la pellicule blanche et fine qui enveloppe le noyau de la datte.</p>
<h3>Extraction des contenus des versets</h3>
<ol>
<li>Quels sont les signes cosmiques figurant dans ces versets ?</li>
<li>Sur quoi Allah — exalté soit-Il — argumente-t-Il par ces signes cosmiques ?</li>
</ol>
<h2>Le Tafsīr</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : quelques manifestations des signes cosmiques de Dieu</h3>
<p>Après l’argumentation de la survenance de la résurrection au Jour de la résurrection, ces versets exposent certaines preuves de Sa puissance et de Sa grandeur dans la création des choses diverses, malgré l’unité de leur utilité pour l’homme. Dieu — exalté soit-Il — a dit : « Les deux mers ne sont pas semblables : celle-ci est douce, désaltérante, agréable à boire ; celle-là salée, âcre » : c’est-à-dire que ces deux mers ne s’équivalent pas — l’une douce à l’extrême, jusqu’à la suavité ; l’autre salée, brûlante de salinité, jointe à l’amertume. Le verset vise à signaler la puissance de Dieu, Son unicité et Sa grâce envers Ses serviteurs.</p>
<p>Puis Il a exposé — exalté soit-Il — les visages du profit des hommes par les deux mers, la douce et la salée, disant — le Puissant, le Majestueux : « De chacune vous mangez une chair fraîche » : c’est là un excursus (istitrād) sur la description des deux mers et les bienfaits qu’elles contiennent ; c’est-à-dire : de chacune des deux mers vous mangez un poisson tendre et frais. « Et vous en extrayez une parure que vous portez » : c’est-à-dire que vous en extrayez la gemme et le corail, pour la parure et l’ornement. Si l’on objecte : la parure ne sort que de la mer salée, non de la douce — comment a-t-Il dit : « de chacune », c’est-à-dire de chacune des deux ?, la réponse se fait de trois manières.</p>
<p>La première : c’est une latitude d’expression (taǧawwuz), comme Sa parole : « Ô communauté des djinns et des hommes ! Des messagers ne sont-ils pas venus à vous, d’entre vous ? » [al-Anʿām : 131] — alors que les messagers ne furent que du genre humain.</p>
<p>La deuxième : le corail ne se trouve que dans la mer salée, là où se déversent les fleuves d’eau douce, ou où descend la pluie ; puisque les fleuves et la pluie — qui sont la mer douce — se déversent dans la mer salée, l’extraction vient bien de l’une et de l’autre ensemble.</p>
<p>La troisième : certains ont prétendu que la perle et le corail sortent de la salée et de la douce — dire que le constat dément, c’est-à-dire la réalité.</p>
<p>Et Sa parole — exalté soit-Il : « et tu vois le navire y fendre l’eau (mawāḫira) » : « pluriel de māḫira ; on dit : maḫarat as-safīna (" le navire fendit l’eau ") ; et le maḫr est la fente de l’eau ; on a dit aussi : le bruit de la course des navires portés par les vents » [at-Tashīl : 1/423]. « Pour que vous recherchiez de Sa faveur, et peut-être rendrez-vous grâce » : c’est-à-dire qu’Il vous a assujetti la mer pour que vous recherchiez la faveur de Dieu par les divers commerces et autres, et pour que vous rendiez grâce à votre Seigneur de Ses bienfaits et de Sa faveur, de vous avoir assujetti cela.</p>
<p>Puis les versets ont continué d’exposer les manifestations de la puissance de Dieu — exalté soit-Il — dans l’horizon (āfāq), disant — exalté soit-Il : « Il fait entrer la nuit dans le jour, et fait entrer le jour dans la nuit » : c’est-à-dire qu’Il fait entrer chacun des deux dans l’autre — en accroissant l’un et en diminuant l’autre, ou en faisant entrer l’obscurité de la nuit sur la lumière du jour, et la lumière du jour sur l’obscurité de la nuit [at-Tashīl : 2/140].</p>
<p>Puis Il a établi — exalté soit-Il — qu’Il a assujetti le soleil et la lune par Sa puissance et Sa volonté, disant — le Puissant, le Majestueux : « et Il a assujetti le soleil et la lune » : c’est-à-dire qu’Il a dompté le soleil et la lune au profit des serviteurs : chacun des deux court dans son orbite jusqu’au Jour de la résurrection.</p>
<h3>Deuxièmement : la preuve qu’Allah — exalté soit-Il — mérite l’adoration à l’exclusion de tout autre</h3>
<p>Après l’exposé de scènes des manifestations de Sa puissance, Sa science, Sa sagesse, Sa douceur et Sa miséricorde, Il a adressé aux hommes cette parole : « Tel est Allah, votre Seigneur : à Lui la royauté » : c’est-à-dire que Celui-là qui a accompli les choses précédentes est votre Seigneur — nul Seigneur en dehors de Lui, nul adoré en vérité sinon Lui ; à Lui la royauté, la grandeur et l’autorité.</p>
<p>Puis Il a établi — exalté soit-Il — que ce que les associationnistes adorent en dehors de Lui ne mérite pas l’adoration, car ces objets d’adoration sont indigents et ne possèdent rien, disant — exalté soit-Il : « Et ceux que vous invoquez en dehors de Lui ne possèdent pas même la pellicule d’un noyau de datte » : le qiṭmīr est la pellicule blanche et fine sur le noyau de la datte. Le sens est que les idoles ne possèdent pas la moindre des choses — de la grandeur d’une pellicule de noyau —, comment donc ce qui est plus grand !</p>
<p>Et Dieu — exalté soit-Il — a renforcé [l’exposé de] la faiblesse des idoles et de leur impuissance par Sa parole : « Si vous les invoquez, ils n’entendent pas votre invocation » : c’est-à-dire que si vous invoquez ces objets d’adoration en dehors de Dieu, ils n’entendent pas votre invocation. « Et quand même ils entendraient, ils ne vous répondraient pas » : c’est-à-dire que quand même ils entendraient — par supposition —, ils ne vous répondraient pas : ce sont des corps inertes, sans sensation, sans pouvoir de procurer un profit. « Au Jour de la résurrection, ils désavoueront votre association » : c’est-à-dire : à cause de votre acte d’associer — le nom d’action (maṣdar) est adjoint à son agent.</p>
<p>Il en est le pendant dans Sa parole : « Dis : " Voyez-vous ce que vous invoquez en dehors de Dieu ? Montrez-moi ce qu’ils ont créé de la terre ; ou ont-ils une part aux cieux ? Apportez-moi un Livre antérieur à celui-ci, ou une trace de science, si vous êtes véridiques. " Et qui est plus égaré que celui qui invoque, en dehors de Dieu, celui qui ne lui répondra pas jusqu’au Jour de la résurrection — eux, indifférents à leur invocation ? » [al-Aḥqāf : 4-5]. Et Sa parole — exalté soit-Il : « Ils ont pris, en dehors de Dieu, des divinités pour en tirer de la gloire. Non ! Ils désavoueront leur adoration, et seront contre eux des adversaires » [Maryam : 82-83]. « Et nul ne t’informe comme Celui qui est parfaitement informé » : c’est-à-dire que nul ne t’informe de l’affaire comme un informateur qui la connaît — Il vise Lui-même — exalté soit-Il — dans Son information que les idoles désavoueront, au Jour de la résurrection, ceux qui les auront adorées.</p>
<h3>Troisièmement : les finalités (maqāṣid) des versets</h3>
<p>Ces versets indiquent, dans leur ensemble, plusieurs finalités, parmi lesquelles :</p>
<ul>
<li>L’exposé de la faveur de Dieu — exalté soit-Il — et de Sa grâce envers Ses serviteurs par les diverses sortes de bienfaits : Il a assujetti à Ses serviteurs la mer et les richesses qu’elle contient, la nuit et le jour, le soleil et la lune.</li>
<li>L’exhortation à réserver le culte à Dieu — exalté soit-Il — seul, à l’exclusion de tout autre : Lui seul mérite l’adoration, à la différence des objets d’adoration vains, qui ne possèdent pour elles-mêmes ni profit ni nuisance — encore moins pour autrui.</li>
</ul>
<h2>L’évaluation</h2>
<ol>
<li>Je déduis la finalité de la bienveillance de Dieu — exalté soit-Il — envers Ses serviteurs par les bienfaits figurant dans ces versets.</li>
<li>Comment Dieu — exalté soit-Il — a-t-Il invalidé l’adoration par les associationnistes d’un autre que Lui ?</li>
<li>Je relie les versets aux finalités mentionnées au troisième point.</li>
</ol>
<h2>L’exploitation (istiṯmār)</h2>
<p>Al-Alūsī — qu’Allah lui fasse miséricorde — a dit : « Il est venu, dans la sourate an-Naḥl : " Et tu vois le navire y fendre l’eau, et pour que vous recherchiez de Sa faveur " [an-Naḥl : 14] — par avance de mawāḫir et retard de " en elle " (fīhi) — et l’inverse a lieu ici (…). Ce qui m’apparaît en cela est que le verset de an-Naḥl fut déroulé pour l’énumération des bienfaits, comme l’annoncent ses précédents et ses suivants, et l’enchâssement des versets par la parole de Dieu — exalté soit-Il : " Si vous comptiez le bienfait d’Allah, vous ne pourriez les dénombrer " [an-Naḥl : 18]. Le plus important là-bas était donc l’avance de ce qui est un bienfait — la fente de l’eau par le navire — ; au contraire d’ici, où [le propos] ne vint qu’en excursus ou complément de l’illustration (…). Il a donc avancé " en elle " (fīhi), pour marquer que ce n’est pas là l’objet visé par soi ; et comme l’intérêt, là-bas, exigeait qu’on dît, dans ce verset, " et pour que vous recherchiez " (wa-li-tabtaġū) avec le wāw, la différence d’ici exigeait d’abandonner le wāw dans Sa parole — exalté soit-Il : " pour que vous recherchiez de Sa faveur " (li-tabtaġū) — c’est-à-dire : de la faveur d’Allah — exalté soit-Il — par la transposition (naqla) qu’il y a en elle. » [Rūḥ al-maʿānī, d’al-Alūsī : 11/353 (adapté)]</p>
<p>Je médite le texte et je réponds à ce qui suit :</p>
<ul>
<li>Je compare ce qui est venu dans la sourate an-Naḥl et dans la sourate Fāṭir, au sujet de Sa parole — exalté soit-Il : « Et tu vois le navire y fendre l’eau, et pour que vous recherchiez de Sa faveur, et peut-être rendrez-vous grâce », avec la justification.</li>
</ul>
<h2>La préparation préalable (iʿdād qablī)</h2>
<p>Je médite les versets 15 à 18 de la sourate Fāṭir et je réponds à ce qui suit :</p>
<ul>
<li>Je recherche la valeur des expressions suivantes : « al-fuqarāʾ » (les indigents) — « al-Ġanī al-Ḥamīd » (le Riche, le Loué) — « muṯqala » (surchargée) — « tadʿu » (elle appelle) — « tazakkā » (se purifie).</li>
<li>Je réalise une recherche exposant les manifestations de la justice divine entre les serviteurs au Jour de la résurrection, à partir de ces versets.</li>
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
        if str(l.get("docId", "")).endswith("-560"):
            l["html"] = HTML_AR
            l["htmlFr"] = html_fr
            l["pdfOnly"] = False
            # titre catalogue confirmé correct : «الآيات : 12 - 14» (citation
            # imprimée [سورة فاطر: 14-12] + CMS 16823 — convention RTL)
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 560 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 560 livrée: AR {len(HTML_AR)} car + FR {len(html_fr)} car")


if __name__ == "__main__":
    main()
