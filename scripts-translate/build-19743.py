#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemblage du doc 19743 (rasm-wa-dabt-4ep, chapitre du bāʾ suite) — 5 fragments + sondes."""
import sys

FR = [f"/home/z/my-project/tr-tmp/fr19743_{i}.html" for i in range(1, 6)]
OUT = "/home/z/my-project/tr-tmp/19743.html"

parts = []
for p in FR:
    parts.append(open(p, encoding="utf-8").read().strip())
html = "\n".join(parts)

PROBES = [
    # structure / titres
    "le chapitre du bāʾ (suite)",
    "<dt></dt>",
    "la septième leçon",
    "ʿUmdat al-Bayān",
    "Idrīs al-Wadghīrī",
    "quatrième année de l’enseignement primaire ancestral",
    "Que je me familiarise avec le reste des mots élidées",
    # matn (7 bayts)
    "li-ʿibadatihi, la première, en Maryam",
    "et ġāyati qurubatin — sache",
    "en elle, ʿibadī",
    "puis ʿibadanā vient, en Ṣād",
    "maʿ aḥadin min — puis le wāw, dans ar-ribā",
    "à l’extrémité, fixe le duel — et abā",
    "comme abay, arbā et ʿuqbā — élis",
    "dans le reste de l’extrême final",
    "Le hāwī de ijtabahu, sans yāʾ, en Ṭāhā",
    "élis, sans yāʾ, son terme — ʿuqbahā",
    "le mumāl de adbari, élidée sans yāʾ",
    "une lettre de ribān, par son Rūm",
    # compréhension
    "Aṭ-ṭaraf",
    "lettre de la prolongation (ḥarf al-madd)",
    "du lexème «&nbsp;ʿibāda&nbsp;»",
    # taḥlīl 1
    "par précaution (iḥtirāz)",
    "ḥaḏf-signal vers la lecture",
    "est au thubūt — le maintien",
    # taḥlīl 2
    "toute alif de duel survenue à l’extrémité est fixe",
    "toute alif de duel survenue au milieu est élidée",
    "tukaḏḏibānī",
    "en sūrat ar-Raḥmān",
    "cernée par la restriction",
    "en sūrat al-Aḥzāb",
    "à l’alif maqṣūra",
    # taḥlīl 3
    "en sūrat Ṭāhā, à l’āya 119",
    "en sūrat Nūn",
    "élidée avec le yāʾ",
    "en sūrat aš-Šams",
    "à cause de la kasra du rāʾ",
    "son jugement fut établi dans la leçon précédente",
    # taḥlīl 4
    "origine wāwī",
    "l’attache (ilḥāq) de l’alif élidée au-dessus du wāw",
    "en sūrat ar-Rūm",
    "selon l’analogie (qiyās)",
    # istitimār
    "Abū ʿAmr ad-Dānī",
    "imraʾatāni",
    "raǧulāni",
    "saḥirāni",
    "udḫulā",
    "wa-qālā al-ḥamdu li-Llāh",
    "wa-qāla al-ḥamdu li-Llāh",
    "marsūm maṣāḥif ahl al-amṣār",
    "Taʿlīq al-Labīb",
    "ad-Durra aṣ-ṣaqīla",
    # iʿdād
    "kitābin",
    "ǧannatāni",
    "mabsūṭatāni",
    "at-talīyat",
    "at-tāʾibūn",
    # notes
    "Notes du traducteur",
    "Leçon 9 / 30",
    "l’unique élidée de tout le corpus",
    "trente et une occurrences du refrain",
    "ijtabāhu",
    "16&nbsp;:121",
    "20&nbsp;:122",
    "68&nbsp;:50",
    "91&nbsp;:15",
    "89&nbsp;:29",
    "38&nbsp;:41",
    "38&nbsp;:45",
    "33&nbsp;:40",
    "16&nbsp;:92",
    "27&nbsp;:15",
    "5&nbsp;:64",
    "52&nbsp;:49",
    "17&nbsp;:46",
    "2&nbsp;:275",
    "3&nbsp;:130",
    "4&nbsp;:161",
    "30&nbsp;:39",
    "douzième tour sans protocole triple",
    "m. 444&nbsp;H",
    "la translittération suit la récitation",
    "[exemple imprimé non porté par le document]",
    "[terme non porté par l’imprimé]",
    "lecture incertaine portée sans reconstruction",
]

failed = [p for p in PROBES if p not in html]
if failed:
    print("SONDES EN ÉCHEC (%d) :" % len(failed))
    for p in failed:
        print("  ✗", p)
    sys.exit(1)

n_lac = html.count("[exemple imprimé non porté par le document]")
n_g_o, n_g_c = html.count("«"), html.count("»")
straight = html.count("'")
print("Assemblage OK : %d car — %d sondes OK — lacunes: %d — guillemets %d/%d — apostrophes droites: %d"
      % (len(html), len(PROBES), n_lac, n_g_o, n_g_c, straight))

open(OUT, "w", encoding="utf-8").write(html)
print("écrit :", OUT)
