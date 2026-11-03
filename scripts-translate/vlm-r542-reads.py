#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R542 — lectures VLM ciblées/ancrées leçon 8 (méthode R538/R541)."""
import json
import subprocess

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r542"
OUT = f"{HOME}/tr-tmp/vlm-r542"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭa' Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible. Si tu n'es pas sûr d'un mot, "
        "écris [illisible]. N'invente AUCUN texte, ne complète jamais de mémoire.")

ASKS = [
    ("p60-matn1-dua", "p60-matn1-num.png",
     "(1) Transcris l'isnād du premier hadith exactement (la couche lit عن يحيى بن سعيد "
     "عن عمرو بن شعيب — y a-t-il aussi عن أبيه عن جده entre عمرو بن شعيب et le matn ?). "
     "(2) Transcris le matn complet (le duʿāʾ «اللهمّ ...») tel qu'imprimé. "
     "(3) Quel est le NUMÉRO entre crochets après الموطأ رقم ? chiffres exacts."),
    ("p60-matn2-rada", "p60-matn2-start.png",
     "Transcris exactement l'isnād du deuxième hadith (la couche lit : مالك عن عبد "
     "الله بن أبي بكر بن حزم أنه سمع عباد بن تميم) et le début du matn qui suit, "
     "mot à mot."),
    ("p61-malik-num", "p61-malik-quote.png",
     "(1) Transcris exactement la réponse de مالك à la question (commencant par "
     "ركعتان) — la couche lit : ركعتان ولكن يبدأ الإمام بالصلاة قبل الخطبة... ثم "
     "يخطب قائماً... — confirme ou corrige mot à mot. (2) Y a-t-il un NUMÉRO entre "
     "crochets [الموطأ رقم: ...] dans cette zone ? Si oui, chiffres exacts."),
    ("p61-matn3-rain", "p61-matn3-rain.png",
     "(1) Transcris l'isnād du hadith de la pluie (la couche lit عن عتبة بن مسعود — "
     "y a-t-il d'autres noms ?). (2) Transcris le matn exactement : صلاة الصبح "
     "بالحديبية على إثر سماء من الليل... puis la question لعلكم تذكرون آية... puis "
     "أصبح من عبادي مؤمن بي وكافر... (3) le numéro [الموطأ رقم: ...] chiffres exacts."),
    ("p62-anas-hadith", "p62-anas-hadith.png",
     "Transcris mot à mot le hadith d'Anas (la couche lit : أصابت الناس سنة على عهد "
     "رسول الله... قام أعربي في يوم الجمعة... يا رسول الله هلك المال...) jusqu'au "
     "renvoi [صحيح البخاري]."),
    ("p63-hukm-suras", "p63-hukm-malik.png",
     "(1) La couche lit : ويندب أن يقرأ في الأولى بالفاتحة وسبح اسم ربك الأعلى وفي "
     "الثانية بالفاتحة وسورة الغاشية أو والشمس وضحاها — confirme ou corrige mot à "
     "mot. (2) Le mot/groupe après وإذا قرأ بأي سورة : la couche lit «أحهز أقهد» — "
     "que dit l'image exactement ?"),
    ("p63-malik-requote", "p63-khutba-malik.png",
     "Transcris exactement la re-citation de مالك en la section de la khutba — la "
     "couche lit : ثم يخطب قائماً ويدعو... ويجهر في الركعتين بالقراءة، وويلو/ويلف "
     "رداءه حين يستقبل... — confirme ou corrige mot à mot."),
    ("p64-dua-anas", "p64-dua-anas.png",
     "Transcris mot à mot le duʿāʾ d'Anas cité ici — la couche lit : رفع رسول الله "
     "كل يديه ثم قال «اللهمّ أعتْنَاء...» — que dit l'image exactement (أغثنا ? "
     "أعطنا ? autre ?), et quels mots suivent ?"),
    ("p64-p65-abbas", "p64-adab4-umar.png",
     "Transcris mot à mot la phrase garbled de la couche : la couche lit des lexies "
     "éparses (أكرحه الخاری کے هة کن أس بن مالك أن عفر ن الخطاب...) — transcris "
     "exactement ce que montre l'image en ces deux lignes."),
    ("p65-abbas-dua", "p65-abbas-dua.png",
     "Transcris mot à mot le duʿāʾ d'ʿUmar/al-ʿAbbās cité ici — la couche lit : "
     "«اللهمّ إنّا كنا نتبيَّنا إليك بنبيِّنا... وإنا [نتوسل؟] بعم نبينا فاسقنا» — "
     "confirme ou corrige exactement, jusqu'à فيسقون [صحيح البخاري]."),
    ("p65-taqwim-q2", "p65-taqwim.png",
     "Transcris exactement les TROIS questions du التقويم. La couche lit la 2e : "
     "«قاين كيفية صيلاة الاستمقاء» — que dit l'image exactement pour la 2e question ?"),
    ("p65-istithmar", "p65-istithmar.png",
     "(1) Transcris l'isnād exact (la couche lit مالك عن إسحاق بن عبد الله بن أبي "
     "فروة — confirme). (2) Transcris le matn mot à mot (جاء رجل إلى رسول الله... "
     "ملكت المواشي وتقطعت السبل... فدعا... فمطرنا من الجمعة إلى الجمعة... فجاء رجل... "
     "اللهم على ظهور الجبال وبطون الآكام ومنابت الأودية...) jusqu'au numéro. "
     "(3) Le numéro [الموطأ رقم: ...] chiffres exacts."),
    ("p65-exercice-malik", "p65-exercice.png",
     "Transcris exactement : (1) la remarque de مالك qui suit le hadith (la couche "
     "lit : قال مالك: هو من ذلك في سعة إن شاء الله أو في المسجد أو في بيته إذا رجع) "
     "— confirme ou corrige ; (2) le bloc d'exercices (la couche lit : ١- أستخرج... "
     "٢- ماذا يفعل من أدرك خطبة الاستسقاء ولم يدرك الصلاة؟) — que dit exactement la "
     "question 1 ?"),
    ("p66-iqdad", "p66-iqdad.png",
     "Transcris exactement l'الإعداد القبلي (la couche lit : أحفظ أحاديث الدرس "
     "القادم وأجيب عن الآتي : ١- أستخرج من أحاديث الدرس المقبل آداب القبلة. ٢- "
     "أبحث عن السبب في تحويل القبلة) — confirme ou corrige mot à mot."),
]

subprocess.run(["mkdir", "-p", OUT], check=True)
for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
    print(("✓" if r.returncode == 0 else "✗"), key)

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1300])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
