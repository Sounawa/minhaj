# -*- coding: utf-8 -*-
"""R655 — lectures VLM des zooms 600 dpi NEUTRES (sans candidats) — leçon 20 uh2.
Neutral prompts: la question ne suggère JAMAIS la réponse attendue."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r655"
READ = "/tmp/vlm-r651/read.mjs"

PROMPTS = {
    "z1-lisan-ref": (
        "Crop 600 dpi d'une ligne de référence bibliographique bleue dans un manuel arabe. La ligne contient "
        "une référence entre crochets: un titre d'ouvrage (لسان العرب)، un auteur (ابن منظور)، le mot بتصرف, "
        "et UN OU DEUX NOMBRES avec un séparateur /. Transcris la ligne ENTIÈRE exactement, puis lis chaque "
        "nombre chiffre par chiffre en décrivant l'ordre visuel exact sur l'image (quel chiffre est le plus à "
        "droite, quel chiffre est le plus à gauche). Notes courtes en français à la fin."
    ),
    "z2-definition": (
        "Crop 600 dpi d'une ligne arabe. La ligne commence par ب- اصطلاحا: puis عرفه الإمام ابن الصلاح رحمه "
        "الله بقوله: الحديث المعلل هو الحديث الذي ... Transcris la ligne ENTIÈRE exactement lettre à lettre "
        "jusqu'au bout (il y a une référence bleue entre crochets à la fin — transcris-la et lis son chiffre "
        "chiffre par chiffre). Porte une attention particulière au verbe après علة (تقدح ou تقدر — transcris "
        "exactement les lettres visibles). Notes courtes en français à la fin."
    ),
    "z3-mardud": (
        "Crop 600 dpi de deux lignes arabes d'un manuel. Elles contiennent: ورده ابن الصلاح بأنه [un mot] عند "
        "أهل العربية واللغة؛ لأن المعلول من عله بالشراب؛ أي سقاه مرة بعد أخرى وهو غير ملائم وسماه معللا، puis "
        "plus loin تسميته بالمعلول (ou un autre mot). Transcris EXACTEMENT les deux lignes lettre à lettre. "
        "Pour le mot après بأنه: décris chaque lettre visible (ر، ذ، د، و، ل...). Pour le mot après تسميته "
        "بـ: décris chaque lettre visible. Notes courtes en français à la fin."
    ),
    "z4-qari-p103": (
        "Crop 600 dpi d'une référence bibliographique bleue entre crochets. Transcris la référence exactement "
        "puis lis le NOMBRE final chiffre par chiffre en décrivant l'ordre visuel exact (le chiffre le plus à "
        "droite, le milieu, le plus à gauche). Notes courtes en français à la fin."
    ),
    "z5-adtila": (
        "Crop 600 dpi de la fin d'un paragraphe arabe. La dernière ligne se termine par فلا تسمى عندنا علة "
        "suivi d'UN MOT FINAL en gras. Transcris les lignes exactement, puis lis le MOT FINAL lettre par "
        "lettre (décris chaque lettre: ا، ض، ط، ص، ل، ع، ح...). Notes courtes en français à la fin."
    ),
    "z6-qari-p104": (
        "Crop 600 dpi d'une référence bibliographique bleue entre crochets (fin de citation). Transcris la "
        "référence exactement puis lis le NOMBRE final chiffre par chiffre en décrivant l'ordre visuel exact "
        "(le chiffre le plus à droite, le milieu, le plus à gauche). Notes courtes en français à la fin."
    ),
    "z7-ans": (
        "Crop 600 dpi d'une ligne arabe commençant par ب- et contenant: ما انفرد مسلم بإخراجه في حديث أنس "
        "[un ou plusieurs mots] بنفي قراءة... Transcris la ligne exactement lettre à lettre, et pour les mots "
        "entre أنس et بنفي: décris chaque lettre visible avec les diacritiques. Notes courtes en français à "
        "la fin."
    ),
    "z8-muqaddima-92": (
        "Crop 600 dpi d'une référence bleue entre crochets. Transcris-la exactement puis lis le NOMBRE chiffre "
        "par chiffre en décrivant l'ordre visuel exact (le chiffre le plus à droite, puis le plus à gauche). "
        "Notes courtes en français à la fin."
    ),
    "z9-taqwim": (
        "Crop 600 dpi de la rubrique التقويم d'un manuel arabe. Transcris EXACTEMENT le titre puis les DEUX "
        "questions numérotées 1 et 2 lettre à lettre, chacune dans son intégralité (les chiffres ١ et ₂ aussi). "
        "Notes courtes en français à la fin."
    ),
    "z10-muqaddima-93": (
        "Crop 600 dpi d'une référence bleue entre crochets. Transcris-la exactement puis lis le NOMBRE chiffre "
        "par chiffre en décrivant l'ordre visuel exact (le chiffre le plus à droite, puis le plus à gauche). "
        "Notes courtes en français à la fin."
    ),
}

IMG = {
    "z1-lisan-ref": "z1-lisan-ref.png",
    "z2-definition": "z2-definition.png",
    "z3-mardud": "z3-mardud.png",
    "z4-qari-p103": "z4-qari-p103.png",
    "z5-adtila": "z5-adtila.png",
    "z6-qari-p104": "z6-qari-p104.png",
    "z7-ans": "z7-ans.png",
    "z8-muqaddima-92": "z8-muqaddima-92.png",
    "z9-taqwim": "z9-taqwim.png",
    "z10-muqaddima-93": "z10-muqaddima-93.png",
}

def run(name):
    out = os.path.join(DIR, f"_r655-read-{name}.json")
    if os.path.exists(out):
        print(f"cache {name}")
        return
    img = os.path.join(DIR, IMG[name])
    prompt = PROMPTS[name]
    cmd = ["node", READ, img, prompt, out + ".raw"]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if res.returncode != 0:
        print(f"ERR {name}: {res.stderr[:300]}")
        return
    body = res.stdout.strip()
    json.dump({"name": name, "image": img, "body": body}, open(out, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    os.path.exists(out + ".raw") and os.remove(out + ".raw")
    print(f"OK {name} — {len(body)} car")


if __name__ == "__main__":
    for n in sys.argv[1:] or list(PROMPTS):
        run(n)
