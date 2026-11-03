#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R558 — 1re passe VLM : structure + hadiths + numéros, composites 300 dpi p.91-97 (leçon 13, pdf-14)."""
import json
import time
import os
import subprocess

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r550"
OUT = f"{HOME}/tr-tmp/vlm-l13"
os.makedirs(OUT, exist_ok=True)

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible, token par token. Si tu n'es "
        "pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne "
        "complète JAMAIS de mémoire (n'utilise PAS de version canonique du hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

ASKS = [
    ("p91", "p91-comp.png",
     "Transcris dans l'ordre : (1) le titre de section en haut (الدرس N) et la liste "
     "numérotée أهداف الدرس (chaque item en entier, mot à mot) ; (2) le paragraphe "
     "d'appel (خلق الله...) ENTIER puis la citation coranique : référence entre "
     "crochets [سورة ... الآية N] chiffre par chiffre tel qu'imprimé, et le texte de "
     "l'āya tel qu'imprimé mot à mot (même si dégradé) ; (3) la question finale "
     "(فما أحكام...) ; (4) le début de la section أحاديث الدرس : le premier isnād "
     "complet (chaque nom, mot à mot) et les premiers mots du matn."),
    ("p92", "p92-comp.png",
     "Transcris dans l'ordre : (1) la suite du premier hadith : matn entier + le "
     "renvoi rouge [الموطأ رقم : N] chiffre par chiffre ; (2) la glose en petit "
     "caractère sous le hadith (أشرنا إليها...) mot à mot ; (3) le DEUXIÈME hadith "
     "ENTIER : isnād complet (chaque nom) + matn (كفّنوني...) + renvoi rouge [الموطأ "
     "رقم : N] chiffre par chiffre ; (4) le troisième citation (عبد الله بن عمر...) "
     "avec son renvoi rouge chiffre par chiffre ; (5) le titre et le contenu de "
     "l'encadré ترجمة الراوي : nom de أم عطية, la glose وقيل..., la liste des "
     "transmetteurs noms par noms, et l'âge عاشت إلى حدود N chiffre par chiffre."),
    ("p93", "p93-comp.png",
     "Transcris dans l'ordre : (1) la glose en petit caractère en haut (نسبت إلى... "
     "وقال الأزهري...) mot à mot ENTIERE ; (2) le titre خلاصة/استخلاص المضامين et sa "
     "liste numérotée ; (3) le titre التلقين/التطبيق + أولاً أحكام غسل الميت ; (4) "
     "l'item 1 (حكم غسل الميت وصفته) : le paragraphe ENTIER mot à mot, y compris la "
     "citation du حديث أم عطيّة qu'il contient."),
    ("p94", "p94-comp.png",
     "Transcris dans l'ordre : (1) la fin de l'item précédent si elle continue ; (2) "
     "l'item 2 (صفة تغسيل الميت) : paragraphe ENTIER mot à mot — position, couverture "
     "de la ʿawra, les TROIS lavages (première : eau + سدر ; deuxième : ? ; troisième "
     ": eau + طيب) et le côté (يمين) ; (3) le renvoi rouge [الموطأ رقم : N] du hadith "
     "أم عطية chiffre par chiffre ; (4) le paragraphe sur le mari lavant son épouse "
     "(les trois imams nommés) + la citation أسماء بنت عميس ENTIÈRE avec son renvoi "
     "[معرفة السنة والآثار للبيهقي] + la phrase suivante (فإن لم يكن أحد الزوجين...)."),
    ("p95", "p95-comp.png",
     "Transcris dans l'ordre : (1) la fin du paragraphe sur qui lave (فإن لم تجد "
     "امرأة...) ENTIERE ; (2) le renvoi rouge [الموطأ رقم : N] (مُتُمْ فمِسحنا...) "
     "chiffre par chiffre ; (3) le titre ثانياً تكفين الميت والصلاة عليه + l'item 1 "
     "تكفين الميت ENTIER (couleur, nombre d'étoffe 3 ou 5, الزيادة في الستر, hadith "
     "cité avec son isnād mot à mot + renvoi rouge chiffre par chiffre) ; (4) l'item "
     "2 الصلاة على الجنازة : حكم الصلاة على الجنازة — paragraphe ENTIER y compris le "
     "hadith du Najāšī avec son isnād mot à mot et son renvoi rouge chiffre par "
     "chiffre."),
    ("p96", "p96-comp.png",
     "Transcris dans l'ordre : (1) la suite du paragraphe du Najāšī (pourquoi la "
     "prière lui fut spécifique) mot à mot ENTIERE ; (2) le titre ب صفة الصلاة على "
     "الجنازة et son paragraphe ENTIER (position de l'imam : وسط الجثة pour un "
     "homme / منكبيها pour une femme ; orientation du tête ; أربع تكبيرات ; le "
     "duʿāʾ court اللهم اغفر له...) ; (3) le paragraphe sur le duʿāʾ après la "
     "quatrième takbīra (مالك + أبي هريرة + دعاء) avec l'isnād mot à mot ; (4) le "
     "duʿāʾ long ENTIER mot à mot (فإذا... اللهم اغفر لأحيائنا وميّتنا وشاهدنا "
     "وغائبنا...) + le renvoi rouge [الموطأ رقم : N] chiffre par chiffre."),
    ("p97", "p97-comp.png",
     "Transcris dans l'ordre : (1) le titre التطبيق et ses questions numérotées ; "
     "(2) le titre استكمال الدرس : les DEUX hadiths ENTIERs — premier (عن نافع... "
     "عبد الله بن عمر...) avec renvoi rouge [الموطأ رقم : N] chiffre par chiffre ; "
     "deuxième (عن نافع... قال : صلّي...) avec renvoi rouge chiffre par chiffre ; "
     "(3) le titre استخلاص et ses items numérotés ; (4) le titre ضَدّ القبل : "
     "l'item 1 ENTIER mot à mot (أرجني في مصيبتي... ou équivalent) + l'item 2."),
]

def vision_call(prompt, img, out, tries=5):
    cmd = ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out]
    for t in range(tries):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0:
            return True, ""
        err = (r.stderr or "") + (r.stdout or "")
        if "429" in err or "Too many" in err:
            wait = 45 + 30 * t
            print(f"  429 — attente {wait}s (tentative {t + 1}/{tries})")
            time.sleep(wait)
            continue
        return False, err[:200]
    return False, "429 persistant"

for key, img, q in ASKS:
    out = f"{OUT}/pass1-{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    ok, err = vision_call(f"{BASE}\nQUESTION : {q}", f"{CROPS}/{img}", out)
    print(("✓" if ok else "✗"), key, err)

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/pass1-{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:4500])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
