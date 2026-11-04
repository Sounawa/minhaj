# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la livraison hadith2-pdf-31 (annexe 30, lāʾiḥat
al-maṣādir wa-l-marāǧiʿ + fihrist al-mawāḍīʿ, p.201-208) : 27 entrées
bibliographiques + 36 rangées d'index des thèmes, adjudications 600 dpi
(Muṣaddī, maṭwūʿāt, Sālim, Naǧībūh, Dārat, iḍāʾāt, la-mā, mawḍūʿāt,
manūʿ, šadda sīn, baqiyyat al-ʾalmaʿī), ouverture Warš (doctrine R511),
AUCUNE citation coranique, garde-doublon, livre clos 30/30.
Usage: python3 scripts-translate/verify-hadith2-pdf31.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-31-fr.html"
ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS — {label}")
    else:
        fail += 1
        print(f"FAIL — {label}")


t = open(HTML, encoding="utf-8").read()
raw = t
t = t.replace("\u202f", " ")

# --- structure générale ---
chk("h1 porte le titleFr du registre", "Liste des sources et références" in t)
chk("h1 porte la série et l'annexe 30", "annexe 30" in t)
chk("badge leçon 31 / 31 déclaré", "Leçon 31 / 31" in t)
chk("bornes p.201 à 208 déclarées", "pages 201 à 208" in t)
chk("source manuel miroir citée", "hadith-2-iadadi_text.pdf" in t)
chk("quadruple preuve des bornes documentée", "quadruple preuve de contenu" in t)
chk("bannière lāʾiḥat translittérée", "lāʾiḥat al-maṣādir wa-l-marāǧiʿ" in t)
chk("bannière fihrist al-mawāḍīʿ citée", "fihrist al-mawāḍīʿ" in t)
chk("page 206 blanche documentée", "page BLANCHE vérifiée à l’image 300 dpi entière" in t)
chk("carte hadith2-map.py citée", "hadith2-map.py" in t)
chk("tail R573 cité", "tail R573" in t)
chk("R574 cité pour la suite des bornes", "R574" in t)

# --- écart de bornes + découverte du troisième index ---
chk("écart de bornes déclaré", "ÉCART DE BORNES DÉCLARÉ" in t)
chk("corrigé par sondage d'en-tête", "SONDAGE D’EN-TÊTE" in t or "sondage des en-têtes" in t)
chk("composite bornes R574 cité", "bornes-p201-p202-p203.png" in t)
chk("troisième index découvert et déclaré", "TROISIÈME index" in t)
chk("36 rangées annoncées", "trente-six rangées" in t)
chk("27 entrées annoncées", "vingt-sept entrées numérotées" in t)

# --- ouverture Warš (R511) ---
chk("Warš ʿan Nāfiʿ ṭarīq al-ʾAzraq", "Warš ʿan Nāfiʿ" in t and "ṭarīq al-ʾAzraq" in t)
chk("al-Muṣḥaf al-Muṣaddī déclaré avec doute", "al-Muṣḥaf al-Muṣaddī" in t and "doute déclaré" in t)
chk("Fondation Mohammed VI citée", "Muʾassasat Muḥammad as-Sādis li-našr al-Muṣḥaf aš-Šarīf" in t)
chk("doctrine R511 confirmée", "R511" in t)

