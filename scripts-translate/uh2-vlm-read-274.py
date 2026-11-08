# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM de vérification R655 (slot pdf-mut23h2u-274, leçon 20 ulum-hadith-tanawi-2).
Méthode hadith3-vlm-read-400-r654.py (R654) ; SDK isolé /tmp/vlm-r651 HORS arbre git.
Bandes 300 dpi (uh2-crops-274.py) ; cache tr-tmp/qa-crops-r655/_r655-read-<name>.json ;
toute récusation de la couche texte est documentée (nom d'image, ce qui a été lu), jamais devinée."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r655"
READ = "/tmp/vlm-r651/read.mjs"

PROMPTS = {
    "p102-banner-objectifs": (
        "Bande supérieure 300 dpi d'une page de manuel scolaire arabe. Transcris EXACTEMENT, de haut en bas: "
        "1) la bannière décorative avec un médaillon circulaire — lis le chiffre du médaillon chiffre par "
        "chiffre (attendu ٢٠ pour la leçon 20) et le titre sous la bannière (attendu الحديث المعلل) — "
        "transcris les mots exactement; 2) la rubrique أهداف الدرس s'il y a un encadré jaune — transcris les "
        "QUATRE objectifs ligne par ligne exactement, en lisant la puce/le chiffre de début de chaque ligne "
        "chiffre par chiffre. Attendu au 1er: أن أتعرف مفهوم الحديث المعلل; au 2e: أن أدرك أهمية معرفة المعلل "
        "وطرق معرفته; au 3e: أن أجتنب الاستدلال بالأحاديث التي فيها علة; au 4e: أن أتخلق بخلق الأمانة في نقل "
        "الأخبار وأداء العلم — CONFIRME ou corrige mot à mot. Notes courtes en français à la fin."
    ),
    "p102-tamhid-matn": (
        "Bande 300 dpi d'une page de manuel arabe (cours de sciences du hadith). Transcris EXACTEMENT, de haut "
        "en bas: 1) le titre تمهيد et le PARAGRAPHE ENTIER qui suit (attendu: النظر في الحديث يختلف باختلاف "
        "الناظر فيه... فماذا يسمى هذا النوع؟ وما طرق معرفته؟) — confirme la fin exacte et les questions posées; "
        "2) le titre المتن puis le TEXTE ENCADRÉ (bordure) du ḥāfiẓ Ibn Ḥaǧar: transcris LE TEXTE COMPLET de "
        "l'encadré mot à mot, avec la vocalisation — attendu environ: قال الحافظ ابن حجر رحمه الله: «ثُمَّ "
        "الوَهْمُ؛ إن اطَّلَعَ عَلَيْهِ بِالقَرَائِنِ وَجَمْعِ الطُّرُقِ؛ ...» — DÉTERMINE s'il y a une suite "
        "après وَجَمْعِ الطُّرُقِ (par ex. فالوَاهِمُ ou autre) et transcris-la exactement. Notes courtes en "
        "français à la fin."
    ),
    "p102-gloses": (
        "Bande 300 dpi (bas de page d'un manuel arabe, deux colonnes). Transcris EXACTEMENT dans l'ordre "
        "imprimé: 1) la rubrique الفهم puis les TROIS gloses lexicales (الشرح) — 1re: الوهم: أي رواية الحديث "
        "على سبيل التوهم؛ 2e: القرّائن: جمع قرينة، والقرينة: أمر يشير إلى المطلوب؛ 3e: المعلل: اسم مفعول من "
        "«أعله» بكذا فهو «معل» وهو القياس الصرفي المشهور — CONFIRME chaque glose mot à mot, en lisant "
        "particulièrement «فهو معل» (معل) exactement; 2) la rubrique استخلاص المضامين et son item: أستخرج من "
        "المتن ما يعرف به الوهم في الحديث. Notes courtes en français à la fin."
    ),
    "p103-def-lugha-istilah": (
        "Bande 300 dpi d'une page arabe (rubric التحليل, section أولا: تعريف المعلل). Transcris EXACTEMENT: "
        "1) rubrique أولا: تعريف المعلل; 2) l'item أ- لغة: le PARAGRAPHE COMPLET (عل يعل واعتل أي مرض فهو "
        "عليل ولا أعلك الله أي لا أصابك بعلة والعلة: المرض) puis la référence bleue entre crochets [لسان "
        "العرب، ابن منظور، بتصرف، N/P] — LIS LE CHIFFRE chiffre par chiffre (candidates: ١١/١٧٤ ou ١٧٤/١١) et "
        "indique chaque chiffre; 3) l'item ب- اصطلاحا: la DÉFINITION COMPLÈTE d'Ibn aṣ-Ṣalāḥ «عرفه الإمام ابن "
        "الصلاح رحمه الله بقوله: الحديث المعلل هو الحديث الذي ...» — transcris la suite complète mot à mot "
        "(il y a une suite importante après الحديث الذي — par ex. une mention d'علة خفية/غامضة), puis la "
        "mention عبارة كثير من المحدثين: كالبخاري والترمذي وابن عدي والدارقطني، وكذا في عبارة المتكلمين "
        "والأصوليين تسميته بالمعلول، ورده ابن الصلاح بأنه مرذول/مردود عند أهل العربية واللغة — CONFIRME le mot "
        "exact مرذول ou مردود, puis la suite (لأن المعلول من عله بالشراب أي سقاه مرة بعد أخرى وهو غير ملائم "
        "وسماه معللا) et le passage قال الحافظ العراقي: الأجود في تسميته: المعلل وكذا وقع في عبارة بعضهم avec "
        "sa référence bleue [شرح شرح نخبة الفكر في مصطلحات أهل الأثر، للقاري، ص NNN] — LIS LE CHIFFRE chiffre "
        "par chiffre (candidates: ٥٤٩ ou ٩٤٥); 4) le paragraphe ويفهم من تقييد العلة الذي أوردناه أنه لا بد أن "
        "يتحقق فيها شرطان وهما: الغموض والخفاء والقدح في صحة الحديث، فإن اختل واحد منهما: كأن تكون العلة "
        "ظاهرة أو غير قادحة فلا تسمى عندنا علة + le MOT FINAL exact (attendu possible: اضطلاعا) — lis-le "
        "lettre à lettre. Notes courtes en français à la fin."
    ),
    "p103-turuq": (
        "Bande 300 dpi d'une page arabe (section ثانيا: طرق معرفة المعلل). Transcris EXACTEMENT: 1) le titre "
        "ثانيا: طرق معرفة المعلل et la ligne مما تعرف به العلة في الحديث; 2) l'item أ- COMPLET (attendu: "
        "كثرة التتبع وجمع القرائن والنظر في رجال الأسانيد لتبين الأشياء القادحة: كإبدال راو ورواية غيرهم على "
        "سبيل التوهم، فقد روي عن علي بن المديني أنه قال: الباب إذا لم تجمع طرقه لم يتبين خطؤه) — CONFIRME où "
        "se termine exactement l'item أ- et où commence l'item ب-; 3) l'item ب- COMPLET (attendu: جمع الطرق؛ "
        "أي الأسانيد المشتملة على المتون واستقصاؤها من المجامع والمسانيد ليحصل الترجيح بذلك ويعلم أنه موصول "
        "أو مرسل أو نحوهما والنظر في اختلاف رواة كل حديث وضبطهم وإتقانهم) — CONFIRME la phrase ويعلم أنه "
        "موصول أو مرسل أو نحوهما; 4) le paragraphe final: وقد تقصر عبارة المعلل الناظر في علة الحديث المعلل "
        "عن إقامة الحجة على دعواه بأن يعلم أن في الحديث قصورا لكن لا يقدر على بيانه؛ كالصيرفي في ... — "
        "TRANSCRIS EXACTEMENT la fin (attendu possible: كالصيرفي في نقد الدينار والدرهم) lettre à lettre. "
        "Notes courtes en français à la fin."
    ),
    "p104-ihtilaq": (
        "Bande 300 dpi (haut de page arabe). Transcris EXACTEMENT le paragraphe qui commence par هذا. وبعضهم "
        "يطلق العلة على غير المعنى المذكور: ككذب الراوي وفسقه وغفلته وسوء حفظه ونحوه من أسباب تضعيف الحديث؛ "
        "كالتدليس، والإمام الترمذي سمى النسخ علة، قال الحافظ السخاوي: فكأنه أراد علة مانعة من العمل لا "
        "الاصطلاحية — puis la référence bleue [شرح نخبة الفكر في مصطلحات أهل الأثر، علي القاري، ص NNN] — LIS "
        "LE CHIFFRE chiffre par chiffre (candidates: ١٦٤ ou ٤٦١) et indique chaque chiffre. Notes courtes en "
        "français à la fin."
    ),
    "p104-ahammiya": (
        "Bande 300 dpi d'une page arabe (section ثالثا: أهمية معرفة المعلل). Transcris EXACTEMENT: 1) le "
        "titre ثالثا: أهمية معرفة المعلل et la première phrase (المعلل من أشرف ما يطلب في علم الحديث); 2) la "
        "citation de l'Imām ʿAbd ar-Raḥmān Ibn Mahdī «لأن أعرف علة حديث هو عندي أحب إليّ من أن أكتب حديثا ليس "
        "عندي» avec sa référence bleue [علل الحديث، لابن أبي حاتم، N/P] — LIS LE CHIFFRE chiffre par chiffre "
        "(candidate: ١/٩); 3) la suite complète: وهذا الفن من أغمض أنواع علوم الحديث وأدقها ولا يقوم به إلا من "
        "رزقه الله تعالى فهما ثاقبا وحفظا واسعا ومعرفة تامة بمراتب الرواة وملكة قوية بالأسانيد والمتون؛ ولهذا "
        "لم يتكلم فيه إلا القليل من أهل هذا الشأن — puis LA LISTE EXACTE des savants (attendu: كعلي ابن "
        "المديني وأحمد بن حنبل والبخاري ويعقوب بن شيبة وأبي حاتم وأبي زرعة والدارقطني) — CONFIRME chaque nom. "
        "Notes courtes en français à la fin."
    ),
    "p104-mithal": (
        "Bande 300 dpi d'une page arabe (section رابعا: مثال المعلل). Transcris EXACTEMENT: 1) le titre رابعا: "
        "مثال المعلل et le paragraphe introductif COMPLET (قد تقع العلة في إسناد الحديث وهو الأكثر وقد تقع في "
        "متنه وما يقع في الإسناد قد يقدح في صحة الإسناد والمتن جميعا كما في التعليل بالإرسال والوقف وقد يقدح "
        "في صحة الإسناد خاصة من غير قدح في صحة المتن ومثال ذلك في الآتي); 2) l'item أ- مثال العلة في الإسناد: "
        "la chaîne EXACTE (ما رواه الثقة يعلى بن عبيد عن سفيان الثوري عن عمرو بن دينار عن ابن عمر عن النبي "
        "ﷺ قال: كل بيعين لا بيع بينهما حتى يتفرقا إلا بيع الخيار) avec sa référence bleue [المعجم الكبير، "
        "الطبراني، باب العين، ...] — transcris la référence complète, puis toute l'explication (فهذا إسناد "
        "متصل بنقل العدل عن العدل وهو معلل غير صحيح والمتن على كل حال صحيح والعلة في قوله عن عمرو بن دينار "
        "إنما هو عن عبد الله بن دينار عن ابن عمر هكذا رواه الأئمة من أصحاب سفيان عنه؛ فوهم يعلى بن عبيد وعدل "
        "عن عبد الله بن دينار إلى عمرو بن دينار وكلاهما ثقة); 3) l'item ب- مثال العلة في المتن: le début "
        "EXACT — y a-t-il حديث أنس المصرح به / أنس المالِح / autre? LIS le mot après أنس lettre à lettre, "
        "puis la suite (بنفي قراءة «بسم الله الرحمن الرحيم» ونصه «صليت خلف النبي ﷺ وأبي بكر وعمر وعثمان» "
        "فكانوا يستفتحون بالحمد لله رب العالمين لا يذكرون «بسم الله الرحمن الرحيم» في أول قراءة ولا في آخرها) "
        "avec sa référence bleue [صحيح مسلم، كتاب الصلاة، باب حجة من قال لا يجهر بالبسملة], puis فعلل قوم "
        "رواية اللفظ المذكور لما رأوا الأكثرين إنما ... transcris la fin de la page exactement. Notes courtes "
        "en français à la fin."
    ),
    "p105-b-cont": (
        "Bande 300 dpi (haut de page arabe, suite d'une explication). Transcris EXACTEMENT: 1) les lignes "
        "قالوا فيه: «فكانوا يستفتحون القراءة بـ«الحمد لله رب العالمين»» من غير تعرض لذكر البسملة، وهو الذي "
        "اتفقت البخاري ومسلم على إخراجه في الصحيح — CONFIRME le verbe exact (اتفقت أو اتفق); 2) ورأوا أن من "
        "رواه باللفظ المذكور رواه بالمعنى الذي وقع له ففهم من قوله: كانوا يستفتحون بالحمد أنهم كانوا لا "
        "يبسملون فرواه على ما فهم؛ لأن معناه أن السورة التي كانوا يفتتحون بها من السور هي الفاتحة وليس فيه "
        "تعرض لذكر التسمية; 3) وانضم إلى ذلك أمور منها: أنه ثبت عن أنس: أنه سئل عن الافتتاح بالتسمية فذكر أنه "
        "لا يحفظ فيه شيئا عن رسول الله ﷺ avec sa référence bleue [مقدمة ابن الصلاح، ص NNN] — LIS LE CHIFFRE "
        "chiffre par chiffre (candidates: ٢٩ ou ٩٢). Notes courtes en français à la fin."
    ),
    "p105-hukm-ahtadi": (
        "Bande 300 dpi d'une page arabe. Transcris EXACTEMENT: 1) le titre خامسا: حكم المعلل et le "
        "PARAGRAPHE COMPLET (العلة كما سبق عبارة عن أسباب خفية غامضة قادحة في صحة الحديث بحيث يغلب على ظن "
        "الناظر فيه وجود علة فيحكم بعدم صحة الحديث لذلك اكتفاء بغلبة الظن أو يتردد لعدم ترجيح أحد الطرفين "
        "فيتوقف في الحكم بالصحة وعدمها وأما إذا لم يطلع عليه بما ذكر من القرائن فالظاهر السلامة من الجرح); "
        "2) la rubrique أهتدي وأقتدي et la citation complète روى الإمام الدارمي بسنده عن معمر عن الزهري قال: "
        "«عرضت عليه كتابا فقلت: أرويه عنك؟ قال: ومن حدثك به غيري» avec sa référence bleue [سنن الدارمي، باب "
        "في العرض] — CONFIRME chaque mot. Notes courtes en français à la fin."
    ),
    "p105-taqwim-istithmar": (
        "Bande 300 dpi d'une page arabe. Transcris EXACTEMENT: 1) la rubrique التقويم (ou التفقويم — lis le "
        "titre exactement) et LES DEUX questions numérotées — IMPORTANT: la PREMIÈRE question est un "
        "texte court difficile: lis-la LETTRE À LETTRE (elle ne commence PAS par لم كانت — c'est la 2e; la "
        "1re attendue peut être: ما الذي تعرف به الوهم في الحديث؟ ou similaire); la 2e attendue: لم كانت "
        "معرفة العلل من أغمض أنواع علوم الحديث وأدقها؟ — CONFIRME les deux; 2) la rubrique الاستثمار et la "
        "citation COMPLÈTE de l'Imām Ibn aṣ-Ṣalāḥ «قد يطلق اسم العلة على غير ما ذكرناه من باقي الأسباب "
        "القادحة في الحديث المخرجة له من حال الصحة إلى حال الضعف المانعة من العمل به على ما هو مقتضى لفظ "
        "العلة في الأصل ولذلك تجد في كتب علل الحديث الكثير من الجرح بالكذب والغفلة وسوء الحفظ ونحو ذلك من "
        "أنواع الجرح» avec sa référence bleue [مقدمة ابن الصلاح، ص NNN] — LIS LE CHIFFRE chiffre par chiffre "
        "(candidates: ٣٩ ou ٩٣). Notes courtes en français à la fin."
    ),
    "p106-idad": (
        "Bande 300 dpi (bas de page arabe). Transcris EXACTEMENT: 1) les DEUX items numérotés qui terminent "
        "l'exploitation: 1- أناقش قول ابن الصلاح مبينا إطلاقات اسم العلة، 2- أقرأ مقدمة كتاب من كتب العلل "
        "التي وُجهت في الإعداد القبلي لإحضارها — CONFIRME chaque mot; 2) la rubrique الإعداد القبلي et son "
        "item complet (أقرأ متن الدرس القادم وأنجز الأنشطة المقترحة من الأستاذ(ة)). Notes courtes en français "
        "à la fin."
    ),
    "p107-banner-l21": (
        "Bande supérieure 300 dpi d'une page de manuel arabe. DÉTERMINE: 1) la bannière décorative avec un "
        "médaillon circulaire — lis le chiffre du médaillon CHIFFRE PAR CHIFFRE (attendu ٢١ pour la leçon 21) "
        "et le titre (attendu المدرج والمقلوب) — transcris exactement; 2) la rubrique أهداف الدرس si un "
        "encadré apparaît — transcris TOUS les objectifs ligne par ligne (attendus: أن أميز بين الإدراج في "
        "السند والإدراج في المتن؛ أن أتعرف مفهوم القلب في الحديث وأسبابه؛ أن أضيضها أحفظ من الأحاديث أنقليها "
        "بالفاظها دون تغلي أو تلذيت — CONFIRME mot à mot); 3) le début du تمهيد (قد علمت أن من أسباب الطعن "
        "في الراوي مخالفته للثقات...). Notes courtes en français à la fin."
    ),
}

IMG = {
    "p102-banner-objectifs": "p102-banner-objectifs.png",
    "p102-tamhid-matn": "p102-tamhid-matn.png",
    "p102-gloses": "p102-gloses.png",
    "p103-def-lugha-istilah": "p103-def-lugha-istilah.png",
    "p103-turuq": "p103-turuq.png",
    "p104-ihtilaq": "p104-ihtilaq.png",
    "p104-ahammiya": "p104-ahammiya.png",
    "p104-mithal": "p104-mithal.png",
    "p105-b-cont": "p105-b-cont.png",
    "p105-hukm-ahtadi": "p105-hukm-ahtadi.png",
    "p105-taqwim-istithmar": "p105-taqwim-istithmar.png",
    "p106-idad": "p106-idad.png",
    "p107-banner-l21": "p107-banner-l21.png",
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
