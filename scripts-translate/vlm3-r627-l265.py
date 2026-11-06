# -*- coding: utf-8 -*-
# R627 — passe 3 MICRO : lectures VLM ancrées, une question fermée par litige.
import json, subprocess, time, os

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r627"
OUT = f"{HOME}/tr-tmp/vlm-r627"
os.makedirs(OUT, exist_ok=True)

BASE = ("Image d'un manuel marocain d'ulum al-hadith (arabe imprimé naskh, "
        "références en vert). Transcription EXACTE token par token des lignes "
        "demandées. En cas de doute sur UN mot : [illisible]. Jamais de mémoire. "
        "Pour tout nombre : transcris la suite de chiffres EXACTEMENT dans l'ordre "
        "visuel gauche→droite, puis dis ce qu'elle donne lue en sens arabe.")

ASKS = [
    ("a-luga", "ADJ3-p64-luga-ligne-1200.png",
     "Transcris la ligne de définition لغة : « اسم مفعول من أحكمت الشيء ... » — le "
     "deuxième mot exact après «أحكمتُ الشيء» : أتقنته ou أنقته ? Transcris la "
     "ligne ENTIÈRE mot à mot, et la ligne suivante « وأحكمَ الكلامَ ... » avec son "
     "mot final exact."),
    ("b-istikhlac", "ADJ3-p63-istikhlac-lignes-1200.png",
     "Transcris l'item 1 du bloc استخلاص المضامين mot à mot : « أستخلص من ... » — "
     "le mot après «من» : المتن ou اللفظ ? Transcris les items 1 et 2 entiers."),
    ("c-tasawwuf", "ADJ3-p64-tasawwuf-lignes-1200.png",
     "Transcris mot à mot les lignes : « وإن كانت معارضته بمثله فلا يخلو إما أن "
     "يمكن الجمع بين مدلولهما بغير ... » — le dernier mot : تعسف ou تعريف ? Puis "
     "la phrase « فإن أمكن الجمع فهو النوع المسمى: «مختلف الحديث» » et la phrase "
     "« وإن لم يمكن الجمع فلا يخلو إما أن يعرف التاريخ، أو لا، فإن عُرف وثبت "
     "التأخر منهما فهو الناسخ والآخر المنسوخ (سيأتي بيانه) » — mot à mot."),
    ("d-hadith2", "ADJ3-p64-hadith2-matn-1200.png",
     "Transcris mot à mot le hadith : « لا تدخل الملائكة بيتاً فيه كلب ... » (texte "
     "INTÉGRAL tel qu'imprimé) et sa référence verte entre crochets EXACTE."),
    ("e-taqrib", "ADJ3-p65-taqrib-lignes-1200.png",
     "Transcris mot à mot : (1) la ligne « أن يوجد حديثان أو أكثر متضادان في "
     "المعنى ظاهراً، ... بينهما » — le verbe exact : فيُوقَف ou فيُوافَق ? (2) la "
     "référence verte : titre + auteur (للنووي ou للنوري ?) + numéro de page."),
    ("f-dawani", "ADJ3-p65-dawani-lignes-1200.png",
     "Transcris mot à mot la référence verte : le premier mot exact (الفتاوى ?), "
     "le nom du livre, l'auteur (ابن أبي زيد ? القيرواني ?), et les nombres dans "
     "l'ordre visuel gauche→droite PUIS leur lecture en sens arabe."),
    ("g-jam-fin", "ADJ3-p66-jam-fin-1200.png",
     "Transcris mot à mot les dernières lignes du passage : « ... فأمر بتجنبه ... » "
     "— les 2-3 mots exacts après «بتجنبه» (حسماً لـ... ?) — puis « والله أعلم » si "
     "visible, et le titre de section qui suit (3- أشهر الكتب...)."),
    ("h-shafii", "ADJ3-p66-shafii-item-1200.png",
     "Transcris mot à mot : (1) la ligne d'intro « ألّف ... وغيرهم في علم مختلف "
     "الحديث كتباً قيمة، من أشهرها » (premier mot exact après ألّف) ; (2) l'item "
     "«اختلاف الحديث» للإمام الشافعي ENTIER (y compris : ولم يقصد؟ استيفاء مسائل "
     "هذا العلم وقضاياه، وإنما قصد... حتى «من العلماء»)."),
    ("i-furak", "ADJ3-p66-furak-item-1200.png",
     "Transcris mot à mot l'item du livre «مشكل الآثار» (nom complet de l'auteur : "
     "أحمد بن محمد بن سلمة الطحاوي ?) et l'item «مشكل الحديث وبيانه» (nom complet "
     "de l'auteur : محمد بن الحسين ou محمد بن الحسن بن فورك ? transcris EXACTEMENT "
     "ce qui est imprimé)."),
    ("j-thawri", "ADJ3-p66-thawri-lignes-1200.png",
     "Transcris mot à mot la citation : « قال الإمام سفيان الثوري رحمه الله: "
     "«تعلّموا؟ هذا الحديث ... » » — chaque proposition « فإذا ... فـ... » mot à "
     "mot (les verbes exacts), jusqu'à « فانشروه ». Puis la référence verte "
     "ENTIÈRE : titre + auteurs + les nombres dans l'ordre visuel gauche→droite "
     "PUIS leur lecture en sens arabe."),
    ("k-balaqini", "ADJ3-p67-balaqini-fin-1200.png",
     "Transcris mot à mot la fin de la citation السخاوي : « وانتُقد عليه بعض ... في "
     "توسيعه؛ فقال البلقيني: إنه لو فتحنا باب ... » jusqu'à la fermeture «».» — "
     "les mots exacts. Puis la référence verte ENTIÈRE (titre + auteurs + nombres : "
     "ordre visuel gauche→droite PUIS lecture en sens arabe)."),
    ("l-question2", "ADJ3-p67-question2-1200.png",
     "Transcris mot à mot la question 2 de أتأمل النص وأجيب عن الآتي : « لم كان "
     "الناظر في مختلف الحديث يحتاج لصناعتي: الحديث، والفقه، ومعرفة ... ? » — le "
     "DERNIER mot exact (المعاني ou العامة ou autre)."),
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
        print(d["choices"][0]["message"]["content"][:1300])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")
