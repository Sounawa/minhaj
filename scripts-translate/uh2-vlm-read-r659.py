# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM pleine page R659 (slot pdf-mut23h2u-277, leçon 23
المصحف والمحرف). Mécanique uh2-vlm-read-278.py (R658) : couche texte recoupée
par rendus 300 dpi (tr-tmp/qa-crops-r659/), chaque lecture = cache
tr-tmp/qa-crops-r659/_r659-read-<name>.json — toute récusation de la couche
texte est documentée (nom d'image, ce qui a été lu), jamais devinée. Moteur :
CLI z-ai vision (SDK VLM), prompts ciblés par page."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r659"

PROMPTS = {
    "r659-p120-full": (
        "Full Arabic schoolbook page (300 dpi), lesson 23 opening. Transcribe ALL Arabic lines EXACTLY, "
        "right-to-left, in reading order, from the top: 1) green banner + medallion (read the lesson number "
        "digit-by-digit; expected ٢٣) and expected title المصحف والمحرف — transcribe the printed title exactly; "
        "2) the rubric أهداف الدرس with EVERY numbered objective (expected four, text layer suggests: أن أتعرف "
        "مفهومي المصحف والمحرف / a second garbled objective — transcribe it exactly from the image / أن أجتنب "
        "التصحيف والتحريف في الكتابة والنقل / أن أتخلق بخلق الأمانة وقيم الصدق في تحصيل العلم وتبليغه) — "
        "transcribe each exactly; 3) the tamhid paragraph beginning بذل علماء الحديث جهودا لحفظ الأحاديث النبوية "
        "وصونها من التبديل والتغيير — transcribe to its final question, including the exact word naming the "
        "classification (text layer suggests اسما خادعا or اسما خاصا or اسما خاضا — read letter by letter) and "
        "the three closing questions (فماذا يسمى النوع الأول؟ وماذا يسمى النوع الثاني؟ وما فائدة معرفة كل منهما؟) "
        "— transcribe exactly; 4) the boxed matn of Ibn Hajar (the text layer is garbled there: «... أو بتغيير م "
        "بقاء الساق» is NOT trustworthy) — transcribe the WHOLE boxed matn EXACTLY letter by letter, noting it "
        "begins with an ellipsis and a bracket, and read every word digit and dot; 5) the rubric الفهم / الشرح "
        "with the three glosses (أو بتغيير / المصحف / السّياق) and استخلاص المضامين with its numbered items — "
        "transcribe each exactly. Mark [؟] where unclear. Short French notes at the end."
    ),
    "r659-p121-full": (
        "Full Arabic schoolbook page (300 dpi), lesson 23 part أولا: الحديث المصحف. Transcribe ALL Arabic lines "
        "EXACTLY, right-to-left, in reading order: 1) the rubric أولا: الحديث المصحف then item 1. تعريفه with "
        "sub-items أ (لغة: اسم مفعول من التصحيف، والتصحيف: الخطأ في الصحيفة — transcribe the bracketed reference "
        "EXACTLY and read its page number DIGIT BY DIGIT; text layer suggests [القاموس المحيط، الفيروزآبادي، ص "
        "628] or 826) and ب (اصطلاحا: ما كانت المخالفة فيه بتغيير حرف أو حروف مع بقاء صورة الخط) — transcribe "
        "exactly; 2) item 2. أهمية معرفة المصحف with the quote of Ibn al-Salah (expected قال ابن الصلاح: «هذا "
        "فن جليل إنما ينهض بأعبائه الحذاق من الحفاظ، والدارقطني منهم، وله فيه تصنيف مفيد») — transcribe EXACTLY "
        "and read the bracketed reference DIGIT BY DIGIT (text layer suggests [مقدمة ابن الصلاح، ص 384] or 483); "
        "3) item 3. أقسامه: قسم العلماء المصحف إلى ثلاثة تقسيمات، كل تقسيم باعتبار (transcribe exactly) then "
        "sub-item أ- باعتبار موقعه، وينقسم بهذا الاعتبار إلى قسمين، وهما: — then the example of تصحيف في "
        "الإسناد: transcribe the chain AND matn of the Uthman ibn Affan hadith EXACTLY letter by letter with "
        "its vocalisation (expected: عن الحَوامِّ بن ...، عن أبي عثمان النهدي، عن عثمان بن عفان قال: قال رسول "
        "الله صلى الله عليه وسلم: «لَتُوَدَّنَّ الحقوق إِلَى أهلها حتّى يُقَصّ للشاة الْجَمّاء منَ الشاة "
        "القَرْنَاء») — read the bracketed reference DIGIT BY DIGIT (text layer suggests [علل الدارقطني، حديث "
        "782] or 287); then the sentence about يحيى بن معين correcting the name (expected: صحف فيه يحيى بن "
        "معين فقال «ابن مزاحم» بالزاي، وإنما هو «ابن مراجم» بالراء المهملة والجيم) with its reference DIGIT BY "
        "DIGIT (text layer suggests [مقدمة ابن الصلاح، ص 384]); 4) the example of تصحيف في المتن: transcribe "
        "the chain (expected: ما رواه الليث عن كتاب موسى بن عقبة إليه بإسناده عن زيد بن ثابت) and the matn "
        "EXACTLY (expected: «أن رسول الله صلى الله عليه وسلم احتجم في السجدة» وإنما هو بالراء؛ كما هو في "
        "الصحيح عند مسلم: «احتجر رسول الله صلى الله عليه وسلم في حجيرة بخصفة» أو حصير) with the bracketed "
        "source EXACTLY (expected [صحيح مسلم، كتاب صلاة المسافرين، باب استحباب صلاة النافلة في بيته وجوازها "
        "في المسجد]) and the sentence فصحفه ابن لهيعة لكونه أخذه من كتاب بغير سماع with its reference DIGIT "
        "BY DIGIT (text layer suggests [مقدمة ابن الصلاح، ص 385]), and the gloss ومعنى «احتجر»: اتخذ شبه "
        "الحجرة; 5) the beginning of sub-item ب- باعتبار منشئه: وينقسم بهذا الاعتبار إلى قسمين، وهما: — "
        "transcribe exactly. Mark [؟] where unclear. Short French notes at the end."
    ),
    "r659-p122-full": (
        "Full Arabic schoolbook page (300 dpi), lesson 23 continuation. Transcribe ALL Arabic lines EXACTLY, "
        "right-to-left, in reading order: 1) the item تصحيف البصر: «وهو الأكثر» أي يشتبه الخط على بصر القارئ "
        "إما لرداءة الخط، أو عدم نقطه — transcribe exactly; 2) its example: transcribe the hadith EXACTLY with "
        "vocalisation (expected: «مَنْ صَامَ رَمَضَانَ وَأَتْبَعَهُ ستا مِنْ شَوَّال فَكَأنَمَا صَامَ "
        "الدَّهْرَ») and the bracketed source EXACTLY word by word (expected [صحيح مسلم، كتاب الصيام، باب "
        "استحباب صوم ستة أيام من شوال إتباعا لرمضان]) then the sentence صحفه أبو بكر الصولي فقال: «من صام "
        "رمضان وأتبعه شيئا من شوال...» فصحف «ستا» إلى «شيئا» كما ذكر ذلك ابن الصلاح وغيره — transcribe exactly "
        "and read its reference DIGIT BY DIGIT (text layer suggests [مقدمة ابن الصلاح، ص 389]); 3) تصحيف "
        "السمع: وقد يكون سببه ضعف السمع، أو بُعده، أو غير ذلك، فتشتبه عليه بعض الكلمات — transcribe exactly; "
        "4) its example: نحو حديث لعاصم الأحول رواه بعضهم فقال: «عن واضل الأحذب» — transcribe the two names "
        "LETTER BY LETTER, then the sentence فذكر إلى أن ذلك مما —والله أعلم— قال الدارقطني أنه من تصحيف "
        "السمع لا من تصحيف البصر، كأنه ذهب إلى أن ذلك مما لا يشتبه من حيث الكتابة وإنما أخطأ فيه سمع من رواه "
        "(transcribe exactly, respecting the order of قال الدارقطني and the sentence structure) with its "
        "reference DIGIT BY DIGIT (text layer suggests [مقدمة ابن الصلاح، ص 389]); 5) sub-item ج- باعتبار "
        "لفظه أو معناه: وينقسم باعتبار لفظه أو معناه إلى قسمين، وهما: — then تصحيف في اللفظ: «وهو الأكثر» "
        "وذلك كالأمثلة السابقة — transcribe exactly; 6) تصحيف في المعنى: بحيث يبقي الراوي المصحف اللفظ على "
        "حاله، لكن يفسره تفسيرا يدل على أنه فهم معناه فهم غير مراد — transcribe exactly; 7) its example: "
        "ومثاله: قول أبي موسى (read the LAST NAME of this narrator letter by letter: العنزي or الأشعري or "
        "other — the text layer is unreliable): «نحن قوم لنا شرف نحن من عنزة، صلى إلينا رسول الله ﷺ» يريد "
        "بذلك حديث «أن النبي ﷺ صلى إلى عنزة» — transcribe exactly; 8) the bracketed source of the Musnad "
        "reference (expected [المسند أحمد بن حنبل؛ حديث NNNNN]) — read the hadith number DIGIT BY DIGIT (text "
        "layer suggests 16781 or 18761); 9) the closing sentence فتوهم أنه صلى إلى قبيلتهم، وإنما العَنَزة هنا "
        "الحربة تنصب بين يدي المصلى — transcribe exactly with its reference DIGIT BY DIGIT (text layer suggests "
        "[مقدمة ابن الصلاح، ص 387] or 783); 10) the rubric ثانيا: الحديث المحرف then item 1. تعريفه sub-item "
        "أ- لغة: اسم مفعول من التحريف وهو التغيير، وتحريف الكلام: عدله عن جهته — transcribe exactly with the "
        "bracketed reference EXACTLY (expected [مقاييس اللغة، ابن فارس، 2/34] — read the volume and page DIGIT "
        "BY DIGIT, layer suggests 2/34 or 2/43). Mark [؟] where unclear. Short French notes at the end."
    ),
    "r659-p123-full": (
        "Full Arabic schoolbook page (300 dpi), lesson 23 continuation (المحرف). Transcribe ALL Arabic lines "
        "EXACTLY, right-to-left, in reading order: 1) sub-item ب- اصطلاحا: المحرف: عرفه ابن حجر بأنه ما كان "
        "التغيير فيه بالنسبة إلى شكل الحروف، مع بقاء صورة الخط — transcribe EXACTLY including any bracketed "
        "reference (the text layer shows a stray 53 — read ANY blue bracket on this line DIGIT BY DIGIT and "
        "give its full content, e.g. [النخبة في مصطلح أهل الأثر...] or [شرح النخبة، ص 53] — transcribe whatever "
        "is really printed); 2) the example: ومثاله حديث جابر رضي الله عنه — transcribe the hadith EXACTLY "
        "letter by letter WITH vocalisation (text layer garbled: «رميّ أَبَيْ يَوْمَ الأخرَاب عَلَى أكحّله...» "
        "is NOT trustworthy — expected something like «رمَى أَبِي يَوْمَ الأَخْرَبَ عَلَى الأَكَحْل...» — read "
        "the REAL printed words); 3) the bracketed source EXACTLY (expected [صحيح مسلم، كتاب السلام، باب لكل "
        "داء دواء واستحباب التداوي]) — transcribe word by word; 4) the sentence حرفه غندر وقال فيه: «أبي» "
        "وإنما هو «أبّي بن كعب»... — transcribe the WHOLE correction sentence EXACTLY (it concerns غندر who "
        "changed the name, and a companion killed before — read every word; the text layer suggests وأدركه/وقد "
        "استشهد قل ذلك يومًا واحدًا — give the exact printed form); 5) the reference of this passage DIGIT BY "
        "DIGIT (text layer suggests [مقدمة ابن الصلاح، ص 385]); 6) the gloss والأكحل: عرق في اليد في وسط "
        "الذراع — transcribe exactly; 7) item 2. الفرق بين المصحف والمحرف — transcribe the WHOLE paragraph "
        "exactly (expected: الصحف يكون التغيير فيه بتغيير حرف أو حروف مع بقاء صورة الخط، والمحرف يكون التغيير "
        "فيه بالنسبة إلى شكل الحروف مع بقاء صورة الخط، وكلاهما يجمعهما التغيير ويختلفان في نوعه); 8) item 3. "
        "حكم التصحيف والتحريف — transcribe the WHOLE paragraph exactly (expected: إذا وقع التصحيف أو التحريف "
        "من الراوي نادرا فإنه لا يقدح في ضبطه؛ لأن الخطأ اليسير لا يسلم منه أحد، وإذا كثر التصحيف منه قدح في "
        "ضبطه، فيكون الراوي خفيف الضبط، والقدر الصحف أو المحرف مردود؛ لوروده على غير أصله); 9) the rubric "
        "أهتدي وأقتدي with the quote of Yahya ibn Ma'in (expected قال يحيى بن معين رحمه الله: «آلة المحدث "
        "الصدق») — transcribe EXACTLY and read the bracketed reference DIGIT BY DIGIT (text layer suggests "
        "[التمييد، 1/70]); 10) the rubric التقويم with EVERY numbered item — transcribe each exactly (item 3 "
        "text layer garbled: أنطلق من كلام يحيى بن معين ... — read the full item 3 exactly). Mark [؟] where "
        "unclear. Short French notes at the end."
    ),
    "r659-p124-full": (
        "Full Arabic schoolbook page (300 dpi), lesson 23 closing page. Transcribe ALL Arabic lines EXACTLY, "
        "right-to-left, in reading order: 1) the green rubric at the top — read its name LETTER BY LETTER (the "
        "text layer suggests الاستتمار or الاستثمار — decide from the image; R658 read the same rubric on "
        "p.128 as الاستثمار) — transcribe the rubric name exactly; 2) the quote of Imam Ibn al-Salah: «وأما "
        "التصحيف فسبيل السلامة منه الأخذ من أفواه أهل العلم والضبط، فإن من حرم ذلك ...» — transcribe the WHOLE "
        "quote EXACTLY letter by letter to its final word (the middle is garbled in the text layer — expected "
        "something like فإن من حرم ذلك عُرَّض لأخطاء الكتّاب إلى التحريف، ولم يفلت من التبديل والتصحيف — read "
        "the REAL printed words) and read the bracketed reference DIGIT BY DIGIT (text layer suggests [مقدمة "
        "ابن الصلاح، ص 218] or 812); 3) the extraction sentence أستخلص من النص أهمية التحلي بقيمة الصبر لتلقي "
        "العلم من أفواه الرجال وأثر ذلك في الضبط والإتقان — transcribe exactly; 4) the rubric الاعداد القبلي "
        "with EVERY numbered item — transcribe each exactly (expected two: 1. أعد بحثا مركزا عن مذهب الإمام "
        "مالك في حكم رواية الحديث بالمعنى. 2. أبحث عن الفروق بين رواية الحديث باللفظ وروايته بالمعنى، وما "
        "يترتب على ذلك.) — read leading digits digit-by-digit, state how many items there really are. Mark [؟] "
        "where unclear. Short French notes at the end."
    ),
}

IMG = {
    "r659-p120-full": "p120-full.png",
    "r659-p121-full": "p121-full.png",
    "r659-p122-full": "p122-full.png",
    "r659-p123-full": "p123-full.png",
    "r659-p124-full": "p124-full.png",
}


def run(name):
    out = os.path.join(DIR, f"_r659-read-{name}.json")
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
