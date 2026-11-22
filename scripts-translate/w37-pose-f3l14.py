#!/usr/bin/env python3
# W37 — pose fiqh-3es pdf-14 أحكام اللقطة والغصب (pp.109-115) + registre
import json, re, subprocess

REPO = '/home/z/my-project/minhaj'
HTMLFR = '/home/z/my-project/work/l14/htmlfr-pdf14.html'
DOCID = 'pdf-14'

html = open(HTMLFR, encoding='utf-8').read().strip()
body = re.sub(r'<[^>]+>', '', html)

# --- QA typo ---
for tag in ('em', 'p', 'h1', 'h2', 'h3', 'dl', 'ul', 'ol', 'strong', 'li', 'dt', 'dd'):
    o = html.count(f'<{tag}>'); c = html.count(f'</{tag}>')
    assert o == c, f'balises {tag} déséquilibrées: {o} vs {c}'
assert len(re.findall(r'[\u0600-\u06FF]', body)) == 0, 'arabe résiduel'
assert body.count('«') - body.count('»') == 0, 'guillemets non appariés'
assert body.count("'") == 0, 'apostrophes droites'
assert html.count('<h2>') == 9, 'h2 attendus 9'
assert html.count('<h1>') == 1 and html.count('<dl>') == 1 and html.count('<ul>') == 2 and html.count('<ol>') == 1
assert html.count('<h3>') == 3, 'h3 attendus 3'
assert len(body) > 14000, f'htmlFr trop court: {len(body)}'
print(f'QA PASS — {len(body)} car FR-seule')

# --- slot vide (fetch-avant-pose) ---
r = subprocess.run(['git', 'fetch', 'origin', 'main'], cwd=REPO, capture_output=True, text=True)
assert r.returncode == 0, f'fetch KO: {r.stderr[:200]}'
subprocess.run(['rm', '-f', f'{REPO}/.git/tmp_pack_*'])
r = subprocess.run(['git', 'merge', '--ff-only', 'origin/main'], cwd=REPO, capture_output=True, text=True)
print('ff-only:', r.stdout.strip()[:80] or 'déjà à jour')

path = f'{REPO}/content/books/fiqh-3es.json'
raw = open(path, encoding='utf-8').read()
d = json.loads(raw)
lessons = [x for x in d['lessons'] if x.get('docId') == DOCID]
assert len(lessons) == 1, f'{DOCID}: {len(lessons)} correspondances'
assert lessons[0]['htmlFr'].strip() == '', 'slot pdf-14 non vide — pose concurrente ?'
lessons[0]['htmlFr'] = html
out = json.dumps(d, ensure_ascii=False, indent=2) + '\n'
open(path, 'w', encoding='utf-8').write(out)
print('htmlFr posé dans content/books/fiqh-3es.json')

# --- registre IA-3 ---
rpath = f'{REPO}/scripts-ia3/savant-registry-ia3.json'
reg = json.load(open(rpath, encoding='utf-8'))
assert f'fiqh-3es/{DOCID}' not in reg['hand'], 'déjà inscrit'
reg['hand'].append(f'fiqh-3es/{DOCID}')
open(rpath, 'w', encoding='utf-8').write(json.dumps(reg, ensure_ascii=False, indent=2) + '\n')
print(f"registre IA-3 → {DOCID} ({len(reg['hand'])} ids)")
