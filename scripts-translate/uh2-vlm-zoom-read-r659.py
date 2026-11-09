# -*- coding: utf-8 -*-
"""Minhāj — Re-lectures VLM des zooms 900 dpi R659 (slot pdf-mut23h2u-277,
leçon 23 المصحف والمحرف). Patron uh2-vlm-zoom-read-278.py (R658). Chaque
lecture = cache tr-tmp/qa-crops-r659/_r659-zoom-<name>.json — adjudication
par preuve image, jamais devinée."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r659"

PROMPTS = {
    "z900-p120-objectifs": (
        "Zoom 900 dpi of a green banner zone of an Arabic schoolbook page. Transcribe EXACTLY: 1) the lesson "
        "number inside the round medallion DIGIT BY DIGIT; 2) the printed lesson title; 3) the rubric أهداف "
        "الدرس with its FOUR numbered objectives, letter by letter (candidate readings for objective 2: أن "
        "أميز بين المصحف والمحرف — confirm or give the real printed words; objective 1 expected أن أتعرف "
        "مفهومي المصحف والمحرف; objective 3 expected أن أجتنب التصحيف والتحريف في الكتابة والنقل; objective 4 "
        "expected أن أتخلق بخلق الأمانة وقيم الصدق في تحصيل العلم وتبليغه). Mark [؟] where unclear."
    ),
    "z900-p120-tamhid": (
        "Zoom 900 dpi of the tamhid paragraph of an Arabic schoolbook page. Transcribe EVERY word EXACTLY letter "
        "by letter: it begins بذل علماء الحديث جهودا لحفظ الأحاديث النبوية وصونها من التبديل والتغيير — then "
        "decide letter-by-letter: (a) the verb after that: وبينوا or ويبنيونا? (b) the noun: المخالفة or "
        "الخلافَة? (c) the closing classification: وأطلقوا على كل منهما اسما خاصا — read the word after اسما "
        "LETTER BY LETTER (candidates: خاصا or خاضا or خادعا) — and (d) the exact bracket/ellipsis punctuation "
        "at the paragraph start, plus the three closing questions فماذا يسمى النوع الأول؟ وماذا يسمى النوع "
        "الثاني؟ وما فائدة معرفة كل منهما؟ Mark [؟] where unclear."
    ),
    "z900-p120-matn": (
        "Zoom 900 dpi of the boxed matn (النص) of an Arabic schoolbook page. Transcribe the WHOLE box EXACTLY "
        "letter by letter WITH vocalisation: it starts with قال الحافظ ابن حجر رحمه الله: «... — the expected "
        "content is ... أو بتغيير مع بقاء السياق: فالمصحف والمحرف» — verify letter by letter: (a) is the word "
        "السِّياق (with شين) or الساق or شيء else? (b) is there a colon after السياق? (c) the final words "
        "فالمصحف والمحرف exactly. Give the exact printed punctuation (ellipsis, brackets). Mark [؟] where unclear."
    ),
    "z900-p120-sharh-istikhlas": (
        "Zoom 900 dpi of the bottom block of an Arabic schoolbook page with two green rubrics الشرح and استخلاص "
        "المضامين. Transcribe EVERY line EXACTLY: under الشرح there should be glosses (expected: أو بتغيير: أو "
        "إن كانت المخالفة بتغيير حرف أو حروف مع بقاء صورة الخط... AND السِّياق: أي سياق اللفظ، والسياق يقصد به: "
        "القرينة الدالة على المقصود) — read every gloss in full including any continuation (does the first gloss "
        "end with مع بقاء صورة الخط only, or مع بقاء صورة الخط واللحرف?); under استخلاص المضامين transcribe the "
        "numbered items EXACTLY (candidate: أستخلص من المتن تعريف المصحف — is there more text, e.g. والمحرف or "
        "مع بقاء صورة الخط? How many items exactly?). Mark [؟] where unclear."
    ),
    "z900-p121-def-refs": (
        "Zoom 900 dpi of the top of an Arabic schoolbook page. Transcribe EXACTLY: 1) the green rubric أولا: "
        "الحديث المصحف; 2) 1. تعريفه: أ- لغة: اسم مفعول من التصحيف، والتصحيف: «الخطأ في الصحيفة» followed by a "
        "bracketed reference — transcribe the bracket CONTENT WORD BY WORD and read its page number DIGIT BY "
        "DIGIT (candidates [القاموس المحيط، الفيروزآبادي، ص 826] vs ص 628 — decide from the glyphs, leftmost "
        "digit first); 3) ب- اصطلاحا: ما كانت المخالفة فيه بتغيير حرف أو حروف، مع بقاء صورة الخط. Mark [؟] where unclear."
    ),
    "z900-p121-isnad": (
        "Zoom 900 dpi of the middle of an Arabic schoolbook page (example of تصحيف في الإسناد). Transcribe "
        "EXACTLY: 1) the line أعلى: أهمية معرفة المصحف continuation if visible; 2) the numbered heading 3. "
        "أقسامه: قسم العلماء المصحف إلى ثلاثة تقسيمات، كل تقسيم باعتبار: (verify the word before التقسيمات: "
        "ثلاثة?) and sub-item أ- باعتبار موقعه، وينقسم بهذا الاعتبار إلى قسمين، وهما:; 3) the example line "
        "تصحيف في الإسناد: ومثاله: عن ... — transcribe the chain NAMES LETTER BY LETTER (candidates for the "
        "first narrator: شعبة? العوام بن مراجم? الحوام بن ...? — give exactly what is printed); 4) the hadith "
        "matn with vocalisation «لَتُوَدَّنَّ الحقوق إِلَى أهلها حتّى يُقَصّ للشاة الْجَمّاء منَ الشاة "
        "القَرْنَاء»; 5) the bracketed reference — read its page/hadith number DIGIT BY DIGIT (candidates: "
        "[علل الدارقطني، حديث 782] vs حديث 287); 6) the correction sentence صحف فيه يحيى بن معين فقال: «ابن "
        "مزاحم» ... وإنما هو: «ابن مراجم» — transcribe the WHOLE sentence exactly (is there a word like فرد "
        "عليه or بالزاي والحاء? give the exact printed form) and its bracketed reference DIGIT BY DIGIT "
        "(candidates ص 384 vs 483). Mark [؟] where unclear."
    ),
    "z900-p121-matan-muslim": (
        "Zoom 900 dpi of an Arabic schoolbook page (example of تصحيف في المتن). Transcribe EXACTLY: 1) the "
        "heading line تصحيف في المتن، ومثاله: ما رواه ... عن كتاب موسى بن عقبة ... عن زيد بن ثابت — transcribe "
        "the chain LETTER BY LETTER (candidates: الليث عن كتاب موسى بن عقبة بناه بإسناده vs ابن لهيعة — decide "
        "from the glyphs; give every word including بناه/إليه بإسناده); 2) the matn «أن رسول الله ﷺ احتجم في "
        "السجدة» وإنما هو بالراء؛ كما هو في الصحيح عند مسلم: «احتجر رسول الله ﷺ في حجيرة بخصفة» أو حصير — "
        "transcribe letter by letter (candidates احتجم/احتم/احتجر and السجدة/حجيرة); 3) the bracketed source "
        "WORD BY WORD (candidates [صحيح مسلم، كتاب صلاة المسافرين، باب استحباب صلاة النافلة في بيته وجوازها في "
        "المسجد] vs كتاب صلاة المسافر وقصرها — decide from the glyphs); 4) the sentence فصحفه ابن لهيعة لكونه "
        "أخذه من كتاب بغير سماع with its bracketed reference DIGIT BY DIGIT (candidates ص 385 vs 583); 5) the "
        "gloss ومعنى «احتجر»: اتخذ شبه الحجرة. Mark [؟] where unclear."
    ),
    "z900-p122-sam-names": (
        "Zoom 900 dpi of an Arabic schoolbook page (example of تصحيف السمع). Transcribe EXACTLY letter by "
        "letter: 1) تصحيف السمع: وقد يكون سببه ضعف السمع، أو بُعده، أو غير ذلك، فتشتبه عليه بعض الكلمات؛ 2) "
        "نحو حديث لعاصم الأحول رواه بعضهم فقال: «عن ...» — transcribe the corrupted name LETTER BY LETTER "
        "(candidates: واضل الأحذب vs واصل الأحدب vs واضح الأحدب — decide from the glyph dots: does the first "
        "word end with صل or ضل or ضح? does the second word have ذ or د?); 3) then the sentence with فذكر "
        "الدارقطني — transcribe the WHOLE sentence exactly and give the EXACT position of والله أعلم (is it "
        "فذكر — والله أعلم — الدارقطني، or فذكر الدارقطني ... كأنه ذهب — والله أعلم — إلى أن...?); 4) its "
        "bracketed reference DIGIT BY DIGIT (candidates ص 389 vs 983). Mark [؟] where unclear."
    ),
    "z900-p122-musnad": (
        "Zoom 900 dpi of an Arabic schoolbook page (example of تصحيف في المعنى). Transcribe EXACTLY: 1) ج- "
        "باعتبار لفظه أو معناه وينقسم باعتبار لفظه أو معناه إلى قسمين، وهما:; 2) تصحيف في اللفظ: «وهو الأكثر» "
        "وذلك كالأمثلة السابقة؛ 3) تصحيف في المعنى: بحيث يبقي الراوي المصحف اللفظ على حاله، لكن يفسره تفسيرا "
        "يدل على أنه فهم معناه فهم غير مراد (verify the first word: بحيث or حيث?); 4) ومثاله: قول أبي موسى "
        "العَنَزي — read the narrator's LAST NAME letter by letter (العنزي with ʿayn-nūn-zāy?); 5) the quote "
        "«نحن قوم لنا شرف نحن من عنزة، صلى إلينا رسول الله ﷺ» يريد بذلك حديث «أن النبي ﷺ صلى إلى عنزة»; 6) "
        "the bracketed reference [المسند أحمد بن حنبل؛ حديث NNNNN] — read the hadith number DIGIT BY DIGIT "
        "(candidates 18761 vs 16781); 7) فتوهم أنه صلى إلى قبيلتهم، وإنما العَنَزة هنا الحربة تنصب بين يدي "
        "المصلى with its bracketed reference DIGIT BY DIGIT (candidates ص 387 vs 783). Mark [؟] where unclear."
    ),
    "z900-p122-luga-ref": (
        "Zoom 900 dpi of the bottom of an Arabic schoolbook page. Transcribe EXACTLY: 1) the green rubric "
        "ثانيا: الحديث المحرف; 2) 1. تعريفه: أ- لغة: اسم مفعول من التحريف، وهو التغيير، «وتحريف الكلام: عدله "
        "عن جهته» followed by the bracketed reference — transcribe it WORD BY WORD and read the volume and "
        "page DIGIT BY DIGIT (candidates [مقاييس اللغة، ابن فارس، 2/43] vs 2/34 — decide from the glyphs). "
        "Mark [؟] where unclear."
    ),
    "z900-p123-top": (
        "Zoom 900 dpi of the top of an Arabic schoolbook page. Transcribe EXACTLY: ب- اصطلاحا: المحرف: عرفه "
        "ابن حجر بأنه ما كان التغيير فيه بالنسبة إلى شكل الحروف، مع بقاء صورة الخط — AND check whether ANY "
        "bracketed blue reference follows (candidates: [النخبة، ص 53]? [شرح النخبة، ص 53]? nothing?) — if a "
        "bracket or digits exist anywhere on this line or the next, transcribe them DIGIT BY DIGIT; if none, "
        "state clearly 'no bracket'. Mark [؟] where unclear."
    ),
    "z900-p123-jabir": (
        "Zoom 900 dpi of an Arabic schoolbook page (example of المحرف, hadith of Jabir). Transcribe EXACTLY "
        "letter by letter WITH vocalisation: 1) ومثاله حديث جابر رضي الله عنه: «رُمِيَّ أَبِي يَوْمَ "
        "الأَخْرَبِ عَلَى الأَكَحْلِ ... رَسُولُ اللهِ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ» — read the words "
        "after الأَكَحْلِ EXACTLY (candidates: فَكَأَنَّهُ فكأنه / فَكَأَه — decide glyph by glyph; also the "
        "exact first word: رُمِيَّ or رُمِيَ or رُميّ? and أَبِي or أَبَيْ?); 2) the bracketed source WORD BY "
        "WORD (expected [صحيح مسلم، كتاب السلام، باب لكل داء دواء واستحباب التداوي]); 3) حرفه غندر وقال فيه: "
        "«أبي» وإنما هو «أبّي بن كعب»، وأبو جابر كان قد استُشهد قبل ذلك بأَحُد/بأُحُد/بأحد — transcribe the "
        "WHOLE correction sentence exactly, letter by letter (what exactly is printed after قبل ذلك? one word? "
        "أَحُد? يَوْمًا وَاحِدًا? أَحَدَ?); 4) the bracketed reference DIGIT BY DIGIT (candidates [مقدمة ابن "
        "الصلاح، ص 385] vs 583); 5) the gloss والأكحل: عرق في اليد في وسط الذراع. Mark [؟] where unclear."
    ),
    "z900-p123-hukm-end": (
        "Zoom 900 dpi of an Arabic schoolbook page (item 2 الفرق بين المصحف والمحرف + item 3 حكم التصحيف "
        "والتحريف). Transcribe EXACTLY: 1) 2. الفرق بين المصحف والمحرف: الصحف يكون التغيير فيه بتغيير حرف أو "
        "حروف مع بقاء صورة الخط، والمحرف يكون التغيير فيه بالنسبة إلى شكل الحروف مع بقاء صورة الخط، وكلاهما "
        "يجمعهما التغيير ويختلفان في نوعه — verify EVERY word (esp. يختلفان في نوعه); 2) 3. حكم التصحيف "
        "والتحريف: إذا وقع التصحيف أو التحريف من الراوي نادرا فإنه لا يقدح في ضبطه؛ لأن الخطأ اليسير لا يسلم "
        "منه أحد، وإذا كثر التصحيف منه قدح في ضبطه، فيكون الراوي خفيف الضبط، والقدر ... — transcribe the "
        "ENDING of this paragraph EXACTLY (candidates: والقدر الصحف أو المحرف مردود؛ لوروده على غير أصله vs "
        "other — give the exact printed words after فيكون الراوي خفيف الضبط). Mark [؟] where unclear."
    ),
    "z900-p123-ahtadi-taqwim": (
        "Zoom 900 dpi of the bottom of an Arabic schoolbook page (rubrics أهتدي وأقتدي and التقويم). Transcribe "
        "EXACTLY: 1) أهتدي وأقتدي: قال يحيى بن معين رحمه الله: «آلة المحدث الصدق» — read the quote letter by "
        "letter (آلة المحدِّث الصِّدْق? any extra word?) and the bracketed reference DIGIT BY DIGIT (candidates "
        "[التمييد، 1/70] vs 1/07 — also the book name letter by letter التمييد? التمهيد?); 2) التقويم with its "
        "numbered items — transcribe each EXACTLY (item 1 أذكر أنواع التصحيف; item 2 candidates: أبين الفرق "
        "بين تصحيف السمع وتصحيف البصر vs أبين الفرق بين تصحيف الاسم وتصحيف البصر — decide letter by letter "
        "(سمع with م? اسم?); item 3 candidates: أنطلق من كلام يحيى بن معين، وان... vs أنظر من كلام يحيى بن "
        "معين... — transcribe the WHOLE item 3 exactly letter by letter). Mark [؟] where unclear."
    ),
    "z900-p124-quote": (
        "Zoom 900 dpi of the top of an Arabic schoolbook page. Transcribe EXACTLY: 1) the green rubric name — "
        "letter by letter (الاستثمار with ث? or الاستتمار with ت? decide by the DOT); 2) قال الإمام ابن الصلاح "
        "رحمه الله: «وأما التصحيف فسبيل السلامة منه الأخذ من أفواه أهل العلم، والضبط، فإن من حرم ذلك، وكان "
        "أخذه وتعلمه من بطون الكتب، كان من شأنه التحريف، ولم يفلت من التبديل، والتصحيف» — transcribe the "
        "WHOLE quote EXACTLY letter by letter, verifying especially the middle (كان أخذه وتعلمه من بطون "
        "الكتب، كان من شأنه التحريف) and the end (ولم يفلت من التبديل، والتصحيف); 3) the bracketed reference "
        "DIGIT BY DIGIT (candidates [مقدمة ابن الصلاح، ص 218] vs 812). Mark [؟] where unclear."
    ),
}

IMG = {
    "z900-p120-objectifs": "z900-p120-objectifs.png",
    "z900-p120-tamhid": "z900-p120-tamhid.png",
    "z900-p120-matn": "z900-p120-matn.png",
    "z900-p120-sharh-istikhlas": "z900-p120-sharh-istikhlas.png",
    "z900-p121-def-refs": "z900-p121-def-refs.png",
    "z900-p121-isnad": "z900-p121-isnad.png",
    "z900-p121-matan-muslim": "z900-p121-matan-muslim.png",
    "z900-p122-sam-names": "z900-p122-sam-names.png",
    "z900-p122-musnad": "z900-p122-musnad.png",
    "z900-p122-luga-ref": "z900-p122-luga-ref.png",
    "z900-p123-top": "z900-p123-top.png",
    "z900-p123-jabir": "z900-p123-jabir.png",
    "z900-p123-hukm-end": "z900-p123-hukm-end.png",
    "z900-p123-ahtadi-taqwim": "z900-p123-ahtadi-taqwim.png",
    "z900-p124-quote": "z900-p124-quote.png",
}


def run(name):
    out = os.path.join(DIR, f"_r659-zoom-{name}.json")
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
