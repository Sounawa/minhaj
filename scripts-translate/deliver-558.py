#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Livraison de la leçon 558 (سورة فاطر 7-9, الدرس 3, R99-WARSH).

Vérifications R99 (méthode Warsh e-verification + croisement CMS 16808) :
- BLOC v7-9 : 4 lignes (p1 ×3 + p2 ×1) conformes au squelette tanzil lettre à
  lettre (garbles 300 dpi : مركا برط الل كااه الووجيعا = من كان يريد العزة فلله
  العزة جميعا / وزوز وال لفحم يى تل تور ثم جاح وا لماو تمان اتيى = والله خلقكم
  من تراب ثم من نطفة ثم جعلكم أزواجا / عَلو اتير = على الله يسير) — pas de
  divergence Warsh/Ḥafṣ dans Fāṭir 7-9 (45 versets dans les deux comptages).
  Citation imprimée [سورة فاطر: ٩-٧] = 7-9. Le titre du catalogue habous
  «7-10» est ERRONÉ (corrigé en 7-9 : triple signal = citation imprimée +
  CMS 16808 + idad de 557) ; titleAr/titleFr corrigés.
- GLOSSAIRE 4 entrées (l'OCR PDF n'en lisait que 2 !) : «سُوٓءُ عَمَلِهِ» =
  قبيح عمله / «فَتُثِيرُ» = فتحرك بشدة / «بَلَدٍۢ مَّيِّتٍۢ» = لا نبات فيه /
  «ٱلنُّشُورُ» = البعث والحشر — définitions CMS + TERMES = idad de 557
  (correspondance 4/4 : la règle d'or idad N = شرح N+1 tient encore).
- [الشورى: ٤٥] = «إِنْ عَلَيْكَ إِلَّا ٱلْبَلَٰاغُ» (Ḥafṣ 48 ; numérotation
  médinoise — 5e précédent : Muǧādala 21=Ḥ22, Aʿrāf 21=Ḥ22 & 16-15=Ḥ17-16,
  Nisāʾ 118=Ḥ119 & 142=Ḥ143). Sura lue pixel 600 dpi «[الشورى:» + CMS texte
  «الشورى: 45» + la quote contient «إِلَّا» (garble 600 dpi «ذْإلاٌ») qui
  n'existe que en Šūrā 48 (Raʿd 40 = «فَإِنَّمَا عَلَيْكَ» sans إِلَّا).
- Ibn ʿAǧība [البحر المديد: 520/4] : CMS verbatim ✓.
- Rāzī [مفاتيح الغيب: 225/26] : reconstruit triple-canal (CMS verbatim +
  600 dpi : «فلم َل»=فلم يقل, «فَوَغٌ»=فرغ, «المموواضع الْعَيِّنَة»=المواضع
  المعينة, «وَل أَسْنَدَ»=ولما أسند) ; fin «أي على هَيْنَتهَا» (600) /
  «مَيْتَتهَا» (300) / «هَيْئَتِهَا» (CMS) → هيئتها (convergence 6 lettres).
- Idad v10-11 craqué par la règle d'or (glossaire 559 OCR frais) :
  «ٱلْعِزَّةُ» (garble idad «الْعِزَكِ» + def 559 «الشرف والمنعة» = glose
  canonique de العزة) - «مَكْرٌ» (idad 600 dpi «مَكُرٌ» + glossaire 559
  «مَكْزْ/مَكرٌ» + def «المكر ما عمل على سبيل احتيال وخديعة») - «يَبُورُ»
  (idad «يَبُوزٌ» + glossaire 559 «يبور: يهلك ويكسد» — glose Ibn Ǧuzayy
  «ومكرهم يبور») - «أَزْوَاجًا» (idad «أزولماً» + glossaire 559 «أزْوِمِاً»
  + v11 «ثُمَّ جَعَلَكُمْ أَزْوَاجًا»).
- Question istiṯmār complétée du CMS (ligne coupée dans le PDF) : «لماذا
  استعمل الله تعالى الفعل أَرْسَلَ بصيغة الماضي، وعطف عليه الفعل تُثِيرُ
  بصيغة المضارع؟».
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"

HTML_AR = """<h1>سورة فاطر (الآيات: 7-9): كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي للسنة الثانية إعدادي الدرس 3</h1>
<p>درس في تفسير سورة فاطر الآيات (7-9)، كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي، للسنة الثانية من التعليم الإعدادي العتيق (الدرس 3).</p>
<ol>
<li>أن أتعرف قدرة الله تعالى على البعث والحساب.</li>
<li>أن أقارن بين جزاء الطائعين والعاصين يوم القيامة.</li>
<li>أن أهتدي بالمقاصد التي ترشد إليها الآيات.</li>
</ol>
<h2>تمهيد</h2>
<p>بعد تحذير الله تعالى عباده من الاغترار بملذات الحياة الدنيا ومن وساوس الشيطان؛ بين في هذه الآيات أن الناس فريقان: فريق اتبع الشيطان وكفر بالله تعالى فاستحق عذابه؛ وفريق آمن بالله وعمل صالحا فكان جزاؤه المغفرة والأجر العظيم. وفي هذه الآيات أرشد الله سبحانه نبيه ﷺ إلى عدم الحسرة والحزن على من أعرض عن رسالته وكذب بها؛ وبين سبحانه قدرته على البعث.</p>
<p>فكيف قارن الله تعالى بين الفريقين؟ وكيف أستدل على قدرة الله وعظمته انطلاقا من الآيات؟</p>
<h2>الآيات</h2>
<p><span>سورة فاطر: 7-9</span></p>
<p>«ٱلَّذِينَ كَفَرُوا۟ لَهُمْ عَذَابٌۭ شَدِيدٌۭ ۖ وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُم مَّغْفِرَةٌۭ وَأَجْرٌۭ كَبِيرٌ» [فاطر: 7]</p>
<p>«أَفَمَن زُيِّنَ لَهُۥ سُوٓءُ عَمَلِهِۦ فَرَءَاهُ حَسَنًۭا ۖ فَإِنَّ ٱللَّهَ يُضِلُّ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ ۖ فَلَا تَذْهَبْ نَفْسُكَ عَلَيْهِمْ حَسَرَٰتٍ ۚ إِنَّ ٱللَّهَ عَلِيمٌۢ بِمَا يَصْنَعُونَ» [فاطر: 8]</p>
<p>«وَٱللَّهُ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ فَتُثِيرُ سَحَابًۭا فَسُقْنَٰهُ إِلَىٰ بَلَدٍۢ مَّيِّتٍۢ فَأَحْيَيْنَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ كَذَٰلِكَ ٱلنُّشُورُ» [فاطر: 9]</p>
<h2>الفهم</h2>
<h3>الشرح:</h3>
<p>«سُوٓءُ عَمَلِهِ»: قبيح عمله.</p>
<p>«فَتُثِيرُ»: فتحرك بشدة.</p>
<p>«بَلَدٍۢ مَّيِّتٍۢ»: لا نبات فيه.</p>
<p>«ٱلنُّشُورُ»: البعث والحشر.</p>
<h3>استخلاص مضامين الآيات:</h3>
<ol>
<li>ما هو جزاء الكافرين والمؤمنين يوم القيامة؟</li>
<li>عماذا نهى الله تعالى نبيه ﷺ في الآيات؟</li>
<li>بماذا استدل الله تعالى على وقوع البعث؟</li>
</ol>
<h2>التفسير</h2>
<p>اشتملت هذه الآيات على ما يأتي:</p>
<h3>أولا: جزاء الكافرين والمؤمنين:</h3>
<p>قسم الله عز وجل الناس إلى فريقين وبين جزاء كل منهما؛ فقال سبحانه: «ٱلَّذِينَ كَفَرُوا۟ لَهُمْ عَذَابٌۭ شَدِيدٌ» هذا استئناف ابتدائي بمثابة النتيجة لما تقدم؛ فالذين كفروا هم حزب الشيطان وجنوده؛ المستحقون لعذاب دائم شديد يوم القيامة. ونكر «عَذَابٌ» لتعظيم مدته؛ ثم ذكر الله تعالى جزاء ما يقابل هذا الفريق؛ فقال سبحانه: «وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُم مَّغْفِرَةٌۭ وَأَجْرٌۭ كَبِيرٌ» أي: الذين آمنوا بالله ورسله؛ وعملوا الأعمال الصالحة التي ترضي الله؛ جزاؤهم يوم القيامة مغفرة الله تعالى لذنوبهم وإثابتهم الثواب العظيم.</p>
<p>وفي الآية وعيد لمن استجاب لوساوس الشيطان؛ ووعد لمن خالف أمره وعاداه ولم يكن من حزبه. وقد بنى الله تعالى الأمر كله على الإيمان والعمل الصالح؛ فبهما يتمايز الناس يوم القيامة.</p>
<h3>ثانيا: تسلية الله لنبيه ﷺ بعدم الحزن عمن زين لهم سوء أعمالهم:</h3>
<p>أرشد الله تعالى رسوله ﷺ إلى عدم الحزن عمن أعرض عنه وكذب بآيات ربه؛ فقال سبحانه: «أَفَمَن زُيِّنَ لَهُۥ سُوٓءُ عَمَلِهِۦ فَرَءَاهُ حَسَنًۭا» الاستفهام للإنكار؛ وجوابه محذوف تقديره: أفمن زين له سوء عمله؛ كمن لم يزين له؟ فالذي زين له سوء عمله هو الذي أضله الله؛ ومن لم يزين له سوء عمله هو الذي هداه الله؛ ودل على الحذف السابق قوله تعالى: «فَإِنَّ ٱللَّهَ يُضِلُّ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ» قال ابن عجيبة رحمه الله: «أي: فمن أضله رأى الباطل حقا، فتبعه؛ ومن هداه رأى الباطل باطلا، فاجتنبه؛ والحق حقا فاتبعه» [البحر المديد لابن عجيبة: 520/4].</p>
<p>ثم سلى الله تعالى نبيه ﷺ عن حزنه لعدم إيمانهم؛ لأن ذلك بيد الله تعالى؛ فقال سبحانه: «فَلَا تَذْهَبْ نَفْسُكَ عَلَيْهِمْ حَسَرَٰتٍ» أي: فلا تهلك نفسك حسرات باغتمامك على الذين زينت لهم أنفسهم سوء أعمالهم «إِنَّ ٱللَّهَ عَلِيمٌۢ بِمَا يَصْنَعُونَ» أي: إن الله تعالى عليم بما يفعل هؤلاء من الذنوب والمعاصي؛ ومجازيهم على ذلك.</p>
<h3>ثالثا: أدلة القدرة الإلهية على وقوع البعث:</h3>
<p>ولما كان من طبيعة الضالين عن طريق الهدى والصواب؛ إنكار وقوع البعث والنشور؛ لفت الله تعالى نظرهم إلى قدرته التامة على ذلك؛ فقال سبحانه: «وَٱللَّهُ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ» أي: والله تعالى بقدرته هو الذي أطلق الرياح مؤذنة بنزول المطر «فَتُثِيرُ» أي: فتحرك سحابا كان ساكنا؛ وجيء بفعل الماضي في قوله: «أَرْسَلَ» وغير إلى المضارع في قوله: «تُثِيرُ» للدلالة على الحال العجيبة التي تقع فيها إثارة الرياح السحاب «فَسُقْنَٰهُ» أي: فجعلناها تسير إلى بلد لا نبات فيه «فَأَحْيَيْنَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا» أي: فأحيينا به الأرض بعد أن كانت جدباء يابسة «كَذَٰلِكَ ٱلنُّشُورُ» معنى «النشور»: الحشر؛ أي: وكما أحيا الله تعالى الأرض الميتة؛ كذلك يحيي الأموات ويبعثهم للحشر يوم القيامة.</p>
<h3>رابعا: مقاصد الآيات:</h3>
<p>تسعى هذه الآيات إلى تحقيق مقاصد تربوية عديدة؛ منها:</p>
<ul>
<li>مجازاة الله تعالى عباده يوم القيامة بالقسط والعدل كل بما يستحق من خلال جوده على المؤمنين بجنات النعيم؛ وعقابه الكافرين بنار السعير.</li>
<li>توجيه الله تعالى رسوله ﷺ لعدم الحزن على من زين له سوء عمله وضل عن الطريق ليرشده سبحانه إلى نهج أسلوب الحكمة في دعوة الناس إلى الإسلام؛ وتبليغهم رسالته دون إلزامهم بقبول هذه الدعوة أو عدمها؛ فمهمته تقتصر على البلاغ؛ قال تعالى: «إِنْ عَلَيْكَ إِلَّا ٱلْبَلَٰاغُ» [الشورى: 45] وهذا منهج ينبغي للمسلم أن يلتزم به اقتداء بالرسول ﷺ.</li>
<li>إثبات عظمة الله تعالى وقدرته على بعث الناس وحشرهم يوم القيامة؛ بدليل قدرته على إرسال الرياح وما تحركه من سحاب لينزل منه ماء يحيي الأرض بعد موتها؛ ففي إحياء الأرض بعد موتها دليل واضح على البعث.</li>
<li>الدعوة إلى التزكية وتهذيب النفس بالاستجابة لأوامر الله تعالى؛ واجتناب نواهيه؛ والاستعداد بالأعمال الصالحة ليوم القيامة.</li>
</ul>
<h2>التقويم</h2>
<ol>
<li>أقارن بين جزاء المؤمنين وجزاء الكافرين يوم القيامة.</li>
<li>لماذا نهى الله تعالى نبيه ﷺ عن التحسر على الكافرين والمذنبين؟</li>
<li>أربط بين الآيات ومقاصدها الواردة في العنصر الرابع.</li>
</ol>
<h2>الاستثمار</h2>
<p>ذكر فخر الدين الرازي في تفسير قوله تعالى: «وَٱللَّهُ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ فَتُثِيرُ سَحَابًۭا فَسُقْنَٰهُ إِلَىٰ بَلَدٍۢ مَّيِّتٍۢ فَأَحْيَيْنَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ كَذَٰلِكَ ٱلنُّشُورُ» مسائل؛ منها:</p>
<p>الْمَسْأَلَةُ الأُولَى: قَالَ تَعَالَى: «وَٱللَّهُ ٱلَّذِىٓ أَرْسَلَ» بِلَفْظِ الْمَاضِي وَقَالَ: «تُثِيرُ» بِصِيغَةِ الْمُسْتَقْبَلِ، وَذَلِكَ لِأَنَّهُ لَمَّا أَسْنَدَ فِعْلَ الْإِرْسَالِ إِلَى اللَّهِ وَمَا يَفْعَلُ اللَّهُ يَكُونُ بِقَوْلِهِ «كُنْ» فَلَا يَبْقَى فِي الْعَدَمِ لَا زَمَانًا وَلَا جُزْءًا مِنَ الزَّمَانِ، فَلَمْ يَقُلْ بِلَفْظِ الْمُسْتَقْبَلِ لِوُجُوبِ وُقُوعِهِ وَسُرْعَةِ كَوْنِهِ كَأَنَّهُ كَانَ وَكَأَنَّهُ فَرَغَ مِنْ كُلِّ شَيْءٍ، فَهُوَ قَدَّرَ الْإِرْسَالَ فِي الْأَوْقَاتِ الْمَعْلُومَةِ إِلَى الْمَوَاضِعِ الْمُعَيَّنَةِ وَالتَّقْدِيرُ كَالْإِرْسَالِ، وَلَمَّا أَسْنَدَ فِعْلَ الْإِثَارَةِ إِلَى الرِّيحِ وَهُوَ يَؤَلِّفُ فِي زَمَانٍ قَالَ: «تُثِيرُ» أَيْ عَلَى هَيْئَتِهَا.</p>
<p>[مفاتيح الغيب، لفخر الدين الرازي: 225/26]</p>
<p>أتأمل النص وأجيب عن الآتي:</p>
<p>لماذا استعمل الله تعالى الفعل «أَرْسَلَ» بصيغة الماضي؛ وعطف عليه الفعل «تُثِيرُ» بصيغة المضارع؟</p>
<h2>الإعداد القبلي</h2>
<p>أتأمل الآيتين: 10-11 من سورة فاطر وأجيب عن الآتي:</p>
<ol>
<li>أبحث عن مدلولات العبارات الآتية: «ٱلْعِزَّةُ» - «مَكْرٌ» - «يَبُورُ» - «أَزْوَاجًا».</li>
<li>أبحث عن أدلة وقوع البعث من خلال آيات الأنفس.</li>
</ol>"""

HTML_FR = """<h1> Sourate Fāṭir, versets 7-9 : livre du Tafsīr à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy, deuxième année collégiale — leçon 3</h1>
<p>Leçon sur l’exégèse de la sourate Fāṭir, versets 7 à 9, du livre du Tafsīr fondé sur le <em>Tashīl li-ʿulūm al-tanzīl</em> d’Ibn Juzayy, pour la deuxième année de l’enseignement collégial traditionnel (leçon 3).</p>
<ol>
<li>Que je fasse connaissance de la puissance d’Allah — exalté soit-Il — sur la résurrection et le compte.</li>
<li>Que je compare la rétribution des obéissants et celle des désobéissants au Jour de la résurrection.</li>
<li>Que je me guide par les finalités auxquelles ces versets orientent.</li>
</ol>
<h2>Introduction (tamhīd)</h2>
<p>Après qu’Allah — exalté soit-Il — a averti Ses serviteurs contre l’illusion des plaisirs de la vie terrestre et contre les insufflations de Satan, ces versets exposent que les hommes sont deux groupes : un groupe qui a suivi Satan et mécru en Allah — exalté soit-Il — et s’est rendu digne de Son châtiment ; et un groupe qui a cru en Allah et fait œuvre bonne, dont la rétribution a été le pardon et la récompense immense. Et dans ces versets, Allah — exalté soit-Il — a guidé Son Prophète ﷺ vers l’abstention de regret et d’affliction envers celui qui s’est détourné de sa mission et l’a traitée de mensonge ; et Il a exposé Sa puissance sur la résurrection.</p>
<p>Comment donc Allah — exalté soit-Il — a-t-Il comparé les deux groupes ? Et comment établis-je la preuve de la puissance et de la grandeur d’Allah à partir de ces versets ?</p>
<h2>Les versets</h2>
<p><span>Sourate Fāṭir, versets 7 à 9</span></p>
<p>« Ceux qui ont mécru ont un châtiment dur ; et ceux qui croient et font les bonnes œuvres ont, à eux, pardon et récompense immense » (7).</p>
<p>« Et celui dont la laideur de l’action a été embellie, au point qu’il la voit belle… Allah égare qui Il veut et guide qui Il veut. Que ton âme ne se consumpe donc pas de regrets à leur sujet : Allah sait parfaitement ce qu’ils font » (8).</p>
<p>« Et c’est Allah qui envoie les vents, qui soulèvent des nuées ; puis Nous les conduisons vers une contrée morte, et par elles Nous faisons revivre la terre après sa mort. C’est ainsi que sera la résurrection » (9).</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>« suʾu ʿamalih » (la laideur de son action) : le caractère détestable de son action.</p>
<p>« fa-tuṯīru » (et elle soulève) : et elles se mettent en mouvement avec force.</p>
<p>« balad mayyit » (contrée morte) : où nulle végétation n’existe.</p>
<p>« an-nušūr » (la résurrection) : le fait de faire sortir [les morts] et de les rassembler.</p>
<h3>Extraction des contenus des versets</h3>
<ol>
<li>Quelle est la rétribution des mécréants et des croyants au Jour de la résurrection ?</li>
<li>De quoi Allah — exalté soit-Il — a-t-Il interdit Son Prophète ﷺ dans ces versets ?</li>
<li>Par quoi Allah — exalté soit-Il — a-t-Il établi la preuve de la survenance de la résurrection ?</li>
</ol>
<h2>Le Tafsīr</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la rétribution des mécréants et des croyants</h3>
<p>Allah — le Puissant, le Majestueux — a réparti les hommes en deux groupes et exposé la rétribution de chacun, et a dit — exalté soit-Il : « Ceux qui ont mécru ont un châtiment dur » : ceci est un recommencement initial tenant lieu de conséquence de ce qui précède : ceux qui ont mécru sont le parti de Satan et ses soldats, dignes d’un châtiment durable et dur au Jour de la résurrection. Et « châtiment » a été laissé indéterminé pour magnifier sa durée ; puis Allah — exalté soit-Il — a mentionné la rétribution du groupe opposé, et a dit — exalté soit-Il : « et ceux qui croient et font les bonnes œuvres ont, à eux, pardon et récompense immense » : c’est-à-dire ceux qui ont cru en Allah et en Ses messagers, et ont accompli les œuvres bonnes qui satisfisent Allah : leur rétribution, au Jour de la résurrection, est le pardon d’Allah — exalté soit-Il — de leurs fautes, et leur attribution de la récompense immense.</p>
<p>Et il y a dans le verset une menace pour quiconque a répondu aux insufflations de Satan, et une promesse pour quiconque a contredit son ordre, l’a pris en inimitié et n’a pas été de son parti. Et Allah — exalté soit-Il — a édifié toute l’affaire sur la foi et l’œuvre bonne : c’est par elles que les hommes se distinguent au Jour de la résurrection.</p>
<h3>Deuxièmement : la consolation d’Allah envers Son Prophète ﷺ par l’interdiction de s’affliger sur ceux dont les mauvaises actions ont été embellies</h3>
<p>Allah — exalté soit-Il — a guidé Son messager ﷺ à ne pas s’affliger sur celui qui s’est détourné de lui et a traité de mensonge les signes de son Seigneur, et a dit — exalté soit-Il : « Et celui dont la laideur de l’action a été embellie, au point qu’il la voit belle » : l’interrogation est négative, et sa réponse est sous-entendue, son estimation étant : celui dont la laideur de l’action a été embellie — est-il semblable à celui à qui elle n’a pas été embellie ? Celui dont la laideur de l’action a été embellie est celui qu’Allah a égaré ; et celui à qui elle n’a pas été embellie est celui qu’Allah a guidé. Et ce qui indique l’ellipse précédente est Sa parole — exalté soit-Il : « Allah égare qui Il veut et guide qui Il veut ». Ibn ʿAǧība — qu’Allah lui fasse miséricorde — dit : “C’est-à-dire : celui qu’Il a égaré a vu le faux sous l’aspect du vrai et l’a suivi ; et celui qu’Il a guidé a vu le faux sous l’aspect du faux et l’a évité, et le vrai sous l’aspect du vrai et l’a suivi” [al-Baḥr al-madīd, d’Ibn ʿAǧība : 520/4].</p>
<p>Puis Allah — exalté soit-Il — a consolé Son Prophète ﷺ de son affliction pour leur absence de foi — car cela dépend d’Allah — exalté soit-Il —, et a dit : « Que ton âme ne se consumme donc pas de regrets à leur sujet » : c’est-à-dire : ne te fais pas périr d’afflictions, par le chagrin que tu éprouves pour ceux dont les âmes se sont vu embellir leurs mauvaises actions. « Allah sait parfaitement ce qu’ils font » : c’est-à-dire qu’Allah — exalté soit-Il — sait parfaitement ce que ceux-ci commettent comme fautes et péchés, et qu’Il les en rétribuera.</p>
<h3>Troisièmement : les preuves de la puissance divine sur la survenance de la résurrection</h3>
<p>Et puisque c’est de la nature des égarés du chemin de la guidée et de la droiture, de nier la survenance de la résurrection et du rassemblement, Allah — exalté soit-Il — a attiré leur regard sur Sa puissance parfaite en cela, et a dit — exalté soit-Il : « Et c’est Allah qui envoie les vents » : c’est-à-dire : Allah — exalté soit-Il —, par Sa puissance, est Celui qui lance les vents en annonciation de la descente de la pluie. « qui soulèvent des nuées » : c’est-à-dire : et elles mettent en mouvement des nuées qui étaient immobiles. Et le passé a été employé dans Sa parole « Il a envoyé », et l’on est passé au présent dans Sa parole « elles soulèvent », pour marquer l’état étonnant dans lequel se produit l’agitation des nuées par les vents. « puis Nous les conduisons » : c’est-à-dire : Nous les faisons alors marcher vers une contrée où nulle végétation n’existe. « et par elles Nous faisons revivre la terre après sa mort » : c’est-à-dire : Nous faisons revivre par elles la terre, après qu’elle a été aride et sèche. « C’est ainsi que sera la résurrection » : le sens de « la résurrection (an-nušūr) » est le rassemblement ; c’est-à-dire : de même qu’Allah — exalté soit-Il — fait revivre la terre morte, de même Il fait vivre les morts et les fait sortir pour le rassemblement au Jour de la résurrection.</p>
<h3>Quatrièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation de nombreuses finalités éducatives, parmi lesquelles :</p>
<ul>
<li>La rétribution par Allah — exalté soit-Il — de Ses serviteurs au Jour de la résurrection, avec équité et justice, à chacun selon ce qu’il mérite — par Sa générosité envers les croyants par les jardins de délices, et Son châtiment des mécréants par le Feu de la Fournaise.</li>
<li>La guidance donnée par Allah — exalté soit-Il — à Son messager ﷺ, de ne pas s’affliger sur celui dont la mauvaise action a été embellie et qui s’est égaré du chemin, afin de l’orienter vers la voie de la méthode de la sagesse dans l’appel des hommes à l’islam et la transmission de sa mission, sans les contraindre à accepter ou refuser cet appel : sa mission se limite à la transmission. Allah — exalté soit-Il — a dit : « Il ne t’incombe que la transmission » [ach-Chūrā : 45]. Et c’est une méthode à laquelle le musulman doit se tenir, par imitation du Messager ﷺ.</li>
<li>L’affirmation de la grandeur d’Allah — exalté soit-Il — et de Sa puissance à faire sortir les hommes et les rassembler au Jour de la résurrection, à la preuve de Sa capacité d’envoyer les vents et les nuées qu’ils meuvent, d’où descend une eau qui fait vivre la terre après sa mort : dans la vivification de la terre après sa mort, il y a une preuve manifeste de la résurrection.</li>
<li>L’appel à la purification et à l’éducation de l’âme par la réponse aux ordres d’Allah — exalté soit-Il —, l’évitement de Ses interdits, et la préparation, par les œuvres bonnes, au Jour de la résurrection.</li>
</ul>
<h2>L’évaluation</h2>
<ol>
<li>Je compare la rétribution des croyants et celle des mécréants au Jour de la résurrection.</li>
<li>Pourquoi Allah — exalté soit-Il — a-t-Il interdit à Son Prophète ﷺ l’affliction sur les mécréants et les fauteurs ?</li>
<li>Je relie les versets aux finalités exposées dans le quatrième élément.</li>
</ol>
<h2>L’exploitation (istiṯmār)</h2>
<p>Faḫr ad-Dīn ar-Rāzī a mentionné, dans son exégèse de Sa parole — exalté soit-Il : « Et c’est Allah qui envoie les vents, qui soulèvent des nuées ; puis Nous les conduisons vers une contrée morte, et par elles Nous faisons revivre la terre après sa mort. C’est ainsi que sera la résurrection », des questions, parmi lesquelles :</p>
<p>Première question : Allah — exalté soit-Il — a dit « Et c’est Allah qui a envoyé » au passé, et a dit « elles soulèvent » au futur. Cela tient à ce que, lorsqu’Il a attribué l’action de l’envoi à Allah — or ce qu’Allah fait s’accomplit par Sa parole “Sois !”, sans que rien demeure dans le non-être, ni un temps ni une partie de temps —, Il n’a pas employé le futur, en raison de la nécessité de sa survenance et de la rapidité de son advenue : c’est comme s’il avait été, et comme s’Il en avait fini avec toute chose. C’est Lui qui a déterminé l’envoi dans les temps connus vers les lieux désignés, et la détermination est comme l’envoi. Et lorsqu’Il a attribué l’action de l’agitation au vent — lequel se compose dans un temps —, Il a dit : “elles soulèvent”, c’est-à-dire : selon son état propre.</p>
<p>[Mafātīḥ al-ġayb, de Faḫr ad-Dīn ar-Rāzī : 225/26]</p>
<p>Je médite le texte et je réponds à ce qui suit :</p>
<p>Pourquoi Allah — exalté soit-Il — a-t-Il employé le verbe « Il a envoyé » au passé, et y a-t-Il joint le verbe « elles soulèvent » au présent ?</p>
<h2>La préparation préalable (iʿdād qablī)</h2>
<p>Je médite les versets 10 et 11 de la sourate Fāṭir et je réponds à ce qui suit :</p>
<ol>
<li>Je recherche la valeur des expressions suivantes : « al-ʿizza » (la gloire) — « makr » (la ruse) — « yabūr » (il s’anéantit) — « azwāǧan » (en couples).</li>
<li>Je recherche les preuves de la survenance de la résurrection à travers les versets portant sur les personnes.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if str(l.get("docId", "")).endswith("-558"):
            l["html"] = HTML_AR
            l["htmlFr"] = HTML_FR
            l["pdfOnly"] = False
            # correction du titre du catalogue habous (erroné «7-10») — la
            # citation imprimée [سورة فاطر: ٩-٧] + CMS 16808 donnent 7-9
            l["titleAr"] = "سورة فاطر (الآيات : 7 - 9)"
            l["titleFr"] = "Sourate Fatir (versets\u00a0: 7-9)"
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 558 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 558 livrée: AR {len(HTML_AR)} car + FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
