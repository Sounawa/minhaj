# -*- coding: utf-8 -*-
"""R559 — translittération intégrale des segments arabes de la leçon pdf-12
(règle R552/R558 : zéro caractère arabe dans le rendu FR-seule)."""
import re

PATH = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-12-fr.html"
h = open(PATH, encoding="utf-8").read()

MAP = [
    ("blocs الفهم et استخراج المضامين", "blocs al-Fahm (la compréhension) et istikhrāj al-maḍāmīn (l’extraction des contenus)"),
    ("Le bloc الفهم (la compréhension)", "Le bloc al-Fahm (la compréhension)"),
    ("le sous-titre الشرح (l’explication)", "le sous-titre aš-Šarḥ (l’explication)"),
    ("le bloc استخراج المضامين (l’extraction des contenus)", "le bloc istikhrāj al-maḍāmīn (l’extraction des contenus)"),
    ("Le bloc التحليل (l’analyse)", "Le bloc at-Taḥlīl (l’analyse)"),
    ("Le bloc التقويم (l’évaluation)", "Le bloc at-Taqwīm (l’évaluation)"),
    ("Le bloc الاستدلال (l’argumentation)", "Le bloc al-istidlāl (l’argumentation)"),
    ("Le bloc الإعداد القبلي (la préparation préalable)", "Le bloc al-iʿdād al-qiblī (la préparation préalable)"),
    ("Le bloc des aḥādīth (الأحاديث)", "Le bloc des aḥādīth (al-aḥādīth)"),
    ("Le bloc ترجمة الراوي (la traduction du transmetteur)", "Le bloc tarǧamat ar-rāwī (la traduction du transmetteur)"),
    ("« الدرس 11 »", "« al-dars 11 »"),
    ("« الدرس 12 »", "« al-dars 12 »"),
    ("« الدرس 14 »", "« al-dars 14 »"),
    ("bannière du cours — numéro imprimé « الدرس 11 »", "bannière du cours — numéro imprimé « al-dars 11 »"),
    ("(مائة)", "(miʾa)"),
    ("« عَشْرِ رِقَابٍ »", "« ʿašri riqāb »"),
    ("« عَشْرُ رِقَابٍ »", "« ʿašru riqāb »"),
    ("« أَبِي عَبْدِ اللهِ الأَغَرِّ »", "« Abī ʿAbdillāh al-Aġarr »"),
    ("« الأعراج »", "« al-Aʿrāǧ »"),
    ("la conjonction « وَعَنْ »", "la conjonction « wa-ʿan »"),
    ("[الموطأ رقم : 562]", "[Muwaṭṭaʾ, numéro : 562]"),
    ("[الموطأ رقم : 572]", "[Muwaṭṭaʾ, numéro : 572]"),
    ("les renvois rouges portent « الموطأ »", "les renvois rouges portent « al-Muwaṭṭaʾ »"),
    ("« تَوَاتِي عَشْرَةَ مِنَ الْعَبِيدِ »", "« tawātī ʿašarata min al-ʿabīd »"),
    ("« حِرْزًا مِنَ الشَّيْطَانِ »", "« ḥirzan mina š-šayṭān »"),
    ("« حِصْنًا واقِيًا مِنْ وَسَاوِسِ الشَّيْطَانِ »", "« ḥiṣnan waqīyan min wasāwisi š-šayṭān »"),
    ("« يُبْتَدِرُونَهَا »", "« yubtadirūnahā »"),
    ("« يُسارِعُونَ إلَى الكَلِمَاتِ المَذْكُورَةِ أَيُّهُمْ يَكْتُبُهَا؛ ليُصَدِّقَ بها »", "« yusāriʿūna ilā l-kalimāti l-maḏkūrati ayyuhum yaktubuhā ; li-yuṣaddiqa bihā »"),
    ("porte « ليُصَدِّقَ بها » (lecture 900 dpi)", "porte « li-yuṣaddiqa bihā » (lecture 900 dpi)"),
    ("porte « ليصعد »", "porte « li-yuṣʿad »"),
    ("porte « الصبغ »", "porte « aṣ-ṣabġ »"),
    ("porte « الصيغ » (les formes)", "porte « aṣ-ṣiyāġ » (les formes)"),
    ("« زَبَدِ الْبَحْرِ » (l’écume de la mer, relu", "« zabad al-baḥr » (l’écume de la mer, relu"),
    ("porte « رَبَدِ »", "porte « rabad »"),
    ("porte « وَأَنْزَاهَا » (la plus pure) et « عِنْدَ مَلِيكُمْ »", "porte « wa-anẓāhā » (la plus pure) et « ʿinda malīkum »"),
    ("porte « مليكم »", "porte « malīkum »"),
    ("« رَفَاعَةَ بن رَافِعَ بن رَافِعَ » (trois maillons imprimés", "« Rāfiʿa b. Rāfiʿ b. Rāfiʿ » (trois maillons imprimés"),
    ("porte « رفاعة بن رافع », la lecture", "porte « Rāfiʿa b. Rāfiʿ », la lecture"),
    ("« بَضْعَةَ وَثَلَاثِينَ » (trente-sept)", "« baḍʿa wa-ṯalāṯīn » (trente-sept)"),
    ("« عَلَى أَنَّ الذِّكْرَ حِصْنٌ مَتِينٌ »", "« ʿalā anna ḏ-ḏikra ḥiṣnun matīn »"),
    ("« وَكَمَا ذَكَرَ الْعَبْدُ مَوْلَاهُ خَسَّ الشَّيْطَانِ »", "« wa-kamā ḏakara l-ʿabdu mawlāhu ḫassa š-šayṭān »"),
    ("porte « المَوْطِإِ », orthographe du corps déclarée", "porte « al-Mawṭiʾ », orthographe du corps déclarée"),
    ("porte « سَبَّحَ دُبُرَ كُلِّ صَلَاةٍ » (glorifie après chaque prière)", "porte « sabbaḥa dubura kulli ṣalāt » (glorifie après chaque prière)"),
    ("porte « ذِكْرَ » (le dhikr de)", "porte « ḏikra » (le dhikr de)"),
    ("(rendu « دُبُرَ »)", "(rendu « dubura »)"),
    ("« مَغْفِرَةٌ ذُنُوبُهُ » (rémission de ses péchés)", "« maġfiratun ḏunūbuhu » (rémission de ses péchés)"),
    ("porte « غُفِرَتْ خَطَايَاهُ »", "porte « ġufirat ḫaṭāyāhu »"),
    ("« كَانَ فِي أَثْنَاءِ الصَّلَاةِ »", "« kāna fī aṯnāʾi ṣ-ṣalāt »"),
    ("« دعاء التمتُع بالصحة والتعوُّذ من الفقر »", "« duʿāʾ at-tamattuʿ bi-ṣ-ṣiḥḥa wa-t-taʿawwuḏ min al-faqr »"),
    ("porte « التعوُّذ »", "porte « at-taʿawwuḏ »"),
    ("« التعافي »", "« at-taʿāfī »"),
    ("« زيد بن أبي زيد » : Zayd b. Abī Zayd", "« Zayd b. Abī Zayd » (Zayd, fils d’Abū Zayd)"),
    ("« طَلْحَةَ بن عُبَيْدِ اللهِ بن كَرِيزٍ » : Ṭalḥa b. ʿUbaydallāh b. Karīz", "« Ṭalḥa b. ʿUbaydallāh b. Karīz » (Ṭalḥa, fils d’ʿUbaydallāh, fils de Karīz)"),
    ("porte « كان يُعَلِّمُهُمْ هذا الدُّعَاءَ كما يُعَلِّمُهُمُ السُّورَةَ مِنَ الْقُرْآنِ يَقُولُ »", "porte « kāna yuʿallimuhum hāḏā duʿāʾa kamā yuʿallimuhum sūratan mina l-qurʾān yaqūl » (il leur enseignait cette invocation comme Il leur enseignait une sūra du Coran, disant)"),
    ("« فِي المَوْطِإِ عَنْ أَبِي هُرَيْرَةَ »", "« fī l-Mawṭiʾ ʿan Abī Hurayra »"),
    ("« مَالِكٌ، أَنَّهُ بلغَهُ »", "« Mālik annahu balġahu »"),
    ("« قَرْنَ الشيطان » (le fait de demeurer auprès", "« qarn ash-shayṭān » (le fait de demeurer auprès"),
    ("translittération qarn ash-shayṭān) ;", ") ;"),
    ("« المَوْطِإِ » (dans le Muwaṭṭaʾ)", "« fī l-Mawṭiʾ » (dans le Muwaṭṭaʾ)"),
    ("l’imprimé clôt « وَمَا يَأْتِي أَحَدٌ بِأَفْضَلَ مِمَّا جَاءَ بِهِ، إِلَّا أَحَدٌ عَمِلَ أَكْثَرَ مِنْ ذَلِكَ »", "l’imprimé clôt par la formule du premier texte (nul ne vint avec quelque chose de meilleur, sinon un qui en fit davantage)"),
]

n = 0
for old, new in MAP:
    if old in h:
        h = h.replace(old, new)
        n += 1
    else:
        print("ABSENT :", old[:60])

open(PATH, "w", encoding="utf-8").write(h)
print(f"{n}/{len(MAP)} remplacements appliqués")

# contrôle résiduel
left = re.findall(r"[\u0600-\u06FF]+", h)
print("RÉSIDU ARABE :", len("".join(left)), "car —", sorted(set(left))[:20])
