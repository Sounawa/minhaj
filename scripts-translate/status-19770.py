#!/usr/bin/env python3
"""R338 status: book lessons + registry, decide next docId."""
import json, sys

BASE = '/home/z/my-project'
book = json.load(open(f'{BASE}/content/books/rasm-wa-dabt-4ep.json'))
print('top keys:', list(book.keys()))
lessons = book.get('lessons') or book.get('docs') or book.get('items') or []
if not lessons:
    for k, v in book.items():
        if isinstance(v, list) and v and isinstance(v[0], dict):
            print(f'list under key {k!r}, len {len(v)}')
            lessons = v
            break

reg = json.load(open(f'{BASE}/scripts-translate/savant-registry.json'))
hand = [str(x) for x in reg['hand']]
llm = [str(k) for k in reg['llm']]
done = set(hand) | set(llm)
print(f'registry: hand {len(hand)} + llm {len(llm)} = {len(hand)+len(llm)} / 950')
print()

for i, d in enumerate(lessons):
    if not isinstance(d, dict):
        print(i, str(d)[:100])
        continue
    did = str(d.get('docId', d.get('id', '?')))
    title = d.get('title', d.get('name', ''))
    status = 'DONE' if did in done else ('hand' if did in hand else 'llm') if did in (set(hand) | set(llm)) else 'TODO'
    if did in hand and did in llm:
        status = 'DONE(hand+llm?)'
    print(i, did, status, str(title)[:60])
