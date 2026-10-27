import json, subprocess, sys

CACHE = json.load(open('scripts-translate/quran-cache.json'))

def get(sura, aya):
    s = CACHE[str(sura)]
    ar = [x for x in s['ar'] if str(x[0])==str(aya)]
    return ar[0][1] if ar else None

SURA = {'hadid4':(57,[3,4,5]), 'taghabun4':(64,[3,4,5]), 'shura10':(42,[9,10,11,12]),
        'talaq12':(65,[11,12,13]), 'mulk14':(67,[13,14,15]), 'anam40':(6,[38,39,40,41]),
        'ibrahim29':(14,[4,27,28,29]), 'fatir8':(35,[7,8,9]), 'kahf17':(18,[16,17]),
        'zumar37':(39,[36,37,38])}

for name,(s,ayas) in SURA.items():
    ext = 'jpg' if name=='taghabun4' else 'png'
    img = f'tr-tmp/v16722/{name}-big.png'
    cands = {}
    for a in ayas:
        t = get(s,a)
        if t: cands[a] = t
    lines = []
    for i,(a,t) in enumerate(cands.items(),1):
        lines.append(f"{i}) [ayah {a}] {t}")
    prompt = ("This image shows ONE Quranic verse in Arabic script (Maghrebi/Warsh calligraphy style). "
              "Below are candidate verse texts. Compare carefully with the image and reply with ONLY "
              "the number (1,2,3...) of the candidate that best matches the verse written in the image. "
              "If none matches, reply 0.\n\n" + "\n".join(lines))
    out = subprocess.run(['z-ai','vision','-p',prompt,'-i',img],
                         capture_output=True, text=True, timeout=120)
    raw = out.stdout
    i = raw.find('{')
    ans = '?'
    if i>=0:
        try:
            d = json.loads(raw[i:])
            ans = d['choices'][0]['message']['content'].strip()[:80]
        except Exception:
            ans = raw[:120]
    print(f"{name}: {ans}", flush=True)
