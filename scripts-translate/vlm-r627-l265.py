# -*- coding: utf-8 -*-
# R627 — lectures VLM ancrées leçon 11 uh2 (slot pdf-mut23h2u-265, p.63-67).
# Méthode R541/R622 : question fermée ancrée par crop ; sortie tr-tmp/vlm-r627/<key>.json.
# Jamais deviné : chaque chiffre (référence miroir) et chaque bloc brouillé par l'OCR
# est relu SUR L'IMAGE.
import json, subprocess, time

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r627"
OUT = f"{HOME}/tr-tmp/vlm-r627"
import os; os.makedirs(OUT, exist_ok=True)

BASE = ("Tu lis une image d'un manuel scolaire marocain d'ouluwm al-hadith (ulum "
        "al-hadith, 2e année du cycle secondaire traditionnel, d'après an-Nukhba "
        "d'Ibn Hajar). Réponds UNIQUEMENT à la question posée, par transcription "
        "EXACTE du texte imprimé visible, token par token. Si tu n'es pas sûr d'un "
        "mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne complète "
        "JAMAIS de mémoire, ne corrige pas l'imprimé même s'il te paraît fautif. "
        "Pour tout nombre entre crochets [ ] transcris CHIFFRE PAR CHIFFRE tel "
        "qu'imprimé.")

