#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R749 — commentaires des leçons 9-10 hadith-5ep : pdf-9 (الإحداث والابتداع
في الدين — les innovations dans la religion : le cinquième hadīth des Quarante,
ʿĀʾiša — les deux versions, al-Iʿtiṣām, ce qui n'entre pas dans la bidʿa,
iḫlāṣ + mutābaʿa) et pdf-10 (الحلال والحرام والمشتبهات — le sixième hadīth,
an-Nuʿmān ibn Bašīr : les trois catégories d'affaires, la divergence sur les
muštabahāt, les deux types de gens, la troisième catégorie d'Ibn Raǧab).
Cinquième vague du livre (SUIVANT de R748, leçons 9-10 ; hadith-5ep 8/29 au
départ). Rédaction d'après la lecture complète FR des deux leçons (extraction
non lossy scripts/extrait-r749.py). Aucune invention (règle 2) : hadiths,
versets, citations et attributions tels que la leçon les donne.
NB de lecture consigné (zone IA-2, journal worklog) : les références imprimées
du tirage portent al-Anʿām 154, al-Bayyina 5 et an-Naml 19 (pdf-9), al-Māʾida 6
et al-Baqara 186 (pdf-10) — les versets qui portent ces paroles sont le 153
(al-Anʿām), al-Ḥašr 7, at-Tawba 105, al-Aʿrāf 157 et le 187 (al-Baqara),
vérifiés web ; le commentaire le dit en langage lecteur, comme en R742/R747.
Corrects dans le tirage : an-Nisāʾ 23, an-Nisāʾ 24, al-Māʾida 96.
NB consigné transcription (zone IA-2) : la notice de Nuʿmān ibn Bašīr du tirage
traduit « naquit en l'an 90 de l'Hégire » — contradictoire avec « le premier
enfant né dans l'islam parmi les Anṣār après l'Hégire » (biographies : né peu
après l'Hégire) ; le commentaire ne répète pas le chiffre.
Garde-fous de comm-r747.py repris (typographie FR, arabe entre parenthèses
seulement, vocab ar sans harakat, guillemets appariés) + fenêtre de mots
1700-2400 (resume+explication+points) par entrée."""
import json, re, os, sys

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_9 = {
    "auteur": "IA-1, tour R749",
    "resume": ("Guide de lecture de la leçon 9 (les innovations dans la religion — "
               "al-iḥdāṯ wa-l-ibtidāʾ fī d-dīn (الإحداث والابتداع في الدين)) : le cinquième "
               "hadīth des Quarante de l'imam al-Nawawī, rapporté par la mère des croyants "
               "ʿĀʾiša — « Quiconque introduit dans notre affaire présente ce qui n'en fait "
               "pas partie, cela en sera rejeté » —, rendu avec la seconde version de Muslim "
               "(« Quiconque accomplit une œuvre qui ne relève pas de notre ordre, cela en "
               "sera rejeté »). Le tamhīd pose la double exigence : obéir dans tout ce que la "
               "Loi a apporté, ne rien y introduire sans preuve probante. L'analyse répond en "
               "trois stations : la définition de l'innovation et son jugement (d'après "
               "al-Iʿtiṣām — rejetée à son auteur, fondement de la nullité des contrats "
               "prohibés), ce qui n'entre pas dans l'innovation (l'intérêt qui ne sort pas de "
               "la Sunna ni des finalités — muṣḥafs, iǧtihād, livres des sciences), et les "
               "deux conditions de l'œuvre acceptée (iḫlāṣ et mutābaʿa, d'après le Ǧāmiʿ "
               "al-ʿUlūm wa-l-Ḥikam, avec al-Anʿām). L'exploitation réunit deux versets de "
               "l'agir — prendre le donné du Messager, agir sous le regard d'Allah, de Son "
               "Messager et des croyants — et la préparation ouvre la leçon 10 : Nuʿmān ibn "
               "Bašīr et les choses ambiguës (muštabahāt)."),
    "explication": [
        ("La leçon 9 tourne une page dans le livre des Quarante : les quatre premiers "
         "hadīths avaient posé les fondements — l'intention et le jugement sur les actes, le "
         "iḥsān, les piliers de l'islām, le décret et ce qui est inscrit —, le cinquième "
         "installe le garde-fou qui les protège tous : aucun chemin vers Allah que la Loi "
         "n'a pas tracé. Elle répond à la préparation de la leçon 8 : « Je recherche la "
         "biographie de la mère des croyants ʿĀʾiša — qu'Allah l'agrée », « Je détermine le "
         "sens de “ar-rad” (le rejet) dans le hadīth ». Trois objectifs : « Que je me "
         "familiarise avec l'innovation (bidʿa) dans la Loi, et avec le jugement de son "
         "établissement » ; « Que je distingue ce qui entre dans l'innovation de ce qui n'y "
         "entre pas » ; « Que je m'en tienne à la Sunna dans mes actes d'adoration et mes "
         "transactions » — connaître, distinguer, s'en tenir."),
        ("Le tamhīd part de la foi comme obéissance : « Parmi les exigences de la foi en "
         "Allah et en Son Messager — prière et salut d'Allah sur lui —, il y a l'obéissance "
         "à l'un et à l'autre dans tout ce que la Loi a apporté comme règles, qu'il s'agisse "
         "des actes d'adoration, des transactions ou de la conduite », et son versant "
         "négatif : « le fait de ne rien introduire dans l'affaire de cette religion parmi "
         "ce que la Loi n'a pas apporté et qui ne repose sur aucune preuve probante ». Deux "
         "questions ouvrent le chemin : « Quel est donc le jugement de l'innovation dans la "
         "religion ? Et quelles sont les conditions d'acceptation de l'œuvre et de sa prise "
         "en compte par la Loi ? » — le jugement du nouveau et les conditions du reçu : "
         "l'analyse répondra station par station."),
        ("Le texte rend le hadīth avec ses deux versions [Ṣaḥīḥ de al-Buḫārī et Muslim] : "
         "« Quiconque introduit dans notre affaire présente ce qui n'en fait pas partie, "
         "cela en sera rejeté » ; « et dans une version de Muslim : Quiconque accomplit une "
         "œuvre qui ne relève pas de notre ordre, cela en sera rejeté ». La notice de la "
         "transmettrice répond à la préparation : « la mère des croyants, épouse du Prophète "
         "— prière et salut d'Allah sur lui —, la Véridique, fille du Véridique "
         "(aṣ-ṣiddīqa bint aṣ-ṣiddīq) », qui « a transmis à la communauté une science "
         "abondante et une jurisprudence (fiqh) considérable », fut « la plus versée des "
         "femmes des musulmans en religion et en lettres » — « les plus éminents Compagnons "
         "l'interrogeaient sur les parts successorales (farāʾiḍ), et elle leur répondait » — "
         "et « est décédée en l'an 57 ou en l'an 58 de l'Hégire ». Le glossaire fixe trois "
         "gloses : « il a introduit (aḥdataṯa) » — « il a créé et forgé (anšaʾa wa-ḫtaraʿa) "
         "» ; « notre affaire (ʾamranā) » — « notre Loi et notre religion (šarʿunā "
         "wa-dīnunā) » ; « rejeté (radd) » — « repoussé (mardūd) ». L'extraction pose deux "
         "travaux : le jugement énoncé « au sujet de l'œuvre contraire à la Sunna », et "
         "l'exposé « des conditions d'acceptation de l'œuvre et de la prise en compte de "
         "celle-ci »."),
        ("La première section définit et juge. Dans le langage, l'ibtidāʾ est « le fait "
         "d'introduire une chose sans précédent semblable » ; dans la Loi, la bidʿa est "
         "« une voie inventée dans la religion, qui ressemble à la Loi, et par laquelle on "
         "entend se rapprocher d'Allah » — la leçon renvoie à al-Iʿtiṣām, l'ouvrage "
         "d'ash-Shāṭibī consacré aux avantages de la Sunna. Trois notes dans la définition : "
         "une voie, inventée ; une ressemblance à la Loi, qui trompe ; une intention de "
         "rapprochement, qui donne à l'ajout l'apparence de la piété. Le jugement suit : "
         "« elle est rejetée à son auteur : rien n'en est accepté en droit, et elle ne "
         "comporte aucune récompense » — ni validité ni récompense."),
        ("La seconde version étend la portée : elle « est formelle (ṣarīḥa) quant au rejet "
         "de toute œuvre non conforme à la Loi, que son auteur l'ait instituée de lui-même "
         "ou qu'un précédent y ait pourvu. Quiconque accomplit une œuvre que Allah et Son "
         "Messager n'ont pas prescrite, ou bien introduit dans la religion ce dont ne "
         "témoigne ni un fondement authentique (aṣl ṣaḥīḥ) ni une règle générale (qāʿida "
         "ʿāmma) : cela lui est rejeté, et il est pécheur. » Et la leçon donne au hadīth une "
         "portée juridique générale : « ce hadīth constitue un fondement (aṣl) établissant "
         "la nullité de tous les contrats (ʿuqūd) prohibés, et l'absence d'obligation des "
         "fruits (ṯamarāt) qui en découlent » — du culte au contrat, la même règle du "
         "fondement."),
        ("La deuxième section protège contre l'excès inverse — qualifier d'innovation tout "
         "ce qui est nouveau : « N'entre pas dans l'innovation l'intérêt (maṣlaḥa) qui ne "
         "sort pas de la Sunna ni des finalités générales (maqāṣid) de la Loi, et que ce "
         "rejet ne contredit pas ». Trois exemples : « telle la transcription du Coran dans "
         "les muṣḥafs » ; « tel l'effort d'interprétation (iǧtihād) ramenant les branches "
         "du fiqh à leurs principes, déduits de la parole d'Allah et de celle de Son "
         "Messager » ; « tels encore les livres composés en grammaire, en calcul, en parts "
         "successorales et autres sciences, dont la source et le fondement sont le Livre "
         "d'Allah le Très-Haut et la Sunna de Son Messager — prière et salut d'Allah sur "
         "lui » — « tout cela, en effet, n'entre pas dans ce hadīth ». La clef du tri n'est "
         "pas la nouveauté de la forme mais le rattachement : l'intérêt qui reste dans la "
         "Sunna et les maqāṣid est de l'obéissance, non de l'innovation."),
        ("La troisième section répond à la seconde question du tamhīd : « Toute œuvre par "
         "laquelle on se rapproche d'Allah le Très-Haut ne profite pas à son auteur tant "
         "que deux conditions ne s'y réunissent pas : la sincérité exclusive (iḫlāṣ), et la "
         "conformité au modèle du Messager d'Allah — prière et salut d'Allah sur lui — "
         "(mutābaʿa). La seconde condition est précisément l'exigence du hadīth de ʿĀʾiša — "
         "qu'Allah l'agrée » [Ǧāmiʿ al-ʿUlūm wa-l-Ḥikam, avec adaptations]. Le cas limite "
         "est tranché : « Si donc l'œuvre est sincère pour Allah le Très-Haut, mais qu'elle "
         "repose sur un ordre récemment introduit dans la religion, sans fondement ni "
         "preuve, elle est rejetée à son auteur » — la sincérité seule ne sauve pas une "
         "œuvre sans mutābaʿa. La preuve coranique : « Voici Mon chemin, qui est droit : "
         "suivez-le donc ; et ne suivez pas les autres chemins, car ils vous écarteraient "
         "de Son chemin. Voilà ce qu'Il vous enjoint, puissiez-vous être pieux ! » (Sourate "
         "al-Anʿām — la référence imprimée porte le verset 154 ; le verset qui porte ces "
         "paroles est le 153) — un chemin, pas des chemins."),
        ("Ce qu'il faut retirer du hadīth, en quatre : « L'incitation à la conformité au "
         "modèle (ittibāʿ) et la mise en garde contre l'innovation (ibtidāʿ) » ; « la "
         "valeur des œuvres se mesure à leur conformité à la Loi ; toute œuvre qui la "
         "contredit est rejetée » ; « Se tenir aux limites des enseignements du Livre et de "
         "la Sunna, selon leur compréhension saine » ; « Le besoin de s'orienter d'après "
         "l'exposé des savants et les règles de la Loi pour comprendre l'innovation » — la "
         "dernière protège l'élève de la précipitation : le mot innovation est un jugement "
         "de la Loi, appris par les règles, pas une impression du jour."),
        ("L'exploitation réunit deux versets de l'agir : « Prenez ce que le Messager vous "
         "a donné, et ce qu'il vous a interdit, abstenez-vous-en » (Sourate al-Bayyina — la "
         "référence imprimée porte le verset 5 ; le verset qui porte ces paroles est "
         "al-Ḥašr 7) ; « Et agissez : Allah observera votre œuvre, de même que Son "
         "Messager et les croyants » (Sourate an-Naml — la référence imprimée porte le "
         "verset 19 ; le verset qui porte ces paroles est at-Tawba 105). L'exercice demande "
         "de « Je dégage des deux āyāt les conditions de l'acceptation de l'œuvre auprès "
         "d'Allah le Très-Haut » : le premier verset donne la mutābaʿa — prendre ce que le "
         "Messager a donné, s'abstenir de ce qu'il a interdit ; le second donne l'iḫlāṣ et "
         "l'observance — un agir vu par Allah, par Son Messager et par les croyants. Le "
         "lexique (al-muʿǧam) propose quatre mots à expliquer — « prenez-le (fa-ḫuḏūhu) », "
         "qui se lit en toutes lettres dans l'arabe du premier verset —, puis « forgée "
         "(muḫtalaʿa) », « droite (ṣāliḥan) », « qu'Il l'agrée (tarḍīhi) »."),
        ("L'évaluation retourne au texte : « Qu'entend-on par le mot “notre affaire” dans "
         "le hadīth ? », « Expose les conditions de l'œuvre acceptée auprès d'Allah le "
         "Très-Haut », « Quel est l'apport de la seconde version du hadīth ? » — la glose, "
         "les conditions, la portée. La préparation ouvre la leçon suivante : « Je recherche "
         "la biographie du noble Compagnon Nuʿmān ibn Bašīr — qu'Allah l'agrée » ; « "
         "J'expose le jugement des choses ambiguës (muštabahāt) et la méthode pour les "
         "traiter » — du garde-fou au discernement : après le rejet de l'ajout, la carte du "
         "licite, de l'illicite et de l'ambigu, que la leçon 10 lira avec le sixième hadīth "
         "des Quarante."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (familiariser avec l'innovation dans la Loi et "
         "le jugement de son établissement ; distinguer ce qui y entre de ce qui n'y entre "
         "pas ; s'en tenir à la Sunna dans adorations et transactions) → tamhīd (l'obéissance "
         "dans tout ce que la Loi a apporté ; ne rien y introduire sans preuve probante ; "
         "deux questions) → le hadīth à deux versions → analyse en trois stations → quatre "
         "utilités → exploitation (deux āyāt, lexique) → préparation (Nuʿmān ibn Bašīr, "
         "muštabahāt)."),
        ("La continuité du fil : la préparation de la leçon 8 demandait « la biographie de "
         "la mère des croyants ʿĀʾiša » et le sens de « ar-rad » — la leçon 9 les tient : "
         "la notice (aṣ-ṣiddīqa bint aṣ-ṣiddīq, les farāʾiḍ des Compagnons, morte en 57 ou "
         "58) et le glossaire (« rejeté (radd) » — « repoussé (mardūd) »)."),
        ("Les deux versions et leur division du travail : la première vise l'ajout dans "
         "« notre affaire » — « notre Loi et notre religion » ; la seconde est « formelle "
         "(ṣarīḥa) quant au rejet de toute œuvre non conforme à la Loi, que son auteur "
         "l'ait instituée de lui-même ou qu'un précédent y ait pourvu » — et le hadīth "
         "« constitue un fondement (aṣl) établissant la nullité de tous les contrats "
         "(ʿuqūd) prohibés »."),
        ("La définition d'al-Iʿtiṣām (l'ouvrage d'ash-Shāṭibī) : « une voie inventée dans "
         "la religion, qui ressemble à la Loi, et par laquelle on entend se rapprocher "
         "d'Allah » — la voie, la ressemblance, l'intention de rapprochement ; le jugement : "
         "« rien n'en est accepté en droit, et elle ne comporte aucune récompense »."),
        ("La garde de la deuxième section : l'intérêt « qui ne sort pas de la Sunna ni des "
         "finalités générales (maqāṣid) de la Loi » — les muṣḥafs, l'iǧtihād ramenant « les "
         "branches du fiqh à leurs principes », les livres des sciences « dont la source et "
         "le fondement sont le Livre d'Allah le Très-Haut et la Sunna » : « tout cela, en "
         "effet, n'entre pas dans ce hadīth »."),
        ("Les deux conditions de l'œuvre acceptée : « la sincérité exclusive (iḫlāṣ) » et "
         "« la conformité au modèle du Messager d'Allah — prière et salut d'Allah sur lui — "
         "(mutābaʿa) » — « la seconde condition est précisément l'exigence du hadīth de "
         "ʿĀʾiša » ; sincère mais « sans fondement ni preuve » → « rejetée à son auteur » ; "
         "al-Anʿām — référence imprimée 154, verset porteur 153 : « Voici Mon chemin, qui "
         "est droit », un chemin, pas des chemins."),
        ("Les deux āyāt de l'exploitation relues dans les conditions : al-Ḥašr 7 (référence "
         "imprimée : al-Bayyina 5) — prendre ce que le Messager a donné, s'abstenir de ce "
         "qu'il a interdit ; at-Tawba 105 (référence imprimée : an-Naml 19) — « Allah "
         "observera votre œuvre, de même que Son Messager et les croyants » : l'observance "
         "d'Allah, la conformité au Messager."),
        ("La pédagogie de la mesure : « Le besoin de s'orienter d'après l'exposé des "
         "savants et les règles de la Loi pour comprendre l'innovation » ; la préparation "
         "ouvre la leçon 10 (Nuʿmān ibn Bašīr, « J'expose le jugement des choses "
         "ambiguës (muštabahāt) et la méthode pour les traiter ») — du rejet de l'ajout "
         "au discernement de l'ambigu."),
    ],
    "vocabulaire": [
        {"ar": "الإحداث والابتداع في الدين", "translit": "al-iḥdāṯ wa-l-ibtidāʾ fī d-dīn",
         "fr": "l'introduction d'une nouveauté dans la religion — le titre arabe de la leçon ; la bidʿa dans la Loi est « une voie inventée dans la religion, qui ressemble à la Loi, et par laquelle on entend se rapprocher d'Allah » (al-Iʿtiṣām)."},
        {"ar": "البدعة", "translit": "al-bidʿa",
         "fr": "l'innovation — son jugement selon la leçon : « elle est rejetée à son auteur : rien n'en est accepté en droit, et elle ne comporte aucune récompense » ; la version de Muslim l'étend à « toute œuvre non conforme à la Loi »."},
        {"ar": "امرنا", "translit": "ʾamranā",
         "fr": "« notre affaire » — la glose du glossaire : « notre Loi et notre religion (šarʿunā wa-dīnunā) » ; le domaine dans lequel tout ajout est rejeté : « Quiconque introduit dans notre affaire présente ce qui n'en fait pas partie, cela en sera rejeté »."},
        {"ar": "احدث", "translit": "aḥdataṯa",
         "fr": "« il a introduit » — la glose du glossaire : « il a créé et forgé (anšaʾa wa-ḫtaraʿa) » ; le verbe du hadīth, première racine de l'innovation avec l'ibtidāʿ."},
        {"ar": "الرد", "translit": "ar-radd",
         "fr": "le rejet — « repoussé (mardūd) » ; le mot que la préparation de la leçon 8 demandait de déterminer : « Je détermine le sens de “ar-rad” (le rejet) dans le hadīth »."},
        {"ar": "القاعدة العامة", "translit": "al-qāʿida al-ʿāmma",
         "fr": "la règle générale — avec « un fondement authentique (aṣl ṣaḥīḥ) », l'un des deux rattachements qui sauvent une œuvre ; ce dont ne témoigne ni l'un ni l'autre « lui est rejeté, et il est pécheur »."},
        {"ar": "الاخلاص", "translit": "al-iḫlāṣ",
         "fr": "la sincérité exclusive — première des deux conditions : « Toute œuvre par laquelle on se rapproche d'Allah le Très-Haut ne profite pas à son auteur tant que deux conditions ne s'y réunissent pas »."},
        {"ar": "المطابعة", "translit": "al-mutābaʿa",
         "fr": "la conformité au modèle du Messager — seconde condition, « précisément l'exigence du hadīth de ʿĀʾiša » ; elle porte aussi le nom d'ittibāʿ dans les utilités : « L'incitation à la conformité au modèle (ittibāʿ) et la mise en garde contre l'innovation (ibtidāʿ) »."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

E_10 = {
    "auteur": "IA-1, tour R749",
    "resume": ("Guide de lecture de la leçon 10 (le licite, l'illicite et les choses "
               "ambiguës — al-ḥalāl wa-l-ḥarām wa-l-muštabahāt (الحلال والحرام والمشتبهات)) : "
               "le sixième hadīth des Quarante de l'imam al-Nawawī, rapporté par an-Nuʿmān "
               "ibn Bašīr — « Le licite est évident et l'illicite est évident ; et entre les "
               "deux se trouvent des choses ambiguës que beaucoup de gens ne connaissent pas "
               "» —, avec la parabole du berger autour d'une réserve, les trois « Sachez-le "
               "» et le morceau de chair qui est le cœur. Le tamhīd pose la règle de "
               "conduite : ne pas s'engager avant de connaître le jugement d'Allah, et "
               "« le mieux est de s'en abstenir par scrupule (at-tawarruʿ) » quand le statut "
               "hésite. L'analyse répond en trois stations : les trois catégories d'affaires "
               "au regard de la Loi (le licite pur, l'illicite évident, le douteux qui "
               "appelle le scrupule — la datte tombée), le jugement divergé des choses "
               "ambiguës (illicites, licites, ni l'un ni l'autre), les deux types de gens "
               "face à elles. L'exploitation imprime Ibn Raǧab : la troisième catégorie — "
               "celui qui connaît le jugement d'Allah et le suit — est « la meilleure des "
               "trois ». La préparation ouvre la leçon 11 : le cœur."),
    "explication": [
        ("La leçon 10 descend le garde-fou de la leçon 9 dans la vie quotidienne de "
         "l'élève : après le rejet de tout ajout dans la religion, la carte du terrain — ce "
         "qui est licite, ce qui est illicite, et ce qui hésite entre les deux. Elle répond "
         "à la préparation de la leçon 9 : « Je recherche la biographie du noble Compagnon "
         "Nuʿmān ibn Bašīr — qu'Allah l'agrée », « J'expose le jugement des choses "
         "ambiguës (muštabahāt) et la méthode pour les traiter ». Trois objectifs : « Que "
         "je me familiarise avec le licite, l'illicite et les choses ambiguës » ; « Que je "
         "distingue les catégories des choses ambiguës et leurs jugements » ; « Que je "
         "m'abstienne par scrupule des choses ambiguës, de crainte de tomber dans ce qui "
         "est illicite »."),
        ("Le tamhīd donne la règle de conduite avant les définitions : « Il convient au "
         "musulman de ne pas s'engager dans une affaire avant de connaître le jugement "
         "d'Allah à son sujet : si Allah l'a autorisée, il l'accomplit ; s'Il l'a interdite, "
         "il la délaisse ; et si son jugement hésite entre l'autorisation et l'interdiction "
         "et que son statut devient ambigu pour le responsable (al-mukallaf), le mieux est "
         "de s'en abstenir par scrupule (at-tawarruʿ) ». Quatre questions : « Qu'est-ce que "
         "le licite ? Qu'est-ce que l'illicite ? Que sont les choses ambiguës ? Et quelle "
         "est l'orientation de la Loi dans le traitement de celles-ci ? » — trois "
         "définitions et une méthode."),
        ("Le texte rend le hadīth en entier [Ṣaḥīḥ de al-Buḫārī et Muslim] : « Le licite "
         "est évident et l'illicite est évident ; et entre les deux se trouvent des choses "
         "ambiguës que beaucoup de gens ne connaissent pas. Quiconque se garde des choses "
         "douteuses préserve ainsi la pureté de sa religion et de son honneur, et quiconque "
         "tombe dans les choses douteuses tombe dans l'illicite, comme le berger qui fait "
         "paître autour d'une réserve et qui risque d'y paître. » Suivent trois « Sachez-le "
         "» : « tout roi possède une réserve » — « la réserve d'Allah, ce sont Ses "
         "interdictions » —, et le morceau de chair qui, « s'il est sain, rend sain tout le "
         "corps, et s'il est corrompu, corrompt tout le corps — sachez-le : c'est le cœur » "
         ". Le hadīth dépasse son titre : son dernier trait annonce la leçon 11, consacrée "
         "au cœur. La notice du transmetteur répond à la préparation : an-Nuʿmān ibn Bašīr "
         "ibn Saʿd ibn Ṯaʿlaba al-Anṣārī al-Ḫazraǧī, kunya Abū ʿAbd Allāh, « le premier "
         "enfant né dans l'islam parmi les Anṣār après l'Hégire » — né à Médine, du temps "
         "même du Messager d'Allah — ; « Muʿāwiya — qu'Allah soit satisfait de lui — le "
         "nomma gouverneur de la Kūfa, puis de Ǧumaṣ (Ḥimṣ) et du Qaṣāʾ de Damas. C'était "
         "un orateur éloquent. Il est décédé en l'an 65 de l'Hégire. »"),
        ("La compréhension donne huit gloses : « le licite (al-ḥalāl) » — « ce que la Loi "
         "a autorisé, ou ce dont aucune interdiction n'est connue » ; « l'illicite "
         "(al-ḥarām) » — « ce que la Loi est venue interdire » ; « les choses ambiguës "
         "(al-muštabahāt) » — « ce qui hésite entre le licite et l'illicite » ; « il s'est "
         "gardé (ittaqā) » — « il a pris garde et s'est abstenu » ; « il s'est préservé "
         "(istabrāʾa) » — « il a recherché la pureté et la sauvegarde à l'égard du péché » ; "
         "« l'honneur (al-ʿirḍ) » — « chez l'homme, le lieu de la louange et du blâme » ; "
         "« la réserve (al-ḥimā) » — « ce qui est interdit à quiconque n'en est pas le "
         "propriétaire » ; « il y paît (yartaʿī fīhi) » — « son bétail en mange et y "
         "broute ». L'extraction pose deux travaux : « Quel est le sens du licite et de "
         "l'illicite ? » et « Quel est le jugement des choses ambiguës ? »."),
        ("La première section classe les affaires au regard de la Loi en trois "
         "catégories. « Ce sur quoi Allah a tranché pour le déclarer licite est le licite "
         "pur et bon (al-ḥalāl aṭ-ṭayyib) » — « Il rend licites pour eux les bonnes choses "
         "et Il leur interdit les mauvaises » (Sourate al-Māʾida — la référence imprimée "
         "porte le verset 6 ; le verset qui porte ces paroles est al-Aʿrāf 157) ; « Et Il "
         "vous a rendu licites ce qui est au-delà de cela » (Sourate an-Nisāʾ — verset 24). "
         "« Ce sur quoi Allah a tranché pour le déclarer illicite est l'illicite évident » "
         "— « Sont illicites pour vous vos mères, vos filles » (Sourate an-Nisāʾ — verset "
         "23) ; « Et Il vous a interdit le gibier de la terre tant que vous êtes en état de "
         "sacralisation » (Sourate al-Māʾida — verset 96) — « ainsi que Sa prohibition des "
         "turpitudes, apparentes ou cachées, et de toute chose pour laquelle Allah a établi "
         "une peine (ḥadd), une sanction ou une menace »."),
        ("La troisième catégorie : « Ce que la Loi n'a pas explicitement tranché, en le "
         "déclarant illicite ou licite, et dont le moyen de le rattacher à l'un des deux ne "
         "s'est pas manifesté, sur lequel se disputent les arguments tirés du Livre et de "
         "la Sunna » — « il relève des choses douteuses, et l'abstention à son égard est un "
         "scrupule ». Le Prophète — prière et salut d'Allah sur lui — en donne la leçon par "
         "son propre geste : il « délaissa de manger la datte tombée (an-namra as-sāqiṭa) "
         "qu'il trouva dans sa maison » — « Si je n'avais pas craint qu'elle fût de "
         "l'aumône, je l'aurais mangée » [Sunan al-Bayhaqī al-kubrā] — et par sa règle : "
         "« Écarte ce qui te met dans le doute pour ce qui ne t'en met pas » [Sunan "
         "an-Nasāʾ] — le doute quitté pour le certain, même sur un petit bien."),
        ("La deuxième section expose la divergence des savants sur le statut des choses "
         "ambiguës, en trois positions : « elles sont illicites », d'après « il préserve "
         "ainsi la pureté de sa religion et de son honneur » — « quiconque ne préserve pas "
         "la pureté de sa religion et de son honneur est tombé dans l'illicite » ; « elles "
         "sont licites », d'après « comme le berger qui fait paître autour d'une réserve » "
         "— « cela indique en effet qu'elles sont licites, et que de les délaisser relève "
         "du scrupule (al-waraʿ) » ; « elles ne sont ni illicites ni licites », car lui "
         "« les a placées entre le licite et l'illicite » — « il convient donc que nous "
         "nous en abstenions, et cela relève du scrupule ». La divergence porte sur le "
         "statut, la conduite reste une : les trois positions demandent l'abstention."),
        ("La troisième section peint les deux types de gens : « un type qui s'en abstient "
         "par scrupule sans y tomber : sa religion et son honneur sont alors sauves » ; "
         "« un type qui s'y risque en dépit de leur caractère ambigu et s'expose par là "
         "aux choses illicites » — « la complaisance à leur égard incite à l'audace envers "
         "l'illicite ». La parabole est dépliée : « berger qui fait paître autour d'une "
         "réserve — un pâturage dont l'accès est interdit — et qui risque d'y paître ; "
         "car quiconque s'approche de l'interdit s'y trouve généralement mêlé ». Et le verset "
         "ferme le chemin des abords : « Telles sont les limites d'Allah — ne vous en "
         "approchez pas » (Sourate al-Baqara — la référence imprimée porte le verset 186 ; "
         "le verset qui porte ces paroles est le 187) — « elles interdisent ainsi de s'en "
         "approcher, par crainte de tomber dans l'illicite » : l'interdit a une garde, le "
         "scrupule la tient."),
        ("Ce qu'il faut retirer du hadīth, en deux : « La mise en garde contre tout ce qui "
         "mène à l'illicite, de crainte d'y tomber » ; « L'appel à éduquer au scrupule "
         "(al-waraʿ), à la continence (al-ʿafāf) et au contentement (al-qanāʿa) » — "
         "l'éducation du caractère comme protection de la religion. L'exploitation imprime "
         "Ibn Raǧab [Ǧāmiʿ al-ʿulūm wa-l-ḥikam] : la parole du hadīth sur celui qui se "
         "garde des choses douteuses « divise les gens, face aux choses ambiguës, en deux "
         "catégories » — « cela concerne celui sur qui elles sont devenues ambiguës, "
         "c'est-à-dire celui qui ne les connaît pas. Quant à celui qui les connaît et suit "
         "ce qui les lui indique, celui-là constitue une troisième catégorie, qui est la "
         "meilleure des trois ; car il connaît le jugement d'Allah, dans ces affaires "
         "ambiguës, à l'égard des gens, et il suit son savoir à ce sujet » — l'ambiguïté "
         "est relative à la personne, et la science du jugement sort du doute. L'exercice "
         "demande d'expliquer « les catégories de gens face aux choses ambiguës telles que "
         "le texte les met en lumière »."),
        ("L'évaluation en trois items : « Cite un exemple de licite et d'illicite, et deux "
         "exemples de choses ambiguës » ; « Explique la manière dont la Loi oriente le "
         "traitement des choses ambiguës parmi les affaires » ; « Explique le sens de Sa "
         "parole — prière et salut d'Allah sur lui : “Quiconque se garde des choses "
         "douteuses préserve ainsi la pureté de sa religion et de son honneur.” » — "
         "exemples, méthode, sens. La préparation ouvre la leçon suivante : « J'explique "
         "l'importance du cœur parmi les membres du corps » ; « Je précise l'effet du cœur "
         "sur la droiture de l'œuvre ou sur sa corruption » — le dernier trait du hadīth "
         "(le morceau de chair) devient la leçon 11, le septième hadīth des Quarante."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (familiariser avec licite, illicite, ambiguës ; "
         "distinguer leurs catégories et jugements ; s'abstenir par scrupule de crainte de "
         "tomber dans l'illicite) → tamhīd (connaître le jugement avant de s'engager ; le "
         "tawarruʿ ; quatre questions) → le hadīth en entier (réserve, cœur) → analyse en "
         "trois stations → deux utilités → exploitation (Ibn Raǧab, trois catégories) → "
         "préparation (le cœur)."),
        ("La continuité du fil : la préparation de la leçon 9 demandait la biographie de "
         "Nuʿmān ibn Bašīr et « J'expose le jugement des choses ambiguës (muštabahāt) et "
         "la méthode pour les traiter » — la leçon 10 y répond ; son hadīth portait déjà "
         "le cœur — la leçon 11 le lira pour lui-même."),
        ("Le hadīth en trois « Sachez-le » : « tout roi possède une réserve » — « la "
         "réserve d'Allah, ce sont Ses interdictions » ; le morceau de chair qui « s'il est "
         "sain, rend sain tout le corps », et s'il est corrompu, « corrompt tout le corps » "
         "— « sachez-le : c'est le cœur » ; la parabole du berger « qui fait paître autour "
         "d'une réserve et qui risque d'y paître »."),
        ("Les trois catégories d'affaires : « le licite pur et bon (al-ḥalāl aṭ-ṭayyib) » "
         "tranché par Allah (al-Aʿrāf 157 — référence imprimée al-Māʾida 6 ; an-Nisāʾ 24 "
         "correct) ; « l'illicite évident » — « Sont illicites pour vous vos mères, vos "
         "filles » (an-Nisāʾ 23), « le gibier de la terre tant que vous êtes en état de "
         "sacralisation » (al-Māʾida 96), les turpitudes et les peines ; le non-tranché "
         "« dont le moyen de le rattacher à l'un des deux ne s'est pas manifesté » — le "
         "scrupule."),
        ("Les deux preuves prophétiques du scrupule : « la datte tombée (an-namra "
         "as-sāqiṭa) » — « Si je n'avais pas craint qu'elle fût de l'aumône, je l'aurais "
         "mangée » [Sunan al-Bayhaqī al-kubrā] ; « Écarte ce qui te met dans le doute pour "
         "ce qui ne t'en met pas » [Sunan an-Nasāʾ]."),
        ("La divergence sur le statut, l'unanimité sur la conduite : « elles sont "
         "illicites » (d'après « il préserve ainsi la pureté de sa religion et de son "
         "honneur »), « elles sont licites » (d'après « le berger qui fait paître autour "
         "d'une réserve » — « de les délaisser relève du scrupule (al-waraʿ) »), « elles "
         "ne sont ni illicites ni licites » (placées « entre le licite et l'illicite ») — "
         "les trois positions demandent l'abstention."),
        ("Les deux types de gens : l'abstinent — « sa religion et son honneur sont alors "
         "sauves » ; le risqué — « la complaisance à leur égard incite à l'audace envers "
         "l'illicite » ; « Telles sont les limites d'Allah — ne vous en approchez pas » "
         "(référence imprimée : al-Baqara 186, verset porteur 187) — l'interdit a des "
         "abords gardés."),
        ("La troisième catégorie d'Ibn Raǧab : l'ambigu ne l'est que pour « celui qui ne "
         "les connaît pas » ; « celui qui les connaît et suit ce qui les lui indique » est "
         "« la meilleure des trois » — la science sort du doute ; la préparation ouvre la "
         "leçon 11 (« l'importance du cœur », « l'effet du cœur sur la droiture de l'œuvre "
         "ou sur sa corruption »)."),
    ],
    "vocabulaire": [
        {"ar": "الحلال والحرام والمشتبهات", "translit": "al-ḥalāl wa-l-ḥarām wa-l-muštabahāt",
         "fr": "le licite, l'illicite et les choses ambiguës — le titre de la leçon et le sixième hadīth des Quarante ; « entre les deux se trouvent des choses ambiguës que beaucoup de gens ne connaissent pas »."},
        {"ar": "المشتبهات", "translit": "al-muštabahāt",
         "fr": "les choses ambiguës — « ce qui hésite entre le licite et l'illicite » (glossaire) ; « ce que la Loi n'a pas explicitement tranché, en le déclarant illicite ou licite, et dont le moyen de le rattacher à l'un des deux ne s'est pas manifesté »."},
        {"ar": "التورع", "translit": "at-tawarruʿ",
         "fr": "le scrupule — « le mieux est de s'en abstenir par scrupule (at-tawarruʿ) » ; quand les savants disent les ambiguës licites, « de les délaisser relève du scrupule (al-waraʿ) »."},
        {"ar": "الحمى", "translit": "al-ḥimā",
         "fr": "la réserve — « ce qui est interdit à quiconque n'en est pas le propriétaire » (glossaire) ; « la réserve d'Allah, ce sont Ses interdictions » — le trait du berger qui risque « d'y paître »."},
        {"ar": "العرض", "translit": "al-ʿirḍ",
         "fr": "l'honneur — « chez l'homme, le lieu de la louange et du blâme » (glossaire) ; sa préservation fait partie des fruits de l'abstention : « préserve ainsi la pureté de sa religion et de son honneur »."},
        {"ar": "استبرا", "translit": "istabrāʾa",
         "fr": "« il s'est préservé » — « il a recherché la pureté et la sauvegarde à l'égard du péché » ; la glose du verbe du hadīth, comme « il s'est gardé (ittaqā) » — « il a pris garde et s'est abstenu »."},
        {"ar": "النمرة الساقطة", "translit": "an-namra as-sāqiṭa",
         "fr": "la datte tombée — délaissée par le Prophète de crainte qu'elle fût de l'aumône : « Si je n'avais pas craint qu'elle fût de l'aumône, je l'aurais mangée » [Sunan al-Bayhaqī al-kubrā]."},
        {"ar": "حدود الله", "translit": "ḥudūd Allāh",
         "fr": "les limites d'Allah — « Telles sont les limites d'Allah — ne vous en approchez pas » (référence imprimée al-Baqara 186, verset porteur 187) ; l'interdit a des abords, le scrupule les garde."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

ENTREES = [('pdf-9', E_9), ('pdf-10', E_10)]


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

# Garde-fous : volume (1700-2400 mots) + ponctuation FR + arabes hors parenthèses + guillemets
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']), sorted(data2['commentaires'].keys()))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
for DOCID in ('pdf-9', 'pdf-10'):
    e = data2['commentaires'][DOCID]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    fenetre = 'PASS' if 1700 <= mots <= 2400 else 'HORS FENETRE'
    print(f'{DOCID} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])} — fenêtre 1700-2400 : {fenetre}')
    if fenetre != 'PASS':
        mauvais += 1
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
        if not re.search(r'[\u02BE\u02BF]', v['translit']):
            print('   note : translit sans ʾ/ʿ :', v['translit'])
print('contrôle ponctuation/arabe FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')
if mauvais:
    sys.exit(1)
