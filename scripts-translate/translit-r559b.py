# -*- coding: utf-8 -*-
"""R559 — translittération par segment arabe (robuste aux auto-fix typo)."""
import re

PATH = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-12-fr.html"
h = open(PATH, encoding="utf-8").read()

T = {
    "الفهم": "al-Fahm",
    "استخراج المضامين": "istikhrāj al-maḍāmīn",
    "الدرس": "al-dars",
    "الأحاديث": "al-aḥādīth",
    "مائة": "miʾa",
    "عَشْرِ رِقَابٍ": "ʿašri riqāb",
    "أَبِي عَبْدِ اللهِ الأَغَرِّ": "Abī ʿAbdillāh al-Aġarr",
    "الأعراج": "al-Aʿrāǧ",
    "وَعَنْ": "wa-ʿan",
    "الموطأ رقم": "Muwaṭṭaʾ, numéro",
    "ترجمة الراوي": "tarǧamat ar-rāwī",
    "الشرح": "aš-Šarḥ",
    "عَشْرُ رِقَابٍ": "ʿašru riqāb",
    "تَوَاتِي عَشْرَةَ مِنَ الْعَبِيدِ": "tawātī ʿašarata min al-ʿabīd",
    "حِرْزًا مِنَ الشَّيْطَانِ": "ḥirzan mina š-šayṭān",
    "حِصْنًا واقِيًا مِنْ وَسَاوِسِ الشَّيْطَانِ": "ḥiṣnan waqīyan min wasāwisi š-šayṭān",
    "يُبْتَدِرُونَهَا": "yubtadirūnahā",
    "يُسارِعُونَ إلَى الكَلِمَاتِ المَذْكُورَةِ أَيُّهُمْ يَكْتُبُهَا؛ ليُصَدِّقَ بها": "yusāriʿūna ilā l-kalimāti l-maḏkūrati ayyuhum yaktubuhā ; li-yuṣaddiqa bihā",
    "ليُصَدِّقَ بها": "li-yuṣaddiqa bihā",
    "ليصعد": "li-yuṣʿad",
    "الصبغ": "aṣ-ṣabġ",
    "الصيغ": "aṣ-ṣiyāġ",
    "التحليل": "at-Taḥlīl",
    "أولا": "awwalan",
    "ثانيا": "ṯāniyan",
    "ثالثا": "ṯāliṯan",
    "زَبَدِ الْبَحْرِ": "zabad al-baḥr",
    "رَبَدِ": "rabad",
    "وَأَنْزَاهَا": "wa-anẓāhā",
    "عِنْدَ مَلِيكُمْ": "ʿinda malīkum",
    "مليكم": "malīkum",
    "مَلِيكُمْ": "malīkum",
    "رَفَاعَةَ بن رَافِعَ بن رَافِعَ": "Rāfiʿa b. Rāfiʿ b. Rāfiʿ",
    "بَضْعَةَ وَثَلَاثِينَ": "baḍʿa wa-ṯalāṯīn",
    "عَلَى أَنَّ الذِّكْرَ حِصْنٌ مَتِينٌ": "ʿalā anna ḏ-ḏikra ḥiṣnun matīn",
    "وَكَمَا ذَكَرَ الْعَبْدُ مَوْلَاهُ خَسَّ الشَّيْطَانِ": "wa-kamā ḏakara l-ʿabdu mawlāhu ḫassa š-šayṭān",
    "المَوْطِإِ": "al-Mawṭiʾ",
    "الموطأ": "al-Muwaṭṭaʾ",
    "سَبَّحَ دُبُرَ كُلِّ صَلَاةٍ": "sabbaḥa dubura kulli ṣalāt",
    "ذِكْرَ": "ḏikra",
    "دُبُرَ": "dubura",
    "مَغْفِرَةٌ ذُنُوبُهُ": "maġfiratun ḏunūbuhu",
    "غُفِرَتْ خَطَايَاهُ": "ġufirat ḫaṭāyāhu",
    "كَانَ فِي أَثْنَاءِ الصَّلَاةِ": "kāna fī aṯnāʾi ṣ-ṣalāt",
    "دعاء التمتُع بالصحة والتعوُّذ من الفقر": "duʿāʾ at-tamattuʿ bi-ṣ-ṣiḥḥa wa-t-taʿawwuḏ min al-faqr",
    "التعوُّذ": "at-taʿawwuḏ",
    "التعافي": "at-taʿāfī",
    "زيد بن أبي زيد": "Zayd b. Abī Zayd",
    "طَلْحَةَ بن عُبَيْدِ اللهِ بن كَرِيزٍ": "Ṭalḥa b. ʿUbaydallāh b. Karīz",
    "كان يُعَلِّمُهُمْ هذا الدُّعَاءَ كما يُعَلِّمُهُمُ السُّورَةَ مِنَ الْقُرْآنِ يَقُولُ": "kāna yuʿallimuhum hāḏā duʿāʾa kamā yuʿallimuhum sūratan mina l-qurʾān yaqūl",
    "فِي المَوْطِإِ عَنْ أَبِي هُرَيْرَةَ": "fī l-Mawṭiʾ ʿan Abī Hurayra",
    "التقويم": "at-Taqwīm",
    "الاستدلال": "al-istidlāl",
    "مَالِكٌ، أَنَّهُ بلغَهُ": "Mālik annahu balġahu",
    "الإعداد القبلي": "al-iʿdād al-qiblī",
    "قَرْنَ الشيطان": "qarn ash-shayṭān",
    "أبي": "Abī",
    "أبو": "Abū",
    "الإعداد": "al-iʿdād",
    "القبلي": "al-qiblī",
}

ar_re = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF][\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\s\u064B-\u0652\u0670\u0640]*")


def repl(m):
    seg = m.group(0).strip()
    if seg in T:
        return m.group(0).replace(seg, T[seg])
    # essai sans diacritiques
    bare = re.sub(r"[\u064B-\u0652\u0670\u0640]", "", seg)
    if bare in T:
        return m.group(0).replace(seg, T[bare])
    print("NON MAPPÉ :", repr(seg))
    return m.group(0)


h2 = ar_re.sub(repl, h)
open(PATH, "w", encoding="utf-8").write(h2)
left = re.findall(r"[\u0600-\u06FF]+", h2)
print("RÉSIDU ARABE :", len("".join(left)), "car")
for s in sorted(set(left))[:30]:
    print("  ·", repr(s))
