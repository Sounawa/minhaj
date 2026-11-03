#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R552 — 2bis passe VLM : micro-crops 1000 dpi lettre-niveau sur les points restés
ambigus après les passes 1-2 (leçon 14, pdf-15). L'image tranche, jamais deviné."""
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
        "par transcription EXACTE du texte imprimé visible, token par token, LETTRE PAR "
        "LETTRE pour les mots interrogés. Si tu n'es pas sûr, écris [illisible]. "
        "N'invente AUCUN texte, ne complète JAMAIS de mémoire, ne corrige pas l'imprimé "
        "même s'il te paraît fautif ou étrange — transcris-le tel quel.")

doc = fitz.open(PDF)

def crop(page_no, y0f, y1f, dpi, name, x0f=0.04, x1f=0.96):
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{CROPS}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")

crop(98, 0.00, 0.13, 1000, "r3-p98-title")
crop(98, 0.20, 0.45, 1000, "r3-p98-obj")
crop(98, 0.40, 0.68, 900, "r3-p98-tamhid")
crop(98, 0.60, 0.86, 1000, "r3-p98-t1")
crop(99, 0.00, 0.16, 1000, "r3-p99-t2")
crop(99, 0.26, 0.54, 1000, "r3-p99-t3")
crop(99, 0.50, 0.80, 900, "r3-p99-bio")
crop(100, 0.44, 0.66, 1000, "r3-p100-sad")
crop(100, 0.62, 0.86, 1000, "r3-p100-fin")
crop(101, 0.00, 0.15, 1000, "r3-p101-uthm")
crop(101, 0.74, 0.98, 1000, "r3-p101-jabir")
crop(102, 0.00, 0.16, 1000, "r3-p102-latabki")
crop(102, 0.26, 0.55, 1000, "r3-p102-ummsal")
crop(102, 0.60, 0.86, 1000, "r3-p102-item3")
crop(103, 0.16, 0.52, 900, "r3-p103-t3bones")
crop(104, 0.05, 0.30, 1000, "r3-p104-lex")

