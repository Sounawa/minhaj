# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM pleine page R663 (slot pdf-mut23h2x-401, leçon 12
أحكام السعي بين الصفا والمروة, p.84-89). Mécanique hadith3-vlm-read-402-r657.py
(R657) : couche texte recoupée par rendus 300 dpi (tr-tmp/qa-crops-r663/),
chaque lecture = cache tr-tmp/qa-crops-r663/_r663-read-<name>.json — toute
récusation de la couche texte est documentée (nom d'image, ce qui a été lu),
jamais devinée. Moteur : CLI z-ai vision (SDK VLM), prompts ciblés par page."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r663"

PROMPTS = {
    "r663-p84-full": (
        "Full Arabic schoolbook page (300 dpi), lesson 12 opening, aḥkām as-saʿy between Ṣafā and Marwa. "
        "Transcribe ALL Arabic lines EXACTLY, right-to-left, in reading order, from the top: 1) green banner "
        "+ blue medallion (expected الدرس 12, title أحكام السعي بين الصفا والمروة) and rubric أهداف الدرس "
        "with EVERY numbered objective (two expected: أن أتعرف أحكام السعي بين الصفا والمروة وصفته / أن أتبع "
        "هدي النبي في أحكام السعي); 2) the tamhīd/intro paragraph: transcribe EVERY sentence exactly "
        "(expected: السعي بين الصفا والمروة ركن من أركان الحج التي لا يسوغ تركها بحال، وينجبر بالدم... فما "
        "أحكام السعي بين الصفا والمروة؟) including the words after وينجبر and before فما; 3) the first bold "
        "hadith quote with its full chain (expected: عن هشام بن عروة عن أبيه... عائشة أم المؤمنين...) — "
        "transcribe the matn EXACTLY word by word, especially the quoted Quranic text and the phrase before "
        "the verse quote (expected words like أرأيت؟ سُنَّ حديثا يومئذ...); 4) the Quranic quote inside the "
        "hadith (expected إِنَّ الصَّفَا وَالْمَرْوَةَ مِنْ شَعَائِرِ اللهِ... فَلَا جُنَاحَ عَلَيْهِ أَنْ "
        "يَطَّوَّفَ بِهِمَا...) with the blue bracket [سورة البقرة الآية: NNN] — read the verse number DIGIT "
        "BY DIGIT (157 or 158?). Mark illegible as [؟]. Short French notes at the end."
    ),
    "r663-p85-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the end of the first hadith (ʿĀʾiša matn about الأنصار, مناة, قديد, يطوفون بين "
        "الصفا والمروة) — transcribe EVERY line exactly; 2) the green rubric الشرح and EVERY glossed word "
        "with its FULL gloss text (expected glosses: مناة، ثقيلة، يعتلون — transcribe each gloss exactly, "
        "including the Zarqānī-style explanations); 3) the second bold hadith quote with full chain (expected: "
        "عن هشام بن عروة عن أبيه أن سودة بنت عبد الله بن عمرو؟...) — transcribe EVERY word of the chain and "
        "matn exactly (the woman of عروة بن الربير walking between Ṣafā and Marwa, امْرَأَةٌ تَقِيَّةٌ, "
        "قَضَتْ طَوَاقَهَا, نُودِيَ بالأول من الصبح, فَقَصَّتْ طَوَافَهَا, يَنْهَاهُمْ أَشَدَّ النَّهْىِ, "
        "خَابَ هَؤُلَاءِ وَخَسِرُوا, وَبِالْمَرَضِ بِحَيَاءَ مِئْهَمْ...) with the blue [الموطأ رقم: NNN] — "
        "read the hadith numbers DIGIT BY DIGIT (both occurrences on this page). Mark illegible as [؟]. "
        "Short French notes at the end."
    ),
    "r663-p86-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the rubric استخلاص المضامين with EVERY numbered item (digits digit-by-digit; "
        "expected three items: أحدد حكم السعي بين الصفا والمروة / أبين صفة السعي / ما حكم من ركب أو وقف "
        "أثناء السعي؟); 2) the green rubric أولا: حكم السعي بين الصفا والمروة and the first commentary "
        "paragraph quoting the ʿĀʾiša hadith with the Quranic citation — transcribe the quoted verse and its "
        "blue bracket [سورة البقرة الآية: NNN] with the number DIGIT BY DIGIT (157 or 158?); 3) the "
        "commentary explaining the āya meaning (expected: ليس على الرجل شيء إن لم يسع بهما... إذ مفهوم "
        "الآية أن السعي ليس بواجب لأن رفع الجناح يقتضي الإباحة فصححت له...) — transcribe EVERY line; 4) the "
        "paragraph about ʿĀʾiša's answer and فهم (expected: عائشة رضي الله عنها ما نن عنها...) and the "
        "closing reference [صحيح مسلم]; 5) the paragraph on فقه عائشة ومعرفة الأحكام بالألفاظ (expected "
        "because the āya's ظاهر implies رفع الجناح...) — transcribe fully. Mark illegible as [؟]. Short "
        "French notes at the end."
    ),
    "r663-p87-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the opening lines of the page (the continuation about the man who thought nothing "
        "is allowed at night between Ṣafā and Marwa — expected: فسأل الغروب عند صلاتها له لا يشرع أنه فظن "
        "الظهر عليه... ذهب جماهير... لا صحيح فالجواب صليته...) — transcribe exactly; 2) the paragraph about "
        "the scholars saying saʿy is a rukn (expected: العلماء من الصحابة والتابعين ومن بعدهم إلى أن السعي "
        "ركن لا يصح الحج إلا به ولا يجبر بدم ولا غيره); 3) the green rubric ثانيا: صفة السعي and its sub-line "
        "1- البدء بالصفا في السعي; 4) the bold hadith quote with full chain (expected: عن جابر بن عبد الله "
        "أنه قال: قال رسول الله: حين خرج من المسجد قال: الله أكبر بدا الله به?) with blue [الموطأ رقم: NNN] "
        "digit-by-digit and the commentary mentioning surat al-Baqara with the verse about البدء بالصفا "
        "(expected: لأن الله بدا بهبابه؟ وقد قال في سورة البقرة الآية: NNN فقال: فابدأوا ما؟) — read the "
        "verse number DIGIT BY DIGIT; 5) the sub-line 2- الرقي على الصفا والمروة والدعاء and the "
        "commentary (expected الجمهور: إذا كان بي وقف على الصفا ويستقبل القبلة ويكبر ثلاثا ويقول: لا إله إلا "
        "الله وحده لا شريك له له الملك له الحمد وعد على كل شيء قدير? ثلاث مرات ويودعو?...) with blue "
        "[الموطأ رقم: NNN] digit-by-digit, the paragraph about الرقي عند أحد من العلماء وفي الذكر والدعاء "
        "ولا حدّ له مثل ذلك, the verse from surat Ghāfir with number DIGIT BY DIGIT (expected: وإلا نك لآ "
        "تخلف؟ says قل اللهم قال في سورة غافر الآية: 60?) and the ending hadith (expected: من تنزه؟ عني "
        "حنى؟ أنا مسلم؟ [الموطأ رقم: NNN]). Mark illegible as [؟]. Short French notes at the end."
    ),
    "r663-p88-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the green sub-line 3- الإسراع ببطن الوادي and the Jābir hadith (expected: فعن "
        "جابر عنه؟ رضي الله عنه أن رسول الله قال: كان؟ إذا مشى من الصفا إلى المروة مشى حنَا إذا انصبت "
        "قدماه في بطن الوادي سعى؟ [الموطأ رقم: NNN]) — transcribe exactly, read the blue number DIGIT BY "
        "DIGIT, plus the gloss line (انصباب القدم وانحدار الصبب والموضع المنحدر منه); 2) the green rubric "
        "ثالثا2: الركوب والوقف في السعي and sub-line الركوب للسعي; 3) the commentary (expected: السعي مشيا "
        "واجب على القادر عليه؛ لأنه قال: كان إذا أراد الصفا والمروة مشى؟ وكانت سودة رضي الله عنها مشى؟ ولا "
        "تكمل طوافها إلا... لثقل جسمها ولم تكن تركب؟ للصبح؛ وكان عروة إذا رأى الناس يسعون على الدواب "
        "ينهاهم أشد النهي؛ لما ورد في حديث هشام بن عروة) — transcribe exactly; 4) the sub-line الوقوف "
        "للحديث خلال السعي with the Mālik ruling (expected: عن مالك عن رجل يلقى الحَرْكَة؟ الرجل؟ بين الصفا "
        "والمروة فحَثَّه: يحنث? فقال: لا يكره؛ لأن المطلوب حينئذ الذكر والدعاء له؟ [الموطأ رقم: NNN]) — "
        "read the blue number DIGIT BY DIGIT; 5) the green rubric رابعا: حكم من جهل فبدأ بالسعي قبل الطواف "
        "and its full commentary with the long hadith quote (expected: قال مالك في رجل جهل فبدأ بالسعي بين "
        "الصفا والمروة قبل أن يطوف بالبيت قال: يَرْجِعْ بالبَيْتِ فَطَافَ بِهِ وَيَسْعَى بين الصفا والمروة، "
        "وإن جهل ذلك حتى خرج من مكة يستبعد؟ فإنه يرجع إلى مكة فيطوف... وإن كان امرأة؟ رجع فطاف بالبيت وسعى "
        "بين الصفا والمروة وإن كان امرأة؟ ثم عليه عمرة أخرى الهدَيُ؟ [الموطأ رقم: NNN]) — transcribe EVERY "
        "line, read the blue number DIGIT BY DIGIT. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r663-p89-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the rubric استخلاص المضامين with EVERY numbered item and sub-case (expected: 1- "
        "أبين حكم الحالتين الآتيتين مع الاستدلال والتعليل: حجت امرأة بطيئة السير السائرة من يرافقها ركبت في "
        "سعيها بين الصفا والمروة؛ حجت امرأة؟ الظاهر؟ [second case transcribe EXACTLY]; 2- ما حكم الرقي على "
        "الصفا والمروة؟); 2) any commentary paragraph after these questions (expected: فإنه يقطع سعييه يتم "
        "طوافه على ما يستيقن ثم يركع ركعتي الطواف ثم يبتدئ سعيه بين الصفا والمروة [الموطأ رقم: NNN]) with "
        "the blue number DIGIT BY DIGIT; 3) the line أقرأ الأثر وأبين حكم من نسي شيئا من طوافه أو شك فيه "
        "فتذكر ذلك في السعي — transcribe exactly; 4) the rubric الإعداد القبلي (expected أحفظ أحاديث الدرس "
        "المقبل وأجيب عن الآتي) with EVERY numbered item (expected: 1- أبحث عن أحكام الصلاة والخطبة بعرفة، "
        "2- أبين حكم صيام يوم عرفة للحاج) — digits digit-by-digit. Mark illegible as [؟]. Short French "
        "notes at the end."
    ),
}

IMG = {
    "r663-p84-full": "p84-full.png",
    "r663-p85-full": "p85-full.png",
    "r663-p86-full": "p86-full.png",
    "r663-p87-full": "p87-full.png",
    "r663-p88-full": "p88-full.png",
    "r663-p89-full": "p89-full.png",
}


def run(name):
    out = os.path.join(DIR, f"_r663-read-{name}.json")
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
