#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Livraison de la leçon 584 (فهرس الأعلام وترجمتهم, R97-WARSH).

Vérifications R97 :
- Titre décoratif lu pixel + VLM : «فهرس الأعلام» (le م final de الأعلام
  confirmé par la forme) + sous-ligne «وترجمتهم» → h1 «فهرس الأعلام وترجمتهم».
- 14 notices, chacune identifiée par son contenu + étiquette de marge.
- Faits biographiques croisés contre le corpus minhaj (tafsir-1ep/5ep/6ep,
  tafsir-tanawi-2 ont des notices aux formulations parallèles) :
  Ibn Ǧuzayy (verbatim tafsir-6ep), Ibn ʿĀshūr (verbatim), Ibn ʿAṭiyya
  (nisba المحاربي confirmée ×3 : tesseract + web + tafsir-6ep), Ibn
  al-ʿArabī (المعافري tesseract ; «والأصول والتفسير والأدب والتاريخ. منها:
  «العواصم»» décodé psm6 5x), dates : 741/327/310/1393/68/1224/542/774/
  543/745/1270/538/606/544 H (Ibn ʿAbbās 68 lu pixel ; Ālūsī 1248 lu 600dpi).
- Nom d'Ibn al-ʿArabī récupéré (ligne manquée par l'OCR html) : «محمد بن عبد
  الله بن محمد؛ أبو بكر بن العربي المعافري».
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"