ASKS = [
    ("r3-p98-title", "r3-p98-title.png",
     "Transcris LETTRE PAR LETTRE l'en-tête de leçon complet : les mots après "
     "أحكام الجنائز (séparés par des tirets) — القبر والدفن ? الغسل والكفن ? "
     "autre ? Puis le numéro du الدرس."),
    ("r3-p98-obj", "r3-p98-obj.png",
     "Transcris mot à mot la liste أهداف الدرس. Point fermé LETTRE PAR LETTRE sur "
     "l'objectif 3 : ses derniers mots — (a) ودفنه (b) وتلقيه (c) وتلقييه (d) "
     "autre ? Transcris les 4 derniers tokens de l'objectif 3 exactement."),
    ("r3-p98-tamhid", "r3-p98-tamhid.png",
     "Transcris TOKEN PAR TOKEN le hadith du tamhīd (entre guillemets) : «من صلى على "
     "جنازة ...» jusqu'à la fin du matn, puis le renvoi entre crochets [مصنف ابن "
     "أبي شيبة كتاب الجنائز باب ...] COMPLET, puis la question finale (فما هي "
     "أحكام الدفن وما آداب الجنازة ?). Point fermé : la fin du matn après "
     "قيراطان — deux-points puis القيراط مثل جبل أُحد ? transcris exactement."),
    ("r3-p98-t1", "r3-p98-t1.png",
     "Transcris LETTRE PAR LETTRE l'isnād du premier hadith : مالك، عن غير واحد "
     "[SUITE EXACTE — ممن يثق به ? من ثقاته ? autre ?] puis le matn et le renvoi "
     "[الموطأ رقم : N] chiffre par chiffre."),
    ("r3-p99-t2", "r3-p99-t2.png",
     "Transcris LETTRE PAR LETTRE l'isnād complet : مالك، عن محمد بن أبي بكر بن "
     "[?]، عن [? — أبي النضر ? أبيه ?] [السلامي ? السلمي ? autre ?]. Puis le "
     "début du matn exactement (لا يموت ... فيحتسبهم ?)."),
    ("r3-p99-t3", "r3-p99-t3.png",
     "Transcris LETTRE PAR LETTRE : (1) ce qui est imprimé entre عن أمه عمرة بنت "
     "عبد الرحمن et تقول (أنها سمعت ? عنه سمعتها ? Le nom عائشة apparaît-il ?) ; "
     "(2) les DEUX mots maudits entre لعن رسول الله ﷺ et la ponctuation — écris "
     "chaque mot lettre par lettre (المختفي ? المخنثي ? المختنقة ? المخنثات ? "
     "autre ?) ; (3) la glose après يعني (نباش القبور ?) ; (4) le renvoi [الموطأ "
     "رقم : N] chiffre par chiffre."),
    ("r3-p99-bio", "r3-p99-bio.png",
     "Transcris mot à mot l'encadré ترجمة الراوي (عمرة بنت عبد الرحمن ...) ENTIER "
     "y compris les jugements et les années (chiffres en toutes lettres). S'il y a "
     "une rubrique الحكم ou الشرح visible, transcris-la aussi."),
    ("r3-p100-sad", "r3-p100-sad.png",
     "Transcris TOKEN PAR TOKEN le hadith de Saʿd : la formule d'introduction (ففي "
     "صحيح مسلم عن [عامر بن سعد بن أبي وقاص ? عن أبيه ?]), le matn entre "
     "guillemets LETTRE PAR LETTRE (الحدوا لي لحدًا ? ائتوا لي بلبنًا ? وأصبوا "
     "عليّ اللبن نصبًا ? كما صُنع برسول الله ﷺ / كما صنع به رسول الله ﷺ ?) et le "
     "renvoi [صحيح مسلم]."),
    ("r3-p100-fin", "r3-p100-fin.png",
     "Transcris TOKEN PAR TOKEN les phrases : (1) ثم [يصب ? يبسط ?] التراب على "
     "القبر في سهولة [وما suit EXACTEMENT : وتقريق ? وتفريج ? وفرق ? autre ?] "
     "(2) [دون ? دون ذلك ?] [دك ? ذلك ?] الأرض و[قبورها ? قرعها ? عقرها ?] بشدة "
     "بالأقدام (3) فإذا فرغ الناس من الدفن يندب أن يبقى أحدهم [قريبا من رأس "
     "القبر ? عند القبر ?] ويدعو للميت بالمغفرة و[التثبيت ? الثبات ?] عند "
     "[السؤال ?]. Transcris tout exactement."),
    ("r3-p101-uthm", "r3-p101-uthm.png",
     "Transcris TOKEN PAR TOKEN le hadith d'ʿUthmān : على la première ligne "
     "visible (عَلَيْهِ وَسَلَّمَ إِذَا فَرَغَ ...) et le matn entre guillemets "
     "LETTRE PAR LETTRE : استغفروا [لأخيكم ?] و[سلوا ? أسألوا ?] له [التثبيت ? "
     "التثبيتَ ?]، فإنه الآن [يُساءَل ? يُسأل ?] — puis le renvoi entre "
     "crochets [سنن أبي داود ?] exactement (visible en rouge)."),
    ("r3-p101-jabir", "r3-p101-jabir.png",
     "Transcris TOKEN PAR TOKEN le début du hadith de جابر : لما جاء في الموطأ "
     "[من ? عن ?] حديث جابر بن [عتيك ? عبد الله ? autre ?]، أنَّ رسول الله ﷺ "
     "جاء [بعوض ? يعود ? autre ?] [عبد الله بن ثابت ?] — puis ce qui suit "
     "jusqu'à la fin visible (فوجده قد غلب عليه... فاسترجع... غُلبنا عليك يا "
     "أبا الربيع ?). LETTRE PAR LETTRE sur le nom après جابر بن."),
    ("r3-p102-latabki", "r3-p102-latabki.png",
     "Transcris TOKEN PAR TOKEN la fin du hadith : ﷺ [قال :] دعْهن فإذا وجب فلا "
     "[LE VERBE EXACT : تبك ? تتكلموا ? تنكّن ? autre ?] [عليه ?] [باكية ? "
     "باكتين ? autre ?]. Puis قالوا : يا رسول الله وما الوجوب ? قال : «إذا "
     "مات». Puis le renvoi [الموطأ رقم : N] chiffre par chiffre. Puis la glose : "
     "ومعنى [la phrase exacte : لا تبك باكية ? لا تنكّن باكية ?] : لا [ترفع ? "
     "نرفع ?] صوتها بالبكاء."),
    ("r3-p102-ummsal", "r3-p102-ummsal.png",
     "Transcris TOKEN PAR TOKEN le hadith d'أم سلمة : (1) le matn : ... اللهم "
     "[أْجُرْني ? أوجرني ?] في مصيبتي، وأعقبني [خيرًا ? خيرا ?] منها، [إلا ? "
     "آلا ?] [فعل الله ذلك به ? autre chose ?] ; (2) la parole d'أم سلمة : "
     "فلما توفي أبو سلمة قلت ذلك... فأعقب[ني ? ها ?] الله [رسولَه ? رسوله ?] "
     "فتزوج[ته ? ها ?] ; (3) LE RENVOI [الموطأ رقم : N] CHIFFRE PAR CHIFFRE — "
     "le chiffre du milieu est-il 3 ou 5 ? écris chaque chiffre séparément ; (4) "
     "le renvoi de la citation coranique [سورة البقرة الآية : N] chiffre par "
     "chiffre s'il est visible."),
    ("r3-p102-item3", "r3-p102-item3.png",
     "Transcris TOKEN PAR TOKEN l'item 3 : (1) ويكون إسراعا [LE MOT EXACT : "
     "خفيفا ? حفيفا ? autre ?] ; (2) بحيث لا [يشق ? يثقل ?] على [ضعفة ? ضعفاء ?] "
     "من يتبعها ; (3) والأمر للاستحباب [LE MOT EXACT : باتفاق ? بانتفاء ? "
     "بانتفاق ?] العلماء ; (4) le matn : أسر[ع]وا [بجنازتكم ? بالجنازة ?]، "
     "فإنما هو خير [تقدمونه إليه ? عليه ?]، أو شر [تضعونه ? تقدمونه ?] عن "
     "رقابكم ; (5) le renvoi [الموطأ رقم : N] chiffre par chiffre."),
    ("r3-p103-t3bones", "r3-p103-t3bones.png",
     "Transcris TOKEN PAR TOKEN : (1) la citation ففي حديث الدرس : «لعن رسول "
     "الله ﷺ [LES DEUX MOTS EXACTS lettre par lettre]، يعني [نباش القبور ?]» ; "
     "(2) le hadith d'عائشة : ففي الموطأ عن مالك، أنه بلغه، أن عائشة زوج النبي "
     "ﷺ كانت تقول : «[كَسْرُ ? كَثُرَ ?] عَظْمِ الميّت [مِثْلُ ? مِثْلُ كَسْرِهِ ? "
     "كَكَسْرِهِ ?] وهو [حَيّ ? مَيْتًا ?]» [تعني في الإثم ?] et le renvoi "
     "[الموطأ رقم : N] chiffre par chiffre."),
    ("r3-p104-lex", "r3-p104-lex.png",
     "Transcris LETTRE PAR LETTRE l'item 1 du bloc : ١- أشرح : [LES TROIS LEXIES "
     "EXACTES, chaque mot lettre par lettre, séparées par des tirets — première "
     "lexie : خس نود ? خمس ذود ? الحصيد ? autre ? — deuxième : أولاq ? أولاق ? "
     "العذوق ? autre ? — troisième : أوسق ? الوسيق ? autre ?]. Puis l'item 2 "
     "entier : [أعرف ? أقرأ ?] [الزكاة ? الذكاة ? الزكاء ?] وأبين [حكمها ?] "
     "و[شروطها ?]. Et la phrase d'introduction (أحفظ أحاديث الدرس المُقبل "
     "وأجيب عن الآتي ? ou autre ?)."),
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
        print(d["choices"][0]["message"]["content"][:3000])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
