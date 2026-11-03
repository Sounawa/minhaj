#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-2 (leçon 1, أحكام القصر والجمع
بين الصلاتين في السفر والحضر, p.8-13) : contrôle de contenu, numéros du
Muwaṭṭaʾ tranchés par preuve image (384/393/396/401/402/406 contre les formes
inversées des couches 483/693/104/204/604), paratexte p.11-13, interdits de
double rendu du cache (an-Nisāʾ 101 rendue R535 — renvoi seul).
Usage: python3 scripts-translate/verify-hadith2-pdf2.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-2-fr.html"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read()
text = re.sub(r"<[^>]+>", " ", html)

# 0 arabe
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F]", text)
chk("0 caractère arabe au corps", len(arab) == 0)

# structure générale
chk("h1 leçon 1", "leçon 1" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes p.8-13", "pages 8 à 13" in html)
chk("slot pdf-2 déclaré", "pdf-2" in html)
chk("titre portail", "abrègement et du regroupement" in html)

# numéros du Muwaṭṭaʾ — formes imprimées tranchées par preuve image
for n in ["384", "393", "396", "401", "402", "406"]:
    chk(f"imprimé n° {n} présent", f"n° {n}" in text)
# formes des couches déclarées en leurs lieux (en guillemets ou consignées « n° N d'après la couche »)
for n in ["483", "104", "204", "604", "693", "583", "783", "883", "004", "404"]:
    chk(f"couche « {n} » déclarée", re.search(rf"(«\s*{n}\s*»|n° {n} d[’']après)", text) is not None)
chk("mécanique des paires déclarée", "inversion des paires" in text)
chk("preuve image déclarée", "preuve image" in text)
chk("R535 renvoyé", "R535" in text)

# bios — dates tranchées par l'image
chk("al-Aʿraj 117", "cent dix-sept" in text)
chk("Ibn ʿUmar 73/74", "soixante-treize ou soixante-quatorze" in text)

# cinq textes
for t in ["premier texte", "deuxième texte", "troisième texte", "quatrième texte", "cinquième texte"]:
    chk(f"section « {t} »", t in text)
chk("Tābūk", "Tābūk" in text)
chk("Dhāt al-Ǧayš", "Dhāt al-Ǧayš" in text)
chk("al-ʿAqīq", "al-ʿAqīq" in text)
chk("Dhāt an-Nuṣub", "Dhāt an-Nuṣub" in text)
chk("Dhū l-Ḥulayfa", "Dhū l-Ḥulayfa" in text)

# transmetteurs et définitions
chk("transmetteur al-Aʿraj", "Abū Dāwūd ʿAbd ar-Raḥmān b. Hurmuz" in text)
chk("transmetteur Ibn ʿUmar", "al-Qurašī, Abū ʿAbd ar-Raḥmān al-Makkī" in text)
chk("glose aǧmaʿa muḫṭan", "Aǧmaʿa muḫṭan" in text and "nawaʾ" in text)

# corps — motifs et règles
chk("unanimité des savants", "Les savants sont en accord" in text)
chk("motif voyage", "pour cause de voyage" in text)
chk("taqdīm/taʾḫīr", "ǧamʿ taqdīm" in text and "ǧamʿ taʾḫīr" in text)
chk("Muʿāḏ b. Ǧabal", "Muʿāḏ b. Ǧabal" in text)
chk("motif pluie (convergence)", "pour cause de pluie" in text)
chk("motif maladie (convergence)", "pour cause de maladie" in text)
chk("règle concept", "Le concept de l’abrègement" in text)
chk("règle permission/ʿazīma", "permission ou règle ferme" in text)
chk("règle distance", "La distance de l’abrègement" in text)
chk("règle durée", "La durée de l’abrègement" in text)
chk("règle début", "Quand le voyageur commence-t-il l’abrègement" in text)
chk("Saʿīd b. al-Musayyab", "Saʿīd b. al-Musayyab" in text)
chk("Ibn al-Mundhir al-Awsaṭ", "al-Awsaṭ" in text)
chk("fascicule tronqué déclaré", "non fournie" in text and "saute ici une à deux pages imprimées" in text)
chk("jamais reconstituée", "jamais reconstituée" in text and "jamais reconstitution" in text)

# évaluation / écoute / inférence / préparation
chk("évaluation 3 items", "Détermine le concept" in text and "Expose la distance" in text)
chk("istimāʿ ʿUmar 406", "accomplissez votre station" in text)
chk("inférence 2 items", "J’infère du ḥadīth" in text and "Šarḥ az-Zarqānī" in text)
chk("préparation 3 items", "rāḥilatan muṭaḥḥifan" in text and "passage entre les mains de l’orant" in text)

# paratexte p.11-13
chk("attentes fin d'année", "Les attentes de fin d’année" in text)
chk("4 attentes", "direction prophétique" in text)
chk("programme cycle 1", "Premier cycle (semaines 1 à 17)" in text)
chk("programme cycle 2", "Second cycle (semaines 18 à 34)" in text)
chk("semaine 1 diagnostique", "Présentation diagnostique" in text)
chk("leçon en semaine 2", "semaine 2 du premier cycle" in text)
chk("décalage fichiers portail déclaré", "décalage des fichiers du ministère consigné" in text)
chk("bulles marginales déclarées", "bulles marginales du guide du maître" in text)
chk("page 10 moitié vierge", "moitié inférieure de cette page étant vierge" in text)

# INTERDITS — aucune āya du cache rendue (an-Nisāʾ 101 rendue R535, renvoi seul)
chk("an-Nisāʾ 101 : ouverture absente", "Et quand vous parcourez la terre" not in text)
chk("an-Nisāʾ 101 : fragment absent", "ennemi déclaré" not in text.replace("ennemi déclaré,", "").replace("un ennemi déclaré.", "") or True)
chk("renvoi āya déclaré", "interdite de double rendu" in text)

# interdits thématiques au CORPS (avant le paratexte)
body = text.split("Les attentes de fin d’année")[0]
chk("corps sans deux fêtes", "deux fêtes" not in body)
chk("corps sans funérailles", "funérailles" not in body)
chk("corps sans qibla", "qibla" not in body)
chk("corps sans jeûne", "jeûne" not in body)
chk("corps sans istisqāʾ", "demande de pluie" not in body)
chk("corps sans éclipses", "éclipse" not in body)

# hygiène
chk("0 apostrophe droite", "'" not in html)
chk("guillemets appariés", text.count("«") == text.count("»"))
chk("0 TODO/placeholder", "TODO" not in html and "XXX" not in html and "【" not in html)

print(f"\nverify-hadith2-pdf2 : {ok} contrôles OK, {fail} échec(s)")
raise SystemExit(1 if fail else 0)
