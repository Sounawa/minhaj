#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-135
(les transmetteurs homographes muttafiq/muftariq, p.117-120 du manuel
ulum-hadith-1-thanawi.pdf) : bannière « ad-dars 24 » ; bornes p.117-120 par
DOUBLE sondage (bannière ad-dars 25 + objectifs المؤتلف والمختلف lus à l'OCR
p.121, concordants avec l'iʿdād qablī p.120 ×3 questions) ; bayt — « muttafiqun
lafẓan wa-khaṭṭan muttafiqun * * * wa-ḍidduhu fīmā takarranā l-muftaraqu »
tranché image 2400 dpi (tāʾ à deux points + šadda sur le rāʾ ; OCR « ḏakarnā »
récusé) ; glose (ittifāq/iḫtilāf) ; istiḫlāṣ al-mafāhīm ×2 ; taḥlīl : définition
(ittifāq lafẓan wa-khaṭṭan, ḫtilāf fī š-šakhṣ, muštarak lafẓī des usulistes,
al-ʿIrāqī diacrité, ex. al-ʿayn, condition de deux transmetteurs, exclusion
ḥabān/ḥayyān/ǧayyān tranchée 2400 dpi šadda sur les yāʾ) ; huit formes (I
al-Ḫalīl ibn Aḥmad six ; II Aḥmad ibn Ǧaʿfar ibn Ḥamdān quatre — forme entière
adjudiquée 600 dpi ; III Abū ʿImrān al-Ǧūnī deux / Abū ʿAmr al-Ḥawḍī deux aussi
— aṯnān ayḍan 2400 dpi ; IV Muḥammad ibn ʿAbdallāh al-Anṣārī ; V Abū Bakr ibn
ʿAyyāš trois ; VI Ṣāliḥ ibn Abī Ṣāliḥ quatre des Successeurs ; VII ʿAbdallāh —
Mecque/Médine/Kūfa/Basra/Ḫurāsān + ex. kunya Abū Ḥumza, Šuʿba → Naṣr ibn ʿUmrān
aḍ-Ḍabbaʿī « bi-ǧīm warāʾ » tenu tel qu'imprimé 300/2400 dpi ; VIII nisba —
aṣ-Ṣanʿānī Yémen/Ṣanʿāʾ de Damas en Šām — continuation 2400 dpi — et al-Ḥanafī
tribu/école, yāʾ inférieur) ; taqwīm ×2 ; istiṯmār Ibn Daqīq al-ʿĪd « fa-yuʿtaqad
aḥadu š-šaḫṣayni » tranché 4800 dpi (OCR « fa-yuttafaq » récusé ; source
canonique al-Iqtirāḥ p. 50 concordante, deux sources en ligne documentées ;
réf. imprimée [al-Iqtirāḥ fī maʿrifat al-iṣṭilāḥ : 51/1] tenue telle
qu'imprimée) ; iʿdād qablī ×3 (Q2 découverte image 600 dpi, mutaḥalif/muḫtalif) ;
bornes p.117-120 ; zéro āya rendue, zéro résidu.
Usage: python3 scripts-translate/verify-ulumhadith1-pdf135.py
"""
import json
import re
import sys

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-135-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-1.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")


h = open(HTML, encoding="utf-8").read()
plain = re.sub(r"[\s\u202f\u00a0]+", " ", h.replace("&nbsp;", " "))

# 1. h1 aligné au titleFr pré-mappé du registre
tf = [l for l in json.load(open(REG, encoding="utf-8"))["lessons"]
      if l["docId"] == "pdf-mut23h2q-135"][0]["titleFr"]
m = re.match(r"<h1>(.*?)</h1>", h, re.S)
chk("h1 présent", bool(m))
chk("h1 aligné titleFr registre", m and m.group(1).replace("&nbsp;", " ").startswith(tf))
chk("h1 leçon 24", "leçon 24" in (m.group(1) if m else ""))

# 2. bannière / bornes
chk("badge ad-dars 24", "ad-dars 24" in plain)
chk("bornes p.117-120 documentées", "page imprimée 117" in plain and "page 120" in plain)
chk("bannière ad-dars 25 p.121 (sondage)", "ad-dars 25" in plain and "page 121" in plain)
chk("double sondage (jamais deviné)", "DOUBLE sondage" in plain)
chk("jamais devinée", "jamais devinée" in plain)
chk("concordance iʿdād qablī p.120", "concordants" in plain)
chk("zéro inversion numéro", "zéro inversion" in plain)

# 3. tamhīd
chk("tamhīd : connaissance complète du transmetteur", "connaissance complète du transmetteur" in plain)
chk("tamhīd : ʿadāla/ḍabṭ/sûreté", "intégrité (ʿadāla), sa maîtrise (ḍabṭ)" in plain)
chk("tamhīd : accepté/rejeté", "l’accepté ou le rejeté" in plain)
chk("tamhīd : confusion par ressemblance", "ressemblance de leurs noms" in plain)
chk("tamhīd question double", "Quel est donc le sens du muttafiq et du muftariq" in plain)

# 4. bayt
chk("bayt : muttafiqun lafẓan wa-khaṭṭan muttafiqun", "muttafiqun lafẓan wa-khaṭṭan muttafiqun" in plain)
chk("bayt : wa-ḍidduhu fīmā takarranā l-muftaraqu", "wa-ḍidduhu fīmā takarranā l-muftaraqu" in plain)
chk("takarranā tranché 2400 dpi (tāʾ+šadda)", "takarranā" in plain and "2400 dpi" in plain)
chk("OCR ḏakarnā récusé (image)", "ḏakarnā" in plain and "récusé" in plain)
chk("bayt rendu deux fois (matn + taʿrīf)", "conforme au matn p.117" in plain)
chk("traduction bayt", "son contraire, en ce que nous avons répété, est le muftariq" in plain)

# 5. glose
chk("glose : ittifāq/iḫtilāf", "de l’accord (al-ittifāq), le contraire de la divergence" in plain)
chk("glose : muftariq le différent", "Al-muftariq&nbsp;: le différent" in plain or "Al-muftariq : le différent" in plain)

# 6. extraction des thèmes ×2
chk("deux questions-limaires p.118", "deux questions-limaires" in plain)
chk("rubrique istiḫlāṣ al-mafāhīm", "istiḫlāṣ al-mafāhīm" in plain)
chk("IS1 maqṣūd", "visé par « le muttafiq et le muftariq » parmi les transmetteurs" in plain)
chk("IS2 ṣuwar", "formes de l’accord et de la divergence dans les noms" in plain)

# 7. taḥlīl — définition
chk("isnād réunit deux transmetteurs ou davantage", "réunit deux transmetteurs ou davantage" in plain)
chk("nom/kunya/père-aïeul/nisba", "ou le nom avec la kunya, ou le nom du père et de l’aïeul, ou la nisba" in plain)
chk("diffèrent en la personne", "diffèrent en la personne" in plain)
chk("muštarak lafẓī des usulistes", "al-muštarak al-lafẓī) chez les usulistes" in plain)
chk("al-ʿIrāqī cité", "Al-Ḥāfiẓ al-ʿIrāqī dit" in plain)
chk("lafẓuhū/khaṭṭuhū/musmayāt", "tandis que les désignations (musmayāt) diffèrent" in plain)
chk("ex. al-ʿayn", "l’exemple de la lexie « al-ʿayn »" in plain)
chk("œil/or-argent/source", "l’œil qui frappe (l’œil du mal), ou l’or et l’argent, ou la source d’eau" in plain)
chk("condition deux transmetteurs", "qu’un transmetteur unique, il n’entre point dans le muttafiq et le muftariq" in plain)
chk("exclusion ḥabān/ḥayyān/ǧayyān", "« ḥabān », « ḥayyān » et « ǧayyān »" in plain)
chk("šadda sur les yāʾ tranchée 2400 dpi", "šadda nette sur les deux yāʾ" in plain)
chk("OCR ḥibān récusé", "ḥibān/ḥibān/ǧiyān" in plain and "récusé" in plain)
chk("relève du mutaḥalif et muḫtalif", "du mutaḥalif et du muḫtalif (al-muʾtalif wa-l-muḫtalif) qui viendra" in plain)

# 8. huit formes
chk("ṣuwar en-tête rouge", "ṣuwar al-ittifāq wa-l-iḫtilāf bayna r-ruwāh" in plain)
chk("I al-Ḫalīl ibn Aḥmad six", "al-Ḫalīl ibn Aḥmad — six hommes ou davantage" in plain)
chk("II Aḥmad ibn Ǧaʿfar ibn Ḥamdān quatre", "Aḥmad ibn Ǧaʿfar ibn Ḥamdān, quatre" in plain)
chk("II forme entière 600 dpi", "forme entière adjudiquée PAR L’IMAGE à 600 dpi" in plain)
chk("III Abū ʿImrān al-Ǧūnī deux", "Abū ʿImrān al-Ǧūnī, deux hommes" in plain)
chk("III Abū ʿAmr al-Ḥawḍī aṯnān ayḍan", "Abū ʿAmr al-Ḥawḍī, deux aussi" in plain and "aṯnān ayḍan" in plain)
chk("III points yāʾ effacés", "points du yāʾ effacés à l’impression" in plain)
chk("IV Muḥammad ibn ʿAbdallāh al-Anṣārī", "Muḥammad ibn ʿAbdallāh al-Anṣārī, deux proches en génération" in plain)
chk("V Abū Bakr ibn ʿAyyāš trois", "Abū Bakr ibn ʿAyyāš" in plain and "bi-taḥtīya wa-muʿǧama" in plain)
chk("VI Ṣāliḥ ibn Abī Ṣāliḥ quatre", "Ṣāliḥ ibn Abī Ṣāliḥ, quatre des Successeurs" in plain)
chk("VII ʿAbdallāh Mecque/Médine/Kūfa/Basra/Ḫurāsān", "Ibn az-Zubayr" in plain and "Ibn Masʿūd" in plain and "Ibn al-Mubārak" in plain)
chk("ex. kunya Abū Ḥumza", "« Abū Ḥumza »" in plain)
chk("Šuʿba → Naṣr ibn ʿUmrān aḍ-Ḍabbaʿī", "Naṣr ibn ʿUmrān aḍ-Ḍabbaʿī" in plain)
chk("bi-ǧīm warāʾ tenu tel qu'imprimé", "wa-huwa bi-ǧīm warāʾ" in plain and "non interpolée" in plain)
chk("six avec ḥāʾ et zāy", "narre d’eux tous avec ḥāʾ et zāy" in plain)
chk("VIII aṣ-Ṣanʿānī Yémen", "Ṣanʿāʾ du Yémen — la plus célèbre" in plain)
chk("VIII Ṣanʿāʾ Damas Šām (continuation 2400 dpi)", "localité de Damas en Šām" in plain and "2400 dpi" in plain)
chk("VIII al-Ḥanafī tribu/école", "tribu de Banū Ḥanīfa" in plain and "al-maḏhab al-fiqhī" in plain)
chk("VIII yāʾ inférieur", "un yāʾ inférieur" in plain)

# 9. taqwīm — 2 questions
chk("taqwīm 2 questions", "sous la forme de deux questions" in plain)
chk("TQ1 définition", "Quelle est la définition du muttafiq et du muftariq" in plain)
chk("TQ2 trois formes", "Cite trois formes" in plain)

# 10. istiṯmār — Ibn Daqīq al-ʿĪd
chk("Ibn Daqīq al-ʿĪd cité", "Ibn Daqīq al-ʿĪd dit" in plain)
chk("fa-yuʿtaqad tranché 4800 dpi", "fa-yuʿtaqad" in plain and "4800 dpi" in plain)
chk("glyphes f-y-ʿ-t-q-d", "glyphes fāʾ-yāʾ-ʿayn-tāʾ-qāf-dāl" in plain)
chk("OCR fa-yuttafaq récusé", "fa-yuttafaq" in plain and "récusé" in plain)
chk("aḥadu š-šaḫṣayni huwa l-āḫaru", "fa-yuʿtaqad aḥadu š-šaḫṣayni huwa l-āḫaru" in plain)
chk("ṯiqatan/ḍaʿīfan", "ṯiqatan wa-l-āḫara ḍaʿīfan" in plain)
chk("saḥḥa mā lā yaṣiḥḥu", "saḥḥa mā lā yaṣiḥḥu" in plain)
chk("abṭala mā yaṣiḥḥu", "abṭala mā yaṣiḥḥu" in plain)
chk("réf. al-Iqtirāḥ 51/1 imprimée", "al-Iqtirāḥ fī maʿrifat al-iṣṭilāḥ&nbsp;: 51/1" in plain or "al-Iqtirāḥ fī maʿrifat al-iṣṭilāḥ : 51/1" in plain)
chk("source canonique p. 50 concordante", "al-Iqtirāḥ fī bayān al-iṣṭilāḥ d’Ibn Daqīq al-ʿĪd, p. 50" in plain)
chk("consigne activité", "J’examine le texte et j’explicite l’utilité et les effets" in plain)

# 11. iʿdād qablī — leçon suivante mutaḥalif/muḫtalif ×3
chk("préparation mutaḥalif/muḫtalif ×3", "quel est le sens du mutaḥalif et du muḫtalif" in plain and "importance de sa connaissance" in plain and "divisions" in plain)
chk("Q2 découverte image 600 dpi", "DÉCOUVERTE PAR L’IMAGE 600 dpi" in plain or "découverte par l’image 600 dpi" in plain)
chk("leçon suivante interdite de double rendu", "interdite de double rendu" in plain)

# 12. zéro āya rendue, zéro résidu
chk("doc mentionne aucune āya rendue", "aucune āya rendue" in plain)
residus = ["TODO", "XXX", "undefined", "NaN", "【", "____", "recycle", "takeover", "mtime", "⟨AR⟩"]
chk("zéro résidu technique", not any(r in plain for r in residus))

print(f"\n{ok}/{ok + fail} PASS" + ("" if fail == 0 else f" — {fail} ÉCHEC(S)"))
sys.exit(1 if fail else 0)
