#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R628 — lectures VLM ancrées leçon 4 hadith-3es (slot pdf-mut23h2x-393, p.31-38).
Méthode R624 (vlm-r624-l390.py) : question fermée ou ancrée par crop ; sortie
tr-tmp/vlm-r628/<key>.json. Jamais deviné : chaque chiffre (n° de hadith) et
chaque bloc brouillé par l'OCR est relu SUR L'IMAGE ; [illisible] admis ;
JAMAIS de complétion de mémoire. Si 429 → lectures d'image directes."""
import json
import subprocess

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r628"
OUT = f"{HOME}/tr-tmp/vlm-r628"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 3e année de l'enseignement collégial traditionnel). "
        "Réponds UNIQUEMENT à la question posée, par transcription EXACTE du texte "
        "imprimé visible. Si tu n'es pas sûr d'un mot, écris [illisible]. "
        "N'invente AUCUN texte, ne complète jamais de mémoire.")

ASKS = [
    ("p31-banniere", "ADJ-p31-banniere-900.png",
     "Transcris exactement le haut de cette page : (1) la bannière calligraphique "
     "de titre de leçon « الدرس ... : ... » avec son numéro ; (2) le badge circulaire "
     "numéroté s'il y en a un ; (3) le bloc أهداف الدرس avec les items numérotés "
     "1-, 2-, 3-, mot à mot tel qu'imprimé."),
    ("p31-objectifs-tamhid", "p31-full.png",
     "Transcris exactement : (1) le bloc أهداف الدرس (3 items) ; (2) le paragraphe "
     "تمهيد qui suit (من يسر الشريعة الإسلامية...) mot à mot ; (3) les questions "
     "d'ouverture (فما أنواع الإحرام...) ; (4) le premier hadith avec son isnād "
     "(مالك عن أبي الأسود...) et le numéro imprimé dans le crochet [الموطأ رقم : ...]."),
    ("p32-hadiths", "p32-full.png",
     "Transcris exactement les hadiths de cette page : (1) le hadith عن جعفر بن محمد "
     "عن أبيه أن المقدام بن الأسود دخل على علي (بالسقيا... بكرات... عثمان بن عفان "
     "ينهى...) avec le numéro entre crochets [الموطأ رقم : ...] ; (2) le hadith قال "
     "يحيى قال مالك من اعتملر في شوال... avec son numéro ; (3) le hadith مالك عن "
     "ابن شهاب عن عروة عن عائشة أنها كانت تقول... الصيام... بالعمرة إلى الحج... "
     "avec son numéro ; (4) la notice biographique ترجمة عائشة en bas de page, "
     "y compris l'année de décès (توفيت سنة ... أو ... ه)."),
    ("p33-gloses-mabhas", "p33-full.png",
     "Transcris exactement : (1) les quatre gloses du haut de page (يُحلوا، السُّقيا، "
     "ينجع بكرات، الخبط) mot à mot ; (2) le bloc استخلاص المضامين (2 items) ; "
     "(3) l'annonce أولا: الإفراد et le bloc 1- تعريف الإفراد وحكمه (الإفراد هو...) "
     "jusqu'à la re-citation du hadith d'عائشة."),
    ("p34-afdaliyya", "p34-full.png",
     "Transcris exactement : (1) la fin de la citation du hadith d'عائشة et la phrase "
     "أي فمنا من أهل بعمرة فقط...؛ (2) le bloc 2- أفضلية الإفراد على غيره : la phrase "
     "جاء في حديث الموطأ... كله بالحج، le hadith [الموطأ رقم : ...] des روايات "
     "(أن... الحج), la phrase ورجح الإفراد بالحج لأنه صح عن... avec les noms des "
     "compagnons cités ; (3) les arguments (أخذ الصحابة سياقا... ابن عمر... عائشة... "
     "ابن عباس... وبأن الخلفاء الراشدين واظبوا...) mot à mot ; (4) l'annonce ثانيا: "
     "القران et 1- تعريف القران وحكمه."),
    ("p35-qiran-dalil", "p35-full.png",
     "Transcris exactement : (1) le bloc دليل جوازه حديث أم المؤمنين عائشة وما رواه "
     "مالك عن جعفر بن محمد عن أبيه (المقدام/علي/عثمان... لبيك اللهم لبيك بحجة وعمرة "
     "معا) ; (2) le récit وعن مالك عن ابن شهاب عن محمد بن عبد الله بن الحارث بن "
     "نوفل... سعد بن أبي وقاص والضحاك بن قيس عام حج معاوية بن أبي سفيان... avec "
     "le numéro [الموطأ رقم : ...] ; (3) le paragraphe وفي قصة عثمان وعلي... من "
     "الفوائد ; (4) l'annonce 2- وقت إحلال المحرم بالقران et ses premières lignes."),
    ("p36-waqt-hukm", "p36-full.png",
     "Transcris exactement : (1) le bloc 2- وقت إحلال المحرم بالقران : la phrase من "
     "قرن بين الحج والعمرة..., le hadith «من كان معه هدي فليهلل بالحج مع العمرة ثم "
     "لا يحل حتى يحل منهما جميعا» avec son numéro [الموطأ رقم : ...], le hadith "
     "ولحديث أمنا عائشة «وأما من أهل بحج أو جمع الحج والعمرة...» avec son numéro ; "
     "(2) le bloc 3- حكم إدخال الحج والعمرة أحدهما على الآخر : اتفق الجمهور..., "
     "عن مالك أنه سمع بعض أهل العلم يقولون..., la citation de عبد الله بن عمر (إن "
     "صددت عن البيت... أشهدكم...) avec le numéro [الموطأ رقم : ...] et la suite "
     "(فإن طاف وصلى ركعتيه...)."),
    ("p37-tamattu", "p37-full.png",
     "Transcris exactement : (1) la fin de l'interdiction de مالك (وإنما لم يجز "
     "الإمام مالك إدخال العمرة على الحج...) ; (2) le bloc ثالثا: التمتع بالعمرة "
     "1- تعريف التمتع وحكمه (التمتع هو...) et la phrase de أبو عمر ابن عبد البر ; "
     "(3) le récit وعن... عن محمد بن عبد الله بن الحارث بن نوفل... سعد بن أبي "
     "وقاص والضحاك بن قيس... avec le numéro [الموطأ رقم : ...] ; (4) la phrase "
     "وروى الشيخان... عن أبي موسى ; (5) le paragraphe وقول سعد... يدل على أن فعل "
     "الرسول... et la phrase يستفاد من تعدد أنواع الإحرام..."),
    ("p38-isti-thmar", "p38-bas-idad-900.png",
     "Transcris exactement le bas de cette page : (1) les trois items du haut (أعرف "
     "أنواع الإحرام...) ; (2) le hadith de l'encadré (هو أمتمت الحج؟... المتعة... "
     "الصيام أو الهدي على من لم يجد... أهل مكة...) avec le numéro [الموطأ رقم : ...] ; "
     "(3) le bloc أتأمل النص وأجيب عن الآتي مع التعليل (2 questions) ; (4) le bloc "
     "أحفظ أحاديث الدرس المقبل وأجيب عن الآتي (الإعداد القبلي) : les 2 items."),
]

for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        print(("OK  " if r.returncode == 0 else "FAIL") + f" {key}")
        if r.returncode != 0:
            print(r.stderr[:200])
    except subprocess.TimeoutExpired:
        print(f"TIMEOUT {key}")

print("\n===== EXTRAITS =====")
for key, _, _ in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1200])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
