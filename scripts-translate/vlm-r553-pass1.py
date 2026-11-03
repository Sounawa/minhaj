#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R553 — Passe 1 VLM : transcription structurée par zone, leçon 15 hadith-2es
(slot pdf-16, p.105-111 + preuve borne p.112). Crops 250 dpi, questions cadrées.
Retry 429 : pause 60-120 s (service saturé par les ouvriers parallèles)."""
import fitz
import json
import os
import subprocess
import time
import random

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = f"{HOME}/tr-tmp/qa-crops-r553"
OUT = f"{HOME}/tr-tmp/vlm-r553"
os.makedirs(OUT, exist_ok=True)

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible, token par token. Si tu n'es "
        "pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne "
        "complète JAMAIS de mémoire (n'utilise PAS de version canonique du hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

doc = fitz.open(PDF)


def crop(page_no, x0f, y0f, x1f, y1f, dpi, name):
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{CROPS}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


ZONES = [
    # (key, page, x0f, y0f, x1f, y1f, dpi, question)
    ("p105-objectifs-tamhid", 105, 0.03, 0.19, 0.97, 0.69, 250,
     "(1) Transcris l'en-tête de section et les objectifs numérotés TOKEN PAR TOKEN "
     "(combien sont-ils ?). (2) Transcris le paragraphe d'introduction (tamhīd) TOKEN "
     "PAR TOKEN jusqu'à la série de questions finale incluse. (3) Le badge/en-tête de "
     "page en haut : que lis-tu (numéro de leçon ? numéro de page ?) — transcris tel "
     "qu'imprimé."),
    ("p105-hadith1", 105, 0.03, 0.66, 0.97, 1.00, 300,
     "C'est le premier hadith de la leçon. (1) Transcris l'en-tête de section. "
     "(2) Transcris l'isnād complet TOKEN PAR TOKEN (de مالك jusqu'au compagnon). "
     "(3) Transcris le matn entre guillemets MOT À MOT, ligne par ligne, jusqu'à sa "
     "fin exacte. (4) Le renvoi entre crochets [الموطأ رقم : ...] : transcris-le "
     "ENTIER, le numéro CHIFFRE PAR CHIFFRE tel qu'imprimé (écris chaque chiffre "
     "séparément puis la valeur que tu lis). (5) Y a-t-il autre chose après le "
     "renvoi ?"),
    ("p106-hadith2", 106, 0.03, 0.04, 0.97, 0.42, 300,
     "C'est le deuxième texte de la leçon (parole de Mālik). (1) Transcris TOKEN PAR "
     "TOKEN tout le texte : la phrase introductive (قال مالك في الذهب والورق...), la "
     "citation entre guillemets MOT À MOT jusqu'à sa fermeture, la phrase qui suit "
     "(وكان بعضهم... / وذلك أن رسول الله... / قال مالك وهذا...). (2) Le renvoi entre "
     "crochets [الموطأ رقم : ...] : ENTIER, numéro CHIFFRE PAR CHIFFRE tel "
     "qu'imprimé. (3) Transcris la ligne décorative/chiffres bizarres si elle porte "
     "un sens réel, sinon ignore-la."),
    ("p106-tarjama", 106, 0.03, 0.40, 0.97, 0.62, 300,
     "Encadré ترجمة الراوي. (1) Transcris l'en-tête. (2) Transcris la biographie "
     "TOKEN PAR TOKEN : identité (هو ... بن ... بن ...), يوم أحد, nombre de ghazwāt, "
     "روى عن..., mort. (3) Les années de mort : transcris CHAQUE nombre CHIFFRE PAR "
     "CHIFFRE tel qu'imprimé, dans l'ordre exact d'apparition (droite à gauche), avec "
     "les mots وقيل entre eux."),
    ("p106-scharh", 106, 0.03, 0.60, 0.97, 1.00, 300,
     "Section الشرح (définitions). Transcris TOKEN PAR TOKEN chaque entrée du "
     "glossaire : (1) خمس ذؤد ... (2) أواق ... avec les équivalences en dirhams, la "
     "définition du dirham (grains d'orge), et TOUS les nombres (grammes, etc.) "
     "CHIFFRE PAR CHIFFRE tel qu'imprimés. Ne reformule rien."),
    ("p107-awsq-istikhlac", 107, 0.03, 0.02, 0.97, 0.36, 300,
     "(1) Transcris l'entrée de glossaire restante (أوسق : جمع وسق...) TOKEN PAR "
     "TOKEN avec le nombre de kilogrammes CHIFFRE PAR CHIFFRE. (2) Transcris "
     "l'en-tête استخلاص المضامين et les questions numérotées TOKEN PAR TOKEN "
     "(combien sont-elles ?)."),
    ("p107-mafhum", 107, 0.03, 0.36, 0.97, 1.00, 300,
     "Début du التحليل. (1) Transcris l'en-tête du bloc (أولا : ...) et le "
     "sous-titre (مفهومها -1). (2) أ- : la définition linguistique avec la citation "
     "d'Ibn Fāris MOT À MOT et son renvoi [ ... ] ENTIER. (3) ب- : la définition "
     "légale (الزكاة شرعا...) TOKEN PAR TOKEN avec son renvoi [شرح حدود ابن عرفة ...] "
     "ENTIER, chiffres inclus CHIFFRE PAR CHIFFRE. (4) La phrase وتستعمل شرعا... "
     "jusqu'à تطهير من الذنوب incluse, TOKEN PAR TOKEN."),
    ("p108-hukm", 108, 0.03, 0.04, 0.97, 0.29, 300,
     "Section حكمها -2. (1) Transcris la phrase introductive TOKEN PAR TOKEN. "
     "(2) La citation coranique entre accolades/guillemets : MOT À MOT tel "
     "qu'imprimé. (3) Le renvoi [سورة النور الآية ...] : numéro CHIFFRE PAR CHIFFRE "
     "tel qu'imprimé. (4) Le hadith prophétique qui suit (بني الإسلام...) MOT À MOT "
     "avec son renvoi source ENTIER. (5) La phrase finale (وهي تجب في...)."),
    ("p108-hikma", 108, 0.03, 0.28, 0.97, 0.72, 300,
     "Section حكمتها -3. (1) Transcris أ- ب- ج- د- TOKEN PAR TOKEN. (2) Dans د- : la "
     "citation coranique (وإلى هذه المعاني يشير قوله تعالى : ...) MOT À MOT telle "
     "qu'imprimée. (3) Son renvoi [سورة التوبة الآية : ...] : numéro CHIFFRE PAR "
     "CHIFFRE tel qu'imprimé. (4) La phrase après le renvoi s'il y en a une."),
    ("p108-shurut-intro", 108, 0.03, 0.70, 0.97, 1.00, 300,
     "(1) Transcris l'en-tête ثانيا : شروط زكاة العين et le point -1 ملك النصاب. "
     "(2) Transcris TOKEN PAR TOKEN le paragraphe (الحد الأدنى... نصابا...) avec le "
     "nombre entre parenthèses (grammes d'or) CHIFFRE PAR CHIFFRE."),
    ("p109-nisab-malik", 109, 0.03, 0.03, 0.97, 0.36, 300,
     "Suite du point 1 (نصاب). (1) Transcris TOKEN PAR TOKEN : le poids du dinar "
     "(nombre CHIFFRE PAR CHIFFRE), la citation de Mālik («السنة التي لا اختلاف "
     "فيها عندنا...») MOT À MOT, son renvoi [الموطأ رقم : ...] ENTIER (numéro CHIFFRE "
     "PAR CHIFFRE), la phrase وإليه ذهب الأئمة... (2) Puis ولا يعتبر المال... : la "
     "citation de Mālik sur les soixante et cent dix dirhams MOT À MOT avec son "
     "renvoi [الموطأ رقم : ...] ENTIER (CHIFFRE PAR CHIFFRE), et la phrase parce que "
     "(لأن المال إنما يعتبر...)."),
    ("p109-shuraka-hawl", 109, 0.03, 0.34, 0.97, 1.00, 300,
     "(1) Transcris TOKEN PAR TOKEN le paragraphe ولا فرق عند مالك... jusqu'à على "
     "حدة incluse (citation du Prophète MOT À MOT). (2) En-tête -2 مرور الحول et "
     "أ- : transcris TOKEN PAR TOKEN (أجمع العلماء... فقد كان ابن عمر... «لا تجب "
     "في...») avec le renvoi [الموطأ رقم : ...] ENTIER, numéro CHIFFRE PAR CHIFFRE. "
     "(3) ب- حول الفائدة والربح : en-têtes et le paragraphe حول الفائدة TOKEN PAR "
     "TOKEN jusqu'à la fin de page."),
    ("p110-qadi-rbah", 110, 0.03, 0.02, 0.97, 0.42, 300,
     "(1) Transcris TOKEN PAR TOKEN le récit qui commence la page (قال ... عن رجل "
     "أكراه؟ / أجّره؟ — la séquence avec الرجل : هل عندك من مال وجبت عليك فيه "
     "الزكاة...) : chaque mot exactement comme imprimé, y compris les noms propres. "
     "(2) حول الربح : transcris TOKEN PAR TOKEN tout le passage y compris la "
     "citation de Mālik MOT À MOT (رجل كانت له عشرة دنانير...) et le renvoi "
     "[الموطأ رقم : ...] ENTIER (numéro CHIFFRE PAR CHIFFRE)."),
    ("p110-taqwim", 110, 0.03, 0.41, 0.97, 0.62, 300,
     "Section التقويم. Transcris l'en-tête et les questions numérotées TOKEN PAR "
     "TOKEN (combien sont-elles ?), chaque mot exactement comme imprimé."),
    ("p110-istithmar", 110, 0.03, 0.60, 0.97, 1.00, 300,
     "Section الاستثمار. (1) Transcris l'en-tête. (2) Transcris TOKEN PAR TOKEN la "
     "citation [الموطأ رقم : ...] MOT À MOT (proposition de Mālik sur la dîme des "
     "dinars?) avec le numéro CHIFFRE PAR CHIFFRE. (3) Transcris les questions "
     "numérotées qui suivent TOKEN PAR TOKEN (combien sont-elles ? transcris-les "
     "toutes, y compris la première)."),
    ("p111-idad", 111, 0.03, 0.05, 0.97, 0.40, 300,
     "Section الإعداد القبلي (préparation préalable). (1) Transcris l'en-tête et le "
     "badge de page. (2) Transcris TOKEN PAR TOKEN la consigne (أحفظ أحاديث الدرس "
     "المقبل وأعد ما يأتي :) et les items numérotés (combien sont-ils ?). (3) Y "
     "a-t-il autre chose sur la page ?"),
    ("p112-borne", 112, 0.03, 0.18, 0.97, 0.45, 300,
     "PREUVE DE BORNE (page suivante). (1) Quel est l'en-tête de section ? (2) "
     "Transcris les objectifs numérotés TOKEN PAR TOKEN (combien sont-ils ?) — de "
     "quel sujet s'agit-il ? (3) Le badge de leçon : quel numéro de leçon est "
     "imprimé ?"),
]

for key, page, x0f, y0f, x1f, y1f, dpi, q in ZONES:
    name = f"z-{key}"
    out = f"{OUT}/{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    crop(page, x0f, y0f, x1f, y1f, dpi, name)
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{name}.png", "-o", out]
    attempt = 0
    while True:
        attempt += 1
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0 and os.path.exists(out):
            print("✓", key)
            break
        err = (r.stderr or r.stdout or "").strip()
        if "429" in err or "Too Many" in err or "rate" in err.lower():
            pause = random.uniform(60, 120)
            print(f"… 429 sur {key} (essai {attempt}) — pause {pause:.0f}s")
            time.sleep(pause)
        else:
            print("✗", key, err[:200])
            if attempt >= 3:
                break
            time.sleep(10)

print("\n===== RÉSULTATS =====")
for key, *_ in ZONES:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:2500])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
