#!/usr/bin/env bash
# R634 — lectures VLM batch leçon 393 (pages 31-38 + badges), méthode r625-r632
cd /home/z/my-project
mkdir -p tr-tmp/r634
FULLP="Page d'un manuel arabe de hadith, leçon « أنواع الإحرام » (les formes de l'iḥrām). Transcris EXACTEMENT tout le texte imprimé visible, de haut en bas, en arabe, diacritiques inclus quand lisibles. Les textes encadrés portent un badge numéroté (chiffre dans un disque) : commence chaque encadré par « BADGE <numéro lu> : » puis transcris son contenu intégral. Marque toute zone illisible par [ILLISIBLE]. Transcris SEULEMENT ce qui est visible — ne complète jamais de mémoire. Aucun commentaire, aucune traduction."
NUMSP="Voici un empilement vertical de recadrages 900 dpi de badges numérotés (chiffre dans un disque) d'un manuel arabe. Pour CHAQUE badge, de haut en bas, transcris le numéro EXACT chiffre par chiffre tel qu'imprimé (les glyphes imprimés font foi — l'OCR texte du manuel inverse parfois l'ordre, ignore ce risque : lis l'image). Format strict : BADGE_1: <numéro> puis une ligne vide entre chaque. Aucun commentaire."

for p in 031 032 033 034 035 036 037 038; do
  f="tr-tmp/r634/read-p${p}-full.txt"
  if [ ! -s "$f" ]; then
    echo "== page $p =="
    timeout 180 z-ai vision -p "$FULLP" -i "tr-tmp/qa-crops-r626b/p${p}-full-200.png" -o "tr-tmp/r634/tmp-vision.json" >/dev/null 2>&1
    python3 -c "
import json,sys
try:
    d=json.load(open('tr-tmp/r634/tmp-vision.json'))
    print(d['choices'][0]['message']['content'])
except Exception as e:
    print('ERREUR_LECTURE',e)" > "$f"
  fi
done

for p in 031 032 034 035 036 037 038; do
  f="tr-tmp/r634/read-p${p}-nums.txt"
  if [ ! -s "$f" ]; then
    echo "== nums $p =="
    timeout 180 z-ai vision -p "$NUMSP" -i "tr-tmp/qa-crops-r626b/p${p}-nums-stack.png" -o "tr-tmp/r634/tmp-vision.json" >/dev/null 2>&1
    python3 -c "
import json,sys
try:
    d=json.load(open('tr-tmp/r634/tmp-vision.json'))
    print(d['choices'][0]['message']['content'])
except Exception as e:
    print('ERREUR_LECTURE',e)" > "$f"
  fi
done
echo "lectures batch terminées"
