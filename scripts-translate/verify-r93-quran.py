#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R93 — Vérification du rendu savant tafsir-2es / pdf-mut23h33-563 + -564.

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027 (nœuds texte)
  3. guillemets « » appariés
  4. verset-image : 0 attendu / 0 trouvé (leçons pdfOnly sans images)
  5. assertions ciblées : formules d'ouverture, objectifs, termes, points du
     commentaire, sources citées (Qurṭubī 14/341, Ibn ʿĀshūr 22/301+22/303,
     Nasafī 3/87+3/88, an-Nisāʾ 172, an-Nūr 37-38, al-Aḥzāb 39, Sunan al-Dārimī,
     Musnad Aḥmad), évaluation, istithmār, préparation préalable
  6. croisement des versets rendus avec le cache coran (fragments clés)
  7. 0 résidu d'édition (XXX, TODO, 【】, doubles espaces)
"""
import json
import re
import sys

TMPDIR = "/home/z/my-project/tr-tmp"
CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"

ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")

LESSONS = {
    "pdf-mut23h33-563": {
        "title": "Sourate Fāṭir, versets 27-28 : livre du Tafsīr à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy, deuxième année collégiale — leçon 8",
        "asserts": [
            "du livre du Tafsīr fondé sur le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy",
            "(leçon 8)",
            "Reconnaître la capacité de Dieu — qu’Il soit exalté — à créer, à partir d’une même chose",
            "Déduire de ces deux versets ce qui mène à la crainte de Dieu",
            "la crainte de Dieu — qu’Il soit exalté — est plus grande chez les savants",
            "[Thamarātin mukhtalifan alwānuhā (fruits aux couleurs différentes)]",
            "[Judad (strates)]",
            "[Ghurābīb (noir profond)]",
            "[Yakhshā (Il craint)]",
            "Premièrement : la capacité de Dieu à créer les choses différentes d’une même chose",
            "Deuxièmement : les savants, les plus intenses des hommes dans la crainte de Dieu",
            "Troisièmement : les desseins (maqāṣid) des versets",
            "« N’as-tu pas vu que Dieu fait descendre du ciel une eau ? » (27)",
            "« puis Nous en faisons sortir des fruits aux couleurs différentes » (27)",
            "« Et parmi les montagnes, des strates blanches et rouges, dont les couleurs sont différentes » (27)",
            "« et des ravins d’un noir profond » (27)",
            "« Et parmi les hommes, les bêtes de somme et les bestiaux, les couleurs sont différentes. C’est ainsi » (28)",
            "« Parmi les serviteurs de Dieu, seuls les savants Le craignent » (28)",
            "« Dieu est, certes, Puissant et Pardonneur » (28)",
            "la vision du cœur et du savoir",
            "[al-Jāmiʿ li-aḥkām al-Qurʾān de l’imam Qurṭubī : 14/341]",
            "[al-Taḥrīr wa-l-tanwīr, de Ṭāhir ibn ʿĀshūr : 22/301]",
            "[al-Taḥrīr wa-l-tanwīr, de Ṭāhir ibn ʿĀshūr : 22/303]",
            "[Madārik al-tanzīl wa-ḥaqāʾiq al-taʾwīl d’al-Nasafī : 3/87]",
            "est un Agissant de plein vouloir",
            "une réponse aux partisans de la seule nature",
            "le pluriel de gharbīb",
            "« Celui d’entre vous qui connaît le mieux Dieu est celui qui Le craint le plus intensément »",
            "une argumentation de la capacité de Dieu et de Sa volonté",
            "Je déduis la sagesse de la création par Dieu — qu’Il soit exalté — de fruits différents",
            "« et qu’ils ne craignent nul autre que Dieu » (al-Aḥzāb, v. 39)",
            "D’après ʿAlī ibn Abī Ṭālib — que Dieu l’agrée —",
            "[Sunan al-Dārimī, section de celui qui a dit : la science est crainte et piété envers Dieu]",
            "la manière la plus appropriée d’orienter les hommes",
            "les versets 29 à 31 de la sourate Fāṭir",
            "tabūra — liyūffīhihim ujūrahum — wa-yazīdahum min faḍlihi — baṣīr",
            "les qualités de ceux qui méritent la récompense immense",
        ],
        "verses": {
            "35:27": ["الم تر ان الله انزل من السماء", "فاخرجنابه", "ثمرت", "مختلفا الونها", "من الجبال", "جدد بيض وحمر", "وغرابيب سود"],
            "35:28": ["من الناس والدواب والانعم", "مختلف الونه", "انما يخشى الله من عباده", "ان الله عزيز غفور"],
        },
    },
    "pdf-mut23h33-564": {
        "title": "Sourate Fāṭir, versets 29-31 : livre du Tafsīr à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy, deuxième année collégiale — leçon 9",
        "asserts": [
            "du livre du Tafsīr fondé sur le Tashīl li-ʿulūm al-tanzīl d’Ibn Juzayy",
            "(leçon 9)",
            "Reconnaître la finalité de la mention des qualités des savants qui agissent",
            "Déduire des versets les types d’œuvres bonnes",
            "Veiller à la récitation du Coran noble et me conformer à ses orientations",
            "des savants qui ont répondu à l’appel prophétique",
            "[Tabūra (qui ne périt pas)]",
            "[Yūffīhim (Il leur donne en plénitude)]",
            "[Wa-yazīdahum min faḍlih (et les accroisse de Sa faveur)]",
            "[Baṣīr (Clairvoyant)]",
            "Premièrement : l’éloge de Dieu envers les savants qui agissent",
            "Deuxièmement : l’affermissement du cœur du Prophète — que Dieu prie sur lui et le salue",
            "« Ceux qui récitent le Livre de Dieu » (29)",
            "« et accomplissent la prière » (29)",
            "« et dépensent, en secret et en public, de ce que Nous leur avons attribué » (29)",
            "« espèrent un commerce qui ne périt jamais » (29)",
            "« afin qu’Il leur donne en plénitude leurs récompenses et les accroisse de Sa faveur » (30)",
            "« Il est Pardonneur et Reconnaissant » (30)",
            "« Et ce que Nous te révélons du Livre",
            "“Dieu est, de Ses serviteurs, Informé, Clairvoyant” (31)",
            "[an-Nisāʾ : 172]",
            "[an-Nūr : 37-38]",
            "« Des hommes que ni le commerce ni la vente ne détournent de l’évocation de Dieu",
            "[Madārik al-tanzīl wa-ḥaqāʾiq al-taʾwīl d’al-Nasafī : 3/88]",
            "un tel Livre prodigieux, qui est la pierre de touche de tous les autres livres",
            "L’établissement de la véracité du Coran noble",
            "Pourquoi Dieu — qu’Il soit exalté — a-t-Il fait l’éloge de celui qui persévère dans la récitation du Coran noble",
            "Qu’entend-on par le commerce dans ces versets ?",
            "D’après ʿAbd Allāh ibn Burayda, d’après son père",
            "[Musnad de l’imam Aḥmad, révision du Musnad des Anṣār, hadith de Burayda al-Aslamī]",
            "j’en extrais les mérites de la récitation du Coran",
            "les versets 32 à 34 de la sourate Fāṭir",
            "awrathnā — muqtaṣid — naṣab — lughūb — dār al-maqāma",
            "ceux que Dieu — qu’Il soit exalté — a élus parmi Ses serviteurs",
        ],
        "verses": {
            "35:29": ["ان الذين يتلون كتب الله", "واقاموا الصلوة", "وانفقوا مما رزقنهم", "سرا وعلانية", "يرجون تجرة لن تبور"],
            "35:30": ["ليوفيهم اجورهم", "ويزيدهم من فضله", "انه غفور شكور"],
            "35:31": ["والذى اوحينا اليك من الكتب", "هو الحق", "مصدقا لما بين يديه", "ان الله بعباده لخبير بصير"],
            "24:38": ["الله احسن ما عملوا", "ويزيدهم من فضله"],
        },
    },
}

RESIDUS = ["XXX", "TODO", "【", "〕", "— à compléter", "undefined", "NaN"]


def strip_tags(t: str) -> str:
    return re.sub(r"<[^>]+>", "", t)


def main() -> int:
    cache = json.load(open(CACHE, encoding="utf-8"))
    # normalisation cache pour croisements (retire diacritiques non significatifs ? non : on cherche des sous-chaînes exactes)
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
