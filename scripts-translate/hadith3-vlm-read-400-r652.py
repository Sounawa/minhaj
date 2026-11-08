# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM des rendus 300 dpi R652 (méthode hadith3-vlm-read-r647.py,
SDK isolé /tmp/vlm-r651 hors arbre git — incident wiper R651). Chaque lecture
réussie = 1 unité du budget ≤6 ; cache tr-tmp/qa-crops-r652/_read-<name>.json."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r652"
READ = "/tmp/vlm-r651/read.mjs"

PROMPTS = {
    "p78-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order, from the top: 1) the decorative green banner with a circular medallion "
        "carrying a number — compare الدرس الحادي عشر (lesson 11) vs التمرين الحادي عشر (exercise 11) — "
        "and the main title under it (should be أحكام الطواف (2)); read the medallion text word by word "
        "and the title exactly, 2) rubric أهداف الدرس and EVERY numbered objective line (read the digit "
        "at the start of each line digit-by-digit), 3) the tamhid paragraph including any questions or "
        "answer table between the intro and the first hadith (transcribe every short question line), "
        "4) the bold hadith quotes with their blue bracketed references [الموطأ رقم: NNN] — read the blue "
        "digits digit-by-digit; there should be a short Malik quote about الوقوف والحديث and a hadith of "
        "Umar Ibn al-Khattab يصدّرنّ أحدٌ من الحاج, 5) any page footer number. Mark illegible as [؟]. "
        "Short French notes at the end."
    ),
    "p79-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY, right-to-left, in reading "
        "order: 1) the continuation of Malik's comment (قال مالك: نرى ذلك...) including TWO Quranic "
        "citations set in ornate thuluth calligraphy with blue bracketed markers [سورة الحج: الآية NNN] "
        "and [سورة الحج: الآية NNN] — transcribe the Quranic words exactly and read each digit "
        "digit-by-digit, 2) the bold hadith quote عن سعد بن أبي وقاص with blue [الموطأ رقم: NNN] "
        "(digits digit-by-digit), 3) the bold hadith quote عن عائشة قدمت مكة وأنا حائض with blue "
        "[الموطأ رقم: NNN], 4) the biographical notice of عمر بن الخطاب (his names, كنيته أبو حفص, "
        "descriptions like الأمير العدوي, أمير المؤمنين, خليفة رسول الله, and the final lines about "
        "سيرته and استشهد عام NNN هـ — read every digit digit-by-digit). Mark illegible as [؟]. "
        "Short French notes at the end."
    ),
    "p81-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY, right-to-left, in reading "
        "order: 1) the lines about الرجوع لطواف الوداع بعد مغادرة البيت (مستحب عند مالك...) including the "
        "bold hadith quote عن عائشة أن صفية حاضت with blue [الموطأ رقم: NNN] (digits digit-by-digit), "
        "2) the bold hadith quote جروة عن مروى قال من قضى فقضى حجة الله with blue [الموطأ رقم: NNN], "
        "3) rubric ثانيا: طواف القدوم للمراهق and its full commentary lines (مما المراهق الذي يضيق وقته... "
        "بلغه أن مالك أنّ سعد بن أبي وقاص...), 4) rubric ثالثا: طواف الحائض and the first lines of that "
        "section (ذات ففي الموطأ...), including any bold quote beginning. Mark illegible as [؟]. "
        "Short French notes at the end."
    ),
    "p82-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY, right-to-left, in reading "
        "order: 1) the bold hadith quote ما روى عن ابن عمر لا تصدرنّ ولا تصرفنّ with blue [الموطأ رقم: NNN] "
        "(digits digit-by-digit), 2) the bold hadith quote جاءته امرأة تستفتيه فقالت إني أريد أن أطوف "
        "بالبيت with blue [الموطأ رقم: NNN] and the following commentary (قال عبد الله بن عمر ذلك إنما "
        "ذلك ركض من الدماء فاغتسلي), 3) the lines جماعة من رواة الموطأ by حيض (حرفه) — transcribe them "
        "as best as possible, 4) the bold hadith quote المتمتعة إذا حاضت وخشيت فوات الحج وأفعال العمرة "
        "with blue [الموطأ رقم: NNN], 5) the bold hadith quote قال مالك والمرأة الحائض إذا كانت قد طاقت "
        "بالبيت وصلت before تحيض with blue [الموطأ رقم: NNN] — read the FOUR blue reference numbers "
        "digit-by-digit each; note if two of them are identical or different. Mark illegible as [؟]. "
        "Short French notes at the end."
    ),
    "p83-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY, right-to-left, in reading "
        "order: 1) the closing commentary lines starting يستفاد من الدرس حرمة العبادات ومنها الحج فلا "
        "تصح إلا على طهارة... including any gloss lines after (there may be small gloss entries), "
        "2) the revision questions (التقويم or similar): ماذا يصنع من نسي طواف الوداع ثم تذكره بعد مغادرة "
        "البيت؟ and المستحاضة التي نزل بها الدم بعد أن تطهرت للطواف ماذا تفعل؟ — transcribe the rubric "
        "name exactly, 3) the bold hadith quote عن زينب بنت أبي سلامة عن سلمة أنّها قالت شكوت إلى رسول "
        "الله with blue [الموطأ رقم: NNN] (digits digit-by-digit) and the word describing her (ركب/راكب), "
        "4) the final instruction lines أحفظ أحاديث الدرس المقبل وأجيب عن الآتي: أشرح: مناة يعتلون, ذو "
        "قديد, حذو — and أبحث عن حكم السعي بين الصفا والمروة. Mark illegible as [؟]. Short French notes."
    ),
    "p84-banner": (
        "Top third of an Arabic schoolbook page. Transcribe EXACTLY, right-to-left: 1) the decorative "
        "green banner with a circular medallion carrying a number — compare الدرس الثاني عشر (lesson 12) "
        "vs التمرين الثاني عشر (exercise 12) — read the medallion text word by word, 2) the main title "
        "under the banner (should be أحكام السعي), 3) rubric أهداف الدرس and EVERY numbered objective "
        "line (read digits digit-by-digit), 4) the first line of the tamhid paragraph. If this is NOT a "
        "lesson banner (e.g. it is a continuation of a lesson, no medallion), say so explicitly. "
        "Short French notes at the end."
    ),
}

def run(name):
    out = os.path.join(DIR, f"_read-{name}.json")
    if os.path.exists(out):
        print(f"cache {name}"); return
    pdf_page = name.split("-")[0][1:]
    img = os.path.join(DIR, f"hi-{pdf_page}-{pdf_page.zfill(3)}.png")
    prompt = PROMPTS[name]
    cmd = ["node", READ, img, prompt, out + ".raw"]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
    if res.returncode != 0:
        print(f"ERR {name}: {res.stderr[:300]}"); return
    body = res.stdout.strip()
    json.dump({"name": name, "image": img, "body": body}, open(out, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    os.path.exists(out + ".raw") and os.remove(out + ".raw")
    print(f"OK {name} — {len(body)} car")

if __name__ == "__main__":
    for n in sys.argv[1:] or list(PROMPTS):
        run(n)
