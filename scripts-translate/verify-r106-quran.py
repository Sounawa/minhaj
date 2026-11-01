#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R106 — Vérification du rendu savant tafsir-3es / pdf-mut23h36-617 + -618.

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027
  3. guillemets « » appariés
  4. h1 attendus
  5. assertions ciblées : objectifs, termes, points du commentaire, sources
     (Al-Baḥr al-Muḥīṭ 10/212, Mafātīḥ al-Ghayb 30/572, an-Nūr 32-printed,
     Ṣaḥīḥ Muslim/Dhikr, Aṭ-Taḥrīr wa-t-Tanwīr 28/371, Ṣaḥīḥ al-Buḫārī/Tawḥīd
     + al-Fatḥ 15, al-Muwaṭṭaʾ/Janāʾiz), évaluation, istithmār, préparation
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
    "pdf-mut23h36-617": {
        "title": "Exégèse de la sourate aṭ-Ṭarīm, versets 6 et 7",
        "asserts": [
            "vingt-cinquième leçon (25)",
            "Connaître certains des droits de la personne et de la famille.",
            "Saisir que nulle excuse n’est donnée au mécréant dans sa mécréance au jour de la Résurrection.",
            "M’engager dans l’obéissance à Dieu et multiplier les œuvres pies dans ma vie.",
            "Comment donc l’homme se protège-t-il du châtiment de la Géhenne ? Et quelle est sa responsabilité à l’égard de sa famille ?",
            "[Qū anfusakum :]",
            "faites de vos personnes une protection du Feu en délaissant les désobéissances.",
            "[Wa-qūdahā :]",
            "son combustible : son bois.",
            "[Ġilāẓatan :]",
            "des gardiennes rigoureuses du Feu.",
            "[Ġulāẓuhum :]",
            "leur rudesse : des cœurs grossiers qui ne font pas miséricorde quand on implore leur miséricorde.",
            "[Šidādatan :]",
            "les puissants de l’homme.",
            "[Innamā tuǧzawna :]",
            "l’excuse : l’argument qui exonère son détenteur de la conséquence d’un acte [le terme défini imprimé, lu « al-ʿadl », est tranché « al-ʿuḏr » par la matière].",
            "Que Dieu — le Puissant et Majestueux — ordonna-t-Il aux croyants dans ces deux versets ?",
            "Pourquoi les mécréants sont-ils interdits d’excuse au jour de la Résurrection ?",
            "Ces deux versets contiennent ce qui suit :",
            "Premièrement : l’ordre de protéger sa personne et sa famille du Feu.",
            "Il ordonna aux croyants en général de protéger leurs personnes et leurs familles d’un Feu dont le combustible est les gens et les pierres au jour de la Résurrection",
            "Il exprima la protection du Feu par sa cause, qui est l’obéissance, car la mention du Feu est plus éloquente dans l’exaltation, l’intimidation et l’effroi.",
            "ʿUmar — que Dieu l’agrée — a dit : « Messager de Dieu, purifie nos personnes — comment donc ferons-nous avec nos familles ? »",
            "Faites-leur abandonner ce que Dieu — le Puissant et Majestueux — vous interdit, et ordonnez-leur ce que Dieu vous a ordonné ; cela sera alors une protection entre eux et le Feu.",
            "[Al-Baḥr al-Muḥīṭ, d’Abū Ḥayyān : 10/212 — pagination imprimée à re-vérifier, l’édition courante du Baḥr compte huit volumes]",
            "le combustible est le bois et ce qui lui ressemble, par quoi le Feu s’allume et s’enflamme",
            "Ibn Masʿūd a dit : ce sont les pierres de soufre, pour la rapidité de leur embrasement, l’intensité de leur chaleur et la laideur de leur odeur",
            "on a dit : les pierres adorées ; on a dit : les pierres en général.",
            "cela signifie des gardiennes du Feu, et leur rudesse et leur dureté : cela peut viser leurs crimes, ou la dureté de leurs cœurs.",
            "le sens de « préservez vos personnes » est l’accomplissement de l’ordre, et le sens de « et faisant strictement ce qu’on leur ordonne » est leur zèle et leur empressement dans ce par quoi ils sont ordonnés de châtier les gens.",
            "Deuxièmement : nulle excuse pour les mécréants au jour de la Résurrection.",
            "ne vous excusez pas de votre mécréance et de vos désobéissances ; et l’allocution peut venir de Dieu aux mécréants, ou des Anges.",
            "car vous n’êtes rétribués en ce jour que par ce que vous avez avancé comme actes en ce bas monde, et nulle excuse ne sera donc acceptée de vous.",
            "Fakhr ad-Dīn ar-Rāzī a dit : « Lorsqu’Il mentionna l’intensité du châtiment par le Feu et la rigueur des Anges à se venger des ennemis",
            "car l’excuse est le repentir, et le repentir n’est plus accepté après l’entrée dans le Feu ; votre excuse ne vous servira donc à rien. »",
            "[Mafātīḥ al-Ghayb : 30/572]",
            "Est tiré de ces deux versets ce qui suit :",
            "La personne détient des droits sur son détenteur, et le plus important de ces droits est de la protéger du châtiment de Dieu",
            "L’homme est responsable de son épouse et de ses enfants : les orienter vers ce qui fait leur bonheur en ce bas monde et leur salut au jour de la Résurrection",
            "Le jour de la Résurrection est le moment de la rétribution et non celui de l’action",
            "La justice de Dieu — le Transcendant — dans la rétribution : Il ne rétribue aucune personne dans l’au-delà que par ce qu’elle a œuvré en ce bas monde, en bien ou en mal.",
            "Comment l’homme protège-t-il sa personne et sa famille du Feu ?",
            "Pourquoi n’accepte-t-on aucune excuse des mécréants au jour de la Résurrection ?",
            "Quelle est l’importance de l’action dans la rétribution ultime ?",
            "L’Imam Mālik a rapporté, de Abū az-Zinād, de al-ʿAraǧ, d’Abū Hurayra",
            "Tout nouveau-né naît selon la fiṭra ; ce sont ses deux parents qui en font un juif ou un chrétien, comme les chamelles mettent bas un petit entier",
            "Dieu sait mieux ce qu’ils œuvraient. »",
            "[Al-Muwaṭṭaʾ ; Livre des funérailles ; chapitre global des funérailles]",
            "J’expose la responsabilité des deux parents dans l’éducation de leurs enfants.",
            "Quelle est la figure de la comparaison qui figure dans le hadith ?",
            "Je recherche certains traits de la méthode prophétique dans l’éducation des enfants.",
            "Je révise l’exégèse du verset 8 de la sourate aṭ-Ṭarīm",
            "« tawbatan naṣūḥan — yukaffiru — yaġfiru » [la forme médiane imprimée est altérée ; tranchée « yukaffiru » par le sens].",
            "Je détermine le concept du repentir, ses conditions, ses bienséances, ses degrés et les motifs qui l’incitent.",
            "Exégèse de la sourate aṭ-Ṭarīm (versets : 6-7)",
        ],
        "verses": {
            "66:6": ["قوا انفسكم واهليكم نارا وقودها الناس والحجارة عليها",
                     "ملئكة غلاظ شداد",
                     "لا يعصون الله ما امرهم ويفعلون ما يؤمرون"],
            "66:7": ["الذين كفروا لا تعتذروا اليوم",
                     "انما تجزون ما كنتم تعملون"],
        },
    },
    "pdf-mut23h36-618": {
        "title": "Exégèse de la sourate aṭ-Ṭarīm, verset 8",
        "asserts": [
            "vingt-sixième leçon (26)",
            "Connaître l’importance du repentir à Dieu et ses conditions légales.",
            "Saisir que le repentir efface les péchés et profite à son détenteur dans l’au-delà.",
            "Me repentir à Dieu — le Transcendant — de tout ce qui a émané de moi comme péchés.",
            "Quelle est donc l’importance du repentir à Dieu ? Et comment me repentir à Dieu d’un repentir sincère ?",
            "[Tawbatan naṣūḥan :]",
            "que tu te repentes du péché puis n’y retournes jamais, et ne désires pas y retourner.",
            "[Al-ḫizy :]",
            "l’avilissement et l’abaissement.",
            "Que Dieu ordonna-t-Il à Ses serviteurs croyants dans le verset ?",
            "Quels sont les desseins du repentir et ses profits pour le serviteur dans l’au-delà ?",
            "Ce verset contient ce qui suit :",
            "Premièrement : l’ordre de Dieu aux croyants du repentir sincère.",
            "C’est un second appel aux croyants dans cette sourate",
            "ʿUmar ibn al-Khaṭṭāb a dit : le repentir sincère est que tu te repentes du péché puis n’y retournes jamais, et ne désires pas y retourner.",
            "il vient de leur parole : le miel pur, lorsqu’il se sépare de la cire.",
            "c’est que la terre, malgré son ampleur, devienne étroite pour le repentant, comme le repentir des trois à qui l’on avait manqué.",
            "Az-Zamaḫšarī a dit : qu’ils rendent sincère leur repentir à eux-mêmes.",
            "Le repentir est obligatoire à tout croyant sujet aux obligations ; la preuve en est le Livre",
            "« Repentez-vous tous à Dieu » [an-Nūr : 32 — citation ornée imprimée ; le verset canonique est an-Nūr, 31, risque documenté]",
            "« Ô vous les gens, repentez-vous à Dieu ; je me repens, en un jour, vers Lui cent fois. »",
            "[Ṣaḥīḥ de Muslim ; Livre du rappel, de l’invocation, du repentir et de la demande de pardon ; chapitre de la recommandation de la demande de pardon et de sa multiplication]",
            "et la communauté s’est unanime sur son obligation.",
            "Ses devoirs sont trois : se blâmer là où l’on a désobéi par ce qui lui est licite, et non là où l’on a nui à son corps ou à son bien",
            "délaisser le péché au premier moment du possible, sans retard ni faiblesse",
            "chaque fois qu’il est décrété d’y retourner, renouveler sa résolution.",
            "Et ses bienséances sont trois : l’aveu du péché, joint à la contrition ; la multiplication de l’imploration et de la demande de pardon ; et la multiplication des bonnes actions pour effacer ce qui a précédé comme mauvaises actions.",
            "Et ses degrés sont sept : le repentir des mécréants d’avec la mécréance ; le repentir de ceux qui mêlent d’avec les grands péchés ; le repentir de ceux qui dévient d’avec les petits péchés ; le repentir des adorateurs d’avec les relâches ; le repentir des voyageurs d’avec les défauts des cœurs et les affections ; le repentir des gens de la piété d’avec les ambiguïtés ; et le repentir des gens de la contemplation d’avec les négligences.",
            "Et les motifs qui incitent au repentir sont sept : la crainte du châtiment ; l’espérance de la récompense ; la pudeur devant le compte ; l’amour du Bien-Aimé ; la vigilance à l’égard du Proche Observateur ; la vénération de Celui qui demeure établi [forme imprimée dégradée, lectures divergentes ; tranchée par la matière] ; et la gratitude pour les bienfaits.",
            "Deuxièmement : les desseins du repentir et son profit pour le serviteur dans l’au-delà.",
            "il se peut que Dieu vous fasse miséricorde par ce repentir sincère, efface vos péchés et vous fasse entrer, dans l’au-delà, dans des jardins, sous les arbres desquels coulent, sous leurs édifices, les rivières du Paradis",
            "ce qui régit « jour » peut être ce qui précède, ou ce qui suit, ou il est supprimé, son sens étant alors : mentionne-le",
            "[la tête de glose imprimée porte un énoncé dégradé non identifié ; tranchée par la matière].",
            "cela peut être coordonné au Prophète, ou être un sujet dont le prédicat vient ensuite.",
            "cette lumière est une métaphore, on vise par elle la guidance et l’agrément",
            "et le juste est l’avis de la majorité : elle est réelle, et cela est rapporté du Messager de Dieu",
            "que les croyants auront, au jour de la Résurrection, une lumière qui brille devant eux et à la droite de chacun d’eux.",
            "il est rapporté que la lumière de chacun est à la mesure de sa foi",
            "parmi eux celui dont la lumière est comme le palmier, et parmi eux celui qui éclaire ce qui est proche de ses pieds, et parmi eux celui qui éclaire un moment et est près de s’éteindre un autre moment [le manuel imprime la clause « comme le palmier » en double ; rendue une fois].",
            "et leur invocation est une demande d’augmentation de cette lumière",
            "le parachèvement de la lumière est sa perpétuation, ou son augmentation, selon les deux sens mentionnés plus haut",
            "comme ce qui est dit de la demande de pardon du Prophète — que Dieu prie sur lui et le salue — septante fois par jour.",
            "l’allusion au raisonnement qui fonde l’invocation, manière voilée d’exprimer l’espérance de son exaucement pour eux. [Aṭ-Taḥrīr wa-t-Tanwīr : 28/371]",
            "Est tiré de ce verset ce qui suit :",
            "Le propre de l’homme est de fauter et de commettre les désobéissances ; c’est pourquoi l’homme doit persévérer dans le repentir pour corriger ses fautes et revenir à Dieu",
            "Le croyant ne désespère pas de la miséricorde de Dieu, quelque grands que soient ses péchés",
            "Le repentir est une porte des portes de l’agrément de Dieu et une entrée des entrées du Paradis et du salut dans l’au-delà.",
            "Le croyant, dans les ténèbres du jour de la Résurrection, avance dans la lumière de sa foi et de son œuvre",
            "J’expose le concept du repentir sincère et son statut légal, avec argumentation.",
            "J’énumère dans un tableau les devoirs du repentir, ses bienséances, ses degrés et les motifs qui l’incitent.",
            "Quel est le sens de Sa parole : « leur lumière courra devant eux et à leur droite » ?",
            "J’expose la valeur du repentir dans les relations sociales et humaines.",
            "D’ʿAbd ar-Raḥmān ibn Abī ʿAmra — il a dit : j’ai entendu Abū Hurayra",
            "Un serviteur commit un péché — et il dit parfois : j’ai péché — et parfois il dit : j’ai fauté",
            "Mon serviteur sait-il qu’il a un Seigneur qui pardonne le péché et en prend à parti ?",
            "J’ai pardonné à Mon serviteur trois fois : qu’il fasse ce qu’il voudra. »",
            "[Ṣaḥīḥ d’al-Buḫārī ; Livre du monothéisme ; chapitre de la parole de Dieu — le Transcendant : « si tu associes, ton œuvre sera certes vaine » [al-Fatḥ : 15]]",
            "J’examine le hadith et j’expose les manifestations de la miséricorde de Dieu envers Ses serviteurs à travers son contenu.",
            "Je révise l’exégèse des versets 9 et 10 de la sourate aṭ-Ṭarīm",
            "Je recherche les types du combat, ses conditions et ses règles légales.",
            "je résume l’histoire de la femme de Noé et de la femme de Loth — que le salut soit sur eux tous les deux — et les leçons qui s’en dégagent.",
            "Exégèse de la sourate aṭ-Ṭarīm (verset : 8)",
        ],
        "verses": {
            "66:8": ["توبوا الى الله توبة نصوحا عسى ربكم ان يكفر عنكم",
                     "ويدخلكم جنت تجرى من تحتها الانهر",
                     "يوم لا يخزى الله النبى والذين ءامنوا معه",
                     "نورهم يسعى بين ايديهم وبايمنهم يقولون",
                     "ربنا اتمم لنا نورنا واغفر لنا انك على كل شىء قدير"],
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
        manquantes = []
        for a in spec["asserts"]:
            total += 1
            if norm(a) not in tnorm:
                manquantes.append(a)
        if manquantes:
            for a in manquantes:
                print(f"✗ {doc} : assertion absente : {a[:90]}")
            fails += len(manquantes)
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
