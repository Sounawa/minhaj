# Minhāj — Conventions de traduction savante (référence subagents, R180+)

## Pipeline (ordre strict)
1. Lire `tail -n 130 /home/z/my-project/worklog.md` (entrées récentes — état du corpus).
2. Lire la source AR (AUTORITÉ) : `tr-tmp/<docId>.src.html` (versets en images → perdus au scan → RESTAURER du cache, marquer).
3. Baseline GT : `tr-tmp/<docId>.gt.html` — AIDE AU DÉCODAGE SEULEMENT, ne jamais copier.
4. Vérifier VERBATIM les versets contre le cache :
   ```bash
   python3 -c "
   import json
   qc = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))
   s = qc['67']            # n° de sourate en chaîne
   print(s['ar'][0], '|', s['fr'][0])
   "
   ```
   Structure : `qc[str(n°sourate)]['ar'][k] = [n°verset, texte uthmani]` ; `['fr'][k] = [n°, Hamidullah]`.
   Au verset 1 (sauf sourates 1 et 9) la basmala peut être préfixée — la retirer en citant.
5. Écrire `tr-tmp/<docId>.savant.html` (traduction savante, 5 000–8 000 car).
6. QA : `python3 scripts-translate/qa-lesson.py tr-tmp/<docId>.savant.html` — doit PASSER
   (0 caractère arabe résiduel — seule la ligature ﷺ est exemptée ; « » appariés ; balises
   appariées ; apostrophes U+2019 ; l'auto-fix gère les espaces fines U+202F).
   Réparer et relancer jusqu'à réussite.
7. Rapport : `tr-tmp/rnotes-<docId>.md` (taille source, chaque verset vérifié réf. + verbatim
   + remarques, restaurations, anomalies OCR honnêtes, taille traduite, QA).
8. Retour final : résumé concis.

## Style (imiter tr-tmp/15628.savant.html — R179)
- `<h1>` titre savant « Tajwīd : … ».
- `<p>` intro : « <N>-ième leçon de tajwīd du livre « Applications sur le Naẓm Tuḥfat al-aṭfāl »
  d'al-Jamzūrī, pour les élèves de la cinquième année de l'enseignement primaire traditionnel.
  Cette leçon porte des applications sur … ».
- `<ul>` objectifs numérotés (1. 2. 3.).
- `<h2>` « J'affermis mes apprentissages » + `<ul>`.
- `<h2>` « J'applique et je psalmodie » avec `<h4>` « 1. J'écoute et je prête l'oreille, avec
  recueillement, aux versets coraniques suivants » puis « 2. Je m'exerce à la belle récitation
  à travers ce qui suit ».
- `<h2>` « Je prends guide et exemple » (hadith).
- `<h2>` « J'édifie ma personne » (édification).
- « Notes du traducteur » (N.d.T.) en fin de document.
- Versets en image : `[verset reproduit en image dans le manuel : « … » — la sourate (n) : v — vérifié verbatim]`.
- Tables de vers bilingues (mathn) : convention R170/R178 — premier hémistiche AR en cellule
  droite (`<td dir="rtl" lang="ar">`), FR en cellule gauche (voir tr-tmp/15488.savant.html).

## Typographie
- Guillemets « » ; apostrophe U+2019 ; toute translittération en `<em>`.
- Références coraniques « — la sourate (n) : v — » ; hadith avec référence [collection, chapitre, n°].

## Terminologie figée (R0–R179)
- ghunna = nasalisation ; idghām = assimilation ; ikhfāʾ = occultation ; iẓhār = manifestation.
- « mīm quiescente », « nūn quiescente », « tanwīn », « hamza de liaison », « madd » = allongement,
  « ṣila » = liaison, « waqf » = arrêt, « naql » = transfert de voyelle (suivre tr-tmp/18384.savant.html),
  « mīm du pluriel » = mīm al-jamʿ, « iltiqāʾ as-sākinayn » = la rencontre des deux quiescentes.

## Honnêteté philologique
- Tout élément perdu au scan (images, OCR corrompu) : RESTAURER du cache ou du savoir et SIGNALER en N.d.T.
- Référence douteuse : double lecture honnête.
- Hamidullah = contrôle de sens seulement — on traduit le manuel, souverain.

## Interdictions absolues (subagents)
Pas de `hand-set.py` ; pas de `savant-registry.json` ; aucun git ; pas de `worklog.md` ;
pas de `backup.sh` ; ne pas toucher aux fichiers d'autres leçons. L'intégration sérialisée
(registre, git, worklog) est faite par l'agent principal uniquement.
