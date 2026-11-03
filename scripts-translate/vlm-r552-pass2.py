#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R552 — 2e passe VLM : crops ciblés 800-1000 dpi, points litigieux leçon 14 (pdf-15).
Chaque ambiguïté (matns, isnāds, numéros Muwaṭṭaʾ, lexies) est tranchée par preuve image."""
import fitz
import json
import os
import subprocess
import time

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = f"{HOME}/tr-tmp/qa-crops-r552"
OUT = f"{HOME}/tr-tmp/vlm-r552"
os.makedirs(OUT, exist_ok=True)

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible, token par token. Si tu n'es "
        "pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne "
        "complète JAMAIS de mémoire (n'utilise PAS de version canonique du hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

doc = fitz.open(PDF)

def crop(page_no, y0f, y1f, dpi, name, x0f=0.04, x1f=0.96):
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{CROPS}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")

# --- crops ciblés ---
crop(98, 0.02, 0.22, 900, "r2-p98-objectifs")
crop(98, 0.20, 0.50, 900, "r2-p98-tamhid")
crop(98, 0.48, 0.85, 900, "r2-p98-t1")
crop(99, 0.00, 0.32, 900, "r2-p99-t2")
crop(99, 0.28, 0.58, 900, "r2-p99-t3")
crop(99, 0.54, 0.84, 900, "r2-p99-bio")
crop(99, 0.76, 1.00, 900, "r2-p99-sharh")
crop(100, 0.12, 0.62, 800, "r2-p100-sifa")
crop(100, 0.52, 0.80, 900, "r2-p100-sad")
crop(100, 0.70, 1.00, 900, "r2-p100-uthman")
crop(101, 0.00, 0.16, 900, "r2-p101-uthman")
crop(101, 0.10, 0.62, 800, "r2-p101-naql")
crop(101, 0.56, 1.00, 800, "r2-p101-adab1")
crop(102, 0.00, 0.22, 900, "r2-p102-adab1fin")
crop(102, 0.16, 0.60, 800, "r2-p102-item2")
crop(102, 0.58, 1.00, 800, "r2-p102-item3")
crop(103, 0.00, 0.55, 800, "r2-p103-items45")
crop(103, 0.48, 0.95, 800, "r2-p103-taq-istith")
crop(104, 0.02, 0.45, 900, "r2-p104-iedad")

ASKS = [
    ("r2-p98-objectifs", "r2-p98-objectifs.png",
     "Transcris le titre et les TROIS objectifs numérotés, mot à mot. Point fermé sur "
     "l'objectif 3 : ses derniers mots sont-ils (a) ودفنه (b) وتلقيه (c) autre — "
     "transcris exactement les derniers tokens de l'objectif 3."),
    ("r2-p98-tamhid", "r2-p98-tamhid.png",
     "Transcris le paragraphe du tamhīd ENTIER (de حتّى الإسلام jusqu'à la question "
     "finale), y compris le hadith d'Abū Hurayra entre guillemets TOKEN PAR TOKEN et "
     "son renvoi entre crochets [مصنف ابن أبي شيبة ...] complet. Point fermé : le "
     "matn contient-il «فإن شهد دفنها كان له قيراطان: القيراط مثل جبل أُحد» ? "
     "Transcris la fin du matn exactement comme imprimée."),
    ("r2-p98-t1", "r2-p98-t1.png",
     "Transcris le premier hadith ENTIER : l'isnād (مالك عن ... — le mot après من "
     "est-il ثقاته ? transcris-le), le matn entre guillemets token par token (les "
     "noms : سعد بن أبي وقاص وسعيد بن زيد بن عمرو بن نفيل ?), et le renvoi "
     "[الموطأ رقم : N] CHIFFRE PAR CHIFFRE tel qu'imprimé."),
    ("r2-p99-t2", "r2-p99-t2.png",
     "Transcris ce hadith ENTIER : isnād (مالك عن محمد بن ... بن ... عن ... — "
     "chaque nom exact), matn entre guillemets token par token (commence-t-il par "
     "لا يموت أحد من المسلمين ? y a-t-il ثلاثة من الولد ? le verbe après : "
     "فَيَحْسُبُهُم / فَيَحْتَسِبُهُم / autre ?), la question de la femme (يا رسول "
     "الله أو اثنان ?) et la réponse (أو اثنان ?), et le renvoi [الموطأ رقم : N] "
     "chiffre par chiffre."),
    ("r2-p99-t3", "r2-p99-t3.png",
     "Transcris ce hadith ENTIER token par token : l'isnād (مالك عن أبي الرجال "
     "محمد بن عبد الرحمن عن أمه عمرة بنت عبد الرحمن ... عن عائشة ? — transcris "
     "exactement ce qui est imprimé entre عن أمه et لعن), puis le matn : QUI le "
     "Prophète ﷺ a-t-il maudit — transcris les mots exacts entre لعن رسول الله et "
     "يعني, puis ce qui suit يعني (نباش القبور ? transcris). Points fermés : "
     "(a) le premier mot maudit ressemble-t-il à المُخَنَّثِينَ / المُخْتَفِيَاتِ / "
     "autre ? (b) le deuxième à المُتَرَجِّلَاتِ / المُخْتَنِقَة / autre ? (c) la "
     "glose يعني est-elle نبّاش القبور ? Transcris tout exactement. Enfin le renvoi "
     "[الموطأ رقم : N] chiffre par chiffre."),
    ("r2-p99-bio", "r2-p99-bio.png",
     "Transcris l'encadré ترجمة الراوي ENTIER mot à mot : le nom (عمرة بنت عبد "
     "الرحمن بن سعد بن زرارة الأنصارية المدنية التابعية ?), les jugements (Ibn "
     "Maʿīn, al-ʿIǧlī, Abū Ḥassān az-Ziyādī), l'année de mort EN CHIFFRES (ثمان "
     "وتسعين ?) et l'âge (بنت سبع وتسعين ?) — chiffre par chiffre tel qu'imprimé."),
    ("r2-p99-sharh", "r2-p99-sharh.png",
     "Transcris le bloc الشرح ENTIER mot à mot (les gloses imprimées, séparées par "
     "leurs termes définis : العَقيق : ... ? / [autre terme] : ... ? / جنة من "
     "النار : ... ?). Point fermé : la première glose est-elle العَقيق : موضع قرب "
     "المدينة ? Transcris chaque glose exactement."),
    ("r2-p100-sifa", "r2-p100-sifa.png",
     "Transcris le paragraphe صفة الدفن TOKEN PAR TOKEN depuis يندب jusqu'à "
     "الأقدام. Points fermés : (a) le mot après ويستر على فم القبر est-il بثوب ? "
     "(b) après ويقول من يتولى : إضجاعه / إضعاه / autre ? (c) la série après "
     "بسم الله وعلى سنة رسول الله ﷺ : ويُعدَّل رجله برفق / autre ? (d) la phrase "
     "près de la fin : في سهولة وتقريق / في سهولة وفرق / autre ? et دون ذلك "
     "الأرض وقبورها / autre ? Transcris tout exactement."),
    ("r2-p100-sad", "r2-p100-sad.png",
     "Transcris TOKEN PAR TOKEN le hadith de Saʿd : l'isnād (عامر بن سعد بن أبي "
     "وقاص عن أبيه ? transcris exactement) et le matn entre guillemets (الحدوا لي "
     "لحدًا وأصبوا عليّ اللبن نصبًا كما صنع برسول الله ﷺ ?) et le renvoi entre "
     "crochets complet [صحيح مسلم ?]."),
    ("r2-p100-uthman", "r2-p100-uthman.png",
     "Transcris TOKEN PAR TOKEN la fin du paragraphe (فإذا فرغ الناس من الدفن "
     "يندب أن يبقى أحدهم ...) et le hadith d'ʿUthmān b. ʿAffān tel qu'il "
     "commence (كان النبي ﷺ ...)."),
    ("r2-p101-uthman", "r2-p101-uthman.png",
     "Transcris TOKEN PAR TOKEN le hadith d'ʿUthmān : la suite (إذا فرغ من دفن "
     "الميت وقف عليه فقال ...), le matn entre guillemets (استغفروا لأخيكم "
     "وسلوا له التثبيت فإنه الآن يُساءَل ?) et le renvoi [سنن أبي داود ?] "
     "exactement."),
    ("r2-p101-naql", "r2-p101-naql.png",
     "Transcris TOKEN PAR TOKEN la section 2- حكم نقل الميت avant الدفن : le "
     "titre, le premier paragraphe (يجوز نقل الميت من مكان إلى آخر ... — le mot "
     "après إذا كانت : تترتب / نترتب ?), la citation du hadith (إن سعد بن أبي "
     "وقاص ...) et son renvoi [الموطأ رقم : N] chiffre par chiffre, puis le "
     "paragraphe de divergence (واختلف في جواز نقل الميت من بلد إلى بلد ... "
     "jusqu'à غرض راجح) — le mot avant غرض راجح : هناك / هتك / autre ? et la "
     "phrase الأخرى : والأولى تفصيل ذلك على حالين / تنزيل / autre ? Transcris "
     "tout exactement."),
    ("r2-p101-adab1", "r2-p101-adab1.png",
     "Transcris TOKEN PAR TOKEN : le titre ثانيا (complet — من الآداب المتعلقة "
     "بالجنازة ? autre ?), la phrase d'introduction (هناك مجموعة من الآداب ...), "
     "le titre de l'item 1 (عدم البكاء والنياحة عليه ?), le paragraphe (يحرم "
     "البكاء المصحوب برفع الصوت والنياحة على الميت ولطم الخدود وشنق الجيوب ?) "
     "et le DÉBUT du hadith de جابر (لما جاء في الموطأ عن حديث جابر بن ... — le "
     "nom après بن : عتيك / عبد الله / autre ? puis أن رسول الله ﷺ جاء ... "
     "عبد الله بن ثابت ...) jusqu'à la fin de page."),
    ("r2-p102-adab1fin", "r2-p102-adab1fin.png",
     "Transcris TOKEN PAR TOKEN la fin du hadith de جابر : depuis ﷺ (قال: دعْهن "
     "فإذا وجب فلا ... — le mot après فلا : تبك / تتكلموا / autre ? et ce qui "
     "suit : عليه باكية / باكتين / autre ?), la question (قالوا: يا رسول الله "
     "وما الوجوب ?) et la réponse (قال: إذا مات ?), le renvoi [الموطأ رقم : N] "
     "chiffre par chiffre, et la glose (ومعنى ... بالبكاء) complète."),
    ("r2-p102-item2", "r2-p102-item2.png",
     "Transcris TOKEN PAR TOKEN l'item 2 entier : titre (التصبـر والرضا بما قدَر "
     "الله ?), paragraphe, la citation coranique ﴿...﴾ et son renvoi [سورة البقرة "
     "الآية: N] CHIFFRE PAR CHIFFRE, le hadith d'أم سلمة (isnād + matn complet "
     "dont اللهم أْجُرْني في مصيبتي وأَعْقِبْني خيرًا منها / وأخلف لي / autre ? "
     "et إلا فعل الله ذلك به ?), le renvoi [الموطأ رقم : N] CHIFFRE PAR "
     "CHIFFRE (638 ou 658 ? écris chaque chiffre séparément), puis le paragraphe "
     "final et la citation «لا يموت لأحد من المسلمين ثلاثة من الولد ...» avec la "
     "question et réponse (أو اثنان ?)."),
    ("r2-p102-item3", "r2-p102-item3.png",
     "Transcris TOKEN PAR TOKEN l'item 3 entier : titre (الإسراع بالميت ?), le "
     "paragraphe (من السنة الإسراع بالميت إلى قبره إكراما له، ويكون إسراعا ... — "
     "le mot après إسراعا : خفيفا / حفيفا / autre ? la phrase suivante : فوق "
     "المتوسط / فوق المرشى / autre ? et plus loin : باتفاق العلماء / بانتفاء "
     "العلماء / autre ?), l'isnād (عن نافع، عن أبي هريرة / أن أبا هريرة ?) et "
     "le matn (أسرِعوا بجنازتكم / أسرعوا بجنازتكم / autre ? ... خير تقدمونه "
     "إليه / عليه ?) et le renvoi [الموطأ رقم : N] chiffre par chiffre."),
    ("r2-p103-items45", "r2-p103-items45.png",
     "Transcris TOKEN PAR TOKEN les items 4 et 5 : titres (عدم القعود على قبره ? "
     "وعدم نبش قبره أو كسر عظامه ?), le hadith de l'item 4 entre guillemets (لا "
     "تجلسوا على القبور وَلا تصلوا إليها ? ou autre formulation) et son renvoi "
     "[صحيح مسلم ?], le paragraphe de l'item 5 (يحرُم نبش القبر احتراما "
     "لصاحبه...), la citation ففي حديث الدرس : «لعن رسول الله ...» avec la "
     "glose يعني (نبّاش القبور ?), et le hadith d'عائشة (ففي الموطأ عن مالك "
     "أنه بلغه أن عائشة زوج النبي ﷺ كانت تقول : «كَسْرُ عَظْمِ الميت ...» — "
     "transcris le matn exactement : كَثُر عظم الميت / كَسْر عظم الميت / autre ? "
     "et la suite : كَكَسْره وهو حي / كَثُر وهو حي / autre ? et la glose "
     "تَعْني في الإثم ?) et le renvoi [الموطأ رقم : N] chiffre par chiffre."),
    ("r2-p103-taq-istith", "r2-p103-taq-istith.png",
     "Transcris TOKEN PAR TOKEN : le bloc التقويم (titre + les questions "
     "numérotées), le bloc الاستثمار (titre + l'isnād complet du hadith de علي بن "
     "أبي طالب — مالك عن يحيى بن سعيد عن ... chaque nom — + le matn entre "
     "guillemets exactement (كان يقوم في الجنازة ثم جلس بعد ?) + le renvoi "
     "[الموطأ رقم : N] chiffre par chiffre), et la ligne finale (أراجع شرح "
     "الزرقاني للحديث وأبين أقوال الفقهاء في حكم الوقوف للجنازة ?)."),
    ("r2-p104-iedad", "r2-p104-iedad.png",
     "Transcris TOKEN PAR TOKEN le bloc الإعداد القبلي ENTIER : le titre, la "
     "phrase d'introduction (أحفظ أحاديث الدرس المُقبل وأجيب عن الآتي ? — "
     "transcris exactement), l'item 1 et SES TROIS LEXIES (أشرح : ... — chaque "
     "lexie exactement telle qu'imprimée, séparées : الحصيد ? العذوق ? الوسيق ? "
     "أوسق ? خس نود ? أولاق ? — écris chaque mot séparément), et l'item 2 "
     "entier (أعرف الزكاة / الزكاء ? وأبين حكمها وشروطها ?)."),
]

def vision_call(prompt, img, out, tries=6):
    cmd = ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out]
    for t in range(tries):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0:
            return True, ""
        err = (r.stderr or "") + (r.stdout or "")
        if "429" in err or "Too many" in err:
            wait = 40 + 25 * t
            print(f"  429 — attente {wait}s (tentative {t + 1}/{tries})")
            time.sleep(wait)
            continue
        return False, err[:200]
    return False, "429 persistant"

for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    ok, err = vision_call(f"{BASE}\nQUESTION : {q}", f"{CROPS}/{img}", out)
    print(("✓" if ok else "✗"), key, err)

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:3500])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
