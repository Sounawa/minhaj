# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM R649 des crops de bornes (slot pdf-mut23h2x-399, leçon 10).
Méthode hadith3-vlm-read-r647.py (ouvrier 398) : le sous-agent n'a pas accès aux
images dans son contexte, la lecture passe par le SDK vision (`z-ai vision`).
Chaque lecture réussie = 1 unité du budget ≤6 par sous-passe (doctrine R646).
Cache : tr-tmp/qa-crops-r647/_read-r649-<name>.json (noms uniques R649 — jamais
de collision avec les caches de l'ouvrier 398)."""
import json
import os
import subprocess
import sys
import time

DIR = "/home/z/my-project/tr-tmp/qa-crops-r647"

PROMPTS = {
    "r649-p71-top": (
        "Top strip of an Arabic schoolbook page. Transcribe EXACTLY the decorative banner at the "
        "top: 1) the small word above/left of the blue circular medallion — is it الدرس or التمرين? "
        "read it letter by letter; 2) the number inside the medallion (read the digit digit-by-digit); "
        "3) the main title under the banner (it should be أَحْكَامُ الطَّوَافِ with something); "
        "4) rubric أَهْدَافُ الدَّرْسِ and EVERY numbered objective line EXACTLY with its digit. "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "r649-p78-top": (
        "Top strip of an Arabic schoolbook page. Describe EXACTLY what appears: is there a decorative "
        "banner with a blue circular medallion? If yes: 1) the small word above/left of the medallion "
        "(الدرس أو التمرين؟) letter by letter; 2) the digit inside the medallion digit-by-digit; "
        "3) the main title under the banner. Then transcribe all other Arabic lines EXACTLY in reading "
        "order (bold hadith quotes with blue [الموطأ رقم: NNN] — digits digit-by-digit, rubrics like "
        "الإعداد القبلي, numbered questions). Mark illegible as [؟]. Short French notes at the end."
    ),

    "r649-p71-full": (
        "Full Arabic schoolbook page (lesson 10 opening, after the banner). Transcribe ALL Arabic "
        "lines EXACTLY right-to-left in reading order: 1) rubric أهداف الدرس and the three numbered "
        "objectives (digits digit-by-digit), 2) the tamhid paragraph beginning الطواف عبادة يقوم بها "
        "المحرم... — transcribe EVERY word including the sentence after سبعة أشواط (it may be in bold "
        "or heavy type, some words may look garbled in print — transcribe what you SEE), 3) the "
        "opening question (فما أحكام الطواف؟ وكيف يستلم...), 4) the bold hadith of Malik عن جعفر بن "
        "محمد عن أبيه عن جابر بن عبد الله رأيت رسول الله رَمَل... with blue [الموطأ رقم: NNN] — read "
        "the digits digit-by-digit. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r649-p73-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY right-to-left in reading "
        "order: 1) the two short gloss lines at the very top (they gloss بذي طوى and another word — "
        "the first gloss starts with a word that may be أناغ or أناقة: transcribe it EXACTLY, and the "
        "word after the colon, e.g. الإيلاء؟), 2) rubric استخلاص المضامين and its THREE numbered items "
        "EXACTLY, 3) the sentence beginning اشتملت أحاديث الدرس على أحكام وفضائل خاصة بالطواف منها, "
        "4) the rubric أولا and its exact title (something like الرمل في الطواف or الطواف الرمل), "
        "5) the bold quote عن ابن عمر رضي الله عنهما أن النبي كان إذا طاف بالبيت الأول بحب ثلاثة "
        "أطواف ويمشي ر... with its bracketed reference [صحيح البخاري], 6) the continuation عن عمر "
        "وابن الزبير وعن عبد الله بن عمر كان يرمَل من الحجر إلى الحجر الأسود سبعة أطواف ويمشي... "
        "وعن هشام بن عروة عن أبيه عروة عن مروة? كان إذا طاف بالبيت يسعى الأشواط الثلاثة وكان يقول: "
        "لا إله إلا أنت... لا يشغل الناس بسماعهم عما هم فيه — with blue [الموطأ رقم: NNN] digits "
        "digit-by-digit, 7) the last lines قال مالك وذلك المت... فالرمل سنة في الثلاثة فلو تركه فيها... "
        "ولم يخالف إلا ابن عباس. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r649-p76-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY right-to-left in reading "
        "order: 1) the top garbled lines ending the previous paragraph with blue [الموطأ رقم: NNN] "
        "(digits digit-by-digit), 2) item 2- إذا أقيمت صلاة الصبح أو العصر والطائف لم يتم سبعه — "
        "the quote of Malik ومن طاف بالبيت بعض... and its blue reference digit-by-digit, 3) the THREE "
        "numbered questions (أبين حكم المزاحمة على استلام الركن / كيف يُستلم الركن اليماني؟ / أبين حكم "
        "من أقيمت عليه صلاة الصبح مع الإمام ولم يتم سبعة أشواط), 4) the bold hadith Malik عن ابن شهاب "
        "عن السائب بن يزيد عن عبد الله بن عبد الله بن عبد الله بن محمد بن أبي بكر الصديق أخبر عبد "
        "الله بن عمر عن عائشة أن النبي قال ألا لمروة؟؟ أن عمركم حين بنوا الكعبة أصرروا على قواعد "
        "إبراهيم... قالت فلت يا رسول الله ألا ترددَهُ على قواعد إبراهيم؟ فقال يا رسول؟؟ الله؟?? لو لا "
        "حدثان قومك بالكفر — transcribe EXACTLY every word including any garbled ones, and the blue "
        "[الموطأ رقم: NNN] digit-by-digit. Mark illegible as [؟]. Short French notes at the end."
    ),

    "r649-p73-gloss-zoom": (
        "High-resolution zoom of the TOP of an Arabic schoolbook page. There are two short gloss "
        "lines (dictionary-style entries, each introduced by a hyphen). Transcribe them EXACTLY "
        "letter by letter with the diacritics you see: line 1 starts with a word like أناغ or أناخ "
        "followed by a colon then الإيلاء then another short phrase (أبركها فبركت؟) — transcribe "
        "EVERY glyph, do not normalize; line 2 starts with بذي طوى followed by مُثلث الطاء؟ ويُنَوَّن؟ "
        "موضع قرب مكة. Mark each uncertain glyph as [؟]. Short French notes at the end."
    ),

    "r649-p76-istimar-zoom": (
        "High-resolution zoom of the BOTTOM half of an Arabic schoolbook page. Transcribe EXACTLY, "
        "letter by letter: 1) the three numbered evaluation questions (أبين حكم المزاحمة على استلام "
        "الركن / كيف يُستلم الركن اليماني؟ / أبين حكم من أقيمت عليه...), 2) the bold hadith of Malik "
        "عن ابن شهاب عن سالم بن عبد الله... — transcribe the FULL isnad chain word by word (who is "
        "سالم's father? the chain may contain repetitions like ابن عبد الله بن عبد الله بن محمد بن "
        "أبي بكر الصديق أخبر عبد الله بن عمر), 3) the opening of the Prophet's words (before فالت؟): "
        "transcribe glyph by glyph — it may read ألا لمرواة؟ أو ألا لمراة؟ أو ألا لمراءة؟ أن أمراكم "
        "حين بنوا الكعبة أصرروا على قواعد إبراهيم — do NOT normalize, transcribe what you see, "
        "4) عائشة's question and the Prophet's reply (لو لا حدثان قومك بالكفر؟), 5) the closing "
        "words of عبد الله بن عمر (رسول الله ترك استلام الركنين اللذين يليان الحجر إلا أن البيت لم "
        "يتمم على قواعد إبراهيم؟), 6) the blue reference [الموطأ رقم: NNN] digit by digit. Mark each "
        "uncertain glyph [؟]. Short French notes at the end."
    ),
    "r649-p79-top": (
        "Top strip of an Arabic schoolbook page. Describe EXACTLY what appears: is there a decorative "
        "banner with a blue circular medallion? If yes: 1) the small word above/left of the medallion "
        "(الدرس أو التمرين؟) letter by letter; 2) the digit inside the medallion digit-by-digit; "
        "3) the main title under the banner (compare أحكام الطواف (2)؟). Then transcribe the first "
        "lines (rubric أهداف الدرس, numbered objectives, tamhid beginning) EXACTLY. Mark illegible "
        "as [؟]. Short French notes at the end."
    ),
}


def read_one(name: str, tries: int = 4) -> str:
    out = f"{DIR}/_read-{name}.json"
    if os.path.exists(out):
        with open(out, encoding="utf-8") as f:
            try:
                d = json.load(f)
                if d.get("content"):
                    return d["content"]
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
                c = d.get("content") or json.dumps(d, ensure_ascii=False)
                return c
            except Exception:
                pass
        wait = 20 * (i + 1)
        print(f"[{name}] tentative {i + 1} échouée, attente {wait}s — {r.stderr[:200]}", flush=True)
        time.sleep(wait)
    raise SystemExit(f"ÉCHEC lectures {name}")


if __name__ == "__main__":
    for n in sys.argv[1:]:
        print(f"===== {n} =====", flush=True)
        print(read_one(n), flush=True)
