# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM pleine page R670 (slot pdf-mut23h2x-403, leçon 14
أحكام مزدلفة, p.97-103). Mécanique hadith3-vlm-read-401-r663.py (R663) :
couche texte recoupée par rendus 300 dpi (tr-tmp/qa-crops-r670/), chaque
lecture = cache tr-tmp/qa-crops-r670/_r670-read-<name>.json — toute récusation
de la couche texte est documentée (nom d'image, ce qui a été lu), jamais
devinée. Moteur : CLI z-ai vision (SDK VLM), prompts ciblés par page."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r670"

PROMPTS = {
    "r670-p97-full": (
        "Full Arabic schoolbook page (300 dpi), lesson 14 opening on al-Muzdalifa (أحكام مزدلفة). "
        "Transcribe ALL Arabic lines EXACTLY, right-to-left, in reading order, from the top: 1) green banner "
        "+ blue medallion (expected الدرس 14, title أحكام مزدلفة) and rubric أهداف الدرس with EVERY numbered "
        "objective (expected two: أن أتعرف أحكام ليلة العاشر من ذي الحجة / أن أتعرف حكم الدعاء والذكر ليلة "
        "المزدلفة وعند الوقوف بالمشعر الحرام — transcribe each EXACTLY, note whether ليلة is followed by "
        "المزدلفة or another word); 2) the intro paragraph defining النزول بالمزدلفة (expected: من مناسك الحج، "
        "وهي موضع بين عرفة ومنى، وسميت بذلك لأن...) — transcribe the ENTIRE reason clause exactly, especially "
        "the words after لان and before تقدموا; 3) the guiding questions (فما هي صفة السير إلى المزدلفة وما "
        "أحكام المبيت والصلاة بها وما حكم الوقوف بالمشعر الحرام؟); 4) the first bold hadith quote with its "
        "full chain (expected: عن مالك عن هشام بن عروة عن أبيه أن أسامة بن زيد...) — transcribe the matn "
        "EXACTLY word by word (expected: كيف كان يسير رسول الله في حجة الوداع حين دفع؟ فقال: كان يسير "
        "العنق فإذا وجد فجوة نصّ فوق العتق) with the blue bracket [الموطأ رقم: NNN] — read the number DIGIT "
        "BY DIGIT (1165 or other?). Mark illegible as [؟]. Short French notes at the end."
    ),
    "r670-p98-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the second bold hadith quote with its FULL chain (expected: عن مالك عن موسى بن "
        "عقبة عن كريب عن عباس عن أسامة بن زيد...) — transcribe EVERY word of chain and matn EXACTLY: the "
        "Prophet leaving ʿArafat (من عرفة), the wuḍūʾ story (كان إذا حنى كان يدفع بالشعب؟ فتوضأ؟ فلم "
        "يسبغ الوضوء فقيل له: الصلاة يا رسول الله؟ فقال: الصلاة أمامك), riding at Muzdalifa (فلما جاء "
        "المزدلفة ركب), praying Maghrib (فأسبغ الوضوء ثم أقيمت الصلاة فصلى المغرب), dismounting (ثم خات؟ "
        "كل إنسان بعيره منزله), then ʿIshāʾ (ثم أقيمت العشاء فصلاها ولم يصل بينهما شيئا) — with the blue "
        "[الموطأ رقم: NNN] read DIGIT BY DIGIT (1160?) and any small footnote number; 2) the green rubric "
        "ترجمة الراوي with the FULL biography of أسامة بن زيد بن حارثة الكلبي (transcribe EVERY line: "
        "ولده بعد حبه؟ وعاش بعد البعثة؟ كان يكتف النبي؟ كثير البر؟ قدناه اديكاه؟ إل كرا؟ هوك الله علا غ؟ "
        "على بعض الأقوال فيه 95 عمره؟ توفي بالمدينة سنة أي؟ في خلافة أبي بكر وعمر بن الخطاب) — transcribe "
        "exactly, mark [؟] where the print is broken; 3) the green rubric الشرح with EVERY glossed word and "
        "its FULL gloss (expected: العَنَّقَ: سير بين الإبطاء والإسراع وقيل: الذي يتحرك به عنق الدابة / "
        "نَصَّ: أسرع) — transcribe exactly. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r670-p99-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the end of the الشرح glosses at the top (expected: دَفْعَ: انصرف من عرفة إلى "
        "المزدلفة وسمي دفعا لازدحامهم إذا انصرفوا / الصلاة: موضعك هذه... وهو مزدلفة؟ — transcribe the "
        "second gloss EXACTLY especially what precedes وهو); 2) the box/rubric whose title contains "
        "استخلاص نص المشاعين or similar (read its TITLE EXACTLY letter by letter: المشاعين؟ المشعرين؟ "
        "المشاعر؟) with EVERY numbered item (expected 3 items: كيف يسير الحجاج إلى المزدلفة؟ / أبين أحكام "
        "الوقوف والصلاة بمزدلفة / هل يجب على الحاج المبيت بالمزدلفة؟); 3) the green rubric أولا: الدفع إلى "
        "مزدلفة والوقوف بها and sub-line 1- السير من عرفة إلى المزدلفة; 4) the FULL commentary paragraph "
        "(expected: إذا تحقق غروب الشمس يوم عرفة انصرف الإمام والناس معه إلى المزدلفة بسكينة ووقار فإذا "
        "وجدوا متسعا أسرعوا استعجالا للصلاة لأن المغرب لا تصلى إلا مع العشاء جمع تأخيرا بالمزدلفة بعد "
        "الشفق...) — transcribe EVERY line exactly including the quote of the Usāma hadith in brackets "
        "(أنا جالس معه كيف كان يسير رسول الله في حجة الوداع حين دفع؟ فقال: كان يسير العنق فإذا وجد فجوة...) "
        "and the sentence after (وهذه الكيفية الجمع بين مصلحة الوقار والسكينة عند الزحمة ومصلحة الإسراع "
        "عند عدمها لأجل الصلاة...) and the Muwaṭṭa quote (فعن عروة رضي الله عنه قال: سئل... أن نافع: أن "
        "عبد الله بن عمر كان يحرك راحلته في بطن محسر رمية بحجر؟) with blue [الموطأ رقم: NNN] read DIGIT "
        "BY DIGIT (1166?) and the gloss line (وبطن محسر واد قرب المزدلفة يسميه أهل مكة وادي النار). Mark "
        "illegible as [؟]. Short French notes at the end."
    ),
    "r670-p100-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the green sub-line 2- الوقوف بالمزدلفة and the quote of ʿAlī? or ʿUmar? (expected: "
        "قال علي؟ أو قال عمر؟: والمزدلفة كلها موقف وارتفعوا عن بطن محصر [الموطأ رقم: NNN] — read the "
        "speaker name EXACTLY and the number DIGIT BY DIGIT (1152?)); 2) the sentence وفي حديث جابر: وقد "
        "قفت وما قفت المزدلفة كلها موقف؟ — transcribe exactly with any number; 3) the small reference lines "
        "in faint print between them (راسي عليه العمل رك تا ات يدرو؟ مختصر خليل؟ قال عاطفا على المنديبات؟ "
        "الاستحباب والاستحباب والمختصر؟[مختصر للإسفار ص: 97]?- بالمشعر الحرام يكبر ويدعو؟) — transcribe what "
        "is legible exactly; 4) the green rubric ثانيا: أحكام المزدلفة and sub-line 1- صلاة المغرب ليلة "
        "الأضحى بالمزدلفة; 5) the FULL paragraph (expected: السنة بعد الدفع من عرفة تأخير صلاة المغرب "
        "وجمعها مع صلاة العشاء بالمزدلفة وهذا جمع تأخير فقد ثبت أن رسول الله صلى الله عليه وسلم صلى "
        "المغرب والعشاء جميعا بالمزدلفة [الموطأ رقم: NNN digit by digit — 1192?] وعن نافع وعن عبد الله؟ "
        "كان حمر؟ لزمه؟ فمن صلى المغرب قبل العشاء والمزدلفة جميعا [الموطأ رقم: NNN digit by digit — 1195?] "
        "نقل ابن القاسم أن عليه الإعادة والجمهور على الإجزاء دخول وقت العشاء؟) — transcribe EVERY line "
        "exactly; 6) the green sub-line 2- صفة الجمع وسببه بمزدلفة and the FULL paragraph (expected: ثبت أن "
        "النبي لما جاء مزدلفة نزل عن ناقته القصواء فتوضأ بماء زمزم ثم أقيمت الصلاة فصلى المغرب بالناس قبل "
        "حط الرحال ثم أناخ كل إنسان بعيره رفقا بالدواب ثم أقيمت العشاء فصلاها بالناس ولم يتنفل بينهما لأن "
        "الولاء فوجب كالصلاة الواحدة... في حديث أسامة مق بده؟ دفع يد الله يا من؟) — transcribe EVERY line "
        "exactly. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r670-p101-full": (
        "Full Arabic schoolbook page (300 dpi) — the OCR text layer is nearly empty for the top half; "
        "transcribe from the IMAGE ALL Arabic lines EXACTLY, right-to-left, in reading order: 1) the "
        "continuation of the صفة الجمع paragraph (expected: ثم أقيمت الصلاة فصلى المغرب ثم خات كل إنسان "
        "بعيره في منزله ثم أقيمت العشاء فصلاها ولم يصل بينهما شيئا وهذا الجمع عند المالكية لا يعدل "
        "معناه؟ — transcribe exactly); 2) the green sub-line 3- الأذان والإقامة للعشاءين بمزدلفة and its "
        "FULL paragraph (expected: ظاهر حديث أسامة بن زيد السابق أنه لم يؤذن لهما لأنه اقتصر على الإقامة؟ "
        "وفي البخاري والنسائي عن ابن مسعود أنه أتى المزدلفة فأمر رجلا فأذن ثم أقام؟ ثم صلى المغرب ثم أمر "
        "فأذن وأقام ثم صلى العشاء ركعتين فذكر الحديث وقال في آخره: رأيت به يفعل؟ ومشروعية الأذان والإقامة "
        "لهما وبه أخذ مالك واختاره البخاري) — transcribe EVERY line exactly; 3) the green sub-line 4- "
        "النزول بمزدلفة and its FULL paragraph (expected: النزول بمزدلفة واجب بقدر حط الرحال فإن لم ينزل "
        "على الدم فعليه الأشهر؟ أما البقية فسنة ويسن إحياء هذه الليلة بالعبادة ويصلي بها؟ أول وقت الصبح "
        "ثم يقف بالمشعر الحرام مستقبل القبلة والمشعر الحرام عن يساره يكبر ويدعو إلى الإسفار؟ ثم يلتقط "
        "سبع حصيات لجمرة العقبة من مزدلفة ثم يدفع إلى منى) — transcribe EVERY line exactly; 4) the "
        "رخصة paragraph (expected: ويُرخص للنساء والصبيان وذوي الأعذار في ترك المبيت بالمزدلفة خوف "
        "التأذي بالعظة والزحامة؟ وقد روى؟ ... أن عبد الله بن عمر كان يُمدي أهله و صبيانه إلى المزدلفة "
        "حتى متى؟ يصلون؟) — transcribe exactly; 5) the two Muwaṭṭa athar quotes: عن عطاء بن أبي رباح "
        "(expected: قل نو؟ أن أي الناسن؟ أصبح؟ بمنى [الموطأ رقم: NNN digit by digit]) and أن أسماء مولة "
        "أتبي بكر أخبرته بنت أبي بكر أنها قالت: خرجنا مع أسماء بنت أبي بكر قنا؟ مستبلة؟ فقالت: قال قذ؟ "
        "تشتضت ذلك مع من هو خير مذك؟ فقالت: قال قذ؟ وضعتها؟ قد جنا منى غسل؟ and the third quote (expected: "
        "وعن مالك أنه أن طلحة بن عبيد الله كان يقدم نساءه وصبيانه [الموطأ رقم: NNN — 1161؟] و [الموطأ "
        "رقم: NNN — 1162؟] من المزدلفة إلى منى) — read BOTH numbers DIGIT BY DIGIT. Mark illegible as [؟]. "
        "Short French notes at the end."
    ),
    "r670-p102-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the rubric استخلاص المضامين (or تقويم) with EVERY numbered item EXACTLY "
        "(expected: 1- كيف كان يسير إلى مزدلفة؟ 2- أبين صفة الجمع بين العشاءين بمزدلفة 3- أبين حكم "
        "المسألتين الآتيتين مع الاستدلال والتعليل) and the TWO cases: (a) حاج دفع من عرفة إلى مزدلفة وهو "
        "على يقين بأن وصوله سيكون بعد العشاء فصلى المغرب في الطريق — transcribe exactly; (b) حاج دفع من "
        "عرفة إلى منى دون النزول بمزدلفة — transcribe exactly; 2) the two quoted texts for item 3: FIRST "
        "قال مالك: «...» — transcribe EVERY word (expected: الله شرِك اكتار؟ لا دوي؟) — this is a "
        "MALIK QUOTE on الرفث والفسوق والجدال with the Quranic citation [سورة البقرة الآية: NNN] — read "
        "the verse number DIGIT BY DIGIT (196?) and the SECOND Quranic citation [سورة الحج الآية: NNN] — "
        "read DIGIT BY DIGIT (56? 30?) with the full quoted text (فهدا فيما الجدال أغمُ؟ وقد؟) — "
        "transcribe every legible word; 3) the tafsīr paragraph (expected: كانت العرب قريشا تقف عند "
        "المشعر الحرام بالمزدلفة وغيرهم يقفون بعرفة فكأنهم يتجادلون؟ فيمًا...) — transcribe every legible "
        "line; 4) the last quote (expected: سُرس سات لكلٍ من؟ أي هو لاء؟ هو هؤلاء ويقول سُر؟) and the "
        "closing [الموطأ رقم: NNN] with number DIGIT BY DIGIT (1154?) and the fragment من ذلك 13سمغت؟ — "
        "transcribe what is legible. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r670-p103-full": (
        "Full Arabic schoolbook page (300 dpi, short page). Transcribe ALL Arabic lines EXACTLY, "
        "right-to-left, in reading order: 1) the evaluation line أتأمل النص وأقارن معنى الرفث والفسوق "
        "والجدال في الحج بما ورد عند المالكية من خلال كتب الأحكام — transcribe exactly; 2) the rubric "
        "الإعداد القبلي (expected: أحفظ أحاديث الدرس المقبل وأجيب عن الآتي) with EVERY numbered item "
        "(expected: 1- أبحث عن حكم الصيام أيام منى 2- أبحث عن صفة التكبير أيام منى 3- أبحث عن حكم قصر "
        "الصلاة بمنى) — digits digit-by-digit; 3) any other line present (page number, decorations). Mark "
        "illegible as [؟]. Short French notes at the end."
    ),
}

IMG = {
    "r670-p97-full": "p-097.png",
    "r670-p98-full": "p-098.png",
    "r670-p99-full": "p-099.png",
    "r670-p100-full": "p-100.png",
    "r670-p101-full": "p-101.png",
    "r670-p102-full": "p-102.png",
    "r670-p103-full": "p-103.png",
}


def run(name):
    out = os.path.join(DIR, f"_r670-read-{name}.json")
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
