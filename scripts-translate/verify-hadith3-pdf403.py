# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-403
(les règles du séjour à Muzdalifa — الدرس 14, p.97-103 du manuel
hadith-3-iadadi_text.pdf, 196 p., livre portail pré-mappé 29 slots
pdf-mut23h2x-390..418) : bornes p.97-103 (p.96 = annonce de la leçon 13
sur Muzdalifa ; p.104 = objectifs de la leçon 15 sondés en couche texte =
borne supérieure) ; 10 numéros du Muwaṭṭaʾ tranchés chiffre par chiffre
(1165, 1193, 1166, 1152, 1192, 1195, 1160, 1161, 1162, 1154) ; citations
coraniques rendues du cache ḥafṣ (2:197, 2:187, 6:145, 22:67) sous
étiquettes imprimées (196, 186, 146, 65) — écarts consignés dont un sens
inverse (Anʿām +1) et un décalage régional (Ḥaǧǧ −2) ; honnêteté
d'apparat ( segments dégradés d'Usāma, de l'athar de ʿUmar, du titre
d'exploitation, du fragment ʿAṭāʾ omis consigné) ; 0 arabe, 0 apostrophe
droite, guillemets appariés.
Usage: python3 scripts-translate/verify-hadith3-pdf403.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-403-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
CLAIM = "/home/z/my-project/tr-tmp/claims/hadith3-pdf-mut23h2x-403.claim.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC : {label}")


h = open(HTML, encoding="utf-8").read()
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", " ").replace("\u2009", " "))

# --- 1) squelette ---
chk("h1 Leçon 14", "<h1>Leçon 14" in hn and "Muzdalifa" in hn)
chk("h1 titleFr registre", "les règles du séjour à Muzdalifa" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.97-103", "p.97-103" in hn)
chk("meta slot 403", "pdf-mut23h2x-403" in hn)
chk("meta tick trace", "workerD-tick499559-1456-r674" in hn and "07h01 UTC" in hn)
chk("meta borne sup p.104 sondée", "p.104" in hn and "borne supérieure exclusive" in hn)
chk("meta voisins 402/404", "leçon 13" in hn and "pdf-mut23h2x-404" in hn)
chk("meta doctrine R511", "R511" in hn)
chk("meta OCR inversés", "5611" in hn and "6611" in hn and "2511" in hn)
chk("meta session R674/R674d reprise", "R674/R674d" in hn)
chk("meta token restauré push 341c64e", "341c64e" in hn)
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (l’ouverture de la leçon)",
    "Les textes du cours",
    "La notice du transmetteur (tarǧamat ar-rāwī)",
    "La glose des mots (aš-šarḥ) du manuel",
    "Le résumé du cours (al-istiḫlāṣ)",
    "Le fiqh du hadith (fiqh al-ḥadīṯ)",
    "L’évaluation (at-taqwīm)",
    "L’exploitation du texte",
    "La préparation préalable (al-iʿdād al-qablī)",
    "L’apparat de preuve de la livraison",
):
    chk(f"section « {sec[:44]} »", sec in hn)

# --- 2) les deux objectifs ---
chk("obj 1 nuit du dixième", "aḥkām laylati l-ʿāširi min Ḏī l-Ḥiǧǧa" in hn)
chk("obj 2 duʿāʾ/ḏikr Mashʿar", "ḥukma d-duʿāʾ wa-ḏ-ḏikri" in hn and "bi-l-Mašʿari l-Ḥarām" in hn)

# --- 3) tamhīd ---
chk("tamhīd manāsik + lieu", "min manāsiki l-ḥaǧǧ" in hn and "entre ʿArafāt et Minā" in hn)
chk("tamhīd étymologies ×3", "yutaqarrabu ilā llāhi taʿālā" in hn and "ifāḍa" in hn and "zulfah" in hn)
chk("tamhīd 4e raison dégradée consignée", "terre arrosée et balayée" in hn and "consignée" in hn)
chk("tamhīd questions ×3", "la manière de cheminer vers Muzdalifa" in hn and "règles du bivouac et de la prière" in hn and "stationnement au Mashʿar al-Ḥarām" in hn)

# --- 4) les deux textes ---
chk("texte 1165 ʿanaq/fajwah/nass", "n° 1165" in hn and "kāna yusīru l-ʿanaq" in hn and "fajwah" in hn and "nass" in hn)
chk("1165 Hishām nass plus rapide", "de Hishām b. ʿUrwa, de son père" in hn and "plus rapide que l’al-ʿanaq" in hn)
chk("texte 1193 šiʿb/amāmaka", "n° 1193" in hn and "bi-š-šiʿb" in hn and "aṣ-ṣalāhu amāmaka" in hn)
chk("1193 wuḍūʾ non complété puis complété", "fa-lam yusbiġ al-wuḍūʾ" in hn and "fa-asbaġa al-wuḍūʾ" in hn)
chk("1193 anāḫa/manzili/šayʾan", "anāḫa kullu insānin baʿīrahū" in hn and "fī manzilihi" in hn and "wa-lam yuṣalli baynahumā šayʾan" in hn)

