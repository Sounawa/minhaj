# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-414
(les conditions de l'aḍḥiyya et le statut de l'association — شروط الأضحية
وحكم الشركة فيها, leçon 25 imprimée, p.164-169 du manuel
hadith-3-iadadi_text.pdf, 196 p.)
Usage: python3 scripts-translate/verify-hadith3-pdf414.py
"""
import json, re, sys, os

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-414-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
CLAIM = "/home/z/my-project/tr-tmp/claims/hadith3-pdf-mut23h2x-414.claim.json"

ok, fail = 0, 0

def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC : {label}")

html = open(HTML, encoding="utf-8").read()
text = re.sub(r'<[^>]+>', '', html)  # texte épuré des balises (contrôles de matière)

# 0. garde-doublon registre
book = json.load(open(REG))
lesson = next((l for l in book["lessons"] if l["docId"] == "pdf-mut23h2x-414"), None)
chk("docId pdf-mut23h2x-414 présent au registre", lesson is not None)
if lesson:
    chk("htmlFr vide AVANT pose (garde-doublon)", not (lesson.get("htmlFr") or "").strip())

# 1. claim actif
chk("claim présent", os.path.exists(CLAIM))

# 2. longueur
chk(f"longueur >= 40 000 car (réel : {len(html)})", len(html) >= 40000)

# 3. sections obligatoires (12 H2)
for s in ["Les objectifs du cours", "Le <em>tamhīd</em>", "Les textes du cours",
          "La notice du transmetteur", "La glose des mots", "Le résumé du cours",
          "Le fiqh du hadith", "L’évaluation du cours", "L’exploitation du cours",
          "La préparation préalable", "L’apparat de preuve"]:
    chk(f"section présente : {s}", s in html)

# 4. trois textes + sections fiqh
for t in ["Premier texte", "Deuxième texte", "Troisième texte",
          "Premièrement&nbsp;", "Deuxièmement&nbsp;",
          "L’atteinte de l’âge requis", "La perfection de sa formation"]:
    chk(f"texte/section : {t}", t in html)

# 5. numéros du Muwaṭṭa' (9 occurrences, dont 1362 double)
for n in ["1352", "1353", "1360", "1361", "1362", "1363", "1366", "1358"]:
    chk(f"numéro : n° {n}", n in html)
chk("double étiquette 1362 consignée (R511)", "DEUX fois" in text)

# 6. matière adjudiquée
for key in ["que se garde-t-on dans les bêtes d’offrande",
            "ma main est plus courte que la main du Messager",
            "la boiteuse à claudication manifeste",
            "l’aveugle à l’aveuglement manifeste",
            "la malade au mal manifeste",
            "la maigre que l’on ne peut dégraisser",
            "le plus aimable de ce que j’ai entendu",
            "nous avons immolé avec le Messager d’Allah",
            "l’an de al-ḥudaybiya",
            "le chameau pour sept, et la vache pour sept",
            "compagnon d’un compagnon",
            "s’est présenté au jour de Badr",
            "quinze expéditions",
            "une sourate de al-mufaṣṣal",
            "mort l’an 72",
            "sa claudication",
            "féminin de aʿǧaf",
            "le naqā est la graisse",
            "que je cite les vices qui ne sont pas licites",
            "le statut de l’association dans l’aḍḥiyya",
            "l’âge requis dans l’aḍḥiyya",
            "sa salubrité des vices",
            "ne peut suivre les moutons dans leur marche",
            "elle est alors admise",
            "le mal épuise son corps",
            "ni graisse dans sa chair ni moelle dans ses os",
            "à plus forte raison",
            "le Messager d’Allah ﷺ nous a ordonné d’examiner l’œil",
            "la mudābara celle dont un bout latéral de l’oreille est tranché",
            "celle à l’oreille fendue",
            "celle à l’oreille percée",
            "une chaîne belle",
            "du mouton, de la chèvre, de la vache et du chameau",
            "même d’un jour",
            "d’une entrée manifeste, comme un mois",
            "trois années avec son entrée dans la quatrième",
            "cinq années avec son entrée dans la sixième",
            "la perfection de la formation",
            "diminue son prix et sa graisse",
            "la licéité de la ǧamāʾ",
            "les dons obligatoires",
            "le cadi abū al-ḥasan",
            "l’association dans la récompense",
            "on tire au sort à chacun d’eux une part de son prix",
            "cela est blâmé",
            "les gens d’une seule maison",
            "fussent-ils plus de sept",
            "l’homme l’immolait pour lui et pour les gens de sa maison",
            "le plus parfait de ce que j’ai entendu",
            "c’est lui qui le possède",
            "n’a immolé pour lui et pour les gens de sa maison qu’un seul chameau",
            "ce qui est dans le ventre de la femme",
            "comme dans al-mudawwana",
            "deux personnes se sont associées dans l’achat d’une vache",
            "un veau ayant deux ans",
            "l’aveugle tout court et celle dont la jambe est tranchée",
            "mettez en réserve pour trois",
            "les gens profitaient de leurs bêtes d’offrande",
            "des outres de traite",
            "mangez, donnez en aumône et mettez en réserve",
            "arrivé à la Médine",
            "le concept de la nabīḏ",
            "le statut de l’ʿaqīqa et ses recommandés",
            "chourūṭ al-aḍḥiyya wa-ḥukm ach-chirkah fīhā",
            "ẓalʿuhā", "al-ʿawrāʾ", "al-ʿaǧafāʾ", "lā tanqī"]:
    chk(f"matière : {key[:44]}", key in text)

# 7. notices et autorités
for key in ["abū dāwūd", "an-nesāʾī", "ʿalī", "al-barāʾ", "jābir",
            "abū z-zubayr al-makkī", "abū ayyūb al-ʾanṣārī", "ibn chihāb",
            "Nāfi’", "ʿabd Allāh b. ʿumar", "Yaḥyā", "al-ǧumhūr",
            "al-mudawwana", "ḥasan al-ʾisnād"]:
    chk(f"notice/autorité : {key[:44]}", key in text)

# 8. arabe du tirage (dans les spans, texte épuré)
for key in ["سُئِلَ: مَاذَا يُتَّقَى مِنَ الضَّحَايَا",
            "الْعَرْجَاءُ الْبَيِّنُ ظَلْعُهَا",
            "وَالْعَوْرَاءُ الْبَيِّنُ عَوْرُهَا",
            "وَالْمَرِيضَةُ الْبَيِّنُ مَرَضُهَا",
            "وَالْعَجْفَاءُ الَّتِي لَا تُنْقَى",
            "لَمْ تُسَنَّ",
            "وَالَّتِي نُقِصَ مِنْ خَلْقِهَا",
            "نَحَرْنَا مَعَ رَسُولِ اللهِ",
            "عَامَ الْحُدَيْبِيَّةِ الْبُدْنَةَ عَنْ سَبْعَة",
            "فَيُقْرَعُ",
            "لا يُشْتَرَك في النُّسُك",
            "كُنّا نَضَحِّي بالشّاة الواحدة",
            "بُدْنَةً وَاحِدَةً أو بَقَرَةً وَاحِدَةً",
            "لَمْ يَكُنْ يَضَحِّي عَمّا في بَطْنِ المرأة",
            "اَدَّخِرُوا لَثَلاثٍ",
            "الدَّافَةِ الَّتي دَفَّتْ عليْكم",
            "مَاذَا يُتَّقَى",
            "أَرْبَعٌ",
            "بِمُقاطَعَةٍ",
            "حَرْقاءَ",
            "شروط الأضحية وحكم الشركة فيها",
            "النبيذة"]:
    chk(f"arabe du tirage : {key[:36]}", key in text)

# 9. variantes consignées (matn 1358 : dagr du tirage) et récusées
chk("variante wijmaʿlūna consignée (tirage mīm)", "ويَجْمَلون" in text)
chk("variante raddafat de Muslim consignée dans l’apparat", "رَدَّفَتْ" in text)
chk("variante ḫarqāʾ consignée dans l’apparat", "خَرْقاء" in text)
chk("variante ʿadabara consignée", "مُدَبَرَة" in text)
chk("matn 1363 sans بدمة (بدنة du tirage)", "بِدَمَة" not in text)
chk("doctrine R511 consignée", "doctrine R511" in text)
chk("grandes lignes de la méthode (couches en repère)", "jamais pour autorité" in text)

# 10. arabe uniquement dans spans RTL
body_no_spans = re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', html)
m = re.findall(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]', body_no_spans)
chk(f"0 arabe hors spans RTL (réel : {len(m)})", len(m) == 0)

# 11. pas de placeholders
for bad in ["XXX", "TODO", "à compléter", "【", "TBD", "immoration", "certillance", "la intention"]:
    chk(f"pas de placeholder/typo : {bad!r}", bad not in html)

# 12. bornes de pages consignées
for p in ["p.164", "p.169", "p.164-169", "vingt-quatrième slot"]:
    chk(f"borne : {p}", p in html)

print(f"\n{ok} contrôles OK, {fail} échecs")
sys.exit(1 if fail else 0)
