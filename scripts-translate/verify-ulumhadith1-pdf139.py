#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2r-139
(le ḥadīṯ fabriqué al-mawḍūʿ, p.133-136 du manuel ulum-hadith-1-thanawi.pdf)
: bannière p.133 (OCR r608/t133.txt + image 900 dpi) ; bornes p.133-136 par
DOUBLE sondage (aucune bannière p.134-138 ; p.137 = ornement + notices,
Ibn Abī Ḥātim, OCR r610/t137.txt) ; bayt du nāẓim « wa-l-kaḏibu l-muḫtalaqu
l-maṣnūʿu * * * ʿalā n-nabiyyi fa-ḏālika l-mawḍūʿu » tranché PAR L'IMAGE 900
dpi (boîte p.133 + répétition p.134 après bi-qawlihi, rime maṣnūʿ/mawḍūʿ) ;
glose ×3 définitions ; istikhāṣ al-mafāhīm + 2 questions (Q1 muette OCR, image
900 dpi) ; 3 divisions selon la matière (ḥubbu d-dunyā 900 dpi — OCR récusé —
Mālik b. Dīnār/Ibn Abī d-Dunyā/Bayhaqī/Shuʿab + Irāqī šabhu r-rīḥ ; al-maʿidatu
baytu d-dāʾi ; emprunt + isnād sain composé) ; 2 divisions selon le dessein
(Thābit b. Mūsā, Šurayk, Ibn Māǧah, yaʿhadu š-šayṭānu 900 dpi — yaʿidu récusé)
; 4 causes du waḍʿ (tašakkuk 900 dpi bullet omis OCR ; ittibāʿ al-hawā ;
iktisāb/irtizāq/iġtirāb — iġrāb récusé ; ġalabat al-ǧahl) ; khaṭima 2 bayts
(maẓūmat l-Bayqūnī, 34 bayts, fawqa ṯ-ṯalāṯīna) ; taqwīm ×3 ; istiṯmār 2
hadiths (Bukhārī Mughīra man kaḏaba ʿalayya mutaʿammidan 900 dpi — OCR récusé
; Muslim Muqaddima) ; examen aš-šarḥ d'al-Zarqānī ×2 questions ; bornes ;
zéro āya, zéro arabe, zéro doublon, registre/voisins intacts.
Usage: python3 scripts-translate/verify-ulumhadith1-pdf139.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2r-139-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-1.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC : {label}")


h = open(HTML, encoding="utf-8").read()
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", "").replace("\u2009", ""))
txt = re.sub(r"<[^>]+>", "", h)

# h1 aligné au titleFr pré-mappé
chk("h1 = titleFr « Le hadith fabriqué (mawḍūʿ) »",
    hn.startswith("<h1>Le hadith fabriqué (mawḍūʿ) :"))
chk("h1 mentionne leçon 28", "leçon 28" in h[:400])
chk("h1 mentionne manẓūma d’al-Bayqūnī", "manẓūma d’al-Bayqūnī" in h[:400])

# bayt du nāẓim (boîte p.133 + répétition p.134)
chk("bayt hémistiche 1 (matn)", "wa-l-kaḏibu l-muḫtalaqu l-maṣnūʿu" in h)
chk("bayt hémistiche 1 ×2 (matn + définition p.134)",
    h.count("wa-l-kaḏibu l-muḫtalaqu l-maṣnūʿu") >= 2)
chk("bayt hémistiche 2 « ʿalā n-nabiyyi fa-ḏālika l-mawḍūʿu »",
    "ʿalā n-nabiyyi fa-ḏālika l-mawḍūʿu" in h)
chk("bayt hémistiche 2 ×2 (matn + définition p.134)",
    h.count("ʿalā n-nabiyyi fa-ḏālika l-mawḍūʿu") >= 2)
chk("adjudication 900 dpi du bayt", "900&nbsp;dpi" in h)
chk("rime maṣnūʿ/mawḍūʿ attestée", "attestée à l’image" in h)
chk("introduction encadré qāla n-nāẓimu", "qāla n-nāẓimu raḥimahu llāhu taʿālā" in h)

