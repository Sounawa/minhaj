#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Livraison de la leçon 557 (سورة فاطر 4-6, الدرس 2, R99-WARSH).

Vérifications R99 (méthode Warsh e-verification + croisement CMS) :
- Bloc coranique p1-p2 : 4 lignes — L1 «وَإِن يُكْذِبُوكَ فَقَدْ كُذِّبَتْ رُسُلٌۭ مِّن
  قَبْلِكَ ۚ وَإِلَى ٱللَّهِ» / L2 «تُرْجَعُ ٱلْأُمُورُ ۝٤ يَٰٓأَيُّهَا ٱلنَّاسُ إِنَّ وَعْدَ
  ٱللَّهِ حَقٌّۭ فَلَا تَغُرَّنَّكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا» / p2-A «وَلَا يَغُرَّنَّكُم بِٱللَّهِ
  ٱلْغَرُورُ ۝٥ إِنَّ ٱلشَّيْطَٰنَ لَكُمْ عَدُوٌّۭ فَٱتَّخِذُوهُ عَدُوًّا» / p2-B «إِنَّمَا
  يَدْعُوا۟ حِزْبَهُۥ لِيَكُونُوا۟ مِنْ أَصْحَٰبِ ٱلسَّعِيرِ ۝٦ [سورة فاطر: ٦-٤]» —
  toutes conformes au squelette tanzil lettre à lettre (sondes tesseract 300+600 dpi
  convergentes ; pas de divergence Warsh/Ḥafṣ de rasm dans Fāṭir 4-6).
- Rosettes : ۝٤ confirmée p1 (blob x3962 y5715, juste après «ٱلْأُمُورُ») ; ۝٥ confirmée
  p2-A (blob x2841 y830, juste après «ٱلْغَرُورُ», médaillon circulaire à chiffre
  central) ; ۝٦ p2-B entre «ٱلسَّعِيرِ» et la citation (ornement lu «))»/«ررب» par
  tesseract). Citation imprimée [سورة فاطر: ٦-٤] = plage 4-6 (format inversé du scan).
- NUMÉROTATION MÉDINOISE (découverte clé R99) : le manuel cite «فَدَلَّىٰهُمَا بِغُرُورٍ»
  [الأعراف: ٢١] (= Ḥafṣ 22 — lu pixel : ٢+١, confirmé par la version CMS 16799) et
  [الأعراف: ١٦-١٥] (= Ḥafṣ 17-16, lu «16-15» aux 2 résolutions) et «وَلَأُضِلَّنَّهُمْ»
  [النساء: ١١٨] (= Ḥafṣ 119 ; cohérent avec R96 : [النساء: 142] = Ḥafṣ 143 مذبذبين).
  Aucune NdT comparative (directive Warsh-only) — transcription telle qu'imprimée.
