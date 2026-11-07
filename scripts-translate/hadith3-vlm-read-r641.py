# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM des bandes d'image R641 (méthode R638 adaptée :
la lecture d'image passe par le SDK vision, l'ouvrier sous-agent n'ayant
pas accès aux images dans son contexte). Chaque lecture réussie = 1 unité
du budget (≤ 15). Écrit tr-tmp/qa-crops-r641/_read-<name>.json."""
import json
import os
import subprocess
import sys
import time

DIR = "/home/z/my-project/tr-tmp/qa-crops-r641"

PROMPTS = {
    "p58-a-titre": (
        "Crop from the top of an Arabic schoolbook page. Read the decorative banner: "
        "1) the blue medallion text EXACTLY (compare الدرس 8 vs التمرين 8), 2) the main title EXACTLY, "
        "3) the rubric name (like أهداف الدرس) and the objective lines exactly. "
        "Transcribe Arabic EXACTLY, mark illegible as [؟]. Short French notes at the end."
    ),
    "p58-b-tamhid": (
        "Crop of an Arabic schoolbook paragraph (tamhid). Transcribe ALL Arabic lines EXACTLY, "
        "right-to-left, character by character, preserving vocalisation marks where visible, "
        "mark illegible words as [؟]. Short French notes at the end."
    ),
    "p58-c-quote": (
        "Crop of an Arabic schoolbook paragraph (quote of Malik in bold). Transcribe ALL Arabic lines "
        "EXACTLY, right-to-left, mark illegible as [؟]. Pay attention to any blue bracketed reference "
        "number. Short French notes at the end."
    ),
    "p59-a-1024": (
        "Crop of an Arabic schoolbook: end of a bold quote of Malik with a blue bracketed reference "
        "[الموطأ رقم: NNN]. Transcribe ALL Arabic lines EXACTLY and read the blue digits digit-by-digit "
        "(they may look like e.g. 1024). Mark illegible as [؟]. Short French notes."
    ),
    "p59-b-yahya-verse": (
        "Crop of an Arabic schoolbook containing a chain (قال مالك... قال يحيى...), then a Quranic verse "
        "printed in ornate thuluth calligraphy, then prose (قال مالك فالذي يصيد الصيد...). Transcribe ALL "
        "Arabic lines EXACTLY including the thuluth verse (read it carefully, letter by letter) and the "
        "bracketed marker [سورة المائدة: الآية NNN] (read the digit exactly). Mark illegible as [؟]. Short French notes."
    ),
    "p59-d-1028": (
        "Crop of an Arabic schoolbook: hadith text (خمسٌ فواسق...) with blue bracketed reference "
        "[الموطأ رقم: NNN]. Transcribe ALL Arabic lines EXACTLY and read the blue digits digit-by-digit. "
        "Mark illegible as [؟]. Short French notes."
    ),
    "p59-e-bio": (
        "Crop of an Arabic schoolbook: biographical notice of a transmitter (يحيى بن يحيى...). Transcribe "
        "ALL Arabic lines EXACTLY, especially any year of death (read digits digit-by-digit, e.g. سنة ٢٣٤ or "
        "234). Mark illegible as [؟]. Short French notes."
    ),
    "p61-a-thania-1027": (
        "Tall crop of an Arabic schoolbook fiqh page. Transcribe ALL Arabic lines EXACTLY in order, "
        "including a quote of Malik with blue bracketed reference [الموطأ رقم: NNN] (read digits "
        "digit-by-digit), a citation of ابن شهاب, a Muwatta page reference like 734/3, and the last lines "
        "of the page (may be partially cut). Mark illegible as [؟]. Short French notes."
    ),
    "p62-a-verse-poem": (
        "Crop of an Arabic schoolbook: a Quranic verse fragment in ornate thuluth inside prose "
        "(...أو إطعام مساكين أو صياما... [سورة المائدة: الآية NNN]), then the words قيل وفي ذلك يخير, then "
        "two lines of didactic poetry. Transcribe EXACTLY, read the bracketed digit exactly. Mark "
        "illegible as [؟]. Short French notes."
    ),
    "p62-b-1026": (
        "Crop of an Arabic schoolbook: long quote of Malik (أحسنُ ما سمعتُ...) with blue bracketed "
        "reference [الموطأ رقم: NNN]. Transcribe ALL Arabic lines EXACTLY, digits digit-by-digit. "
        "Mark illegible as [؟]. Short French notes."
    ),
    "p63-a-1033": (
        "Crop of an Arabic schoolbook: quote with blue bracketed reference [الموطأ رقم: NNN] then a "
        "commentary of الباجي. Transcribe ALL Arabic lines EXACTLY, digits digit-by-digit. Mark "
        "illegible as [؟]. Short French notes."
    ),
    "p63-b-siba-num": (
        "Crop of an Arabic schoolbook: partially corrupted zone then a quote (كان من السباع لا يعدها "
        "الضبع والتعلب والهر وما أشبههن من السباع...) with a blue bracketed reference [الموطأ رقم: NNN] "
        "whose digits are partially damaged. Read the digits digit-by-digit as best visible. Transcribe "
        "ALL Arabic lines EXACTLY. Mark illegible as [؟]. Short French notes."
    ),
    "p64-a-texts": (
        "Crop of an Arabic schoolbook with three numbered texts: 1) quote about نظر في المرآة, "
        "2) quote about مريم قالت سالت سعيد بن المسيب... غطق, 3) quote about خُراج المحرم. Each has a blue "
        "bracketed reference [الموطأ رقم: NNN]. Transcribe ALL Arabic lines EXACTLY, read every blue "
        "reference digit-by-digit. Mark illegible as [؟]. Short French notes."
    ),
    "p64-b-vue": (
        "Overview of a full Arabic schoolbook page. List, from top to bottom, every green/grey rubric "
        "banner (like التقييم, التدريب, الإعداد القبلي, أستعين بشرح الزرقاني...) EXACTLY as printed, and "
        "under each banner the item lines. Mark illegible as [؟]. Short French notes."
    ),
    "p65-a-banniere-l9": (
        "Crop from the top of an Arabic schoolbook page. Read the decorative banner: 1) the blue medallion "
        "text EXACTLY (like الدرس 9), 2) the main title EXACTLY, 3) the rubric and objective lines. "
        "Transcribe Arabic EXACTLY, mark illegible as [؟]. Short French notes."
    ),
    "p59-b-ext": (
        "Tall crop of an Arabic schoolbook: an ornate thuluth Quranic verse block inside a hadith quote, "
        "followed by a blue bracketed marker [سورة المائدة: الآية NNN] and then prose (قال مالك فالذي...). "
        "Read the thuluth verse carefully letter by letter and transcribe EXACTLY; read the marker digits "
        "digit-by-digit; transcribe the prose lines after it EXACTLY. Mark illegible as [؟]. Short French notes."
    ),
    "p62-mid": (
        "Tall crop of an Arabic schoolbook fiqh page. From top to bottom transcribe EXACTLY: items أ- ب- ج- "
        "about the estimation of the hunted animal (مثل، قيمة، صيام), a small thuluth Quranic fragment with "
        "blue marker [سورة المائدة: الآية NNN] (read digits digit-by-digit), two lines of didactic poetry, a "
        "long bold quote of Malik (أحسنُ ما سمعتُ...) with blue reference [الموطأ رقم: NNN], then a rubric "
        "ثالثا and a hadith about خمس فواسق with blue reference(s) [الموطأ رقم: NNN]. Transcribe ALL Arabic "
        "lines EXACTLY in order, digits digit-by-digit. Mark illegible as [؟]. Short French notes."
    ),
    "p63-mid": (
        "Tall crop of an Arabic schoolbook fiqh page. Transcribe EXACTLY: a bold quote (المحرم لا يحل له...) "
        "with blue reference [الموطأ رقم: NNN], then a commentary of الباجي, then a partially damaged zone, "
        "then a quote (كان من السباع لا يعدُها...) with blue reference [الموطأ رقم: NNN] — read its digits "
        "digit-by-digit. Transcribe ALL Arabic lines EXACTLY. Mark illegible as [؟]. Short French notes."
    ),
    "p64-mid": (
        "Tall crop of an Arabic schoolbook page with numbered texts then a rubric. From top to bottom: "
        "1) quote about نظر في المرآة with blue [الموطأ رقم: NNN]; 2) quote about مريم قالت سالت سعيد... "
        "قلَّد لك ظفرًا with blue [الموطأ رقم: NNN]; 3) quote about يبطن المحرم ويقطع دملا ويفجأ خراجه with "
        "blue [الموطأ رقم: NNN]; then rubric أستعين بشرح الزرقاني... and items (معنى, أبين حكم, figures). "
        "Transcribe ALL Arabic lines EXACTLY, every blue reference digit-by-digit. Mark illegible as [؟]. "
        "Short French notes."
    ),
}


def read_one(name: str, tries: int = 8) -> str:
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
            capture_output=True, text=True, timeout=240,
        )
        if r.returncode == 0 and os.path.exists(out):
            try:
                with open(out, encoding="utf-8") as f:
                    d = json.load(f)
                return d.get("content", json.dumps(d, ensure_ascii=False))
            except Exception:
                pass
        wait = 60 * (i + 1)
        print(f"[{name}] tentative {i + 1} échouée, attente {wait}s", flush=True)
        time.sleep(wait)
    raise SystemExit(f"ÉCHEC lectures {name}")


if __name__ == "__main__":
    names = sys.argv[1:]
    for n in names:
        print(f"===== {n} =====", flush=True)
        print(read_one(n), flush=True)