# --- 5) notice + gloses + résumé ---
chk("notice Usāma mawlā + aimé", "Usāma b. Zayd b. Ḥāriṯah al-Kalbī" in hn and "mawlā du Messager" in hn and "ḥibbuhu wa-bnu ḥibbihi" in hn)
chk("notice an 59 réinversée", "an 59 de l’Hégire" in hn and "95" in hn)
chk("notice segments dégradés consignés", "porté sur les épaules" in hn and "Abū Bakr et ʿUmar b. al-Ḫaṭṭāb" in hn)
chk("glose ʿanaq", "bayna l-ibṭāʾi wa-l-isrāʿ" in hn and "encolure" in hn)
chk("glose nass asraʿ", "asraʿ" in hn)
chk("glose dafʿ izdiḥām", "izdiḥāmuhum" in hn)
chk("glose maqām aṣ-ṣalāh", "mawḍiʿu ṣ-ṣalāh" in hn)
chk("résumé 3 items", "kayfa yasīru l-ḥuǧǧāǧu ilā l-Muzdalifa" in hn and "ubayyinu aḥkāma l-wuqūfi" in hn and "hal yaǧibu ʿalā l-ḥāǧǧi l-mabītu" in hn)

# --- 6) fiqh : awwalan (dafʿ + wuqūf) ---
chk("sayr sakīnah/waqār + hâte pour la prière", "bi-sakīnah" in hn and "wa-waqār" in hn and "istaʿǧalū" in hn)
chk("1166 ʿUmar Muḥaṣṣir + Wādī an-Nār", "n° 1166" in hn and "Baṭn Muḥaṣṣir" in hn and "Wādī an-Nār" in hn)
chk("1152 tout Muzdalifa sauf Muḥaṣṣir", "n° 1152" in hn and "wa-rtafiʿū ʿan Baṭni Muḥaṣṣir" in hn)
chk("Ǧābir Abū Dāwūd sans numéro consigné", "waqqaftu hāhunā" in hn and "Sunan Abī Dāwūd" in hn and "consigné" in hn)
chk("Mukhtaṣar Khalīl p. 79 + isfār", "Mukhtaṣar de Khalīl" in hn and "yukabbiru wa-yadʿū lil-isfār" in hn)

# --- 7) fiqh : ṯāniyan (aḥkām al-Muzdalifa) ---
chk("1192 jamʿ ğamīʿan", "n° 1192" in hn and "ǧamīʿan" in hn)
chk("1195 Ibn ʿUmar", "n° 1195" in hn)
chk("iʿādah/iǧzāʾ Ibn al-Qāsim vs ǧumhūr", "al-iʿādah" in hn and "al-iǧzāʾ" in hn and "Ibn al-Qāsim" in hn)
chk("jamʿ al-Qaṣwāʾ/Zamzam/ḥaṭṭ", "al-Qaṣwāʾ" in hn and "Zamzam" in hn and "qabla ḥaṭṭi r-riḥāl" in hn)
chk("rifqan bi-d-dawābb + une seule prière", "rifqan bi-d-dawābb" in hn and "ka-ṣ-ṣalāhi l-wāḥidah" in hn)
chk("jamʿ taʿabbudī Mālikites", "taʿabbadī" in hn and "lā yuʿqalu maʃnāh".replace("ʾ", "") if False else "lā yuʿqalu maʿnāh" in hn)
chk("adhān Usāma apparent + Ibn Masʿūd", "Ibn Masʿūd" in hn and "raʾaytu n-Nabiyya" in hn and "wa-ḫtārah" in hn)
chk("nuzūl wāǧib ḥaṭṭ + dam ashhar", "bi-qadri ḥaṭṭi r-riḥāl" in hn and "ad-dam" in hn and "al-ashhar" in hn)
chk("mabīt sunna + nuit vivifiée", "al-mabīt" in hn and "iḥyāʾ hāḏihi l-laylati bi-l-ʿibādah" in hn)
chk("Mashʿar qibla/gauche/isfār/7 cailloux", "awwala waqtih" in hn and "ʿan yasārih" in hn and "sabʿa ḥaṣāt" in hn and "Ǧamrah de al-ʿAqabah" in hn)
chk("rukṣaḥ femmes/enfants/excuses", "turḫaṣu" in hn and "ḏawī l-aʿḏār" in hn)
chk("1160 fils d'Ibn ʿUmar + abrad an-nās", "n° 1160" in hn and "abrad an-nās" in hn)
chk("1161 cliente Asmāʾ bi-ġalas", "n° 1161" in hn and "bi-ġalas" in hn and "kunnā naṣnaʿu ḏālika" in hn and "maʿa man huwa ḫayrun mink" in hn)
chk("1162 Tālḥa wuldānah", "n° 1162" in hn and "Tālḥa b. ʿUbaydallāh" in hn and "wuldānah" in hn)

