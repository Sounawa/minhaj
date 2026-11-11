import json, subprocess

CACHE = json.load(open('scripts-translate/quran-cache.json'))
def get(sura, aya):
    s = CACHE[str(sura)]
    ar = [x for x in s['ar'] if str(x[0])==str(aya)]
    return ar[0][1] if ar else None

# For each image: list of (label, phrase) to test for presence
TESTS = {
 'hadid4': [('H57:4','يَعْلَمُ مَا يَلِجُ فِي الْأَرْضِ'), ('H57:3','وَهُوَ بِكُلِّ شَيْءٍ عَلِيم'), ('H57:5','أَلَمْ تَرَ أَنَّ اللَّهَ يَعْلَمُ مَا فِي السَّمَاوَاتِ')],
 'taghabun4': [('T64:4','عَلِيمٌ بِذَاتِ الصُّدُورِ'), ('T64:5','فَبِمَا كَسَبَتْ أَيْدِيكُمْ')],
 'shura10': [('S42:10','فَحُكْمُهُ إِلَى اللَّهِ'), ('S42:11','وَهُوَ السَّمِيعُ الْبَصِيرُ'), ('S42:12','وَلَهُ مَقَالِيدُ السَّمَاوَاتِ')],
 'talaq12': [('T65:12','أَحَاطَ بِكُلِّ شَيْءٍ عِلْمًا'), ('T65:11','ذَلِكُمُ اللَّهُ رَبِّي عَلَيْهِ تَوَكَّلْتُ')],
 'mulk14': [('M67:14','أَلَا يَعْلَمُ مَنْ خَلَقَ'), ('M67:13','أَسَرَّ قَوْلَكُمْ')],
 'anam40': [('A6:39','صُمٌّ وَبُكْمٌ فِي الظُّلُمَاتِ'), ('A6:40','أَتَاكُمْ عَذَابُ اللَّهِ'), ('A6:41','بَلْ إِيَّاهُ تَدْعُونَ')],
 'ibrahim29': [('I14:27','يُثَبِّتُ اللَّهُ الَّذِينَ آمَنُوا'), ('I14:28','تَبَدَّلُوا نِعْمَتَ اللَّهِ كُفْرًا'), ('I14:29','جَهَنَّمَ يَصْلَوْنَهَا')],
 'fatir8': [('F35:8','زُيِّنَ لَهُ سُوءُ عَمَلِهِ'), ('F35:7','لَهُ عَذَابٌ شَدِيد'), ('F35:9','وَاللَّهُ الَّذِي أَرْسَلَ الرِّيَاحَ')],
 'kahf17': [('K18:17','وَمَن يَهْدِ اللَّهُ فَهُوَ الْمُهْتَدِي'), ('K18:16','إِنَّهُمْ آوُوا إِلَى الْكَهْفِ')],
 'zumar37': [('Z39:37','وَمَن يَهْدِ اللَّهُ فَمَا لَهُ مِن مُّضِلٍّ'), ('Z39:36','أَلَيْسَ اللَّهُ بِكَافٍ عَبْدَهُ'), ('Z39:38','لَئِن')]
}

for name, tests in TESTS.items():
    img = f'tr-tmp/v16722/{name}-big.png'
    results = []
    for label, phrase in tests:
        prompt = (f"Look at this image containing Quranic Arabic text. Does the image contain the exact "
                  f"phrase: {phrase} ? Consider slight orthographic variations of Warsh script. "
                  f"Answer ONLY 'YES' or 'NO'.")
        out = subprocess.run(['z-ai','vision','-p',prompt,'-i',img],
                             capture_output=True, text=True, timeout=120)
        raw = out.stdout; i = raw.find('{')
        ans = '?'
        if i>=0:
            try:
                c = json.loads(raw[i:])['choices'][0]['message']['content'].strip().upper()
                ans = 'YES' if 'YES' in c else ('NO' if 'NO' in c else c[:20])
            except Exception: ans = raw[:60]
        results.append(f"{label}={ans}")
    print(f"{name}: " + ' | '.join(results), flush=True)
