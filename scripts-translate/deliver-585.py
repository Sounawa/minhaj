#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Livraison de la leçon 585 (فهرس المصادر والمراجع, R97-WARSH).

Vérifications R97 :
- Titre : «فهرس المصادر والمراجع» (bande décorative lue pixel + tesseract).
- 30 entrées numérotées ; débuts manqués par l'OCR html reconstruits pixel :
  entrée 1 «القرآن الكريم: برواية ورش عن نافع، الطبعة الصادرة عن مؤسسة
  محمد السادس لطباعة المصحف الشريف، الطبعة الثالثة 2012م» (confirmé ligne
  par ligne + corpus tafsir-5ep verbatim) ; entrée 2 «أحكام القرآن: للقاضي
  محمد بن عبد الله أبي بكر بن العربي المعافري...» (corpus tafsir-tanawi-2
  verbatim) ; entrée 9 «التفسير: لابن أبي حاتم عبد الرحمن بن محمد بن إدريس
  بن المنذر...» (VLM) ; entrée 25 «...بن هلال بن أسد الشيباني (المتوفى:
  241ه)» (ligne p6) ; nisba al-Bayhaqī «الخسروجردي» (VLM lettre à lettre) ;
  السجستاني (correction du garble السحستاني) ; روح البيان/إسماعيل حقي
  (corpus tafsir-5ep : المولى أبو الفداء d.1127) ; الأنجري pour Ibn ʿAǧība
  (corpus tafsir-5ep identique) ; النسفي d.710 (corpus).
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"

