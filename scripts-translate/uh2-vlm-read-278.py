# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM pleine page R658 (slot pdf-mut23h2u-278, leçon 24
الاختصار في الحديث وروايته بالمعنى). Mécanique hadith3-vlm-read-402-r657.py
(R657) : couche texte recoupée par rendus 300 dpi (tr-tmp/qa-crops-r658/),
chaque lecture = cache tr-tmp/qa-crops-r658/_r658-read-<name>.json — toute
récusation de la couche texte est documentée (nom d'image, ce qui a été lu),
jamais devinée. Moteur : CLI z-ai vision (SDK VLM), prompts ciblés par page."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r658"

PROMPTS = {
    "r658-p125-full": (
        "Full Arabic schoolbook page (300 dpi), lesson 24 opening. Transcribe ALL Arabic lines EXACTLY, "
        "right-to-left, in reading order, from the top: 1) green banner + medallion (read the lesson number "
        "digit-by-digit; expected ٢٤) and expected title الاختصار في الحديث وروايته بالمعنى — transcribe the "
        "printed title exactly; 2) the rubric أهداف الدرس with EVERY numbered objective (expected four: أن "
        "أتعرف حكم رواية الحديث بالمعنى / أن أميز بين من يجوز له رواية الحديث بالمعنى ومن لا يجوز له ذلك / أن "
        "أحرص على حفظ الحديث ونقله بلفظه كما هو / أن أتخلق بأخلاق العلماء في التبليغ عن رسول الله صلى الله "
        "عليه وسلم) — transcribe each exactly; 3) the tamhid paragraph beginning الأصل فيمن سمع الحديث أن "
        "يقيده ويحفظه — transcribe to its final word including the closing question فما حكم اختصار الحديث أو "
        "روايته بالمعنى؛ 4) the boxed matn of Ibn Hajar (expected قال الحافظ ابن حجر رحمه الله: ولا يجوز تعمد "
        "ترك اللفظ والمرادف إلا لعالم بما يحيل المعاني؛ فإن حفي المعنى حاج إلى شرح الغريب وما المشكل) — "
        "transcribe EXACTLY, note whether the last words are وما المشكل or وما أشكل; 5) the rubric الفهم / "
        "الشرح and استخلاص المضامين with its numbered items, and the boxed definition (expected الغريب: البعيد "
        "عن وطنه، وغريب الحديث: ...) — transcribe the WHOLE boxed definition exactly, including what follows "
        "(the fragments ما القن وأشكل معد / بسبب تعارض ظاهر suggest ما ظهر معناه وأشكل لفظه؟ أو بسبب تعارض "
        "ظاهر؟) — read word by word, mark [؟] where unclear. Short French notes at the end."
    ),
    "r658-p126-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the green rubric التحليل and sub-rubric أولا: اختصار الحديث with its definition "
        "sentence (expected اختصار الحديث يقصد به الاقتصار على بعض الحديث وحذف بعضه وقد اختلف العلماء فيه على "
        "أقوال) — transcribe exactly; 2) the THREE bullets of the scholarly opinions (منهم من منع... مطلقا / "
        "منهم من منع ذلك مع تجويز النقل بالمعنى... على التمام / منهم من جوز ذلك وأطلق ولم يفصل) — transcribe "
        "each bullet fully; 3) the fourth paragraph beginning وذلك أنه يجوز ذلك من العالم العارف (expected "
        "phrase -وهو الصحيح- التفصيل و بمنزلة خبرين منفصلين في أمرين لا تعلق لأحدهما بالآخر) with its blue "
        "bracketed reference [مقدمة ابن الصلاح، ص NNN] — read the page digit DIGIT BY DIGIT (expected 324); "
        "4) the exception paragraph beginning وإنما جاز ذلك للعالم دون غيره with the Quranic-legal example "
        "لا تبيعوا الذهب بالذهب إلا سواء بسواء and its blue bracketed source — transcribe the source line "
        "EXACTLY word by word (expected صحيح مسلم، كتاب البيوع، باب بيع الذهب بالذهب — verify each word, mark "
        "[؟] where unclear); 5) the closing paragraph وأما تقطيع مصنف الحديث الواحد وتفريقه في الأبواب "
        "(expected المواضع المتفرقة, الأئمة كمالك وأحمد وأبي داود والنسائي وغيرهم) — transcribe exactly, "
        "note whether the word before المتفرقة is المواضع. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r658-p127-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the continuation of the 'prohibition' school of thought (expected بل رواه ابن "
        "السمعاني عن ابن عمر وقيل لا يجوز في حديث النبي صلى الله عليه وسلم ولا يجوز في حديث غيره وهو مروي عن "
        "مالك ولعله رواية التهوين في ذلك وقيده بعضهم بما إذا لم يكن مما تعبد بلفظه ولا هو من جوامع الكلم) with "
        "its blue bracketed reference — transcribe fully and read the reference digits DIGIT BY DIGIT "
        "(expected [شرح نخبة الفكر في مصطلحات أهل الأثر، للقاري، ص 500]); 2) the rubric وبعضهم فصل في ذلك "
        "فقال with the THREE numbered clauses أ/ ب/ ج (expected: أ- يجوز في المفردات لظهور ترادفها فتغييره "
        "يسير دون المركبات لاحتياجها إلى زيادة / ب- إنما يجوز لمن يستحضر اللفظ ليتمكن من التصرف فيه وهذا قد "
        "يعترض عليه بأنه إذا استحضر اللفظ فلم الرواية بالمعنى / ج- يجوز لمن كان يحفظ الحديث فنسي لفظه وبقي "
        "معناه مرتسما في ذهنه فله أن يرويه بالمعنى لمصلحة تحصيل الحكم) — transcribe each clause to its end, "
        "including the long clause ج (لا ينهض إلى التعبير عن ألفاظ من أوتي جوامع الكلم... مفوت للتبرك بألفاظ "
        "صاحب الشريعة ومفتح لأبواب الشك والشبهة في موارد السنة) with the second blue reference read DIGIT BY "
        "DIGIT (expected ص 500); 3) the bottom paragraph beginning وذلك أنه إن لم يكن عاما بالألفاظ ومقاصدها "
        "خبيرا بما يحيل معانيها بصيرا بمقادير التفاوت — transcribe every line EXACTLY (this zone is "
        "OCR-garbled in the text layer; expected continuation mentioning قال الحافظ ابن حجر repeated quote "
        "ولا يجوز تعمد ترك اللفظ والمرادف إلا لعالم بما يحيل المعاني and وعمله أهل العلم أن ينقلوا الرواية "
        "كما وصلت ولا يغيروها في كتبهم ونقل الحافظ ابن حجر عن القاضي عياض رحمهما الله قوله ينبغي سد باب "
        "الرواية بالمعنى لئلا يتسلط من لا يحسن ممن يظن أنه يحسن وقد عقد القاضي عياض في كتابه الإلماع إلى "
        "معرفة أصول الرواية وتقييد السماع بابا عنوانه باب تحري الرواية والمجيء باللفظ ومن رخص للعلماء في "
        "المعنى ومن منع وخلص فيه إلى أن المستحب المجيء بنفس اللفظ ما استطيع) with the final blue reference "
        "read DIGIT BY DIGIT (expected [الإلماع إلى معرفة أصول الرواية وتقييد السماع، القاضي عياض، ص 179]) — "
        "verify each expected phrase against the image, mark [؟] where unclear. Short French notes at the end."
    ),
    "r658-p128-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the rubric أهتدي وأقتدي with the quote of Ibn al-Salah (expected قال الإمام ابن "
        "الصلاح رحمه الله مبينا آداب طالب الحديث: وليسأل الله تبارك وتعالى التيسير والتأييد والتوفيق وليأخذ "
        "نفسه بالأخلاق الزكية والآداب المرضية ولا يحملنه الحرص والشره على التساهل في السماع والتحمل والإخلال "
        "بما يشترط عليه في ذلك) with its blue bracketed reference — transcribe fully, read the page digit "
        "DIGIT BY DIGIT (expected [مقدمة ابن الصلاح، ص 247 بتصرف]); 2) the rubric التقويم (the text layer "
        "garbled it as اللفويم — verify the real rubric name) with EVERY numbered item (expected three: "
        "أستخلص مما سبق الفرق بين اختصار الحديث وروايته بالمعنى / أبين الراجح من أقوال العلماء في اختصار "
        "الحديث / أصنف في خطاطة آداب طالب الحديث) — read leading digits digit-by-digit; 3) the rubric "
        "الاستثمار with the quote of al-Qadi Iyad (expected قال الإمام القاضي عياض رحمه الله: لا خلاف أن على "
        "الجاهل والمبتدىء ومن لم يمهر في العلم ولا تقدم في معرفة تقديم الألفاظ وترتيب الجمل وفهم المعاني أن "
        "لا يكتب ولا يروي ولا يحكي حديثا إلا على اللفظ الذي سمعه وأنه حرام عليه التعبير بغير لفظه المسموع إذ "
        "جميع ما يفعله من ذلك تحكم بالجهالة وتصرف على غير حقيقة في أصول الشريعة وتقول على الله ورسوله ما لم "
        "يحط به علما) with its blue reference read DIGIT BY DIGIT (expected [الإلماع إلى معرفة أصول الرواية "
        "وتقييد السماع، القاضي عياض، ص 174]) and the numbered sub-item أ- أبين ما يجب على طالب الحديث أن "
        "يلتزمه من قيم الأمانة والصدق والخشية; 4) the rubric الاعداد القبلي with the lead line (expected يراعى "
        "في إنجاز درس الأنشطة التطبيقية ما يلي) and EVERY numbered item — read each leading digit DIGIT BY "
        "DIGIT (text layer suggested 1. 2. 4. with item 1 garbled as لزن تتح حضية الأنشطة التطبيقية داخل "
        "المكلية — transcribe item 1 EXACTLY as printed, expected أن تنفذ حصص الأنشطة التطبيقية داخل "
        "المؤسسة, and state how many items there really are and their real numbers). Mark illegible as [؟]. "
        "Short French notes at the end."
    ),
}

IMG = {
    "r658-p125-full": "p125-full.png",
    "r658-p126-full": "p126-full.png",
    "r658-p127-full": "p127-full.png",
    "r658-p128-full": "p128-full.png",
}


def run(name):
    out = os.path.join(DIR, f"_r658-read-{name}.json")
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
