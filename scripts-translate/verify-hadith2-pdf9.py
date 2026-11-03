#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-9 (leçon 8, صلاة الاستسقاء,
p.60-66) : contrôle de contenu, numéros du Muwaṭṭaʾ tranchés par preuve image
(515/513/514/518/516/517 contre couches 515ar/315/lettres/815/615 — mécanique
d'inversion totale R535-R541), bornes p.60-66 à triple convergence (objectifs
p.60, إعداد p.66 → القبلة, STARTS l8=60/l9=67 carte R534), AUCUN rendu du
cache coranique (aucun renvoi coranique au cours), isnāds tranchés par image
(Šurayk b. ʿAbdallāh b. Abī Namir contre lecture VLM « Ishāq … Abī Farwa »
récusée), lexies tranchées 400-600 dpi (farraqa/aġiṯnā ×3 [Muslim] ;
ṯalāṯu daʿawātin [Bayhaqī] ; mutabaḏḏilan/mutawāḍiʿan/mutaḍarriʿan [Tirmiḏī] ;
aǧzaʾatuhu contre couches aqhād/aḥzaz ; anǧayāt aṯ-ṯuqab), taqwīm q1 aux
CAUSES contre lecture VLM šurūṭ, fragments non élucidés déclarés.
Usage: python3 scripts-translate/verify-hadith2-pdf9.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-9-fr.html"

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
chk("h1 leçon 8", "leçon 8" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 60 à 66", "pages 60 à 66" in html)
chk("slot pdf-9 déclaré", "pdf-9" in html)
chk("badge portail Leçon 9 / 31", "Leçon 9 / 31" in text)
chk("hadith-2es déclaré", "hadith-2es" in html)
chk("miroir 208 pages cité", "deux cent huit pages" in html)

# takeover réglementaire consigné
chk("takeover réglementaire documenté", "TAKEOVER RÉGLEMENTAIRE" in html)
chk("claim R542 périmé consigné", "PÉRIMÉ" in html and "08\u00a0:01\u00a0:24Z" in html.replace("\u202f", "\u00a0"))
chk("R542/R543 non consignés comme livraisons", "étiquettes de claims non livrés" in html)
chk("GARDE-DOUBLON registre 1111 → 1112", "registre 1111 → 1112" in html)
chk("hadith-2es 8/30", "hadith-2es 8/30" in html)

# bornes triple convergence
chk("objectifs p.60", "page 60" in html)
chk("préparation p.66 déclarant القبلة", "page 66" in html and "qibla" in html)
chk("carte R534 l8=60", "l8 = 60" in html)
chk("carte R534 l9=67", "l9 = 67" in html)
chk("page 67 ouvre la leçon suivante", "page 67 ouvre la leçon suivante" in html)
chk("jamais devinée (borne)", "jamais devinée" in html)

# numéros Muwaṭṭaʾ tranchés + couches déclarées
for num, couche in [("515", "515ar"), ("513", "315"), ("514", "lettres"),
                    ("518", "815"), ("516", "615")]:
    chk(f"numéro {num} présent", f"n° {num}" in html)
chk("couche 315 déclarée", "315" in html)
chk("couche 815 déclarée", "815" in html)
chk("couche 615 déclarée", "615" in html)
chk("couche 515ar palindrome déclarée", "515ar" in html)
chk("inversion totale citée", "inversion totale" in html)
chk("numéro 517 présent", "n° 517" in html)
chk("série 50X déclarée", "50X" in html)

# AUCUN rendu du cache coranique
chk("aucun renvoi coranique", "aucun renvoi coranique" in html)
chk("aucun rendu du cache déclaré", "aucun rendu du cache coranique" in html)
chk("0 bloc citation coranique (leçon sans āya)", "Qâf." not in html and "L'Heure approche" not in html)
chk("sourates = matière de récitation", "matière de récitation" in html)

# isnāds tranchés
chk("ʿAmr b. Shuʿayb (tamhīd)", "ʿAmr b. Shuʿayb" in html)
chk("Yaḥyā b. Saʿīd (tamhīd)", "Yaḥyā b. Saʿīd" in html)
chk("ʿAbdallāh b. Abī Bakr b. Ḥazm", "ʿAbdallāh b. Abī Bakr b. Ḥazm" in html)
chk("ʿIbād b. Tamīm", "ʿIbād b. Tamīm" in html)
chk("ʿAbdallāh b. Zayd al-Māzinī", "ʿAbdallāh b. Zayd al-Māzinī" in html)
chk("Ṣāliḥ b. Kisān", "Ṣāliḥ b. Kisān" in html)
chk("ʿUbaydallāh b. ʿAbdallāh b. ʿUtba b. Masʿūd", "ʿUbaydallāh b. ʿAbdallāh b. ʿUtba b. Masʿūd" in html)
chk("Zayd b. Khālid al-Ǧuhanī", "Zayd b. Khālid al-Ǧuhanī" in html)
chk("Šurayk b. ʿAbdallāh b. Abī Namir", "Šurayk b. ʿAbdallāh b. Abī Namir" in html)
chk("Anas b. Mālik", "Anas b. Mālik" in html)
chk("VLM Ishāq… Abī Farwa récusée", "Ishāq b. ʿAbdallāh b. Abī Farwa" in html and "RÉFUTÉE PAR L’IMAGE" in html)
chk("cinq lectures VLM récusées déclaré", "cinq récusées par l’image" in html)

# matns et lexies tranchées
chk("duʿāʾ tamhīd : donne à boire à Tes serviteurs", "donne à boire à Tes serviteurs" in html)
chk("wa-bahīmatika tel qu'imprimé", "wa-bahīmatika" in html)
chk("écart wa-bahāʾimaka déclaré", "wa-bahāʾimaka" in html)
chk("répands Ta miséricorde", "répands Ta miséricorde" in html)
chk("contrée morte", "contrée morte" in html)
chk("yastasqūna bihī", "yastasqūna bihī" in html)
chk("al-muṣallā (premier texte)", "al-muṣallā" in html)
chk("rakʿatān (Mālik)", "rakʿatān" in html)
chk("qibla avant la khutba", "avant la khutba" in html)
chk("jehran — récitation à voix haute", "à voix haute" in html)
chk("hum quʿūd (assis)", "wa-hum quʿūd" in html)
chk("al-Ḥudaybiya (texte pluie)", "al-Ḥudaybiya" in html)
chk("ʿalā iṯri samāʾ", "iṯri samāʾ" in html)
chk("faveur de Dieu et Sa miséricorde", "la faveur de Dieu et Sa miséricorde" in html)
chk("bi-nawʾi ka-ḏā wa-ka-ḏā", "bi-nawʾi ka-ḏā wa-ka-ḏā" in html)
chk("kāfir bil-kawkab", "kāfir bil-kawkab" in html)
chk("muʾmin bil-kawkab", "muʿmin bil-kawkab" in html or "muʾmin bil-kawkab" in html)
chk("qazʿa (Anas/Bukhārī)", "qazʿa" in html)
chk("vendredi en vendredi", "vendredi en vendredi" in html)
chk("fragment VLM-seule déclaré", "lecture VLM seule déclarée" in html)
chk("farraqa (Muslim)", "farraqa" in html)
chk("aġiṯnā ×3", html.count("donne-nous à boire") >= 3)
chk("renvoi Muslim", "Ṣaḥīḥ Muslim" in html)
chk("ṯalāṯu daʿawātin lā turaddu", "ṯalāṯu daʿawātin lā turaddu" in html)
chk("invocation du parent", "l’invocation du parent" in html)
chk("celui qui jeûne", "celui qui jeûne" in html)
chk("invocation du voyageur", "l’invocation du voyageur" in html)
chk("renvoi Bayhaqī", "al-Bayhaqī" in html)
chk("mutabaḏḏilan", "mutabaḏḏilan" in html)
chk("mutawāḍiʿan", "mutawāḍiʿan" in html)
chk("mutaḍarriʿan", "mutaḍarriʿan" in html)
chk("renvoi Tirmiḏī", "Sunan at-Tirmiḏī" in html)
chk("clôture suspendue jamais reconstituée", "jamais reconstituée" in html)
chk("al-Bukhārī fī ṣaḥīḥihī (ʿUmar/ʿAbbās)", "al-Buḫārī" in html or "al-Bukhārī" in html)
chk("faḥaṭū (sécheresse)", "faḥaṭ" in html)
chk("al-ʿAbbās b. ʿAbd al-Muṭṭalib", "al-ʿAbbās b. ʿAbd al-Muṭṭalib" in html)
chk("fa-sqinā", "fa-sqinā" in html)
chk("renvoi Bukhārī", "Ṣaḥīḥ al-Bukhārī" in html)
chk("aǧzaʾatuhu", "aǧzaʾatuhu" in html)
chk("couches aqhād/aḥzaz déclarées", "aqhād" in html and "aḥzaz" in html)
chk("Sabaḥ isma rabbika l-aʿlā", "Sabaḥ isma rabbika l-aʿlā" in html)
chk("al-Ġāšiyya", "al-Ġāšiyya" in html)
chk("aš-Šams wa-ḍuḥāhā", "aš-Šams wa-ḍuḥāhā" in html)
chk("al-Muhallab (sagesse ridāʾ)", "al-Muhallab" in html)
chk("tafāʾul", "tafāʾul" in html)
chk("anǧayāt aṯ-ṯaqab", "anǧayāt aṯ-ṯuqab" in html)
chk("ẓuhūr al-ǧibāl wa-l-ʾakām", "ẓuhūr al-ǧibāl wa-l-ʾakām" in html)
chk("buṭūn al-ʾawdiya", "buṭūn al-ʾawdiya" in html)
chk("manābit aš-šaǧar", "manābit aš-šaǧar" in html)
chk("huwa min ḏālika fī saʿa", "fī saʿa" in html)

# transmetteurs
chk("Ibn Umm ʿAmāra", "Ibn Umm ʿAmāra" in html)
chk("jour de la Ḥarra an 63", "Ḥarra" in html and "soixante-trois" in html)
chk("kunyā Abū ʿAbd ar-Raḥmān", "Abū ʿAbd ar-Raḥmān" in html)
chk("assista à al-Ḥudaybiya", "avait assisté à al-Ḥudaybiya" in html)
chk("as-Sāʾib b. Yazīd al-Kindī", "as-Sāʾib b. Yazīd al-Kindī" in html)
chk("Saʿīd b. al-Musayyab", "Saʿīd b. al-Musayyab" in html)
chk("Abū Salama b. ʿAbd ar-Raḥmān", "Abū Salama b. ʿAbd ar-Raḥmān" in html)
chk("Bisr b. Saʿīd", "Bisr b. Saʿīd" in html)
chk("mort an 78, 85 ans", "soixante-dix-huit" in html and "quatre-vingt-cinq" in html)

# structure des sections
for section in ["Les objectifs de la leçon", "Le tamhīd", "Les textes du cours",
                "Les traductions des transmetteurs", "Les définitions du cours",
                "L’extraction des contenus", "Le corps du cours", "L’évaluation",
                "L’exploration", "La préparation préalable"]:
    chk(f"section « {section} »", section in html)
chk("trois textes du cours", html.count("<h3>Le ") >= 3 and "Le troisième texte" in html)
chk("quatre bienséances", "Première —" in html and "Quatrième —" in html)
chk("trois objectifs", "Que je connaisse la manière" in html and "sollicite l’abreuvement" in html)
chk("préparation : bienséances de la qibla", "les bienséances de la qibla" in html)
chk("préparation : cause du retournement", "cause du retournement de la qibla" in html)
chk("évaluation q1 aux causes (contre VLM šurūṭ)", "Je cite les causes" in html and "šurūṭ" in html)
chk("évaluation q3 : Dieu fait descendre la pluie", "fait descendre la pluie" in html)

# typographie redondante (double contrôle indépendant de qa-lesson)
chk("0 apostrophe droite", "'" not in html)
chk("guillemets appariés", html.count("«") == html.count("»"))
chk("0 marqueur TODO/XXX/【", "TODO" not in html and "XXX" not in html and "【" not in html)
chk("ﷺ symbole corpus présent", "ﷺ" in html)

print(f"verify-hadith2-pdf9 : {ok} contrôles OK, {fail} échec(s)")
raise SystemExit(1 if fail else 0)