HTML_AR = """<h1>فهرس المصادر والمراجع: كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي للسنة الثانية إعدادي</h1>
<ol>
<li><span>القرآن الكريم:</span> برواية ورش عن نافع، الطبعة الصادرة عن مؤسسة محمد السادس لطباعة المصحف الشريف، الطبعة الثالثة 2012م.</li>
<li><span>أحكام القرآن:</span> للقاضي محمد بن عبد الله أبي بكر بن العربي المعافري الإشبيلي المالكي (المتوفى: 543ه)، دار الكتب العلمية، بيروت، لبنان، الطبعة الثالثة، 1424ه، 2003م.</li>
<li><span>الأعلام:</span> لخير الدين بن محمود بن محمد بن علي بن فارس، الزركلي الدمشقي (المتوفى: 1396ه)، دار العلم للملايين، الطبعة الخامسة عشر، 2002م.</li>
<li><span>أنوار التنزيل وأسرار التأويل:</span> لناصر الدين أبي سعيد عبد الله بن عمر بن محمد الشيرازي البيضاوي (المتوفى: 685ه)، تحقيق: محمد عبد الرحمن المرعشلي، دار إحياء التراث العربي، بيروت، الطبعة الأولى، 1418ه.</li>
<li><span>البحر المحيط في التفسير:</span> لأبي حيان محمد بن يوسف بن علي بن يوسف بن حيان أثير الدين الأندلسي (المتوفى: 745ه)، تحقيق: صدقي محمد جميل، دار الفكر، بيروت، طبعة 1420ه.</li>
<li><span>البحر المديد في تفسير القرآن المجيد:</span> لأبي العباس أحمد بن محمد بن المهدي بن عجيبة الحسني الأنجري الفاسي الصوفي (المتوفى: 1224ه)، تحقيق: أحمد عبد الله القرشي رسلان، الطبعة: 1419ه.</li>
<li><span>تحرير المعنى السديد وتنوير العقل الجديد من تفسير الكتاب المجيد:</span> المشهور ب«التحرير والتنوير»، لمحمد الطاهر بن محمد بن محمد الطاهر بن عاشور التونسي (المتوفى: 1393ه)، الدار التونسية للنشر، تونس، 1984م.</li>
<li><span>تفسير القرآن العظيم:</span> لأبي الفداء إسماعيل بن عمر بن كثير القرشي البصري ثم الدمشقي (المتوفى: 774ه)، تحقيق: سامي بن محمد سلامة، دار طيبة للنشر والتوزيع، الطبعة الثانية، 1420ه، 1999م.</li>
<li><span>التفسير:</span> لابن أبي حاتم عبد الرحمن بن محمد بن إدريس بن المنذر التميمي الحنظلي الرازي (المتوفى: 327ه)، تحقيق: أسعد محمد الطيب، مكتبة نزار مصطفى الباز، المملكة العربية السعودية، الطبعة الثالثة، 1419ه.</li>
<li><span>التسهيل لعلوم التنزيل:</span> لأبي القاسم محمد بن أحمد بن محمد بن عبد الله، ابن جزي الكلبي الغرناطي (المتوفى: 741ه)، تحقيق: الدكتور عبد الله الخالدي، شركة دار الأرقم بن أبي الأرقم، بيروت، الطبعة الأولى، 1416ه.</li>
<li><span>جامع البيان في تأويل القرآن:</span> لمحمد بن جرير بن يزيد بن كثير بن غالب الآملي، أبو جعفر الطبري (المتوفى: 310ه)، تحقيق: أحمد محمد شاكر، مؤسسة الرسالة، الطبعة الأولى، 1420ه، 2000م.</li>
<li><span>الجامع المسند الصحيح المختصر من أمور رسول الله ﷺ وسننه وأيامه:</span> المعروف ب«صحيح البخاري»، لمحمد بن إسماعيل أبي عبد الله البخاري الجعفي (المتوفى: 256ه)، تحقيق: محمد زهير بن ناصر الناصر، دار طوق النجاة، الطبعة الأولى، 1422ه.</li>
<li><span>الجامع لأحكام القرآن والمبين لما تضمنه من السنة وآي الفرقان:</span> لأبي عبد الله محمد بن أحمد بن أبي بكر بن فرح الأنصاري الخزرجي شمس الدين القرطبي (المتوفى: 671ه)، تحقيق: أحمد البردوني وإبراهيم أطفيش، دار الكتب المصرية، القاهرة، الطبعة الثانية، 1384ه.</li>
<li><span>روح البيان:</span> لإسماعيل حقي بن مصطفى الإستانبولي الحنفي الخلوتي، المولى أبو الفداء (المتوفى: 1127ه)، دار الفكر، بيروت.</li>
<li><span>روح المعاني في تفسير القرآن العظيم والسبع المثاني:</span> لشهاب الدين محمود بن عبد الله الحسيني الألوسي (المتوفى: 1270ه)، تحقيق: علي عبد الباري عطية، دار الكتب العلمية، بيروت، الطبعة الأولى، 1415ه.</li>
<li><span>سنن ابن ماجه:</span> لابن ماجه أبي عبد الله محمد بن يزيد القزويني، وماجه اسم أبيه يزيد (المتوفى: 273ه)، تحقيق: محمد فؤاد عبد الباقي، دار إحياء الكتب العربية، فيصل عيسى البابي الحلبي.</li>
<li><span>سنن أبي داود:</span> لأبي داود سليمان بن الأشعث بن إسحاق بن بشير بن شداد بن عمرو الأزدي السجستاني (المتوفى: 275ه)، تحقيق: شعيب الأرنؤوط ومحمد كامل قره بللي، دار الرسالة العالمية، الطبعة الأولى، 1430ه، 2009م.</li>
<li><span>سنن الترمذي:</span> لمحمد بن عيسى بن سورة بن موسى بن الضحاك، الترمذي، أبو عيسى (المتوفى: 279ه)، تحقيق وتعليق: أحمد محمد شاكر ومحمد فؤاد عبد الباقي وإبراهيم عطوة عوض، شركة مكتبة ومطبعة مصطفى البابي الحلبي، مصر، الطبعة الثانية، 1395ه.</li>
<li><span>السنن الكبرى:</span> (سنن البيهقي الكبرى)، لأحمد بن الحسين بن علي بن موسى البيهقي أبو بكر، تحقيق: محمد عبد القادر عطا، دار الكتب العلمية، الطبعة الثالثة، 1424ه، 2003م.</li>
<li><span>شعب الإيمان:</span> لأحمد بن الحسين بن علي بن موسى الخسروجردي الخراساني، أبو بكر البيهقي (المتوفى: 458ه)، تحقيق: الدكتور عبد العلي عبد الحميد حامد، مكتبة الرشد للنشر والتوزيع بالرياض، الطبعة الأولى، 1423ه، 2003م.</li>
<li><span>الشفا بتعريف حقوق المصطفى:</span> للقاضي عياض بن موسى بن عياض بن عمرون اليحصبي السبتي، أبو الفضل (المتوفى: 544ه)، دار الفيحاء، عمان، الطبعة الثانية، 1407ه.</li>
<li><span>الكشاف عن حقائق غوامض التنزيل:</span> لأبي القاسم محمود بن عمرو بن أحمد، الزمخشري جار الله (المتوفى: 538ه)، دار الكتاب العربي، بيروت، الطبعة الثالثة، 1407ه.</li>
<li><span>المحرر الوجيز في تفسير الكتاب العزيز:</span> لأبي محمد عبد الحق بن غالب بن عبد الرحمن بن تمام بن عطية الأندلسي المحاربي (المتوفى: 542ه)، تحقيق: عبد السلام عبد الشافي محمد، دار الكتب العلمية، بيروت، الطبعة الأولى، 1422ه.</li>
<li><span>مدارك التنزيل وحقائق التأويل:</span> المشهور بتفسير النسفي، لأبي البركات عبد الله بن أحمد بن محمود حافظ الدين النسفي (المتوفى: 710ه)، تحقيق: يوسف علي بديوي، دار الكلم الطيب، بيروت، الطبعة الأولى، 1419ه.</li>
<li><span>مسند الإمام أحمد بن حنبل:</span> لأبي عبد الله أحمد بن محمد بن حنبل بن هلال بن أسد الشيباني (المتوفى: 241ه)، تحقيق: أحمد محمد شاكر، دار الحديث، القاهرة، الطبعة الأولى، 1416ه، 1995م.</li>
<li><span>مسند الدارمي المعروف بـ«سنن الدارمي»:</span> لأبي محمد عبد الله بن عبد الرحمن بن الفضل بن بهرام بن عبد الصمد الدارمي التميمي السمرقندي (المتوفى: 255ه)، تحقيق: حسين سليم أسد الداراني، دار المغني للنشر والتوزيع، المملكة العربية السعودية، الطبعة الأولى، 1412ه، 2000م.</li>
<li><span>المسند الصحيح المختصر بنقل العدل عن العدل إلى رسول الله ﷺ:</span> لمسلم بن الحجاج أبو الحسين القشيري النيسابوري (المتوفى: 261ه)، تحقيق: محمد فؤاد عبد الباقي، دار إحياء التراث العربي، بيروت.</li>
<li><span>المعجم الأوسط:</span> لسليمان بن أحمد بن أيوب بن مطير اللخمي الشامي، أبو القاسم الطبراني (المتوفى: 360ه)، تحقيق: طارق بن عوض الله بن محمد، عبد المحسن بن إبراهيم الحسيني، دار الحرمين، القاهرة.</li>
<li><span>مفاتيح الغيب ويسمى التفسير الكبير:</span> لأبي عبد الله محمد بن عمر بن الحسن بن الحسين التيمي الرازي الملقب بفخر الدين الرازي خطيب الري (المتوفى: 606ه)، دار إحياء التراث العربي، بيروت، الطبعة الثالثة، 1420ه.</li>
<li><span>الموطأ:</span> للإمام مالك بن أنس بن مالك بن عامر الأصبحي المدني (المتوفى: 179ه)، صححه ورقمه وخرج أحاديثه وعلق عليه: محمد فؤاد عبد الباقي، دار إحياء التراث العربي، بيروت، لبنان، 1406ه، 1985م.</li>
</ol>"""

