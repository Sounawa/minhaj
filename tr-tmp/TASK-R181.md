# TASK R181 — Traduction savante leçon 15797 (tajwid-5ep, leçon 11)

Exécute intégralement les instructions de /home/z/my-project/tr-tmp/CONVENTIONS-savant.md
(pipeline, style, typographie, terminologie, honnêteté philologique, interdictions).

## Fichiers à lire AVANT d'écrire (ordre strict)
1. tail -n 130 /home/z/my-project/worklog.md (état du corpus, entrées R175–R179)
2. /home/z/my-project/tr-tmp/15628.savant.html (leçon 9 — structure exacte à imiter)
3. /home/z/my-project/tr-tmp/18384.savant.html (tajwid-2es — règles du naql / transfert de
   voyelle — TERMINOLOGIE DIRECTEMENT PERTINENTE : « transfert de voyelle », « mīm du pluriel »,
   « hamza de liaison »)
4. /home/z/my-project/tr-tmp/15797.src.html (source AR — AUTORITÉ — leçon 11 : حكم الميم
   الأصلية الساكنة قبل الهمز)
5. /home/z/my-project/tr-tmp/15797.gt.html (baseline GT — décodage seulement, jamais copier)

## Livrables (UNIQUEMENT ces deux fichiers)
- /home/z/my-project/tr-tmp/15797.savant.html — traduction savante FR complète (5 000–8 000 car)
- /home/z/my-project/tr-tmp/rnotes-15797.md — rapport de livraison

## Matière spécifique — la mīm originale quiescente devant la hamza (lecture de Warsh)
- La mīm originale (radicale du mot, DISTINCTE de la mīm du pluriel de la leçon 10) quiescente
  suivie d'une hamza de liaison (hamzat al-waṣl) : pour éviter la rencontre des deux quiescentes
  (iltiqāʾ as-sākinayn), on TRANSFÈRE (naql) la voyelle de la hamza à la mīm.
- Versets imprimés au manuel, à vérifier VERBATIM au cache : an-Nūr (24):48 ; az-Zukhruf (43):79 ;
  Āl ʿImrān (3):1 ; al-ʿAnkabūt (29):1.
- Cas canoniques (vérifie chaque forme au texte uthmani du cache, détaille l'analyse) :
  1. 24:48 « أَمِ ارْتَابُوا » (source : « أَمِرْتَابُوا ») — kasra transférée : lu « a-mir-tābū ».
  2. 43:79 « أَمْ أَبْرَمُوا أَمْرًا » — fatḥa transférée : lu « a-mab-ramū » (source : « أَمَبْرَمُوا »).
  3. 3:1 « الم ﴿اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ…﴾ » — mīm de « الم » jointe au nom de majesté :
     fatḥa devant le lām divin : lu « alif-lām-mi-mallāh » (source : « أَلِفْ لَامْمِيمَلَّاهُ »).
  4. 29:1 « الم ﴿أَحَسِبَ النَّاسُ…﴾ » — jointe à « أَحَسِبَ » : lu « alif-lām-mi-ma-hasaba ».
- L'énoncé : « فَيَجِبُ كَسْرُ الْمِيمِ لِالْتِقَاءِ السَّاكِنَيْنِ » — « la mīm doit prendre la kasra
  en raison de la rencontre des deux quiescentes ».
- Distinction mīm du pluriel (leçon 10) / mīm originale (leçon 11) : explicite-la dans
  « J'affermis mes apprentissages » comme le fait l'énoncé.
- Deux états de la mīm originale quiescente : (a) devant hamza de liaison → transfert de voyelle ;
  (b) sinon → manifestation (iẓhār) ordinaire.
- Les ﴿﴾ vides de la source : RESTAURER les mots d'exemple du cache (« أَمِ ارْتَابُوا »,
  « أَمْ أَبْرَمُوا », « الم », « اللَّهُ », « أَحَسِبَ »…) et signaler chaque restauration en N.d.T.
- Cherche aussi : la section « أهتدي وأقتدي » (hadith/édification — si absente ou vide au scan,
  signaler honnêtement en N.d.T.) et l'iʿdād final (annonce de la leçon 12 : la nūn et la mīm
  redoublées).

## QA final (obligatoire)
python3 /home/z/my-project/scripts-translate/qa-lesson.py /home/z/my-project/tr-tmp/15797.savant.html
→ doit PASSER (réparer et relancer jusqu'à réussite).

## Rappel
Ne modifie AUCUN fichier hors tr-tmp/15797.savant.html et tr-tmp/rnotes-15797.md.
Pas de git, pas de hand-set.py, pas de worklog.md, pas de backup.sh.
