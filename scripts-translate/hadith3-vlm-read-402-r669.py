# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM ciblées R669 (slot pdf-mut23h2x-402, leçon 13).
Mécanique hadith3-vlm-read-402-r657.py : CLI z-ai vision, cache json par zone.
Chaque lecture tranche une zone restée ambiguë : toute récusation de la couche
texte est documentée (nom d'image, ce qui a été lu), jamais devinée."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r669"

PROMPTS = {
    "r669-a-p90-tamhid-chain": (
        "Bande 600 dpi du tamhid d'une leçon de hadith arabe. Transcris EXACTEMENT, de droite à gauche : "
        "1) l'isnad du tamhid (attendu : مالك عن زياد بن أبي زياد مولى عبد الله بن عياش بن أبي ربيعة عن طلحة "
        "بن عبيد الله بن كريز — transcris CHAQUE maillon lettre à lettre : le mawla s'appelle-t-il زياد بن أبي زياد "
        "ou زيد بن أبي زيد ? l'ancêtre est-il عياش بن أبي ربيعة ?), 2) le matn (attendu : أن رسول الله صلى الله "
        "عليه وسلم قال: أفضل الدعاء دعاء يوم عرفة وأفضل ما قلت أنا والنبيون من قبلي لا إله إلا الله وحده لا شريك له), "
        "3) la référence bleue [الموطأ رقم: NNN] — lis chaque chiffre un par un et écris le nombre latin, "
        "4) les deux questions imprimées sous le hadith (attendu : ما حكم الوقوف بعرفة وما أعمال هذا اليوم). "
        "Marque [؟] l'illisible. Notes françaises courtes."
    ),
    "r669-b-p91-salim-notice": (
        "Bande 600 dpi du bas d'une page : notices biographiques. Transcris EXACTEMENT de droite à gauche : "
        "1) la fin de la notice d'أم الفضل بنت الحارث (attendu : هي لُبابة الكبرى بنت الحارث الهلالية، أم بني "
        "العباس الستة النجباء، كُنِيَت كأبيهم باسم أكبرهم. قال ابن حبان: توفيت في خلافة عثمان قبل زوجها العباس) — "
        "vérifie le nom du clan (الهلالية ?) et la phrase de Ibn Ḥibbān ; 2) la notice complète de سالم بن عبد الله "
        "(attendu : هو سالم بن عبد الله بن عمر بن الخطاب العدوي. قال مالك: [citation de Mālik] — transcris la "
        "citation de Mālik MOT POUR MOT : les candidats sont « لم يكن أحد في زمان سالم بن عبد الله أشبه من صيام "
        "الصالحين في الزهد والفضل والعيش منه » ou « ... أشبه من المباركين من بني عبد ... » — lis lettre à lettre "
        "et tranche ; 3) l'année de mort : lis les chiffres UN PAR UN (candidat 106) et le mois (ذي القعدة أو ذي الحجة ?). "
        "Marque [؟] l'illisible. Notes françaises courtes."
    ),
    "r669-c-p92-sharh-glosses": (
        "Bande 600 dpi du haut d'une page : rubrique الشرح (gloses). Combien de mots sont glossés ? "
        "Transcris EXACTEMENT chaque glose ligne par ligne : candidats = تمارَوا : اختلفوا ; السرادق : ما يُحيط "
        "بالخيمة وله باب يُدخل منه إليها ; ملحفة مُعَصْفَرة : إزار كبير مصبوغ بالعصفر ; existe-t-il un QUATRIÈME "
        "item ? Si oui transcris-le lettre à lettre (candidats : فأنظرني ? فألزمني ? ألزمني ?). Tranche par la "
        "lecture lettre à lettre. Marque [؟] l'illisible. Notes françaises courtes."
    ),
    "r669-d-p94-salat-jumua": (
        "Bande 600 dpi du bas d'une page : rubrique ثالثا. Transcris EXACTEMENT de droite à gauche : "
        "1) le titre vert (attendu ثالثا: الصلاة والخطبة يوم عرفة) et le sous-titre (1- صلاة الظهر والخطبة يوم عرفة) ; "
        "2) la règle de Mālik (attendu : لا يجهر الإمام بالقراءة في صلاة الظهر يوم عرفة لأن الظهر سرية ويخطب "
        "بجامع نمرة... — transcris MOT POUR MOT tout le paragraphe, notamment بجامع نمرة et la suite : "
        "يعلم الناس ? حتى ? التلاف ? — et la phrase qui suit : هذا الظهر يوم عرفة ? إن وافقت الجمعة ?) ; "
        "3) le hadith cité en gras (attendu : وفي الصلاة يوم عرفة وهي ظهر وإن وافقت الجمعة فإنما هي ظهر ولا "
        "تصلى الجمعة كفاك أذية يوم عرفة من أجل السفر قصرت) avec sa référence bleue [الموطأ رقم: NNN] — "
        "chiffre par chiffre ; 4) la ligne finale (attendu : لا جمعة على مسافر. قال مالك في إمام الحاج إذا وافق "
        "يوم الجمعة يوم عرفة أو يوم النحر أو بعض أيام التشريق: إنه لا يجمع في شيء من تلك الأيام) avec sa "
        "référence bleue [الموطأ رقم: NNN] chiffre par chiffre. Marque [؟] l'illisible. Notes françaises courtes."
    ),
    "r669-e-p95-istithmar": (
        "Bande 600 dpi d'une page : après l'évaluation, une rubrique avec un hadith encadré. Transcris EXACTEMENT : "
        "1) le titre de la rubrique (lettre à lettre : الاستثمار ? الاستشهاد ? الاستشهار ? — tranche) ; "
        "2) l'isnad complet du hadith encadré (candidats : مالك عن إبراهيم بن عبد الله بن أبي عطابة عن طلحة بن "
        "عبد الله بن كريز — le troisième maillon de طلحة est-il عبد الله ou عبيد الله ? vérifie lettre à lettre) ; "
        "3) le matn MOT POUR MOT (attendu : ما رأيت الشيطان يوم البذر أبدا أصغر ولا أدحر ولا أحجر ولا أغيظ منه "
        "في يوم عرفة وما ذلك إلا مما رأى من تنزل الرحمة وتجاوز الله عن الذنوب العظام إلا ما رأى يوم البذر) ; "
        "4) les deux questions réponses après (قيل وما رأى يوم البذر قال أما إنه قد رأى جبريل يزع الملاكية — "
        "transcris exactement, surtout le verbe يزع) ; 5) la référence bleue [الموطأ رقم: NNN] chiffre par chiffre ; "
        "6) s'il y a une ligne d'appel imprimée sous le hadith (je prends appui... ?), transcris-la. "
        "Marque [؟] l'illisible. Notes françaises courtes."
    ),
}

IMG = {
    "r669-a-p90-tamhid-chain": "r669-a-p90-tamhid-chain.png",
    "r669-b-p91-salim-notice": "r669-b-p91-salim-notice.png",
    "r669-c-p92-sharh-glosses": "r669-c-p92-sharh-glosses.png",
    "r669-d-p94-salat-jumua": "r669-d-p94-salat-jumua.png",
    "r669-e-p95-istithmar": "r669-e-p95-istithmar.png",
}


def run(name):
    out = os.path.join(DIR, f"_r669-read-{name}.json")
    if os.path.exists(out):
        print(f"cache {name}")
        return
    img = os.path.join(DIR, IMG[name])
    prompt = PROMPTS[name]
    cmd = ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if res.returncode != 0:
        print(f"ERR {name}: {res.stderr[:300]}")
        return
    try:
        d = json.load(open(out, encoding="utf-8"))
        body = d["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"ERR parse {name}: {e}")
        return
    print(f"OK {name} — {len(body)} car")


if __name__ == "__main__":
    for n in sys.argv[1:] or list(PROMPTS):
        run(n)
