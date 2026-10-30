# GARDE-DOUBLON — règle renforcée pour les append worklog (rédigée au tour R420)

## Événement fondateur (R420, 2026-10-30 ~17:07 +08:00)

Premier doublon de Task ID dans l'histoire du worklog : deux entrées R420
(459daca = instance parallèle « continue », c33fa10 = cron 17:07), apposées
pendant la même fenêtre d'ouverture, toutes deux poussées, fast-forward propre,
zéro perte. Le journal ne réécrit jamais son passé : le doublon RESTE et est
documenté ici + sera consigné dans l'entrée suivante (R421).

## Cause technique

La garde anti-doublon des scripts `append-rN.py` vérifiait
`content[-4000:]` — or une entrée récente peut dépasser 4 000 caractères :
son header `Task ID: R<N>` sort alors de la fenêtre et la garde passe à côté.

## Règle renforcée (obligatoire pour tout futur append)

```python
import re
# ... lecture de content ...
ids = re.findall(r"Task ID: R(\d+)", content)
if ids and int(ids[-1]) >= N:   # N = numéro de l'entrée à appender
    print("REFUS : une entrée >= R%d existe déjà (dernier = R%s)." % (N, ids[-1]))
    sys.exit(1)
```

- Scanner le fichier ENTIER pour le dernier `Task ID: R<N>`, pas un tail borné.
- Refuser si le dernier ID >= le numéro à appender.
- La règle h tient : le tail du worklog reste l'autorité de priorité — mais la
  détection de doublon, elle, doit balayer tout le fichier.
