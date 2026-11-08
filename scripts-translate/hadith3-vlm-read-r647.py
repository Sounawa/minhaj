# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM des rendus 300 dpi R647 (méthode hadith3-vlm-read-r641.py
adaptée : le sous-agent n'a pas accès aux images dans son contexte, la lecture
passe par le SDK vision ; chaque lecture réussie = 1 unité du budget ≤6).
Écrit tr-tmp/qa-crops-r647/_read-<name>.json (cache : re-run ne reconsomme pas)."""
import json
import os
import subprocess
import sys
import time

DIR = "/home/z/my-project/tr-tmp/qa-crops-r647"

PROMPTS = {
    "p65-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY, right-to-left, "
        "in reading order, from the top: 1) the decorative banner with a blue medallion "
        "(compare الدرس 9 vs التمرين 9) and the main title under it (about العجز والإحصار عن الحج), "
        "2) rubric أهداف الدرس and EVERY numbered objective line (read the digit at the start of "
        "each line digit-by-digit), 3) the tamhid paragraph (أقسام العبادة ثلاثة...), 4) the bold "
        "hadith quote (قال مالك عن ابن شهاب عن سليمان بن يسار عن عبد الله بن عباس...) with the "
        "blue bracketed reference [الموطأ رقم: NNN] — read the blue digits digit-by-digit. "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "p66-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) bold hadith quote of Malik about رسول الله حَلَّ وَضَحَابَةَ بالحديبية "
        "with blue [الموطأ رقم: NNN] (digits digit-by-digit), 2) second bold quote (قال مالك عن ابن "
        "شهاب عن سالم عن عبد الله بن عمر المحصر...) with blue [الموطأ رقم: NNN], 3) the biographical "
        "notice (the name, surnames like الحبر والبحرة ترجمان القرآن, دعا له رسول الله, the year of "
        "death مات بالطائف سنة — read every digit digit-by-digit), 4) rubric الشرح and the first line. "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "p67-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) rubric استخلاص المضامين and its numbered items (digits digit-by-digit), "
        "2) rubric أولا: and its exact title line, 3) the full commentary (قول الخثعمية..., صحة "
        "النيابة في الحج عن العاجز..., قال العياض..., وقال ابن عبد البر...), including the Quranic "
        "citation introduced by وكان لقوله تعالى with its ornate text and blue bracketed marker "
        "[سورة آل عمران: الآية NNN] — read the Quranic words and the digit digit-by-digit. "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "p68-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) rubric ثانيا: الإحصار عن الحج and its two-line preamble, 2) item 1- "
        "الإحصار بعدو with commentary, 3) bold quote of Malik من حبس بعدو... with blue [الموطأ رقم: "
        "NNN] (digits digit-by-digit), 4) quote عن عمر عنهما ما أمرهما إلا واحد with blue reference, "
        "5) the Quranic citation with its ornate text and blue marker [سورة البقرة: الآية NNN] — "
        "read digit digit-by-digit, 6) item 2- الإحصار بغير عدو: the bold hadith quote (it may look "
        "partially damaged) and the following commentary lines up to the end of the page, including "
        "any second Quranic citation with marker. Mark illegible as [؟]. Short French notes at the end."
    ),
    "p69-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY, right-to-left, in "
        "reading order: 1) first lines (ومن صور الإحصار بغير عدو: الخطأ في العدد وخفاء الهلال...), "
        "2) bold quote of Malik وَقَدْ أَمَرَ عُمَرُ بْنُ الْخَطَّابِ أَبَا أَيُوبَ... with blue "
        "[الموطأ رقم: NNN] (digits digit-by-digit), 3) second bold quote ما يحرم إما بمَرَضٍ أو "
        "بعيره أو بخطم من العدو أو حُفِيَ عليه الهلال فهو محصر with blue reference — transcribe the "
        "word before من العدو carefully, 4) rubric lines أبحث وأجيب / أبين طريقة المالكية..., 5) last "
        "bold quote (مالك عن عقبة بن إبراهيم عن كريب مولى ابن عباس...) with blue [الموطأ رقم: NNN]. "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "p70p71top": (
        "Image with TWO parts separated by a gap: TOP = end of a schoolbook lesson (rubric أبحث في "
        "شرح الزرقاني وأجيب عن الأسئلة with numbered questions — transcribe every line EXACTLY, "
        "digits digit-by-digit, especially question 1 which may look partly damaged); BOTTOM = top "
        "of the NEXT page: decorative banner with blue medallion (compare الدرس 10 vs التمرين 10), "
        "main title, rubric أهداف الدرس and every numbered objective line EXACTLY, then tamhid "
        "beginning (الطواف عبادة...). Mark illegible as [؟]. Short French notes at the end."
    ),
}


def read_one(name: str, tries: int = 5) -> str:
    out = f"{DIR}/_read-{name}.json"
    if os.path.exists(out):
        with open(out, encoding="utf-8") as f:
            try:
                return json.load(f)["content"]
            except Exception:
                pass
    prompt = PROMPTS[name]
    img = f"{DIR}/{name}.png"
    for i in range(tries):
        r = subprocess.run(
            ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out],
            capture_output=True, text=True, timeout=300,
        )
        if r.returncode == 0 and os.path.exists(out):
            try:
                with open(out, encoding="utf-8") as f:
                    d = json.load(f)
                return d.get("content", json.dumps(d, ensure_ascii=False))
            except Exception:
                pass
        wait = 20 * (i + 1)
        print(f"[{name}] tentative {i + 1} échouée, attente {wait}s", flush=True)
        time.sleep(wait)
    raise SystemExit(f"ÉCHEC lectures {name}")


if __name__ == "__main__":
    names = sys.argv[1:]
    for n in names:
        print(f"===== {n} =====", flush=True)
        print(read_one(n), flush=True)