# tamhīd : bayt citation + question de transition
chk("tamhīd bayt « wa-kullu mā ʿan rutbati l-ḥusni qaṣur »",
    "wa-kullu mā ʿan rutbati l-ḥusni qaṣur" in h)
chk("tamhīd « fa-huwa ḍ-ḍaʿīf »", "fa-huwa ḍ-ḍaʿīf" in h)
chk("tamhīd question de transition", "qu’est-ce donc que le ḥadīṯ fabriqué" in hn.lower()
    or "qu’est-ce donc que le ḥadīṯ fabriqué" in h)

# objectifs ×3
chk("objectif 1 notion du mawḍūʿ", "Que je reconnaisse la notion du ḥadīṯ fabriqué (mawḍūʿ)" in h)
chk("objectif 2 causes de la fabrication", "Que je saisisse les causes portant à la fabrication du ḥadīṯ" in h)
chk("objectif 3 abstention avec exposé de l’état", "sans en exposer l’état" in h)

# glose ×3 définitions
chk("glose muḫtalaq = muftarā + makḏūb", "le fabriqué de toutes pièces (al-muftarā) et le mensonger (al-makḏūb)" in h)
chk("glose maṣnūʿ murādif", "synonyme de l’inventé" in h)
chk("glose mawḍūʿ = waḍʿ/ḥaṭṭa/asqaṭa", "l’abaisse (ḥaṭṭa) et la rejette (asqaṭa)" in h)

# istikhāṣ al-mafāhīm
chk("bandeau istikhāṣ al-mafāhīm", "istikhlāṣu l-mafāhīm" in h)
chk("bandeau muet OCR + image 900 dpi", "mué pour l’OCR automatique" in h or "muet pour l’OCR automatique" in h)
chk("Q1 liminaire « mā l-maqṣūdu bi-l-ḥadīṯi l-mawḍūʿ »",
    "mā l-maqṣūdu bi-l-ḥadīṯi l-mawḍūʿ" in h)
chk("Q2 liminaire causes", "Quelles sont les causes portant à la fabrication du ḥadīṯ" in h)
chk("vue d’ensemble « cette leçon comprend »", "Cette leçon comprend ce qui suit" in h)

# définition : trois termes réunis + mention parmi les anwāʿ
chk("trois termes kaḏib/muḫtalaq/maṣnūʿ", "le mensonge" in h and "l’inventé" in h and "le façonné" in h)
chk("à la suite d’al-ʿIrāqī", "al-ʿIrāqī en sa définition" in h)
chk("insistance à en détourner", "à en détourner" in h)
chk("mention parmi les types, non-ḥadīṯ en réalité", "alors qu’il n’est pas, en réalité, un ḥadīṯ" in h)
chk("par rapport à autre chose que son forgeur", "autre chose que son forgeur" in h)

# divisions selon la matière ×3
chk("division 1 invention de son fonds", "le forgeur invente un propos de son propre fonds" in h)
chk("ḥubbu d-dunyā matn", "ḥubbu d-dunyā raʾsu kulli ḫṭīʾatin" in h)
chk("ḥubbu d-dunyā traduite", "L’amour du bas-monde est la racine de toute faute" in h)
chk("Mālik b. Dīnār / Ibn Abī d-Dunyā", "Mālik b. Dīnār, comme l’a rapporté Ibn Abī d-Dunyā" in h)
chk("ʿĪsā / al-Bayhaqī az-Zuhd", "comme l’a rapporté al-Bayhaqī en az-Zuhd" in h)
chk("Shuʿab al-īmān mursal Ḥasan al-Baṣrī", "des mursal d’al-Ḥasan al-Baṣrī" in h)
chk("Irāqī šabhu r-rīḥ", "šabhu r-rīḥ" in h)
chk("lecture OCR ḥubbu récusée documentée", "récusée par le sens" in h)
chk("division 2 emprunt aux non-prophètes", "emprunte le propos de certains prophètes, sages, médecins" in h)
chk("al-maʿidatu baytu d-dāʾi", "al-maʿidatu baytu d-dāʾi wa-l-ḥimyatu raʾsu d-dawāʾi" in h)
chk("al-maʿidatu traduite", "L’estomac est la maison du mal" in h)
chk("isrāʾīliyyāt", "isrāʾīliyyāt" in h)
chk("division 3 isnād sain composé", "lui compose un isnād sain afin qu’il soit transmis par lui" in h)