ASKS = [
    ("p63-banniere", "ADJ-p63-banniere-900.png",
     "Transcris exactement : (1) la bannière de titre de leçon « الدرس ... : ... » "
     "avec son numéro en toutes lettres et son titre ; (2) tout badge ou numéro "
     "circulaire visible ; (3) la première ligne sous la bannière."),
    ("p63-objectifs-tamhid", "ADJ-p63-objectifs-tamhid-700.png",
     "Transcris exactement : (1) le bloc أهداف الدرس (items numérotés, mot à mot) ; "
     "(2) le paragraphe تمهيد entier ; (3) les questions d'ouverture qui terminent "
     "le tamhīd (فبماذا يسمى...؟)."),
    ("p63-matn-istikhlac", "ADJ-p63-bas-matn-istikhlac-700.png",
     "Transcris exactement : (1) le bloc المتن (citation d'Ibn Hajar « ثم المقبول... ») "
     "mot à mot ; (2) le bloc الفهم et le début du الشرح ; (3) le bloc استخلاص "
     "المضامين ENTIER (chaque item numéroté mot à mot, y compris toute ligne sur "
     "« عُرِض بمثله »)."),
    ("p64-def-muhkam", "ADJ-p64-haut-def-muhkam-700.png",
     "Transcris exactement le bloc أولا: المحكم 1- تعريف المحكم : (a) لغة (avec la "
     "référence entre crochets [لسان العرب ...] transcrite CHIFFRE PAR CHIFFRE) ; "
     "(b) اصطلاحا (phrase entière) ; puis le développement (فإن يخلو...) jusqu'à "
     "« (سيأتي بيانه) »."),
    ("p64-mithal", "ADJ-p64-bas-mithal-700.png",
     "Transcris exactement : (1) 2- مثال المحكم (phrase d'intro) ; (2) le premier "
     "hadith cité (texte intégral + sa source entre crochets [صحيح ... باب ...]) ; "
     "(3) le deuxième hadith (texte intégral + source entre crochets) ; (4) le début "
     "du bloc ثانيا: الحديث المختلف 1- تعريفه (phrase de définition + la phrase sur "
     "le ضبط du mot «المختلف» : بفتح اللام / ضم الميم, et « مصدر ميمي »)."),
    ("p65-def-mukhtalif", "ADJ-p65-haut-mukhtalif-700.png",
     "Transcris exactement : (1) la fin de la définition (أحاديث أكثر أو متضادان... "
     "ظاهراً...) avec la référence entre crochets si visible ; (2) le passage sur "
     "الضبط الأول والثاني (نفس التضاد والتعارض...) ; (3) le bloc 2- أقسامه : "
     "l'intro ENTIERE (les deux types/قسمان) mot à mot."),
    ("p65-hadith-ma", "ADJ-p65-hadith-ma-900.png",
     "Transcris exactement : (1) le hadith de l'eau (الماء... لا يُنجِّس...) mot à "
     "mot tel qu'imprimé ; (2) sa ligne d'attribution (رواه... / سنن...) avec les "
     "noms des collections EXACTS ; (3) la phrase qui suit sur القلتين (فإن "
     "القلتين إذا تغير...) ; (4) toute référence entre crochets visible."),
    ("p65-qultayn", "ADJ-p65-qultayn-700.png",
     "Transcris exactement le passage sur القلتان : (1) « فإن القلتين إذا تغير... » "
     "jusqu'à « أم قلتين » ; (2) la phrase sur المشهور عند مالك ; (3) la phrase "
     "« ولا يعارض حديث القلتان... » avec les noms cités ; (4) le début du bloc "
     "النوع الثاني (ما لا يمكن الجمع فيه)."),
    ("p65-ref-qayrawani", "ADJ-p65-ref-qayrawani-900.png",
     "Transcris CHIFFRE PAR CHIFFRE la référence entre crochets concernant ابن أبي "
     "زيد (رسالة القيرواني) : le nom exact de l'auteur et de l'ouvrage tel "
     "qu'imprimé + les nombres (ex. 1/125 ou 125/1) EXACTEMENT comme imprimés, "
     "chiffre par chiffre."),
    ("p65-bas-naw", "ADJ-p65-bas-naw-700.png",
     "Transcris exactement : (1) النوع الأول : أن يعرف المتقدم من المتأخر (phrase "
     "entière avec الناسخ/المنسوخ) ; (2) النوع الثاني (phrase entière : فإن لم "
     "يعلم... بالترجيح/المرجوح) ; (3) la phrase « والتعارض بين الحديثين هو بحسب "
     "ما ظهر للناظر... » ; (4) les exemples de الجمع : « لا عدوى ولا طيرة » avec "
     "« فر من المجذوم فرارك من الأسد », et « الشؤم في ثلاث... » — transcris les "
     "formulations EXACTES imprimées et la phrase de جمع (جعل مخالطة المريض... "
     "أو ابن الصلاح...)."),
    ("p66-haut-jam", "ADJ-p66-haut-jam-700.png",
     "Transcris exactement le haut de la page : (1) la phrase sur وأول من قال في "
     "الجمع (quote attribuée, avec le nom du savant) ; (2) le récit/hadith qui suit "
     "mot à mot (y compris « لعن الله... » ou « شيءٌ شيءاً » si visible) ; (3) les "
     "phrases sur الجرج/الأعمى/معمر si visibles."),
    ("p66-tasnim-liste", "ADJ-p66-tasnim-liste-700.png",
     "Transcris exactement le bloc 3- أشهر الكتب المؤلفة في الحديث المختلف: CHAQUE "
     "item (tirets -) mot à mot : (1) الإمام الشافعي « اختلاف الحديث » (phrase "
     "entière) ; (2) كتاب « مشكل الآثار » للطحاوي (nom complet de l'auteur) ; (3) "
     "كتاب « مشكل الحديث وبيانه » (nom complet de l'auteur) ; (4) toute AUTRE "
     "mention de livre/auteur dans ce bloc."),
    ("p66-ref-fath", "ADJ-p66-ref-fath-900.png",
     "Transcris CHIFFRE PAR CHIFFRE : (1) la référence entre crochets du type "
     "[فتح المغيث ... N/N] : nom du livre et de l'auteur EXACTS + les nombres "
     "EXACTEMENT comme imprimés ; (2) la phrase qui précède immédiatement (quote de "
     "الإمام مالك « إذا علمتم هذا الحديث... ») mot à mot."),
    ("p66-bas-taqwim", "ADJ-p66-bas-taqwim-700.png",
     "Transcris exactement : (1) la quote de l'Imam Malik (إذا علمتم هذا الحديث... "
     "فإن ظننتم...) mot à mot ; (2) le bloc التقويم (تقويم) avec ses items "
     "numérotés 1-, 2-, 3- mot à mot."),
    ("p67-haut-sakhawi", "ADJ-p67-haut-sakhawi-900.png",
     "Transcris exactement le haut de la page : (1) la quote du حافظ (le savant "
     "citée : nom EXACT) sur أهمية الحديث المختلف (من أهم الأنواع...) mot à mot ; "
     "(2) la phrase sur أئمة الجماعة / أبو بكر بن خزيمة؛ (3) la phrase « لكنه "
     "التوسع... لا أعرف... » ; (4) la référence entre crochets [فتح المغيث ...] : "
     "nom de l'auteur + nombres CHIFFRE PAR CHIFFRE exactement comme imprimés."),
    ("p67-bas-idad", "ADJ-p67-bas-idad-700.png",
     "Transcris exactement le bas de la page : (1) le bloc أتأمل النص وأجيب عن "
     "الآتي (les 2 questions numérotées mot à mot) ; (2) le bloc أطلع الدرس القادم "
     "(الإعداد القبلي) : les 2 items numérotés mot à mot."),
]

for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    if os.path.exists(out) and os.path.getsize(out) > 200:
        print(f"SKIP {key} (déjà lu)"); continue
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
        print(d["choices"][0]["message"]["content"][:1500])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