# --- les 14 livres de hadith ---
chk("1 Tarġīb wa-t-tarhīb — Munḏirī — 1417", "Tarġīb wa-t-tarhīb" in t and "al-Munḏirī" in t and "1417 H" in t)
chk("2 Ṣaḥīḥ al-Buḫārī — Ṭawq an-Naǧāt — 1422", "Ṭawq an-Naǧāt" in t and "an-Nāṣir" in t and "1422 H" in t)
chk("3 Sunan Abī Dāwūd — Arnaʾūṭ/Qarah Ballī — 1430", "Qarah Ballī" in t and "1430 H" in t)
chk("4 Sunan at-Tirmiḏī — Bābī l-Ḥalabī — 1395", "Bābī l-Ḥalabī" in t and "1395 H" in t)
chk("4 trois éditeurs Tirmiḏī (Šākir/ʿAbd al-Bāqī/ʿAṭwa)", "Ibrāhīm ʿAṭwa ʿAwwaḍ" in t)
chk("5 Sunan ad-Dāraquṭnī — 4 taḥqīq — 1424", "Barr Hūm" in t and "1424 H" in t)
chk("6 Sunan al-Kubrā an-Nasāʾī — Šalabī — 1421", "as-Sunan al-Kubrā" in t and "1421 H" in t)
chk("7 Sunan al-Kubrā Bayhaqī — 3e éd. — 1424", "troisième édition, 1424 H" in t)
chk("8 Šuʿab al-ʾīmān — Riyad + Bombay — 1423", "Bombay" in t and "1423 H" in t)
chk("9 Ṣaḥīḥ Ibn Ḥibbān — Dārimī al-Bustī — 1408", "ad-Dārimī al-Bustī" in t and "1408 H" in t)
chk("10 al-Muǧtabā — Abī Gudda — Alep — 1406", "Abī Gudda" in t and "Alep" in t and "1406 H" in t)
chk("11 al-Mustadrak al-Ḥākim — 1411", "al-Mustadrak ʿalā ṣ-Ṣaḥīḥayn" in t and "1411" in t)
chk("12 Musnad Aḥmad — Dār al-Ḥadīth — 1416", "Dār al-Ḥadīth" in t and "1416 H" in t)
chk("13 Ṣaḥīḥ Muslim — ʿAbd al-Bāqī — Iḥyāʾ at-Turāṯ", "binuql al-ʿadl ʿan al-ʿadl" in t and "Iḥyāʾ at-Turāṯ al-ʿArabī" in t)
chk("14 al-Muwaṭṭaʾ Yaḥyā b. Yaḥyā — Maǧlis 1434/2013", "riwāyat Yaḥyā b. Yaḥyā al-Layṯī" in t and "al-Maǧlis al-ʿIlmī al-ʾAʿlā" in t and "2013" in t)

# --- les 5 commentaires ---
chk("15 al-ʾIstiḏkār — Sālim ʿAṭā + Maʿwaḍ — 1421", "Sālim Muḥammad ʿAṭā" in t and "Maʿwaḍ" in t and "1421 H" in t)
chk("16 Šarḥ az-Zarqānī — Ṭāhā Saʿd — 1424", "Ṭāhā ʿAbd ar-Raʾūf Saʿd" in t and "Maktabat aṯ-Ṯaqāfa ad-Dīniyya" in t)
chk("17 Fatḥ al-Bārī — Dār al-Maʿrifa — 1379", "Dār al-Maʿrifa" in t and "1379 H" in t)
chk("18 al-Muntaqā al-Baǧī — Saʿāda — 1332", "al-Baǧī" in t and "Maṭbaʿat as-Saʿāda" in t and "1332 H" in t)
chk("19 Naṣb ar-Rāya — ʿAwāma — Rayyān/Qibla — 1418", "Muḥammad ʿAwāma" in t and "ar-Rayyān" in t and "Dār al-Qibla" in t and "1418 H" in t)
chk("19 baqiyyat al-ʾalmaʿī vocalisation incertaine déclarée", "Baqiyyat al-ʾalmaʿī" in t and "incertitude déclarée" in t)

# --- les 5 livres de fiqh ---
chk("20 al-Bayān — b. Rušd — Ḥiǧǧī + Akhzīn — 1408", "b. Rušd al-Qurṭubī" in t and "Akhzīn" in t and "1408 H" in t)
chk("21 at-Tawḍīḥ — Ḫalīl — Markaz Naǧībūh — 1429", "Markaz Naǧībūh" in t and "1429 H" in t)
chk("22 Šarḥ Ibn Nāǧī — Tanūḫī — 1428", "at-Tanūḫī" in t and "1428 H" in t)
chk("23 Matn ar-Risāla — Dār al-Fikr", "Matn ar-Risāla" in t and "Dār al-Fikr" in t)
chk("24 Šarḥ al-Kabīr Dardīr + Dasūqī — 1419/1998", "Dardīr" in t and "ad-Dasūqī" in t and "1998" in t)

# --- les 3 livres de biographies ---
chk("25 Tahḏīb at-Tahḏīb — Dārat al-Maʿārif — 1326", "Dārat al-Maʿārif an-Niẓāmiyya" in t and "1326 H" in t)
chk("26 al-ʾIṣāba — Mawǧūd/Muʿawwaḍ — 1445", "ʿAbd al-Mawǧūd" in t and "Muʿawwaḍ" in t and "1445 H" in t)
chk("27 Sayr ʾAʿlām an-Nubalāʾ — Ḏahabī — 3e éd. 1405", "aḏ-Ḏahabī" in t and "Qāyimāz" in t and "1405 H" in t)

