# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM pleine page R657 (slot pdf-mut23h2x-402, leçon 13
أعمال يوم عرفة). Mécanique hadith3-vlm-read-400-r654.py (R654) : couche texte
recoupée par rendus 300 dpi (tr-tmp/qa-crops-r657/), chaque lecture = cache
tr-tmp/qa-crops-r657/_r657-read-<name>.json — toute récusation de la couche
texte est documentée (nom d'image, ce qui a été lu), jamais devinée.
Moteur : CLI z-ai vision (SDK VLM), prompts ciblés par page."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r657"

PROMPTS = {
    "r657-p90-full": (
        "Full Arabic schoolbook page (300 dpi), lesson 13 opening. Transcribe ALL Arabic lines EXACTLY, "
        "right-to-left, in reading order, from the top: 1) green banner + blue medallion (expected الدرس 13, "
        "title أعمال يوم عرفة) and the rubric أهداف الدرس with EVERY numbered objective (read each leading "
        "digit digit-by-digit; expected three objectives about الوقوف بعرفة / الصلاة والخطبة بعرفات / مقاصد "
        "الشرع من الوقوف بعرفة); 2) the tamhid paragraph and the short questions at its end (expected ما حكم "
        "الوقوف بعرفة وما أعمال هذا اليوم) — transcribe every question line exactly; 3) the first bold hadith "
        "quote with its full chain of transmission and blue bracketed reference [الموطأ رقم: NNN] — expected "
        "hadith of أفضل الدعاء دعاء يوم عرفة — read the blue reference digits DIGIT BY DIGIT; 4) the second "
        "bold hadith quote of Ibn Umar through Nafi' (expected من لم يقف بعرفة فقد فاته الحج) with its blue "
        "[الموطأ رقم: NNN] read digit-by-digit; 5) the beginning of the third bold hadith quote (expected "
        "chain through مالك عن أبي النضر about أم الفضل بنت الحارث) — transcribe every chain word. "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "r657-p91-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the continuation of the أم الفضل hadith about صيام يوم عرفة (expected lines: "
        "تماروا عندها في صيام يوم عرفة، قال بعضهم هو صائم، فقال رسول الله صلى الله عليه وسلم: صيام نص؟ — "
        "transcribe exactly, mark [؟] where the print is unclear) with blue [الموطأ رقم: NNN] read "
        "digit-by-digit; 2) the long hadith of الحجاج visiting عبد الله بن عمر يوم عرفة (expected: كان يوم "
        "عرفة جاءه عبد الله بن عمر وأنا معه؟، فقال له يا أبا عبد الرحمن، ملحفة معصرة، السرادق، فقال ما لك يا "
        "أبا عبد الرحمن؟، إن كنت تصيب هذه السنة الحجاج؟ فاقصر الخطبة وعجل الصلاة) — transcribe EVERY line of "
        "this hadith exactly with its blue [الموطأ رقم: NNN] read digit-by-digit; 3) the biography notice of "
        "أم الفضل بنت الحارث (expected: لُبابة الكبرى بنت الحارث بن حُبَب؟، أم بني العباس الستة النجباء، كُنيت "
        "بأبيهم كأبيهم الأكبر، قال ابن حبان: توفيت في خلافة عثمان قبل زوجها العباس) — transcribe exactly; 4) "
        "the biography notice of سالم بن عبد الله بن عمر بن الخطاب العدوي (expected lines: أبو محمد؟، من "
        "العدويين، إمام من أئمة البصر? مالك: أتخذ العلم سنة? توفي سنة NNN هـ) — read the death year "
        "DIGIT BY DIGIT. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r657-p92-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the gloss rubric الشرح and EVERY glossed word with its definition (expected: "
        "تمارَوا، السرادق، مُعَصْفَرة) — transcribe each gloss exactly; 2) the rubric استخلاص المضامين with "
        "EVERY numbered item (read leading digits digit-by-digit; expected three items about مكان وزمان "
        "الوقوف بعرفة / الفطر والركوب والطهارة / صلاة وخطبة يوم عرفة); 3) the green rubric أولا: موقف عرفة "
        "and sub-line 1- مكان الوقوف; 4) the bold hadith quote (expected كلها موقف أي جزء منها آت بسنة "
        "إبراهيم عليه السلام) with its full chain and blue [الموطأ رقم: NNN] read digit-by-digit — also "
        "transcribe the printed pronunciation note if any (عُرَنَّة بضم العين وفتح الراء وارتفاع؟); 5) the "
        "commentary paragraph quoting an-Nawawi (قال النووي: وأما ما اشتهر عند العوام من الاعتناء بصعود "
        "الجبل...) — transcribe fully to its end. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r657-p93-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the closing lines of the an-Nawawi commentary (expected أنّ الفضيلة أنّ موقفه عند "
        "الصخرات... فليقرب منه بحسب الإمكان); 2) the green sub-line 2- وقت الوقوف and the full commentary "
        "paragraph (expected: يبدأ وقت الوقوف من زوال التاسع من ذي الحجة ويمتد إلى فجر يوم الأضحى، غير أنه "
        "لا بد من الوقوف بعد الغروب ولو زمنا يسيرا لتحصيل الركن، فمن لم يقف ليلة المزدلفة قبل طلوع الفجر فلا "
        "وقوف له وقد فاته الحج لأن الوقوف ركن لا يجزئ بالنهار فقد) — transcribe exactly; 3) the re-quoted "
        "hadith of Ibn Umar (من لم يقف بعرفة فقد فاته الحج ومن وقف ليلة المزدلفة قبل أن يطلع الفجر فقد أدرك "
        "الحج) with blue [الموطأ رقم: NNN] digit-by-digit; 4) the closing Mālik-style judgment line (expected "
        "فمن فاته الوقوف بالليل فليتحلل بعمرة وعليه القضاء في عام قابل) — transcribe exactly; 5) the green "
        "rubric ثانيا: آداب يوم عرفة and sub-line 1- تعجيل الرواح من عرفة إلى منى with the first lines of "
        "the الحجاج hadith (expected من السنة تعجيل الرواح فعن سالم بن عبد الله عن أبيه) and the second "
        "sub-line 2- الطهارة للوقوف with its first lines (يستحب للحاج عند الوقوف بعرفة أن يكون متوضئا) and "
        "the Mālik question-answer about praying/rutting without wudu (سئل مالك هل يقف أحد بعرفة أو بالمزدلفة "
        "أو يرمي وهو غير متوضئ) and the beginning of the bold quote (المُنِيّ? الرجل يُضَعِّعُه? فهو غير طاهر). "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "r657-p94-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the end of the Mālik ruling about purity at ʿArafa (expected قال لا شيء عليه "
        "الحائض أمره? الرجل المُنيّ يُضَعِّعُه فهو غير طاهر ولا شيء في ذلك) with blue [الموطأ رقم: NNN] read "
        "DIGIT BY DIGIT; 2) the green sub-line 3- الفطر يوم عرفة and the full أم الفضل hadith (expected عن أم "
        "الفضل بنت الحارث... تماروا عندها في صيام يوم عرفة قال بعضهم هو صائم فقال رسول الله صلى الله عليه "
        "وسلم: صيام نص? فشرب? وهو واقف على بعير) with blue [الموطأ رقم: NNN] digit-by-digit; 3) the "
        "commentary paragraph (expected ولذلك كان فطر يوم عرفة للحاج أفضل من صومه لأنه اختاره النبي لنفسه "
        "وللتقوى، والجمهور: يستحب فطره للحاج وإن كان قويا، وكانت عائشة لا ترى استحباب الفطر يوم عرفة، قال "
        "القاسم: ولقد رأيتها عشيّة عرفة ما يَدْقَعُ كُمّها تَدْعُو وتفترٌ? بشرّاب?) with blue [الموطأ رقم: "
        "NNN] digit-by-digit; 4) the green rubric ثالثا: الصلاة والخطبة يوم عرفة and sub-line 1- صلاة الظهر "
        "والخطبة يوم عرفة with the Mālik ruling (expected لا يجهر الإمام بالقراءة في صلاة الظهر يوم عرفة لأن "
        "الظهر سرية ويخطب بجامع النمرة? حتى يعلم الناس...) and the bold quote (expected صلاة يوم عرفة إنما "
        "هي ظهر إن وافقت الجمعة ولا تصلى الجمعة يوم وافقت عرفة؟ قصرت من أجل السفر) with blue [الموطأ رقم: "
        "NNN] digit-by-digit; 5) the closing Mālik line about the imam of the pilgrim if Friday coincides "
        "(expected لا جمعة على مسافر قال مالك في إمام الحاج إذا وافق يوم الجمعة يوم عرفة أو يوم النحر أو "
        "بعض أيام التشريق: إنما لا يُجمع في شيء من تلك الأيام) with blue [الموطأ رقم: NNN] digit-by-digit. "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "r657-p95-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the green sub-line 2- قصر الصلاة وتعجيل الخطبة يوم عرفة and its full commentary "
        "(expected يستفاد من قول سالم للحجاج في حديث الدرس إن كنت تصيب هذه السنة... فجعل قصر الصلاة وعجل "
        "الخطبة... transcribe EVERY line including any degraded words, mark [؟]); 2) the concluding line "
        "(expected يستفاد من الدرس أن الإسلام دين الوحدة والاجتماع على الهدى وفي الاجتماع أسمى مظاهر الوحدة "
        "والمساواة بين الناس); 3) the rubric التقويم (or التوقيم — read it exactly) with EVERY numbered "
        "question line (digits digit-by-digit; expected ما حكم صوم الحاج بعرفة مع الاستدلال / أبين حكم "
        "المسألتين الآتيتين مع الاستدلال والتعليل) and the first case (رجل وقف بعرفة غير طاهر); 4) the "
        "second evaluation case as a bold hadith quote with full chain (expected chain مالك عن ابن أبي ذئب؟ "
        "عن ابن لهيعة? عن أبي الزناد? عن... بن كريز: قال رسول الله صلى الله عليه وسلم وما تجاوز? عن الذنوب "
        "العظام إلا ما رأى يوم بذر? إنه لذ? جبريل رأى الملايكة) — transcribe EVERY word exactly, especially "
        "the ambiguous words, mark [؟] if truly unclear, and read the blue [الموطأ رقم: NNN] DIGIT BY DIGIT. "
        "Short French notes at the end."
    ),
    "r657-p96-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the exploitation line (expected أقرأ الحديث وأستخلص منه فضل يوم عرفة وأنش?ر ذلك "
        "بين عائلتي — transcribe the verb exactly: أنشُر أو أنسب?); 2) the rubric الإعداد القبلي and the "
        "instruction line (أحفظ أحاديث الدرس المقبل وأجيب عن الآتي) with EVERY numbered item — transcribe "
        "each item FULLY (expected: 1- أبحث عن حكم المبيت والوقوف بمزدلفة، 2- أبين الفضل العظيم... — read "
        "each leading digit digit-by-digit and transcribe every remaining word of item 2 to its final word); "
        "3) any page footer or decorative line. Mark illegible as [؟]. Short French notes at the end."
    ),
}

IMG = {
    "r657-p90-full": "p90-full.png",
    "r657-p91-full": "p91-full.png",
    "r657-p92-full": "p92-full.png",
    "r657-p93-full": "p93-full.png",
    "r657-p94-full": "p94-full.png",
    "r657-p95-full": "p95-full.png",
    "r657-p96-full": "p96-full.png",
}


def run(name):
    out = os.path.join(DIR, f"_r657-read-{name}.json")
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
