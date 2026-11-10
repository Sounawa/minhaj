# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM R673 (slot pdf-mut23h2x-406, leçon 17 أحكام الهدي,
p.116-123). Mécanique hadith3-vlm-read-403-r670.py : couche texte recoupée par
rendus 300/600 dpi (tr-tmp/qa-crops-r673/), chaque lecture = cache
tr-tmp/qa-crops-r673/_r673-read-<name>.json — toute récusation de la couche
texte est documentée, jamais devinée. Moteur : CLI z-ai vision, prompts
ciblés par page (numéros Muwaṭṭa digit-by-digit car OCR en miroir)."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r673"

PROMPTS = {
    "r673-p116-banner": (
        "Zoom 600 dpi of the OPENING BANNER page of lesson 17 of an Arabic schoolbook "
        "(Muwaṭṭa Mālik, Ḥajj chapter). Transcribe EXACTLY, right-to-left: 1) the round blue "
        "MEDALLION number — read it DIGIT BY DIGIT (expected 17 = الدرس 17, but OCR text layer "
        "is unreliable so confirm carefully; answer in form 'medallion: N'); 2) the calligraphic "
        "title of the lesson (expected أحكام الهدي أو الحج وفتدل — transcribe every word); 3) the "
        "rubric line أحفظ أحاديث الدرس المقبل وأجيب عن الآتي — transcribe exactly; 4) EVERY "
        "numbered question below it (expected 1- أشرح: الإشعار والتقليد [third word?] 2- أبحث عن "
        "معنى المستيسر من الهدي) — transcribe each exactly word by word; 5) any other printed "
        "text on the page (page number). Mark illegible as [؟]. Short French notes at the end."
    ),
    "r673-p117-full": (
        "Full Arabic schoolbook page (300 dpi), first content page of lesson 17 أحكام الهدي "
        "(Muwaṭṭa). Transcribe ALL Arabic lines EXACTLY, right-to-left, in reading order: 1) the "
        "rubric أهداف الدرس with EVERY numbered objective (expected 1- أن أتعرف أحكام الهدي في "
        "الحج 2- أن أدرك مقاصد الهدي في الحج) — transcribe each exactly; 2) the intro paragraph "
        "(expected: جعل الله سبحانه الهدي إلى الحرم من مناسك الحج من مناسك وشعيرة الحج من "
        "شعائره... والبذؤ [؟]) — transcribe ENTIRELY word by word, especially the Quranic quote "
        "that follows فقال تعالى: («وتقرباً» + the quoted verse) — transcribe the WHOLE quoted "
        "verse text exactly; 3) the citation reference at the end of the verse, in the form "
        "[سورة NNN] الآيتان M-P — read EVERY digit DIGIT BY DIGIT from the image (text layer "
        "gives 43-53 which may be mirrored; expected al-Ḥajj 34-36 zone: the verse contains "
        "البُدنَ جعلناها من شعائر الله) — give both numbers clearly; 4) the second quote (مقاصد؟ "
        "السن المجزئة في الهدي؟ ما يساق وكيف وما حكم الانتفاع به وما مقاصده؟) — transcribe the "
        "question list exactly; 5) the first Muwaṭṭa athar: عن مالك عن [؟] عن [؟] أن [؟] قال: "
        "يُنْحَرَ مَعَهَا [؟] with the blue bracket [الموطأ رقم: NNN] — read the number DIGIT BY "
        "DIGIT from the image (text layer shows 1111 which is a palindrome so the image is the "
        "only authority) — transcribe the full isnād and matn exactly; 6) any small footnote or "
        "gloss line. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r673-p118-full": (
        "Full Arabic schoolbook page (300 dpi), page 2 of lesson 17 أحكام الهدي (Muwaṭṭa). "
        "Transcribe ALL Arabic lines EXACTLY, right-to-left, in reading order: 1) the FIRST "
        "athar at top: عن مالك عن محمد بن [جعفر؟] عن أبيه عن علي بن أبي طالب؟ قال: ما يقول: "
        "كان [؟] — transcribe the full isnād and matn EXACTLY word by word with the blue "
        "[الموطأ رقم: NNN] read DIGIT BY DIGIT (text layer 1411 → expect 1141 or other); 2) the "
        "SECOND athar: عن مالك عن نافع عن عبد الله بن عمر أنه: أهدى هدياً من المدينة [؟] — full "
        "matn (يُشْعِرُهُ يُقَلِّدُهُ مُوَجَّهٌ للقبلة ذلك في مكان واحد وهو [؟] ويُشْعِرُهُ من "
        "الشقّ الأيسر ثم يُسَاقُ معَه حَتَّى [؟] إذا مَعَهُمْ يُوقفُ به [؟] عرفة إذا دفع [؟] ثم "
        "يَدْفَعُ به مَعَهُمْ فإذا قدم منى نحرَهُ قبل أن يَخْلُقَ أو يُقصَرَ [؟] يَنْحَرْهُ "
        "بيده يصفهن قياماً ويُوَجِّهُهُنَّ ثم يَأكُلُ ويَطْعِمُ [؟]) — transcribe EXACTLY with "
        "[الموطأ رقم: NNN] DIGIT BY DIGIT (text layer 3111 → expect 1113 or other); 3) the THIRD "
        "athar: عن مالك عن نافع عن عبد الله بن عمر بن حزم؟ أن رسول الله كان جَمَلاً لأبي جَهْلِ "
        "بن هشام في [حج؟] أو عمرة — transcribe exactly with [الموطأ رقم: NNN] DIGIT BY DIGIT "
        "(text layer 6011 → expect 1106 or other); 4) the rubric ترجمة الراوي with the biography "
        "of علي بن أبي طالب (expected: هو علي بن أبي طالب بن عبد المطلب رضي الله عنه زوج "
        "ابنته فاطمة رضي الله عنها الرابع الخليفة لرسول الله ذو المناقب الكثيرة والمواقف "
        "العظيمة توفي عام 40 [؟]) — transcribe EVERY line exactly including the year digit by "
        "digit; 5) the second biography عبد الله بن عمرو بن حزم؟ الأنصاري المدني تابعي (روى عن "
        "الزهري وابن جريج وإسحاق بن مالك(?) وغيرهم من الرواة الأولين الذين اهتموا برواية "
        "الأحاديث المتعلقة بالسير حتى المغازي أصحاب الذهبي توفي سنة 131 [؟]) — transcribe every "
        "line, years digit by digit. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r673-p119-full": (
        "Full Arabic schoolbook page (300 dpi), page 3 of lesson 17 أحكام الهدي. Transcribe ALL "
        "Arabic lines EXACTLY, right-to-left: 1) the paragraph above the rubric (commentary on "
        "المجزئة البدنة: [؟] شق [؟] سنامة استعمالها وكثرة الناقة والجمل والبقرة كانت فيما هدياً "
        "[؟]) — transcribe exactly; 2) the rubric استخلاص المضامين with EVERY numbered item "
        "(expected 3 items: 1- ما يجزئ من السن في الهدي 2- أستخلص من الأحاديث صفة سوق الهدي "
        "3- أبين حكم الانتفاع بالهدي) — transcribe each exactly; 3) the next paragraph (الحج من "
        "شعائر الحج العظيمة يجب على الحاج معرفة أحكامها وإدراك حكمها ومقاصدها والهدي لغير ترك "
        "واجب خاص بالتمتع والقران والقاران [؟] فليس على الحاج hedi بالإفراد إلا لترك [؟] ولا "
        "واجب لمن أهله حاضر المسجد الحرام) — transcribe EXACTLY word by word; 4) the rubric "
        "أولا: ما يجزئ من الهدي and sub-line 1- السن في الهدي المجزئ [؟]; 5) the FULL Muwaṭṭa "
        "quote: عن نافع: أنّ عبد الله بن عُمَرَ كانَ يَقُول: في الضَّحَايَا وَالْبُدْنِ الثَّنْيَ "
        "فَمَا فَوْقَهُ [؟] with blue [الموطأ رقم: NNN] read DIGIT BY DIGIT (text layer 8111 → "
        "expect 1118 or other); 6) any gloss line below. Mark illegible as [؟]. Short French "
        "notes at the end."
    ),
    "r673-p120-full": (
        "Full Arabic schoolbook page (300 dpi), page 4 of lesson 17 أحكام الهدي. Transcribe ALL "
        "Arabic lines EXACTLY, right-to-left: 1) the continuation of the fiqh paragraph at top "
        "(الجذع من الضأن وهو ما أوفى سنة [؟] فلولد النحر يوم جاز في هديه قمرية [؟] العام القابل "
        "من ثانيه كما يجوز في الهدي إهداء المعزء من الثني وهو ما أوفى سنة أو دخل [؟] الأنثى "
        "إهداء الذكر بينا دخل الثانية في كشهر [؟] الرابعة في دخل ولو غير بين [؟] الإبل من الثني "
        "وهو ما أوفى خمسا أو دخل السادسة في ولو كان دخولا غير بين) — transcribe EVERY line "
        "exactly; 2) the sentence استيسر من الهدي ما إهداء [؟] قال الله تعالى: [verse quote] "
        "المستيسر والمستيسر من الهدي [؟] [سورة المائدة الآية: NNN] — transcribe the quoted verse "
        "text EXACTLY and read the verse number DIGIT BY DIGIT (text layer 591 mirrored? read "
        "from image carefully — verse should contain فما استيسر من الهدي — al-Baqara 196 area); "
        "3) the two Muwaṭṭa quotes: روى مالك عنه عن عبد الله [؟] ابن عمر فسره ببقرة أو بدنة "
        "قال: ما استَيْسَرَ [؟] وفسره علي وابن عباس بَقَرَةٌ [الموطأ رقم: NNN] read DIGIT BY "
        "DIGIT (text layer 4411 → expect 1144); فعن مالك عن [؟] عباس أنه بلغه أن عبد الله بن "
        "عباس [؟] قال مالك: وذلك ما سمعتُ إليّ في ذلك [؟] ما استَيْسَرَ من الهَذي شاة [الموطأ "
        "رقم: NNN] DIGIT BY DIGIT (text layer 2411 → expect 1142); 4) the الشرح gloss rubric with "
        "EVERY glossed word (المعزء: [؟] الجذع: [؟] الثني: [؟] القرم/القرنيّ? القابل: [؟]) — "
        "transcribe each gloss fully; 5) the closing sentence فمما يحكم به في الهدي الشاة وقد "
        "سماها الله هدياً وذلك لا [؟] وفيه التلف عند [؟] وشك كيف في كل ذلك؟ وكل شيء يجبر أن "
        "يحكم فيه بَيِّنٍ [؟] — transcribe exactly. Mark illegible as [؟]. Short French notes."
    ),
    "r673-p121-full": (
        "Full Arabic schoolbook page (300 dpi), page 5 of lesson 17 أحكام الهدي. Transcribe ALL "
        "Arabic lines EXACTLY, right-to-left: 1) the TOP Quranic quote finishing the فِدية "
        "passage (expected al-Māʾida 95 fragment: فَجَزَاؤُهُ مِثْلُ مَا نَهَرَ مِنَ النَّعَمِ "
        "؟ فَكَفَّارَتُهُ [؟] مِنْ صِيَامٍ أَوْ إِطْعَامُ مَسَاكِينَ [؟] [الموطأ رقم: NNN]? "
        "careful: a blue Muwaṭṭa bracket may follow the verse) — transcribe EXACTLY every word "
        "and read ANY number DIGIT BY DIGIT (text layer 3411 mirrored → 1143? and المساكين), "
        "tell me whether the number is a Muwaṭṭa bracket or a verse reference [سورة NNN الآية "
        "NNN] and read it digit by digit; 2) the rubric ثانيا: سَوْقَ الهدي and sub-line 1- "
        "تعظيم الهدي with the Quranic quote قال تعالى: [؟] تَقْوَى الْقُلُوبِ [؟] [سورة الحج "
        "الآية: NNN] — read the verse number DIGIT BY DIGIT (text layer 03 mirrored → 30? "
        "expected al-Ḥajj 32 zone: من تقوى القلوب) — transcribe verse text exactly; 3) the "
        "commentary (والشعائر: والهدي والأنعام المشعرة تعظيمها وتسمينها والمغالاة بهاء عروة "
        "وكان يقول [؟] يا بني إِنْ لا يُهْدِينَ شيءاً [؟] أن يُهْدِيَهُ الله فن كريمه [؟] "
        "أكْرَمُ ااختير له [الموطأ رقم: NNN]) — transcribe exactly, number DIGIT BY DIGIT (text "
        "layer 0211 → expect 1120?); 4) sub-line 2- العمل في الهدي with the FULL Muwaṭṭa quote "
        "عن عبد الله بن عمر: إذَا كَانَ أَهَدَى هَذِيَاً منَ المَدينَة [؟] قبل يده قَبْلَ أنْ "
        "يُشْعِرَهُ [؟] وذلك في مكان واحد وهو مُوَجَّهٌ للقبلة [؟] ويُشَعرُهُ بِتَغْلِين [؟] "
        "منَ الشقّ الأَيْسَر [؟] ثم يُمَاقَ [؟] معَهُ حَنَى [؟] يُوقفَ به الاس مَعَ [؟] عَرَفَة "
        "إذا ثوا [؟] فإذا قدم منى [؟] وَعَن نافع: أنّ عبدَ الله عَبْدَ عُمَرَ كَانَ يَصْفْهُنَ "
        "قيَامًا وَيُوَجِهُهُنَّ ثم يَأكُلُ وَيَطْعِمُ [الموطأ رقم: NNN] — number DIGIT BY DIGIT "
        "(text layer 4111 → expect 1114); 5) قال: بسم الله وله الله [؟] لقوله تعالى: "
        "والتَّكْبِير [؟] [سورة البقرة الآية: NNN] read DIGIT BY DIGIT (text layer 481 → 185? "
        "expected البقرة 196 zone); 6) any gloss lines. Mark illegible as [؟]. Short French "
        "notes at the end."
    ),
    "r673-p122-full": (
        "Full Arabic schoolbook page (300 dpi), page 6 of lesson 17 أحكام الهدي. Transcribe ALL "
        "Arabic lines EXACTLY, right-to-left: 1) the TOP: فاحتج بإطلاق هذا الحديث وبقوله تعالى "
        "«[verse]» [الموطأ رقم: NNN] — transcribe the quoted verse EXACTLY (expected لك في "
        "الحيّ? لَهَا مَنَافِعُ إِلَى أَجَلٍ مُسَمَّى ثُمَّ مَحِلُّهَا إِلَى الْبَيْتِ الْعَتِيقِ? "
        "al-Ḥajj 33) and the bracket [الموطأ رقم: NNN] DIGIT BY DIGIT (text layer 7011 → expect "
        "1107); 2) the fiqh sentence (من أجاز ركوب الهدي اختيارا حيث لا يضره وكرهه المالكية "
        "والجمهور وفي الآية: [NNN] يأكلون فيها/لضرورة المشهور عنه إلا لضرورة [؟] وسوق الهدي وركوبه قد [؟] "
        "إلى بدائل أخرى تحقق مقصد الشرع [؟] وحاجة المكلف غير أن هذا لا يرفع الأصل عند إمكانه) — "
        "transcribe EXACTLY with any verse number DIGIT BY DIGIT (text layer 13 → 31?); 3) "
        "sub-line 2- شرب لبن الهدي with the paragraph (كرهه مالك في الاختيار ولو فضل الري عن "
        "فصيله؛ لأنه نوع من الرجوع في الهدي ومحل الصدقة حيث لا ضرر وإلا غرم فعن هشام بن عروة "
        "أن أباه قال: إذًا اضطررت إلى بدنتك فَارْكَيْهَا رُكُوباً غَيْرَ فادح وإِذَا اضطررّت "
        "إِلَى لَبَنِهَا فَاشْرْبْ يُروَف فصيلتها فإذا نَحَرْتَهَا فَائِحَرُ فصيلها مَعَهَا "
        "[الموطأ رقم: NNN]) — transcribe exactly, number DIGIT BY DIGIT (text layer 2111 → "
        "expect 1112); 4) sub-line 3- أكل صاحب الهدى من هديه with paragraph (عن مالك أنه سمع "
        "أهل العلم يقولون: لا يأكل صَاحبٌ الْهَدي الْجَرَاء [؟] والمذهب المشهور أنه يأكل من كل "
        "هدي بلغ محله إلا [النسَّشك؟ الصواع؟] [الموطأ رقم: NNN]) — transcribe exactly, number "
        "DIGIT BY DIGIT (text layer 6211 → expect 1126); 5) the closing paragraph يستفاد من "
        "الدرس أن الشريعة مبنية على اليسر ورفع الحرج فقد أذنت في [؟] التمتع بالعمرة إلى الحج "
        "بهدي لبيت الله الحرام تعظيما لشعائر الله وتكرمة لضيوف الرحمن وتوسعة على فقراء مكة [؟] "
        "— transcribe exactly; 6) the numbered recap at bottom (1- أبين السن في المجزئة الهدي "
        "2- أبين حكم الانتفاع بالهدي مع التفصيل والاستدلال) — transcribe exactly. Mark "
        "illegible as [؟]. Short French notes at the end."
    ),
    "r673-p123-full": (
        "Full Arabic schoolbook page (300 dpi), LAST page of lesson 17 أحكام الهدي (p.123). "
        "Transcribe ALL Arabic lines EXACTLY, right-to-left: 1) the FULL Muwaṭṭa athar: عن مالك "
        "عن [؟] عبد الله بن دينار أنه كان عبد الله بن عمر يَرَى [هدياً في الجعار?] [؟] "
        "بدنتين بدنتين وفى العتمة [؟] وَرَأيته فى العمرة يَنحَرٌ بدنة وَهىّ قائمّة فى دار خالد "
        "بن أسيد وكان فيها مُنزله قال: ولقد رأيته طعن فى لِبَة بَدنته حتى خرحّت الحّربة من تحت "
        "كتفها [الموطأ رقم: NNN] — transcribe EVERY word exactly, number DIGIT BY DIGIT (text "
        "layer 8011 → expect 1108); 2) the rubric أستخرج الأثر with its task line (أحكام الهدي "
        "التي يشير إليها الأثر) — transcribe exactly; 3) the rubric استخلاص المضامين [or "
        "الاستخلاص] and its EVERY numbered item; 4) the rubric الإعداد للدرس المقبل [؟] with "
        "the formula أحفظ أحاديث الدرس المقبل وأجيب عن الآتي (text layer garbled: أحقخل أحاديث "
        "الذرون المقيل) — transcribe the formula exactly; 5) EVERY numbered question below (text "
        "layer: 1- أبحث عن حكم من فاته الحج وكيفية تحلله من إحرامه 2- ماذا يفعل من باشر زوجه "
        "وهو محرم بالحج؟) — transcribe each exactly; 6) page number. Mark illegible as [؟]. "
        "Short French notes at the end."
    ),
    "r673-p124-top": (
        "Zoom 600 dpi of the TOP of page 124 of an Arabic schoolbook. Determine: 1) is there an "
        "opening BANNER (decorative band + round blue medallion with a course number, like "
        "other lessons) OR does the page begin directly with numbered objectives lines? 2) if a "
        "medallion exists read its number DIGIT BY DIGIT (expect 18? or absent); 3) transcribe "
        "EVERY line you see exactly (expected: 1- أن أتعرف حكم من فاته الحج وكيفية تحلله من "
        "إحرامه 2- أن أتعرف أحكام عطب الهدي قبل بلوغه محله then a paragraph الهدي أحد مناسك "
        "الحج...); 4) any verse quote with its reference number DIGIT BY DIGIT. Mark illegible "
        "as [؟]. Short French notes at the end."
    ),
    "r673-p129-banner": (
        "Zoom 600 dpi of the OPENING BANNER page of a lesson of an Arabic schoolbook (Muwaṭṭa "
        "Mālik). Transcribe EXACTLY: 1) the round blue MEDALLION number — read DIGIT BY DIGIT "
        "(expected 18? 19? text layer unreliable; answer 'medallion: N'); 2) the calligraphic "
        "lesson title — transcribe every word; 3) any recall line above the rubric (استعين "
        "بشرح الزرقاني لبيان حكم من نسي طواف الإفاضة حتى [؟] رجع إبل [؟]) — transcribe exactly; "
        "4) the rubric أحفظ أحاديث الدرس المقبل وأجيب عن الآتي — exactly; 5) EVERY numbered "
        "question (expected: 1- أشرح: إلقاء التقث لَبَدْتُ رأسي [؟] 2- متى يتحلل المحرم؟ "
        "3- حدد الأعمال التي يقوم بها الحاج يوم النحر ثم أبحث عن أحكامها) — transcribe each "
        "exactly; 6) page number. Mark illegible as [؟]. Short French notes at the end."
    ),
}

IMG = {
    "r673-p116-banner": "zoom-p116-banner.png",
    "r673-p117-full": "p-117.png",
    "r673-p118-full": "p-118.png",
    "r673-p119-full": "p-119.png",
    "r673-p120-full": "p-120.png",
    "r673-p121-full": "p-121.png",
    "r673-p122-full": "p-122.png",
    "r673-p123-full": "p-123.png",
    "r673-p124-top": "zoom-p124-top.png",
    "r673-p129-banner": "zoom-p129-banner.png",
}


def run(name):
    out = os.path.join(DIR, f"_r673-read-{name}.json")
    if os.path.exists(out):
        print(f"cache {name}")
        return
    img = os.path.join(DIR, IMG[name])
    prompt = PROMPTS[name]
    cmd = ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if res.returncode != 0:
        print(f"ERR {name}: {res.stderr[:200]}")
        return
    try:
        d = json.load(open(out, encoding="utf-8"))
        body = d["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"ERR parse {name}: {e}")
        return
    print(f"OK {name} — {len(body)} car")


if __name__ == "__main__":
    for n in sys.argv[1:] or list(PROMPTS):
        run(n)
