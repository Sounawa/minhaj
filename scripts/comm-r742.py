#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R742 — commentaires des leçons 3-4 hadith-5ep : pdf-3 (الإسلام والإيمان —
le hadith de Jibrīl : l'islām et ses cinq piliers, la foi et ses six piliers)
et pdf-4 (الإحسان وأمارات الساعة — l'excellence et ses deux degrés, l'Heure et
ses signes). Deuxième vague du livre (SUIVANT de R741, leçons 3-4 précisées ;
hadith-tanawi-1 vague 22 reste au livreur concurrent, non touché). Rédaction
d'après la lecture complète FR des deux leçons (extraction non lossy
scripts/extrait-r742.py). Aucune invention (règle 2) : hadiths, versets,
citations et attributions tels que la leçon les donne — sans numéros de pages
(l'htmlFr de ce manuel n'en porte pas). NB consigné hors commentaire : la
référence imprimée « Sourate al-Baqara — verset 194 » pour « Allah aime les
bienfaisants » appelle le verset 195 — zone IA-2, journal worklog.
Garde-fous de comm-r741.py repris (typographie FR, arabe entre parenthèses
seulement, vocab ar sans harakat, guillemets appariés — imbriqués courbes)."""
import json, re, os

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_3 = {
    "auteur": "IA-1, tour R742",
    "resume": ("Guide de lecture de la leçon 3 (الإسلام والإيمان) : le deuxième hadith des "
               "Quarante — le hadith de Jibrīl, rapporté par ʿUmar ibn al-Khaṭṭāb dont la "
               "notice a été donnée en leçon 2. La leçon lit la première partie de "
               "l'interrogatoire : l'islām et la foi. Le rang du hadith d'abord : « un hadīth "
               "immense » qui renferme toutes les formes vertueuses des actes, extérieurs et "
               "intérieurs — toutes les sciences de la Loi y renvoient et en procèdent ; il "
               "est, pour la Sunna, comme la mère, de même que la Fātiḥa fut nommée « mère du "
               "Coran ». L'analyse expose ensuite l'islām — dans la langue la soumission, "
               "l'inclination et l'obéissance ; dans la Loi la religion révélée à Muḥammad (paix et bénédiction sur lui), "
               "croyance, Loi révélée et vertus morales, la ḥanīfiyya tolérante et la "
               "communauté d'Ibrāhīm — et ses cinq piliers, puis la foi — la conviction "
               "résolue des six réalités, sans doute ni hésitation, par le cœur, la langue et "
               "les membres — et ses six piliers, chacun avec son importance. Les utilités "
               "tirent du hadīth la preuve que l'islām n'est pas la foi, la question comme "
               "moyen du savoir (la parole d'Ibn ʿAbbās) et le soin des vêtements ; "
               "l'exploitation donne les branches de la foi, et la préparation ouvre "
               "l'excellence (leçon 4)."),
    "explication": [
        ("La leçon pose trois objectifs : connaître l'islām et la foi (īmān) ; distinguer les "
         "piliers de l'islām et ceux de la foi, et leur importance ; incarner les règles de "
         "l'islām et de la foi dans le ressenti et la conduite. Le tamhīd donne le cadre : le "
         "serviteur n'est un musulman véridique que lorsqu'il s'établit fermement sur les "
         "piliers de l'islām et de la foi — en science, en conviction, en acte et en "
         "conduite ; ce sont les soutènements que la Loi a établis, sans lesquels « l'édifice "
         "de la religion ne se dresse, et n'advient pas le salut en ce bas-monde et dans "
         "l'au-delà ». Cinq questions d'ouverture — qu'est-ce que l'islām ? ses piliers ? "
         "qu'est-ce que la foi ? ses piliers ? leur importance ? — et l'extraction des "
         "contenus en deux items : identifier les piliers de l'islām dans le hadīth, exposer "
         "les piliers de la foi à partir du hadīth. La préparation de la leçon précédente "
         "déjà mémorisait ce hadīth et demandait d'expliquer « il nous apparut » (ṭalaʿa "
         "ʿalaynā) et « une trace de voyage » (athar as-safar) — le glossaire de la présente "
         "leçon y répond."),
        ("Le rang du hadīth d'abord : il est appelé le hadīth de Jibrīl ; « un hadīth immense, "
         "qui renferme toutes les formes vertueuses des actes — extérieurs et intérieurs —, "
         "et toutes les sciences de la Loi y renvoient et en procèdent » ; « il est, pour la "
         "Sunna, comme la mère, de même que la Fātiḥa fut nommée “mère du Coran” (Umm "
         "al-Qurʾān) pour ce qu'elle renferme comme sens du Coran ». La leçon lit ainsi le "
         "deuxième hadith des Quarante comme la seconde « grande règle » annoncée par "
         "l'introduction (leçon 1). Le hadīth expose l'islām, la foi et l'excellence — trois "
         "degrés de la religion, mentionnés « dans l'ordre selon leur effet dans "
         "l'obéissance et l'assimilation » : l'islām est une entrée et des piliers en nombre "
         "délimité ; la foi une obéissance globale et un élargissement dans les actes ; "
         "l'excellence un perfection dans l'accomplissement et une stabilité dans la "
         "présence des cœurs. La scène du hadīth elle-même est une leçon : un homme aux "
         "habits d'un blanc éclatant, aux cheveux d'un noir profond, sans trace de voyage, "
         "que nul ne connaissait, s'assied genoux contre genoux, pose ses paumes sur les "
         "cuisses, interroge et confirme — « nous fûmes étonnés de lui : il pose la question "
         "et la confirme » ; le glossaire éclaire cet étonnement : les questions « d'un "
         "savant assuré tout en confirmant ». À la clôture, le Prophète — paix et bénédiction "
         "sur lui — révèle : « c'est Jibrīl, qui est venu à vous pour vous enseigner votre "
         "religion » — l'interrogatoire entier est un enseignement."),
        ("La première section expose l'islām et ses piliers. Dans la langue : « la soumission "
         "(istislām), l'inclination (iqbāl) et l'obéissance ». Dans la Loi : « la religion "
         "qui fut révélée à Muḥammad — paix et bénédiction sur lui » ; il est croyance, Loi "
         "révélée et vertus morales ; « c'est la religion tolérante et modérée, la religion "
         "de l'islām, désignée comme la ḥanīfiyya tolérante et la communauté (milla) "
         "d'Ibrāhīm ». Ses piliers sont cinq, dans la formule même du hadīth : les deux "
         "témoignages, l'accomplissement de la prière, l'acquittement de l'aumône, le jeûne "
         "du ramadan, « et que tu fasses le pèlerinage de la Maison si tu en as le chemin » — "
         "la restriction de capacité intégrée au pilier ; la leçon renvoie au hadīth « "
         "L'islām repose sur cinq [choses] » qui viendra. La notice du transmetteur renvoie "
         "à la leçon 2 : ʿUmar ibn al-Khaṭṭāb, déjà présenté — le hadīth de Jibrīl est le "
         "second des Quarante rapporté par lui, après celui des intentions."),
        ("La deuxième section expose la foi et ses six piliers. La foi : « la conviction "
         "résolue des six réalités exposées dans le hadīth, sans qu'aucun doute ni aucune "
         "hésitation ne s'y mêle » ; elle « s'accomplit par la conviction du cœur, l'énoncé "
         "de la langue et l'acte des membres » — le glossaire la définit : la conviction "
         "(taṣdīq), la soumission (istislām) et l'acceptation de la Loi révélée (qabūl "
         "aš-šarīʿa). Les six réalités, chacune avec sa définition et son importance. La foi "
         "en Allah : la conviction résolue qu'Il est « Lui seul le Nécessaire à l'existence "
         "(wāǧib al-wuǧūd) », décrit par les attributs de la beauté et de la perfection, "
         "exempté des attributs de l'imperfection, Unique, Un, l'Auto-suffisant, Créateur "
         "disposant de toutes les créatures selon Sa volonté — importance : « la source "
         "originaire de toutes les croyances de la foi et de ses actes, et le fondement sur "
         "lequel se bâtit la considération des actes ». La foi en les anges : les serviteurs "
         "honorés « qui ne désobéissent pas à Allah en ce qu'Il leur commande, et font ce "
         "qui leur est ordonné » (les versets cités d'al-ʿAnbiyāʾ et d'at-Taḥrīm 6), leur "
         "nombre connu de Lui seul (al-Muddaṯṯir 31) — importance : le croyant se rassure "
         "des gardiens qui le protègent à chaque instant, se remémore les consignateurs à sa "
         "droite et à sa gauche, « s'élance alors vers les bonnes actions et évite les "
         "mauvaises ». La foi en les Livres : les feuillets d'Ibrāhīm, la Torah, l'Évangile, "
         "le Zabūr et le Coran noble — « la foi du serviteur ne s'accomplit pas tant qu'il "
         "n'aura pas confirmé qu'ils sont la parole d'Allah » — importance : l'acte conforme "
         "à leur direction, qui guide vers le redressement de la religion et du bas-monde. "
         "La foi en les messagers : le rasūl est « celui à qui fut révélée une Loi et qui "
         "fut ordonné de la transmettre » ; on confirme leur véracité étayée par les "
         "miracles, et qu'on ne fait pas de distinction entre eux (al-Baqara 284) — "
         "importance : « des modèles d'application continuelle des rites de la religion, "
         "sans gêne ni contrainte, sans excès ni négligence »."),
        ("Les deux derniers piliers reçoivent le développement le plus éducatif. La foi en le "
         "Jour dernier : appelé « jour dernier » « parce qu'il n'est de jour après lui » ; on "
         "confirme son avènement et ce qu'il renferme — « réitération après la mort, "
         "rassemblement, résurrection, jugement, balance, Pont, Paradis et Enfer », demeure "
         "de récompense et de châtiment — importance : « la certitude que la rétribution de "
         "l'acte survient inévitablement : le bien par le bien, le mal par le mal ; aucun "
         "acte n'est perdu pour son auteur, aucun droit pour son détenteur ». La foi en le "
         "décret : la conviction résolue qu'Allah est « le Créateur des choses et le "
         "Décréteur des décrets », et la confirmation de ce qui est dans la science de "
         "l'inconnaissable — « dénombrement, décret et écriture dans la Table gardée » "
         "(aṣ-Ṣāffāt 96, al-Qamar 49, al-Ḥadīd 22) ; « ce qu'Allah lui a décrété de bien, il "
         "l'atteindra, et que nul ne peut l'en détourner ; et ce qu'Il lui a décrété de mal, "
         "il le rejoindra » — importance : « la sérénité de l'âme en toute situation, et "
         "l'agrément complet de tout ce qui atteint le croyant », sans mécontentement ni "
         "protestation contre Sa volonté et Sa sagesse — « celui qui confirme ces réalités "
         "est un croyant véritable, conforme à la méthode des Pieux Ancêtres (as-salaf) et "
         "des imams de la postérité (al-ḫalaf) ». Ce que l'on tire du hadīth en quatre : la "
         "vigilance envers Allah dans la prospérité comme dans l'adversité ; la preuve que "
         "l'islām n'est pas la foi — « l'islām, ce sont les actes extérieurs ; la foi, ce "
         "sont les actes intérieurs » ; l'attention à la question comme moyen d'acquérir le "
         "savoir (an-Naḥl 43 ; la parole d'Ibn ʿAbbās : « Par une langue qui questionne et "
         "un cœur qui comprend » — Fatḥ al-Bārī, Taḥrīr al-matn, al-Musnad de l'imam "
         "Aḥmad) ; et le soin de l'élégance et de la propreté des vêtements et de l'allure, "
         "« relève de la direction prophétique et des qualités du musulman ». L'évaluation "
         "en trois items retourne au fil ; l'exploitation imprime al-Anfāl 2 — la foi "
         "augmente — et le hadīth d'Abū Hurayra : « La foi comporte soixante et quelques "
         "branches ; la plus basse est d'écarter le mal du chemin, et la plus haute est la "
         "parole : il n'est de dieu qu'Allah » (Sunan d'at-Tirmiḏī), avec ses deux questions "
         "(la foi augmente et diminue ; branches multiples). La préparation ouvre la leçon 4 "
         ": mémoriser le hadīth à venir, déterminer le sens de l'excellence dans le hadīth "
         "de Jibrīl, exposer la définition de chaque pilier en bref."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (connaître islām et īmān ; distinguer les piliers "
         "et leur importance ; incarner) → tamhīd (les soutènements sans lesquels l'édifice "
         "ne se dresse) → le rang du hadīth (immense ; pour la Sunna comme la Fātiḥa pour "
         "le Coran) → trois degrés de la religion → l'islām et ses cinq piliers → la foi et "
         "ses six piliers, chacun avec son importance → fawāʾid en quatre → évaluation en "
         "trois items → istithmār (al-Anfāl 2 ; les branches de la foi, at-Tirmiḏī) → iʿdād "
         "de la leçon 4."),
        ("Le rang : « toutes les sciences de la Loi y renvoient et en procèdent » ; pour la "
         "Sunna « comme la mère », de même que la Fātiḥa est « mère du Coran » — la seconde "
         "grande règle du recueil, dans l'esprit de l'introduction citée en leçon 1."),
        ("Les trois degrés : l'islām — une entrée et des piliers en nombre délimité ; la foi "
         "— une obéissance globale et un élargissement dans les actes ; l'excellence — un "
         "perfection dans l'accomplissement et une stabilité dans la présence des cœurs ; "
         "mentionnés « dans l'ordre selon leur effet dans l'obéissance et l'assimilation »."),
        ("L'islām : dans la langue la soumission, l'inclination, l'obéissance ; dans la Loi "
         "la religion révélée à Muḥammad (paix et bénédiction sur lui) — croyance, Loi "
         "révélée et vertus morales, la "
         "ḥanīfiyya tolérante et la milla d'Ibrāhīm ; cinq piliers dans la formule du "
         "hadīth, la capacité intégrée au pèlerinage (« si tu en as le chemin »)."),
        ("La foi : conviction résolue sans doute ni hésitation, par la conviction du cœur, "
         "l'énoncé de la langue et l'acte des membres (taṣdīq, istislām, qabūl aš-šarīʿa) ; "
         "six réalités — Allah (wāǧib al-wuǧūd, source originaire des croyances), les anges "
         "(gardiens et consignateurs), les Livres (feuillets d'Ibrāhīm, Torah, Évangile, "
         "Zabūr, Coran — la parole d'Allah), les messagers (miracles, pas de distinction — "
         "al-Baqara 284), le Jour dernier (rétribution certaine), le décret (sérénité et "
         "agrément — méthode des as-salaf et des imams al-ḫalaf)."),
        ("Le décret : « dénombrement, décret et écriture dans la Table gardée » (aṣ-Ṣāffāt "
         "96, al-Qamar 49, al-Ḥadīd 22) ; ce qui est décrété de bien il l'atteindra et nul "
         "ne peut l'en détourner, de mal il le rejoindra et nul ne peut l'en repousser — "
         "l'importance : la sérénité de l'âme, sans mécontentement ni protestation."),
        ("Deux utilités pédagogiques tirées du hadīth : la question, moyen d'acquérir le "
         "savoir — an-Naḥl 43 et la parole d'Ibn ʿAbbās « Par une langue qui questionne et "
         "un cœur qui comprend » —, et le soin de l'élégance et de la propreté des "
         "vêtements et de l'allure, qui relève de la direction prophétique ; la scène "
         "elle-même (l'interrogateur qui pose et confirme) est une leçon de méthode."),
        ("L'exploitation des branches de la foi : al-Anfāl 2 (« dont la foi augmente ») et "
         "Abū Hurayra « La foi comporte soixante et quelques branches ; la plus basse est "
         "d'écarter le mal du chemin, et la plus haute est la parole : il n'est de dieu "
         "qu'Allah » (Sunan d'at-Tirmiḏī) — la foi augmente et diminue ; la préparation "
         "annonce l'excellence (leçon 4, posée dans la même vague)."),
    ],
    "vocabulaire": [
        {"ar": "حديث جبريل", "translit": "ḥadīṯ Ǧibrīl",
         "fr": "le hadith de Jibrīl — le deuxième hadith des Quarante : l'interrogatoire venu « vous enseigner votre religion » ; pour la Sunna comme la Fātiḥa pour le Coran"},
        {"ar": "طله علينا", "translit": "ṭalaʿa ʿalaynā",
         "fr": "il nous apparut — « il nous fut manifesté », dit du questionneur inconnu aux habits d'un blanc éclatant"},
        {"ar": "اثر السفر", "translit": "athar as-safar",
         "fr": "une trace de voyage — « le signe du voyage et son apparence », dont l'interrogateur ne portait aucune"},
        {"ar": "الايمان", "translit": "al-īmān",
         "fr": "la foi — la conviction (taṣdīq), la soumission (istislām) et l'acceptation de la Loi révélée (qabūl aš-šarīʿa) ; conviction du cœur, énoncé de la langue, acte des membres"},
        {"ar": "الاسلام", "translit": "al-islām",
         "fr": "dans la langue : la soumission, l'inclination et l'obéissance ; dans la Loi : la religion révélée à Muḥammad (paix et bénédiction sur lui) — croyance, Loi révélée et vertus morales"},
        {"ar": "الواجب الوجود", "translit": "wāǧib al-wuǧūd",
         "fr": "le Nécessaire à l'existence — Allah seul, décrit par les attributs de la beauté et de la perfection, exempté des attributs de l'imperfection"},
        {"ar": "ايمان بالقدر", "translit": "al-īmān bi-l-qadar",
         "fr": "la foi au décret — la conviction résolue du Créateur et Décréteur, l'écriture dans la Table gardée ; sérénité de l'âme en toute situation"},
        {"ar": "السؤال", "translit": "as-suʾāl",
         "fr": "la question — « l'un des moyens d'acquérir le savoir » (an-Naḥl 43) ; Ibn ʿAbbās : « Par une langue qui questionne et un cœur qui comprend »"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

E_4 = {
    "auteur": "IA-1, tour R742",
    "resume": ("Guide de lecture de la leçon 4 (الإحسان وأمارات الساعة) : la suite du hadīth "
               "de Jibrīl — l'excellence (iḥsān) et les signes de l'Heure. La leçon répond à "
               "la préparation de la leçon 3 : le sens de l'excellence dans le hadīth de "
               "Jibrīl. L'excellence est le troisième degré de la religion ; dans la langue, "
               "la perfection (itqān) d'une chose et son accomplissement dans l'excellence "
               "(taǧawwud) ; dans le hadīth, la perfection des adorations et la surveillance "
               "— se remémorer Son regard, Son savoir et Sa majesté — et elle embrasse toute "
               "parole, action, intention et dessein, adoration ou transaction, envers le "
               "Maître ou les créatures. Ses deux degrés tirés de la formule du hadīth : la "
               "vision intérieure (mušāhada) — « que tu adores Allah comme si tu Le voyais » "
               "— et la surveillance (murāqaba) — « si tu ne Le vois pas, Lui, Il te voit » "
               "—, complétés par les trois stations du qāḍī (Ikmāl ikmām al-muʾallim). "
               "L'Heure : la Résurrection, dont nul ne connaît le temps hormis Allah — l'une "
               "des cinq choses de l'invisible (Luqmān 33) ; ses deux signes dans le hadīth "
               "(la servante qui enfante sa maîtresse ; la rivalité d'édifices des bergers) "
               "et leur sens — la corruption des mœurs et l'accumulation vantarde des "
               "richesses, l'acquisition licite restant celle de l'intention droite."),
    "explication": [
        ("La leçon pose trois objectifs : identifier le sens de l'excellence (iḥsān) et ses "
         "degrés ; distinguer les signes de l'Heure ; incarner le caractère de l'excellence "
         "dans sa vie. Le tamhīd élargit : les versets du Coran noble et les hadiths du "
         "Prophète — paix et bénédiction sur lui — « invitent à l'excellence en toute "
         "chose : ce en quoi l'excellence entre s'en trouve embelli, et ce dont elle manque "
         "s'en trouve avili » — c'est la préoccupation du croyant « en guise de préparation "
         "au Jour de la Résurrection, dont les signes ont commencé à paraître "
         "successivement ». Trois questions — le sens de l'excellence, ses degrés, les "
         "signes de l'Heure — et l'extraction des contenus en deux items. Le hadīth est "
         "imprimé en entier une seconde fois : la leçon lit maintenant sa seconde partie "
         "(l'excellence, l'Heure, ses signes), après l'islām et la foi (leçon 3)."),
        ("L'excellence d'abord. Elle est « le troisième degré des degrés de la religion » ; "
         "dans la langue, elle désigne « la perfection (itqān) d'une chose et son "
         "accomplissement dans l'excellence (taǧawwud) » ; dans le hadīth, « la perfection "
         "des adorations, l'égard des droits d'Allah — le Très-Haut —, et la surveillance "
         "consistant à se remémorer Son regard, Son savoir et Sa majesté durant les "
         "adorations ». Son étendue est totale : « elle embrasse toute parole ou action, "
         "toute intention et tout dessein, adoration ou transaction, entre le serviteur et "
         "son Maître, ou entre le serviteur et les autres créatures » — la même étendue que "
         "l'intention de la leçon 2, mais prise au degré supérieur : non plus la validité "
         "de l'acte, mais sa perfection. Les deux degrés sortent de la formule même du "
         "hadīth : « que tu adores Allah comme si tu Le voyais » — le degré de la vision "
         "intérieure (mušāhada) ; « car si tu ne Le vois pas, Lui, Il te voit » — le degré "
         "de la surveillance (murāqaba). Le résultat : la dévotion sincère du croyant à Sa "
         "douceur, « en parole et en acte », et la remémoration qu'Allah le voit et le "
         "surveille « en secret comme en public », qu'Il « pénètre chacun de ses mouvements "
         "et de ses immobilités »."),
        ("Le manuel ajoute la parole du qāḍī (source donnée : Ikmāl ikmām al-muʾallim) : « le "
         "serviteur, dans son adoration, traverse trois stations » — premièrement "
         "l'accomplir « de la manière qui acquitte l'obligation, c'est-à-dire en remplissant "
         "toutes les conditions et tous les piliers » ; deuxièmement « l'accomplir de même, "
         "tout en étant absorbé dans l'océan du dévoilement, comme s'il voyait Allah — le "
         "Très-Haut » ; troisièmement « l'accomplir de même, tout en étant dominé par la "
         "conscience qu'Allah — le Très-Haut — l'observe : telle est la station de la "
         "surveillance ». Les trois stations redonnent les trois degrés du recueil lui-même "
         ": l'obligation acquittée (l'islām), la vision intérieure (l'excellence), la "
         "surveillance (l'excellence dans son second degré) — le hadīth de Jibrīl se lit "
         "alors comme l'escalier entier de la religion, du pilier à la perfection."),
        ("L'Heure ensuite. Elle est « la Résurrection : elle est la fin de la demeure "
         "d'ici-bas et le début de la demeure de l'au-delà » ; « nul n'en connaît le temps, "
         "hormis Allah, le Puissant et le Majestueux » ; elle est du nombre « des cinq "
         "choses de l'invisible que nul ne connaît, hormis Allah » — le verset de Luqmān 33 "
         "est imprimé en entier : « Certes, Allah détient la connaissance de l'Heure ; Il "
         "envoie la pluie et sait ce que portent les entrailles ; et nulle âme ne sait ce "
         "qu'elle acquerra demain, et nulle âme ne sait en quelle terre elle mourra ». Le "
         "hadīth en renferme deux signes. Le premier — « que la servante enfante sa "
         "maîtresse » — « signifie la corruption des mœurs, qui mène à des situations "
         "inhabituelles, parmi lesquelles la fréquence de l'ingratitude filiale des "
         "enfants ». Le second — « que tu voies les déchaussés, les nus, les démunis, "
         "bergers de menu bétail, rivaliser d'édifices » — « signifie l'accumulation des "
         "richesses et des gains vils pour bâtir et s'en vanter devant les gens », chose "
         "« blâmable en loi religieuse » ; et la leçon d'ajouter la règle qui protège de "
         "toute généralisation : « l'expansion de l'acquisition avec une intention droite "
         "et un dessein noble, elle relève de ce que la Loi a rendu licite » — le critère "
         "est encore l'intention, fil de la leçon 2. Le glossaire donne le lexique complet "
         "du second signe : al-ḥufāt (les déchaussés, pluriel de ḥāfiʿ, sans sandales), "
         "al-ʿurāt (les nus, pluriel de ʿārī), al-ʿāla (les démunis, pluriel de ʿāʾil, le "
         "pauvre qui a besoin de celui dont il subsiste), raʿāt (les bergers, pluriel de "
         "rāʿī, gardien d'une chose), aš-šāʾ (le menu bétail, pluriel de šāʾ, la femelle "
         "des ovins)."),
        ("Ce que l'on tire du hadīth en deux : l'orientation vers la perfection des "
         "adorations, l'égard des droits d'Allah, la remémoration de Sa majesté durant les "
         "adorations « et de Sa surveillance en toutes situations » ; et que l'avènement de "
         "l'Heure est du nombre des réalités de l'invisible « dont Allah s'est réservé la "
         "connaissance et qu'Il n'a dévoilées à nul de Sa création », toutefois « Il y a "
         "placé des marques qui attestent sa proximité ». L'évaluation en trois items "
         "retourne au fil : définir l'excellence et exposer ses degrés ; déterminer les "
         "marques de l'Heure mentionnées dans le hadīth ; en extraire des utilités. "
         "L'exploitation imprime les vertus de l'excellence dans le Coran : couplée à la "
         "compagnie d'Allah — « Certes, Allah est avec ceux qui Le craignent, et avec ceux "
         "qui font le bien » (an-Naḥl 128) ; avec l'amour d'Allah — « et les bienfaisants : "
         "Allah aime les bienfaisants » (la référence imprimée porte al-Baqara 194 ; le "
         "verset qui porte cet amour est le 195) ; avec l'augmentation — « Ceux qui font le bien ont la plus "
         "belle récompense et un surcroît » (Yūnus 26) ; la question demande d'en extraire "
         "les vertus. La préparation ouvre la leçon 5 : mémoriser le hadīth suivant et "
         "méditer « les piliers de l'islām et l'importance de chacun d'eux » — le hadīth « "
         "L'islām repose sur cinq [choses] » annoncé dès la leçon 3."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (le sens de l'excellence et ses degrés ; les "
         "signes de l'Heure ; incarner l'excellence) → tamhīd (l'embellissement de toute "
         "chose ; la préparation au Jour dont les signes paraissent) → l'iḥsān en langue et "
         "en Loi → ses deux degrés (mušāhada, murāqaba) → les trois stations du qāḍī → "
         "l'Heure et l'invisible de son temps (Luqmān 33) → ses deux signes et leur sens → "
         "fawāʾid en deux → évaluation en trois items → istithmār (compagnie, amour, "
         "surcroît) → iʿdād de la leçon 5."),
        ("L'excellence en langue et en Loi : la perfection (itqān) et l'accomplissement dans "
         "l'excellence (taǧawwud) ; dans le hadīth, la perfection des adorations, l'égard "
         "des droits d'Allah, la surveillance — Son regard, Son savoir, Sa majesté — ; "
         "étendue totale : paroles, actions, intentions, desseins, adoration ou "
         "transaction, envers le Maître ou les créatures."),
        ("Les deux degrés de la formule : « que tu adores Allah comme si tu Le voyais » — la "
         "vision intérieure (mušāhada) ; « si tu ne Le vois pas, Lui, Il te voit » — la "
         "surveillance (murāqaba) ; le résultat : la dévotion sincère à Sa douceur et la "
         "remémoration de Sa vue et de Sa surveillance, en secret comme en public."),
        ("Les trois stations du qāḍī (Ikmāl ikmām al-muʾallim) : l'obligation acquittée (toutes "
         "conditions et piliers remplis) ; l'absorption dans « l'océan du dévoilement, "
         "comme s'il voyait Allah » ; la conscience dominante qu'Allah l'observe — la "
         "station de la surveillance ; elles redonnent les degrés du recueil."),
        ("L'Heure : la Résurrection, fin de l'ici-bas et début de l'au-delà ; du nombre « des "
         "cinq choses de l'invisible » — Luqmān 33 imprimé en entier ; nul n'en connaît le "
         "temps hormis Allah ; des marques attestent sa proximité."),
        ("Les deux signes du hadīth : la servante qui enfante sa maîtresse — la corruption "
         "des mœurs et l'ingratitude filiale fréquente ; les déchaussés, les nus, les "
         "démunis, bergers de menu bétail rivalisant d'édifices — l'accumulation des "
         "richesses et des gains vils pour se vanter, « blâmable en loi religieuse » ; la "
         "règle de l'acquisition : licite avec « une intention droite et un dessein noble » "
         "— le critère de l'intention (leçon 2) au tribunal des richesses."),
        ("Le lexique du second signe (glossaire complet) : al-ḥufāt (déchaussés, ḥāfiʿ), "
         "al-ʿurāt (nus, ʿārī), al-ʿāla (démunis, ʿāʾil), raʿāt (bergers, rāʿī), aš-šāʾ "
         "(menu bétail, femelle des ovins)."),
        ("Les vertus de l'excellence dans le Coran (istithmār) : la compagnie d'Allah "
         "(an-Naḥl 128), Son amour (« Allah aime les bienfaisants » — la référence imprimée "
         "porte al-Baqara 194, le verset qui porte cet amour est le 195), le surcroît (Yūnus 26) ; la "
         "préparation annonce le hadīth « L'islām repose sur cinq » (leçon 5) déjà annoncé "
         "en leçon 3."),
    ],
    "vocabulaire": [
        {"ar": "الاحسان", "translit": "al-iḥsān",
         "fr": "l'excellence — le troisième degré de la religion ; en langue la perfection (itqān) et l'accomplissement dans l'excellence (taǧawwud) ; ici la perfection des adorations et la surveillance"},
        {"ar": "مشاهدة", "translit": "mušāhada",
         "fr": "la vision intérieure — premier degré de l'excellence : « que tu adores Allah comme si tu Le voyais »"},
        {"ar": "مراقبة", "translit": "murāqaba",
         "fr": "la surveillance — second degré : « si tu ne Le vois pas, Lui, Il te voit » ; se remémorer Son regard, Son savoir et Sa majesté"},
        {"ar": "الساعة", "translit": "as-sāʿa",
         "fr": "l'Heure — « la portion de temps » ; ici le Jour dernier : la fin de la demeure d'ici-bas et le début de l'au-delà"},
        {"ar": "اماراتها", "translit": "ʾamārātuhā",
         "fr": "ses marques — les signes qui attestent la proximité de l'Heure ; le hadīth en renferme deux"},
        {"ar": "الحفات", "translit": "al-ḥufāt",
         "fr": "les déchaussés — pluriel de ḥāfiʿ, « celui qui n'a point de sandales aux pieds », premier rang des édificateurs du second signe"},
        {"ar": "العالة", "translit": "al-ʿāla",
         "fr": "les démunis — pluriel de ʿāʾil, « le pauvre démuni, qui a besoin de celui dont il subsiste »"},
        {"ar": "الشاء", "translit": "aš-šāʾ",
         "fr": "le menu bétail — pluriel de šāʾ, « la femelle des ovins » ; leurs bergers, riches d'édifices, donnent le second signe"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

ENTREES = [('pdf-3', E_3), ('pdf-4', E_4)]

def norme_fr(s):
    s = s.replace('\'', '’')
    s = re.sub(r'\s+([;:!?»])', '\u202f\\1', s)
    s = s.replace('« ', '«\u202f')
    return s

def norme_entree(e):
    e['resume'] = norme_fr(e['resume'])
    e['avertissement'] = norme_fr(e['avertissement'])
    e['explication'] = [norme_fr(x) for x in e['explication']]
    e['points'] = [norme_fr(x) for x in e['points']]
    for v in e.get('vocabulaire', []):
        v['fr'] = norme_fr(v['fr'])
    return e

data = json.load(open(CHEMIN, encoding='utf-8'))
com = data['commentaires']
bloque = [d for d, _ in ENTREES if d in com]
if bloque:
    print(f'!! déjà présent : {bloque} — rien de fait')
    raise SystemExit(1)
for docid, e in ENTREES:
    com[docid] = norme_entree(e)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Garde-fous : volume + ponctuation FR + arabes hors parenthèses + guillemets appariés
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']), sorted(data2['commentaires'].keys()))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
for DOCID in ('pdf-3', 'pdf-4'):
    e = data2['commentaires'][DOCID]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    print(f'{DOCID} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
    textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] \
             + [v['fr'] for v in e['vocabulaire']] + [v['translit'] for v in e['vocabulaire']]
    for t in textes:
        hors_parenth = re.sub(r'\([^)]*[\u0600-\u06FF][^)]*\)', '()', t)
        if "'" in t or re.search(r' [;:!?»]', t) or re.search(r'« ', t):
            mauvais += 1
            print('   ponctuation à revoir dans :', t[:60])
        if motif_ar.search(hors_parenth):
            mauvais += 1
            print('   caractère arabe hors parenthèses :', t[:60])
        if t.count('«') != t.count('»'):
            mauvais += 1
            print('   guillemets non appariés :', t[:60])
    for v in e['vocabulaire']:
        if not motif_ar.search(v['ar'].replace(' ', '')):
            mauvais += 1
            print('   vocab ar non arabe :', v['ar'])
        if re.search(r'[\u064B-\u0652\u0670]', v['ar']):
            mauvais += 1
            print('   vocab ar avec harakat :', v['ar'])
        if motif_ar.search(v['fr']):
            mauvais += 1
            print('   vocab fr contient de l arabe :', v['fr'][:60])
print('contrôle ponctuation/arabe FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')
