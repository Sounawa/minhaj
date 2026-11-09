# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM zoom R659 (slot pdf-mut23h2u-279) : adjudications
ciblées sur les zones critiques des pages 129-130 (objectifs, أقرأ, organigramme
أطبق, isnad + bracket source, items 1-6, bandeau الإعداد القبلي). Caches
tr-tmp/qa-crops-r659-uh2/_r659-zoom-<name>.json — toute récusation documentée."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r659-uh2"

PROMPTS = {
    "r659-zoom-p129-top": (
        "Zoom on a 300-dpi crop (top of an Arabic schoolbook page): green lesson banner + rubric "
        "أهداف الأنشطة. Transcribe EXACTLY, right-to-left: 1) the banner — medallion number digit by "
        "digit (expected 25) and the banner title (expected أنشطة تطبيقية); 2) EVERY numbered objective "
        "of أهداف الأنشطة, from its number to its final period. Objectives: verify word-by-word whether "
        "objective 1 reads أن أثبت معارفي النظرية السابقة or another form (أثبّت؟ أعتني؟) and whether the "
        "last word is السابقة alone or السابقة plus more words; whether objective 2 reads أن أنمي مهاراتي "
        "النظرية في البحث التطبيقي العملي or أن أنمي مهاراتي في البحث التطبيقي العملي or another form; "
        "whether objective 3 reads أن أدرك الغاية من ضبط المصطلحات الحديثة وأهمية ذلك في مجال التطبيقات "
        "(verify المصطلحات الحديثة vs الحديثة المستصلحة؟ and كل التطبيقات? مجال التطبيقات?); whether "
        "objective 4 reads أن أتمرن على دراسة الأحاديث دراسة تطبيقية عملية. Mark [؟] where unclear. "
        "Short French notes at the end."
    ),
    "r659-zoom-p129-aqra": (
        "Zoom on a 300-dpi crop (middle of an Arabic schoolbook page): the rubric أقرأ and its TWO "
        "paragraphs. Transcribe BOTH paragraphs EXACTLY, word by word, right-to-left. Verify these "
        "suspicious spots: paragraph 1 first word (عرّفت? ناقشنا?), the phrase بعد «جملة من» (المعارف "
        "الأساسية؟ المعارف الأساسية؟), the phrase «تعين طالب الحديث على» followed by (التوصل؟ التوصصل؟ "
        "coquille imprimée possible) and «ببحثه الخاص إلى التمييز بين» (الصحيح والضعيف؟) ; paragraph 2: "
        "its first words (وتقريبا؟ ولتقريبا؟ وتقريب؟ للتطبيقات العملية), the phrase (رأينا أن نضع؟) + "
        "(هذه الخطوات الأولية؟) + (التي تعين على الوصول إلى) + (المقصود؟ القصود؟ الأغراض؟) , then "
        "(ويراعى فيها؟ ويراعينا فيها؟) (الاقتصار؟ الاقتصاد؟) (على الضروري والمهم؟), then the closing "
        "sentence (وغرضنا من هذا مباشرة الجانب التطبيقي لهذا العلم وأن تكون هذه التجربة مفتاحا؟ مفتاح؟) "
        "+ (لعناية؟ عناية؟) (بالتطبيقات والتوسع فيها؟). Mark [؟] where unclear. Short French notes."
    ),
    "r659-zoom-p129-flow": (
        "Zoom on a 300-dpi crop (lower half of an Arabic schoolbook page): the rubric أطبق with a "
        "flowchart titled خطوات دراسة وتخريج حديث (steps of study and takhrij of a hadith) — boxes "
        "connected by arrows. Transcribe: 1) the rubric name أطبق exactly; 2) the flowchart title exactly; "
        "3) EVERY box EXACTLY, in order, with its numbering style (أولا/ثانيا/ثالثا/رابعا/خامسا or 1/2/3/"
        "4/5). Verify: box 1 (تقديم الحديث المراد دراسته، واستخراجه من — مصادره؟ مصادر؟ الأصلية? مصادره "
        "الأصلية? مصادرها الأصلية?) ; box 2 (البحث عن طرق الحديث — ورواه؟ ورواته؟) ; box 3 (دراسة سند "
        "الحديث الأصلي) + the parenthetical list (اتصال السند، عدالة الرواة، ضبط الرواة... exactly) ; box 4 "
        "(دراسة طرق الحديث ورواته؟ دراسة طرق ورواه الحديث؟ رابثا؟) ; box 5 (الحكم الكلي على الحديث الأصلي؟ "
        "التحكم الكلي؟) + its parenthetical (بعد دراسة طرقه وشواهده؟). Also transcribe any small side "
        "text. Mark [؟] where unclear. Short French notes at the end."
    ),
    "r659-zoom-p130-isnad": (
        "Zoom on a 300-dpi crop (top of an Arabic schoolbook page): the yellow rubric الحديث المطلوب "
        "تخريجه and the printed hadith with its full chain of transmission and a blue bracketed source. "
        "Transcribe EXACTLY, word by word, line by line: 1) the rubric exactly; 2) the COMPLETE chain: "
        "expected حدثنا أبو هشام الرفاعي، قال: حدثنا يحيى بن اليمان، عن شيخ من بني زهرة، عن الحارث بن "
        "عبد الرحمن بن أبي ذباب، عن طلحة بن عبيد الله، قال: قال النبي صلى الله عليه وسلم: «لكل نبي رفيق "
        "ورفيقي — يعني في الجنة — عثمان» — verify EVERY proper name digit-free: أبو هشام الرفاعي ( Mohamed "
        "بن يزيد? does the book print محمد بن يزيد?) ; يحيى بن اليمان? ; شيخ من بني زهرة (or الزهري?) ; "
        "الحارث بن عبد الرحمن بن أبي ذباب (each word!) ; طلحة بن عبيد الله ; the matn with the parenthetical "
        "(يعني في الجنة — is it printed inline with dashes?) and the final word عثمان ; 3) the blue "
        "bracketed source at the very end: verify EXACTLY — [سنن الترمذي، أبواب ...] : does it read أبواب "
        "المناقب or أبواب الثلثية? and باب في مناقب عثمان بن عفان رضي الله عنه? any hadith number printed? "
        "Mark [؟] where unclear. Short French notes at the end."
    ),
    "r659-zoom-p130-items": (
        "Zoom on a 300-dpi crop (middle of an Arabic schoolbook page): six numbered work items after the "
        "printed hadith (takhrij exercise steps). Transcribe EACH item EXACTLY with its real number: "
        "expected 1. أكتب الحديث كما هو بلفظه وسنده — verify بلفظه وسنده? بلفظه وبسنده? ; 2. أبحث عن "
        "الحديث وسنده ولفظه في — مطبوعه الأصلية? مطبوعاته الأصلية? مطبوعاتها الأصلية? — verify exactly; "
        "3. أبحث عن طرق الحديث وشواهده ; 4. أدرس سند الحديث الأصلي، متبعا ما يلي: with its four "
        "sub-bullets (أقوم بتشجير سند الحديث واستخراج رواته / أبحث عن كل راو من حيث العدالة والضبط / أبحث "
        "في اتصال السند / أبين درجة سند الحديث الأصلي) — verify each sub-bullet word by word; 5. أدرس طرق "
        "الحديث وشواهده (إن وجدت) وأبين درجة كل طريق أو شاهد ; 6. أبين درجة الحديث الأصلي بعدما تم البحث "
        "عن طرقه وشواهده — verify بعدما? بعد أن? and the whole wording. Mark [؟] where unclear. Short "
        "French notes at the end."
    ),
    "r659-zoom-p130-bottom": (
        "Zoom on a 300-dpi crop (bottom strip of an Arabic schoolbook page): a green banner heading and "
        "one line beneath it. Transcribe EXACTLY: 1) the banner heading — is it الإعداد القبلي? الإعداد "
        "التقليدي? الاعداد القبلي? — read letter by letter; 2) the line beneath: expected التعاون مع "
        "أصدقائي على تكوين فرق عمل لإنجاز أنشطة ورشات الدعم والتطبيق — verify أنشطة ورشات الدعم والتطبيق? "
        "ورشات عمل للدعم والتطبيق? كل word. 3) the page footer number digit by digit (expected 130). "
        "Mark [؟] where unclear. Short French notes at the end."
    ),
}

IMG = {
    "r659-zoom-p129-top": "p129-top.png",
    "r659-zoom-p129-aqra": "p129-aqra.png",
    "r659-zoom-p129-flow": "p129-flow.png",
    "r659-zoom-p130-isnad": "p130-isnad.png",
    "r659-zoom-p130-items": "p130-items.png",
    "r659-zoom-p130-bottom": "p130-bottom.png",
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
