# Cartographie des slots vides de 13478 (protocole R271/R272 : prev/next de chaque <p> vide)
import re, html

src = open('/home/z/my-project/tr-tmp/13478.src.html', encoding='utf-8').read()

tokens = re.split(r'(?=<(?:h1|h2|h3|p|dl|ol|ul|div)[>\s])', src)
seq = []
for t in tokens:
    t2 = t.strip()
    if not t2:
        continue
    m = re.match(r'<(h1|h2|h3|p|dl|ol|ul|div)', t2)
    if not m:
        continue
    seq.append((m.group(1), t2))

n_empty = 0
for i, (tag, inner) in enumerate(seq):
    if tag == 'p':
        txt = re.sub(r'<span[^>]*>.*?</span>', '⟪SPAN⟫', inner, flags=re.S)
        txt = re.sub(r'<[^>]+>', '', txt)
        txt = html.unescape(txt).replace('\xa0', ' ').strip()
        if txt == '' and '⟪SPAN⟫' not in inner:
            n_empty += 1
            prev_i = i-1
            while prev_i >= 0 and seq[prev_i][0] in ('div',):
                prev_i -= 1
            next_i = i+1
            while next_i < len(seq) and seq[next_i][0] in ('div',):
                next_i += 1
            def brief(j):
                if j < 0 or j >= len(seq):
                    return '(fin)'
                tg, it = seq[j]
                it2 = re.sub(r'<span[^>]*>(.*?)</span>', r'⟪S:\1⟫', it, flags=re.S)
                it2 = re.sub(r'<[^>]+>', ' ', it2)
                it2 = html.unescape(it2).replace('\xa0', ' ')
                it2 = re.sub(r'\s+', ' ', it2).strip()
                return f'{tg}: {it2[:100]}'
            print(f'--- SLOT VIDE #{n_empty} (pos {i})')
            print('    PREV :', brief(prev_i))
            print('    NEXT :', brief(next_i))

print()
print('TOTAL slots vides <p> :', n_empty)
print()
print('=== SPANS subsistants (guides) ===')
for m in re.finditer(r'<span[^>]*>(.*?)</span>', src, flags=re.S):
    s = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).replace('\xa0', ' ').strip()
    print('  SPAN :', repr(s))
print()
print('=== Fente dl ===')
for m in re.finditer(r'<dl>.*?</dl>', src, flags=re.S):
    print('  dl:', re.sub(r'\s+', ' ', m.group(0))[:120])
