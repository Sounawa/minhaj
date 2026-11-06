# -*- coding: utf-8 -*-
"""R620 — append worklog leçon 7 ulum-hadith-tanawi-2 (pdf-mut23h2u-261).
Garde anti double-append : NO-OP si une entrée R620 ou R621 est déjà présente
(méthode append-worklog-r619.py), et NO-OP si le dernier ID dépasse R620.
"""
import io
import sys

WL = "/home/z/my-project/worklog.md"
TRACE = "1a1a172f41684dc9-cron-agent-loop-202611061826"

ENTRY = (
    "\nR620 — leçon 7 ulum-hadith-tanawi-2 (pdf-mut23h2u-261, p.41-46, الدرس 7 : الحديث الحسن) : "
    "tick C 18:19+08 (trace " + TRACE + ") ; ÉTAPES 0/1/2 : contrôle GitHub OK (distant 727df3c5, zéro retard, jamais reset), "
    "commit R619-bis resté en retard POUSSÉ (86850cc6, push sec OK), supervisor v4 ACTIF, heartbeat cron-alive 18:26 ; "
    "ÉTAPE 3bis : claim pdf-mut23h2u-261 posé (trace du tick, refresh 10:30:55Z) ; "
    "WIP de la passe interrompue 17:57-17:58 RECOUPÉ (13 verdicts VLM zones A1-F1 + 21 crops G1-G6/N1 dans tr-tmp/qa-crops-r620/, "
    "aucune livraison, registre 261 vide — claimant défunt recoupé, méthode R619) ; "
    "SOUS-AGENT FANTÔME CONFIRMÉ : dispatch Task « context deadline exceeded » mais sous-agent SURVÉCU DÉTACHÉ — "
    "claim uh2-pdf-mut23h2u-262 posé par lui, extraction tr-tmp/r621/ p047-p051 + crops en cours → slot 262 COUVERT, "
    "zéro chevauchement (piège R619), ce tick NE TOUCHE PAS 262 ; "
    "BORNES : p.41-46 par DOUBLE sondage, jamais devinées (p.41 = bannière الدرس 7 + boîte jaune 3 objectifs + tamhīd + matn ; "
    "p.46 = évaluation 4 items + boîte verte istiṯmār + atāmal an-naṣṣ 2 questions + al-iʿdād al-qablī 3 consignes ; "
    "p.47 = bannière leçon 8 زيادة الثقة والمحفوظ والشاذ, sondage OCR 300 dpi) ; "
    "PRODUCTION : extraction multicouche tr-tmp/r619/ + tr-tmp/r620/ (pdftotext incorporée + OCR 300 dpi tesseract psm 4 "
    "TESSDATA_PREFIX=scripts-translate/tessdata du dépôt + couche logique FIDÈLE PyMuPDF p041-pymu.txt → p046-pymu.txt), "
    "NEUF recadrages d'adjudication 600-1500 dpi (tr-tmp/qa-crops-r620/ADJ1-ADJ12, lecture image DIRECTE de l'ouvrier) ; "
    "NOMBRES DE LA COUCHE pdftotext INVERSÉS EN MIROIR, chaque inversion tranchée : «114/13»→t. 13, p. 114 (Lisān al-ʿarab), "
    "«32-31»→p. 31-32 (Muqaddimat Ibn aṣ-Ṣalāḥ), «45/2»→t. 2, p. 45 (aš-Šifāʾ du qāḍī ʿIyāḍ), «29-28»→p. 28-29 (al-Mūqiẓa), "
    "n° de page «14»→41 ; ADJUDICATIONS MOT À MOT documentées : matn du quote « فلتردد في التقليد حيث التفرد وإلا فاعتبار إسنادين » "
    "tranché au recadrage 900 dpi (lectures basses « الناقل/التقرد » récusées par l'image) ; "
    "« وهو مع ذلك يرفع عن حال من بعد ما انفرد به من حديثه منكرا » porté TEL QU'IMPRIMÉ (lectures concordantes 600/900/1200 dpi — "
    "paraphrase imprimée du « يخاف على حاله » classique d'Ibn aṣ-Ṣalāḥ, sens doctrinal restitué en traduction FR) ; "
    "« بن عاقبة » (image directe 600 dpi) face à « علقمة » (OCR tesseract 300 dpi) — divergence documentée, portée sur la lecture image ; "
    "« المشهورين » (OCR) / « الشهورين » (image) — même racine شهر, rendu FR identique ; "
    "matn ابن حبان « له ابنتان... » tranché par l'OCR 300 dpi concordant au renvoi (lecture vlm-C2 divergente récusée) ; "
    "récit Mālik « توضأ وتهيأ ولبس ثيابه ثم يحدث » tranché par l'OCR (lecture vlm-E3 « ولم يثبه » récusée par le sens) ; "
    "istiṯmār « لا تظنن أن الحسن قاعدة... » (trois lectures image) face à « لا تطمع بأن للحسن » (OCR) — image majoritaire portée, OCR documenté ; "
    "en-tête « ثانيا : مراتب الحسن، مصادره، حكمه » + titre « 3. حكم الحديث الحسن » CONFIRMÉS par recadrages ADJ11/ADJ5 "
    "(le paragraphe مصادر الحسن كثيرة, sauté par les crops G4, rétabli par l'OCR 300 dpi) ; "
    "CONTENU : définition لغة (ṣifa mušabbaha du ḥusn, Lisān t. 13 p. 114) + اصطلاحا (deux sections), "
    "les deux sections du ḥasan li-ḏāti-hi d'Ibn aṣ-Ṣalāḥ (mastūr / mašhūrīn bi-aṣ-ṣidq wa-l-amāna, muwāfaqa + šāhid, "
    "propos d'at-Tirmiḏī sur la 1re et d'al-Ḫaṭābī sur la 2e, Muqaddima p. 31-32), "
    "ḥasan li-ġayri-hi (définition Muqaddima p. 31, cause du nom, image combinée qui répare le déficit de ḍabṭ), "
    "TROIS exemples (siwāk « لولا أن أشق على أمتي... » + comment d'Ibn aṣ-Ṣalāḥ ص. 35 Muḥammad b. ʿAmr b. ʿĀqiba ; "
    "deux filles d'Ibn Ḥibbān « ما من مسلم له ابنتان... » + isnād Abū Yaʿlā→Abū Ḫayṯama→Ǧarīr→Fiṭr→Šurayḥ b. Saʿd→Ibn ʿAbbās, "
    "ḥasan bi-šawāhidi-hi, ad-Dāraquṭnī, Ǧarīr = Ibn ʿAbd al-Ḥamīd, Fiṭr = Ibn Ḫalīfa al-Maḫzūmī ; "
    "vin des orphelins « كان عندنا خمر يتامى... » + Maǧlad affaibli par une troupe mais at-Tirmiḏī l'a déclarée ḥasan, "
    "ṣunna rapportée par d'autres voies) ; "
    "degrés (Baḥz b. Ḥakīm et ʿAmr b. Šuʿayb pères-grands-pères = plus bas degré du ṣaḥīḥ, puis al-Ḥāriṯ b. ʿAbd Allāh et ʿĀṣim b. Ḍamura, "
    "al-Mūqiẓa ص. 32) ; sources (Sunan/Musnads/Muṣannafs, Ǧāmiʿ at-Tirmiḏī أصل en la connaissance du ḥasan sans réserve exclusive) ; "
    "statut (maqbūl muḥtaǧǧ bi-hi, li-ḏāti-hi plus fort que li-ġayri-hi, معنى قولهم « حسن صحيح » = deux isnād, "
    "objection « حسن غريب » et réponse, les SEPT formules d'at-Tirmiḏī, citation finale « وما قلنا في كتابنا حديث حسن... عندنا ») ; "
    "ahtadī wa-aqtadī (Mālik en ablutions par vénération, aš-Šifāʾ t. 2 p. 45) ; "
    "évaluation 4 items ; istiṯmār adh-Dhahabī (variation de l'iǧtihād du ḥāfiẓ, al-Mūqiẓa p. 28-29) + atāmal 2 questions ; "
    "al-iʿdād al-qablī 3 consignes (حكم زيادة الثقة ; تعريف الشاذ والمحفوظ وأمثلة ; الفرق بين الشاذ والمحفوظ) ; "
    "QA : qa-lesson.py PASS (28 694 car, 0 arabe, 69 « » appariées, 0 apostrophe droite) ; "
    "verify-ulumhadith2-pdf261.py (nouveau) 113/113 PASS (bornes, inversions miroir documentées, "
    "voisins 255-260 intacts 17252/15854/23766/19291/23786/29786, 262 vide, livre 1 intacts 24319/16018/20967) ; "
    "REGISTRE : hand-set posé (1 170 → 1 171 savants : 1 114 hand + 57 llm) ; "
    "SYNC PORTAIL : content/books/ulum-hadith-tanawi-2.json + scripts-translate/savant-registry.json copiés vers portal-r616 (méthode R618) ; "
    "QA NAVIGATEUR VERTE 1280/390 : la route SANS hash /livre/... renvoie 404 app (documenté), route EFFECTIVE "
    "/#/livre/ulum-hadith-tanawi-2/pdf-mut23h2u-261 — h1 = « Leçon 7 : Le hadith satisfaisant (ḥasan) », badge Traduction savante VISIBLE "
    "(API 200 après sync), 0 overflow 1280 ET 390 (scrollW 390 exact), 11 h2, 0 erreur console, "
    "captures tr-tmp/qa-r620-261-{1280,390}-full.png (1280×9297 / 390×17908) 10,0/15,1 % non-blanc ; "
    "ÉTAPE 5 : commit-push « R620 — leçon 7 ulum-hadith-tanawi-2 (pdf-mut23h2u-261, p.41-46) — livraison complète, WIP interrompu recoupé, "
    "sous-agent fantôme confirmé sur 262, verify 113/113, registre 1171 » [RÉSULTAT CI-DESSOUS SI PUSH] ; "
    "PROCHAINE PRIORITÉ R621+ : ulum-hadith-tanawi-2 leçon 8 (pdf-mut23h2u-262, الدرس 8 : زيادة الثقة والمحفوظ والشاذ, p.47-?) — "
    "CLAIM ACTIF détenu par le sous-agent détaché (r621 p047-p051 en cours) : NE PAS rouvrir 262 tant que le claim vit "
    "(expiration 50 min, takeover autorisé si périmé, vérifier mtimes avant de finaliser) ; "
    "hadith-2es : claims pdf-15/16/18/20/21/22/24/25 actifs côté ouvriers voisins ; "
    "MÉTHODE : couches recoupées, NOMBRES miroir tranchés par recadrages 600-1500 dpi + lecture image, jamais deviné ; "
    "tessdata ara = scripts-translate/tessdata du dépôt ; PARALLÈLE: 1 ; jamais deux ouvriers sur le même slot ; "
    "Task ID R621 et suivants, jamais ≤R620.\n"
)


def main() -> int:
    with io.open(WL, encoding="utf-8") as f:
        content = f.read()
    import re
    ids = [int(m.group(1)) for m in re.finditer(r"^R(\d+) —", content, flags=re.M)]
    if "R620 — leçon 7 ulum-hadith-tanawi-2" in content or "R621 —" in content:
        print("NO-OP : entrée R620/R621 déjà présente")
        return 0
    if ids and max(ids) > 620:
        print(f"NO-OP : dernier ID R{max(ids)} > R620")
        return 1
    with io.open(WL, "a", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"APPEND R620 OK (dernier ID avant : R{max(ids) if ids else 0})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