- Croisement CMS (16799, version minhaj.ma du même ouvrage) : Nasafī 77/3, Ibn ʿĀšūr
  258/22 + 259/22 (بتصرف), Saʿīd b. Ǧubayr / Qurṭubī 323/14, Ibn Kaṯīr 534/6 (×2),
  hadith Bukhārī (Ribqāq) et Ibn Baṭṭāl 150/10 (بتصرف) — tous VERBATIM conformes ;
  glose 4 «ٱلسَّعِيرُ: النار المستعرة» récupérée (manquée par l'OCR PDF).
- «تُفَارِقُهُ» (Ibn Baṭṭāl) : triple lecture tesseract «تُقَارِفَهُ/تُقَارَقَهُ» (confusion
  ق/ف classique) mais 3 dammas pixel-comptées = pattern تُXَارِقُهُ + CMS «تُفَارِقُهُ» +
  sémantique (les bienfaits qui ne le quittent pas) → retenu.
- Saʿīd b. Ǧubayr : «يَعْمَلُ بِالْمَعَاصِي ثُمَّ يَتَمَنَّى عَلَى اللَّهِ الْمَغْفِرَةَ»
  (600 dpi + CMS ; le garble 300 dpi «يَجْمَلُ» = يَعْمَلُ, ج→ع).
- Idad (expressions v7-9) : «سُوٓءُ عَمَلِهِ» (psm8 «مُوَؤْعَمَلف» = س→م ء→ؤ ه→ف) -
  «فَتُثِيرُ» (lectures convergentes مَترْ/جَيثيرْ/زيث/قثي = [ف]ت+ث+ي+ر) -
  «بَلَدٍۢ مَّيِّتٍ» (garble جَلْوْتَيتٍ ≈ glossaire 558 «بَلْوميتٍ») -
  «ٱلنُّشُورُ» (garble التثوز/النثوز, ث↔ش ز↔ر ; règle d'or : idad N = شرح N+1 —
  glossaire 558 définit بَلَدٍ مَّيِّتٍ et النُّشُورُ).
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"

HTML_AR = """<h1>سورة فاطر (الآيات: 4-6): كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي للسنة الثانية إعدادي الدرس 2</h1>
<p>درس في تفسير سورة فاطر الآيات (4-6)، كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي، للسنة الثانية من التعليم الإعدادي العتيق (الدرس 2).</p>
<ol>
<li>أن أتعرف وجوه اغترار الإنسان بالحياة الدنيا والشيطان.</li>
<li>أن أستدل على صدق رسالة النبي ﷺ.</li>
<li>أن أحذر الاغترار بما يزينه الشيطان من متع الحياة الدنيا.</li>
</ol>
<h2>تمهيد</h2>
<p>بعد استدلال الله سبحانه في الآيات السابقة على قدرته وعظمته في الخلق والإبداع؛ جاءت هذه الآيات تسلي النبي ﷺ وتؤكد على صدق رسالته؛ وتذكر الناس بنعم الله عليهم وتحذرهم من الاغترار بوساوس الشيطان وحزبه الذين يدعون أتباعهم إلى عذاب النار.</p>
<p>فكيف سلى الله تعالى نبيه ﷺ في هذه الآيات؟ ولماذا حذر عباده من الاغترار بالدنيا والشيطان؟</p>
<h2>الآيات</h2>
<p><span>سورة فاطر: 4-6</span></p>
<p>«وَإِن يُكْذِبُوكَ فَقَدْ كُذِّبَتْ رُسُلٌۭ مِّن قَبْلِكَ ۚ وَإِلَىٰ ٱللَّهِ تُرْجَعُ ٱلْأُمُورُ» [فاطر: 4]</p>
<p>«يَٰٓأَيُّهَا ٱلنَّاسُ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ ۖ فَلَا تَغُرَّنَّكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۖ وَلَا يَغُرَّنَّكُم بِٱللَّهِ ٱلْغَرُورُ» [فاطر: 5]</p>
<p>«إِنَّ ٱلشَّيْطَٰنَ لَكُمْ عَدُوٌّۭ فَٱتَّخِذُوهُ عَدُوًّا ۚ إِنَّمَا يَدْعُوا۟ حِزْبَهُۥ لِيَكُونُوا۟ مِنْ أَصْحَٰبِ ٱلسَّعِيرِ» [فاطر: 6]</p>
<h2>الفهم</h2>
<h3>الشرح:</h3>
<p>«ٱلْأُمُورُ»: جمع أمر، وهو الشأن والحال.</p>
<p>«ٱلْغُرُورُ»: الشيطان؛ وقيل: التسويف.</p>
<p>«حِزْبُهُ»: شيعته وأتباعه.</p>
<p>«ٱلسَّعِيرُ»: النار المستعرة.</p>
<h3>استخلاص مضامين الآيات:</h3>
<ol>
<li>بم سلى الله تعالى رسوله ﷺ في الآيات؟</li>
<li>مم حذر الله تعالى عباده في الآيات؟</li>
</ol>
<h2>التفسير</h2>
<p>اشتملت هذه الآيات على ما يأتي:</p>
<h3>أولا: تسلية الرسول ﷺ والتأكيد على صدق رسالته:</h3>
<p>بعد أن تضمنت آيات الدرس السابق الأصل الأول من أصول العقيدة الإسلامية؛ وهو التوحيد؛ نصت هذه الآيات على الأصل الثاني الذي هو الرسالة؛ فقال سبحانه: «وَإِن يُكْذِبُوكَ فَقَدْ كُذِّبَتْ رُسُلٌۭ مِّن قَبْلِكَ» هذه الآية تسلية للنبي ﷺ على تكذيب قومه؛ كأنه يقول له: إن يكذبوك؛ فلا تحزن لذلك؛ فإن الله سينصرك عليهم؛ كما كذبت رسل من قبلك فنصرهم الله. قال النسفي رحمه الله: «سلى رسوله؛ بأن له في الأنبياء قبله أسوة؛ ولهذا نكر "رسل" أي: رسل ذوو عدد كثير؛ وأولو آيات ونذر؛ وأهل أعمار طوال؛ وأصحاب صبر وعزم؛ لأنه أسلى له. وتقدير الكلام: وإن يكذبوك فتأس بتكذيب الرسل من قبلك؛ لأن الجزاء يتعقب الشرط؛ ولو أجري على الظاهر يكون سابقاً عليه. ووضع "قد كذبت" موضع "فتأس" استغناء بالسبب عن المسبب» أي: بالتكذيب عن التأسي. «وَإِلَىٰ ٱللَّهِ تُرْجَعُ ٱلْأُمُورُ» كلام يشتمل على الوعد والوعيد؛ من رجوع الأمور إلى حكمه؛ ومجازاة المكذَّب والمكذِّب بما يستحقانه» [مدارك التنزيل وحقائق التأويل، للنسفي: 77/3].</p>
<h3>ثانيا: التحذير من غرور الدنيا وغرور الشيطان:</h3>
<p>بعد الأصل الثاني من أصول العقيدة الإسلامية التي تضمنتها آيات العنصر الأول؛ نبهت هذه الآيات على أصل ثالث؛ وهو البعث والنشور؛ وبينت الآيات أنه حق؛ وموعظةٌ للمكذبين للرسول ﷺ؛ فقال سبحانه: «يَٰٓأَيُّهَا ٱلنَّاسُ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ» «الوعد مصدر؛ وهو الإخبار عن فعل المخبر شيئا في المستقبل. والأكثر أن يكون فيما عدا الشر. ويخص الشر منه باسم الوعيد؛ يعمهما وهو هنا مستعمل في القدر المشترك» [التحرير والتنوير، لابن عاشور: 258/22]. والحق: يقابل الكذب؛ وإضافة الوعد إلى الله تعالى يشعر بكونه حقا؛ لأن الله سبحانه لا يأتي منه الباطل. والمعنى: إن وعد الله بالبعث والحشر والجزاء صدق لا شك فيه.</p>
<p>ثم حذرت هذه الآيات من الاغترار بما يوجب الخسران يوم القيامة؛ فقال عز وجل: «فَلَا تَغُرَّنَّكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا» أي: فلا تلهينكم الحياة الدنيا ويذهلنكم التمتع بملذاتها عن طلب الآخرة والسعي لها. فغرور الحياة الدنيا هو اشتغال الإنسان بنعيمها وملذاتها عن عمل الآخرة؛ لأن إسناد التغرير إلى الحياة الدنيا؛ إسناد مجازي؛ ذلك أن الذي يغر الإنسان هو نفسه التي انخدعت بملذات الحياة الدنيا ونعيمها. فهذا من باب إسناد الفعل إلى سببه.</p>
<p>بعد تحذيره تعالى من الاغترار بالحياة الدنيا؛ حذر من الاغترار بالشيطان ووساوسه؛ فقال سبحانه: «وَلَا يَغُرَّنَّكُم بِٱللَّهِ ٱلْغَرُورُ» المقصود بـ«ٱلْغُرُورُ»: الشيطان؛ وقيل: التسويف. قال تعالى: «فَدَلَّىٰهُمَا بِغُرُورٍ» [الأعراف: 21]. والمعنى: لا يلهينكم الشيطان ويصرفنكم عن تصديق رسل الله تعالى وأنبيائه بإيهامكم بأن الله سيتجاوز عنكم لفضلكم؛ رغم ارتكابكم للمعاصي والذنوب. قال سعيد بن جبير: «الْغُرُورُ بِٱللَّهِ أَنْ يَكُونَ الْإِنْسَانُ يَعْمَلُ بِالْمَعَاصِي ثُمَّ يَتَمَنَّى عَلَى ٱللَّهِ الْمَغْفِرَةَ» [الجامع لأحكام القرآن، للإمام القرطبي: 323/14].</p>
<p>و«الباء» في قوله «بِٱللَّهِ» للملابسة دخلت على مضاف محذوف؛ تقديره: بشأن الله. لأن فعل «غر» يتعدى إلى مفعول واحد؛ فإذا أريد تعديته إلى بعض متعلقاته عدي إليه بواسطة حرف الجر؛ مثل باء الملابسة؛ كما ورد في قوله تعالى: «يَٰٓأَيُّهَا ٱلْإِنسَٰنُ مَا غَرَّكَ بِرَبِّكَ ٱلْكَرِيمِ» [الانفطار: 6]» [التحرير والتنوير: 259/22 (بتصرف)].</p>
<p>ثم بين الله تعالى عداوة الشيطان للبشر وحذرهم منه فقال سبحانه: «إِنَّ ٱلشَّيْطَٰنَ لَكُمْ عَدُوٌّۭ فَٱتَّخِذُوهُ عَدُوًّا» أي: إن الشيطان عدو قديم لكم؛ بدليل تسببه في إخراج أبيكم من الجنة؛ وهو يوسوس لكم ليضلكم؛ وقد أفصح الشيطان عن عداوته لبني آدم في آيات كثيرة منها: قوله تعالى: «وَلَأُضِلَّنَّهُمْ» [النساء: 118] الآية. وقوله: «قَالَ فَبِمَآ أَغْوَيْتَنِى لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ ۝ ثُمَّ لَءَاتِيَنَّهُم مِّنۢ بَيْنِ أَيْدِيهِمْ وَمِنْ خَلْفِهِمْ وَعَنْ أَيْمَٰنِهِمْ وَعَن شَمَآئِلِهِمْ ۖ وَلَا تَجِدُ أَكْثَرَهُمْ شَٰكِرِينَ» [الأعراف: 16-15].</p>
<p>ثم حث الله تعالى عباده على اتخاذ الشيطان عدوا لهم؛ فقال سبحانه: «فَٱتَّخِذُوهُ عَدُوًّا» قال ابن كثير رحمه الله، أي: «هو مبارز لكم بالعداوة؛ فعادوه أنتم أشد العداوة؛ وخالفوه وكذبوه فيما يغركم به» [تفسير القرآن العظيم، لابن كثير: 534/6]. ثم وضح الله تعالى هدف الشيطان من إغواء أتباعه؛ فقال عز وجل: «إِنَّمَا يَدْعُوا۟ حِزْبَهُۥ لِيَكُونُوا۟ مِنْ أَصْحَٰبِ ٱلسَّعِيرِ» «إن» مكفوفة عن العمل بـ«ما»؛ لذلك وقع الفعل بعدها. ومعنى الآية: «إنما يقصد الشيطان أن يضلكم؛ حتى تدخلوا معه إلى عذاب جهنم المستعرة» [تفسير القرآن العظيم، لابن كثير: 534/6].</p>
<h3>ثالثا: مقاصد الآيات:</h3>
<p>تهدف هذه الآيات إلى تحقيق مقاصد متعددة؛ أهمها ما يأتي:</p>
<ul>
<li>إثبات الأصل الثاني من أصول العقيدة الإسلامية المتمثل في صدق رسالة النبي المصطفى ﷺ.</li>
<li>التأكيد على أن كل أمور الخلائق وشؤونها مرجعها إلى الله تعالى؛ الذي سيقرر مصيرها يوم القيامة.</li>
<li>أهمية تزكية الإنسان لنفسه بحثها على عدم الاغترار بالحياة الدنيا وملذاتها؛ وعدم الانسياق وراء شهواتها، واتباع خطوات الشيطان المؤدية إلى الهلاك وإلى الوقوع في نار السعير.</li>
</ul>
<h2>التقويم</h2>
<ol>
<li>ما الغاية من ذكر تكذيب الأمم السابقة للأنبياء والرسل؟</li>
<li>لماذا ربط الله تعالى بين غرور الحياة الدنيا وغرور الشيطان؟</li>
<li>ما الفرق بين الوعد والوعيد من خلال قوله تعالى: «إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ»؟</li>
</ol>
<h2>الاستثمار</h2>
<p>عَنْ عَبْدِ اللهِ رَضِيَ اللهُ عَنْهُ، قَالَ: «خَطَّ النَّبِيُّ ﷺ خَطًّا مُرَبَّعًا، وَخَطَّ خَطًّا فِي الْوَسَطِ خَارِجًا مِنْهُ، وَخَطَّ خُطُوطًا صِغَارًا إِلَى هَذَا الَّذِي فِي الْوَسَطِ مِنْ جَانِبِهِ الَّذِي فِي الْوَسَطِ، وَقَالَ: هَذَا الْإِنْسَانُ، وَهَذَا أَجَلُهُ مُحِيطٌ بِهِ - أَوْ: قَدْ أَحَاطَ بِهِ - وَهَذَا الَّذِي هُوَ خَارِجٌ أَمَلُهُ، وَهَذِهِ الْخُطُوطُ الصِّغَارُ الْأَعْرَاضُ، فَإِنْ أَخْطَأَهُ هَذَا نَهَشَهُ هَذَا، وَإِنْ أَخْطَأَهُ هَذَا نَهَشَهُ هَذَا» [صحيح البخاري، كتاب الرقاق، باب في الأمل وطوله]. قَالَ ابْنُ بَطَّالٍ رَحِمَهُ اللهُ: «مَثَّلَ النَّبِيُّ ﷺ فِي حَدِيثِ ابْنِ مَسْعُودٍ أَمَلَ ابْنِ آدَمَ وَأَجَلَهُ وَأَعْرَاضَ الدُّنْيَا الَّتِي لَا تُفَارِقُهُ بِالْخُطُوطِ، فَجُعِلَ أَجَلُهُ الْخَطَّ الْمُحِيطَ، وَجُعِلَ أَمَلُهُ وَأَعْرَاضَهُ خَارِجَةً مِنْ ذَلِكَ الْخَطِّ، وَمَعْلُومٌ فِي الْعُقُولِ أَنَّ ذَلِكَ الْخَطَّ الْمُحِيطَ بِهِ الَّذِي هُوَ أَجَلُهُ؛ أَقْرَبُ إِلَيْهِ مِنَ الْخُطُوطِ الْخَارِجَةِ مِنْهُ (...) وَفِي هَذَا تَنْبِيهٌ مِنَ النَّبِيِّ ﷺ لِأُمَّتِهِ عَلَى تَقْصيرِ الْأَمَلِ، وَاسْتِشْعَارِ الْأَجَلِ خَوْفَ بَغْتَةِ الْأَجَلِ، وَمَنْ غُيِّبَ عَنْهُ أَجَلُهُ، فَهُوَ حَرِيٌّ بِتَوَقُّعِهِ وَانْتِظارِهِ خَشْيَةَ هُجُومِهِ عَلَيْهِ فِي حَالِ غِرَّةٍ وَغَفْلَةٍ، وَنَعُوذُ بِاللهِ مِنْ ذَلِكَ» [شرح صحيح البخاري، لابن بطال: 150/10 (بتصرف)].</p>
<p>أتأمل النص وأجيب عن الآتي:</p>
<ol>
<li>أوضح العلاقة بين النص ومضامين الدرس.</li>
<li>كيف تسهم مضامين النص في تزكية نفسي وتهذيبها؟</li>
</ol>
<h2>الإعداد القبلي</h2>
<p>أتأمل الآيات: 7-9 من سورة فاطر وأجيب عن الآتي:</p>
<ol>
<li>أبحث عن مدلولات العبارات الآتية: «سُوٓءُ عَمَلِهِ» - «فَتُثِيرُ» - «بَلَدٍۢ مَّيِّتٍ» - «ٱلنُّشُورُ».</li>
<li>أبين أدلة قدرة الله تعالى على البعث والحساب وأثر ذلك في تزكية نفسي.</li>
</ol>"""

HTML_FR = """<h1> Sourate Fāṭir, versets 4-6 : livre du Tafsīr à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy, deuxième année collégiale — leçon 2</h1>
<p>Leçon sur l’exégèse de la sourate Fāṭir, versets 4 à 6, du livre du Tafsīr fondé sur le <em>Tashīl li-ʿulūm al-tanzīl</em> d’Ibn Juzayy, pour la deuxième année de l’enseignement collégial traditionnel (leçon 2).</p>
<ol>
<li>Que je fasse connaissance des formes d’illusion de l’homme par la vie terrestre et par Satan.</li>
<li>Que j’établisse la preuve de la véracité de la mission du Prophète ﷺ.</li>
<li>Que je me prémunisse contre l’illusion de ce que Satan embellit comme plaisirs de la vie terrestre.</li>
</ol>
<h2>Introduction (tamhīd)</h2>
<p>Après qu’Allah — exalté soit-Il — a, dans les versets précédents, établi la preuve de Sa puissance et de Sa grandeur dans la création et l’invention, ces versets sont venus consoler le Prophète ﷺ et affirmer la véracité de sa mission ; ils rappellent aux hommes les bienfaits d’Allah envers eux et les avertissent contre l’illusion des insufflations de Satan et de son parti, qui appellent leurs suiveurs au châtiment du Feu.</p>
<p>Comment donc Allah — exalté soit-Il — a-t-Il consolé Son Prophète ﷺ dans ces versets ? Et pourquoi a-t-Il averti Ses serviteurs contre l’illusion de ce bas monde et de Satan ?</p>
<h2>Les versets</h2>
<p><span>Sourate Fāṭir, versets 4 à 6</span></p>
<p>« Si l’on te traite de menteur — des messagers avant toi ont été traités de menteurs. Et c’est vers Allah que font retour les affaires » (4).</p>
<p>« Ô hommes ! La promesse d’Allah est vérité : que la vie présente ne vous abuse point, et que le Trompeur ne vous abuse point au sujet d’Allah » (5).</p>
<p>« Satan est pour vous un ennemi : traitez-le donc en ennemi. Il ne fait qu’appeler son parti pour qu’ils soient des compagnons de la Fournaise » (6).</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>« al-umūr » (les affaires) : pluriel de amr, qui est la situation et l’état.</p>
<p>« al-ġurūr » (le Trompeur) : Satan ; on a dit aussi : le report (des repentirs).</p>
<p>« ḥizbahu » (son parti) : ses partisans et ses suiveurs.</p>
<p>« as-saʿīr » (la Fournaise) : le Feu ardent.</p>
<h3>Extraction des contenus des versets</h3>
<ol>
<li>Par quoi Allah — exalté soit-Il — a-t-Il consolé Son messager ﷺ dans ces versets ?</li>
<li>De quoi Allah — exalté soit-Il — a-t-Il averti Ses serviteurs dans ces versets ?</li>
</ol>
<h2>Le Tafsīr</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la consolation du Messager ﷺ et l’affirmation de la véracité de sa mission</h3>
<p>Après que les versets de la leçon précédente ont contenu le premier fondement des fondements du dogme islamique — l’unicité —, ces versets ont posé le second fondement, qui est la mission prophétique. Allah — exalté soit-Il — a dit : « Si l’on te traite de menteur — des messagers avant toi ont été traités de menteurs » : ce verset est une consolation pour le Prophète ﷺ face à la négation de son peuple, comme si [Allah] lui disait : s’ils te traitent de menteur, ne t’afflige pas pour cela ; Allah te donnera victoire sur eux, comme des messagers avant toi furent traités de menteurs et qu’Allah leur donna victoire. An-Nasafī — qu’Allah lui fasse miséricorde — dit : « Il a consolé Son messager en lui faisant savoir qu’il a, dans les prophètes qui l’ont précédé, un modèle ; c’est pourquoi il a laissé “messagers” indéterminé — c’est-à-dire : des messagers en très grand nombre, détenteurs de signes et d’avertissements, gens de longues vies et compagnons d’endurance et de constance, car cela Le console davantage. L’estimation du discours est : si l’on te traite de menteur, prends modèle sur le traitement de menteur infligé aux messagers avant toi, car la récompense suit la condition ; si on la rapportait au sens apparent, elle la précéderait. Et la mise de “ils ont été traités de menteurs” à la place de “prends modèle” relève de l’économie de la cause par l’effet » — c’est-à-dire : du traitement de menteur par la consolation. « Et c’est vers Allah que font retour les affaires : parole qui embrace la promesse et la menace — le retour des affaires à Son jugement, et la rétribution du négateur et du traité-de-menteur selon ce qu’ils méritent » [Madārik at-tanzīl wa-ḥaqāʾiq at-taʾwīl, d’an-Nasafī : 77/3].</p>
<h3>Deuxièmement : l’avertissement contre l’illusion de ce bas monde et l’illusion de Satan</h3>
<p>Après le second fondement du dogme islamique contenu dans les versets du premier élément, ces versets ont signalé un troisième fondement : la résurrection et le rassemblement ; et les versets ont établi qu’il est vérité, et exhortation pour ceux qui traitent le Messager ﷺ de menteur. Allah — exalté soit-Il — a dit : « Ô hommes ! La promesse d’Allah est vérité » : « La promesse (al-waʿd) est un nom d’action : l’information donnée par l’énonciateur d’un fait qu’il fera dans l’avenir. Le plus souvent, elle porte sur autre chose que le mal ; on réserve au mal le nom de menace (al-waʿīd) ; le terme les englobe tous deux, et il est ici employé dans l’acception commune » [at-Taḥrīr wa-t-tanwīr, d’Ibn ʿĀšūr : 258/22]. La vérité (al-ḥaqq) s’oppose au mensonge ; et l’annexion de la promesse à Allah — exalté soit-Il — fait sentir qu’elle est vérité, car de la part d’Allah — exalté soit-Il — ne provient pas le vain. Le sens est : la promesse d’Allah — résurrection, rassemblement et rétribution — est véridique, sans aucun doute.</p>
<p>Puis ces versets ont averti contre l’illusion de ce qui occasionne la perte au Jour de la résurrection. Allah — le Puissant, le Majestueux — a dit : « Que la vie présente ne vous abuse point » : c’est-à-dire : que la vie terrestre ne vous distraie pas, et que la jouissance de ses plaisirs ne vous fasse pas oublier la recherche de l’au-delà et l’effort pour lui. L’illusion de la vie terrestre est l’occupation de l’homme par ses délices et ses plaisirs au détriment de l’œuvre pour l’au-delà : attribuer l’abus à la vie terrestre est une attribution figurée, car celui qui abuse l’homme est son propre âme, dupée par les plaisirs et les délices de la vie terrestre. C’est là du genre de l’attribution de l’action à sa cause.</p>
<p>Après Son avertissement — exalté soit-Il — contre l’illusion de la vie terrestre, Il a averti contre l’illusion de Satan et de ses insufflations, et a dit — exalté soit-Il : « Et que le Trompeur ne vous abuse point au sujet d’Allah » : ce que vise « al-ġurūr » (le Trompeur), c’est Satan ; on a dit aussi : le report (des repentirs). Allah — exalté soit-Il — a dit : « Il les fit glisser tous deux par illusion » [al-Aʿrāf : 21]. Le sens est : que Satan ne vous distraie pas et ne vous détourne pas de croire aux messagers d’Allah — exalté soit-Il — et à Ses prophètes, en vous faisant accroire qu’Allah passera outre pour vous en raison de votre mérite, malgré les péchés et les fautes que vous commettez. Saʿīd ibn Ǧubayr dit : « L’illusion au sujet d’Allah, c’est que l’homme œuvre dans les péchés puis forme le souhait qu’Allah lui pardonne » [al-Ǧāmiʿ li-aḥkām al-Qurʾān, de l’imām al-Qurṭubī : 323/14].</p>
<p>« Le “bāʾ” de Sa parole “au sujet d’Allah (bi-llāh)” est le bāʾ de la circumstance, entré sur un complément déterminé sous-entendu, dont l’estimation est : au sujet de l’affaire d’Allah. Car le verbe “abuser (ġarra)” se construit avec un seul objet ; quand on veut l’étendre à certains de ses compléments, on l’étend au moyen d’une particule, telle que le bāʾ de la circumstance, comme il est venu dans Sa parole — exalté soit-Il : “Ô homme ! Qu’est-ce qui t’a abusé au sujet de ton Seigneur, le Noble ?” [al-Infiṭār : 6] » [at-Taḥrīr wa-t-tanwīr : 259/22 (adapté)].</p>
<p>Puis Allah — exalté soit-Il — a exposé l’inimitié de Satan envers les hommes et les en a avertis, et a dit — exalté soit-Il : « Satan est pour vous un ennemi : traitez-le donc en ennemi » : c’est-à-dire : Satan est un ennemi ancien pour vous — la preuve étant sa contribution à faire sortir votre père du Paradis —, et il vous insuffle des suggestions pour vous égarer. Satan a proclamé son inimitié envers les fils d’Adam en de nombreux versets, parmi lesquels Sa parole — exalté soit-Il : « J’égarerai certes… » [an-Nisāʾ : 118] (suite du verset). Et Sa parole : « Il dit : “Puisque Tu m’as égaré, je m’assiérai pour eux sur Ton chemin droit ; puis je les assaillirai de face, de derrière, par leur droite et par leur gauche — et Tu ne trouveras pas la plupart d’entre eux reconnaissants” » [al-Aʿrāf : 16-15].</p>
<p>Puis Allah — exalté soit-Il — a exhorté Ses serviteurs à prendre Satan pour ennemi, et a dit — exalté soit-Il : « Traitez-le donc en ennemi ». Ibn Kaṯīr — qu’Allah lui fasse miséricorde — dit, c’est-à-dire : « Il vous affronte ouvertement en inimitié ; opposez-lui donc, vous, l’inimitié la plus vive, contredisez-le et traitez-le de menteur en ce par quoi il vous abuse » [Tafsīr al-Qurʾān al-ʿAẓīm, d’Ibn Kaṯīr : 534/6]. Puis Allah — le Puissant, le Majestueux — a clarifié le but de Satan dans l’égarement de ses suiveurs, et a dit : « Il ne fait qu’appeler son parti pour qu’ils soient des compagnons de la Fournaise » : « inna » est neutralisée dans son effet par « mā », c’est pourquoi le verbe est venu après elle. Et le sens du verset est : « Satan ne vise qu’à vous égarer, jusqu’à ce que vous entriez avec lui dans le châtiment de la Géhenne ardente » [Tafsīr al-Qurʾān al-ʿAẓīm, d’Ibn Kaṯīr : 534/6].</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation de finalités multiples, parmi les plus importantes :</p>
<ul>
<li>L’affirmation du second fondement du dogme islamique, incarné par la véracité de la mission du Prophète l’Élu ﷺ.</li>
<li>L’affirmation que toutes les affaires des créatures et leurs situations font retour à Allah — exalté soit-Il —, qui décidera de leur sort au Jour de la résurrection.</li>
<li>L’importance pour l’homme de purifier son âme en l’exhortant à ne pas se laisser abuser par la vie terrestre et ses plaisirs, à ne pas suivre ses désirs, ni les pas de Satan, qui conduisent à la ruine et à la chute dans le Feu de la Fournaise.</li>
</ul>
<h2>L’évaluation</h2>
<ol>
<li>Quelle est la finalité de la mention du traitement de menteur infligé par les communautés antérieures aux prophètes et messagers ?</li>
<li>Pourquoi Allah — exalté soit-Il — a-t-Il lié l’illusion de la vie terrestre à l’illusion de Satan ?</li>
<li>Quelle est la différence entre la promesse et la menace, à partir de Sa parole — exalté soit-Il : « La promesse d’Allah est vérité » ?</li>
</ol>
<h2>L’exploitation (istiṯmār)</h2>
<p>D’après ʿAbdallah — qu’Allah soit satisfait de lui —, le Prophète ﷺ traça un carré, et traça une ligne au milieu, sortant de lui, et traça de petites lignes vers celle qui est au milieu, du côté de celle qui est au milieu, et dit : « Ceci est l’homme ; ceci est son terme, qui l’entoure — ou : l’a entouré — ; et ceci, qui est à l’extérieur, est son espoir ; et ces petites lignes sont les épreuves : si celle-ci le manque, celle-là l’atteint ; et si celle-là le manque, celle-ci l’atteint » [Ṣaḥīḥ al-Buḫārī ; livre des attendrissements (riqqāq) ; chapitre de l’espoir et de sa longueur]. Ibn Baṭṭāl — qu’Allah lui fasse miséricorde — dit : « Le Prophète ﷺ a, dans le hadith d’Ibn Masʿūd, figuré par des traits l’espoir du fils d’Adam, son terme, et les biens de ce monde qui ne le quittent pas : son terme a été figuré par le trait qui entoure, et son espoir et ses biens ont été placés à l’extérieur de ce trait. Et il est connu des intelligences que ce trait qui l’entoure — qui est son terme — lui est plus proche que les traits extérieurs (...) En cela il y a un avertissement du Prophète ﷺ à sa communauté sur le raccourcissement de l’espoir et la conscience du terme, dans la crainte de sa soudaineté ; et celui dont le terme lui est caché est enclin à l’attendre et à l’attendre, dans la crainte de son assaut en un état d’insouciance et d’oubli. Et nous cherchons refuge auprès d’Allah contre cela » [Šarḥ Ṣaḥīḥ al-Buḫārī, d’Ibn Baṭṭāl : 150/10 (adapté)].</p>
<p>Je médite le texte et je réponds à ce qui suit :</p>
<ol>
<li>J’explicite le rapport entre le texte et les contenus de la leçon.</li>
<li>Comment les contenus du texte contribuent-ils à la purification et à l’éducation de mon âme ?</li>
</ol>
<h2>La préparation préalable (iʿdād qablī)</h2>
<p>Je médite les versets 7 à 9 de la sourate Fāṭir et je réponds à ce qui suit :</p>
<ol>
<li>Je recherche la valeur des expressions suivantes : « suʾu ʿamalih » (la laideur de son action) — « fa-tuṯīru » (et elle soulève) — « balad mayyit » (contrée morte) — « an-nušūr » (la résurrection).</li>
<li>J’expose les preuves de la puissance d’Allah — exalté soit-Il — sur la résurrection et le compte, et l’effet de cela sur la purification de mon âme.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if str(l.get("docId", "")).endswith("-557"):
            l["html"] = HTML_AR
            l["htmlFr"] = HTML_FR
            l["pdfOnly"] = False
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 557 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 557 livrée: AR {len(HTML_AR)} car + FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