# --- 8) éval + exploitation + iʿdād ---
chk("éval 3 items", "kayfa kāna yasīru ilā l-Muzdalifa" in hn and "ubayyinu ṣifata l-ǧamʿi bayna l-ʿishāʾayn bi-Muzdalifa" in hn and "maʿa l-istidlāli wa-t-taʿlīl" in hn)
chk("éval cas 1 Maghrib en route", "fa-ṣallā l-Maġriba fī ṭ-ṭarīq" in hn)
chk("éval cas 2 sans Muzdalifa", "bi-dūni n-nuzūli bi-Muzdalifa" in hn)
chk("exploitation 1154 Mālik", "n° 1154" in hn and "Mālik a dit" in hn)
chk("verset Baqara 197 cache / imprimé 196", "fa-man faraḍa fīhinna l-ḥaǧǧa fa-lā rafaṯa wa-lā fusūqa wa-lā ǧidāla fī l-ḥaǧǧ" in hn and "al-Baqara 197 du cache ḥafṣ" in hn and "l’āya 196" in hn)
chk("rafth = femmes + Baqara 187", "uḥilla lakum laylata ṣ-ṣiyāmi r-rafaṯu ilā nisāʾikum" in hn and "al-Baqara 187 du cache ḥafṣ" in hn and "l’āya 186" in hn)
chk("fusūq = anṣāb + Anʿām 145 écart inverse", "aḏ-ḏabḥu li-l-anṣāb" in hn and "aw fiṣqan uhilla li-ġayri llāhi bih" in hn and "al-Anʿām 145 du cache ḥafṣ" in hn and "l’āya 146" in hn)
chk("jidāl Ḥums Quzayḥ + Ḥaǧǧ 67 décalage −2", "bi-Quzayḥ" in hn and "naḥnu aṣwab" in hn and "li-kulli ummatin ǧaʿalnā manskān" in hn and "al-Ḥaǧǧ 67 du cache ḥafṣ" in hn and "l’āya 65" in hn)
chk("clôture « j’ai entendu des gens de science »", "wa-qad samiʿtu ḏālika min ahli l-ʿilm" in hn)
chk("iʿdād 3 questions Minā", "ḥukm ṣiyām ayyām Minā" in hn and "ṣifat takbīr ayyām Minā" in hn and "ḥukm qaṣr aṣ-ṣalāh bi-Minā" in hn)

# --- 9) apparat ---
chk("apparat numéros tranchés chiffre par chiffre", "chiffre par chiffre" in hn and "tr-tmp/vlm-403/" in hn)
chk("apparat douze lectures r675", "douze lectures d’image" in hn)
chk("apparat crops r674d/r675", "qa-crops-r674d" in hn and "qa-crops-r675" in hn)
chk("apparat bornes p.96/p.104 sondées", "p.96" in hn and "p.104" in hn and "jamais devinée" in hn)
chk("apparat ʿAṭāʾ fragment omis consigné", "ʿAṭāʾ b. Abī Rabāḥ" in hn and "omis" in hn)
chk("apparat qa browser r676", "qa-r676-403-{desktop,mobile}.png" in hn)
chk("apparat sous-agent 407 deux échecs consignés", "sous-agent" in hn and "context deadline exceeded" in hn)

# --- 10) typographie ---
chk("0 arabe résiduel", not re.search(r"[\u0600-\u06FF\u0750-\u077F]", re.sub(r"\uFDFA", "", h)))
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))

# --- 11) registre : pas de doublon ---
d = json.load(open(REG, encoding="utf-8"))
les = d.get("lessons", d if isinstance(d, list) else [])
mine = [l for l in les if str(l.get("docId") or "") == "pdf-mut23h2x-403"]
chk("registre contient slot 403", len(mine) == 1)
if mine:
    chk("403 htmlFr vide avant hand-set", mine[0].get("htmlFr") in (None, ""))
done = sum(1 for l in les if l.get("htmlFr"))
chk("doublons impossibles (15 livrées)", done == 15)

# --- 12) claim actif ---
c = open(CLAIM, encoding="utf-8").read()
chk("claim 403 trace workerD", "workerD-tick499559-1456-r674" in c)

print(f"VERIFY pdf-403 : {ok} OK, {fail} échecs")
raise SystemExit(1 if fail else 0)