HTML_FR = """<h1>Sources et références — Le Livre d'exégèse fondé sur le Tashīl li-ʿulūm al-tanzīl d'Ibn Ǧuzayy, deuxième année de l'enseignement collégial traditionnel</h1>
<ol>
<li>Le Coran noble, selon la transmission (riwāya) de Warsh d'après Nāfiʿ, édition de la Fondation Muḥammad VI pour l'impression du Noble Muṣḥaf, 3e édition, 2012.</li>
<li>Aḥkām al-Qurʾān [Les Règles tirées du Coran], du qāḍī Muḥammad ibn ʿAbd Allāh Abī Bakr ibn al-ʿArabī al-Maʿāfirī al-Ishbīlī al-Mālikī (mort en 543 H.), Dār al-Kutub al-ʿIlmiyya, Beyrouth, Liban, 3e édition, 1424 H., 2003.</li>
<li>al-Aʿlām [Les personnalités éminentes], de Khayr al-Dīn ibn Maḥmūd ibn Muḥammad ibn ʿAlī ibn Fāris, al-Ziriklī al-Dimashqī (mort en 1396 H.), Dār al-ʿIlm li-l-Malāyīn, 15e édition, 2002.</li>
<li>Anwār al-Tanzīl wa-asrār al-Taʾwīl [Les Lumières de la révélation et les secrets de l'interprétation], de Nāṣir al-Dīn Abī Saʿīd ʿAbd Allāh ibn ʿUmar ibn Muḥammad al-Shīrāzī al-Bīḍāwī (mort en 685 H.), établissement du texte par Muḥammad ʿAbd al-Raḥmān al-Marʿashlī, Dār Iḥyāʾ al-Turāth al-ʿArabī, Beyrouth, 1re édition, 1418 H.</li>
<li>al-Baḥr al-Muḥīṭ fī al-Tafsīr [L'Océan enveloppant, en exégèse], d'Abū Ḥayyān Muḥammad ibn Yūsuf ibn ʿAlī ibn Yūsuf ibn Ḥayyān Athīr al-Dīn al-Andalusī (mort en 745 H.), établissement du texte par Ṣidqī Muḥammad Jamīl, Dār al-Fikr, Beyrouth, édition 1420 H.</li>
<li>al-Baḥr al-Madīd fī tafsīr al-Qurʾān al-Maǧīd [L'Océan prodigieux, en exégèse du glorieux Coran], d'Abū al-ʿAbbās Aḥmad ibn Muḥammad ibn al-Mahdī ibn ʿAǧība al-Ḥasanī al-Anǧarī al-Fāsī al-Ṣūfī (mort en 1224 H.), établissement du texte par Aḥmad ʿAbd Allāh al-Qurashī Raslān, édition 1419 H.</li>
<li>Taḥrīr al-maʿnā al-sadīd wa-tanwīr al-ʿaql al-ǧadīd min tafsīr al-kitāb al-maǧīd [La Libération du sens fidèle et l'illumination de la raison neuve], connu sous le nom d'« al-Taḥrīr wa-l-Tanwīr », de Muḥammad al-Ṭāhir ibn Muḥammad ibn Muḥammad al-Ṭāhir ibn ʿĀshūr al-Tūnisī (mort en 1393 H.), al-Dār al-Tūnisiyya li-l-Nashr, Tunis, 1984.</li>
<li>Tafsīr al-Qurʾān al-ʿAẓīm [L'Exégèse du noble Coran], d'Abū al-Fidāʾ Ismāʿīl ibn ʿUmar ibn Kathīr al-Qurashī al-Baṣrī puis al-Dimashqī (mort en 774 H.), établissement du texte par Sāmī ibn Muḥammad Salāma, Dār Ṭayba li-l-Nashr wa-l-Tawzīʿ, 2e édition, 1420 H., 1999.</li>
<li>al-Tafsīr [L'Exégèse], d'Ibn Abī Ḥātim ʿAbd al-Raḥmān ibn Muḥammad ibn Idrīs ibn al-Mundhir al-Tamīmī al-Ḥanẓalī al-Rāzī (mort en 327 H.), établissement du texte par Asʿad Muḥammad al-Ṭayyib, Maktabat Nizār Muṣṭafā al-Bāz, Arabie saoudite, 3e édition, 1419 H.</li>
<li>al-Tashīl li-ʿulūm al-tanzīl [La Facilitation des sciences de la Révélation], d'Abū al-Qāsim Muḥammad ibn Aḥmad ibn Muḥammad ibn ʿAbd Allāh, Ibn Ǧuzayy al-Kalbī al-Gharnāṭī (mort en 741 H.), établissement du texte par le docteur ʿAbd Allāh al-Khālidī, Sharikat Dār al-Arqaṣ ibn Abī al-Arqaṣ, Beyrouth, 1re édition, 1416 H.</li>
<li>Ǧāmiʿ al-bayān fī taʾwīl al-Qurʾān [Le Recueil de l'exposé, sur l'interprétation du Coran], de Muḥammad ibn Ǧarīr ibn Yazīd ibn Kathīr ibn Ghālib al-Āmulī, Abū Ǧaʿfar al-Ṭabarī (mort en 310 H.), établissement du texte par Aḥmad Muḥammad Shākir, Muʾassasat al-Risāla, 1re édition, 1420 H., 2000.</li>
<li>al-Ǧāmiʿ al-musnad al-ṣaḥīḥ al-mukhtaṣar min umūr rasūl Allāh ﷺ wa-sunanihi wa-ayyāmihi [Le Recueil authentique abrégé des affaires du messager d'Allah, de ses sunna et de ses jours], connu sous le nom de « Ṣaḥīḥ al-Bukhārī », de Muḥammad ibn Ismāʿīl Abī ʿAbd Allāh al-Bukhārī al-Ǧuʿfī (mort en 256 H.), établissement du texte par Muḥammad Zuhayr ibn Nāṣir al-Nāṣir, Dār Ṭawq al-Najāh, 1re édition, 1422 H.</li>
<li>al-Ǧāmiʿ li-aḥkām al-Qurʾān wa-l-mubayyin li-mā taḍammana min al-sunna wa-āy al-furqān [Le Recueil des règles du Coran et l'exposant de ce qu'il contient de sunna et de versets du discernement], d'Abū ʿAbd Allāh Muḥammad ibn Aḥmad ibn Abī Bakr ibn Farḥ al-Anṣārī al-Khazraǧī Shams al-Dīn al-Qurṭubī (mort en 671 H.), établissement du texte par Aḥmad al-Bardūnī et Ibrāhīm Aṭfīsh, Dār al-Kutub al-Miṣriyya, Le Caire, 2e édition, 1384 H.</li>
<li>Rūḥ al-Bayān [L'Esprit de l'exposition], d'Ismāʿīl Ḥaqqī ibn Muṣṭafā al-Istanbūlī al-Ḥanafī al-Khalwatī, al-Mawlā Abū al-Fidāʾ (mort en 1127 H.), Dār al-Fikr, Beyrouth.</li>
<li>Rūḥ al-maʿānī fī tafsīr al-Qurʾān al-ʿaẓīm wa-l-sabʿ al-mathānī [L'Esprit des sens, en exégèse du noble Coran et des sept répétées], de Shihāb al-Dīn Maḥmūd ibn ʿAbd Allāh al-Ḥusaynī al-Ālūsī (mort en 1270 H.), établissement du texte par ʿAlī ʿAbd al-Bārī ʿAṭiyya, Dār al-Kutub al-ʿIlmiyya, Beyrouth, 1re édition, 1415 H.</li>
<li>Sunan Ibn Māǧa [Les Sunna d'Ibn Māǧa], d'Ibn Māǧa Abī ʿAbd Allāh Muḥammad ibn Yazīd al-Qazwīnī — Māǧa étant le nom de son père Yazīd — (mort en 273 H.), établissement du texte par Muḥammad Fuʾād ʿAbd al-Bāqī, Dār Iḥyāʾ al-Kutub al-ʿArabiyya, Fayṣal ʿĪsā al-Bābī al-Ḥalabī.</li>
<li>Sunan Abī Dāwūd [Les Sunna d'Abū Dāwūd], d'Abū Dāwūd Sulaymān ibn al-Ashʿath ibn Isḥāq ibn Bashīr ibn Shaddād ibn ʿAmr al-Azdī al-Sijistānī (mort en 275 H.), établissement du texte par Shuʿayb al-Arnaʾūṭ et Muḥammad Kāmil Qara Bilalī, Dār al-Risāla al-ʿĀlamiyya, 1re édition, 1430 H., 2009.</li>
<li>Sunan al-Tirmidhī [Les Sunna d'al-Tirmidhī], de Muḥammad ibn ʿĪsā ibn Sawra ibn Mūsā ibn al-Ḍaḥḥāk, al-Tirmidhī, Abū ʿĪsā (mort en 279 H.), établissement du texte et annotations par Aḥmad Muḥammad Shākir, Muḥammad Fuʾād ʿAbd al-Bāqī et Ibrāhīm ʿAṭwa ʿAwḍ, Sharikat Maktabat wa-Maṭbaʿat Muṣṭafā al-Bābī al-Ḥalabī, Égypte, 2e édition, 1395 H.</li>
<li>al-Sunan al-Kubrā [Les grandes Sunna] (Sunan al-Bayhaqī al-Kubrā), d'Aḥmad ibn al-Ḥusayn ibn ʿAlī ibn Mūsā al-Bayhaqī Abū Bakr, établissement du texte par Muḥammad ʿAbd al-Qādir ʿAṭāʾ, Dār al-Kutub al-ʿIlmiyya, 3e édition, 1424 H., 2003.</li>
<li>Shuʿab al-īmān [Les branches de la foi], d'Aḥmad ibn al-Ḥusayn ibn ʿAlī ibn Mūsā al-Khusrawjardī al-Khurāsānī, Abū Bakr al-Bayhaqī (mort en 458 H.), établissement du texte par le docteur ʿAbd al-ʿAlī ʿAbd al-Ḥamīd Ḥāmid, Maktabat al-Rushd li-l-Nashr wa-l-Tawzīʿ, Riyad, 1re édition, 1423 H., 2003.</li>
<li>al-Shifāʾ bi-taʿrīf ḥuqūq al-Muṣṭafā [La Guérison par la reconnaissance des droits de l'Élu], du qāḍī ʿIyāḍ ibn Mūsā ibn ʿIyāḍ ibn ʿAmrūn al-Yaḥṣubī al-Sabtī, Abū al-Faḍl (mort en 544 H.), Dār al-Fayḥāʾ, Amman, 2e édition, 1407 H.</li>
<li>al-Kashshāf ʿan ḥaqāʾiq ghawāmiḍ al-tanzīl [Le Découvreur des réalités obscures de la Révélation], d'Abū al-Qāsim Maḥmūd ibn ʿAmr ibn Aḥmad, al-Zamakhsharī Ǧār Allāh (mort en 538 H.), Dār al-Kitāb al-ʿArabī, Beyrouth, 3e édition, 1407 H.</li>
<li>al-Muḥarrar al-waǧīz fī tafsīr al-kitāb al-ʿazīz [L'Excellent abrégé, en exégèse du Livre puissant], d'Abū Muḥammad ʿAbd al-Ḥaqq ibn Ghālib ibn ʿAbd al-Raḥmān ibn Tamām ibn ʿAṭiyya al-Andalusī al-Maḥāribī (mort en 542 H.), établissement du texte par ʿAbd al-Salām ʿAbd al-Shāfī Muḥammad, Dār al-Kutub al-ʿIlmiyya, Beyrouth, 1re édition, 1422 H.</li>
<li>Madārik al-tanzīl wa-ḥaqāʾiq al-taʾwīl [Les Lieux de la révélation et les réalités de l'interprétation], connu sous le nom de tafsīr al-Nasafī, d'Abū al-Barakāt ʿAbd Allāh ibn Aḥmad ibn Maḥmūd Ḥāfiẓ al-Dīn al-Nasafī (mort en 710 H.), établissement du texte par Yūsuf ʿAlī Badīwī, Dār al-Kalim al-Ṭayyib, Beyrouth, 1re édition, 1419 H.</li>
<li>Musnad al-imām Aḥmad ibn Ḥanbal [Le Recueil de l'imam Aḥmad ibn Ḥanbal], d'Abū ʿAbd Allāh Aḥmad ibn Muḥammad ibn Ḥanbal ibn Hilāl ibn Asad al-Shaybānī (mort en 241 H.), établissement du texte par Aḥmad Muḥammad Shākir, Dār al-Ḥadīth, Le Caire, 1re édition, 1416 H., 1995.</li>
<li>Musnad al-Dārimī, connu sous le nom de « Sunan al-Dārimī » [Le Recueil d'al-Dārimī], d'Abū Muḥammad ʿAbd Allāh ibn ʿAbd al-Raḥmān ibn al-Faḍl ibn Bahrām ibn ʿAbd al-Ṣamad al-Dārimī al-Tamīmī al-Samarqandī (mort en 255 H.), établissement du texte par Ḥusayn Salīm Asad al-Dārānī, Dār al-Mughnī li-l-Nashr wa-l-Tawzīʿ, Arabie saoudite, 1re édition, 1412 H., 2000.</li>
<li>al-Musnad al-ṣaḥīḥ al-mukhtaṣar bin-naql al-ʿadl ʿan al-ʿadl ilā rasūl Allāh ﷺ [Le Recueil authentique abrégé, transmis de témoin fiable à témoin fiable, jusqu'au messager d'Allah], de Muslim ibn al-Ḥaǧǧāǧ Abū al-Ḥusayn al-Qushayrī al-Naysābūrī (mort en 261 H.), établissement du texte par Muḥammad Fuʾād ʿAbd al-Bāqī, Dār Iḥyāʾ al-Turāth al-ʿArabī, Beyrouth.</li>
<li>al-Muʿǧam al-awsaṭ [Le Dictionnaire moyen], de Sulaymān ibn Aḥmad ibn Ayyūb ibn Maṭīr al-Lakhmī al-Shāmī, Abū al-Qāsim al-Ṭabarānī (mort en 360 H.), établissement du texte par Ṭāriq ibn ʿAwḍ Allāh ibn Muḥammad et ʿAbd al-Muḥsin ibn Ibrāhīm al-Ḥusaynī, Dār al-Ḥaramayn, Le Caire.</li>
<li>Mafātīḥ al-ghayb, dit al-Tafsīr al-Kabīr [Les Clefs du mystère, dit le Grand Tafsīr], d'Abū ʿAbd Allāh Muḥammad ibn ʿUmar ibn al-Ḥasan ibn al-Ḥusayn al-Taymī al-Rāzī, surnommé Fakhr al-Dīn al-Rāzī, Khaṭīb al-Rayy (mort en 606 H.), Dār Iḥyāʾ al-Turāth al-ʿArabī, Beyrouth, 3e édition, 1420 H.</li>
<li>al-Muwaṭṭaʾ [La Voie aplanie], de l'imam Mālik ibn Anas ibn Mālik ibn ʿĀmir al-Aṣbaḥī al-Madanī (mort en 179 H.), revu, numéroté, muni des références des hadiths et annoté par Muḥammad Fuʾād ʿAbd al-Bāqī, Dār Iḥyāʾ al-Turāth al-ʿArabī, Beyrouth, Liban, 1406 H., 1985.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if str(l.get("docId", "")).endswith("-585"):
            l["html"] = HTML_AR
            l["htmlFr"] = HTML_FR
            l["pdfOnly"] = False
            l["titleAr"] = "فهرس المصادر والمراجع"
            l["titleFr"] = "Sources et références (fihris al-maṣādir)"
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 585 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 585 livrée: AR {len(HTML_AR)} car + FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
