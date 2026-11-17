# Commentaires pédagogiques — mission « leçon + commentaire »

> Mission spéciale confiée par l’utilisateur (17 nov. 2026) : un travail
> d’**explication / commentaire** de chaque leçon — pas de traduction.
> **Rien du travail existant n’est effacé** : la transcription arabe et la
> traduction savante restent exactement en place ; le commentaire s’ajoute
> sous la leçon. À la fin du projet, l’affichage pourra être réglé à volonté
> (leçon seule / commentaire seul / les deux) grâce au drapeau de build
> `--mode-commentaires` — sans toucher aux données.

## 1. Où vivent les données

- `content/commentaires/<slug>.json` — **un fichier par livre**, slug =
  nom du livre sans `.json` (ex. `hadith-3es.json`).
- **JAMAIS toucher à `content/books/*.json`** pour poser un commentaire :
  le lien se fait par `docId`, au build, en lecture seule.

## 2. Schéma d’un fichier

```json
{
  "livre": "hadith-3es",
  "noteLivre": "…(optionnel)…",
  "commentaires": {
    "<docId>": {
      "auteur": "IA-1, tour R7xx",
      "resume": "2-3 phrases : ce que la leçon exige de retenir.",
      "explication": ["paragraphe 1", "paragraphe 2", "…"],
      "points": ["point à retenir 1", "…"],
      "vocabulaire": [
        {"ar": "الأَضْحِيَّة", "translit": "aḍḥiyya", "fr": "…"}
      ],
      "avertissement": "rappel optionnel que le manuel fait foi"
    }
  }
}
```

- Clé = le `docId` exact de la leçon dans `content/books/<slug>.json`.
- Introduction du livre : clé `"introduction"` (ou le `docId` de l’intro).
- Tous les champs sont optionnels mais **au moins un** champ de contenu est
  requis (resume / explication / points / vocabulaire) — sinon l’entrée est
  ignorée avec avertissement au build.
- `explication` accepte une liste de paragraphes (recommandé) ou une chaîne.

## 3. Règles de rédaction (qualité commune, non négociable)

1. **Ancrage** : le commentaire explique LA leçon telle qu’elle est —
   rubriques du manuel (ahdāf ad-dars, tamhīd, textes, tarjamat ar-rāwī,
   ach-charḥ, istiḫlāṣ al-muḍāmīn, fiqh al-ḥadīth…), textes cités, gloses.
   Lire d’abord la leçon complète (htmlFr) avant d’écrire.
2. **Aucune invention** : ne jamais ajouter un hadith, un numéro, une page,
   une attribution qui n’est pas dans la leçon. Une incertitude reste
   incertaine, consignée comme telle.
3. **Typographie FR** : apostrophe typographique ’, guillemets « » appariés,
   espace fine insécable (U+202F) avant `; : ! ? »` et après `«` ;
   aucun caractère arabe hors des champs `ar` du vocabulaire et des citations
   entre parenthèses — le build les échappe dans les balises RTL prévues.
4. **Translittération** : convention du corpus (ʾ U+02BE / ʿ U+02BF,
   ḥ, ḏ, ṯ, š, ġ, ā ī ū) — reprendre les formes exactes du texte de la leçon.
5. **Le commentaire ne corrige jamais la leçon** : si un défaut est repéré
   dans content/books (zone d’une autre IA), le consigner dans son journal ;
   le propriétaire corrige.
6. **Ton** : pédagogique, précis, sans paraphrase lourde — dire où va
   l’essentiel et pourquoi. Longueur cible : 300-600 mots par leçon.

## 4. Rendu au site (automatique)

- Page leçon : section « Commentaire pédagogique » (h2 + شرح الدرس) sous la
  leçon ; puce `✧ comm.` dans les sommaires ; compteur par livre sur la page
  du livre ; zone d’avancement repliable sur l’accueil ; inclus dans la
  version hors-ligne.
- Drapeaux de build : `--mode-commentaires les-deux|lecon|commentaire`
  (défaut `les-deux`). Vérification : `python3 scripts/build-site.py` puis
  QA habituelle.

## 5. État au 17 nov. 2026

- Pilote : `hadith-3es.json` — leçons pdf-mut23h2x-413 et pdf-mut23h2x-414
  (leçons 24-25 du manuel, أحكام الأضحية). Objectif : valider schéma et ton
  avant de dérouler le corpus (1 782 documents).
