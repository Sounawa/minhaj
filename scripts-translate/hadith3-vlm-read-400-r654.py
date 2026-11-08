# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM de vérification R654 (slot pdf-mut23h2x-400, leçon 11).
Méthode hadith3-vlm-read-400-r652.py (R652) / hadith3-vlm-read-r647.py ; SDK isolé
/tmp/vlm-r651 HORS arbre git (incident wiper R651). Couche texte recoupée par
rendus 300 dpi (hi-*.png, rendus R652 réutilisés) ; chaque lecture R654 réussie =
1 unité du budget ≤6 de la sous-passe 1 (pages pleines), sous-passe 2 = bande
p.84 + zooms des blocs calligraphiques coraniques. Cache tr-tmp/qa-crops-r654/
_r654-read-<name>.json — toute récusation de la couche texte est documentée
(nom d'image, ce qui a été lu), jamais devinée."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r654"
READ = "/tmp/vlm-r651/read.mjs"

PROMPTS = {
    "r654-p78-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order, from the top: 1) the decorative green banner with a circular medallion carrying a "
        "number — compare الدرس الحادي عشر (lesson 11) vs التمرين الحادي عشر (exercise 11) — read the "
        "medallion digit by digit and the main title under it (expected أحكام الطواف (2)); 2) rubric "
        "أهداف الدرس and EVERY numbered objective line (read the digit at the start of each line "
        "digit-by-digit); 3) the tamhid paragraph including the two short questions at its end (transcribe "
        "every short question line); 4) the bold hadith quotes with their blue bracketed references "
        "[الموطأ رقم: NNN] — there should be one short Mālik quote about stopping to talk during the ṭawāf "
        "and one hadith of Umar Ibn al-Khattab (لا يصدّرنّ) — read the blue digits digit-by-digit each; "
        "5) any page footer number. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r654-p79-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the continuation of Mālik's comment (ذلك فيما نرى والله أعلم لقول الله تعالى) "
        "including TWO Quranic citations set in ornate thuluth calligraphy with blue bracketed markers "
        "[سورة الحج: الآية NNN] and [سورة الحج: الآية NNN] — transcribe the Quranic words as best as you can "
        "(mark [؟] if uncertain) and read each bracketed digit digit-by-digit; 2) the bold hadith quote "
        "about Sa'd Ibn Abi Waqqas entering Makkah as a mūrahiq with blue [الموطأ رقم: NNN] (digits "
        "digit-by-digit); 3) the bold hadith quote of Aisha (قدمت مكة وأنا حائض) with blue [الموطأ رقم: NNN]; "
        "4) the biographical notice of Umar Ibn al-Khattab — his name, kunya أبو حفص, the epithets (العدوي، "
        "أمير المؤمنين، خليفة رسول الله), the line about his biography volumes, and the final استشهد عام NNN "
        "هـ — read the year digit-by-digit. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r654-p80-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order, from the top: 1) the rubric استخلاص المضامين and EVERY numbered item line (read the "
        "leading digits digit-by-digit); 2) the green rubric line like أولا: طواف الوداع and the sub-line "
        "1- حكم طواف الوداع; 3) the full commentary paragraph about the first ruling (مستحب عند مالك...) "
        "including the quoted words of Umar (لا يصدّرنّ...) and the words سماه نسكا لكونه عبادة, and whether "
        "two Quranic citations in ornate calligraphy appear in this paragraph with blue labels [سورة الحج "
        "الآية NNN] — transcribe the calligraphic words as best as possible, mark [؟] if uncertain, and read "
        "each blue digit digit-by-digit; 4) the closing gloss line starting قال مالك and/or والمراد بالشعائر "
        "(transcribe it fully); 5) any page footer number. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r654-p81-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the lines about الرجوع لطواف الوداع بعد مغادرة البيت including the bold hadith "
        "quote of Safiyya bint Huyayy (أحابستنا هي؟... فلا إذا) with blue [الموطأ رقم: NNN] (digits "
        "digit-by-digit), 2) the bold quote of Urwa/Jarwa (من قضى فقد قضى الله حجه) with blue [الموطأ رقم: "
        "NNN] and the words about آخر عهده الطواف بالبيت, 3) the green rubric ثانيا: طواف القدوم للمراهق and "
        "its full commentary (مما المراهق الذي يضيق وقته... ابن القاسم... يتوجه إلى عرفة... ينسقط عنه طواف "
        "القدوم... بلغه أن مالك أنّ سعد بن أبي وقاص...) — transcribe every line, 4) the green rubric ثالثا: "
        "طواف الحائض and the first lines of that section (ففي الموطأ... عائشة...) including the beginning of "
        "any bold quote. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r654-p82-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the continuation of the haid ruling (عدم الطهارة، الحائض والنفساء والمحدث) with "
        "the bold Mālik quote لا يطوف أحد بالبيت ولا بين الصفا والمروة إلا وهو طاهر with blue [الموطأ رقم: "
        "NNN] (digits digit-by-digit); 2) the bold hadith quote عن ابن عمر: جاءته امرأة تستفتيه فقالت إني "
        "أريد أن أطوف بالبيت... هرقت الدماء... فقال عبد الله بن عمر إنما ذلك ركضة من الشيطان فاغتسلي... "
        "with blue [الموطأ رقم: NNN]; 3) the commentary lines about رواة الموطأ (أن عجوزا استفتت، الاستحاضة، "
        "من ندب الاغتسال للطواف...) transcribe them as best as possible; 4) the green numbered heading "
        "2 - المتمتعة إذا حاضت وخشيت فوات الحج وأفعال العمرة with its commentary and bold quote أهلّت بالحج "
        "وأهديت/وتهدي... جزاء عنها طواف واحد with blue [الموطأ رقم: NNN]; 5) the green numbered heading "
        "3 - إذا حاضت المرأة بعد ركعتي الطواف with the bold quote عن الصفا والمروة وتنقض بعرفة والمزدلفة "
        "وترمي الجمار... حتى تطهر من حيضها with blue [الموطأ رقم: NNN] — read ALL the blue reference numbers "
        "digit-by-digit each and note whether any two are identical. Mark illegible as [؟]. Short French notes."
    ),
    "r654-p83-full": (
        "Full Arabic schoolbook page (300 dpi). Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) the closing paragraph starting يستفاد من الدرس حرمة العبادات (transcribe it "
        "fully to its last word); 2) the rubric التقويم (or التوقيم — read it exactly) and EVERY numbered "
        "question line (digits digit-by-digit); 3) the boxed hadith under the exploitation rubric (if a "
        "rubric like الاستثمار or similar appears, read the rubric name exactly): مالك عن أبي الأسود محمد "
        "بن عبد الرحمن بن نوفل عن عروة بن الزبير عن زينب بنت أبي سلامة عن أم سلمة... شكوت إلى رسول الله "
        "أني أشكى/اشتكى فقال: طوفي من وراء الناس وأنتي راكبة... يصلي إلى جانب البيت وهو يقرأ بالطور وكتاب "
        "مسطور — transcribe it exactly with blue [الموطأ رقم: NNN] digits digit-by-digit; 4) the closing "
        "instruction line أستعين بشرح الزرقاني... ; 5) rubric الإعداد القبلي with أحفظ أحاديث الدرس المقبل "
        "وأجيب عن الآتي and the numbered items (أشرح: ... ; أبحث عن ...) — transcribe the glossed words "
        "EXACTLY in order. Mark illegible as [؟]. Short French notes."
    ),
    # --- sous-passe 2 : zooms 600 dpi (tranchage des blocs calligraphiques) ---
    "r654-zoom-p79-comment": (
        "High-resolution 600 dpi crop of the top band of an Arabic schoolbook page. It contains the end "
        "of a comment by Mālik (ذلك فيما نرى والله أعلم لقول الله تبارك وتعالى) followed by TWO Quranic "
        "citations in ornate thuluth calligraphy, then Mālik's words فمحل الشعائر كلها وانقضاءها إلى البيت "
        "العتيق, then a blue reference [الموطأ رقم: NNN]. TASKS: 1) For EACH calligraphic citation, "
        "transcribe the ornate Arabic words word by word as precisely as possible (the candidates are "
        "thuluth-styled; look carefully for the words شعائر / تقوى / القلوب / لكم / منافع / أجل / مسمى / "
        "محلها / البيت / العتيق / ليقضوا / تفثهم / نذورهم / ليطوفوا) — say EXACTLY which of these words you "
        "can actually see in each citation. 2) Read each BLUE bracketed label [سورة الحج الآية : N] — read "
        "the 2-digit number digit by digit, taking great care to distinguish 0 from 2 (٠ vs ٢) and 1 from 3 "
        "(١ vs ٣) — report each digit explicitly. 3) Transcribe the blue Muwatta reference digit by digit. "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "r654-zoom-p80-fiqh": (
        "High-resolution 600 dpi crop of the lower band of an Arabic schoolbook page (fiqh section أولا: "
        "طواف الوداع). It contains a paragraph: طواف الوداع مستحب عند مالك؛ لقول عمر... لا يصدّرنّ... "
        "فإنّ آخر النسك الطواف بالبيت، فسماه نسكا لكونه عبادة، وذكر مالك أنّ ذلك مأخوذ من قوله تعالى: "
        "followed by TWO Quranic citations in ornate thuluth calligraphy with BLUE labels [سورة الحج الآية "
        ": N] each, then قال مالك: فمحل الشعائر كلها وانقضاءها إلى البيت العتيق، والمراد بالشعائر أعلام "
        "الحج وأفعاله. TASKS: 1) For EACH calligraphic citation transcribe the ornate words word by word as "
        "precisely as possible (look for شعائر / تقوى / القلوب / لكم / منافع / أجل / مسمى / محلها / البيت / "
        "العتيق / ليقضوا / تفثهم / نذورهم / ليطوفوا) — say EXACTLY which of these words are visible in each "
        "citation. 2) Read each BLUE 2-digit number digit by digit, distinguishing carefully 0 vs 2 and 1 "
        "vs 3 — report each digit explicitly. 3) Confirm the exact wording of the printed gloss line "
        "فمحل الشعائر كلها وانقضاءها إلى البيت العتيق and of والمراد بالشعائر أعلام الحج وأفعاله. "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "r654-zoom-p78-banner": (
        "High-resolution 600 dpi crop of the top band of an Arabic schoolbook page. It should contain: 1) a "
        "decorative green banner with a circular medallion carrying a two-digit number — read the medallion "
        "digit by digit (compare الدرس الحادي عشر = lesson 11 vs التمرين الحادي عشر = exercise 11 — read the "
        "banner words), 2) the main title under the banner (expected أحكام الطواف (2)), 3) rubric أهداف "
        "الدرس and the numbered objective lines — transcribe EVERY objective exactly, reading the leading "
        "digit of each line digit by digit, and read the FIRST objective's words carefully: does it say "
        "طواف القدوم والوداع or طواف القصور؟, 4) the beginning of the tamhid paragraph and whether a short "
        "Mālik quote with blue [الموطأ رقم: NNN] appears — read the blue digits digit by digit. "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
}

IMG = {
    "r654-p78-full": "hi-78-078.png",
    "r654-p79-full": "hi-79-079.png",
    "r654-p80-full": "hi-80-080.png",
    "r654-p81-full": "hi-81-081.png",
    "r654-p82-full": "hi-82-082.png",
    "r654-p83-full": "hi-83-083.png",
    "r654-zoom-p78-banner": "zoom-p78-banner.png",
    "r654-zoom-p79-comment": "zoom-p79-comment.png",
    "r654-zoom-p80-fiqh": "zoom-p80-fiqh.png",
}

def run(name):
    out = os.path.join(DIR, f"_r654-read-{name}.json")
    if os.path.exists(out):
        print(f"cache {name}")
        return
    img = os.path.join(DIR, IMG[name])
    prompt = PROMPTS[name]
    cmd = ["node", READ, img, prompt, out + ".raw"]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if res.returncode != 0:
        print(f"ERR {name}: {res.stderr[:300]}")
        return
    body = res.stdout.strip()
    json.dump({"name": name, "image": img, "body": body}, open(out, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    os.path.exists(out + ".raw") and os.remove(out + ".raw")
    print(f"OK {name} — {len(body)} car")


if __name__ == "__main__":
    for n in sys.argv[1:] or list(PROMPTS):
        run(n)
