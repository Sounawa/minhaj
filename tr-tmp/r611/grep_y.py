import sys
pg = sys.argv[1]
kws = sys.argv[2:]
rows = {}
for ln in open(f"tr-tmp/r611/tsv{pg}.tsv", encoding="utf-8"):
    f = ln.rstrip("\n").split("\t")
    if len(f) < 12 or f[0] != "5":
        continue
    text = f[11]
    if not text.strip():
        continue
    top, height = int(f[7]), int(f[9])
    for k in kws:
        if k in text:
            key = (top // 40)
            rows.setdefault(key, []).append((top, height, text))
for key in sorted(rows):
    tops = rows[key]
    y0 = min(t for t, h, x in tops)
    y1 = max(t + h for t, h, x in tops)
    print(f"y0={y0} y1={y1} words={' '.join(x for _, _, x in tops)}")