HTML_AR = """<h1>فهرس الأعلام وترجمتهم: كتاب التفسير من خلال التسهيل لعلوم التنزيل لابن جزي للسنة الثانية إعدادي</h1>
<h3>ابن جزي</h3>
<p>هو محمد بن أحمد بن عبد الله بن يحيى بن عبد الرحمن بن يوسف بن جزي الكلبي الأندلسي؛ ترك كثيرا من الآثار في مختلف فنون العلوم كالفقه والحديث والتصوف والقراءات. من أهم مؤلفاته: كتاب «القوانين الفقهية»؛ وكتاب «التسهيل في علوم التنزيل». توفي رحمه الله سنة 741 ه.</p>
<h3>ابن أبي حاتم</h3>
<p>عبد الرحمن بن محمد بن أبي حاتم بن إدريس بن المنذر التميمي الحنظلي الرازي؛ أبو محمد؛ حافظ للحديث؛ له تصانيف، منها «الجرح والتعديل» و«التفسير»؛ كان منزله في درب حنظلة بالري؛ توفي عام 327 ه.</p>
<h3>ابن جرير الطبري</h3>
<p>محمد بن جرير بن يزيد؛ أبو جعفر الطبري؛ الفقيه المفسر المؤرخ. من أشهر مؤلفاته: «جامع البيان في تفسير القرآن» و«اختلاف الفقهاء» و«أخبار الرسل والملوك» ويعرف بتاريخ الطبري. ولد في آمل طبرستان؛ واستوطن بغداد وتوفي بها سنة 310 ه.</p>
<h3>ابن عاشور</h3>
<p>محمد الطاهر بن عاشور التونسي؛ رئيس المفتين المالكيين بتونس وشيخ جامع الزيتونة وفروعه بتونس. له مؤلفات كثيرة، من أشهرها «مقاصد الشريعة الإسلامية» و«التحرير والتنوير في تفسير القرآن»، وغيرها من المؤلفات. توفي رحمه الله سنة 1393 ه.</p>
<h3>ابن عباس</h3>
<p>عبد الله بن عباس بن عبد المطلب القرشي الهاشمي؛ الصحابي الجليل حبر الأمة؛ ولد بمكة، ونشأ في بدء عصر النبوة؛ فلازم رسول الله ﷺ وروى عنه أحاديث كثيرة، رضي الله عنه، حيث بلغت في الصحيحين وغيرهما نحو 1660 حديثا. وكف بصره في آخر عمره؛ فسكن الطائف، وتوفي بها سنة 68 ه.</p>
<h3>ابن عجيبة</h3>
<p>هو أحمد بن محمد بن المهدي بن الحسين بن محمد المعروف بابن عجيبة، والمكنى بأبي عباس؛ الإمام المفسر. من مؤلفاته: «البحر المديد في تفسير القرآن المجيد»، و«حاشية على مختصر خليل»، و«حاشية على الجامع الصغير» للسيوطي وغيرها. توفي رحمه الله سنة 1224 ه.</p>
<h3>ابن عطية</h3>
<p>هو عبد الحق بن غالب بن عبد الرحمن بن غالب بن عبد الرؤوف بن عبد الله بن تمام بن عطية أبو محمد المحاربي الغرناطي المالكي الأندلسي؛ الفقيه المفسر. تلقى العلم من مشايخ الأندلس؛ ومنهم: أبوه أبو بكر غالب وأبي علي الغساني. له تأليف كثيرة منها: «المحرر الوجيز في تفسير الكتاب العزيز»؛ توفي سنة 542 ه.</p>
<h3>ابن كثير</h3>
<p>هو إسماعيل بن عمر بن كثير؛ أبو الفداء الدمشقي الشافعي؛ الإمام الحافظ المحدث المؤرخ. من أشهر مؤلفاته: «تفسير القرآن العظيم» و«الباعث الحثيث شرح اختصار علوم الحديث» وغيرها. توفي رحمه الله سنة 774 ه.</p>
<h3>أبو بكر ابن العربي</h3>
<p>محمد بن عبد الله بن محمد؛ أبو بكر بن العربي المعافري الإشبيلي المالكي؛ من حفاظ الحديث. برع في الأدب، وبلغ رتبة الاجتهاد في علوم الدين. صنف كتبا في الحديث والفقه والأصول والتفسير والأدب والتاريخ. منها: «العواصم من القواصم» و«عارضة الأحوذي في شرح الترمذي» و«أحكام القرآن» و«القبس في شرح موطأ ابن أنس». ولد في إشبيلية، وولي فيها القضاء، ورحل إلى المشرق. توفي سنة 543 ه.</p>
<h3>أبو حيان</h3>
<p>محمد بن يوسف بن علي بن يوسف بن حَيّان الغرناطي الأندلسي الجياني النفزي أثير الدين أبو حيان؛ من كبار العلماء بالعربية والتفسير والحديث والتراجم واللغات. من أشهر كتبه: «البحر المحيط في تفسير القرآن». ولد في غرناطة، ورحل إلى مالقة، ثم أقام بالقاهرة، وتوفي فيها عام 745 ه.</p>
<h3>الآلوسي</h3>
<p>محمود بن عبد الله؛ شهاب الدين أبو الثناء الحسيني الآلوسي البغدادي؛ مفسر ومحدث وأديب. تقلد الإفتاء ببلده سنة 1248 ه وعزل فانقطع للعلم. من كتبه: «روح المعاني في التفسير». ولد ببغداد وتوفي بها سنة 1270 ه.</p>
<h3>الزمخشري</h3>
<p>محمود بن عمرو بن أحمد؛ أبو القاسم جار الله الزمخشري. كان إماما في التفسير والنحو واللغة والأدب؛ ألف كتبا كثيرة أهمها تفسيره المشهور: «الكشاف عن حقائق غوامض التنزيل». توفي سنة 538 ه.</p>
<h3>فخر الدين الرازي</h3>
<p>محمد بن عمر بن الحسن بن الحسين التيمي البكري؛ أبو عبد الله فخر الدين الرازي الإمام المفسر. أوحد زمانه في المعقول والمنقول؛ من أشهر كتبه: «التفسير الكبير المسمى مفاتيح الغيب» و«المحصول في علم الأصول». ولد في الري وإليها نسبته؛ ويقال له: ابن خطيب الري. رحل إلى خوارزم وما وراء النهر وخراسان؛ وتوفي في هراة سنة 606 ه.</p>
<h3>القاضي عياض</h3>
<p>عياض بن موسى بن عياض بن عمرون اليحصبي السبتي؛ أبو الفضل؛ عالم المغرب وإمام أهل الحديث في وقته. ولي قضاء سبتة، ثم قضاء غرناطة. من تصانيفه: «الشفا بتعريف حقوق المصطفى» و«ترتيب المدارك» و«تقريب المسالك في معرفة أعلام مذهب الإمام مالك» و«شرح صحيح مسلم» و«الإلماع إلى معرفة أصول الرواية وتقييد السماع». ولد بسبتة وتوفي بمراكش عام 544 ه.</p>"""

