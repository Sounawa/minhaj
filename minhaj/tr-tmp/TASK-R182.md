# TASK R182 — Traduction savante leçon 15814 (tajwid-5ep, leçon 12)

Exécute intégralement les instructions de /home/z/my-project/tr-tmp/CONVENTIONS-savant.md
(pipeline, style, typographie, terminologie, honnêteté philologique, interdictions).

## Fichiers à lire AVANT d'écrire (ordre strict)
1. tail -n 130 /home/z/my-project/worklog.md (état du corpus, entrées R175–R179)
2. /home/z/my-project/tr-tmp/15628.savant.html (leçon 9 — structure exacte à imiter)
3. /home/z/my-project/tr-tmp/15488.savant.html (R178 — table de vers bilingue du mathn —
   TA TABLE DU VERS TUḤFAT AL-AṬFĀL DOIT SUIVRE CETTE MÊME CONVENTION : premier hémistiche
   AR en cellule droite `<td dir="rtl" lang="ar">`, FR en cellule gauche)
4. /home/z/my-project/tr-tmp/15814.src.html (source AR — AUTORITÉ — leçon 12 : النون
   والميم المشددتين)
5. /home/z/my-project/tr-tmp/15814.gt.html (baseline GT — décodage seulement, jamais copier)

## Livrables (UNIQUEMENT ces deux fichiers)
- /home/z/my-project/tr-tmp/15814.savant.html — traduction savante FR complète (5 000–8 000 car)
- /home/z/my-project/tr-tmp/rnotes-15814.md — rapport de livraison

## Matière spécifique — la nūn et la mīm redoublées (ghunna obligatoire)
- Toute nūn ou mīm portant la shadda DOIT être nasillisée (ghunna) d'une nasalisation
  obligatoire de deux temps (ḥarakatayn), des fosses nasales (khayāshīm).
- Versets imprimés au manuel, à vérifier VERBATIM au cache : Hūd (11):48 ; al-Fatḥ (48):1-2 ;
  hadith avec le verset des Femmes (4):41 (qc['4']['ar'][40]).
- Hūd 11:48 : « قِيلَ يَا نُوحُ اهْبِطْ بِسَلَامٍ مِّنَّا وَبَرَكَاتٍ عَلَيْكَ وَعَلَى أُمَمٍ مِّمَّنْ
  مَعَكَ… » — passage type « وَعَلَى أُمَمٍ مِّمَّنْ مَعَكَ » : mīm redoublées consécutives,
  psalmodie transcrite au manuel « وَأُمَمِمْمِمْمَعَكَ » — chaque ghunna = deux temps.
  Vérifie le verbatim (le texte uthmani porte les shadda — détaille-les).
- al-Fatḥ 48:1-2 : répéter trois fois en fixant la ghunna de la nūn redoublée d'un mot et de
  la mīm redoublée d'un autre où le tanwīn est assimilé (idghām) à la mīm. Les mots sont perdus
  au scan (﴿﴾ vides) : IDENTIFIE-les depuis le texte du cache (cherche les shadda réelles du
  passage : « وَيُتِمَّ », « صِرَاطًا مُّسْتَقِيمًا » — le tanwīn de « ṣirātan » assimilé à la mīm de
  « mustaqīman » → mīm redoublée avec ghunna de deux temps…) et signale l'identification
  restaurée en N.d.T.
- Vers du mathn Tuḥfat al-Aṭfāl (l'énoncé : « أَسْتَدِلُّ عَلَى وُجُوبِ الْغُنَّةِ فِي كُلِّ نُونٍ
  وَمِيمٍ مُشَدَّدَتَيْنِ مِنْ تُحْفَةِ الْأَطْفَالِ ») : le vers est « وَغُنَّ مِيمًا ثُمَّ نُونًا
  شَدِّدَا » (« Et nasillisé la mīm puis la nūn redoublées »). Vérifie d'abord sa présence DANS LA
  SOURCE ; s'il est perdu au scan, restaure-le, rends-le en table bilingue et signale en N.d.T.
  Cherche dans le corpus (grep tr-tmp/*.savant.html avec « Tuḥfat » / tables de vers) si le mathn
  a déjà été traduit intégralement — réutilise le rendu exact déjà consacré si tu le trouves.
- Hadith ʿAbd Allāh b. Masʿūd : « اِقْرَأْ عَلَيَّ » — « Lis pour moi. — Sur toi, ô Messager de
  Dieu, et sur toi il a été descendu ? — Oui. — Je lus la sourate des Femmes jusqu'à ce que
  j'arrivasse à [4:41 « Comment sera-t-il quand Nous ferons venir de chaque communauté un
  témoin, et que Nous te ferons venir toi comme témoin de ceux-ci ? »]. Il dit : Cela te
  suffit. » — le scan coupe après « حَسْبُكَ الْ » (compléter « حَسْبُكَ الْآنَ ») ; le hadith est
  dans les deux Ṣaḥīḥ (al-Bukhārī, tafsīr ; Muslim, salāt al-musāfirīn) — suivre la référence
  imprimée du manuel si visible, sinon noter la complétion en N.d.T.
- L'iʿdād final (annonce de la leçon 13) : le chercher ; s'il est absent au scan, signaler
  honnêtement.

## QA final (obligatoire)
python3 /home/z/my-project/scripts-translate/qa-lesson.py /home/z/my-project/tr-tmp/15814.savant.html
→ doit PASSER (réparer et relancer jusqu'à réussite).

## Rappel
Ne modifie AUCUN fichier hors tr-tmp/15814.savant.html et tr-tmp/rnotes-15814.md.
Pas de git, pas de hand-set.py, pas de worklog.md, pas de backup.sh.
