#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R92 — Append de l'entrée worklog du tour (faraid-tanawi-3, leçon 310)."""

ENTRY = """\
---
Task ID: R92
Agent: Z.ai Code (agent principal — TOUR DE PRODUCTION AUTONOME cron 490480, trace 1a192862dcae2069-cron-agent-loop-202611010716)
Task: 14ᵉ exécution consécutive du canal (0253→0707) — tour de production sur la priorité R91 : faraid-tanawi-3 manẓūma (310-313) — leçon savante 310 (ḥaǧb 1) via OCR + scans, QA navigateur, backup, worklog.

Work Log:
- **Canal / moteur** : TICK 0707 consigné dans tr-tmp/cron-alive.log (+ rattrapage 0552, déjà régularisé par une session parallèle) ; superviseur v4 VIVANT (PID 1359) — pas de relance nécessaire.
- **Recadrage GARDE-DOUBLON (9ᵉ occurrence)** : le résumé de reprise de session invoquait ENCORE R464→R465 / tafsir-5ep leçons 717-718 Isrāʾ / isra-l9-l10-readable / verify-716 / pdf-mut23h3c-716 / commit 17226d5 / PID 16546 / slot 708+leçon# / « tafsir-5ep 69/122 » — VÉRITÉ TERRAIN : AUCUN de ces objets n'existe (ls/glob/git vérifiés) ; HEAD réel 1129da1 = R91, dernier Task ID réel R91, registre 529/950. Le tail réel a dicté la priorité : faraid-tanawi-3 manẓūma 310-313. Fantôme post-compression à sa 9ᵉ récidive documentée — la vérification physique (tail worklog + git log + ls) demeure la 1ʳᵉ étape obligatoire du tour.
- **Sources 310-313** : leçons pdfOnly (html vide, scans habous) ; **les 5 pdfUrl 310-314 répondent 404** (site restructuré, constat R91 confirmé par sonde urllib sur les 5 URLs ; OCR 311-313 tentés via ocr-one.py → HTTPError 404, logs tr-tmp/ocr-311/312/313.log). SEULE la leçon 310 dispose d'une source : PDF local tr-tmp/ft3-310.pdf (téléchargé 15-10, 6 pages) + cache OCR content/ocr-cache/pdf-mut23h2v-310.json. Tour à UNE leçon (écart au rythme 2/tour, justifié par l'indisponibilité des sources 311-313 — nul contenu inventé).
- **Transcription manẓūma (critique exactitude)** : l'OCR tesseract détruit les vers (fonte ornée) — relecture VISUELLE des scans : rendu pdftoppm 400 dpi + recadrages par colonnes (ṣadr/ʿaǧuz) + zooms ×3-4 sur les mots douteux. Titre du manuel fixé par zoom : « فقه الحجب (1) : مفهوم وتصور » (illusion « الصميم » dissipée : points sous ح/ج/ب + šadda de تصوُّر). **25 bayts transcrits** (5+5+6+5+4 sur les 5 pages de contenu ; p16 décorative, 3,2 % non-blanc). Doctrine malikite vérifiée cohérente vers par vers : البنت jamais exclue (نقص/تعصيب seulement) ; بنت الابن exclue par ابن وابنتين ارفعا (règle malikite distinctive du تنقيض بالبنتين) sauf ابن معها ; الأقرب تنقل الأبعد من النصف إلى السدس ; الأخت محجوبة بالجد sauf الأكدرية (زوج وجد أم والأخت معهم في العدد) ; الزوجان sans حجاب عن الربع/الثمن.
- **Termes imprimés douteux rendus tels quels (gloses assumées documentées, rien d'inventé)** : « بدون مَيْن » (v.5) → « sans réserve » (terme ainsi imprimé dans le manuel et repris tel quel par un enseignant citant la manẓūma en ligne ; sens attendu « sans منع ») ; « صَنَبٌ » (v.2) → « le dernier venu de sa descendance » (racine ṣ-n-b « suivre/queue ») ; « يُعَصِّبُ بَانِهَا » (v.12) → « [son frère] la rend dévolutive » (sujet elided, entre crochets) ; « من صِفْهِ وفوق من حجبا » (v.7) et « لأمّه معها افتراق لزما » (v.21) rendus littéralement. Le vers = la fonte du manuel fait foi, zéro correction silencieuse de la manẓūma.
- **savant(faraid-tanawi-3/pdf-mut23h2v-310)** — leçon 1, la science de l'exclusion successorale (ḥaǧb) (1) : gabarit = leçon 335 (seule leçon HAND du book) — h1 = titleFr, intro conventionnelle (« Leçon sur …, matière Farāʾiḍ — la manẓūma al-Rasmūkiyya avec le commentaire Īḍāḥ al-asrār al-maṣūna, pour les élèves de la troisième année de l'enseignement secondaire traditionnel (ʿatīq) — la première leçon : … »), objectifs ×3, ouverture (prose du manuel), analyse en 3 points (البنت وبنت الابن / الأخت الشقيقة والأخت لأب / الزوجين) avec les 25 bayts traduits vers par vers en français (zéro caractère arabe, termes du corpus : abolition/isqāṭ, participation/šarika, diminution/naqṣ, dévolution résiduelle/taʿṣīb, ʿawl, tašqīq, šādhdha), activités rendues (2 blocs numérotés, 9 cas d'exercice, sous-points أ/ب), 5 tableaux d'activités à cellules vides rendus en descriptions entre crochets (convention 335 : « [tableau à compléter par l'élève — …] »). titleFr conservé tel quel (GT exact, non GT-isme). QA 0 arabe, 35 guillemets appariés.
- **Outils du tour** : verify-r92-quran.py (0 arabe + 0 apostrophe droite + guillemets appariés + 0 verset-image attendu/trouvé + 48 assertions ciblées + résidus — **PASS**, normalisation U+202F des assertions pour suivre l'auto-fix qa-lesson) ; qa-lesson.py PASS (auto-fix NNBSP + apostrophes, 7 821 car) ; finalize-r92.py (htmlFr 0 → 7 820 car + registre hand += pdf-mut23h2v-310) ; crosscheck Muwaṭṭaʾ N/A (aucune référence hadith dans la leçon — manẓūma pure) ; pas de citation coranique dans 310 (pas de cross-check cache requis).
- **QA navigateur (agent-browser)** : route #/livre/faraid-tanawi-3/pdf-mut23h2v-310 — desktop 1280 (h1 « La science de l'exclusion successorale (ḥaǧb) (1) », badge « Traduction savante », scrollWidth 1280 = **0 overflow**, 0 erreur page, console = messages dev HMR uniquement) ; mobile 390 (h1, **0 overflow**) ; captures tr-tmp/qa-R92-310-1280.png / qa-R92-310-390.png (contrôle non-à-blanc PIL : 3,9 % / 8,1 %).
- **Git** : commit local (faraid-tanawi-3.json + registre + tr-tmp 310 + OCR cache si non suivi + outils + captures) ; backup.sh PASS ; toujours aucun remote configuré (push impossible sans token — constat R83-R91 inchangé).

Stage Summary:
- **État** : registre **530/950** (+1 ce tour) — faraid-tanawi-3 **2/27 savant** (335 + 310). 48 livres complets ; hadith-1es 32/32 savant inchangé.
- **Décisions clés** : (a) 9ᵉ recadrage GARDE-DOUBLON — le fantôme R465/tafsir-717-718 a survécu à une nouvelle compression de session ; seul le tail réel fait foi ; (b) première leçon manẓūma rendue savante : pipeline OCR + lecture visuelle des scans par colonnes/zooms, la transcription des vers prime sur l'OCR défaillant sur la fonte ornée ; (c) rendu 100 % français, vers traduits par bayt, tables d'activités vides en descriptions entre crochets (gabarit 335) ; (d) tour à une leçon : 311-313 sans source (404) — aucune invention.
- **Risques** : (a) relecture par recadrages (pas de relecture visuelle page entière intégrale) — les 4 termes douteux sont rendus par gloses assumées, documentées ; si les scans du manuel renaissent ailleurs, re-vérifier « بدون مَيْن », « صَنَبٌ », « يُعَصِّبُ بَانِهَا », « لأمّه معها افتراق لزما » ; (b) 311-336 bloquées jusqu'à trouver les PDF du manuel الفرائض الثالثة ثانوي (miroir scribd repéré — accès non trivial) ; (c) compteur lecteur et badge à surveiller sur les prochaines leçons pdfOnly du book.
- **Priorités suivantes** : (1) miroirs des PDF 311-336 de faraid-tanawi-3 puis reprise du rythme (311 فقه الحجب (2), 312 taʿṣīb, 313 ʿawl) ; (2) poursuite des séries ouvertes — tafsir-2es (7/37), tafsir-3es (6/43), fiqh-3es (2/29), rasm-wa-dabt-5ep (2/31) ; (3) nettoyage des 3 erreurs TS préexistantes ; (4) étendre l'audit labels-aux-images à hadith-1ep/12583 (même manuel).
"""

def main() -> None:
    path = "/home/z/my-project/worklog.md"
    with open(path, "a", encoding="utf-8") as f:
        f.write(ENTRY)
    print("worklog.md : entrée R92 apposée")


if __name__ == "__main__":
    main()
