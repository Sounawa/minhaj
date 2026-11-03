#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-11 (leçon 10, الطهارة لمس
المصحف وسجود التلاوة, p.73-78 + p.79 matière) : contrôle de contenu,
numéros du Muwaṭṭaʾ tranchés par preuve image (536/540/555/556/544 contre
couches 635/045/555/65/445 — mécanique d'inversion totale R535-R544),
bornes p.73-78 à convergence d'image (objectifs p.73, إعداد p.78,
ouverture du cours suivant p.79 — écart carte R534 (73-79) déclaré),
isnāds tranchés par image (ʿAbdallāh b. Abī Bakr b. Ḥazm ; Dāwūd b. al-Ḥuṣayn
/ al-Aʿraǧ / ʿAbd ar-Raḥmān b. ʿAbd al-Qārī / ʿUmar ; Hišām b. ʿUrwah /
son père / ʿĀʾiša, al-Ḥāriṯ b. Hišām demandeur dans le matn),
ĀYĀT rendues du cache coranique (al-Ḥiǧr 9 cache 9 ; « lā yamassuhu illā
l-muṭahharūn » = cache al-Wāqiʿa 79, imprimé 82 — écart documenté,
correspondance par le texte), lexies tranchées 400-1000 dpi
(taliḥaqhā contre taliḥaqhumā ; fuḍiʿat contre muniʿat ;
ʿaraqan contre ḥarqan ; fa-lā iṯm ʿalayhi contre fa-lā inna ʿalayhi ;
šann muʿallaqa / fa-tawaḍḍaʾ minhā), fragments non élucidés déclarés
(queue de la liste …lam/tanzīl/wa-ṣ/ḥam ; wa-n-Naǧmi yanzil?? ; wa-ʿiṯtu??).
Usage: python3 scripts-translate/verify-hadith2-pdf11.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-11-fr.html"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read()
text = re.sub(r"<[^>]+>", " ", html).replace("\u202f", " ").replace("\u00a0", " ")

# 0 arabe (ﷺ U+FDFA exempté par convention corpus)
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", text)
arab = [c for c in arab if c != "\ufdfa"]
chk("0 caractère arabe au corps", len(arab) == 0)

