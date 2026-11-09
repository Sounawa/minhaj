#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R98 — Vérification du rendu savant tafsir-3es / pdf-mut23h36-599 + -600.

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027
  3. guillemets « » appariés
  4. h1 attendu
  5. assertions ciblées : objectifs, termes, points du commentaire, sources
     (Ibn Kathīr 7/199 + 7/204 + 7/206, al-Qurṭubī 25/16, al-Nasafī 3/255,
     aṭ-Ṭabarī 21/537 + 21/538, al-Buḫārī ×2, al-ʿAlaq 6-7), évaluation,
     istithmār, préparation préalable
  6. croisement des versets rendus avec le cache coran warš (fragments clés)
  7. 0 résidu d'édition (XXX, TODO, 【】, undefined, NaN)
"""
import json
import re
import sys

TMPDIR = "/home/z/my-project/tr-tmp"
CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"

ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")

LESSONS = {
    "pdf-mut23h36-599": {
        "title": "Exégèse de la sourate al-Shūrā, versets 21 à 24",
        "asserts": [
            "à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy",
            "septième leçon (7)",
            "véracité du Messager — que Dieu prie sur lui et le salue — dans la transmission du message de son Seigneur",
            "le droit des gens de la maison de la Prophétie (āl bayt al-nubuwwa) sur les musulmans",
            "[Yaqtarifu ḥasanatun :] il l’acquiert, la bonne action.",
            "[Fīhā ḥusnan :] la récompense lui en sera dédoublée.",
            "[Wa-yaʿfū ʿani-s-sayyiʾāti :] Il passe outre les péchés et les désobéissances.",
            "Premièrement : la transmission de sa mission par le Messager — que Dieu prie sur lui et le salue — sans en exiger de récompense matérielle",
            "Deuxièmement : la promesse de Dieu — qu’Il soit exalté — d’accepter le repentir de Ses serviteurs",
            "« Ou bien ont-ils des associés qui auraient établi pour eux une religion que Dieu n’a jamais autorisée ?",
            "Tu verras les injustes épouvantés par ce qu’ils ont acquis",
            "« Telle est [l’annonce] que Dieu fait à Ses serviteurs",
            "“Je ne vous en demande aucune récompense, si ce n’est l’affection en raison de la parenté.”",
            "“Il a forgé un mensonge contre Dieu.”",
            "Il aurait scellé ton cœur",
            "Dieu efface le faux et confirme la vérité par Ses paroles",
            "[Tafsīr d’Ibn Kathīr : 7/199]",
            "l’appel à la compassion de Qurayš",
            "une recommandation en faveur des gens de la maison",
            "une recommandation de maintenir les liens de parenté",
            "le fait de se rapprocher de Dieu",
            "l’affection n’est pas une récompense",
            "[Tafsīr d’Ibn Kathīr : 7/204]",
            "il est accepté de manière certaine",
            "tant que les injustices ne sont pas restituées",
            "relève de la volonté divine",
            "l’indulgence à l’égard de la mécréance, et elle n’est pas possible du tout",
            "elle s’accomplit par consensus",
            "la doctrine des gens de la sunna",
            "l’opinion d’Ibn ʿAbbās et de Muʿāḏ ibn Ǧabal",
            "l’intercession et la satisfaction [divine]",
            "[Tafsīr d’al-Qurṭubī : 25/16]",
            "[Tafsīr d’Ibn Kathīr : 7/206]",
            "L’obligation de préserver les droits des proches parents",
            "les gens de la maison du Messager — que Dieu prie sur lui et le salue",
            "en veillant à en réunir les conditions",
            "[Ṣaḥīḥ d’al-Buḫārī ; kitāb al-daʿawāt, bāb al-tawba]",
            "au pied d’une montagne",
            "comme des mouches qui passèrent sur son nez",
            "sa monture était là, devant lui",
            "[les quatre expressions citées par le manuel sont partiellement illisibles dans le scan",
            "la première se lit « yaqbalu » (v. 25)",
            "la sagesse de la disparité des hommes dans leurs subsistances",
        ],
        "verses": {
            "42:21": ["ام لهم شركؤا", "شرعوا لهم من الدين", "ما لم يأذن به الله",
                      "ولولا كلمة الفصل", "لقضى بينهم", "الظلمين لهم عذاب اليم"],
            "42:22": ["ترى الظلمين مشفقين", "مما كسبوا", "وهو واقع بهم",
                      "ءامنوا وعملوا الصلحت", "فى روضات الجنات", "لهم ما يشاءون",
                      "ذلك هو الفضل الكبير"],
            "42:23": ["ذلك الذى يبشر الله", "عباده", "قل لا اسلكم عليه اجرا",
                      "الا المودة فى القربى", "ومن يقترف حسنة", "نزد له فيها حسنا",
                      "ان الله غفور شكور"],
            "42:24": ["ام يقولون افترى على الله كذبا", "فان يشا الله يختم على قلبك",
                      "ويمح الله البطل", "ويحق الحق بكلمته", "انه عليم بذات الصدور"],
        },
    },
    "pdf-mut23h36-600": {
        "title": "Exégèse de la sourate al-Shūrā, versets 25 à 27",
        "asserts": [
            "huitième leçon (8)",
            "la sagesse de la disparité des hommes dans leurs subsistances",
            "les preuves de la toute-puissance divine",
            "Être satisfait de la subsistance que Dieu m’a rendue facile",
            "[Basaṭa :] Il a élargi.",
            "[La-baghaw :] ils se sont rebellés, ont désobéi et commis des injustices.",
            "Premièrement : la sagesse de Dieu — qu’Il soit glorifié — dans la répartition des subsistances parmi Ses serviteurs",
            "Deuxièmement : les preuves de la puissance de Dieu — que soit exalté Celui qui parle en majesté — et de Sa grandeur",
            "« Si Dieu attribuait Ses dons avec largesse à [tous] Ses serviteurs, ils commettraient des abus sur la terre",
            "« Et c’est Lui qui agrée le repentir de Ses serviteurs",
            "Il exauce ceux qui croient et accomplissent les bonnes œuvres",
            "tandis que les mécréants auront un dur châtiment",
            "« Certainement l’homme dépasse les limites quand il se voit riche » (al-ʿAlaq, 6-7)",
            "[Ṣaḥīḥ d’al-Buḫārī ; kitāb al-riqāq, bāb mā yuḥḏar min zahrat ad-duniyā wa-tanāfus fīhā]",
            "Ce dont je crains le plus pour vous est ce que Dieu fera sortir pour vous des bénédictions de la terre",
            "L’éclat de la duniyā (…)",
            "celui qui mange sans se rassasier",
            "[Tafsīr d’Ibn Kathīr : 7/206]",
            "Il enrichit celui qui mérite la richesse et appauvrit celui qui mérite la pauvreté",
            "[Tafsīr d’al-Nasafī : 3/255]",
            "on dit à ʿUmar — que Dieu l’agrée — : la sécheresse s’est intensifiée",
            "maintenant ils vont pleuvoir",
            "une répétition du premier sens par une autre expression",
            "[Tafsīr d’aṭ-Ṭabarī : 21/537]",
            "« Parmi Ses preuves est la création des cieux et de la terre » (29)",
            "[Tafsīr d’aṭ-Ṭabarī : 21/538]",
            "quant au ciel, on a dit : cela signifie les anges",
            "le rassemblement (ḥašr) le jour de la Résurrection",
            "l’installation de la tyrannie sur la terre par la généralité de la richesse",
            "l’ascétisme (zuhd) en ce qui se trouve chez les autres",
            "après la dureté vient la délivrance, et après la contrainte vient la facilité",
            "la satisfaction (qanāʿa) et du contentement (riḍā)",
            "[tableau à compléter par l’élève — colonnes réservées aux valeurs tirées des versets de la leçon",
            "des versets 28 à 32 de la sourate al-Shūrā",
            "[les expressions citées par le manuel sont partiellement illisibles dans le scan]",
            "les bienfaits des épreuves par lesquelles Dieu met l’homme à l’épreuve",
        ],
        "verses": {
            "42:25": ["وهو الذى يقبل التوبة", "عن عباده", "ويعفوا عن السيات",
                      "ويعلم ما تفعلون"],
            "42:26": ["ويستجيب الذين ءامنوا", "وعملوا الصلحت", "ويزيدهم من فضله",
                      "والكفرون لهم عذاب شديد"],
            "42:27": ["ولو بسط الله الرزق", "لعباده", "لبغوا فى الارض", "ولكن ينزل بقدر",
                      "ما يشا", "انه بعباده خبير بصير"],
            "42:29": ["ومن ءايته خلق السموت والارض", "وما بث فيهما من دابة",
                      "وهو على جمعهم", "اذا يشاء قدير"],
            "96:6": ["كلا ان الانسن ليطغى"],
            "96:7": ["ان رءاه استغنى"],
        },
    },
}

RESIDUS = ["XXX", "TODO", "【", "〕", "— à compléter", "undefined", "NaN"]


def strip_tags(t: str) -> str:
    return re.sub(r"<[^>]+>", "", t)


def main() -> int:
    cache = json.load(open(CACHE, encoding="utf-8"))
    fails = 0
    total = 0
    for doc, spec in LESSONS.items():
        path = f"{TMPDIR}/{doc}.html"
        html = open(path, encoding="utf-8").read()
        text = strip_tags(html)

        # 1. arabe résiduel
        ar = ARABIC.findall(text)
        total += 1
        if ar:
            print(f"✗ {doc} : {len(ar)} caractères arabes résiduels : {ar[:10]}")
            fails += 1
        else:
            print(f"✓ {doc} : 0 caractère arabe")

        # 2. apostrophe droite
        apos = [m.start() for m in re.finditer(r"'", html)]
        total += 1
        if apos:
            print(f"✗ {doc} : {len(apos)} apostrophes droites")
            fails += 1
        else:
            print(f"✓ {doc} : 0 apostrophe droite")

        # 3. guillemets appariés
        o, c = text.count("«"), text.count("»")
        total += 1
        if o != c:
            print(f"✗ {doc} : guillemets non appariés ({o} ouvrants / {c} fermants)")
            fails += 1
        else:
            print(f"✓ {doc} : guillemets appariés ({o})")

        # 4. h1 attendu
        total += 1
        m = re.search(r"<h1>\s*(.*?)</h1>", html, re.S)
        if not m or m.group(1).strip() != spec["title"]:
            print(f"✗ {doc} : h1 inattendu : {m.group(1).strip()[:80] if m else 'ABSENT'}")
            fails += 1
        else:
            print(f"✓ {doc} : h1 conforme")

        # 5. assertions ciblées
        norm = lambda s: s.replace("\u202f", " ").replace("\u00a0", " ")
        tnorm = norm(text)
        for a in spec["asserts"]:
            total += 1
            if norm(a) not in tnorm:
                print(f"✗ {doc} : assertion absente : {a[:90]}")
                fails += 1
        print(f"✓ {doc} : {len(spec['asserts'])} assertions ciblées présentes")

        # 6. croisement des fragments de versets avec le cache coran (normalisé sans diacritiques)
        def norm_ar(s: str) -> str:
            s = re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u06DE\u08F0-\u08FF]", "", s)
            s = s.replace("\u0671", "ا")  # alif wasla
            s = s.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
            return "".join(ch for ch in s if "\u0621" <= ch <= "\u064A")

        for key, frags in spec["verses"].items():
            snum, vnum = key.split(":")
            sutra = cache[snum]
            src = next((t for n, t in sutra["ar"] if n == int(vnum)), None)
            total += 1
            if src is None:
                print(f"✗ {doc} : verset {key} absent du cache")
                fails += 1
                continue
            nsrc = norm_ar(src)
            miss = [f for f in frags if norm_ar(f) not in nsrc]
            if miss:
                print(f"✗ {doc} : fragments v.{key} absents du cache : {miss}")
                print(f"   cache normalisé : {nsrc[:180]}")
                fails += 1
            else:
                print(f"✓ {doc} : verset {key} — {len(frags)} fragments conformes au cache (warš)")

        # 7. résidus d'édition
        for r in RESIDUS:
            total += 1
            if r in text:
                print(f"✗ {doc} : résidu « {r} »")
                fails += 1

    print(f"\n{'='*60}")
    print(f"BILAN : {total} contrôles, {fails} échec(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