# --- écarts déclarés (600 dpi) ---
chk("écart maṭwūʿāt/maṭbūʿāt déclaré", "al-maṭwūʿāt" in t and "al-maṭbūʿāt" in t)
chk("écart Sālim/Salīm déclaré", '"Sālim" ainsi — contre "Salīm"' in t)
chk("écart Naǧībūh/Naǧīb déclaré", "probablement \"Markaz Naǧīb\"" in t)
chk("Dārat al-Maʿārif tranchée", "Dārat al-Maʿārif an-Niẓāmiyya" in t)
chk("ʾiḍāʾāt tranché contre couche ʾiḍāʿāt", "ʾiḍāʾāt manhaǧiyya" in t and "ʾiḍāʿāt" in t)
chk("coquille la-mā/lahum déclarée", 'probablement "lahum"' in t)
chk("coquille mawḍūʿāt/mawāḍīʿ déclarée", 'probablement "al-mawāḍīʿ"' in t)
chk("coquille manūʿ/mamnūʿ déclarée", "al-manūʿ" in t and "al-mamnūʿ" in t)
chk("šadda sur sīn de wa-sitta documentée", "šadda sur le sīn du mot \"wa-sitta\"" in t)
chk("raqama kutubahū formule imprimée portée", "raqama kutubahū wa-ʾabwābahū wa-ʾaḥādīṯahū" in t)

# --- l'index des thèmes (36 rangées) ---
chk("36 lignes tbody", raw.count("<tr><td>") == 36)
chk("2 tables rendues ? (1 seule attendue)", raw.count("<table>") == 1)
chk("rangées pédagogiques 5/6/8/11/12", "<td>5</td>" in raw and "<td>6</td>" in raw and "<td>8</td>" in raw and "<td>11</td>" in raw and "<td>12</td>" in raw)
chk("leçon 1 à la page 14", "fī s-safar wa-l-ḥaḍar.</td><td>14" in raw)
chk("leçon 28 à la page 192", "min Šawwāl (l’imprimé porte la šadda sur le sīn du mot \"wa-sitta\" — écart documenté).</td><td>192" in raw)
chk("annexes 199/201/207", "<td>199</td>" in raw and "<td>201</td>" in raw and "<td>207</td>" in raw)
chk("coïncidence annexes/pagination scan", "coïncident exactement avec la pagination du scan" in t)
chk("coïncidence rangées 6-33 avec pdf-2 à pdf-29", "slots pdf-2 à pdf-29 du registre" in t)
chk("fiṭr à 152", "zakāt al-fiṭr.</td><td>152" in raw)

# --- aucune citation coranique ---
chk("AUCUNE citation coranique déclarée", "AUCUNE citation coranique" in t)
chk("cache quran-cache non sollicité documenté", "quran-cache.json non sollicité" in t)

# --- chaîne de production ---
chk("trace du tick consignée", "1a1a172f41684dc9-cron-agent-loop-202611050405" in t)
chk("claim 20:41:36Z consigné", "20 :41 :36Z" in t or "20:41:36Z" in t)
chk("même passe que R574 + mandat avancer", "tu dois avancer" in t)
chk("garde-doublon pdf-31 ABSENT consigné", "pdf-31 ABSENT" in t)
chk("couche 5 468 car consignée", "couche texte 5 468 car" in t)
chk("9 zones d'adjudication consignées", "NEUF zones d’adjudication" in t)
chk("méthode à l'œil 300 dpi consignée", "lus in extenso À L’ŒIL" in t)
chk("livre clos 30/30 consigné", "30/30 — LIVRE CLOS" in t)

# --- typographie ---
AR = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")
residus = [c for c in raw if AR.match(c) and ord(c) != 0xFDFA]
chk(f"0 arabe résiduel hors ﷺ — trouvé {len(residus)}", len(residus) == 0)
chk("ﷺ présent (2 entrées imprimées)", raw.count("\uFDFA") == 2)
chk("guillemets appariés", raw.count("«") == raw.count("»"))
chk("0 apostrophe droite", "'" not in raw)

print(f"\n{'=' * 60}")
print(f"verify-hadith2-pdf31 : {ok} PASS / {fail} FAIL")
raise SystemExit(1 if fail else 0)
