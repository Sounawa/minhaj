#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R1737-PAR — lectures VLM ciblées/ancrées leçon 10 hadith-2es (méthode R538/R541/R542/R543)."""
import json
import os
import subprocess

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-pdf11"
OUT = f"{HOME}/tr-tmp/vlm-pdf11"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭa' Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible. Si tu n'es pas sûr d'un mot, "
        "écris [illisible]. N'invente AUCUN texte, ne complète jamais de mémoire.")

ASKS = [
    ("p73-objectifs-intro", "p73-objectifs-intro.png",
     "(1) Transcris les objectifs numérotés de la page (١- ٢- ٣- ...) EXACTEMENT, "
     "tous, dans l'ordre. (2) Transcris le paragraphe d'introduction qui suit "
     "(la couche lit : أنزل الله عز وجل القرآن الكريم على قلب سيدنا محمد صلّى الله "
     "عليه وسلّم وتولى حفظه فقال سبحانه وتعالى) mot à mot, y compris la citation "
     "coranique imprimée en cursive et son renvoi [سورة الحجر الآية: ...] — "
     "chiffres EXACTS du renvoi. (3) Transcris la phrase interrogative qui clôt "
     "l'introduction (la couche lit : فما حكم الطهارة لمس المصحف وما أحكام سجود التلاوة)."),
    ("p73-hadith1-num", "p73-hadith1-num.png",
     "Transcris mot à mot l'isnād et le matn du hadith de cette zone : la couche lit "
     "مالك عن عبد الله بن أبي بكر بن حزم ... الكتاب الذي كتبه رسول الله صلّى الله عليه "
     "وسلّم إلى لعمرو بن حرم «أن لا يمس القرآن إلا طاهر» [الموطأ رقم: ...] — transcris "
     "l'imprimé EXACT, notamment : (a) le nom du destinataire tel qu'imprimé (لعمرو ؟ "
     "عامر ؟), (b) le contenu de la lettre entre guillemets, (c) le numéro du Muwaṭṭaʾ "
     "entre crochets — CHIFFRES EXACTS un par un (si les chiffres sont arabes "
     "orientaux, donne chaque chiffre)."),
    ("p74-hadith2-umar", "p74-hadith2-umar.png",
     "(1) Transcris l'isnād EXACT : la couche lit مالك عن داود بن الحصين عن الأعرج عن "
     "عبد الرحمن بن عبد القاري عن عمر بن الخطاب — confirme ou corrige mot à mot, y "
     "compris les vocatifs/vocalisations. (2) Transcris le matn complet : «من فاته "
     "حزبه من الليل فقرأه حين تزول الشمس فإنه لم يفته أو كأنه أدركه» [الموطأ رقم: ...] "
     "— confirme ou corrige, et donne le numéro du Muwaṭṭaʾ en CHIFFRES EXACTS un "
     "par un."),
    ("p74-hadith3-malik", "p74-hadith3-malik.png",
     "Transcris mot à mot le texte de cette zone : la couche lit قال يحيى قال مالك: "
     "«الأمر عندنا أن عزائم سجود القرآن إحدى عشرة سجدة، ليس في المفصل منها شيء» "
     "[الموطأ رقم: ...] — confirme ou corrige chaque mot (notamment الأمر عندنا، "
     "عزائم، إحدى عشرة سجدة، المفصل) et donne le numéro du Muwaṭṭaʾ en CHIFFRES "
     "EXACTS un par un."),
    ("p74-bio-amr-hazm", "p74-bio-amr-hazm.png",
     "Transcris EXACTEMENT la biographie (ترجمة الراوي) imprimée : la couche lit عمرو "
     "بن حزم: هو أبو الضحاك عمرو بن حزم بن زيد النجاري الخزرجي الأنصاري، استعمله رسول "
     "الله صلّى الله عليه وسلّم على أهل نجران ليفقههم في الدين ويعلم القرآن ويأخذ "
     "صدقاتهم، مات بالمدينة سنة إحدى وخمسين — confirme ou corrige mot à mot, "
     "notamment la kunyā (أبو الضحاك), le nasab, la mission (نجران, ليفقههم, ويعلم "
     "القرآن, ويأخذ صدقاتهم) et l'année de la mort (سنة إحدى وخمسين)."),
    ("p74-glossaire-extraction", "p74-glossaire-extraction.png",
     "Transcris exactement : (1) l'en-tête (الفهم والفهم ? الشرح ?) ; (2) les "
     "définitions : حزبه من الليل : ... / عزائم سجود القرآن : السجدات المؤكدات / "
     "تجادل : تحاجج وتدافع — la couche lit : ورده من القرآن الذي يقرؤه بالليل — "
     "confirme ou corrige chaque définition mot à mot. (3) les items numérotés de "
     "استخلاص المضامين : ١- أذكر حكم مس المصحف من غير وضوء. ٢- أستخرج من الأحاديث "
     "أحكام سجود التلاوة — confirme ou corrige."),
    ("p75-analyse-mushaf", "p75-analyse-mushaf.png",
     "Transcris mot à mot le début de la page (التحليل / أولا: حكم مس المصحف والقراءة "
     "منه من غير طهارة / ١- مس المصحف من غير طهارة) puis la phrase : la couche lit "
     "يدل كتاب رسول الله صلّى الله عليه وسلّم إلى لعمرو بن حزم رضي الله عنه في شأن "
     "القرآن الكريم أنه لا يجوز أن يمس القرآن محدثاً، وهو مذهب مالك رحمه الله تعالى — "
     "confirme ou corrige (notamment «محدثاً» et «وهو مذهب مالك»)."),
    ("p75-aya-waqia", "p75-aya-waqia.png",
     "Transcris mot à mot : (1) la phrase لقوله تعالى suivie de la citation coranique "
     "imprimée en cursive et son renvoi [سورة الواقعة الآية: ...] — CHIFFRES EXACTS "
     "du renvoi, et transcription complète de la citation coranique entre "
     "parenthèses/crochets ; (2) la phrase qui suit : la couche lit وهذا نهي وإن كان "
     "لفظه خبراً؛ لأن خبر الباري تعالى لا يكون بخلاف مخبره — confirme ou corrige "
     "chaque mot."),
    ("p75-exceptions", "p75-exceptions.png",
     "Transcris mot à mot les DEUX exceptions introduites par ويستثنى من ذلك : (1) la "
     "couche lit : معلم القرآن ومن يتعلمه، كبيراً أو صغيراً، للمشقة التي تلحقهما من "
     "تكرار المس عند التعليم — confirme ou corrige. (2) la couche lit : كتب التفسير "
     "والحديث والعلوم الشرعية تكتب فيها آيات القرآن متفرقة، فيجوز مسها من غير طهارة "
     "ولو لجنب أو حائض، لأن المقصود منها معاني القرآن، وليس تلاوته — confirme ou "
     "corrige."),
    ("p75-lecture-ibnabbas", "p75-lecture-ibnabbas.png",
     "Transcris mot à mot l'en-tête (٢- قراءة القرآن من غير وضوء) et le début du "
     "hadith : la couche lit لا يشترط فيمن يقرأ القرآن من حفظه أن يكون متوضئاً؛ لما "
     "رُوي عن عبد الله بن عباس رضي الله عنهما: «أنه بات ليلة عند ميمونة مولاة النبي "
     "صلّى الله عليه وسلّم وهي خالته...» — confirme ou corrige mot à mot (notamment "
     "ميمونة وهي خالته et le début du matn)."),
    ("p76-ibnabbas-suite", "p76-ibnabbas-suite.png",
     "Transcris mot à mot la fin du hadith d'ابن عباس : la couche lit فجلس يمسح النوم "
     "عن وجهه ثم قرأ العشر الآيات الخواتم من سورة آل عمران ثم قام إلى شن معلقة "
     "[أخرجه البخاري] — confirme ou corrige chaque mot (notamment شن معلقة et le "
     "renvoi entre crochets)."),
    ("p76-hukm-sajdah", "p76-hukm-sajdah.png",
     "Transcris mot à mot : (1) l'en-tête ثانيا: سجود تلاوة القرآن puis ١- حكمه ; "
     "(2) la phrase اختلاف المالكية (هل هو سنة أو فضيلة؟) ; (3) le hadith : la couche "
     "lit واستدلوا بما أخرجه البخاري: عن عطاء بن يسار أنه أخبره: أن زيد بن ثابت رضي "
     "الله عنه قرأ على النبي صلّى الله عليه وسلّم سورة النجم فلم يسجد فيها [صحيح "
     "البخاري] — confirme ou corrige mot à mot ; (4) la citation du dire d'عمر : la "
     "couche lit وقول عمر: «... من سجد فقد أصاب ...» — transcris le dire d'عمر "
     "EXACTEMENT tel qu'imprimé (chaque mot, même s'il paraît inhabituel)."),
    ("p76-adad-mawadi", "p76-adad-mawadi.png",
     "Transcris mot à mot : (1) l'en-tête ٢- عدد سجدات التلاوة ووقتها puis أ- عدد "
     "سجدات التلاوة ; (2) la phrase : la couche lit مذهب الإمام مالك وجمهور أصحابه "
     "وبه قال ابن عباس وابن عمر أن عدد السجدات في القرآن إحدى عشرة سجدة؛ ففي الموطأ "
     "قال الإمام مالك: «الأمر عندنا أن عزائم سجود القرآن إحدى عشرة سجدة...» — "
     "confirme ou corrige ; (3) l'en-tête ب- مواضع سجدات التلاوة et le début : la "
     "couche lit وهي التي ذكرها عبد الرزاق عن ابن جريج قال: «أخبرني عكرمة بن خالد أن "
     "سعيد بن جبير أخبره...» — confirme ou corrige (chaque nom : عبد الرزاق، ابن "
     "جريج، عكرمة بن خالد، سعيد بن جبير)."),
    ("p77-liste-sujud", "p77-liste-sujud.png",
     "Transcris mot à mot la liste des sourates imprimée dans cette zone : la couche "
     "lit فقالا: «الأعراف والرعد والنخل والإسراء ومريم والحج ... والفرقان وطس وألم "
     "تنزيل وص وحم عسق، إحدى عشرة سجدة، قالا: وليس في المفصل منها شيء» [مصنف عبد "
     "الرزاق] — transcris la liste EXACTEMENT comme imprimée, sourate par sourate, "
     "dans l'ordre, avec les mots d'ouverture entre guillemets s'ils y sont (طس ؟ "
     "ألم تنزيل ؟ هاء ميم ؟ أولها ؟), le décompte final (إحدى عشرة سجدة) et le renvoi "
     "[مصنف عبد الرزاق]."),
    ("p77-waqt-ruwayatan", "p77-waqt-ruwayatan.png",
     "Transcris mot à mot : (1) l'en-tête ج- وقت سجود التلاوة et la phrase d'accord "
     "des فقهاء et le désaccord (الأوقات التي تكون الصلاة فيها مكروهة، ولمالك روايتان) "
     "; (2) الرواية الأولى : la couche lit ثبت عنه في الموطأ أنه قال: «لا ينبغي لأحد "
     "يقرأ من سجود القرآن شيئاً بعد صلاة الصبح ولا بعد صلاة العصر» وذلك أن رسول الله "
     "صلّى الله عليه وسلّم نهى عن الصلاة بعد الصبح حتى تطلع الشمس وعن الصلاة بعد "
     "العصر حتى تغرب الشمس، والسجدة من الصلاة، فلا ينبغي لأحد أن يقرأ سجدة في تلك "
     "الساعتين [الموطأ رقم: ...] — confirme ou corrige, CHIFFRES EXACTS du numéro "
     "du Muwaṭṭaʾ ; (3) ووجه هذه الرواية ... ; (4) الرواية الثانية : la couche lit روى "
     "عنه ابن القاسم في المدونة: يسجد لها بعد الصبح ما لم تسفر، وبعد العصر ما لم تصفر "
     "الشمس — confirme ou corrige."),
    ("p77-taqwim", "p77-taqwim.png",
     "Transcris exactement les TROIS questions du التقويم. La couche lit : ١- أبين "
     "حكم مس القرآن بغير وضوء. ٢- أذكر مواضع السجدات التي أخذ بها الإمام مالك. ٣- ما "
     "هي الأوقات التي لا يجوز فيها سجود التلاوة؟ — confirme ou corrige mot à mot."),
    ("p78-istinass-hadith", "p78-istinass-hadith.png",
     "(1) Quel est le titre imprimé de cette section ? (2) Transcris la citation "
     "coranique du début avec son renvoi [سورة الواقعة الآية: ...] — CHIFFRES EXACTS, "
     "et la phrase d'introduction. (3) Transcris l'isnād et le matn du hadith : la "
     "couche lit عن الحارث بن هشام عن عائشة زوج النبي صلّى الله عليه وسلّم عن أبيه؟ "
     "عن عروة؟ — retranscris l'isnād EXACT tel qu'imprimé (ordre des noms), puis le "
     "matn complet : «أحياناً يأتيني مثل صلة الجرس وهو أشده عليّ فيفصم عني وقد وعيت "
     "ما قال، وأحياناً يتمثل لي الملك رجلاً فيكلمني فأعي ما يقول، قالت عائشة: ولقد "
     "رأيته ينزل عليه البرد الشديد فيفصم عنه وإن جبينه ليتفصد حرقاً» [الموطأ رقم: "
     "...] — confirme ou corrige chaque mot, CHIFFRES EXACTS du numéro."),
    ("p78-questions-idad", "p78-questions-idad.png",
     "Transcris exactement : (1) les questions numérotées après le hadith : ١- ما "
     "معنى قوله تعالى: «لا يمسه إلا المطهرون»؟ ٢- أستخرج من النص الثاني ما يدل على "
     "منزلة القرآن وعظمته — confirme ou corrige mot à mot. (2) l'الإعداد القبلي "
     "complet : أحفظ أحاديث الدرس المقبل وأجيب عن الآتي : ١- أشرح : (transcris les "
     "lexies EXACTEMENT — la couche lit : عدل عشر - رقاب من الشيطان - حرزاً "
     "يبتدرونها) ٢- أستخرج من أحاديث الدرس المقبل فضائل الذكر والدعاء — confirme ou "
     "corrige chaque lexie."),
    ("p79-full", "p79-full.png",
     "Cette page ouvre-t-elle une nouvelle leçon ? (1) Transcris l'en-tête "
     "(أهداف الدرس). (2) Transcris les objectifs numérotés. (3) Transcris la phrase "
     "d'introduction et le premier renvoi coranique avec ses chiffres exacts. (4) "
     "Indique si le mot ذكر/الدعاء y figure — le thème de cette page."),
]

subprocess.run(["mkdir", "-p", OUT], check=True)
for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
    print(("✓" if r.returncode == 0 else "✗"), key, (r.stderr or "").strip()[:120])

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1600])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
