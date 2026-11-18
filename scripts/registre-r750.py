#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R750 — inscription au registre savant des 6 leçons hadith-tanawi-3
transcrites par la série R (IA-1) mais jamais inscrites au registre
« hand » (le flux hand-set.py datait des vagues traduction/typo) :

- pdf-mut23h2n-10  Les règles du témoignage (šahāda)            [R736 réconciliation]
- pdf-mut23h2n-11  La vente du gage à l'échéance (ġalq al-rahn) [R736 réconciliation]
- pdf-mut23h2n-12  La mise en gage des fruits et des animaux    [R737]
- pdf-mut23h2n-13  La responsabilité du gage (ḏamān al-rahn)    [R739]
- pdf-mut23h2n-14  La justice en matière d'abus et de responsabilité [R741]
- pdf-mut23h2n-15  La justice en matière de mise en valeur des terres [R743]

Chaque livraison a passé la QA double porte (lectures VLM, arbitrages
consignés, vérifications) et est EN LIGNE depuis les tours respectifs ;
le build les comptait déjà comme « traduits » mais « en attente du cap
savant » — les 6 documents du compteur d'accueil. L'IA-1, auteur de la
série R, inscrit ces ids dans le registre scripts-translate/
savant-registry.json (fait foi) avec le verrou de hand-set.py ; le miroir
racine est resynchronisé par le build --publier . (publication IA-1).
Aucun htmlFr n'est touché — inscription registre seule.
"""
import json, os, time

REGISTRY = '/home/z/my-project/minhaj-repo/scripts-translate/savant-registry.json'
LOCK = REGISTRY + '.lock'

IDS = ['pdf-mut23h2n-10', 'pdf-mut23h2n-11', 'pdf-mut23h2n-12',
       'pdf-mut23h2n-13', 'pdf-mut23h2n-14', 'pdf-mut23h2n-15']


def purge_stale_lock():
    try:
        age = time.time() - os.path.getmtime(LOCK)
        if age > 90:
            os.rmdir(LOCK)
            print(f'verrou périmé ({age:.0f} s) purgé')
    except OSError:
        pass


def acquire_lock():
    purge_stale_lock()
    for _ in range(40):
        try:
            os.mkdir(LOCK)
            return
        except OSError:
            time.sleep(0.25)
    raise RuntimeError('verrou registre occupé après 10 s')


with open(REGISTRY, encoding='utf-8') as fh:
    reg = json.load(fh)
avant = set(reg.get('hand', [])) | set(reg.get('llm', {}))
deja = [i for i in IDS if i in avant]
if deja:
    print('déjà inscrits (rien de fait) :', deja)
    raise SystemExit(1)

acquire_lock()
try:
    with open(REGISTRY, encoding='utf-8') as fh:
        reg = json.load(fh)  # relecture-fusion de l'état disque le plus récent
    reg.setdefault('hand', [])
    reg.setdefault('llm', {})
    ajoutes = []
    for i in IDS:
        if i not in reg['hand'] and i not in reg['llm']:
            reg['hand'].append(i)
            ajoutes.append(i)
    tmp = REGISTRY + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(reg, fh, indent=2, ensure_ascii=False)
        fh.write('\n')
    os.replace(tmp, REGISTRY)
finally:
    try:
        os.rmdir(LOCK)
    except OSError:
        pass

total = len(reg['hand']) + len(reg['llm'])
print('inscrits :', ajoutes)
print('registre hand :', len(reg['hand']), '| llm :', len(reg['llm']), '| total :', total)
