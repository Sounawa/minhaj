#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Livraison de la leçon 556 (سورة فاطر 1-3, الدرس ١, R98-WARSH).

Vérifications R98 (méthode Warsh e-verification) :
- Bloc coranique p1 : 3 lignes (basmala centrée 4,5 cm + v1 sur 2 lignes) —
  structure IDENTIQUE à la leçon 570 (Ḥadīd 1-4, basmala dans le v1, livrée
  et vérifiée) : ligne courte centrée = basmala confirmée par croisement.
- v1 vérifiée lettre à lettre contre le squelette tanzil (VLM ligne complète
  conforme, y compris «أُو۟لِىٓ أَجْنِحَةٍۢ» et «يَشَآءُ»).
- p2 : 3 lignes = v2 + v3, rosette finale = ٣ (citation imprimée
  [سورة فاطر: 3-1] = 1-3, format inversé du scan).
- DIVERGENCE WARSH/ḤAFṢ 35:3 : «غَيْرِ» (kasra sous le rāʾ, lecture de Warsh
  'an Nāfiʿ) vs «غَيْرُ» Ḥafṣ (tanzil) — kasra confirmée par 3 sondes VLM
  indépendantes sur crops 1800-2400 dpi (marque SOUS le rāʾ, deux diachrons).
  Squelette adapté en conséquence : «هَلْ مِنْ خَٰلِقٍ غَيْرِ ٱللَّهِ».
- Glossaire : «فَاطِرِ» / «أُولِي أَجْنِحَةٍ» (VLM crop 1600 dpi ×2).
- Citation Qurṭubī (Ibn ʿAbbās, les deux bédouins) vérifiée MOT A MOT contre
  quran.ksu.edu.sa — y compris «حتى أتاني أعرابيان» (أتاني confirmé par
  zoom 2000 dpi : nūn + yāʾ finals) ; réf. 319/14 (VLM digit-shape : ٣=W).
- 2e réf. Qurṭubī : 321/14 (VLM digit-shape : ٣-٢-١ / ١-٤).
- Abū Ḥayyān : 13/9 (VLM digit-shape : ١=trait, ٣=W, ٩=boucle).
- Bayḍāwī : 253/4 (VLM digit-shape : ٢-٥-٣ / ٤) — nombre en fin de ligne
  wrappée, retrouvé par TSV x=4390.
- Ibn Kaṯīr : 24/2 (VLM digit-shape : ٢= crochet, ٤=zigzag / ٢= crochet).
- Nasafī : 76/3 (VLM digit-shape : ٧=V, ٦=courbe / ٣=W).
- Hadith d'Abū Saʿīd al-Ḫudrī (duʿāʾ après rukūʿ) vérifié MOT A MOT contre
  Ṣaḥīḥ Muslim 476 (muslim.lna.io + islamweb) — garbles OCR résolus :
  أهل الثناء والمجد / لا مانع لما أعطيت / ولا معطي لما منعت / ولا ينفع
  ذا الجد منك الجد.
- Note grammaticale «و(من بعده) فيه حذف مضاف» : parenthèse lue par VLM
  (tesseract garble #ماتع#2) = «مِنْ بَعْدِهِ» ✓ cohérent avec v2.
- Idad (expressions v4-6) : «ٱلْأُمُورُ - ٱلْغُرُورُ - حِزْبَهُۥ - ٱلسَّعِيرِ»
  — craqué par croisement avec le glossaire de la leçon 557 (Fāṭir 4-6 :
  الاوز=الْأُمُور، ألْخَرُورَ=الْغُرُور، حِزْيَةُ=حِزْبَهُ) + formes tanzil
  v4/v5/v6 ; E4 confirmé par VLM (lettres ص-ع-ي-ر, «de 35:6»).
- Tafsīr identifié : Ibn Juzayy (gloses «غير منصرفة... العدل والوصف» =
  Tashīl, style du corpus).
- Titre : الدرس 1 (556 = 1er des 28 leçons numérotées : 583=28, 570=15).
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"

HTML_AR = """<h1>سورة فاطر (الآيات: 1-3): كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي للسنة الثانية إعدادي الدرس 1</h1>
<p>درس في تفسير سورة فاطر الآيات (1-3)، كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي، للسنة الثانية من التعليم الإعدادي العتيق (الدرس 1).</p>
<ol>
<li>أن أتعرف مظاهر قدرة الله تعالى من خلال الآيات.</li>
<li>أن أستنتج الغاية من تذكير الله تعالى عباده بنعمه.</li>
<li>أن أشكر الله تعالى على نعمه العظيمة.</li>
</ol>
<h2>تمهيد</h2>
<p>سورة فاطر مكية وآياتها ست وأربعون؛ وقد تضمنت آيات موضوع الدرس القضايا الكبرى للعقيدة الإسلامية المتمثلة في توحيد الله تعالى وإقامة البراهين القاطعة على وجوده وقدرته في إبداع الكون؛ وخلق الملائكة وجعلهم وسائط بينه وبين أنبيائه لتبليغهم رسالاته ووحيه. ثم ذكرت الناس نعم الله ورحمته بهم، وحثتهم على شكره، بالتزام طاعته وطاعة رسوله ﷺ.</p>
<p>فما هي الأدلة القاطعة على قدرة الله تعالى؟ وكيف يسهم استحضار عظمة الخالق في الاستجابة لأوامر الله تعالى ونواهيه وشكره على نعمه؟</p>
<h2>الآيات</h2>
<p><span>سورة فاطر: 1-3</span></p>
<p>«بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ ٱلْحَمْدُ لِلَّهِ فَاطِرِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ جَاعِلِ ٱلْمَلَٰٓئِكَةِ رُسُلًا أُو۟لِىٓ أَجْنِحَةٍۢ مَّثْنَىٰ وَثُلَٰثَ وَرُبَٰعَ ۚ يَزِيدُ فِى ٱلْخَلْقِ مَا يَشَآءُ ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ» [فاطر: 1]</p>
<p>«مَّا يَفْتَحِ ٱللَّهُ لِلنَّاسِ مِن رَّحْمَةٍۢ فَلَا مُمْسِكَ لَهَا ۖ وَمَا يُمْسِكْ فَلَا مُرْسِلَ لَهُۥ مِنۢ بَعْدِهِۦ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ» [فاطر: 2]</p>
<p>«يَٰٓأَيُّهَا ٱلنَّاسُ ٱذْكُرُوا۟ نِعْمَتَ ٱللَّهِ عَلَيْكُمْ ۚ هَلْ مِنْ خَٰلِقٍ غَيْرِ ٱللَّهِ يَرْزُقُكُم مِّنَ ٱلسَّمَآءِ وَٱلْأَرْضِ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ۖ فَأَنَّىٰ تُؤْفَكُونَ» [فاطر: 3]</p>
<h2>الفهم</h2>
<h3>الشرح:</h3>
<p>«فَاطِرِ»: الخالق ابتداء.</p>
<p>«أُو۟لِىٓ أَجْنِحَةٍ»: ذوي أجنحة.</p>
<h3>استخلاص مضامين الآيات:</h3>
<ol>
<li>ما هي الأدلة التي تضمنتها هذه الآيات؟</li>
<li>بم ذكر الله تعالى عباده في هذه الآيات؟</li>
</ol>
<h2>التفسير</h2>
<p>اشتملت هذه الآيات على ما يأتي:</p>
<h3>أولا: من أدلة القدرة الإلهية:</h3>
<p>افتتح الله سبحانه هذه السورة بقوله: «ٱلْحَمْدُ لِلَّهِ» ليؤذن بأن صفات عظيمة له سبحانه ستذكر فيها؛ وقد أثنى الله تعالى على ذاته بهذا الحمد تعظيما لنفسه وتعليما لخلقه بأن يثنوا عليه بذلك؛ والألف واللام في قوله: «ٱلْحَمْدُ لِلَّهِ» للاستغراق؛ أي: جميع المحامد ثابت له سبحانه.</p>
<p>(«فَاطِرِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ») الْفَطْرُ: الابتداء والاختراع. قال ابن عباس: كُنْتُ لا أَدْرِي ما (فَاطِرَ السَّمَاوَاتِ وَالْأَرْضِ) حَتَّى أَتَانِيَ أَعْرَابِيَّانِ يَخْتَصِمَانِ فِي بِئْرٍ، فَقَالَ أَحَدُهُمَا: أَنَا فَطَرْتُهَا، أَيْ أَنَا ابْتَدَأْتُهَا (...) والمراد بذكر السموات والأرض العالم كله؛ ونبه بهذا على أن من قدر على الابتداء قادر على الإعادة» [الجامع لأحكام القرآن؛ للإمام القرطبي: 319/14].</p>
<p>وقوله تعالى: «جَاعِلِ ٱلْمَلَٰٓئِكَةِ رُسُلًا» أي: وسائط بين الله وبين الأنبياء متصرفين في أمر الله.</p>
<p>وقوله تعالى: «أُو۟لِىٓ أَجْنِحَةٍۢ مَّثْنَىٰ وَثُلَٰثَ وَرُبَٰعَ» أي: ذوي أجنحة؛ والصفات التي بعدها للأجنحة؛ وهي غير منصرفة؛ والمانع لها من الصرف العدل والوصف؛ والمعنى: أن الملائكة منهم من له جناحان؛ ومنهم من له ثلاثة أجنحة؛ ومنهم من له أربعة أجنحة.</p>
<p>«يَزِيدُ فِى ٱلْخَلْقِ مَا يَشَآءُ» الآية تتناول زيادات الصور والمعاني. «قيل: يعني حسن الصوت؛ وقيل: حسن الوجه؛ وقيل: حسن الخط» والأظهر أنه يرجع إلى أجنحة الملائكة؛ أو يكون على الإطلاق في كل زيادة في المخلوقين.</p>
<p>وقوله تعالى: «إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ» أي: هو تعالى قادر على ما يريد؛ لا يمتنع عليه فعل شيء أراده؛ ولا يعجزه شيء.</p>
<h3>ثانيا: التذكير بنعم الله على عباده:</h3>
<p>ذكر الله تعالى عباده بنعمه عليهم؛ فقال تعالى: «مَّا يَفْتَحِ ٱللَّهُ لِلنَّاسِ مِن رَّحْمَةٍۢ فَلَا مُمْسِكَ لَهَا ۖ وَمَا يُمْسِكْ فَلَا مُرْسِلَ لَهُۥ مِنۢ بَعْدِهِۦ» الفتح: عبارة عن العطاء؛ والإمساك: عبارة عن المنع. والإرسال: الإطلاق بعد المنع؛ والرحمة كل ما يمن الله به على عباده من خيري الدنيا والآخرة؛ فمعنى الآية: لا مانع لما أعطى الله؛ ولا معطي لما منع الله «وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ» قوله: «ٱلْعَزِيزُ» أي: «الغالب القادر على الإرسال والإمساك» «ٱلْحَكِيمُ»: الذي يرسل ويمسك ما تقتضي الحكمة إرساله وإمساكه» [البحر المحيط في التفسير، لأبي حيان: 13/9].</p>
<p>فإن قيل: لم أنث الضمير في قوله: «فَلَا مُمْسِكَ لَهَا» وذكره في قوله: «فَلَا مُرْسِلَ لَهُۥ مِنۢ بَعْدِهِۦ» وكلاهما يعود على «ما» الشرطية؛ فالجواب: أنه لما فسر «ما» الأولى بقوله «مِنْ رَحْمَةٍ» أنثه لتأنيث الرحمة؛ وترك الآخر على الأصل من التذكير؛ و«مِنْ بَعْدِهِ» فيه حذف مضاف.</p>
<p>وقوله تعالى: «يَٰٓأَيُّهَا ٱلنَّاسُ» نداء لقريش، ويعم الناس كافة؛ للفت انتباههم وإحضار حواسهم، لتلقي الأمر الوارد في قوله تعالى: «ٱذْكُرُوا۟ نِعْمَتَ ٱللَّهِ عَلَيْكُمْ» أي: «احفظوها بمعرفة حقها والاعتراف بها وطاعة موليها» [أنوار التنزيل وأسرار التأويل، للبيضاوي: 253/4].</p>
<p>والمراد بـ«نِعْمَتَ ٱللَّهِ» كل ما أنعم الله به على عباده؛ مما ذكر في الآيات المتقدمة؛ إذ مهد لهم الأرض ورفع السماء فوقها لتيسير حياتهم؛ وأرسل الرسل والأنبياء لبيان السبيل لهم؛ وفتح لهم أبواب رزقه.</p>
<p>ثم أنكر الله تعالى أن يكون لغيره في ذلك مدخل، فقال سبحانه: «هَلْ مِنْ خَٰلِقٍ غَيْرِ ٱللَّهِ» الاستفهام هنا إنكاري بمعنى النفي؛ لذلك اقترن ما بعده بـ«مِنْ» التي تزاد لتأكيد النفي؛ ورفع «غير» على الصفة لخالق بالرفع تبعا للمحل؛ وبالخفض تبعا للفظ. قال القرطبي: «فالرفع من وجهين: أحدهما: بمعنى: هل من خالق إلا الله، بمعنى: ما خالق إلا الله. والوجه الثاني: أن يكون نعتا على الموضع؛ لأن المعنى: هل خالق غير الله و«من» زائدة. والنصب على الاستثناء، والخفض على اللفظ» [الجامع لأحكام القرآن، للقرطبي: 321/14].</p>
<p>وقوله تعالى: «يَرْزُقُكُم مِّنَ ٱلسَّمَآءِ وَٱلْأَرْضِ» أي: يرزقكم من السماء بالمطر، ومن الأرض بالنبات. والمعنى: تذكير الناس بنعم الله تعالى وإقامة الحجة على المشركين؛ ولذلك أعقبه بقوله: «لَآ إِلَٰهَ إِلَّا هُوَ» قال ابن كثير: أي: «التفرد بالإلهية لجميع الخلائق» [تفسير القرآن العظيم، لابن كثير: 24/2]. و«فَأَنَّىٰ تُؤْفَكُونَ» قال النسفي: معناه: «فبأي وجه تصرفون عن التوحيد إلى الشرك؟» [مدارك التنزيل وحقائق التأويل، للنسفي: 76/3].</p>
<h3>ثالثا: مقاصد الآيات:</h3>
<p>ترشد هذه الآيات إلى مقاصد عظيمة، منها:</p>
<ul>
<li>بيان جود الله تعالى وكمال إنعامه على عباده بأصناف النعم والأرزاق والأقوات التي أودعها سبحانه في السموات والأرض.</li>
<li>إثبات وحدانية الله تعالى من خلال وصفه نفسه بالوحدانية والقدرة على خلق السموات والأرض وخلق الملائكة.</li>
<li>بيان شمول خطاب الله تعالى للناس كافة دون تخصيص أو تقييد.</li>
<li>أهمية حماية حقوق الناس من كل اعتداء، فلا معطي إلا الله ولا مانع إلا هو سبحانه؛ ومن هنا يتبين أن الإسلام اهتم بحقوق الإنسان التي هي غاية كل تشريع.</li>
</ul>
<h2>التقويم</h2>
<ol>
<li>أستخرج من الآيات أدلة قدرة الله تعالى وعظمته.</li>
<li>أستخلص من الآيات آلاء الله سبحانه على عباده.</li>
<li>كيف أهتدي بهذه الآيات لتحقيق شكر الله تعالى؟</li>
</ol>
<h2>الاستثمار</h2>
<p>عن أبي سعيد الخدري رضي الله عنه، قال: «كان رسول الله ﷺ إذا رفع رأسه من الركوع قال: ربنا لك الحمد ملء السماوات والأرض، وملء ما شئت من شيء بعد، أهل الثناء والمجد، أحق ما قال العبد، وكلنا لك عبد: اللهم لا مانع لما أعطيت، ولا معطي لما منعت، ولا ينفع ذا الجد منك الجد» [صحيح مسلم؛ كتاب الصلاة؛ باب ما يقول إذا رفع رأسه من الركوع].</p>
<p>أتأمل النص وأجيب عن الآتي:</p>
<ol>
<li>أستنتج من النص ما يفيد ضمان الله سبحانه لحقوق الناس.</li>
<li>كيف يسهم ذلك في تزكية نفسي وتهذيبها؟</li>
</ol>
<h2>الإعداد القبلي</h2>
<p>أتأمل الآيات: 4-6 من سورة فاطر وأجيب عن الآتي:</p>
<ol>
<li>أبحث عن مدلولات العبارات الآتية: «ٱلْأُمُورُ» - «ٱلْغُرُورُ» - «حِزْبَهُۥ» - «ٱلسَّعِيرِ».</li>
<li>أبحث عن الأمور التي حذر الله من الاغترار بها؛ والغاية من هذا التحذير.</li>
</ol>"""

HTML_FR = """<h1> Sourate Fāṭir, versets 1-3 : livre du Tafsīr à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy, deuxième année collégiale — leçon 1</h1>
<p>Leçon sur l’exégèse de la sourate Fāṭir, versets 1 à 3, du livre du Tafsīr fondé sur le <em>Tashīl li-ʿulūm al-tanzīl</em> d’Ibn Juzayy, pour la deuxième année de l’enseignement collégial traditionnel (leçon 1).</p>
<ol>
<li>Que je fasse connaissance des manifestations de la puissance d’Allah — exalté soit-Il — à travers les versets.</li>
<li>Que je dégage la finalité du rappel par Allah — exalté soit-Il — de Ses bienfaits envers Ses serviteurs.</li>
<li>Que je remercie Allah — exalté soit-Il — pour Ses bienfaits immenses.</li>
</ol>
<h2>Introduction (tamhīd)</h2>
<p>La sourate Fāṭir est mecquoise et compte quarante-six versets. Les versets objet de la leçon ont traité les grandes questions du dogme islamique que sont l’unicité d’Allah — exalté soit-Il — et l’établissement des preuves décisives de Son existence et de Sa puissance dans la création de l’univers, ainsi que la création des anges et leur institution comme intermédiaires entre Lui et Ses prophètes, pour leur transmettre Ses messages et Sa révélation. Puis [la sourate] a rappelé aux hommes les bienfaits d’Allah et Sa miséricorde envers eux, et les a exhortés à Le remercier par l’engagement dans Son obéissance et celle de Son messager ﷺ.</p>
<p>Quelles sont donc les preuves décisives de la puissance d’Allah — exalté soit-Il ? Et comment la présence d’esprit de la grandeur du Créateur contribue-t-elle à répondre aux ordres et aux interdits d’Allah — exalté soit-Il — et à Le remercier de Ses bienfaits ?</p>
<h2>Les versets</h2>
<p><span>Sourate Fāṭir, versets 1 à 3</span></p>
<p>« Au nom d’Allah, le Tout-Miséricordieux, le Très-Miséricordieux. Louange à Allah, Créateur (Fāṭir) des cieux et de la terre, qui a fait des anges des messagers dotés d’ailes — deux, trois ou quatre. Il ajoute à la création ce qu’Il veut : Allah est, sur toute chose, Omnipotent » (1).</p>
<p>« Ce qu’Allah ouvre aux hommes comme miséricorde, nul ne peut le retenir ; et ce qu’Il retient, nul ne peut le relâcher après Lui. Et c’est Lui le Puissant, le Sage » (2).</p>
<p>« Ô hommes ! Rappelez-vous le bienfait d’Allah sur vous. Y a-t-il un créateur en dehors d’Allah, qui vous attribue la subsistance du ciel et de la terre ? Point de divinité en dehors de Lui. Comment vous laissez-vous détourner ? » (3).</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>« fāṭir » (Créateur) : qui crée à l’origine, sans modèle préalable.</p>
<p>« ulī ajniḥatin » (dotés d’ailes) : possesseurs d’ailes.</p>
<h3>Extraction des contenus des versets</h3>
<ol>
<li>Quelles sont les preuves comprises dans ces versets ?</li>
<li>Par quoi Allah — exalté soit-Il — a-t-Il interpellé Ses serviteurs dans ces versets ?</li>
</ol>
<h2>Le Tafsīr</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : parmi les preuves de la puissance divine</h3>
<p>Allah — exalté soit-Il — a ouvert cette sourate par Sa parole « al-ḥamdu li-llāh » (louange à Allah) pour avertir que des attributs immenses Lui seront mentionnés en elle ; Allah — exalté soit-Il — S’est loué Lui-même par cette louange, afin de Se magnifier et d’enseigner à Sa création de Le louer ainsi ; et l’alif et le lām de Sa parole « al-ḥamdu li-llāh » marquent l’exhaustivité : toutes les louanges Lui appartiennent de façon permanente — exalté soit-Il.</p>
<p>(« Créateur (Fāṭir) des cieux et de la terre ») : al-fatr : l’institution à l’origine et l’invention. Ibn ʿAbbās — qu’Allah soit satisfait de lui — dit : « Je ne savais pas ce qu’était (“Créateur des cieux et de la terre”) jusqu’à ce que me viennent deux bédouins se disputant au sujet d’un puits ; l’un d’eux dit : anā faṭartuhā — “moi, je l’ai fait naître”, c’est-à-dire : “moi, je l’ai instituée à l’origine” (...) Ce que visent la mention des cieux et de la terre, c’est l’univers tout entier ; et Il a indiqué par là que Celui qui est capable d’instituer à l’origine est capable de faire revenir [la création] » [al-Ǧāmiʿ li-aḥkām al-Qurʾān, de l’imām al-Qurṭubī : 319/14].</p>
<p>Et Sa parole — exalté soit-Il : « qui a fait des anges des messagers » : c’est-à-dire des intermédiaires entre Allah et les prophètes, agissant dans Son ordre.</p>
<p>Et Sa parole — exalté soit-Il : « dotés d’ailes — deux, trois et quatre » : c’est-à-dire possesseurs d’ailes ; et les adjectifs qui les suivent se rapportent aux ailes ; ils sont invariables (ġayr munṣarif) ; ce qui les empêche de se décliner est le détournement de l’usage (ʿadl) et la qualification (waṣf) ; et le sens est que, parmi les anges, il en est qui ont deux ailes, il en est qui en ont trois, et il en est qui en ont quatre.</p>
<p>« Il ajoute à la création ce qu’Il veut » : le verset englobe les additions des formes et des significations. « On a dit : cela signifie la beauté de la voix ; on a dit : la beauté du visage ; on a dit : la beauté de l’écriture » — et l’avis le plus apparent est qu’il renvoie aux ailes des anges, ou qu’il vaut absolument toute addition dans les créatures.</p>
<p>Et Sa parole — exalté soit-Il : « Allah est, sur toute chose, Omnipotent » : c’est-à-dire qu’Il — exalté soit-Il — est capable de ce qu’Il veut ; aucun acte qu’Il veut ne Lui est impossible, et rien ne L’accable.</p>
<h3>Deuxièmement : le rappel des bienfaits d’Allah envers Ses serviteurs</h3>
<p>Allah — exalté soit-Il — a rappelé à Ses serviteurs Ses bienfaits envers eux et a dit — exalté soit-Il : « Ce qu’Allah ouvre aux hommes comme miséricorde, nul ne peut le retenir ; et ce qu’Il retient, nul ne peut le relâcher après Lui ». L’ouverture (fatḥ) désigne la donation ; la retenue (imsāk) désigne la privation ; l’envoi (irsāl) est la libération après la privation ; et la miséricorde (raḥma) est tout ce qu’Allah accorde en bien à Ses serviteurs parmi les biens de ce monde et de l’au-delà. Le sens du verset est donc : nul ne retient ce qu’Allah a donné, et nul ne donne ce qu’Allah a retenu — « Et c’est Lui le Puissant, le Sage » : Sa parole « al-ʿAzīz » (le Puissant) signifie « le Dominateur, capable de l’envoi et de la retenue » ; « al-Ḥakīm » (le Sage) : « Celui qui envoie et retient ce dont la sagesse exige l’envoi ou la retenue » [al-Baḥr al-muḥīṭ fī at-tafsīr, d’Abū Ḥayyān : 13/9].</p>
<p>Si l’on demande : pourquoi le pronom a-t-il été mis au féminin dans Sa parole « nul ne peut la retenir », et au masculin dans Sa parole « nul ne peut le relâcher après lui », alors que l’un et l’autre renvoient au « mā » conditionnel ? — la réponse est que, lorsqu’Il a interprété le premier « mā » par Sa parole « comme miséricorde », Il l’a mis au féminin en raison du féminin de raḥma, et a laissé l’autre sur l’origine, le masculin ; et dans « après lui » il y a ellipse d’un complément déterminé.</p>
<p>Et Sa parole — exalté soit-Il : « Ô hommes » est une apostrophe aux Quraysh qui englobe les hommes tous ensemble, pour éveiller leur attention et mobiliser leurs sens, afin qu’ils reçoivent l’ordre formulé dans Sa parole — exalté soit-Il : « Rappelez-vous le bienfait d’Allah sur vous », c’est-à-dire : « préservez-le par la connaissance de son droit, la reconnaissance de celui-ci et l’obéissance à son Maître » [Anwār at-tanzīl wa-asrār at-taʾwīl, d’al-Bayḍāwī : 253/4].</p>
<p>Ce que vise « le bienfait d’Allah », c’est tout ce qu’Allah a accordé comme bienfait à Ses serviteurs parmi ce qui a été mentionné dans les versets précédents : Il leur a aplani la terre et élevé le ciel au-dessus d’elle pour faciliter leur vie, Il a envoyé les messagers et les prophètes pour leur exposer la voie, et ouvert pour eux les portes de Sa subsistance.</p>
<p>Puis Allah — exalté soit-Il — a nié qu’autre que Lui ait une part en cela, et a dit — exalté soit-Il : « Y a-t-il un créateur en dehors d’Allah ». L’interrogation est ici négative, au sens de la négation ; c’est pourquoi ce qui la suit est lié à « min », qui est ajoutée pour renforcer la négation ; et « ġayr » est muni de l’élévation comme adjectif de « créateur », à la suite de la fonction syntaxique, et de l’inclinaison à la suite de la forme littérale. Al-Qurṭubī dit : « L’élévation se justifie de deux manières : la première, au sens de : y a-t-il un créateur hormis Allah — c’est-à-dire : il n’est de créateur qu’Allah ; la seconde, qu’il soit une qualification selon la position, car le sens est : y a-t-il un créateur autre qu’Allah, et « min » est superflue. L’accusatif est celui de l’exception, et l’inclinaison celui de la forme littérale » [al-Ǧāmiʿ li-aḥkām al-Qurʾān, d’al-Qurṭubī : 321/14].</p>
<p>Et Sa parole — exalté soit-Il : « qui vous attribue la subsistance du ciel et de la terre » : c’est-à-dire : Il vous attribue la subsistance, du ciel par la pluie, et de la terre par les plantations. Le sens est le rappel aux hommes des bienfaits d’Allah — exalté soit-Il — et l’établissement de l’argument contre les polythéistes ; c’est pourquoi il l’a fait suivre de Sa parole : « Point de divinité en dehors de Lui ». Ibn Kaṯīr dit, c’est-à-dire : « l’exclusivité de la divinité pour l’ensemble des créatures » [Tafsīr al-Qurʾān al-ʿAẓīm, d’Ibn Kaṯīr : 24/2]. Et « Comment vous laissez-vous détourner ? » : an-Nasafī dit que son sens est : « selon quelle face vous détournez-vous de l’unicité vers l’association ? » [Madārik at-tanzīl wa-ḥaqāʾiq at-taʾwīl, d’an-Nasafī : 76/3].</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets guident vers des finalités immenses, parmi lesquelles :</p>
<ul>
<li>L’exposé de la générosité d’Allah — exalté soit-Il — et de la perfection de Ses bienfaits envers Ses serviteurs, par les genres de bienfaits, de subsistances et de nourritures qu’Il — exalté soit-Il — a déposés dans les cieux et la terre.</li>
<li>L’affirmation de l’unicité d’Allah — exalté soit-Il — à travers Sa qualification de Lui-même par l’unicité et la capacité de créer les cieux et la terre et de créer les anges.</li>
<li>L’exposé de l’universalité de l’adresse d’Allah — exalté soit-Il — à tous les hommes, sans restriction ni limitation.</li>
<li>L’importance de la protection des droits des hommes contre toute atteinte : il n’est de donateur qu’Allah et nul reteneur que Lui — exalté soit-Il ; et l’on voit par là que l’islam s’est soucié des droits de l’homme, qui sont la finalité de toute législation.</li>
</ul>
<h2>L’évaluation</h2>
<ol>
<li>J’extrais des versets les preuves de la puissance et de la grandeur d’Allah — exalté soit-Il.</li>
<li>Je dégage des versets les bienfaits d’Allah — exalté soit-Il — envers Ses serviteurs.</li>
<li>Comment ces versets me guident-ils vers la réalisation de la gratitude envers Allah — exalté soit-Il ?</li>
</ol>
<h2>L’exploitation (istiṯmār)</h2>
<p>D’après Abū Saʿīd al-Ḫudrī — qu’Allah soit satisfait de lui —, le messager d’Allah ﷺ, lorsqu’il relevait la tête de l’inclination, disait : « Seigneur ! à Toi la louange, autant que remplissent les cieux et la terre, et autant que Tu veux après eux ; Maître de la louange et de la gloire, la plus juste parole du serviteur, et nous sommes tous, à Toi, des serviteurs : ô Allah ! nul ne retient ce que Tu as donné, nul ne donne ce que Tu as retenu, et la fortune ne sauve pas le fortuné de Toi » [Ṣaḥīḥ Muslim ; livre de la prière ; chapitre de ce qu’il dit lorsqu’il relève la tête de l’inclination].</p>
<p>Je médite le texte et je réponds à ce qui suit :</p>
<ol>
<li>Je dégage du texte ce qui atteste de la garantie des droits des hommes par Allah — exalté soit-Il.</li>
<li>Comment cela contribue-t-il à la purification de mon âme et à son éducation ?</li>
</ol>
<h2>La préparation préalable (iʿdād qablī)</h2>
<p>Je médite les versets 4 à 6 de la sourate Fāṭir et je réponds à ce qui suit :</p>
<ol>
<li>Je recherche la valeur des expressions suivantes : « al-umūr » (les affaires) — « al-ġurūr » (la tromperie) — « ḥizbahu » (son parti) — « as-saʿīr » (la Fournaise).</li>
<li>Je recherche les choses dont Allah a averti de ne pas s’y laisser abuser, et la finalité de cet avertissement.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if str(l.get("docId", "")).endswith("-556"):
            l["html"] = HTML_AR
            l["htmlFr"] = HTML_FR
            l["pdfOnly"] = False
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 556 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 556 livrée: AR {len(HTML_AR)} car + FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