# structure générale
chk("h1 leçon 10", "leçon 10" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 73 à 79 citées (miroir)", "pages 73 à 79" in html)
chk("slot pdf-11 déclaré", "pdf-11" in html)
chk("badge portail Leçon 11 / 31", "Leçon 11 / 31" in text)
chk("hadith-2es déclaré", "hadith-2es" in html)
chk("miroir 208 pages cité", "deux cent huit pages" in html)

# chaîne de production consignée
chk("sous-agent 1737 consigné", "1737" in html)
chk("claim rafraîchi consigné", "10 :20 :06Z" in text)
chk("pdf-10 concurrent intact", "R545-takeover" in html)
chk("GARDE-DOUBLON registre 1113 → 1114", "registre 1113 → 1114" in html)
chk("livraison concurrente R546 consignée", "R546" in html and "b2b443d" in html)
chk("hadith-2es 10/30", "hadith-2es 10/30" in html)

# bornes + écart carte déclaré
chk("objectifs p.73", "page 73" in html)
chk("évaluation/préparation p.78", "page 78" in html)
chk("page 79 ouvre la leçon suivante", "page 79 ouvre la leçon suivante" in html)
chk("carte R534 l10=73", "l10 = 73" in html)
chk("carte R534 l11=80", "l11 = 80" in html)
chk("écart borne haute carte déclaré", "écart de la borne haute" in html)
chk("jamais devinée (borne)", "jamais devinée" in html)

# numéros Muwaṭṭaʾ tranchés + couches déclarées
for num, couche in [("536", "635"), ("540", "045"), ("555", "555"),
                    ("556", "65"), ("544", "445")]:
    chk(f"numéro {num} présent", f"n° {num}" in html)
chk("couche 635 déclarée", "635" in html)
chk("couche 045 déclarée", "045" in html)
chk("couche 65 déclarée", "« 65 »" in text)
chk("couche 445 déclarée", "445" in html)
chk("inversion totale citée", "inversion totale" in html)

# isnāds tranchés
chk("isnād lettre : ʿAbdallāh b. Abī Bakr b. Ḥazm", "ʿAbdallāh b. Abī Bakr b. Ḥazm" in html)
chk("isnād ʿUmar complet", "Dāwūd b. al-Ḥuṣayn" in html and "al-Aʿraǧ" in html
    and "ʿAbd ar-Raḥmān b. ʿAbd al-Qārī" in html and "ʿUmar b. al-Ḫaṭṭāb" in html)
chk("isnād ʿĀʾiša complet", "Hišām b. ʿUrwah" in html and "d’après son père" in html
    and "ʿĀʾiša" in html)
chk("al-Ḥāriṯ b. Hišām demandeur dans le matn", "al-Ḥāriṯ b. Hišām" in html)
chk("destinataire de la lettre = ʿAmr b. Ḥazm", "ʿAmr b. Ḥazm" in html)

# āyāt rendues du cache + écarts documentés
chk("rendu cache al-Ḥiǧr 9", "En vérité c’est Nous qui avons fait descendre le Coran, et c’est Nous qui en sommes gardien." in html)
chk("renvoi imprimé Ḥiǧr 9", "l’āya 9" in html)
chk("rendu cache Wāqiʿa 79", "que seuls les purifiés touchent" in html)
chk("renvoi imprimé Wāqiʿa 82 tranché image", "l’āya 82" in text and "« 28 »" in text)
chk("correspondance par le texte documentée", "correspondance par le texte" in html)
chk("règle Kahf non applicable déclarée", "ne s’applique pas à cette āya" in html)

# lexies tranchées
chk("taliḥaqhā contre taliḥaqhumā", "taliḥaqhā" in html and "taliḥaqhumā" in html)
chk("fuḍiʿat contre muniʿat", "fuḍiʿat" in html and "muniʿat" in html)
chk("ʿaraqan contre ḥarqan", "ʿaraqan" in html and "ḥarqan" in html)
chk("fa-lā iṯm contre fa-lā inna", "fa-lā iṯm ʿalayhi" in html and "fa-lā inna ʿalayhi" in html)
chk("šann muʿallaqa portée", "šann muʿallaqa" in html and "fa-tawaḍḍaʾ minhā" in html)

# fragments déclarés (jamais reconstitués)
chk("queue de liste fragments déclarée", "…lam / tanzīl / wa-ṣ / ḥam" in html
    and "jamais reconstituées" in html)
chk("wa-n-Naǧmi yanzil?? fragment déclaré", "wa-n-Naǧmi yanzil" in html)
chk("wa-ʿiṯtu?? réserve déclarée", "wa-ʿiṯtu" in html and "réserve déclarée" in html)

# doctrine clé
chk("onze prosternations portée", "onze prosternations" in html)
chk("Mufaṣṣal sans prosternation", "Mufaṣṣal" in html)
chk(" deux transmissions de Mālik", "deux transmissions" in html)
chk("Mudawwana : Ibn al-Qāsim", "Ibn al-Qāsim" in html and "Mudawwana" in html)
chk("Biographie ʿAmr b. Ḥazm (Naǧrān, an 51)", "Naǧrān" in html and "an cinquante et un" in html)
chk("dix āyāt finales d’Āl ʿImrān", "Āl ʿImrān" in html)

# préparation préalable : matière leçon suivante déclarée
chk("slot pdf-12 déclaré", "pdf-12" in html)
chk("lexies ʿadl ʿašar / riqāb / ḥirz", "ʿadl ʿašar" in html and "riqāb" in html
    and "ḥirz min aš-šayṭān" in html)
chk("matière āyāt non tranchées déclarée", "chiffres imprimés non tranchés" in html)

print(f"verify-hadith2-pdf11 : PASS {ok} contrôles, {fail} échec" if fail == 0
      else f"verify-hadith2-pdf11 : ÉCHEC {fail} / {ok+fail}")
raise SystemExit(0 if fail == 0 else 1)
