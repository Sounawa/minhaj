#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R105 — Vérification du rendu savant tafsir-3es / pdf-mut23h36-615 + -616.

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027
  3. guillemets « » appariés
  4. h1 attendus
  5. assertions ciblées : objectifs, termes, points du commentaire, sources
     (Tafsīr al-Khāzin 4/313 + 4/316, Ṣaḥīḥ al-Buḫārī/Livre du mariage + tafsīr,
     Mafātīḥ al-Ghayb 30/571, Tafsīr al-Ālūsī 28/155, al-Tasyīl 2/152,
     Tafsīr al-Qāsimī 9/275, Sunan at-Tirmiḏī), évaluation, istithmār, préparation
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
    "pdf-mut23h36-615": {
        "title": "Exégèse de la sourate aṭ-Ṭarīm, versets 3 et 4",
        "asserts": [
            "vingt-troisième leçon (23)",
            "Connaître que Dieu a informé Son Prophète — que Dieu prie sur lui et le salue — de la divulgation de son secret et de qui l’avait divulgué.",
            "Saisir le reproche que le Prophète — que Dieu prie sur lui et le salue — adressa à l’une de ses épouses, et la délicatesse de ce reproche.",
            "Renforcer ma foi dans la véracité du Livre de Dieu et dans la véracité de Son Prophète Muḥammad — que Dieu prie sur lui et le salue.",
            "Comment donc le Prophète — que Dieu prie sur lui et le salue — reprocha-t-il à Ḥafṣa la divulgation de son secret ?",
            "[Baʿḍi azwāǧihi :]",
            "l’une de ses épouses : Ḥafṣa.",
            "[Wa-aẓharahu llāhu ʿalayhi :]",
            "Il le lui manifesta : Il l’informa de la chose et de sa divulgation.",
            "[Ṣaġat :]",
            "elle dévia, elle s’inclina hors du droit.",
            "[Mawlāhu :]",
            "son protecteur et son défenseur.",
            "Pour quoi le Prophète — que Dieu prie sur lui et le salue — reprocha-t-il à Ḥafṣa — que Dieu l’agrée ?",
            "Premièrement : le secret que Ḥafṣa — que Dieu l’agrée — divulgua, et le reproche qu’elle en reçut",
            "On a divergé sur le sens du ḥadīth dans le verset, selon deux avis : le premier : il a dit : Abū Bakr et ʿUmar dirigeront l’ordre après moi.",
            "Le second : il a dit : j’ai bu du miel ; on a dit : autre chose.",
            "Le sens de Sa parole « l’une de ses épouses » est Ḥafṣa — que Dieu l’agrée.",
            "il châtia Ḥafṣa de la divulgation de son secret en la répudiant, puis Dieu lui ordonna de la reprendre, et il la reprit. On a dit : il ne la répudia pas.",
            "Al-Khāzin a dit dans son exégèse : « il s’irrita de la divulgation de son secret et la châtia de cela en la répudiant",
            "si la famille d’al-Khaṭṭāb eût possédé quelque bien, le Messager de Dieu — que Dieu prie sur lui et le salue — ne t’aurait pas répudiée",
            "Gabriel vint alors et dit : ne la répudie pas, car elle est grande jeûneuse et grande dévote, et elle est des femmes du Paradis. »",
            "[Tafsīr d’al-Khāzin : 4/313]",
            "le sujet y est omis, et c’est ʿĀʾiša [l’énoncé imprimé porte à ce point une altération ; le sujet omis est le fāʿil, rendu par le sens].",
            "il reprocha à Ḥafṣa une partie et passa sur une partie, par pudeur et vénération",
            "et al-Kisāʾī a lu « ʿarafa » sans intensification.",
            "elle se tut et se soumit.",
            "Deuxièmement : l’exhortation et l’avertissement de Ḥafṣa et ʿĀʾiša — que Dieu les agrée",
            "Ce discours s’adresse à ʿĀʾiša et à Ḥafṣa ; leur repentir porte sur ce qui advient d’elles dans l’affaire de l’interdiction du miel.".replace("advient", "advint"),
            "Le sens de « ont fléchi » : elles dévièrent du droit ; et Ibn Masʿūd a lu : « elles s’écartèrent ».",
            "il est advenu de vous deux ce qui rend le repentir nécessaire.",
            "il a qui le défend, et c’est Dieu — Puissant et Majestueux.",
            "peut avoir le sens de seigneur suprême : on s’arrête alors sur « son protecteur », et « Gabriel » est sujet, « Michel » son prédicat",
            "il peut aussi avoir le sens d’allié défenseur : « Gabriel » est alors coordonné, et l’on s’arrête sur « les vertueux d’entre les croyants »",
            "le sens de défenseur est plus convenable à cette situation, car cela est honneur pour le Prophète — que Dieu prie sur lui et le salue — et vénération",
            "Dieu — le Très-Haut — est protecteur de toute Sa création en ce sens, si bien qu’il n’y a en cela aucune préséance manifeste pour lui.",
            "Messager de Dieu, qu’y a-t-il de pénible pour toi dans l’affaire des femmes ? Si tu les as répudiées, Dieu avec toi, Ses anges, Gabriel avec toi, Abū Bakr avec toi et moi avec toi",
            "le verset descendit donc en accord avec la parole d’ʿUmar, et la parole implique la défense avec lui.",
            "Selon l’avis du singulier, c’est Abū Bakr ; on a dit : ʿAlī ibn Abī Ṭālib. Selon l’avis du pluriel, il s’agit en général de tout vertueux.",
            "Il incombe à celui qui détient un secret de le garder ; car les musulmans demeurent soumis aux conditions qu’ils posent.",
            "Il est bon de la délicatesse dans le reproche entre les époux, pour préserver l’existence du foyer — en s’inspirant de la vie du Présélectionné — que Dieu prie sur lui et le salue.",
            "Le Coran noble est parole de Dieu en vérité et en sincérité",
            "Pourquoi Ḥafṣa — que Dieu l’agrée — divulgua-t-elle le secret du Messager de Dieu — que Dieu prie sur lui et le salue ?",
            "Comment ces valeurs prophétiques ont-elles un effet dans ma vie conjugale ?",
            "Je n’ai cessé de désirer interroger ʿUmar ibn al-Khaṭṭāb sur les deux femmes du Prophète — que Dieu prie sur lui et le salue",
            "bravo pour toi, ô Ibn ʿAbbās — ce sont ʿĀʾiša et Ḥafṣa…",
            "[Ṣaḥīḥ d’al-Buḫārī ; Livre du mariage ; chapitre de l’exhortation par l’homme de sa fille au comportement de son mari]",
            "Pourquoi Ibn ʿAbbās chercha-t-il à interroger spécifiquement ʿUmar ibn al-Khaṭṭāb sur ce verset ?",
            "Je révise l’exégèse du verset 5 de la sourate aṭ-Ṭarīm",
            "Je détermine les qualités requises de l’épouse vertueuse à partir du verset.",
        ],
        "verses": {
            "66:3": ["ٱلنَّبِىُّ إِلَىٰ بَعْضِ أَزْوَٰجِهِ حَدِيثًۭا فَلَمَّا نَبَّأَتْ بِهِۦ",
                     "عَرَّفَ بَعْضَهُۥ وَأَعْرَضَ عَنۢ بَعْضٍ",
                     "مَنْ أَنۢبَأَكَ هَٰذَا",
                     "قَالَ نَبَّأَنِىَ ٱلْعَلِيمُ ٱلْخَبِيرُ"],
            "66:4": ["فَقَدْ صَغَتْ قُلُوبُكُمَا",
                     "وَجِبْرِيلُ وَصَٰلِحُ ٱلْمُؤْمِنِينَ",
                     "وَٱلْمَلَٰٓئِكَةُ بَعْدَ ذَٰلِكَ ظَهِيرٌ"],
        },
    },
    "pdf-mut23h36-616": {
        "title": "Exégèse de la sourate aṭ-Ṭarīm, verset 5",
        "asserts": [
            "vingt-quatrième leçon (24)",
            "Connaître la consolation que Dieu — le Transcendant — fit à Son Prophète, pour écarter de lui le souci et le dépit.",
            "Déduire le reproche adressé aux mères des croyants, contenu dans le verset.",
            "M’orner des valeurs de l’humilité et du respect dans mes relations familiales et sociales.",
            "Pourquoi donc Dieu — Puissant et Majestueux — menaça-t-il les femmes du Messager de Dieu — que Dieu prie sur lui et le salue ?",
            "[Qānitātin :]",
            "dévotes.",
            "[Tāʾibātin :]",
            "repentantes de tous les péchés, sans qu’elles y retombent.",
            "[ʿĀbidātin :]",
            "très dévotes.",
            "[Sāʾiḥātin :]",
            "jeûneuses.",
            "[Ṯayyibātin :]",
            "la thayyib est celle qui s’est mariée et a quitté son mari après l’avoir connue.",
            "[Wa-abkāran :]",
            "la vierge est la femme qui n’a jamais été approchée.",
            "De quoi Dieu — Puissant et Majestueux — consola-t-il Son Prophète — que Dieu prie sur lui et le salue — après les soucis qui l’atteignirent ?",
            "ce verset contint davantage de discipline divine des mères des croyants et de menace sévère à leur égard",
            "« Ce verset est défense pour le Prophète — que Dieu prie sur lui et le salue — et consolation pour lui",
            "ʿUmar ibn al-Khaṭṭāb — que Dieu l’agrée — a dit : « Les femmes du Prophète — que Dieu prie sur lui et le salue — s’unirent dans la jalousie contre lui",
            "[Ṣaḥīḥ d’al-Buḫārī ; Livre de l’exégèse du Coran ; chapitre de Sa parole : « il se peut que son Seigneur, s’Il vous répudie, lui donne en échange des épouses meilleures que vous, musulmanes, croyantes, obéissantes, repentantes, adoratrices, jeûneuses, déjà mariées ou vierges »]",
            "« ʿAsā » vient pour l’espérance ; mais dans la parole de Dieu — le Très-Haut — il vient pour l’affirmation",
            "son répond est ici suspendu à une condition qui n’eut pas lieu, qui est leur répudiation",
            "elles demeurent donc ses épouses en ce bas monde et dans l’au-delà.",
            "Al-Ālūsī a dit : « ʿasā dans Sa parole — le Très-Haut — porte l’obligation ; et l’obligation, ici, n’intervient qu’après la réalisation de la condition. »",
            "[Tafsīr d’al-Ālūsī : 28/155]",
            "Dieu exposa ensuite les qualités de ces épouses ; ce sont des qualités de perfection dans l’épouse vertueuse",
            "Dieu — Puissant et Majestueux — mentionna ainsi huit qualités pour ces épouses",
            "l’islam est l’abandon, et l’īmān est l’attestation",
            "Ibn Taymiyya — que Dieu lui fasse miséricorde — a exposé la relation entre l’īmān et l’islam, et a dit : « tous deux s’emploient selon trois aspects",
            "par la différence du sens, comme dans Sa parole : “Vous n’avez pas encore la foi. Dites plutôt : Nous nous sommes simplement soumis” (al-Ḥuǧurāt, 14)",
            "par l’accord, de par leur réunion, comme dans Sa parole : “Nous en fîmes sortir alors ce qu’il y avait comme croyants, mais Nous n’y trouvâmes qu’une seule maison de gens soumis” (aḏ-Ḏāriyāt, 35-36)",
            "et par la science : l’islam est plus général, car il engage le cœur et les membres, et l’īmān est plus spécifique, car il engage le cœur seul »",
            "[al-Tasyīl : 2/152 — pagination imprimée douteuse, à re-vérifier sur l’édition courante]",
            "« obéissantes » : dévotes ou obéissantes. Fakhr ad-Dīn ar-Rāzī a dit : « on a dit : debout la nuit en prière — et cela est plus proche",
            "il faut donc que le lever nocturne s’unisse au jeûne du jour. »",
            "[Mafātīḥ al-Ghayb : 30/571]",
            "« adoratrices » : très assidues dans l’adoration de Dieu — Puissant et Majestueux. Al-Qāsimī a dit : « des adoratrices de Dieu, comme si l’adoration s’était mêlée à leurs cœurs jusqu’à leur devenir une seconde nature. »",
            "[Tafsīr d’al-Qāsimī : 9/275 — pagination imprimée douteuse, à re-vérifier sur l’édition courante]",
            "« jeûneuses » : le sens est jeûneuses, selon Ibn ʿAbbās",
            "on a dit : le sens est migrantes ; on a dit : parties vers Dieu, car l’origine de la siyāḥa est le départ dans la terre.",
            "le wāw y est entré pour la division ; et s’il tombait, le sens s’altérerait, car la remariée et la vierge ne s’unissent pas",
            "et les Kufans ont dit : c’est le wāw du pluriel, et cela est faible.",
            "Al-Khāzin a dit dans son exégèse : « cela relève de l’information sur la puissance, non sur l’existence",
            "Il informa donc de Sa puissance que, s’Il les répudiait, Il les remplacerait par des épouses meilleures qu’elles, pour les menacer. »",
            "[Tafsīr d’al-Khāzin : 4/316]",
            "Parmi les droits du Messager de Dieu — que Dieu prie sur lui et le salue — sur sa communauté : le bon comportement avec lui, sa défense et son respect.",
            "L’homme, quelque grande que soit sa position, doit s’abaisser et ne pas se louer lui-même",
            "Quelle est la finalité du rappel aux mères des croyants que Dieu peut remplacer le Prophète — que Dieu prie sur lui et le salue — par une meilleure ?",
            "Je clarifie la valeur du wāw dans Sa parole — le Très-Haut — : « déjà mariées ou vierges ».",
            "« La femme est mariée pour quatre choses : sa richesse, sa lignée, sa beauté et sa religion ; choisis la dévote, que tes mains soient fécondes. »",
            "[Ṣaḥīḥ de Muslim ; Livre de l’allaitement ; chapitre de la recommandation de cela]",
            "« Si quelqu’un vous demande la main d’une femme dont la religion et le caractère vous plaisent, mariez-la ; si vous ne le faites pas, il y aura discorde sur la terre et une large corruption. »",
            "[Sunan d’at-Tirmiḏī ; Livre du mariage ; chapitre de ce qui est dit : si quelqu’un vous demande la main de celui dont la religion vous plaît, mariez-le]",
            "Je rédige un exposé compositionnel mettant en évidence les qualités requises selon la Loi chez l’épouse et chez l’époux",
            "Je révise l’exégèse des versets 6 et 7 de la sourate aṭ-Ṭarīm",
            "Comment l’homme protège-t-il lui-même et sa famille du Feu ?",
        ],
        "verses": {
            "66:5": ["عَسَىٰ رَبُّهُۥٓ إِن طَلَّقَكُنَّ أَن يُبْدِلَهُۥٓ أَزْوَٰجًا خَيْرًۭا مِّنكُنَّ",
                     "مُسْلِمَٰتٍۢ مُّؤْمِنَٰتٍۢ قَٰنِتَٰتٍۢ تَٰٓئِبَٰتٍ عَٰبِدَٰتٍۢ سَٰٓئِحَٰتٍۢ ثَيِّبَٰتٍۢ وَأَبْكَارًۭا"],
            "49:14": ["قُل لَّمْ تُؤْمِنُوا۟ وَلَٰكِن قُولُوٓا۟ أَسْلَمْنَا"],
            "51:35": ["فَأَخْرَجْنَا مَن كَانَ فِيهَا مِنَ ٱلْمُؤْمِنِينَ"],
            "51:36": ["فَمَا وَجَدْنَا فِيهَا غَيْرَ بَيْتٍۢ مِّنَ ٱلْمُسْلِمِينَ"],
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
