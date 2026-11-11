# TASK R180 — Traduction savante leçon 15741 (tajwid-5ep, leçon 10)

Exécute intégralement les instructions de /home/z/my-project/tr-tmp/CONVENTIONS-savant.md
(pipeline, style, typographie, terminologie, honnêteté philologique, interdictions).

## Fichiers à lire AVANT d'écrire (ordre strict)
1. tail -n 130 /home/z/my-project/worklog.md (état du corpus, entrées R175–R179)
2. /home/z/my-project/tr-tmp/15628.savant.html (leçon 9 — structure exacte à imiter)
3. /home/z/my-project/tr-tmp/18384.savant.html (tajwid-2es — terminologie « mīm du pluriel », naql)
4. /home/z/my-project/tr-tmp/15741.src.html (source AR — AUTORITÉ — leçon 10 : أحكام ميم الجمع)
5. /home/z/my-project/tr-tmp/15741.gt.html (baseline GT — décodage seulement, jamais copier)

## Livrables (UNIQUEMENT ces deux fichiers)
- /home/z/my-project/tr-tmp/15741.savant.html — traduction savante FR complète (5 000–8 000 car)
- /home/z/my-project/tr-tmp/rnotes-15741.md — rapport de livraison

## Matière spécifique — la mīm du pluriel (mīm al-jamʿ) chez Warsh
- Versets imprimés au manuel, à vérifier VERBATIM au cache (scripts-translate/quran-cache.json) :
  la Royauté (67):1-2 ; la Vache (2):182 ; al-Ḥijr (15):22.
- Cas type : « لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًا » (67:2) — mīm du pluriel + hamza de liaison de
  « ayyu » → Warsh : ḍamma + wāw de liaison (2 mesures), lu « li-yabluwakumū ayyukum ».
  Détaille l'analyse des trois passages (mīm du pluriel réelles et leurs états : ḍamma+liaison /
  ḍamma / sukūn), en rendant compte honnêtement du texte de contrôle (double lecture si divergence).
- Énoncé imprimé « فورش من طريق الأزرق » (OCR approximatif) = « عن ورش من طريق الأزرق » — traduire
  « selon la lecture de Warsh, par la voie d'al-Azraq », signaler l'anomalie en N.d.T.
- Hadith Jābir (Ibn Māja, iqāmat aṣ-ṣalāt) : « إِنَّ مِنْ أَحْسَنِ النَّاسِ صَوْتًا بِالْقُرْآنِ الَّذِي
  إِذَا سَمِعْتُمُوهُ يَقْرَأُ حَسِبْتُمُوهُ يَخْشَى اللَّهَ » — traduire avec référence (le scan coupe
  après « وَ » — compléter honnêtement, signaler en N.d.T.).
- Les ﴿﴾ vides de la source (mots d'exemple perdus) : RESTAURER du cache (« لِيَبْلُوَكُمْ »…) et
  signaler en N.d.T.
- L'iʿdād final (annonce de la leçon 11 : la mīm originale quiescente devant la hamza) : le chercher ;
  la leçon 9 (15628, livrée) annonçait cette matière — assurer la continuité de registre.

## QA final (obligatoire)
python3 /home/z/my-project/scripts-translate/qa-lesson.py /home/z/my-project/tr-tmp/15741.savant.html
→ doit PASSER (réparer et relancer jusqu'à réussite).

## Rappel
Ne modifie AUCUN fichier hors tr-tmp/15741.savant.html et tr-tmp/rnotes-15741.md.
Pas de git, pas de hand-set.py, pas de worklog.md, pas de backup.sh.
