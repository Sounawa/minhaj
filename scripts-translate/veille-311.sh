#!/bin/bash
# veille-311.sh — canari de reprise faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) »)
# Règle (cx) R381 + (cy) R382 : à lancer À CHAQUE TOUR avant tout autre choix.
# Verdict EXÉCUTABLE seulement si le PDF (ou une page mère vivante) répond 200.
# Sortie : lignes "SONDE|statut|détail" — le worklog journalise le verdict.

URL311='https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/الفرائض-الثالثة-ثانوي/2B0631.PDF'
URLMERE='https://www.habous.gov.ma/%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D8%AC-%D8%A7%D9%84%D8%AA%D8%B9%D9%84%D9%8A%D9%85-%D8%A7%D9%84%D8%B9%D8%AA%D9%8A%D9%82-%D8%A7%D9%84%D8%B1%D8%A6%D9%8A%D8%B3%D9%8A%D8%A9/1700-%D8%A7%D9%84%D9%85%D8%B1%D8%AD%D9%84%D8%A9-%D8%A7%D9%84%D8%A3%D9%88%D9%84%D9%89/%D8%A7%D9%84%D9%81%D8%B1%D8%A7%D8%A6%D9%90%D8%B6/%D8%A7%D9%84%D9%81%D8%B1%D8%A7%D8%A6%D8%B6-%D8%A7%D9%84%D8%AB%D8%A7%D9%86%D9%88%D9%8A-%D8%A7%D9%84%D8%AB%D8%A7%D9%84%D8%AB-%D8%B9%D8%AA%D9%8A%D9%82'
CACHE=/home/z/my-project/content/ocr-cache/pdf-mut23h2v-311.json

verdict=INEXECUTABLE

echo "== CANARI 311 — $(date -u '+%Y-%m-%d %H:%M UTC') =="

# Sonde 1 : cache OCR
if [ -s "$CACHE" ]; then
  echo "CACHE|200|$(basename "$CACHE") présent ($(wc -c < "$CACHE") octets)"
  verdict=EXECUTABLE
else
  echo "CACHE|ABS|aucun cache OCR pour 311"
fi

# Sonde 2 : PDF direct
c2=$(curl -ksS -o /dev/null -w "%{http_code}" --max-time 25 "$URL311" 2>/dev/null)
echo "PDF|${c2}|2B0631.PDF"
[ "$c2" = "200" ] && verdict=EXECUTABLE

# Sonde 3 : page mère de la série (index de recherche, R382)
c3=$(curl -ksS -o /dev/null -w "%{http_code}" --max-time 25 "$URLMERE" 2>/dev/null)
echo "MERE|${c3}|page mère 1700-المرحلة-الأولى/الفرائض"
[ "$c3" = "200" ] && verdict=EXECUTABLE

# Sonde 4 : accueil du site (témoin de vie)
c4=$(curl -ksS -o /dev/null -w "%{http_code}" --max-time 20 "https://www.habous.gov.ma" 2>/dev/null)
echo "HOME|${c4}|accueil (témoin)"

echo "== VERDICT: $verdict =="
[ "$verdict" = "EXECUTABLE" ] && echo "ACTION: rasm disponible → reprendre la série farāʾiḍ (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu)" || echo "ACTION: tour de veille journalisé (règle cx), re-test au tour suivant"
