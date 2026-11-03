#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R543 — lectures VLM ciblées/ancrées leçon 9 hadith-2es (méthode R538/R541/R542)."""
import json
import os
import subprocess

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r543"
OUT = f"{HOME}/tr-tmp/vlm-r543"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭa' Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible. Si tu n'es pas sûr d'un mot, "
        "écris [illisible]. N'invente AUCUN texte, ne complète jamais de mémoire.")

ASKS = [
    ("p67-objectifs-aya", "p67-objectifs-intro-aya.png",
     "(1) Transcris les TROIS objectifs exactement. (2) Dans le paragraphe "
     "d'introduction, transcris la phrase «تلك القبلة التي قال عنها الحق سبحانه (...)» "
     "complète avec ce qui est entre parenthèses (citation en cursive). (3) Quel est le "
     "renvoi coranique imprimé juste après (سورة ... الآية ...) — chiffres exacts — et "
     "transcris le texte coranique imprimé en cursive mot à mot."),
    ("p67-hadith1-isnad", "p67-hadith1-isnad.png",
     "Transcris exactement l'isnād et le début du matn du hadith de cette zone (la "
     "couche lit : مالك عن إسحاق بن عبد الله بن أبي طلحة ... وأنه كان يقال له : مولى "
     "أبي طلحة ... سمع أبا ... الأنصاري صاحب النبي ... وكان ... يقول : والله ما أدري "
     "كيف أصنع بهذه ... وقد قال رسول الله). Transcris mot à mot ce que montre "
     "l'image, y compris les noms des transmetteurs et la fin de la zone."),
    ("p68-hadith1-num", "p68-hadith1-matn-num.png",
     "(1) Transcris mot à mot la fin du hadith et sa clôture [الموطأ رقم: ...] — "
     "chiffres exacts du numéro. La couche lit : «إذا ذهب أحدكم الغائط أو البول فلا "
     "يستقبل القبلة ولا يستدبرها بفرجه» [الموطأ رقم: ١٢٥]. (2) Puis transcris "
     "l'isnād du hadith suivant (la couche lit : مالك - عن عبد الله بن ... رأى بصاقاً "
     "في ...) et son matn jusqu'au numéro [الموطأ رقم: ٤٢٥] — chiffres exacts des "
     "deux numéros."),
    ("p68-hadith3-said", "p68-hadith3-said.png",
     "(1) Transcris l'isnād exact du hadith (la couche lit : مالك عن يحيى بن سعيد عن "
     "سعيد بن المسيب أنه قال). (2) Transcris le matn complet mot à mot — la couche "
     "lit : صلى رسول الله ... بعد أن قدم المدينة ستة عشر شهراً نحو بيت المقدس ثم "
     "حولت القبلة قبل بدر بشهرين [الموطأ رقم: ٧٢٥] — confirme ou corrige, chiffres "
     "exactes du numéro, et le mot rendu «بدر» tel qu'imprimé."),
    ("p68-hadith4-rawda", "p68-hadith4-rawda.png",
     "(1) Transcris l'isnād exact : la couche lit مالك عن عبد بن... عن الرحمن... عن "
     "حفص بن عاصم عن أبي هريرة أو عن أبي سعيد الخدري — confirme ou corrige mot à "
     "mot (y a-t-il deux chaînes alternatives avec «أو» ?). (2) Transcris le matn : "
     "«ما بين بيتي ومنبري روضة من رياض الجنة ومنبري على حوضي» [الموطأ رقم: ...] — "
     "chiffres exactes du numéro."),
    ("p69-hurayra-dates", "p69-bio-hurayra-dates.png",
     "Transcris exactement la fin de la biographie d'أبو هريرة : la couche lit : أسلم "
     "عام خيبر وقيل ... وشهد ... مع رسول الله ثم لازمه الملازمة التامة، توفي في سنة "
     "٩(...)... ودفن بالبقيع — transcris l'imprimé mot à mot, chiffres des années "
     "exactes (l'an de sa mort en hégire), et la phrase «وقيل غير ذلك» si présente."),
    ("p69-glossaire", "p69-glossaire-karais.png",
     "Transcris exactement les définitions imprimées : (1) الكراييس : المراحيض "
     "واحدها كرياس وقيل ... (la couche lit : وأما الغرف فتختص بمراحيض ... وأما "
     "مراحيض البيوت فإنما يقال لها الكثف) — transcris la définition complète mot à "
     "mot. (2) الغائط : أصله المكان المنخفض ... — transcris mot à mot."),
    ("p70-ibnumar", "p70-ibnumar-report.png",
     "Transcris mot à mot le hadith/rapport d'ابن عمر (la couche lit : لما رواه مالك "
     "عن ابن عمر رضي الله عنهما أنه كان يقول : «إن أناساً يقولون : إذا قعدت على "
     "حاجتك ...» puis des lexies garbled ... ومع ذلك يبقى ... [الموطأ رقم: ٣٢٥] ...) — "
     "transcris l'imprimé complet de ce rapport jusqu'au numéro, chiffres exactes."),
    ("p70-basaq-kama", "p70-basaq-kama.png",
     "(1) Transcris le début : la couche lit لا يبصق الإنسان في جهة القبلة لما لها من "
     "مكانة عظيمة باعتبارها الجهة التي ... «إذا كان ...» — transcris le matn entre "
     "guillemets exactement. (2) Transcris le hadith d'عائشة : «أن رسول الله رأى في "
     "جدار القبلة بصاقاً أو مخاطاً أو كامة فحكه» [الموطأ رقم: ...] — confirme ou "
     "corrige mot à mot, chiffres exactes du numéro."),
    ("p70-tahwil-isnad", "p70-tahwil-isnad.png",
     "Transcris exactement le paragraphe de تحويل القبلة : la couche lit كان النبي "
     "وأصحابه في مكة يتوجهون إلى بيت المقدس في صلاتهم واستمر الأمر كذلك بعد هجرته "
     "إلى المدينة ستة عشر شهراً وقيل سبعة عشر شهراً روى مالك في الموطأ عن ... عن سعد "
     "بن ... أنه قال «صلى رسول الله ...» — transcris l'isnād imprimé mot à mot (les "
     "noms entre مالك et أنا قال), et le début du matn."),
    ("p71-aya-tahwil", "p71-aya-tahwil.png",
     "(1) Transcris la phrase d'ouverture : la couche lit كل بعد أن قدم المدينة ست "
     "عشرة شهراً نحو بيت المقدس ثم حولت القبلة قبل بدر بشهرين [الموطأ رقم: ٧٢٥] — "
     "confirme, chiffres exactes. (2) Transcris la phrase ونزل قول ... puis la "
     "citation coranique imprimée en cursive mot à mot et son renvoi [سورة البقرة "
     "الآية: ...] chiffres exactes. (3) Transcris la phrase suivante والمقصود من هذا "
     "التحويل ... كما عُدَّ ذلك من خصائصه — mot à mot."),
    ("p71-fadl", "p71-fadl-muwatta-ahmad.png",
     "(1) Transcris le hadith : «صلاة في مسجدي هذا خير من ...» avec sa clôture "
     "[الموطأ رقم: ...] chiffres exactes. (2) Transcris le hadith d'عبد الله بن "
     "الزبير mot à mot : «صلاة في مسجدي هذا فضل من ألف صلاة فيما سواه من المساجد "
     "إلا المسجد الحرام وصلاة في المسجد الحرام ...» jusqu'à «في هذا» — et le renvoi "
     "imprimé [مسند أحمد ...] tel qu'imprimé."),
    ("p71-taqwim", "p71-taqwim.png",
     "Transcris exactement les TROIS questions du التقويم. La couche lit : ١- ما "
     "الحكمة من النهي عن استقبال القبلة عند قضاء الحاجة؟ ٢- أحدد أسباب تحويل القبلة. "
     "٣- أبين فضل الصلاة في المسجد النبوي — confirme ou corrige mot à mot."),
    ("p72-istinass", "p72-istinass-hadiths.png",
     "(1) Quel est le titre imprimé de cette section (la couche lit الاستئناس) ? "
     "(2) Transcris l'isnād et le matn du premier hadith : la couche lit عن عبد الله "
     "بن عمر أنه بلغه ... قال رسول الله : «لا تمنعوا إماء الله مساجد الله» [الموطأ "
     "رقم: ...] — chiffres exactes. (3) Transcris l'isnād et le matn du deuxième "
     "hadith : la couche lit عن بسر بن سعيد ... أن رسول الله قال : «إذا شهدت العشاء "
     "فلا تمسّنّ طيباً» [الموطأ رقم: ...] — confirme ou corrige mot à mot, chiffres "
     "exactes."),
    ("p72-maqasid-idad", "p72-maqasid-idad.png",
     "Transcris exactement : (1) les items numérotés المقصد/المقاصد qui suivent les "
     "hadiths — la couche lit seulement «-٢ المقصد من منع المرأة من الطيب حال خروجها "
     "للمسجد» — y a-t-il un item -١ avant ? Si oui, transcris-le exactement. (2) "
     "l'الإعداد القبلي complet : أحفظ أحاديث الدرس المقبل وأجيب عن الآتي : ١- أشرح : "
     "(transcris les lexies exactement — la couche lit حزبه من الليل - المعقلة - "
     "سجود القرآن - عزائم تجادل) ٢- أستخلص من أحاديث الدرس المقبل حكم مس القرآن "
     "وقراءته من غير وضوء. ٣- أبحث عن عدد سجدات التلاوة ومواضعها عند الإمام مالك."),
]

subprocess.run(["mkdir", "-p", OUT], check=True)
for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
    print(("✓" if r.returncode == 0 else "✗"), key)

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1400])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
