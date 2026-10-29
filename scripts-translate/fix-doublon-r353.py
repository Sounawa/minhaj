# -*- coding: utf-8 -*-
"""fix-doublon-r353.py — supprime la seconde occurrence de l'entrée R353 (doublon d'append accidentel)."""
path = '/home/z/my-project/worklog.md'
lines = open(path, encoding='utf-8').read().split('\n')
# occurrences de la ligne exacte 'Task ID: R353'
idx = [i for i, l in enumerate(lines) if l.strip() == 'Task ID: R353']
assert len(idx) == 2, f'attendu 2 occurrences, trouvé {len(idx)} : {idx}'
start = idx[1] - 1  # la ligne '---' qui précède le doublon
assert lines[start].strip() == '---', f'ligne {start} != --- : {lines[start]!r}'
kept = lines[:start]
while kept and kept[-1].strip() == '':
    kept.pop()
open(path, 'w', encoding='utf-8').write('\n'.join(kept) + '\n')
print(f'OK — doublon supprimé (lignes {start+1}..{len(lines)}), worklog = {len(kept)} lignes')
occ = open(path, encoding='utf-8').read().count('Task ID: R353')
print(f'occurrences R353 restantes : {occ}')
