#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 738 (tafsir-5ep,
les sources et références — al-maṣādir wa-l-marāǧiʿ, pages 214-220).
La bibliographie ne cite AUCUN āya : contrôle d'ABSENCE des rasm coraniques
du volume (āyāt 105-111 des trois dernières leçons et lemmes d'appui connus)
au corps — toute citation coranique y serait une incursion hors matière ;
contrôle de contenu : les vingt-six références tranchées par l'imprimé
(titres, auteurs, dates hégiriennes ré-inversées concordantes avec
l'historiographie, éditions), le sommaire des vingt-huit plages de versets
tranché par les titres du livre, la structure (deux tables à deux colonnes,
Source du cours), 0 arabe résiduel (ﷺ exempté — convention du corpus)."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-738.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure : deux tables à deux colonnes (26 références + 28 plages)
if "<thead><tr><th>Le rang</th><th>La source et la référence</th></tr></thead>" not in norm:
    errors.append("en-tête du tableau des références absent")
if "<thead><tr><th>La leçon</th><th>Les versets de sūrat al-Isrāʾ</th></tr></thead>" not in norm:
    errors.append("en-tête du tableau du sommaire absent")
n_rows = len(re.findall(r"<tr><td>", norm))
if n_rows != 54:
    errors.append(f"rangées attendues : 54 (26 références + 28 plages), trouvées : {n_rows}")
if "Source du cours" not in norm:
    errors.append("Source du cours absent du DOM")
for frag in [
    "pages 214 à 220 de l’imprimé miroir",
    "la page imprimée 214 ouvre déjà la rubrique",
    "PAR L’IMPRIMÉ, jamais devinées",
    "les pages 214 à 218 rendues en image (150 DPI)",
    "Le sommaire de la page 219",
    "la page 220, blanche, closant l’imprimé",
    "toutes concordantes avec l’historiographie établie",
]:
    if frag not in norm:
        errors.append(f"source du cours : fragment attendu absent : {frag[:55]}")

# 2. les vingt-six références tranchées par l'imprimé
refs = [
    ("« Le Coran karīm »", ["Fondation Muḥammad as-Sādis", "l’édition troisième, 2012", "lecture de Warš d’après Nāfiʿ"]),
    ("« Aḥkām al-Qurʾān »", ["al-Maʿāfirī al-Išbīlī al-Mālikī", "m. 543 h", "Dār al-Kutub al-ʿIlmiyya", "1424 h — 2003 de l’ère chrétienne"]),
    ("« al-Aʿlām »", ["az-Ziriklī ad-Dimašqī", "m. 1396 h", "Dār al-ʿIlm li-l-Malāyīn", "l’édition quinzième, 2002 de l’ère chrétienne"]),
    ("« al-Baḥr al-muḥīṭ fī t-tafsīr »", ["Aṯīr ad-Dīn al-Andalusī", "m. 745 h", "Ṣidqī Muḥammad Ǧamīl", "Dār al-Fikr", "l’édition 1420 h"]),
    ("« al-Baḥr al-madīd fī tafsīr al-Qurʾān al-maǧīd »", ["b. ʿAǧība", "m. 1224 h", "Aḥmad ʿAbd Allāh al-Qurašī", "Rāslān", "l’édition 1419 h"]),
    ("« at-Taḥrīr wa-t-Tanwīr »", ["b. ʿĀšūr at-Tūnisī", "m. 1393 h", "ad-Dār at-Tūnisiyya li-n-našr", "Tunis, 1984 h"]),
    ("« at-Tas-hīl li-ʿulūm at-tanzīl »", ["Ibn Ǧuzayy al-Kalbī al-Ġarnāṭī", "m. 741 h", "ʿAbd Allāh al-Ḫaladī", "Dār al-Arqam b. Abī l-Arqam", "1416 h"]),
    ("« Tafsīr al-Qurʾān al-ʿaẓīm »", ["Ismāʿīl b. ʿUmar b. Kaṯīr", "m. 774 h", "Sāmī b. Muḥammad Salāma", "Dār Ṭayba", "1420 h — 1999 de l’ère chrétienne"]),
    ("Ibn Abī Ḥātim", ["b. Idrīs b. al-Mundir", "m. 327 h", "Asʿad Muḥammad aṭ-Ṭayyib", "Maktabat Niẓār Muṣṭafā al-Bāz", "l’édition troisième, 1419 h"]),
    ("« Ǧāmiʿ al-bayān fī taʾwīl āy al-Qurʾān »", ["al-Āmulī", "m. 310 h", "Aḥmad Muḥammad Šākir", "Muʾassasat ar-Risāla", "1420 h — 2000 de l’ère chrétienne"]),
    ("« Ṣaḥīḥ al-Buḫārī »", ["al-Buḫārī al-Ǧaʿfī", "m. 256 h", "Muḥammad Zuhayr b. Nāṣir an-Nāṣir", "Dār Ṭawq an-Naǧāt", "1422 h", "ﷺ"]),
    ("« al-Ǧāmiʿ li-aḥkām al-Qurʾān", ["Šams ad-Dīn al-Qurṭubī", "m. 671 h", "Aḥmad al-Bardūnī et Ibrāhīm Aṭfīš", "Dār al-Kutub al-Miṣriyya", "l’édition : deuxième, 1384 h"]),
    ("« Rūḥ al-maʿānī", ["al-Ālūsī", "m. 1270 h", "ʿAlī ʿAbd al-Bārī ʿAṭiyya", "l’édition première, 1415 h"]),
    ("« Sunan Ibn Māǧa »", ["al-Qazwīnī", "grand-père Māǧa", "m. 273 h", "Muḥammad Fuʾād ʿAbd al-Bāqī", "Fayṣal ʿĪsā al-Bābī al-Ḥalabī"]),
    ("« Sunan Abī Dāwūd »", ["as-Siǧistānī", "m. 275 h", "Šuʿayb al-Arnaʾūṭ", "Dār ar-Risāla al-ʿĀlamiyya", "1430 h — 2009 de l’ère chrétienne"]),
    ("« Sunan at-Tarmiḏī »", ["Abū ʿĪsā", "m. 279 h", "Ibrāhīm ʿAṭwa ʿAwaḍ", "al-Bābī al-Ḥalabī", "l’édition : deuxième, 1395 h"]),
    ("« as-Sīra an-nabawiyya »", ["Ibn Hišām", "al-Ḥimyarī al-Maʿāfirī", "m. 213 h", "1375 h — 1955 de l’ère chrétienne"]),
    ("« Šuʿab al-Īmān »", ["al-Bayhaqī", "m. 458 h", "ʿAbd al-ʿAlī ʿAbd al-Ḥamīd Ḥāmid", "Maktabat ar-Rušd", "1423 h — 2003 de l’ère chrétienne"]),
    ("« Ṣafwat at-Tafāsīr »", ["aṣ-Ṣābūnī", "Dār aṣ-Ṣābūnī", "l’édition première, 1417 h"]),
    ("« al-Kaššāf ʿan ḥaqāʾiq ġawāmiḍ at-tanzīl »", ["az-Zamaḫšarī", "Ǧār Allāh", "m. 538 h", "Dār al-Kutub al-ʿArabī", "l’édition : troisième, 1407 h"]),
    ("« al-Muḥarrar al-waǧīz fī tafsīr al-Kitāb al-ʿAzīz »", ["b. Tammām b. ʿAṭiyya al-Andalusī al-Muḥārabī", "m. 542 h", "ʿAbd as-Salām ʿAbd aš-Šāfī Muḥammad", "l’édition : première — 1422 h"]),
    ("« al-Musnad aṣ-Ṣaḥīḥ al-Muḫtaṣar bi-naql al-ʿadl ʿan al-ʿadl ilā rasūl Allāh ﷺ »", ["Muslim b. al-Ḥaǧǧāǧ", "m. 261 h", "Muḥammad Fuʾād ʿAbd al-Bāqī", "Dār Iḥyāʾ at-Turāṯ al-ʿArabī"]),
    ("« al-Muʿǧam al-Awsaṭ »", ["aṭ-Ṭabarānī", "m. 360 h", "Ṭāriq b. ʿAwaḍ Allāh b. Muḥammad", "Dār al-Ḥaramayn"]),
    ("« Mafātīḥ al-Ġayb »", ["at-Tafsīr al-kabīr", "Fakhr ad-Dīn ar-Rāzī", "Ibn al-Ḫaṭīb ar-Rayy", "m. 606 h", "l’édition troisième — 1420 h"]),
    ("« al-Muwāfaqāt fī uṣūl aš-šarīʿa »", ["aš-Šāṭibī", "m. l’an 790 h", "Mašhūr b. Ḥasan Āl Salmān", "Dār Ibn ʿAfān", "1417 h — 1997 de l’ère chrétienne"]),
    ("« al-Muwaṭṭaʾ »", ["Mālik b. Anas b. Mālik b. Abī ʿĀmir", "al-Aṣbaḥī al-Madanī", "m. 179 h", "ruqma", "1406 h — 1985 de l’ère chrétienne"]),
]
for titre, frs in refs:
    if titre not in norm:
        errors.append(f"référence absente : {titre[:55]}")
    for f in frs:
        if f not in norm:
            errors.append(f"référence {titre[:35]} : fragment attendu absent : {f[:50]}")

# 3. le sommaire des vingt-huit plages (tranché par les titres du livre)
for plage in ["le verset 1", "2-4", "49-55", "56-60", "99-100", "101-104", "105-108", "109-110"]:
    if f"<td>{plage}</td>" not in norm:
        errors.append(f"plage du sommaire absente : {plage}")

# 4. ABSENCE de citations coraniques (la bibliographie n'en porte aucune) —
#    rasm nu du cache des āyāt récentes du volume + lemmes d'appui connus
def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
probes = []
for v in (105, 106, 107, 108, 110, 111):
    t = bare(ar17[v]).split()
    probes.append(" ".join(t[len(t) // 2:len(t) // 2 + 3]))
for f in ["حجابا مستورا", "وسل من أرسلنا من قبلك من رسلنا", "تسع ءايت بينت"]:
    probes.append(f)
for p in probes:
    if p and p in norm:
        errors.append(f"rasm coranique inattendu au corps de la bibliographie : {p[:40]}")

# rendus français caractéristiques des āyāt — absence attendue
for pat, label in [
    (r"en toute vérité que Nous l’avons fait descendre", "al-Isrāʾ 17:105"),
    (r"le menton contre terre", "al-Isrāʾ 17:107"),
    (r"Gloire à notre Seigneur", "al-Isrāʾ 17:108"),
    (r"Invoquez donc Allah, ou invoquez le Tout Miséricordieux", "al-Isrāʾ 17:110"),
    (r"dans ta prière, et ne la fais pas lourdement", "al-Isrāʾ 17:110"),
    (r"Dis : Louange à Allah", "al-Isrāʾ 17:111"),
]:
    if re.search(pat, norm, re.IGNORECASE):
        errors.append(f"rendu coranique inattendu : {label}")

# 5. 0 arabe résiduel (ﷺ U+FDFA exempté — convention du corpus)
if re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", norm):
    errors.append("caractère arabe résiduel détecté")

if errors:
    print("ÉCHEC :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS : leçon 738 — sources et références (p.214-220) — les vingt-six références "
      "tranchées par l'imprimé (Coran Warš 2012 ; Aḥkām 543/1424h-2003 ; al-Aʿlām 1396/2002m ; "
      "Baḥr al-muḥīṭ 745/1420h ; Baḥr al-madīd 1224/1419h Rāslān ; Taḥrīr 1393/1984h ; "
      "Tas-hīl 741/1416h ; Ibn Kaṯīr 774/1420h-1999 ; Ibn Abī Ḥātim 327/1419h ; Ṭabarī 310/1420h-2000 ; "
      "Buḫārī 256/1422h ; Qurṭubī 671/1384h ; Rūḥ al-maʿānī 1270/1415h ; Ibn Māǧa 273 ; "
      "Abū Dāwūd 275/1430h-2009 ; Tirmiḏī 279/1395h ; Sīra Ibn Hišām 213/1375h-1955 ; "
      "Šuʿab al-Īmān 458/1423h-2003 ; Ṣafwat at-Tafāsīr 1417h ; Kaššāf 538/1407h ; "
      "Muḥarrar 542/1422h ; Muslim 261 ; Muʿǧam al-Awsaṭ 360 ; Mafātīḥ al-ġayb 606/1420h ; "
      "Muwāfaqāt 790/1417h-1997 ; Muwaṭṭaʾ 179/1406h-1985) et leurs éditions portées, "
      "sommaire des vingt-huit plages (1 ; 2-4 … 99-100 … 105-108 ; 109-110) au DOM, "
      "deux tables à deux colonnes et Source du cours au DOM, aucune citation coranique "
      "au corps (ABSENCE des rasm des āyāt 105-111 et des lemmes d'appui vérifiée), "
      "0 arabe résiduel.")

if __name__ == "__main__":
    sys.exit(0)
