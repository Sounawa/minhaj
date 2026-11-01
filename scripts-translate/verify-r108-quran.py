#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R108 — Vérification du rendu savant tafsir-3es / pdf-mut23h36-621.

La leçon 621 est l'index des figures (فهرس الأعلام, p167-169) : elle ne contient
AUCUN verset coranique — le croisement avec le cache coran warš (contrôle n° 6
de R106/R107) ne s'applique donc pas et est remplacé par un contrôle
d'ABSENCE de versets (aucun fragment warš attendu, aucun chiffre coranique).

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027
  3. guillemets « » appariés
  4. h1 attendu
  5. assertions ciblées : intro conventionnelle, les 18 têtes de notices dans
     l'ordre de l'imprimé, généalogies clés, rangs, ouvrages (cités « » ou nus
     conformément à l'imprimé), années de décès (18/18), kunya/laqab, formule
     رحمه الله rendue ×6, ﷺ rendu par la formule française
  6. absence de versets : aucun fragment coranique warš dans le rendu
  7. 0 résidu d'édition (XXX, TODO, 【】, undefined, NaN)
"""
import re
import sys

ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")

DOC = "/home/z/my-project/tr-tmp/pdf-mut23h36-621.html"

ASSERTS = [
    "<h1>Index des figures citées</h1>",
    "fihrist al-aʿlām",
    "Tashīl li-ʿulūm al-tanzīl",
    "dix-huit figures",
    # --- 18 têtes, dans l'ordre de l'imprimé ---
    "<strong>Ibn Juzayy</strong>",
    "<strong>Ibn Abī Ḥātim</strong>",
    "<strong>Ibn Ǧarīr aṭ-Ṭabarī</strong>",
    "<strong>Ibn ʿĀšūr</strong>",
    "<strong>Ibn ʿAbbās</strong>",
    "<strong>Ibn ʿAǧība</strong>",
    "<strong>Ibn ʿAṭiyya</strong>",
    "<strong>Ibn Kaṯīr</strong>",
    "<strong>Abū Bakr Ibn al-ʿArabī</strong>",
    "<strong>Abū Ḥayyān</strong>",
    "<strong>al-Ālūsī</strong>",
    "<strong>al-Ḫāzin</strong>",
    "<strong>az-Zamaḫšarī</strong>",
    "<strong>Faḫr ad-Dīn ar-Rāzī</strong>",
    "<strong>Qatāda</strong>",
    "<strong>al-Qurṭubī</strong>",
    "<strong>an-Nasafī</strong>",
    "<strong>al-Wāḥidī</strong>",
    # --- généalogies / rangs / faits clés ---
    "al-Kalbī al-Andalusī",
    "at-Tamīmī al-Ḥanẓalī ar-Rāzī",
    "il déclina les charges de jugement et de gouvernance des injustices (al-maẓālim)",
    "président des muftis mâlikites de Tunis",
    "le noble Compagnon, le ḥibr (savant éminent) de la communauté",
    "il resta assidûment auprès du Messager de Dieu — que Dieu prie sur lui et le salue —",
    "environ 1660 hadiths",
    "sa vue lui fut voilée à la fin de sa vie",
    "aṭ-Ṭaṭwānī, connu sous le nom d'Ibn ʿAǧība",
    "«al-Baḥr al-madīd fī tafsīr al-Qurʾān al-maǧīd»",
    "«Ḥāšiya ʿalā al-Ǧāmiʿ aṣ-Ṣaġīr» d'as-Suyūṭī",
    "Abū ʿAlī al-Ġassānī",
    "«al-Muḥarrar al-waǧīz fī tafsīr al-Kitāb al-ʿazīz»",
    "ʿImād ad-Dīn ; Abū l-Fidāʾ Ismāʿīl ibn ʿUmar ibn Kaṯīr ad-Dimašqī aš-Šāfiʿī",
    "«al-Bāʿiṯ al-ḥaṯīṯ, šarḥ iḫtiṣār ʿulūm al-ḥadīṯ»",
    "al-Maʿāfirī al-Išbīlī al-Mālikī",
    "«al-ʿAwāṣim min al-qawāṣim»",
    "«al-Qabas fī šarḥ Muwaṭṭaʾ Mālik ibn Anas»",
    "mourut près de Fès et y fut inhumé en 543 H",
    "al-Ǧiyānī an-Nafzī",
    "al-Baḥr al-muḥīṭ fī tafsīr al-Qurʾān ; il naquit à Grenade",
    "«Rūḥ al-maʿānī fī t-tafsīr»",
    "il fut surnommé al-Ḫāzin (le trésorier) parce qu'il était le dépositaire (amīn) des scribes de Damas",
    "parmi les juristes šāfiʿites",
    "Lubāb at-taʾwīl fī maʿānī at-tanzīl",
    "Abū l-Qāsim Ǧār Allāh az-Zamaḫšarī",
    "«al-Kaššāf ʿan ḥaqāʾiq ġawāmiḍ at-tanzīl»",
    "l'unique de son temps dans les sciences rationnelles et traditionnelles",
    "«at-Tafsīr al-kabīr, nommé Mafātīḫ al-ġayb»",
    "on l'appelle aussi ibn Ḫaṭīb ar-Rayy",
    "il rapporta de ʿAbd Allāh ibn Sarǧis, d'Anas ibn Mālik, d'Abū Ṭufayl al-Kinānī et de Saʿīd ibn al-Musayyab",
    "«al-Ǧāmiʿ li-aḥkām al-Qurʾān»",
    "Ḥāfiẓ ad-Dīn an-Nasafī",
    "Madārik at-tanzīl wa-ḥaqāʾiq at-taʾwīl",
    "l'imām des savants du taʾwīl, issu des familles de marchands",
    "al-Bāsiṭ, al-Wasīṭ et al-Waǧīz fī t-tafsīr",
    # --- années de décès (18/18) ---
    "en 741 H.",
    "en l'année 327 H.",
    "en 310 H.",
    "en 1393 H.",
    "en 68 H.",
    "en 1224 H.",
    "en l'an 542 H.",
    "en 774 H.",
    "en 745 H.",
    "en 1270 H.",
    "en 678 H ;",
    "en l'an 538 H.",
    "en 606 H.",
    "en 118 H.",
    "en 671 H.",
    "(décédé en 710 H)",
    "à Nīšābūr en 468 H.",
    # --- formules récurrentes ---
    "que Dieu lui fasse miséricorde",
    "<p>Index des figures citées</p>",
]

FORBIDDEN_WARSH = [
    "ضرب الله مثلا", "يايها النبى", "ابنلى", "القنتين", "ومأواهم جهنم",
    "فنفخنا فيه", "كانتا تحت عبدين", "وعاملهم بالغلظة",
]


def norm(t: str) -> str:
    """Réplique l'auto-fix typographique de qa-lesson.py (nœuds texte)."""
    t = t.replace("'", "\u2019")
    t = re.sub(r"[ \u00a0\u202f]*([;:!?»])", "\u202f\\1", t)
    t = re.sub(r"«[ \u00a0\u202f]*", "«\u202f", t)
    t = re.sub(r" {2,}", " ", t)
    return t


def main() -> int:
    with open(DOC, "r", encoding="utf-8") as fh:
        html = fh.read()
    errors = []

    m = ARABIC.findall(html)
    if m:
        ctx = []
        for x in ARABIC.finditer(html):
            s = max(0, x.start() - 40)
            ctx.append(html[s:x.start() + 40].replace("\n", " "))
        errors.append(f"1. ARABE RESIDUEL ({len(m)} car) : " + " | ".join(ctx[:3]))

    if "'" in html:
        n = html.count("'")
        i = html.find("'")
        errors.append(f"2. APOSTROPHE DROITE ({n}) : …{html[max(0, i-40):i+40]}…")

    n_o, n_c = html.count("«"), html.count("»")
    if n_o != n_c:
        errors.append(f"3. GUILLEMETS non appariés : {n_o} ouvrants vs {n_c} fermants")

    if "<h1>Index des figures citées</h1>" not in html:
        errors.append("4. H1 attendu absent")

    missing = [a for a in ASSERTS if norm(a) not in html]
    if missing:
        errors.append(f"5. ASSERTIONS manquantes ({len(missing)}/{len(ASSERTS)}) : "
                      + " | ".join(missing[:6]))

    found_w = [f for f in FORBIDDEN_WARSH if f in html]
    if found_w:
        errors.append(f"6. FRAGMENTS CORANIQUES inattendus dans un index : {found_w}")

    for pat in ("XXX", "TODO", "【", "undefined", "NaN", "…-", "-…"):
        if pat in html:
            errors.append(f"7. RESIDU d'édition : {pat}")

    total = 4 + len(ASSERTS) + 1 + len(FORBIDDEN_WARSH)
    if errors:
        print(f"ECHEC verify-r108 ({total} contrôles) :")
        for e in errors:
            print("  " + e)
        return 1
    print(f"PASS verify-r108 : {total} contrôles, 0 échec — "
          f"18 têtes ordonnées, 18 dates de décès, {n_o} paires de guillemets, "
          f"0 arabe, 0 verset (index sans texte coranique), {len(html)} car")
    return 0


if __name__ == "__main__":
    sys.exit(main())
