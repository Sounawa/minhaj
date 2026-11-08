# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM R655 (slot pdf-mut23h2x-400, leçon 11 hadith-3es).
Mécanique hadith3-vlm-read-400-r654.py (R654) : SDK isolé /tmp/vlm-r651 HORS
arbre git ; chaque lecture R655 cible une bande précise (crops r655) avec
prompt anti-plafonnement (mots interdits listés, [؟] obligatoire, lecture des
chiffres bleus UN À UN — loi d'inversion OCR : «94-25» = 49-52, jamais
deviner). Cache tr-tmp/qa-crops-r655/_r655-read-<name>.json."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r655"
READ = "/tmp/vlm-r651/read.mjs"

PROMPTS = {
    "p78-tamhid": (
        "Bande 600 dpi d'une page de manuel scolaire arabe (paragraphe de tamhīd). "
        "Transcris chaque ligne arabe EXACTEMENT comme imprimée, sans corriger. Zone attendue : un "
        "paragraphe commençant vers « للطواف آدابٌ منها؟ / له آدابٌ؟ » — transcris le VRAI début mot "
        "pour mot, puis la question posée à Mālik (le mot رحمه الله), la réponse de Mālik entre "
        "guillemets «...» (transcris-la EXACTEMENT, surtout le dernier mot avant la fermeture), la "
        "référence bleue [الموطأ رقم: NNN] — lis chaque chiffre UN PAR UN (aucune inversion), puis la "
        "phrase après la référence (ويختلف حكمه باختلاف نوعه...) jusqu'à la fin. "
        "NE DEVINE PAS : si un mot est incertain, écris [؟] à sa place. Termine par 3 notes françaises."
    ),
    "p78-hadith": (
        "Bande 600 dpi (bas d'une page de manuel arabe). Transcris EXACTEMENT : 1) les DEUX courtes "
        "questions qui terminent le tamhīd (formules du type فما حكم...؟ وما حكم...؟) — mot à mot ; "
        "2) le hadith en gras qui suit (transmetteur مالك عن نافع عن عبد الله بن عمر — la parole "
        "d'ʿUmar «لا ...» — transcris-la ENTRE GUILLEMETS exactement comme imprimée, mot à mot, "
        "surtout la fin «فإنَّ...الطَّوافُ...») ; 3) la référence bleue [الموطأ رقم: NNN] — chiffres "
        "UN PAR UN. NE DEVINE PAS, [؟] pour tout mot incertain. 3 notes françaises."
    ),
    "p79-cit1": (
        "Bande 900 dpi avec citation coranique en calligraphie thuluth ornée + étiquette bleue "
        "[سورة الحج الآية : N]. 1) Transcris les mots calligraphiés EXACTEMENT tels que visibles, "
        "mot par mot (les candidats plausibles sont وَمَن / يُعَظِّمْ / شَعَائِرَ / اللَّهِ / فَإِنَّهَا / "
        "مِنْ / تَقْوَى / الْقُلُوبِ / أَتِمُّوا / لَكُمْ / فَرَضَ) — dis exactement lesquels tu VOIS ; "
        "2) lis le nom de la sourate de l'étiquette bleue (الحج ou autre) et le numéro chiffre par "
        "chiffre en distinguant ٠ (ovale fermé) de ٢ (crochet ouvert) et ١ (trait vertical) de ٣ "
        "(trois dents) ; 3) transcris les fragments naskh visibles (début/fin de bande). NE DEVINE "
        "PAS les mots invisibles : [؟]. 3 notes françaises."
    ),
    "p79-cit2": (
        "Bande 900 dpi : citation coranique thuluth ornée + étiquette bleue [سورة الحج الآية : N] + "
        "référence bleue [الموطأ رقم: NNN]. 1) transcris les mots calligraphiés VISIBLES mot par mot "
        "(candidats plausibles : ثُمَّ / لْيَقْضُوا / تَفَثَّهُمْ / وَلْيُوفُوا / نُذُورَهُمْ / وَلْيَطَّوَّفُوا / "
        "بِالْبَيْتِ / الْعَتِيقِ / فَمَحِلُّ / الشَّعَائِرِ / كُلُّهَا / وانْقِضاؤُها) — dis exactement "
        "lesquels tu VOIS ; 2) étiquette bleue : sourate + numéro chiffre par chiffre ; 3) référence "
        "الموطأ : chiffres UN PAR UN ; 4) fragments naskh (وقال:... / قال مالك: فمحل...). NE DEVINE "
        "PAS : [؟]. 3 notes françaises."
    ),
    "p79-saad": (
        "Bande 600 dpi : hadith en gras de Saʿd b. Abī Waqqāṣ + référence bleue. Transcris "
        "EXACTEMENT : letransmetteur (مالك أنه بلغه أن سعد بن أبي وقاص...), la teneur : quand il "
        "entrait à La Mecque — quel mot EST imprimé : مُحْرِمًا ou مُرَاهِقًا ou autre ? regarde la "
        "LIGNE imprimée mot par mot ; puis ce qu'il faisait (خرج إلى عرفة قبل أن... ثم يطوف بعد أن "
        "يرجع), la parole de Mālik en gras «وذلك ... إن شاء الله» (mot du milieu : واسع ou أسع ou "
        "أوسع ?), la référence bleue [الموطأ رقم: NNN] chiffres UN PAR UN. [؟] pour incertain. "
        "3 notes françaises."
    ),
    "p79-acha": (
        "Bande 600 dpi : hadith en gras de ʿĀʾiša + référence bleue + début d'une notice "
        "biographique. Transcris EXACTEMENT chaque ligne (transmetteur مالك عن عبد الرحمن بن القاسم "
        "عن أبيه عن عائشة..., les paroles de ʿĀʾiša قدمت مكة وأنا حائض فلم أطف..., la réponse du "
        "Prophète ﷺ «افعلي ما يفعل الحاج...» mot à mot complète, la référence bleue [الموطأ رقم: NNN] "
        "chiffres UN PAR UN), puis la première ligne de la notice biographique qui suit. NE DEVINE "
        "PAS : [؟]. 3 notes françaises."
    ),
    "p80-fahm": (
        "Bande 600 dpi : rubrique verte الفهم (ou autre nom exact) suivie de trois gloses courtes. "
        "Transcris EXACTEMENT : 1) le nom imprimé de la rubrique ; 2) chaque glose complète mot à "
        "mot (formes du type « لا يصدَرَنَّ : لا يصرِفْنَ », « مَحَلُّها : مكان حلّ... », « مُرَاهِقًا : ... » "
        "— transcris la définition ENTIRE entre les deux-points et la fin) ; les parenthèses "
        "(بكسر/بفتح...) si présentes. NE DEVINE PAS : [؟]. 3 notes françaises."
    ),
    "p80-istihlas": (
        "Bande 600 dpi : rubrique استخلاص المضامين suivie de trois items numérotés. Transcris la "
        "rubrique exactement, puis CHAQUE item complet mot à mot avec son chiffre initial UN PAR UN "
        "(formes attendues : أبين... / أستخلص... / ما حكم...؟). NE DEVINE PAS : [؟]. 3 notes françaises."
    ),
    "p80-cit1": (
        "Bande 900 dpi : citation coranique thuluth ornée + étiquette bleue [سورة الحج الآية : N]. "
        "1) transcris les mots calligraphiés VISIBLES mot par mot (candidats : ذَلِكَ / وَمَن / يُعَظِّمْ / "
        "شَعَائِرَ / اللَّهِ / فَإِنَّهَا / مِنْ / تَقْوَى / الْقُلُوبِ / وَأَتِمُّوا / الَّتِي / فَرَضَ / لَكُمْ / "
        "الْفُلْوَى) — dis exactement lesquels tu VOIS ; 2) étiquette bleue : sourate + numéro chiffre "
        "par chiffre (٠ vs ٢, ١ vs ٣). NE DEVINE PAS : [؟]. 3 notes françaises."
    ),
    "p80-cit2": (
        "Bande 900 dpi : citation coranique thuluth ornée + étiquette bleue [سورة الحج الآية : N] + "
        "ligne naskh qui suit (قال مالك: «فمحل الشعائر كلها وانقضاؤها إلى البيت العتيق» + والمراد "
        "بالشعائر...). 1) transcris les mots calligraphiés VISIBLES (candidats : ثُمَّ / لْيَقْضُوا / "
        "تَفَثَّهُمْ / وَلْيُوفُوا / نُذُورَهُمْ / وَلْيَطَّوَّفُوا / بِالْبَيْتِ / الْعَتِيقِ) ; 2) étiquette "
        "bleue chiffre par chiffre ; 3) transcris les lignes naskh COMPLÈTES exactement. [؟] si "
        "incertain. 3 notes françaises."
    ),
    "p81-radd": (
        "Bande 600 dpi : paragraphe d'ouverture (الرجوع لطواف الوداع بعد مغادرة البيت...) puis "
        "hadith en gras de Ṣafiyya + référence bleue. Transcris EXACTEMENT : 1) la première ligne "
        "complète (pourquoi ce retour est recommandé — mot à mot, surtout l'exception ...) ; 2) le "
        "hadith : transmetteur, les paroles du Prophète ﷺ entre guillemets EXACTES (c'est court — "
        "transcris chaque lettre du mot interrogatif qu'il prononce), la réponse قيل..., sa parole "
        "«فلا إذا؟» ; 3) la référence bleue [الموطأ رقم: NNN] chiffres UN PAR UN. NE DEVINE PAS : "
        "[؟]. 3 notes françaises."
    ),
    "p81-urwa": (
        "Bande 600 dpi : passage d'ʿUrwa + référence bleue + rubrique verte ثانيا + début du "
        "paragraphe. Transcris EXACTEMENT : 1) les paroles d'ʿUrwa (من قضى... فَقَدْ...) mot à mot "
        "complètes ; 2) la référence bleue [الموطأ رقم: NNN] chiffres UN PAR UN ; 3) la rubrique "
        "ثانيا : le mot APRÈS طواف القدوم — مراهق ou مجرم ou autre ? regard la LIGNE imprimée ; "
        "4) les premières lignes du paragraphe (طواف القدوم من واجبات الحج...) mot à mot. NE DEVINE "
        "PAS : [؟]. 3 notes françaises."
    ),
    "p81-haid": (
        "Bande 600 dpi : rubrique verte ثالثا : طواف الحائض + sous-ligne 1- حكم... + paragraphe "
        "مذهب الجمهور. Transcris EXACTEMENT chaque ligne mot à mot (surtout : la règle de la "
        "majorité — jusqu'à / حتى..., la cause النهي..., la citation du Muwaṭṭaʾ qui commence ففي "
        "الموطأ...), et lis toute référence bleue visible chiffres UN PAR UN. NE DEVINE PAS : [؟]. "
        "3 notes françaises."
    ),
    "p82-mudtahar": (
        "Bande 600 dpi : suite du paragraphe (هي عدم الطهارة...) puis parole de Mālik en gras + "
        "référence bleue, puis hadith en gras d'une femme qui consulte + référence bleue. Transcris "
        "EXACTEMENT : 1) les lignes du début (هي عدم الطهارة فيعني الحائضُ والجُنْبَ والمحدثُ...) ; "
        "2) la parole de Mālik «لا يَطُوفَ...» complète ; 3) référence [الموطأ رقم: NNN] chiffres UN "
        "PAR UN ; 4) le hadith de la femme : transcris-le ligne à ligne EXACTEMENT — COMPTE "
        "COMBIEN DE FOIS la phrase avec «بَابِ الْمَسْجِدِ» et «هَرَقْتُ الدَّمَاءَ» apparaît (une, deux "
        "ou trois fois ?) — décris la séquence exacte ; 5) référence bleue chiffres UN PAR UN. "
        "NE DEVINE PAS : [؟]. 3 notes françaises."
    ),
    "p82-rijal": (
        "Bande 600 dpi : commentaire sur les transmetteurs du Muwaṭṭaʾ. Transcris EXACTEMENT chaque "
        "ligne : la variante rapportée «أنْ...» (quel mot pour la consultatrice ? عَجُوزَة ou autre), "
        "ce que la réponse prouve (دل جوابه...), le mot المُسْتَحَاضَة, la règle يُحِلُّ الطواف لمن..., "
        "et la conclusion sur قوله «اغتسلي» (ندب الاغتسال للطواف لا أنه...). NE DEVINE PAS : [؟]. "
        "3 notes françaises."
    ),
    "p82-items": (
        "Bande 600 dpi : deux rubriques numérotées en vert (2- المتمتعة... et 3- إذا حاضت المرأة "
        "بعد ركعتي الطواف) avec leurs paragraphes, paroles de Mālik en gras et références bleues. "
        "Transcris EXACTEMENT : 1) titre rubrique 2 complet ; son paragraphe mot à mot ; sa parole "
        "de Mālik «إنها إذا خَشِيَتْ...» complète ; sa référence bleue [الموطأ رقم: NNN] chiffres UN "
        "PAR UN ; 2) titre rubrique 3 complet ; la parole de Mālik «والمَرْأَةُ الحائضُ...» complète "
        "mot à mot ; sa référence bleue chiffres UN PAR UN ; note si les DEUX références sont "
        "identiques. NE DEVINE PAS : [؟]. 3 notes françaises."
    ),
    "p83-ihlal": (
        "Bande 600 dpi : paragraphe de conclusion. Transcris EXACTEMENT chaque ligne mot à mot "
        "comme IMPRIMÉE (même avec coquilles apparentes) : نستفاد/يستفاد من الدرس..., حرمة العبادات, "
        "الحج فلا تصح إلا..., على طهارة, le reste (لما فيها من... طلبا ل...), et la dernière phrase "
        "(الرفق ومراعاة الأحوال الخاصة للناس). NE DEVINE PAS : [؟]. 3 notes françaises."
    ),
    "p83-taqwim": (
        "Bande 600 dpi : rubrique التقويم (ou autre nom exact) + questions numérotées. Transcris le "
        "nom de la rubrique exactement, puis CHAQUE question complète mot à mot avec son chiffre "
        "UN PAR UN (formes attendues : ماذا يصنع من نسى...؟ / المستحاضة التي...). NE DEVINE PAS : "
        "[؟]. 3 notes françaises."
    ),
    "p83-hadith": (
        "Bande 600 dpi : rubrique d'exploitation + hadith encadré + référence bleue + ligne de "
        "consigne. Transcris EXACTEMENT : 1) le nom de la rubrique verte (الاستثمار ou autre) ; 2) le "
        "hadith encadré LIGNE PAR LIGNE : chaîne (مالك عن... عن... عن زينب بنت أبي سلمة عن أم "
        "سلمة زوج النبي ﷺ), son contenu (شكوت... أني... فقال: طوفي... وأنتِ...), la suite (فطفت ورسول "
        "الله ﷺ يُصلي إلى جانب البيت وهو يقرأ بالطُّور...) ; 3) référence bleue [الموطأ رقم: NNN] "
        "chiffres UN PAR UN ; 4) la ligne de consigne après le cadre (أستعين بشرح الزرقاني...). "
        "NE DEVINE PAS : [؟]. 3 notes françaises."
    ),
    "p83-idad": (
        "Bande 600 dpi : consigne + rubrique verte الإعداد القبلي + deux items numérotés. Transcris "
        "EXACTEMENT : 1) la ligne أستعين بشرح الزرقاني وأبين وأحكم... mot à mot ; 2) la rubrique "
        "الإعداد القبلي et sa formule (أحفظ أحاديث الدرس المقبل وأجيب عن الآتي) ; 3) l'item 1 : la "
        "formule أشرح: suivie de TOUS les mots à expliquer EXACTEMENT dans leur ordre (il y en a "
        "2 ou 3 — transcris chaque mot lettre à lettre, même s'il semble étrange) ; 4) l'item 2 "
        "أبحث عن حكم... complet. NE DEVINE PAS : [؟]. 3 notes françaises."
    ),
    "p84-banner": (
        "Bande 600 dpi du HAUT d'une page (bannière d'ouverture d'une leçon + objectifs). 1) "
        "Décris la bannière : mot au-dessus du médaillon (الدرس ou التمرين), chiffre du médaillon "
        "UN PAR UN, titre imprimé (attendu أحكام السعي بين الصفا والمروة ou أحكام السعي — transcris "
        "le vrai titre) ; 2) rubrique أهداف الدرس et CHAQUE objectif mot à mot avec son chiffre UN "
        "PAR UN. NE DEVINE PAS : [؟]. 3 notes françaises."
    ),
}

def run(name):
    out = os.path.join(DIR, f"_r655-read-{name}.json")
    if os.path.exists(out):
        print(f"cache {name}")
        return
    img = os.path.join(DIR, f"{name}.png")
    prompt = PROMPTS[name]
    cmd = ["node", READ, img, prompt, out + ".raw"]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if res.returncode != 0:
        print(f"ERR {name}: {res.stderr[:300]}")
        return
    body = res.stdout.strip()
    json.dump({"name": name, "image": img, "body": body}, open(out, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    if os.path.exists(out + ".raw"):
        os.remove(out + ".raw")
    print(f"OK {name} — {len(body)} car")


if __name__ == "__main__":
    for n in sys.argv[1:] or list(PROMPTS):
        run(n)
