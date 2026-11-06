# -*- coding: utf-8 -*-
# R627 — passe 2 : lectures VLM ancrées sur zones divergentes (arbitrage).
import json, subprocess, time, os

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r627"
OUT = f"{HOME}/tr-tmp/vlm-r627"
os.makedirs(OUT, exist_ok=True)

BASE = ("Tu lis une image d'un manuel scolaire marocain d'ulum al-hadith (2e année "
        "secondaire traditionnel, d'après an-Nukhba d'Ibn Hajar). Transcription "
        "EXACTE token par token du texte imprimé visible. [illisible] si incertain. "
        "N'invente RIEN, ne complète jamais de mémoire. Chiffres des références : "
        "CHIFFRE PAR CHIFFRE tel qu'imprimé (l'ordre imprimé peut être inversé).")

ASKS = [
    ("A-p64-def-lisan", "ADJ2-p64-def-lisan-900.png",
     "Transcris mot à mot : (1) le bloc أولا: المحكم 1- تعريف المحكم أ- لغة (phrase "
     "entière + la référence entre crochets [ ] transcrite CHIFFRE PAR CHIFFRE et "
     "dans l'ordre imprimé) ; (2) ب- اصطلاحا (phrase entière)."),
    ("B-p64-def-suite", "ADJ2-p64-def-lisan-900.png",
     "Transcris mot à mot le développement sous ب- اصطلاحا : « فإن يخلو؟ فإن عُرض "
     "له معارض... » jusqu'à « (سيأتي بيانه) » — chaque phrase entière : (a) « فإن "
     "عُرض له معارض فلا يخلو إما أن يكون... مثله أو... مردوداً أقوى منه » ; (b) "
     "« وإن كانت معارضته بمثله فلا يخلو إما أن يمكن الجمع بين مدلولهما بدون "
     "تعسف أو ... » ; (c) la phrase sur « فإن يمكن الجمع فهو ... » ; (d) « أو "
     "فيعلم التاريخ ... المتأخر منهما فهو الناسخ والآخر المنسوخ (سيأتي بيانه) »."),
    ("C-p63-gloses", "ADJ2-p63-sarh-gloses-900.png",
     "Transcris mot à mot les DEUX gloses du الشرح : (1) « عُرِض بمثله: ... » ; "
     "(2) « المعارضة: ... » (le dernier mot exact : المعنى ou العلة ?)."),
    ("D-p63-istikhlac", "ADJ2-p63-istikhlac-900.png",
     "Transcris mot à mot le bloc استخلاص المضامين : COMBIEN d'items numérotés ? "
     "Transcris chaque item ENTIER dans l'ordre."),
    ("E-p64-mithal-haut", "ADJ2-p64-mithal-haut-900.png",
     "Transcris mot à mot : (1) l'intro « أمثلة الحديث المحكم كثيرة... » ; (2) le "
     "PREMIER hadith intégral + sa référence entre crochets EXACTE ; (3) le "
     "DEUXIÈME hadith intégral + sa référence entre crochets EXACTE."),
    ("F-p64-mithal-bas", "ADJ2-p64-mithal-bas-900.png",
     "Transcris mot à mot TOUS les hadiths visibles avec leurs références entre "
     "crochets EXACTES (y compris « إذا وضع العشاء... » et « لا شغار... » si "
     "visibles), puis le début du bloc ثانيا: الحديث المختلف 1- تعريفه (phrase de "
     "définition + phrase sur ضبط كلمة «المختلف» : qui ضبطها بكسر اللام / بفتح "
     "اللام, et « مصدر ميمي »)."),
    ("G-p65-ref-taqrib", "ADJ2-p65-ref-taqrib-900.png",
     "Transcris mot à mot : (1) la phrase « حديثان أو أكثر متضادان... » entière ; "
     "(2) la référence entre crochets : nom du livre + nom de l'auteur EXACT + "
     "numéro de page CHIFFRE PAR CHIFFRE tel qu'imprimé."),
    ("H-p65-ref-dawani", "ADJ2-p65-ref-dawani-900.png",
     "Transcris mot à mot la (les) phrase(s) contenant « ولا يعارض هذا... » puis la "
     "référence entre crochets EXACTE : titre du livre + auteur + les nombres "
     "CHIFFRE PAR CHIFFRE dans l'ordre imprimé (ex. 1/125 ou 125/1)."),
    ("I-p66-haut-quote", "ADJ2-p66-haut-quote-900.png",
     "Transcris mot à mot la citation du haut : « والأولى في الجمع أن يقال... » "
     "jusqu'à « والله أعلم » — y compris « لا يُعدّي شيئٌ شيئاً » (ou «لا يُعدي "
     "شيءٌ شيئاً» : transcris la forme EXACTE) et le dialogue de l'أعرابي? avec "
     "« فمن أعدى الأول؟ » et « فأمر بتجنبه... »."),
    ("J-p66-shafii-furak", "ADJ2-p66-shafii-furak-900.png",
     "Transcris mot à mot : (1) l'item الإمام الشافعي «اختلاف الحديث» ENTIER "
     "(jusqu'au point final) ; (2) l'item كتاب «مشكل الآثار» (nom complet de "
     "l'auteur) ; (3) l'item كتاب «مشكل الحديث وبيانه» (nom complet de l'auteur : "
     "محمد بن الحسين ou محمد بن الحسن ? transcris EXACTEMENT)."),
    ("K-p66-thawri-quote", "ADJ2-p66-thawri-quote-900.png",
     "Transcris mot à mot : (1) la citation « قال ... رحمه الله: «تعلموا هذا "
     "الحديث...» » ENTIÈRE (nom du savant EXACT) ; (2) la référence entre crochets "
     "EXACTE : titre + auteur(s) + nombres CHIFFRE PAR CHIFFRE dans l'ordre "
     "imprimé ; (3) le bloc التقويم (3 items)."),
    ("L-p67-sakhawi-suite", "ADJ2-p67-sakhawi-suite-900.png",
     "Transcris mot à mot : (1) la suite de la citation du السخاوي : « ...但它 "
     "توسّع حيث قال: لا أعرف حديثين صحيحين متضادين؛ فمن كان عنده شيء من ذلك "
     "فليأتني به لأؤلّف بينهما، وانتقد عليه ... فقال البلقيني: إنه لو فتحنا باب... » "
     "jusqu'à la fin de la citation ; (2) la référence entre crochets EXACTE : "
     "titre + auteurs + nombres CHIFFRE PAR CHIFFRE dans l'ordre imprimé."),
    ("M-p67-atamal", "ADJ2-p67-atamal-700.png",
     "Transcris mot à mot les DEUX questions du bloc أتأمل النص وأجيب عن الآتي "
     "(la question 2 : ... ومعرفة ... ? quel est le DERNIER mot exact)."),
]

for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    if os.path.exists(out) and os.path.getsize(out) > 200:
        print(f"SKIP {key}"); continue
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        print(("OK  " if r.returncode == 0 else "FAIL") + f" {key}")
        if r.returncode != 0:
            print(r.stderr[:200])
        time.sleep(2)
    except subprocess.TimeoutExpired:
        print(f"TIMEOUT {key}")

print("\n===== EXTRAITS =====")
for key, _, _ in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1600])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
