#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R94 — Vérification du rendu savant tafsir-2es / pdf-mut23h33-565 + -566.

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027
  3. guillemets « » appariés
  4. h1 attendu
  5. assertions ciblées : objectifs, termes, points du commentaire, sources
     (Musnad Aḥmad, Muslim, Bukhārī, Ibn Kathīr 6/551+6/552+6/556, Nasafī 3/76,
     Rāzī 26/239, al-Aʿrāf 23 corrigé du 22 imprimé, Tirmidhī), évaluation,
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
    "pdf-mut23h33-565": {
        "title": "Sourate Fāṭir, versets 32-35 : livre du Tafsīr à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy, deuxième année collégiale — leçon 10",
        "asserts": [
            "du livre du Tafsīr fondé sur le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy",
            "(leçon 10)",
            "Reconnaître les serviteurs de Dieu qu’Il a élus et leur rétribution le jour de la Résurrection",
            "Discerner les catégories des serviteurs de Dieu qu’Il a élus",
            "devanciers dans les œuvres bonnes",
            "[Awrathnā (Nous avons donné en héritage)]",
            "[Ẓāliman li-nafsihi (injuste envers son âme)]",
            "[Muqtaṣid (modéré)]",
            "[Al-ḥazan (l’affliction)]",
            "[Dār al-muqāma (la demeure de la résidence)]",
            "[Naṣab (la fatigue)]",
            "[Lughūb (l’épuisement)]",
            "Premièrement : l’honneur que Dieu fait à Ses serviteurs élus",
            "Deuxièmement : la rétribution de ceux que Dieu — qu’Il soit exalté — a élus parmi Ses serviteurs",
            "Troisièmement : les desseins (maqāṣid) des versets",
            "« puis Nous avons fait hériter le Livre à ceux de Nos serviteurs que Nous avons élus » (32)",
            "« parmi eux est l’injuste envers lui-même, parmi eux le modéré, et parmi eux le devancier dans les œuvres bonnes, par la permission de Dieu » (32)",
            "« des jardins d’ʿAdn qu’ils entreront » (33)",
            "« Ils y seront parés » (33)",
            "« et leur vêtement, là-bas, est de soie » (33)",
            "« et ils diront : Louange à Dieu qui a écarté de nous l’affliction » (34)",
            "« que ne nous touchent, là-bas, ni fatigue ni épuisement » (35)",
            "par sa présence dans le hadith et par la grandeur de ceux qui l’ont tenu",
            "[Musnad de l’imam Aḥmad, complément du Musnad des Anṣār, hadith d’Abū al-Dardāʾ]",
            "l’injuste est le mécréant, le modéré est le croyant désobéissant et le devancier est le pieux",
            "afin qu’il ne désespère pas",
            "afin qu’il ne s’admire pas lui-même",
            "Al-Zamakhsharī a dit : il renvoie spécialement au devancier",
            "l’opinion des muʿtazilites au sujet de la menace",
            "« La parure atteint, chez le croyant, là où atteint l’ablution »",
            "[Ṣaḥīḥ Muslim, livre de la pureté, chapitre : la parure atteint là où atteint l’ablution]",
            "« C’est pour cela qu’elle leur était interdite en ce bas monde",
            "[Ṣaḥīḥ al-Bukhārī, livre du vêtement",
            "[Tafsīr al-Qurʾān al-ʿaẓīm d’Ibn Kathīr : 6/551]",
            "Il pardonne les fautes graves, si nombreuses soient-elles",
            "[Madārik al-tanzīl wa-ḥaqāʾiq al-taʾwīl d’al-Nasafī : 3/76]",
            "« Aucun de vous n’entrera au Paradis par ses œuvres »",
            "« Pas même toi, ô Messager de Dieu ? »",
            "[Ṣaḥīḥ Muslim, livre de la description de la Résurrection, du Paradis et du Feu",
            "“Le fornicateur ne fornique pas tandis qu’il demeure croyant”",
            "(al-Aʿrāf, v. 23)",
            "[Mafātīḥ al-ghayb, de Fakhr al-Dīn al-Rāzī : 26/239]",
            "comment l’injuste envers lui-même peut-il être de ceux que Dieu — qu’Il soit exalté — a élus parmi Ses serviteurs ?",
            "les versets 36 et 37 de la sourate Fāṭir",
            "yuqḍā ʿalayhim — kafūr — yaṣṭarikhūna — tuʿammarukum",
            "Quelle est la finalité du durcissement du châtiment des mécréants le jour de la Résurrection ?",
        ],
        "verses": {
            "35:32": ["ثم اورثنا الكتب", "الذين اصطفينا من عبادنا", "فمنهم ظالم لنفسه",
                      "ومنهم مقتصد", "ومنهم سابق", "باذن الله", "ذلك هو الفضل الكبير"],
            "35:33": ["يدخلونها", "يحلون فيها من اساور", "من ذهب ولؤلؤا", "ولباسهم فيها حرير"],
            "35:34": ["وقالوا الحمد لله", "اذهب عنا الحزن", "ان ربنا لغفور شكور"],
            "35:35": ["احلنا دار المقامة", "من فضله", "لا يمسنا فيها نصب", "ولا يمسنا فيها لغوب"],
            "7:23": ["ربنا ظلمنا انفسنا"],
        },
    },
    "pdf-mut23h33-566": {
        "title": "Sourate Fāṭir, versets 36-37 : livre du Tafsīr à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy, deuxième année collégiale — leçon 11",
        "asserts": [
            "du livre du Tafsīr fondé sur le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy",
            "(leçon 11)",
            "Reconnaître le sort des mécréants et leur rétribution le jour de la Résurrection",
            "Déduire les raisons pour lesquelles les mécréants demandent le retour en ce bas monde",
            "Éviter les caractères des mécréants afin d’être sauvé du châtiment de Dieu",
            "[Yuqḍā ʿalayhim (la sentence est prononcée sur eux)]",
            "[Kafūr (ingrat)]",
            "[Yaṣṭarikhūna (ils crient au secours)]",
            "[Tuʿammarukum (Nous vous faisons vivre longtemps)]",
            "Premièrement : le sort des mécréants le jour de la Résurrection",
            "Deuxièmement : les desseins (maqāṣid) des deux versets",
            "« et ceux qui ont mécru, à eux le Feu de la Géhenne » (36)",
            "« Ceux qui récitent le Livre de Dieu » (29)",
            "« on ne prononcera pas sur eux la sentence qui les fera mourir » (36)",
            "« et on ne les allègera pas de son châtiment » (36)",
            "« C’est ainsi que Nous rétribuons tout ingrat »",
            "« tandis qu’ils y crient au secours : Seigneur, fais-nous sortir ! que nous fassions des œuvres bonnes, autres que celles que nous faisions » (37)",
            "« N’avions-Nous pas prolongé vos vies pour que celui qui voulait se rappeler puisse se rappeler ? » (37)",
            "« et l’avertisseur est venu à vous » (37)",
            "« Goûtez donc ! Pas de secoureur pour les injustes » (37)",
            "l’aveu de la mauvaise œuvre et le regret de celle-ci",
            "« Celui que Dieu fait vivre soixante années, Dieu s’est acquitté de l’excuse envers lui quant à la durée de vie »",
            "[Musnad de l’imam Aḥmad, musnad des Compagnons les plus nombreux en récits, musnad d’Abū Hurayra]",
            "« Les âges de ma communauté vont de soixante à soixante-dix ; et les moins nombreux sont ceux qui dépassent cela »",
            "[Sunan al-Tirmidhī, chapitres de l’ascétisme",
            "le cheveu blanc, car il annonce la mort",
            "la première opinion est la plus apparente",
            "[Tafsīr al-Qurʾān al-ʿaẓīm, d’Ibn Kathīr : 6/556]",
            "de châtiment, de tourment et de fardeaux",
            "“Ils crieront : ô Mālik ! que ton Seigneur tranche notre sort ! Il dira : vous demeurerez” (az-Zukhruf, v. 77)",
            "“les criminels sont, dans le châtiment de la Géhenne, éternels ; on ne les épargne pas, et ils y sont désespérés” (az-Zukhruf, v. 74-75)",
            "« chaque fois qu’elle s’éteint, Nous leur accroissons un Feu ardent » (al-Isrāʾ, v. 97)",
            "“Goûtez donc ! Nous ne vous accroîtrons que le châtiment” (an-Nabāʾ, v. 30)",
            "Quant aux gens du Feu qui en sont les gens, ils n’y meurent pas et n’y vivent pas",
            "[Tafsīr al-Qurʾān al-ʿaẓīm, d’Ibn Kathīr : 6/552]",
            "quel est le contenu commun aux versets rapportés dans le texte ?",
            "les versets 38 à 40 de la sourate Fāṭir",
            "bi-dhāt aṣ-ṣudūr",
            "la liste imprimée du manuel comporte quatre expressions de plus, rendues illisibles par le scan",
            "les arguments attestant l’unicité de Dieu — qu’Il soit exalté",
        ],
        "verses": {
            "35:36": ["والذين كفروا لهم نار جهنم", "لا يقضى عليهم فيموتوا",
                      "ولا يخفف عنهم من عذابها", "كذلك نجزى كل كفور"],
            "35:37": ["وهم يصطرخون فيها", "ربنا اخرجنا", "نعمل صلحا", "الذى كنا نعمل",
                      "اولم نعمركم ما يتذكر فيه من تذكر", "وجاءكم النذير", "فذوقوا فما للظلمين من نصير"],
            "35:29": ["ان الذين يتلون كتب الله"],
            "43:77": ["ليقض علينا ربك", "قال انكم مكثون"],
            "43:74": ["المجرمين فى عذاب جهنم خلدون"],
            "43:75": ["لا يفتر عنهم", "وهم فيه مبلسون"],
            "17:97": ["كلما خبت زدنهم سعيرا"],
            "78:30": ["فذوقوا فلن نزيدكم الا عذابا"],
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
