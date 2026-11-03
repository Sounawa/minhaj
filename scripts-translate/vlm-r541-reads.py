#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R541 — lectures VLM ciblées/ancrées (anti-hallucination, méthode R538).
Une question fermée ou ancrée par crop ; sortie tr-tmp/vlm-r541/<key>.json"""
import fitz
import json
import subprocess

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r541"
OUT = f"{HOME}/tr-tmp/vlm-r541"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwatta' Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible. Si tu n'es pas sûr d'un mot, "
        "écris [illisible]. N'invente AUCUN texte, ne complète jamais de mémoire.")

ASKS = [
    # (key, image, question)
    ("p53-renvoi-num", "p53-renvoi-tight.png",
     "Il y a un renvoi coranique entre crochets : [سورة الإسراء الآية : ...]. "
     "Quel est le NUMÉRO imprimé ? Réponds UNIQUEMENT par le nombre en chiffres, "
     "puis transcris la ligne entière du renvoi."),
    ("p53-objectifs", "p53-objectifs.png",
     "Combien d'objectifs sont listés sous أهداف الدرس ? Transcris chaque objectif "
     "exactement avec son numéro, tel qu'imprimé."),
    ("p53-isnad1", "p53-matn1.png",
     "L'isnād du premier hadith commence par مالك عن يحيى بن سعيد عن القاسم بن محمد. "
     "ENTRE القاسم بن محمد ET سهل بن أبي حثمة : quel(s) mot(s)/nom(s) exact(s) "
     "sont imprimés ? (a) عن عباد بن تميم  (b) aucun nom intermédiaire  "
     "(c) autre — transcris exactement ce que tu vois. Transcris ensuite le début "
     "du matn jusqu'à فيركع الإمام."),
    ("p54-matn2-start", "p54-matn2-num509.png",
     "Transcris exactement les 3-4 PREMIÈRES lignes du hadith de عائشة (commençant "
     "par كسفت/خسفت الشمس في عهد رسول الله). Mot à mot, tel qu'imprimé, sans rien ajouter."),
    ("p56-sir-word", "p56-sifat-kusuf.png",
     "Dans le bloc صفة صلاة الكسوف, la phrase contient «بفاتحة الكتاب وسورة طويلة ...». "
     "Quel est le mot imprimé juste après طويلة ? (a) سراً  (b) جهراً  (c) autre — "
     "transcris exactement le mot et la phrase complète de la première rak'a."),
    ("p56-hukm-block", "p56-hukm-khawf.png",
     "Sous le titre حكم صلاة الخوف : (1) y a-t-il un encadré/une phrase donnant le "
     "statut juridique (سنة، مستحبة...) ? Transcris-la exactement. (2) Transcris "
     "exactement la phrase commençant par كان ذلك. (3) Y a-t-il une citation coranique "
     "entre ﴿ ﴾ ou « » avec le renvoi [سورة النساء الآية : ...] ? Quel numéro ?"),
    ("p57-aisha-quote", "p57-aisha-note.png",
     "Transcris exactement la citation de عائشة commençant par فصلى رسول الله, "
     "ligne par ligne, jusqu'à انصرف. La couche OCR lit notamment : قام فأطال "
     "القيام، ثم ركع فأطال الركوع، وهو دون القيام الأول / دون الركوع الأول، "
     "ثم سجد، ثم فعل في الركعة الآخرة مثل ذلك. Confirme ou corrige."),
    ("p57-khutba", "p57-khutba.png",
     "Transcris exactement la citation de la khutba du Prophète : إن الشمس والقمر "
     "آيتان من آيات الله... et la phrase sur les فواحش (الزنى والفجور) et le "
     "رappel du jour du Jugement. La couche OCR lit : ينهيهم عن كل الفواحش من "
     "الزنى والفجور ويذكرهم بيوم القيامة. Confirme ou corrige."),
    ("p58-taqwim3", "p58-hikma-taqwim.png",
     "Les questions du التقويم : transcris les 3 questions exactement. La 3e "
     "commence par أذكر ... صلاة الكسوف والخسوف — quel est le mot entre أذكر et "
     "صلاة ? (a) فضيلة  (b) صفة  (c) autre."),
    ("p58-istithmar", "p58-istithmar.png",
     "Transcris exactement le hadith de l'exploitation (الاستثمار) d'après أبي "
     "هريرة : كان رسول الله ﷺ نازلا بين ضجنان وعسفان... jusqu'au renvoi "
     "[سنن النسائي...]. La couche OCR lit : إن لهؤلاء صلاة... ; فجاء جبريل عليه "
     "السلام فأمره أن يقسم أصحابه نصفين... طائفة... وطائفة مقابلين على عدوهم قد "
     "أخذوا حذرهم ; ركعة وركعتان. Transcris ce que tu vois, mot à mot."),
    ("p59-iqdad", "p59-iqdad-qabli.png",
     "Transcris exactement les DEUX questions de l'إعداد القبلي après la phrase "
     "أحفظ أحاديث الدرس المقبل وأجيب عن الآتي. La 1re contient les mots حول "
     "الرداء — transcris-la entièrement et exactement."),
    ("p55-defs", "p55-definitions.png",
     "Confirme les définitions du glossaire (الشرح) : مواجهة العدو، الكسوف، "
     "الخسوف، تجلت الشمس، آيتان من آيات الله. Transcris chacune exactement."),
    ("p55-maqasid", "p55-maqasid-aya.png",
     "Transcris exactement le bloc استخلاص المقاصد (2 questions), et la citation "
     "coranique après قول الله تعالى (avec son renvoi [سورة النساء الآية : ...] "
     "et son numéro exact)."),
]

subprocess.run(["mkdir", "-p", OUT], check=True)

# crop complémentaire : renvoi Isrāʾ p.53 (bande plus basse que le crop initial)
doc = fitz.open(f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf")
pg = doc[52]
r = pg.rect
clip = fitz.Rect(r.width * 0.05, r.height * 0.52, r.width * 0.95, r.height * 0.82)
pix = pg.get_pixmap(matrix=fitz.Matrix(500 / 72, 500 / 72), clip=clip)
pix.save(f"{CROPS}/p53-renvoi-tight.png")
print("p53-renvoi-tight:", pix.width, "x", pix.height)
doc.close()

for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
    ok = "✓" if r.returncode == 0 else "✗"
    print(f"{ok} {key}")

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1100])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
