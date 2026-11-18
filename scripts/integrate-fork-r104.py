#!/usr/bin/env python3
"""Intégration fork-r104-sauvegarde → main (recalé R498) : les 12 leçons tafsir-3es uniques.
Règles : htmlFr copié si vide côté distant ; titleFr du portail (convention ligne avancée) préservé ;
registre hand += docIds absents. Zéro écrasement de contenu distant existant."""
import json, subprocess, sys

FORK = 'fork-r104-sauvegarde'
BOOK = 'content/books/tafsir-3es.json'
REG  = 'scripts-translate/savant-registry.json'

fork_book = json.loads(subprocess.run(['git','show',f'{FORK}:{BOOK}'],capture_output=True).stdout.decode('utf-8'))
cur_book  = json.load(open(BOOK,encoding='utf-8'))
fork_idx = {x['docId']: x for x in fork_book['lessons'] if isinstance(x.get('docId'),str)}
cur_idx  = {x['docId']: x for x in cur_book['lessons']  if isinstance(x.get('docId'),str)}

only_fork = json.load(open('tr-tmp/fork-only-ids.json'))
print(f"intégration de {len(only_fork)} leçons : {only_fork}")

copied = []
for did in only_fork:
    src, dst = fork_idx.get(did), cur_idx.get(did)
    if src is None or dst is None:
        print(f"  ⚠︎ {did} absent ({'fork' if src is None else 'distant'}) — passé"); continue
    if isinstance(dst.get('htmlFr'),str) and dst['htmlFr'].strip():
        print(f"  ⚠︎ {did} a déjà un htmlFr distant — NON touché"); continue
    if not isinstance(src.get('htmlFr'),str) or not src['htmlFr'].strip():
        print(f"  ⚠︎ {did} htmlFr fork vide — passé"); continue
    dst['htmlFr'] = src['htmlFr']
    if not (isinstance(dst.get('titleFr'),str) and dst['titleFr'].strip()) and isinstance(src.get('titleFr'),str):
        dst['titleFr'] = src['titleFr']
        print(f"  + {did} htmlFr {len(src['htmlFr'])} car + titleFr (distant vide)")
    else:
        print(f"  + {did} htmlFr {len(src['htmlFr'])} car (titleFr portail conservé)")
    copied.append(did)

with open(BOOK,'w',encoding='utf-8') as f:
    json.dump(cur_book, f, ensure_ascii=False, indent=2)
    f.write('\n')

reg = json.load(open(REG,encoding='utf-8'))
added = [d for d in copied if d not in set(reg['hand'])]
reg['hand'].extend(added)
with open(REG,'w',encoding='utf-8') as f:
    json.dump(reg, f, ensure_ascii=False, indent=2)
    f.write('\n')

fr_count = sum(1 for x in cur_book['lessons'] if isinstance(x.get('htmlFr'),str) and x['htmlFr'].strip())
print(f"RÉSULTAT : {len(copied)} leçons intégrées | registre hand {1010}→{len(reg['hand'])} | tafsir-3es htmlFr non-vides : {fr_count}/43")
print("OK" if len(copied)==len(only_fork) else "INCOMPLET")
sys.exit(0 if len(copied)==len(only_fork) else 1)