HTML_FR = """<h1>Personnalités citées et leurs notices (fihris al-aʿlām) — Le Livre d'exégèse fondé sur le Tashīl li-ʿulūm al-tanzīl d'Ibn Ǧuzayy, deuxième année de l'enseignement collégial traditionnel</h1>
<h3>Ibn Ǧuzayy</h3>
<p>Il est Muḥammad ibn Aḥmad ibn ʿAbd Allāh ibn Yaḥyā ibn ʿAbd al-Raḥmān ibn Yūsuf ibn Ǧuzayy al-Kalbī al-Andalusī : il a laissé de nombreux ouvrages dans les diverses disciplines du savoir, telles le droit, le hadith, le soufisme et les lectures coraniques. Parmi ses compositions les plus importantes : le livre « al-Qawānīn al-fiqhiyya » (Les Règles juridiques) et le livre « al-Tashīl li-ʿulūm al-tanzīl » (La Facilitation des sciences de la Révélation). Mort — qu'Allah lui fasse miséricorde — en 741 H.</p>
<h3>Ibn Abī Ḥātim</h3>
<p>ʿAbd al-Raḥmān ibn Muḥammad ibn Abī Ḥātim ibn Idrīs ibn al-Mundhir al-Tamīmī al-Ḥanẓalī al-Rāzī, Abū Muḥammad : gardien du hadith (ḥāfiẓ). Il composa des ouvrages, dont « al-Jarḥ wa-l-taʿdīl » (L'Appréciation critique des rapporteurs) et « al-Tafsīr » (L'Exégèse). Sa demeure se trouvait dans la ruelle de Ḥanẓala, à al-Rayy. Mort en 327 H.</p>
<h3>Ibn Ǧarīr al-Ṭabarī</h3>
<p>Muḥammad ibn Ǧarīr ibn Yazīd, Abū Ǧaʿfar al-Ṭabarī : juriste, exégète et historien. Parmi ses compositions les plus célèbres : « Ǧāmiʿ al-bayān fī tafsīr al-Qurʾān » (Le Recueil de l'exposé, exégèse du Coran), « Iḫtilāf al-fuqahāʾ » (Les Divergences des juristes) et « Aḫbār al-rusul wa-l-mulūk » (Les Annales des envoyés et des rois), connu sous le nom d'Histoire de Ṭabarī. Né à Āmul, au Ṭabaristān, il s'établit à Bagdad et y mourut en 310 H.</p>
<h3>Ibn ʿĀshūr</h3>
<p>Muḥammad al-Ṭāhir ibn ʿĀshūr al-Tūnisī : président des muftīs mālikites de Tunis et shaykh de la mosquée-université al-Zaytūna et de ses dépendances à Tunis. Il a laissé de nombreux ouvrages, dont les plus célèbres : « Maqāṣid al-sharīʿa al-islāmiyya » (Les Finalités de la Loi islamique) et « al-Taḥrīr wa-l-tanwīr fī tafsīr al-Qurʾān » (La Libération et l'Illumination, exégèse du Coran), parmi d'autres compositions. Mort — qu'Allah lui fasse miséricorde — en 1393 H.</p>
<h3>Ibn ʿAbbās</h3>
<p>ʿAbd Allāh ibn ʿAbbās ibn ʿAbd al-Muṭṭalib al-Qurashī al-Hāshimī : le noble compagnon, « l'interprète de la communauté » (ḥibr al-umma). Né à La Mecque, il grandit aux débuts de l'ère prophétique et fréquenta assidûment le messager d'Allah ﷺ, rapportant de lui de nombreux hadiths — qu'Allah soit satisfait de lui — : ils atteignirent environ 1660 dans les deux Ṣaḥīḥ et ailleurs. Ayant perdu la vue dans ses dernières années, il s'établit à Ṭāʾif, où il mourut en 68 H.</p>
<h3>Ibn ʿAǧība</h3>
<p>Il est Aḥmad ibn Muḥammad ibn al-Mahdī ibn al-Ḥusayn ibn Muḥammad, connu sous le nom d'Ibn ʿAǧība et surnommé Abū al-ʿAbbās : l'imam exégète. Parmi ses compositions : « al-Baḥr al-madīd fī tafsīr al-Qurʾān al-maǧīd » (L'Océan prodigieux, exégèse du glorieux Coran), la « Glose sur le Mukhtaṣar de Khalīl », la « Glose sur al-Ǧāmiʿ al-ṣaghīr » d'al-Suyūṭī, entre autres. Mort — qu'Allah lui fasse miséricorde — en 1224 H.</p>
<h3>Ibn ʿAṭiyya</h3>
<p>Il est ʿAbd al-Ḥaqq ibn Ghālib ibn ʿAbd al-Raḥmān ibn Ghālib ibn ʿAbd al-Raʾūf ibn ʿAbd Allāh ibn Tamām ibn ʿAṭiyya, Abū Muḥammad al-Maḥāribī al-Gharnāṭī al-Mālikī al-Andalusī : juriste et exégète. Il reçut la science des maîtres d'al-Andalus, au nombre desquels son père Abū Bakr Ghālib et Abū ʿAlī al-Ghassānī. Il a laissé de nombreux ouvrages, dont « al-Muḥarrar al-waǧīz fī tafsīr al-kitāb al-ʿazīz » (L'Excellent abrégé, exégèse du Livre puissant). Mort en 542 H.</p>
<h3>Ibn Kathīr</h3>
<p>Il est Ismāʿīl ibn ʿUmar ibn Kathīr, Abū al-Fidāʾ al-Dimashqī al-shāfiʿite : l'imam, gardien du hadith, traditionniste et historien. Parmi ses compositions les plus célèbres : « Tafsīr al-Qurʾān al-ʿaẓīm » (L'Exégèse du noble Coran) et « al-Bāʿith al-ḥathīth sharḥ ikhtiṣār ʿulūm al-ḥadīth » (L'Incitateur empressé, commentaire de l'Abrégé des sciences du hadith), entre autres. Mort — qu'Allah lui fasse miséricorde — en 774 H.</p>
<h3>Abū Bakr Ibn al-ʿArabī</h3>
<p>Muḥammad ibn ʿAbd Allāh ibn Muḥammad, Abū Bakr ibn al-ʿArabī al-Maʿāfirī al-Ishbīlī al-Mālikī : parmi les gardiens du hadith. Il excella en littérature et atteignit le rang de l'iǧtihād dans les sciences religieuses. Il composa des livres en hadith, droit, uṣūl, exégèse, littérature et histoire, dont : « al-ʿAwāṣim min al-qawāṣim » (Les Préservatrices des atteintes), « ʿĀriḍat al-aḥwadhī fī sharḥ al-Tirmidhī » (Le Don précieux, commentaire du Tirmidhī), « Aḥkām al-Qurʾān » (Les Règles tirées du Coran) et « al-Qabas fī sharḥ Muwaṭṭaʾ Ibn Anas » (La Braise, commentaire du Muwaṭṭaʾ d'Ibn Anas). Né à Séville, il y exerça la judicature, puis voyagea vers l'Orient. Mort en 543 H.</p>
<h3>Abū Ḥayyān</h3>
<p>Muḥammad ibn Yūsuf ibn ʿAlī ibn Yūsuf ibn Ḥayyān al-Gharnāṭī al-Andalusī al-Ǧayyānī al-Nafzī, Athīr al-Dīn Abū Ḥayyān : parmi les plus grands savants en langue arabe, exégèse, hadith, biographies et langues. Parmi ses livres les plus célèbres : « al-Baḥr al-muḥīṭ fī tafsīr al-Qurʾān » (L'Océan enveloppant, exégèse du Coran). Né à Grenade, il voyagea à Malaga, puis s'établit au Caire, où il mourut en 745 H.</p>
<h3>al-Ālūsī</h3>
<p>Maḥmūd ibn ʿAbd Allāh, Shihāb al-Dīn Abū al-Thanāʾ al-Ḥusaynī al-Ālūsī al-Baghdādī : exégète, traditionniste et lettré. Il assuma la charge de la fatwā dans sa ville en 1248 H, puis en fut destitué et se consacra à la science. Parmi ses livres : « Rūḥ al-maʿānī fī tafsīr al-Qurʾān » (L'Esprit des sens, exégèse du Coran). Né à Bagdad, il y mourut en 1270 H.</p>
<h3>al-Zamakhsharī</h3>
<p>Maḥmūd ibn ʿAmr ibn Aḥmad, Abū al-Qāsim Ǧār Allāh al-Zamakhsharī. Il fut un imam en exégèse, grammaire, langue et littérature ; il composa de nombreux livres, dont le plus important est son exégèse célèbre : « al-Kashshāf ʿan ḥaqāʾiq ghawāmiḍ al-tanzīl » (Le Découvreur des réalités obscures de la Révélation). Mort en 538 H.</p>
<h3>Fakhr al-Dīn al-Rāzī</h3>
<p>Muḥammad ibn ʿUmar ibn al-Ḥasan ibn al-Ḥusayn al-Taymī al-Bakrī, Abū ʿAbd Allāh Fakhr al-Dīn al-Rāzī : l'imam exégète, l'unique de son époque en sciences rationnelles et traditionnelles. Parmi ses livres les plus célèbres : « al-Tafsīr al-kabīr, dit Mafātīḥ al-ghayb » (Le Grand Tafsīr, dit Les Clefs du mystère) et « al-Maḥṣūl fī ʿilm al-uṣūl » (Le Résultat, en science des uṣūl). Né à al-Rayy — d'où sa dénomination —, on l'appelle aussi Ibn Khaṭīb al-Rayy. Il voyagea au Khwārizm, en Transoxiane et au Khorassan, et mourut à Harāt en 606 H.</p>
<h3>al-Qāḍī ʿIyāḍ</h3>
<p>ʿIyāḍ ibn Mūsā ibn ʿIyāḍ ibn ʿAmrūn al-Yaḥṣubī al-Sabtī, Abū al-Faḍl : le savant du Maghreb et l'imam des gens du hadith en son temps. Il exerça la judicature à Ceuta, puis à Grenade. Parmi ses compositions : « al-Shifāʾ bi-taʿrīf ḥuqūq al-Muṣṭafā » (La Guérison par la reconnaissance des droits de l'Élu), « Tartīb al-madārik » (L'Ordre des degrés de la connaissance), « Taqrīb al-masālik fī maʿrifat aʿlām madhhab al-Imām Mālik » (L'Aproximation des voies, connaissance des notables de l'école de l'imam Mālik), le « Commentaire du Ṣaḥīḥ de Muslim » et « al-Ilmāʿ ilā maʿrifat uṣūl al-riwāya wa-taqyīd al-samāʿ » (L'Indication des principes de la transmission et de la fixation de l'audition). Né à Ceuta, il mourut à Marrakech en 544 H.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if str(l.get("docId", "")).endswith("-584"):
            l["html"] = HTML_AR
            l["htmlFr"] = HTML_FR
            l["pdfOnly"] = False
            l["titleAr"] = "فهرس الأعلام"
            l["titleFr"] = "Personnalités citées (fihris al-aʿlām)"
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 584 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 584 livrée: AR {len(HTML_AR)} car + FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
