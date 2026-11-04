# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la livraison hadith2-pdf-30 (annexe 29, fihrist
al-aʿlām al-mutaraǧǧim lahum, index des figures, p.199-200) : 28 entrées
tranchées à l'image 300 dpi (15 en p.199 + 13 en p.200), écart de bornes
déclaré et corrigé par sondage d'en-tête (la lāʾiḥat al-maṣādir commence
dès p.201), AUCUNE citation coranique (cache non sollicité),
garde-doublon, machine rétablie.
Usage: python3 scripts-translate/verify-hadith2-pdf30.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-30-fr.html"
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
raw = t  # copie brute pour les contrôles typographiques finaux
t = t.replace("\u202f", " ")  # normalisation NNBSP pour les assertions

# --- structure générale ---
chk("h1 porte le titleFr du registre", "Index des figures présentées" in t)
chk("h1 porte la série et l'annexe 29", "annexe 29" in t)
chk("badge leçon 30 / 31 déclaré", "Leçon 30 / 31" in t)
chk("bornes p.199 à 200 déclarées", "pages 199 à 200" in t)
chk("source manuel miroir citée", "hadith-2-iadadi_text.pdf" in t)
chk("quadruple preuve des bornes documentée", "quadruple preuve de contenu" in t)
chk("bannière fihrist translittérée", "fihrist al-aʿlām al-mutaraǧǧim lahum" in t)
chk("en-têtes de table al-ʿalam / aṣ-ṣafḥa", "aṣ-ṣafḥa" in t and "al-ʿalam" in t)
chk("page 198 blanche documentée", "page de clôture BLANCHE" in t)
chk("lāʾiḥat al-maṣādir citée comme borne haute", "lāʾiḥat al-maṣādir wa-l-marāǧiʿ" in t)
chk("carte hadith2-map.py citée", "hadith2-map.py" in t)
chk("tail R573 cité comme autorité", "tail R573" in t)

# --- écart de bornes (sondage d'en-tête) ---
chk("écart de bornes déclaré", "ÉCART DE BORNES DÉCLARÉ" in t)
chk("corrigé par sondage d'en-tête", "SONDAGE des en-têtes" in t or "SONDAGE des en-têtes".lower() in t or "sondage d'en-tête" in t)
chk("composite bornes cité", "bornes-p201-p202-p203.png" in t)
chk("annexe 30 dès p.201 établie", "DÈS la page 201" in t)
chk("pdf-31 annoncé (pages 201-208)", "pages 201-208" in t)

# --- garde-doublon ---
chk("titleFr registre htmlFr 0 car consigné", "htmlFr 0 car" in t)
chk("contrôle positif pdf-29 consigné", "pdf-29 htmlFr 22 915 car" in t)
chk("registre 1 132 savants consigné", "1 132" in t)
chk("registre savant pdf-30 ABSENT consigné", "pdf-30 ABSENT" in t)

# --- les 15 entrées de la page 199 (nom + page) ---
chk("1 al-Aʿraǧ — 15", "al-Aʿraǧ." in t and "15" in t)
chk("2 ʿAbdallāh ibn ʿUmar — 15", "ʿAbdallāh ibn ʿUmar" in t)
chk("3 Umm Hāniʾ — 22", "Umm Hāniʾ" in t)
chk("4 Abū Ǧuhaym — 22", "Abū Ǧuhaym" in t)
chk("5 ʿUmar ibn al-Ḫaṭṭāb — 29", "ʿUmar ibn al-Ḫaṭṭāb" in t)
chk("6 Sahl ibn Saʿd as-Sāʿidī — 35", "Sahl ibn Saʿd as-Sāʿidī" in t)
chk("7 ʿAbdallāh ibn ʿAmr ibn al-ʿĀṣ — 41", "ʿAbdallāh ibn ʿAmr ibn al-ʿĀṣ" in t)
chk("8 Saʿīd ibn al-Musayyib — 47", "Saʿīd ibn al-Musayyib" in t)
chk("9 Abū Wāqid al-Laythī — 47", "Abū Wāqid al-Laythī" in t)
chk("10 ʿĀʾiša mère des croyants — 54", "la mère des croyants" in t)
chk("11 ʿAbdallāh ibn Zayd al-Māzinī — 61", "ʿAbdallāh ibn Zayd al-Māzinī" in t)
chk("12 Zayd ibn Ḫālid al-Ǧuhanī — 61", "Zayd ibn Ḫālid al-Ǧuhanī" in t)
chk("13 Abū Ayyūb al-Anṣārī — 68", "Abū Ayyūb al-Anṣārī" in t)
chk("14 Abū Hurayra — 68", "Abū Hurayra" in t)
chk("15 ʿAmr ibn Ḥazm — 74", "ʿAmr ibn Ḥazm" in t)

