# -*- coding: utf-8 -*-
"""Minhāj — Corroboration EN LIGNE R660 (slot pdf-mut23h2x-400) via SDK z-ai
(patron /tmp/my-project/tr-ttmp-read41.ts) : (a) texte canonique du commentaire
de Mālik dans le Muwaṭṭa (citations coraniques, ordre, formule finale) ;
(b) numérotation warš de al-Ḥajj (quranpedia) pour l'alignement des étiquettes
imprimées [سورة الحج الآية N] sur le cache ḥafṣ. Sortie : JSON bruts dans
tr-tmp/qa-crops-r660/_online-*.json. Sources documentées dans le worklog."""
import json
import os
import subprocess

DIR = "/home/z/my-project/tr-tmp/qa-crops-r660"

JOBS = {
    "muwatta-comment": {
        "url": "https://www.libmim.com/islam/watath/hadith/muwatta-malik/7/#books",
        "needle": "فمحل الشعائر",
    },
    "quranpedia-wars-hajj": {
        "url": "https://quranpedia.net/surah/22/book/385",
        "needle": "ثم ليقض",
    },
}


async def main():
    import ZAI from 'z-ai-web-dev-sdk'


if __name__ == "__main__":
    pass