# divisions selon le dessein ×2
chk("dessein — deux cas", "se divise en deux cas" in h)
chk("premier cas motivations viles", "pour un but parmi les motivations viles" in h)
chk("second cas inadvertance/erreur", "que par inadvertance et erreur" in h)
chk("Thābit b. Mūsā az-Zāhid", "Thābit b. Mūsā az-Zāhid" in h)
chk("Ibn Māǧah kitāb iqāmat aṣ-ṣalāh", "Sunan d’Ibn Māǧah" in h and "livre de l’établissement de la prière" in h)
chk("matn « man kaṯurat ṣalātuhu bi-l-layli »",
    "man kaṯurat ṣalātuhu bi-l-layli ḥasuna waǧhuhu bi-n-nahār" in h)
chk("matn traduit", "Celui dont la prière nocturne est abondante" in h)
chk("Šurayk b. ʿAbd Allāh", "Šurayk b. ʿAbd Allāh" in h)
chk("isnād l-Aʿmaš ← Abū Sufyān ← Ǧābir", "ḥaddaṯanā l-Aʿmašu ʿan Abī Sufyāna ʿan Ǧābirin qāla" in h)
chk("rappel Ibn Ḥibbān « yaʿhadu š-šayṭānu »",
    "yaʿhadu š-šayṭānu ʿalā qāfiyati raʾsi aḥadikum" in h)
chk("yaʿidu récusation documentée", "yaʿidu » récusée" in hn)
chk("matn traduit chayṭān", "Le diable monte en embuscade sur la nuque" in h)
chk("méprise née de la droiture du cœur", "née de la droiture de son cœur" in h)

# causes du waḍʿ ×4
chk("cause 1 tašakkuk (image 900 dpi)", "tašakkuku n-nāsi fī dīnihim" in h
    and "omise par l’OCR automatique" in h)
chk("cause 1 FR doute des gens", "Le doute des gens en leur religion" in h)
chk("cause 2 ittibāʿ al-hawā", "ittibāʿu l-hawā wa-t-taʿaṣṣubu li-l-maḏāhib" in h)
chk("cause 3 iktisāb/irtizāq/iġtirāb", "al-iktisābu wa-l-irtizāqu awi l-iġtirābu li-qaṣdi l-ištihār" in h)
chk("iġrāb récusé ghayn", "porte le ghayn de l’exil" in h)
chk("cause 4 ġalabat al-ǧahl", "ġalabatu l-ǧahli ka-baʿḍi ġulāti l-mutaʿabbidīna" in h)
chk("cause 4 faḍāʾil as-suwar", "fī faḍāʾili s-suwar" in h)
chk("cause 4 haram bi-iǧmāʿ", "illicite par consensus de ceux qui font autorité" in h)

# khaṭima de la manẓūma
chk("dénomination manẓūmatu l-Bayqūnī", "manẓūmatu l-Bayqūnī" in h)
chk("34 bayt-s", "34" in h)
chk("khaṭima bayt 1", "wa-qad anǧaztu ka-l-ǧawhari l-maknūni" in h
    and "sammaytuhā manẓūmata l-Bayqūnī" in h)
chk("khaṭima bayt 1 traduit", "tel le joyau cacheté" in h)
chk("khaṭima bayt 2", "fawqa ṯ-ṯalāṯīna bi-arbaʿin abātin" in h
    and "aqsāmuhā tammat bi-ḫayri ḫatmī" in h)
chk("bayts pp.135-136", "clôture de la page 135 et en ouverture de la page 136" in h)

