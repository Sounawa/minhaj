# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM ciblées R673-b (adjudication fine p.120-123)."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r673"

PROMPTS = {
    "r673b-p120-bas": (
        "Zoom 600 dpi, lower half of an Arabic schoolbook page (lesson 17 أحكام الهدي). "
        "Transcribe EXACTLY right-to-left in reading order: 1) the sentence starting قال الله تعالى "
        "and the WHOLE Quranic verse quoted with its bracket [سورة المائدة الآية: NNN] — transcribe "
        "the verse TEXT letter by letter (it should mention الكعبة/الشهر الحرام/الهدى والقلايد) and "
        "read the verse number DIGIT BY DIGIT (is it 97 or 98 or other?); 2) the two Muwaṭṭa "
        "passages around it: (a) روى مالك عن نافع أن عبد الله بن عمر كان يقول ما استيسر من الهدي "
        "بدنة أو بقرة [الموطأ رقم: NNN digit by digit — 1144?]; (b) فعن مالك أنه بلغه أن [NAME?] "
        "كان يقول ما استيسر من الهدي شاة [الموطأ رقم: NNN digit by digit — 1142?] — transcribe the "
        "NAME after بلغه أن EXACTLY letter by letter (علي بن الحسين? ابن عباس? عبد الله بن عباس? "
        "عبد الله بن أبي?); 3) the sentence قال مالك: وذلك [أحب؟/حسن؟] ما سمعت إلى في ذلك; 4) the "
        "closing commentary sentence فمما يحكم به في الهدي... transcribe fully. Mark illegible as "
        "[؟]. Short French notes at the end."
    ),
    "r673b-p121-haut": (
        "Zoom 600 dpi, top third of an Arabic schoolbook page (lesson 17). Transcribe EXACTLY "
        "right-to-left: 1) the opening passage continuing from previous page about the fidya "
        "(أو بقرة، فالحكم فيه شاة، وما لا يبلغ أن يحكم فيه بشاة فهو كفارة من صيام أو إطعام "
        "مساكين) and ANY blue bracket [الموطأ رقم: NNN] read DIGIT BY DIGIT (1143?); 2) the green "
        "rubric ثانيا: سوق الهدي (or سَوْقَ?) and sub-line 1- تعظيم الهدي; 3) the Quranic quote "
        "قال تعالى: «...» with bracket [سورة الحج الآية: NNN] — transcribe the verse TEXT exactly "
        "(expected ذَلِكَ وَمَنْ يُعَظِّمْ شَعَائِرَ اللهِ فَإِنَّهَا مِنْ تَقْوَى الْقُلُوبِ — "
        "check if it starts with ذلك ومن يعظم or another wording) and read the verse number DIGIT "
        "BY DIGIT (is it 30? 31? 32?); 4) the commentary sentence والشعائر: الهدي والأنعام "
        "المشعرة... transcribe fully INCLUDING the name of the person quoted (عروة? عمر?) and the "
        "full quoted words يا بني... and the blue bracket [الموطأ رقم: NNN] DIGIT BY DIGIT (1120?). "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "r673b-p121-mil": (
        "Zoom 600 dpi, middle band of an Arabic schoolbook page (lesson 17). Transcribe EXACTLY "
        "right-to-left: 1) the green sub-line 2- العمل في الهدي; 2) the quote عن عبد الله بن عمر "
        "إذا كان أهدى... (transcribe the FULL matn word by word — قلّده قبل يده؟ وقدّه؟ بذي "
        "الحليفة؟ بغلين؟ ثم ساق؟) and whether this matn carries its own blue bracket [الموطأ رقم: "
        "NNN]; 3) the second quote وعن نافع: أنّ عبد الله بن عمر كان إذا طعن في سنام هديه وهو "
        "يُشعِرُهُ قال: بسم الله وله أكبر(?) امتثالاً — transcribe EXACTLY, then the blue bracket "
        "[الموطأ رقم: NNN] DIGIT BY DIGIT (1114?); 4) the sentence لقوله تعالى: «...» with bracket "
        "[سورة NNN الآية: NNN] — transcribe the SURAH NAME letter by letter (الحج? البقرة?) the "
        "verse number DIGIT BY DIGIT and the quoted TEXT (expected لِتُكَبِّرُوا اللهَ عَلَى مَا "
        "هَدَاكُمْ — or different?). Mark illegible as [؟]. Short French notes at the end."
    ),
    "r673b-p121-bas": (
        "Zoom 600 dpi, bottom third of an Arabic schoolbook page (lesson 17). Transcribe EXACTLY "
        "right-to-left: 1) the green rubric ثالثا: [NAME — الانتفاع بالهدي? الاستفادة?] and sub-line "
        "1- ركوب الهدي; 2) the quote عن أبي هريرة رضي الله عنه: أنّ رسول الله رأى رجلا يسوق بدنة "
        "فقال: اركبها فقال: يا رسول الله إنها بدنة فقال: اركبها ويلك في الثانية أو الثالثة — "
        "transcribe exactly; 3) any blue bracket [الموطأ رقم: NNN] DIGIT BY DIGIT; 4) whether the "
        "text continues onto the next page (does the quote end here?). Mark illegible as [؟]. "
        "Short French notes at the end."
    ),
    "r673b-p122-haut": (
        "Zoom 600 dpi, top third of an Arabic schoolbook page (lesson 17). Transcribe EXACTLY "
        "right-to-left: 1) the opening: فاحتَجَّ بإطلاق هذا الحديث وبقوله تعالى: «...» — transcribe "
        "the quoted verse TEXT exactly (لها منافع إلي أجل مسمى؟ لك فيها منافع?) then the bracket — "
        "is it [سورة NNN] or [الموطأ رقم: NNN]? read ANY digits DIGIT BY DIGIT (surah name letter "
        "by letter, verse number); 2) the following sentence من أجاز ركوب الهدي اختيارا حيث لا "
        "يضرّه وكرهه المالكية والجمهور [هذا هو المشهور عنه إلا لضرورة؟] — transcribe fully and "
        "tell me where the words الآية [NNN] appear and what number (digit by digit 31? 13?) and "
        "in which sentence they belong; 3) the sentence وسوق الهدي وركوبه قد آل في الغالب الأعم "
        "إلى بدائل أخرى تحقق مقصد الشرع وحاجة المكلف غير أن هذا لا يرفع الأصل عند إمكانه — "
        "transcribe exactly. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r673b-p122-mil": (
        "Zoom 600 dpi, middle band of an Arabic schoolbook page (lesson 17). Transcribe EXACTLY "
        "right-to-left: 1) the green sub-line 2- شرب لبن الهدي; 2) the paragraph كرهه مالك في "
        "الاختيار ولو فضل الري عن فصيله؛ لأنه نوع من الرجوع في [الهدي? الصدقة?] — transcribe the "
        "word after الرجوع في EXACTLY (الهدي or الصدقة?), then ومحل [الصدقة? الكراهة?] حيث لا "
        "ضرر وإلا غرم — transcribe exactly; 3) the quote فعن هشام بن عروة أن أباه(?) قال: إذًا "
        "اضطررت إلى بدنتك فَارْكَيْهَا رُكُوبًا غَيْرَ فَادِحٍ وَإِذَا اضْطُرِرْتَ إِلَى "
        "لَبَنِهَا فَاشْرَبْ [يُرَوَّفُ?] فَصِيلُهَا(?) فَإِذَا نَحَرْتَهَا فَاجْعَلْ(?) "
        "فَصِيلَهَا مَعَهَا — transcribe the isnād name EXACTLY and every word of the matn, then "
        "the blue bracket [الموطأ رقم: NNN] DIGIT BY DIGIT (1112?). Mark illegible as [؟]. Short "
        "French notes at the end."
    ),
    "r673b-p122-bas": (
        "Zoom 600 dpi, bottom third of an Arabic schoolbook page (lesson 17). Transcribe EXACTLY "
        "right-to-left: 1) the green sub-line 3- أكل صاحب الهدي من هديه; 2) the quote عن مالك أنه "
        "سمع أهل العلم يقولون: لا يأكل صَاحبُ الْهَدْيِ... — transcribe the matn EXACTLY including "
        "the words after هديّه (والنِّسُكْ? من كل شيء?) and the blue bracket [الموطأ رقم: NNN] DIGIT "
        "BY DIGIT (1126?); 3) the sentence والمشهور من المذهب أنه يأكل من كل هدي بلغ محله إلا "
        "[ثلاثة?]: جزاء [الصيد?] و[فتية?/تُفد?] الأذى(?) وما نُذِرَ(?) للمساكين — transcribe the "
        "three exceptions EXACTLY word by word; 4) the closing paragraph يستفاد من الدرس أن "
        "الشريعة... transcribe fully; 5) the rubric التقويم with EVERY numbered item exactly. "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "r673b-p123-haut": (
        "Zoom 600 dpi, top of the LAST page of lesson 17 (p.123). Transcribe EXACTLY right-to-left "
        "the FULL Muwaṭṭa athar in the green box: عن مالك عن عبد الله بن دينار أنه كان يرى عبد "
        "الله بن عمر... — transcribe EVERY word: does it say يُهدِي في الحجِّ بدنتين بدنتين وفي "
        "العُمْرَةِ [بقرة? بدنة?] [وَهُو يَنْحَرُ? وَهُو يَقِيمُ? وَهِيَ قَائِمَةٌ?] في دار خالد "
        "بن أسيد وكان فيها مِنْزَلُهُ قال: ولقد رأيته طَعَنَ في لِبَةِ بَدَنِتِهِ حتى [خرجت? "
        "خرحَّت?] الحَرْبَةُ من تحت كتِفِهَا — resolve EACH bracketed variant from the image, then "
        "the blue bracket [الموطأ رقم: NNN] DIGIT BY DIGIT (1108?). Mark illegible as [؟]. Short "
        "French notes at the end."
    ),
    "r673b-p123-bas": (
        "Zoom 600 dpi, bottom two-thirds of the last page of lesson 17 (p.123). Transcribe EXACTLY "
        "right-to-left EVERY rubric and line: 1) the green rubric title after the athar box (is it "
        "أستخرج الأثر? الاستخلاص? استخلاص المضامين?) letter by letter; 2) the task line under it "
        "(أستخرج أحكام الهدي التي يشير إليها الأثر?) exactly; 3) the next green rubric (الإعداد "
        "للدرس المقبل? الإعداد القبلي?) exactly; 4) the formula أحفظ أحاديث الدرس المقبل وأجيب عن "
        "الآتي exactly; 5) EVERY numbered question exactly (1- أبحث عن حكم من فاته الحج وكيفية "
        "تحلله من إحرامه 2- ماذا يفعل من باشر زوجه وهو محرم بالحج؟); 6) the page number. Mark "
        "illegible as [؟]. Short French notes at the end."
    ),
}

IMG = {
    "r673b-p120-bas": "z-p120-bas.png",
    "r673b-p121-haut": "z-p121-haut.png",
    "r673b-p121-mil": "z-p121-mil.png",
    "r673b-p121-bas": "z-p121-bas.png",
    "r673b-p122-haut": "z-p122-haut.png",
    "r673b-p122-mil": "z-p122-mil.png",
    "r673b-p122-bas": "z-p122-bas.png",
    "r673b-p123-haut": "z-p123-haut.png",
    "r673b-p123-bas": "z-p123-bas.png",
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
