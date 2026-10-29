# -*- coding: utf-8 -*-
"""build-20054.py — assemble les fragments FR de 20054 (fihrist), vérifie les 4 citations au cache, sondes."""
import json, re, unicodedata

BASE = '/home/z/my-project'
frag = [open(f'{BASE}/tr-tmp/fr20054_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(frag)

data = json.load(open(f'{BASE}/scripts-translate/quran-cache.json', encoding='utf-8'))

def bare2(t):
    out = []
    for c in t:
        if unicodedata.category(c).startswith('M') or c == '\u0640':
            continue
        if c == '\u0622': c = '\u0627'
        if c == '\u0649': c = '\u064a'
        out.append(c)
    return ''.join(out).replace('\u0671', '\u0627')

FINE = '\u202f'
TRANSLIT = {
    (2,102): 'wa-mā yuʿallimāni min aḥadin',
    (21,78): 'wa-dāwūda wa-sulaymāna iḏ yaḥkumāni fī l-ḥarṯi',
    (37,106): 'inna hāḏā la-huwa l-balāʾu l-mubīnu',
    (33,35): 'inna l-muslimīna wa-l-muslimāti wa-l-muʾminīna wa-l-muʾmināti',
}

def ctx(s, a, motif):
    verse = data[str(s)]['ar'][a-1][1]
    words = re.split(r'[\s\u00a0]+', verse.strip())
    bars = [bare2(w) for w in words]
    idx = [i for i, b in enumerate(bars) if motif in b]
    if not idx:
        return None
    i = idx[0]
    lo, hi = max(0, i-3), min(len(words), i+4)
    sel = words[lo:hi]
    sel = sel[0].lstrip('،') if lo > 0 else sel[0]
    return FINE.join(sel)

fails = []
def sub(m):
    s, a, motif = int(m.group(1)), int(m.group(2)), m.group(3)
    c = ctx(s, a, motif)
    if not c:
        fails.append(f'Q:{s}:{a}:{motif}')
        return '⟪ÉCHEC⟫'
    tr = TRANSLIT.get((s, a, motif), TRANSLIT.get((s, a)))
    if tr is None:
        fails.append(f'TR:{s}:{a}:{motif}')
        return '⟪ÉCHEC⟫'
    return f'«{tr}» ({s}:{a})'

html = re.sub(r'\{\{Q:(\d+):(\d+):([^}]+)\}\}', sub, html)
html = html.replace(chr(39), '\u2019')

# ==== SONDES ====
ok = True
def probe(label, cond, detail=''):
    global ok
    print(('OK  ' if cond else 'FAIL') + f' [{label}] {detail}')
    if not cond: ok = False

h1s = re.findall(r'<h1>(.*?)</h1>', html)
probe('h1 unique', len(h1s) == 1, h1s[0] if h1s else '—')
probe('badge', 'Leçon 30 / 30' in html)
probe('h2 x5', len(re.findall(r'<h2>', html)) == 5, f"{len(re.findall(r'<h2>', html))}")
dts, dds = html.count('<dt>'), html.count('<dd>')
probe('métadonnées 3 dt/dd', dts == 3 and dds == 3, f'{dts}/{dds}')
ols = re.findall(r'<ol>\s*<li>', html)
probe('deux ol (fihrist + N.d.T.)', html.count('<ol>') == 2, f"{html.count('<ol>')}")
fihrist = html.split('<h2>Le fihrist des quatorze sources</h2>')[1].split('<h2>')[0]
n_fih = fihrist.count('<li>')
ndt = html.split('<h2>Notes du traducteur</h2>')[1]
n_ndt = ndt.count('<li>')
probe('fihrist 14 entrées', n_fih == 14, f'{n_fih}')
probe('N.d.T. >= 8', n_ndt >= 8, f'{n_ndt}')
probe('marqueurs résolus', len(fails) == 0 and '⟪ÉCHEC⟫' not in html, str(fails))
probe('volume', len(html) >= 12000, f'{len(html)} car')
q = html.count('«') + html.count('»')
probe('guillemets appariés', q % 2 == 0, f'{q}')
probe("0 apostrophe droite", "'" not in html)
ar = [c for c in html if '\u0600' <= c <= '\u06ff']
probe('0 arabe résiduel', len(ar) == 0, f'{len(ar)} chars AR')
probe('muṣḥaf Muḥammadī nommé', 'Muṣḥaf al-Muḥammadī' in html)
probe('Bahǧat an-naẓar nommée', 'Bahǧat an-naẓar' in html)
probe('Ḫizāna al-Malikiyya 74', 'Ḫizāna al-Malikiyya' in html and 'numéro 74' in html)

if ok:
    open(f'{BASE}/tr-tmp/20054.html', 'w', encoding='utf-8').write(html)
    print(f'\nWRITTEN tr-tmp/20054.html — {len(html)} car')
else:
    print('\nBLOQUÉ — corriger avant écriture')