# taqwīm ×3
chk("taqwīm badge image", "badge homonyme" in h)
chk("taqwīm q1 définition", "Quelle est la définition du ḥadīṯ fabriqué" in h)
chk("taqwīm q2 divisions matière/dessein", "selon sa matière ; et selon le dessein de son forgeur" in hn)
chk("taqwīm q3 buts portant au waḍʿ", "Quels sont les buts portant à la fabrication en le ḥadīṯ" in h)

# istiṯmār : 2 hadiths
chk("Bukhārī al-Mughīra translit", "inna kaḏiban ʿalayya laysa kakkaḏibin ʿalā aḥadin" in h)
chk("Bukhārī membre médian mutaʿammidan", "man kaḏaba ʿalayya mutaʿammidan fa-l-yatabawwaʾ maqʿadahu mina n-nār" in h)
chk("Bukhārī traduite", "qu’il prenne pour lui-même une place au Feu" in h)
chk("Bukhārī kitāb al-ǧanāʾiz niyāḥa", "livre des funérailles" in h and "pleureuses sur le mort" in h)
chk("membre médian OCR méconnaissable documenté", "l’OCR automatique l’ayant rendu méconnaissable" in h)
chk("Muslim man ḥaddaṯa ʿannī", "man ḥaddaṯa ʿannī bi-ḥadīṯin wa-huwa yarā annahu kaḏibun fa-huwa aḥadu l-kāḏibīn" in h)
chk("Muslim traduite", "du nombre des menteurs" in h)
chk("Muslim Muqaddima aṯ-ṯiqāt", "d’après les dignes de foi et l’abandon des menteurs" in h)
chk("examen à l’aide d’al-Zarqānī", "le commentaire d’al-Zarqānī" in h)
chk("examen q1 jugement du waḍʿ", "Quel est le jugement de la fabrication du ḥadīṯ" in h)
chk("examen q2 périls du mensonge", "les périls du mensonge sur le messager de Dieu" in h)

# bornes
chk("bornes p.133-136", "s’ouvre en la page imprimée 133 et s’achève en la page 136" in h)
chk("section suivante notices p.137", "les notices biographiques des savants) ouvre en la page 137" in h)
chk("double sondage : aucune bannière p.134-138", "aucune bannière de leçon aux pages 134 à 138" in h)
chk("p.137 ornement + Ibn Abī Ḥātim", "Ibn Abī Ḥātim ar-Rāzī" in h and "tr-tmp/r610/t137.txt" in h)
chk("double sondage jamais devinée", "jamais devinée" in h)
chk("chaîne R602→R608, tour R610", "R602→R608" in h and "tour R610" in h)
chk("livraison parallèle R611 documentée", "R611" in h and "PARALLÈLE" in h)
chk("slot sources p.140-143 interdit de double rendu", "interdite de double rendu" in h)

# hygiene FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF]", h))
chk("zéro caractère cyrillique", not re.search(r"[\u0400-\u04FF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("aucune āya rendue (assertion méta présente)", "āya n’est mobilisée" in h)
chk("balises appariées", h.count("<ol>") == h.count("</ol>")
    and h.count("<li>") == h.count("</li>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>"))

# registre : htmlFr posé, voisins intacts, pas de doublon parallèle
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre 136 intact (20 967 car)", 20_000 <= len(les["pdf-mut23h2r-136"].get("htmlFr") or "") <= 21_500)
chk("registre 137 intact (15 268 car)", 14_800 <= len(les["pdf-mut23h2r-137"].get("htmlFr") or "") <= 15_700)
chk("registre 138 intact (17 739 car)", 17_000 <= len(les["pdf-mut23h2r-138"].get("htmlFr") or "") <= 18_200)
chk("registre 140 = notices R611 intact (>15 000 car)",
    len(les["pdf-mut23h2r-140"].get("htmlFr") or "") > 15_000)
chk("registre 141 sources toujours vide", not (les["pdf-mut23h2r-141"].get("htmlFr") or "").strip())
fr = les["pdf-mut23h2r-139"].get("htmlFr") or ""
chk("registre 139 = htmlFr posé", len(fr) > 15_000 and (
    fr.strip() == h.strip() or abs(len(fr) - len(h.rstrip("\n"))) <= 40))

print(f"verify-ulumhadith1-pdf139 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
