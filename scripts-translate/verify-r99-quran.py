#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R99 — Vérification du rendu savant tafsir-3es / pdf-mut23h36-601 + -602.

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027
  3. guillemets « » appariés
  4. h1 attendu
  5. assertions ciblées : objectifs, termes, points du commentaire, sources
     (al-Bayhaqī Šaʿb al-īmān, al-Buḫārī ×2, al-Nasafī 3/256 + 3/258,
     al-Tasẖīl 2/124 + 1/189, Ibn Kathīr 7/210 + 7/211, al-Rāzī 27/603-604,
     an-Nisāʾ 31, Āl ʿImrān 159, an-Nūr 15-22, Nūḥ 10-12), évaluation,
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
    "pdf-mut23h36-601": {
        "title": "Exégèse de la sourate al-Shūrā, versets 28 à 32",
        "asserts": [
            "neuvième leçon (9)",
            "les causes de l’épreuve par les calamités et les épreuves dures",
            "bienfaits de la terre et de la mer",
            "[Al-ǧawārī :] les navires.",
            "[Maḥīṣ :] une issue et un refuge.",
            "Premièrement : les péchés sont la cause des calamités",
            "Deuxièmement : la navigation des grands navires est l’une des preuves les plus grandes de Dieu",
            "« Tout malheur qui vous atteint est dû à ce que vos mains ont acquis » (30)",
            "ni coupure de bâton, ni trébuchement de pied, ni crispation de nerf, sinon par un péché",
            "[Šaʿb al-īmān d’al-Bayhaqī, chapitre de la patience face aux calamités",
            "jusqu’à l’épine qui le pique",
            "[Ṣaḥīḥ d’al-Buḫārī ; kitāb al-marḍā, bāb mā ǧāʾa fī kaffārāt al-marḍ]",
            "sans le fāʾ, au sens que ce qui vous atteint est le régime de [la particule]",
            "les autres lecteurs ont lu au naṣb",
            "porte peu de regard sur la bienveillance de son Seigneur envers lui",
            "ses offenses dans l’obéissance sont plus nombreuses que ses offenses dans les désobéissances",
            "[Tafsīr d’al-Nasafī : 3/256]",
            "vous n’avez ni issue ni refuge sur la terre ni dans le ciel",
            "[al-Tasẖīl : 2/124]",
            "« al-ǧawārī » est le pluriel de ǧāriya, qui est le navire",
            "« ka-l-aʿlām » est le pluriel de ʿalam, qui est la montagne",
            "l’énumération de la grâce dans l’envoi des vents, ou une menace par leur apaisement",
            "Il les fait périr par noyade, du fait de la violence des vents tempétueux",
            "c’est une lecture irrégulière, et il ne convient pas de charger le Coran de ce qui la contient",
            "coordonné à une justification sous-entendue, dont le sens serait : pour Se venger d’eux",
            "[Maryam, v. 20]",
            "L’obligation de s’éloigner des péchés et des désobéissances pour être sauvé des calamités de la duniyā et de l’āḫira",
            "nul n’échappe à Sa justice et à Sa toute-puissance",
            "[an-Nūr, 15-22]",
            "[Nūḥ, 10-12]",
            "une pluie abondante",
            "leur relation avec l’épreuve, l’augmentation de la subsistance et sa diminution",
            "J’explique les expressions que le professeur (la professeure) m’indiquera.",
            "Quel est le visé par les grands péchés mentionnés dans les versets ?",
        ],
        "verses": {
            "42:28": ["ينزلالغيث", "منبعدماقنطوا", "وينشر رحمته", "الولىالحميد"],
            "42:29": ["ومنءايتهخلقالسموتوالارض", "ومابثفيهمامندابة",
                      "وهوعلىجمعهم", "اذايشاءقدير"],
            "42:30": ["ومااصبكممنمصيبة", "فبما كسبت ايديكم", "ويعفوا عن كثير"],
            "42:31": ["وماانتمبمعجزينفىالارض", "من دون الله من ولى", "ولانصير"],
            "42:32": ["الجوارفىالبحركالاعلم"],
            "24:15": ["تلقونه", "بافواهكم", "وعنداللهعظيم"],
            "24:19": ["انتشيعالفحشة", "فىالذينءامنوا"],
            "24:22": ["الا تحبون", "ان يغفر الله لكم"],
            "71:10": ["فقلتاستغفروا", "انهكانغفارا"],
            "71:11": ["يرسل السماء", "عليكم", "مدرارا"],
            "71:12": ["ويمددكم", "بأمول", "وبنين", "جنت", "انهرا"],
        },
    },
    "pdf-mut23h36-602": {
        "title": "Exégèse de la sourate al-Shūrā, versets 33 à 36",
        "asserts": [
            "dixième leçon (10)",
            "les principaux grands péchés que le responsable doit éviter",
            "Répondre à Dieu — qu’Il soit glorifié — par son obéissance, Son adoration et l’évitement de Sa désobéissance",
            "[Al-fawāḥiš :] toute action et toute parole répréhensibles.",
            "[Šūrā :] ils délibèrent entre eux sur l’avis à tenir.",
            "[Yantaṣirūna :] ils obtiennent leur droit sans injustice.",
            "Premièrement : l’ornement des gens de la foi par l’évitement des grands péchés",
            "Deuxièmement : l’ornement des gens de la foi par la réponse à Dieu — qu’Il soit glorifié — et par Son adoration",
            "« Tout ce qui vous a été donné n’est que jouissance de la vie présente » (36)",
            "ne vous en enorgueillissez pas",
            "[Tafsīr d’Ibn Kathīr : 7/210]",
            "tout péché que Dieu a scellé d’un Feu, d’une malédiction ou d’une colère",
            "depuis le début de la sourate an-Nisāʾ",
            "Si vous évitez les grands péchés qui vous sont interdits, Nous effacerons vos mauvaises actions et vous entrerons par une entrée généreuse",
            "[an-Nisāʾ, 31]",
            "dix-sept",
            "« Évitez les sept choses qui perdent. »",
            "L’associationnisme envers Dieu, la sorcellerie",
            "le meurtre de la personne que Dieu a rendue sacrée hors du droit",
            "la fuite le jour de la marche en campagne",
            "la calomnie des femmes croyantes insoucieuses",
            "[Ṣaḥīḥ d’al-Buḫārī ; kitāb al-ḥudūd, bāb ramy al-muḥṣanāt]",
            "la désobéissance envers les parents, le témoignage mensonger, le serment déloyal",
            "[al-Tasẖīl : 1/189, avec adaptation]",
            "l’indulgence et le pardon envers celui qui leur a fait du tort, au moment de leur colère",
            "« et délibère avec eux à propos des affaires » [Āl ʿImrān, 159]",
            "[Tafsīr d’Ibn Kathīr : 7/211]",
            "ce verset fut révélé au sujet des Anṣār",
            "une allusion à la mention des califes bien guidés",
            "se limitent, dans leur riposte, à ce que Dieu — qu’Il soit exalté — leur a permis",
            "[Tafsīr d’al-Nasafī : 3/258]",
            "L’importance de la délibération (šūrā) parmi les musulmans dans la gestion de leurs affaires",
            "une jouissance vile et appelée à disparaître",
            "[Mafātīḥ al-ghayb d’al-Rāzī : 27/603-604, avec adaptation]",
            "être parmi ceux qui se remettent à la faveur de Dieu",
            "ne pas commettre d’excès, en s’efforçant de récupérer les droits spoliés",
            "cinq qualités énumérées par al-Rāzī",
            "des versets 37 à 40 de la sourate al-Shūrā",
            "les valeurs d’amour, de tolérance et de paix dans la société présentes dans les versets",
        ],
        "verses": {
            "42:33": ["ان يشا يسكن الريح", "فيظللنرواكد", "على ظهره",
                      "لكل صبار شكور"],
            "42:34": ["او يوبقهن بما كسبوا", "ويعف عن كثير"],
            "42:35": ["الذين يجدلون فى ءايتنا", "مالهممن محيص"],
            "42:36": ["فمااوتيتممن شىء", "فمتع الحيوة الدنيا",
                      "وما عند الله خيرو ابقى", "وعلىربهميتوكلون"],
            "4:31": ["كبائر ما تنهون عنه", "سياتكم"],
            "3:159": ["وشاورهمفىالامر"],
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