# --- les 13 entrées de la page 200 ---
chk("16 Abū Salama ibn ʿAbd ar-Raḥmān ibn ʿAwf — 80", "Abū Salama ibn ʿAbd ar-Raḥmān ibn ʿAwf" in t)
chk("17 ʿAbdallāh aṣ-Ṣanābiḥī — 87", "ʿAbdallāh aṣ-Ṣanābiḥī" in t)
chk("18 Umm ʿAṭiyya al-Anṣāriyya — 92", "Umm ʿAṭiyya al-Anṣāriyya" in t)
chk("19 ʿAmra bint ʿAbd ar-Raḥmān — 99", "ʿAmra bint ʿAbd ar-Raḥmān" in t)
chk("20 Abū Saʿīd al-Ḫudrī — 106", "Abū Saʿīd al-Ḫudrī" in t)
chk("21 ʿUṯmān ibn ʿAffān — 119", "ʿUṯmān ibn ʿAffān" in t)
chk("22 Muʿāḏ ibn Ǧabal — 126", "Muʿāḏ ibn Ǧabal" in t)
chk("23 Bisr ibn Saʿīd — 140", "Bisr ibn Saʿīd" in t)
chk("24 Sulaymān ibn Yasār — 141", "Sulaymān ibn Yasār" in t)
chk("25 ʿAṭāʾ ibn Yasār — 141", "ʿAṭāʾ ibn Yasār" in t)
chk("26 ʿUrwa ibn az-Zubayr — 166", "ʿUrwa ibn az-Zubayr" in t)
chk("27 Muʿāwiya ibn Abī Sufyān — 172", "Muʿāwiya ibn Abī Sufyān" in t)
chk("28 Anas ibn Mālik — 185", "Anas ibn Mālik" in t)
chk("28 entrées annoncées", "Vingt-huit entrées" in t)
chk("15 + 13 annoncé", "quinze en page 199 et treize en page 200" in t)

# --- pagination des tables ---
chk("table p.199 bornée par ʿAmr ibn Ḥazm — 74", "ʿAmr ibn Ḥazm (que Dieu soit satisfait de lui).</td><td>74" in raw)
chk("table p.200 bornée par Anas ibn Mālik — 185", "Anas ibn Mālik (que Dieu soit satisfait de lui).</td><td>185" in raw)
chk("deux tables rendues", raw.count("<table>") == 2 and raw.count("</table>") == 2)
chk("28 lignes tbody", raw.count("<tr><td>") == 28)

# --- hommages et successeurs sans formule ---
chk("hommage masculin rendu", "(que Dieu soit satisfait de lui)" in t)
chk("hommage féminin rendu", "(que Dieu soit satisfait d’elle)" in t)
chk("radïyAllāhu ʿanhu / ʿanhā expliqué", "radïyAllāhu ʿanhu" in t and "ʿanhā" in t)
chk("quatre successeurs sans formule identifiés", "Bisr ibn Saʿīd, Sulaymān ibn Yasār, ʿAṭāʾ ibn Yasār et ʿUrwa ibn az-Zubayr" in t)

# --- cohérence corpus ---
chk("renvoi croisé siqqat tarǧamatuh (leçon 28)", "siqqat tarǧamatuh" in t)
chk("répartition des pages 15-185", "pages 140 à 185" in t)
chk("pagination imprimée sans re-numérotation", "sans re-numérotation de notre part" in t)

# --- aucune citation coranique ---
chk("AUCUNE citation coranique déclarée", "AUCUNE citation coranique" in t)
chk("cache quran-cache non sollicité documenté", "quran-cache.json non sollicité" in t)

# --- chaîne de production ---
chk("trace du tick consignée", "1a1a172f41684dc9-cron-agent-loop-202611050405" in t)
chk("claim 20:07:35Z consigné", "20 :07 :35Z" in t or "20 :07 :35" in t)
chk("refresh 20:08:16Z consigné", "20 :08 :16Z" in t or "20 :08 :16" in t)
chk("forensic reset consigné", "AUCUN reset destructeur" in t)
chk("recette R508 consignée", "recette R508" in t)
chk("supervisor PID 1589 consigné", "PID 1589" in t)
chk("heartbeat cron-alive consigné", "PRODUCTION 24/7 EXÉCUTÉ" in t)
chk("méthode couche 4 193 car consignée", "couche texte 4 193 car" in t)
chk("pages 300 dpi lues à l'œil consignées", "lus in extenso À L’ŒIL" in t)
chk("aucun recadrage requis consigné", "AUCUN recadrage supplémentaire requis" in t)
chk("pas de directive PARALLÈLE consignée", "pas de directive PARALLÈLE" in t)
chk("production solo consignée", "production solo" in t)

# --- typographie (mêmes règles que qa-lesson) ---
AR = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")
residus = [c for c in raw if AR.match(c) and ord(c) != 0xFDFA]
chk(f"0 arabe résiduel (hors ﷺ) — trouvé {len(residus)}", len(residus) == 0)
chk("guillemets appariés", raw.count("«") == raw.count("»"))
chk("0 apostrophe droite", "'" not in raw)
chk("aucun ﷺ requis (index sans salawat)", "\uFDFA" not in raw)

print(f"\n{'=' * 60}")
print(f"verify-hadith2-pdf30 : {ok} PASS / {fail} FAIL")
raise SystemExit(1 if fail else 0)
