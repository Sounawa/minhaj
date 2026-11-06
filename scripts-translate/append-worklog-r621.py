#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R621 — append du bloc worklog (garde : dernier Task ID lu au tail, jamais ≤)."""
import re, sys, datetime

WL = "/home/z/my-project/worklog.md"

def last_rid(txt):
    # seuls les EN-TÊTES de bloc « ## R620 — ... » font autorité
    ids = [int(m.group(1)) for m in re.finditer(r"^## R(\d{3,4}) —", txt, re.M)]
    return max(ids) if ids else 0

tail = open(WL, encoding="utf-8").read()[-6000:]
last = last_rid(tail)
if last >= 621:
    print(f"REFUS : worklog déjà à R{last} — pas d'append R621")
    sys.exit(1)

ts = datetime.datetime.now().strftime("%d-%m %H:%M")
block = (
    "\n\n## R621 — " + ts + " UTC+8 — leçon 8 ulum-hadith-tanawi-2 (pdf-mut23h2u-262, p.47-51) "
    "— L'AJOUT DU TRANSMETTEUR FIABLE, LE RETENU (MAḤFŪẒ) ET L'ANOMAL (ŠĀḎḎ) — tick C 19:49, Job 499558, "
    "trace 1a1a172f41684dc9-cron-agent-loop-202611061949 — ÉTAPES 0/1 : ls-remote + fetch (local AHEAD 1 commit "
    "f8cdda86 → PUSH immédiat rétabli, canal OK) ; ÉTAPE 2 : supervisor OK (487 cycles), heartbeat cron-alive.log posé ; "
    "ÉTAPE 3 : tail R620 → slot 262. TAKEOVER LÉGITIME du claim uh2-pdf-mut23h2u-262 (sous-agent détaché r621 "
    "« ouvrier-r621-1296040 », claim 11:01:03Z expiré à 50,8 min, WIP riche SANS livraison : 12 pages extraites "
    "4 couches tr-tmp/r621/ p047-p058 + 20 zones VLM vlm-A à vlm-S3 sur crops A-p47-matn à S3-p49-case4, "
    "mtimes figés à 10:52-11:01) — mtimes recoupés, registre 262 vide, aucune livraison antérieure ; "
    "SIX recadrages d'adjudication 450-900 dpi en lecture image DIRECTE de l'ouvrier "
    "(tr-tmp/qa-crops-r621/ADJ1-ADJ7o) ; NOMBRES DE LA COUCHE pdftotext INVERSÉS EN MIROIR, chaque inversion "
    "tranchée : «2/78»→t. 2, p. 87 (Maqāyīs al-luġa d'Ibn Fāris, entrée ḥ-f-ẓ — OCR+image concordantes «87/2»), "
    "«3/081»→t. 3, p. 180 بتصرف (entrée š-ḏ-ḏ), «2/802»→t. 2, p. 208 (al-Ǧāmiʿ li-aḫlāq ar-rāwī), "
    "«97»→p. 79 (Muqaddimat Ibn aṣ-Ṣalāḥ — ADJ6 image directe, vlm-I concordant) ; ADJUDICATIONS MOT À MOT "
    "documentées : matn du quote p. 47 tranché par QUATRE lectures concordantes (crops A/P/S1/S2 + OCR) "
    "«mā lam tanāfiʿa manāfiyatan li-man huwa awṯaq ; fa-in ḫuwwifa bi-arǧaḥ fa-r-rāǧiḥu l-maḥfūẓu wa-muqābila-hu "
    "š-šāḏḏ» (vlm-A «tanāfiʾ manāṭ al-ʿadl» récusé par triple concordance ; «ḫullifa» de vlm-P documenté en "
    "divergence) ; diagramme p. 48 tranché par ADJ1 image directe : selon le nombre DEUX cases (un seul / plus d'un), "
    "selon le lieu TROIS cases (dans l'isnād / dans le matn / dans les deux) — vlm-Q (3 cases sous le nombre, case "
    "coupée) récusé ; schéma p. 49 des quatre cas concordant à trois lectures (vlm-D/R/S3 + OCR) : non-contradiction "
    "→ مقبولة, contradiction avec plus fiable → مردودة, avec moins fiable → مقبولة, avec son pareil → يتوقف فيها ; "
    "matn de l'exemple du maḥfūẓ p. 49→50 porté AVEC les points de suspension IMPRIMÉS («qu'un homme mourut du "
    "vivant du Messager de Dieu…» — citation elliptique de l'imprimé, rien d'inventé) ; «fa-rāwā-hu ʿan ʿAmr b. "
    "Dīnār» rétabli par ADJ3 (OCR avait perdu fa-rāwā-hu) ; renvoi at-Tirmiḏī «bāb mā ǧāʾa fī l-iḍṭiǧāʿ» tranché "
    "par ADJ4 (vlm-G «al-inḍibāʿ» récusé) ; renvoi al-Buḫārī «kitāb al-ǧumuʿa, bāb aḍ-ḍiǧāʿa ʿalā š-šiqq al-ayman» "
    "tranché au zoom 900 dpi ×4 (ADJ7o — lectures intermédiaires de l'ouvrier «aṣ-ṣubḥ» et vlm-H «aḍ-ḍuḥā» récusées, "
    "OCR concordant) ; «Abū l-Aswad» porté (OCR concordant, vlm-H «Abū Hurayra» récusé) ; citation d'al-Ḫaṭīb "
    "al-Baġdādī p. 50-51 tranchée par ADJ4/ADJ5 : «yatamahhar» (OCR+vlm-M concordants), «yaqifu ʿalā ġawāmiḍi-hi» "
    "(OCR concordant, vlm-M «yaqiʿu» récusé), «yastanīru l-ḫafī» (OCR, vlm-M «yastīṯīru» récusé), «mutašattita-hu» "
    "(OCR), «wa-ḍamma baʿḍa-hu ilā baʿḍ» (image, vlm-M «wa-ḍaʿa» récusé), suite «wa-ḏakkā l-qalb, wa-ašḥaḏa ṭ-ṭabʿ, "
    "wa-bassaṭa l-lisān, wa-aǧāda l-bayān, wa-kašafa l-muštabah, wa-waḍaḥa l-multabas, wa-kasaba ayḍan ǧamīla "
    "ḏ-ḏikr, wa-taḫlīda-hu ilā āḫiri d-dahr» portée d'après ADJ5 (fragments brouillés pdftotext «al-hamma/al-qalb» "
    "réconciliés : «wa-ḏakkā l-qalb») ; «wa-lā yatāʾtā ḏālika ʿalā ṭarīq al-muḥaddiṯīn» (p. 48) porté tel qu'imprimé "
    "(deux couches concordantes, sens doctrinal — l'acceptation absolue de l'ajout ne s'obtient que par la voie des "
    "muḥaddiṯūn — restitué en traduction) ; questions d'istiṯmār «aqrāʾu n-naṣṣa wa-ubayyinu» (OCR+ADJ6 concordants, "
    "vlm-I «afrā» récusé) ; CONTENU : objectifs (4 buts), tamhīd (la contradiction dans la transmission et ses "
    "terminologies, selon le siṇd et le matn, selon l'état du rapporteur), matn du quote d'Ibn Ḥaǧar, fahm "
    "(aš-šarḥ : aṯ-ṯiqa = al-muʾtaman, yuṯaq ṯiqatan, pluriel ṯiqāt ; al-maḥfūẓ = ce que rapporta l'awṯaq contredisant "
    "ceux d'en dessous ; istiḫrāǧ al-maḍāmīn 2 tâches), trois sections (1. ziyādat aṯ-ṯiqa : définition "
    "(infirād du rapporteur avec addition non mentionnée), ce qu'on en tire (ziyādat al-aḥkām, taqyīd al-iṭlāq, "
    "iḍāḥat al-maʿānī), formes (nombre wāḥid/akṯar min wāḥid ; lieu fī s-sanad/fī l-matn/fī s-sanad wa-l-matn), "
    "statut (accepté sous condition de non-contradiction ; cas a non-contradiction → accepté en absolu au rang du "
    "hadith indépendant ; cas b contradiction → tarǧīḥ, on accepte le plus fort ; troupe de savants réputés pour "
    "l'acceptation absolue via la voie des muḥaddiṯūn ; les imams anciens ʿAbd ar-Raḥmān b. Mahdī, Yaḥyā "
    "al-Qaṭṭān, Aḥmad b. Ḥanbal, Yaḥyā b. Maʿīn, ʿAlī b. al-Madīnī, al-Buḫārī, Abū Zurʿa, Abū Ḥātim, an-Nasāʾī, "
    "ad-Dāraquṭnī — tarǧīḥ et pas d'acceptation absolue connue ; schéma des quatre cas) ; 2. al-maḥfūẓ : langue "
    "(ḥifẓ, ḥafaẓtu š-šayʾa ḥifẓan, taḥaffuẓ = peu de négligence, Maqāyīs t. 2 p. 87) + terminologie (awṯaq "
    "contredisant fiable d'en dessous ; tarǧīḥ par ḍabṭ accru, multitude ou autres voies), exemple du hadith du "
    "mourant au temps du Messager (at-Tirmiḏī/an-Nasāʾī/Ibn Māǧah via Ibn ʿAyna → ʿAmr b. Dīnār → ʿAwṣaǧa → Ibn "
    "ʿAbbās, abwāb al-farāʾiḍ, points de suspension imprimés ; Ibn Ǧurayǧ suit le waṣl ; Ḥammād b. Zayd contredit "
    "sans Ibn ʿAbbās ; Abū Ḥātim «le retenu est le hadith d'Ibn ʿAyna», Ḥammād pourtant ʿadl+ḍābiṭ, multitude "
    "préférée ; statut = genre du maqbūl) ; 3. aš-šāḏḏ : langue (infirād/mufāraqa, šāḏa yašīḏu šuḏūḏan, Maqāyīs "
    "t. 3 p. 180 بتصرف) + terminologie (maqbūl contredisant plus digne ; Ibn aṣ-Ṣalāḥ unifiait munkar/šāḏḏ, Ibn "
    "Ḥaǧar distingua — šāḏḏ rapporteur thiqah, munkar rapporteur ḍaʿīf — distinction aqwam wa-asadd, as-Saḫāwī la "
    "préféra), exemple : šuḏūḏ dans l'isnād (l'exemple précédent, médite-le) et dans le matn (hadith d'Abū Hurayra "
    "«qu'il s'allonge sur son côté droit» via Bušr b. Muʿāḏ al-ʿUqadī → ʿAbd al-Wāhid b. Ziyād → al-Aʿmaš → Abū "
    "Ṣāliḥ, abwāb aṣ-ṣalāt, bāb mā ǧāʾa fī l-iḍṭiǧāʿ ; correctif retenu : acte non parole, al-Buḫārī via ʿAbd "
    "Allāh b. Yazīd → Saʿīd b. Abī Ayyūb → Abū l-Aswad → ʿUrwa b. az-Zubayr → ʿĀʾiša, kitāb al-ǧumuʿa, bāb "
    "aḍ-ḍiǧāʿa ʿalā š-šiqq al-ayman ; statut = genre du mardūd)), ahtadī wa-aqtadī (citation d'al-Ḫaṭīb al-Baġdādī, "
    "al-Ǧāmiʿ t. 2 p. 208, lien : la réunion des voies révèle l'ajout) ; évaluation 3 items ; istiṯmār Ibn "
    "aṣ-Ṣalāḥ (l'isolement examiné, Muqaddima p. 79) + 2 questions ; al-iʿdād al-qablī 2 consignes (معنى الحديث "
    "المعروف والمنكر ; الفرق بين المنكر والشاذ) ; QA : qa-lesson.py PASS (27 968 car, 0 arabe, 62 « » appariées, "
    "0 apostrophe droite) ; verify-ulumhadith2-pdf262.py (nouveau) 121/121 PASS (bornes, inversions miroir "
    "documentées, voisins 255-261 intacts 17252/15854/19291/29786, 263 vide, livre 1 intacts 24319/16018/20967) ; "
    "REGISTRE : hand-set posé (1 171 → 1 172 savants : 1 114 hand + 58 llm) ; SYNC PORTAIL (méthode R618, cwd "
    "serveur /home/z/portal-r616 recoupé par /proc/<pid>/cwd) : content/books/ulum-hadith-tanawi-2.json + "
    "scripts-translate/savant-registry.json copiés, API 200 htmlFr 27 968 savant True après TTL 30 s ; QA NAVIGATEUR "
    "VERTE 1280/390 : route EFFECTIVE /#/livre/ulum-hadith-tanawi-2/pdf-mut23h2u-262 — h1 = « Leçon 8 : L'ajout du "
    "transmetteur fiable, le retenu (maḥfūẓ) », badge Traduction savante VISIBLE, 12 h2, 9 h3, 0 erreur console, "
    "0 overflow 1280 ET 390 (scrollW 1280/390 exact), captures tr-tmp/qa-r621-262-{1280,390}-full.png "
    "(1280×9015 / 390×17380) 10,0/15,1 % non-blanc ; ÉTAPE 5 : commit-push « R621 — leçon 8 ulum-hadith-tanawi-2 "
    "(pdf-mut23h2u-262, p.47-51) — livraison complète, takeover légitime du WIP sous-agent interrompu recoupé, "
    "verify 121/121, registre 1172 » [RÉSULTAT CI-DESSOUS SI PUSH] ; PROCHAINE PRIORITÉ R622+ : "
    "ulum-hadith-tanawi-2 leçon 9 (pdf-mut23h2u-263, الدرس 9 : الحديث المعروف والمنكر, bannière p.52, iʿdād déjà "
    "posée fin de leçon 8 : معنى الحديث المعروف والمنكر + الفرق بين المنكر والشاذ) — slot libre, à revendiquer ; "
    "hadith-2es : claims pdf-15/16/18/20/21/22/24/25 anciens (03-11/04-11, présumés périmés — vérifier avant tout "
    "takeover) ; dispatch sous-agent R622 tenté ×2 au tick 19:49 : ÉCHEC infrastructure Task tool (context deadline "
    "exceeded ×2) — production solo assumée, machine maintenue ; MÉTHODE : couches recoupées, NOMBRES miroir "
    "tranchés par recadrages 450-900 dpi + lecture image directe, jamais deviné ; tessdata ara = "
    "scripts-translate/tessdata du dépôt ; PARALLÈLE: 1 ; jamais deux ouvriers sur le même slot ; Task ID R622 et "
    "suivants, jamais ≤R621."
)
with open(WL, "a", encoding="utf-8") as f:
    f.write(block)
print("R621 append OK —", len(block), "car")
