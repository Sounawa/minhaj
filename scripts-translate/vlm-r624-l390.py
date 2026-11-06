#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R624 — lectures VLM ancrées leçon 1 hadith-3es (slot pdf-mut23h2x-390, p.10-16).
Méthode R541 : question fermée ou ancrée par crop ; sortie tr-tmp/vlm-r624/<key>.json.
Jamais deviné : chaque chiffre (n° de hadith, verset) et chaque bloc brouillé par
l'OCR est relu SUR L'IMAGE.
"""
import json
import subprocess

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r624"
OUT = f"{HOME}/tr-tmp/vlm-r624"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 3e année de l'enseignement collégial traditionnel). "
        "Réponds UNIQUEMENT à la question posée, par transcription EXACTE du texte "
        "imprimé visible. Si tu n'es pas sûr d'un mot, écris [illisible]. "
        "N'invente AUCUN texte, ne complète jamais de mémoire.")

ASKS = [
    ("p10-objectifs", "p10-full.png",
     "Transcris exactement le bloc أهداف الدرس de cette page (leçons objectives "
     "numérotées 1-, 2-, 3-), puis le paragraphe تمهيد qui suit, mot à mot tel "
     "qu'imprimé. Transcris aussi les questions d'ouverture qui précèdent le premier "
     "hadith (فما هو الحج؟ ...)."),
    ("p10-h1-h2", "p10-full.png",
     "Transcris exactement les DEUX premiers hadiths imprimés (avec leurs isnāds et "
     "les crochets [الموطأ رقم : ...]) : (1) le hadith d'أسماء بنت عميس (ولادة محمد "
     "بن أبي بكر بالبيضاء), (2) le hadith عن عطاء أن عمر بن الخطاب كان يغتسل. Pour "
     "chaque hadith donne le NUMÉRO imprimé entre crochets."),
    ("p11-h3-h4", "p11-full.png",
     "Transcris exactement les DEUX hadiths imprimés sur cette page : (1) le hadith "
     "de عمر بن الخطاب et ليسي/ليلى (يصب على رأسي...) avec son numéro entre "
     "crochets [الموطأ رقم : ...], (2) le hadith التي أُتي رسول الله (حاجا أو "
     "معتمرا / إذا حنى اغتسل...) avec son numéro entre crochets."),
    ("p11-tarjamat", "p11-bottom.png",
     "Transcris exactement les DEUX notices biographiques (ترجمة) du bas de page : "
     "(1) عطاء بن أبي رباح (??), (2) عبد الله بن عمر بن الخطاب. Mot à mot tel "
     "qu'imprimé, y compris les années de naissance et de mort."),
    ("p12-tarjamat", "p12-top.png",
     "Transcris exactement les notices biographiques en haut de cette page (عبد "
     "الله بن عمر بن الخطاب, années de vie) et le bloc الشرح commençant par "
     "البَيْدَاء ثم طُوّى ثم الثنيّتان."),
    ("p12-ta-rif", "p12-full.png",
     "Transcris exactement le bloc 1- تعريف الحج (اللغة والاصطلاح) et le bloc 2- "
     "حكم الحج, y compris la citation coranique entre [ ] avec le nom de la sourate "
     "et le NUMÉRO de l'آية imprimé, et toute citation attribuée à ابن عرفة ou au "
     "شرح (avec les renvois [شرح ص : ...])."),
    ("p13-halat-1", "p13-full.png",
     "Transcris exactement le bloc « 1- الغسل للإحرام » : la définition, le hadith "
     "d'أسماء cité avec son numéro [الموطأ رقم : ...], la discussion du شارح (الآمر "
     "قاعدة, قوله «مرها»?, صحة إحرام الحائض والنفساء), puis le passage de الخطابي "
     "(في الحديث استحباب...). Mot à mot tel qu'imprimé."),
    ("p14-halat-2", "p14-full.png",
     "Transcris exactement le bloc « 2- غسل المحرم للجنابة أو للتبرد » : (a) la "
     "phrase d'الإجماع et le hadith d'ابن عباس et مُغيرة/مخرومة avec son numéro "
     "[الموطأ رقم : ...] ; (b) la discussion -ب غسل رأسه للتبرد, le hadith de ابن "
     "حنين عن أبي أيوب?? avec son numéro, le récit فَقُلْتُ: مَنْ هَذَا؟, et la "
     "phrase قول أبي أيوب: هكذا رأيت رسول الله يفعل. Transcris les NUMÉROS "
     "imprimés entre crochets."),
    ("p15-halat-3", "p15-top.png",
     "Transcris exactement le bloc « 3- غسل المحرم لدخول مكة » : la phrase sur "
     "الاغتسالات المستحبة, la citation de عائشة entre « » avec sa source entre [ ] "
     "(صحيح البخاري ou autre), puis le paragraphe خلاصة الدرس (الحج عبادة عظيمة...). "
     "Mot à mot tel qu'imprimé."),
    ("p15-taqwim", "p15-bottom.png",
     "Transcris exactement les QUATRE items d'évaluation (الاستدلال) numérotés 1- "
     "2- 3- 4- de cette page, y compris les deux cas de la question 4 (رجل أحرم ولم "
     "يغتسل / امرأة نفساء لم تغتسل لدخول مكة)."),
    ("p16-nass", "p16-full.png",
     "Transcris exactement : (1) le hadith d'ouverture قال يحيى: قال مالك: سمعت... "
     "(le texte sur العلم et le muḥrim qui se lave la tête au ghūsūl, à la pierre "
     "chaude?/الكداء, قتل القمل وإلقاء الشعر, حلقة التفث?) avec son numéro entre "
     "crochets [الموطأ رقم : ...] ; (2) les DEUX questions أقرأ النص ثم أجيب عن "
     "الواتي 1- 2- ; (3) le bloc أحفظ أحاديث الدرس المقبل وأجيب عن الآتي (الإعداد "
     "القبلي) : les 2 items."),
    ("p10-num1", "p10-nums.png",
     "Vois les crochets [الموطأ رقم : ...] de cette page. Quel NUMÉRO exact est "
     "imprimé dans CHAQUE crochet ? Réponds chiffre par chiffre (ex. 109, 309...). "
     "Regarde bien l'ordre des chiffres."),
    ("p14-nums", "p14-nums.png",
     "Quel NUMÉRO exact est imprimé dans chaque crochet [الموطأ رقم : ...] de "
     "cette page ? Réponds chiffre par chiffre pour chacun."),
]

for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    print(("OK  " if r.returncode == 0 else "FAIL") + f" {key}")

print("\n===== EXTRAITS =====")
for key, _, _ in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:900])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
