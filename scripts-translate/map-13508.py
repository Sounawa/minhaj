# Cartographie des slots vides de 13508 (protocole R271 : prev/next de chaque <p> vide)
import re, html

src = open('/home/z/my-project/tr-tmp/13508.src.html', encoding='utf-8').read()

# découpe en éléments de premier niveau (h1/h2/h3/p/dl/ol/ul/div/span lines)
# on parcourt séquentiellement les blocs
blocks = re.findall(r'<(h1|h2|h3|p|dl|ol|ul|div|span)[^>]*>.*?</\1>|<(h1|h2|h3|p|dl|ol|ul|div)[^>]*/?>', src, flags=re.S)
# approche plus simple : splitter sur les balises connues
tokens = re.split(r'(?=<(?:h1|h2|h3|p|dl|ol|ul|div)[>\s])', src)
seq = []
for t in tokens:
    t2 = t.strip()
    if not t2:
        continue
    m = re.match(r'<(h1|h2|h3|p|dl|ol|ul|div)', t2)
    if not m:
        continue
    tag = m.group(1)
    inner = t2
    seq.append((tag, inner))

n_empty = 0
for i, (tag, inner) in enumerate(seq):
    if tag == 'p':
        # contenu textuel hors spans
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
                return f'{tg}: {it2[:110]}'
            print(f'--- SLOT VIDE #{n_empty} (pos {i})')
            print('    PREV :', brief(prev_i))
            print('    NEXT :', brief(next_i))
        elif '⟪SPAN⟫' in inner and txt == '':
            n_empty += 0  # span seul, guide

print()
print('TOTAL slots vides <p> :', n_empty)
print()
print('=== SPANS subsistants (guides) ===')
for m in re.finditer(r'<span[^>]*>(.*?)</span>', src, flags=re.S):
    s = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).replace('\xa0', ' ').strip()
    print('  SPAN :', repr(s))
