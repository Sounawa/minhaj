// Z2-21 — hadith-5ep leçon 19 — ultra-zooms s-série : dernières adjudications
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-19';

const PRE = `Ultra-zoom très haute résolution d'une ligne d'un manuel marocain d'hadith (5e primaire), leçon 19 « مِنْ خِصَالِ الْإِيمَانِ ». Transcris la ligne STRICTEMENT lettre à lettre avec toutes les diacritiques. Pour chaque mot contesté, énumère les lettres avec leur NOMBRE DE POINTS et leur VOYELLE exacte. Ne devine jamais : si un signe est invisible, dis-le. Réponds en deux parties : TRANSCRIPTION puis RÉPONSES. `;

const S = {
  s01: `LIGNE(S) : « ... وَرَجَا [X] وَاجْتَهَدَ فِي فِعْلِ مَا أُمِرَ بِهِ وَتَرْكِ مَا نُهِيَ عَنْهُ. وَأَهَمُّ مَا عَلَيْهِ مِنْ ذَلِكَ ضَبْطُ [Y] [Z] رَعَايَتُهُ/رَعِيَّتُهُ وَهُوَ مَسْئُولٌ عَنْهَا »
QUESTIONS : (1) X = mot après « وَرَجَا » : « ثَوَابَهُ » (thāʾ 3 points + wāw + alif + bāʾ) ou « وَعْدَهُ » (wāw + ʿayn SANS point + dāl) ? Décris les lettres vues. (2) Y = mot après « ضَبْطُ » : « جَوَارِحِهِ » ou « لِسَانِهِ » ? Décris. (3) Z = pronom relatif : « الَّتِي هِيَ » ou « الَّذِي هُوَ » ? (4) Le mot « رَعَايَتُهُ/رَعِيَّتُهُ » : y a-t-il un ALIF entre le ʿayn et le yāʾ (رَعَايَـ) ou deux yāʾ consécutifs (رَعِيَّـ) ? Combien de yāʾ comptes-tu ? Quelle est la voyelle du tāʾ final (ḍamma) ? (5) Transcris la ligne complète.`,
  s02: `LIGNE(S) : « وَمِنْ [X] الْحَثِّ عَلَى حِفْظِ اللِّسَانِ مَا يَأْتِي: » + « أ - أَنَّ [Y] اللِّسَانِ مِنْ خُصَالِ الْإِيمَانِ كَمَا فِي الْحَدِيثِ: «مَنْ كَانَ يُؤْمِنُ بِاللهِ وَالْيَوْمِ الْآخِرِ فَلْيَقُلْ خَيْرًا أَوْ لِيَصْمُتْ» »
QUESTIONS : (1) X = mot après « وَمِنْ » : « أَسْبَابِ » (hamza + sīn 0 point + bāʾ 1 point + alif + bāʾ) — confirme ou corrige. (2) Le mot suivant : « الْحَثِّ » (ḥāʾ 0 point + thāʾ 3 points + shadda sur thāʾ) ou « الْحَدِيثِ » (ḥāʾ + dāl + yāʾ + thāʾ) ? (3) Y = mot après « أَنَّ » : « اسْتِقَامَةَ » (alif + sīn + tāʾ 2 points + qāf 2 points + alif + mīm + tāʾ marbūṭa, fatha finale) ou « إِقَامَةَ » ou autre ? Décris les lettres une à une. (4) Transcris les lignes.`,
  s03: `LIGNE(S) : « قَوْلُهُ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ «مَنْ كَانَ يُؤْمِنُ بِاللهِ وَالْيَوْمِ الْآخِرِ» يَعْنِي مَنْ كَانَ يُؤْمِنُ الْإِيمَانَ الْكَامِلَ الْمُنْجِيَ مِنْ عَذَابِ اللهِ الْمُوصِلَ إِلَى رِضْوَانِ اللهِ »
QUESTIONS : (1) Le mot entre « قَالَ » et « يَعْنِي » : « مَنْ كَانَ » ou juste « مَنْ » ? (2) Après « يَعْنِي » : « مَنْ كَانَ يُؤْمِنُ » ou « مُؤْمِنًا » ? (3) « الْإِيمَانَ » (accusatif, fatha sur nūn) ou « بِالْإِيمَانِ » (avec bāʾ) ? (4) « الْمُنْجِيَ » (fatha sur yāʾ) et « الْمُوصِلَ » (fatha sur lām) ou nominatifs « الْمُنْجِي / الْمُوصِلُ » ? Décris la voyelle finale de chaque mot. (5) « رِضْوَانِ » (kasra sous rāʾ) ou « رَضْوَانِ » (fatha) ? (6) Transcris les 2-3 lignes.`,
  s04: `LIGNE(S) : titre « 2. ... اللِّسَانِ » + « خَصَّ النَّبِيُّ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ فِي الْحَدِيثِ اللِّسَانَ دُونَ غَيْرِهِ مِنَ الْجَوَارِحِ لِخُطُورَتِهِ [X] فِيمَا يَأْتِي: »
QUESTIONS : (1) Le titre : « 2. مَخَاطِرُ اللِّسَانِ » — confirme le premier mot lettre par lettre et sa voyelle finale. (2) X = mot entre « لِخُطُورَتِهِ » et « فِيمَا يَأْتِي » : décris ses lettres une à une avec leurs points. Est-ce « الْمُنْذِرَةِ » ou « الْمُتَّصِلَةِ » ou « الْمُحْتَمَلَةِ » ou « الْمُوجِبَةِ » ou un tout autre mot ? (3) « لِخُطُورَتِهِ » (kasra sous lām + ḍamma sur thāʾ) — confirme. (4) Transcris les lignes.`,
  s05: `LIGNE(S) : « ب - أَنَّهُ أَكْثَرُ الْجَوَارِحِ [X] [Y] وَلِذَلِكَ كَانَ أَكْثَرَ مَا [Z] الْإِنْسَانَ [W] كَمَا جَاءَ فِي الْحَدِيثِ: «وَهَلْ [V] النَّاسَ فِي النَّارِ عَلَى وُجُوهِهِمْ أَوْ عَلَى مَنَاخِرِهِمْ إِلَّا حَصَائِدُ أَلْسِنَتِهِمْ». [سنن الترمذي] »
QUESTIONS : (1) X = « ارْتِكَابًا » ou « تَكَلُّمًا » ? Décris les lettres. (2) Y = « لِلزَّلَّاتِ » (zāy 1 point + lām + shadda + lām + tāʾ) ou « لِلذُّنُوبِ » (dhāl + nūn) ou « لِلذَّلَّاتِ » ? Décris. (3) Z = « يُدْخِلُ » (yāʾ + ḍamma + dāl + kasra + ḥāʾ + lām) ou « يَدْخُلُ » (sans ḥāʾ) ? (4) W = « النَّارَ » (accusatif direct) ou « إِلَى النَّارِ » (avec ilā) ? (5) V = « يَكُبُّ » (yāʾ + fatha + kāf + shadda sur bāʾ) ou « يُكَبُّ » (ḍamma sur yāʾ) ou « يُكَبِّبُ » ? Décris la première voyelle et la shadda. (6) « أَوْ عَلَى مَنَاخِرِهِمْ » présent ? (7) Transcris tout.`,
  s06: `LIGNE : « ... مِمَّا يَدُلُّ عَلَى عِنَايَةِ الْإِسْلَامِ بِالْجَارِ عِنَايَةً خَاصَّةً [X] تَمَاسُكَ الْمُجْتَمَعِ وَتُرَسِّخُ مَبْدَأَ التَّعَاوُنِ وَالتَّكَافُلِ وَالتَّعَايُشِ. »
QUESTIONS : (1) Le mot après « بِالْجَارِ » : « عِنَايَةً خَاصَّةً » — confirme (tanwīn fatha sur les deux mots). (2) X = le VERBE entre « خَاصَّةً » et « تَمَاسُكَ » : décris-le lettre à lettre (points + voyelles). Est-ce « تُحَقِّقُ » / « تُمَكِّنُ » / « تُدَعِّمُ » / « تَدْعَمُ » / « تُقَوِّي » / « تَسْتَلْزِمُ » ou autre ? (3) « تَمَاسُكَ » : fatha sur kāf (objet direct) ou kasra (مضاف إليه) ? (4) « الْمُجْتَمَعِ » : kasra ? (5) « وَتُرَسِّخُ » (tāʾ + ḍamma + rāʾ + shadda + kasra + khāʾ + ḍamma) — verbe, confirme. (6) La ligne finit par « وَالتَّعَايُشِ. » ou y a-t-il autre chose après (comme « بَيْنَ أَفْرَادِ الْمُجْتَمَعِ ») ? (7) Transcris la ligne entière.`,
  s07: `LIGNE(S) : « ب - أَنَّ الْإِحْسَانَ إِلَى الْجَارِ وَصِيَّةُ اللهِ [X] وَرَسُولِهِ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ كَمَا يُفْهَمُ مِنْ حَدِيثِ عَائِشَةَ رَضِيَ اللهُ عَنْهَا: «مَا زَالَ جِبْرِيلُ يُوصِينِي بِالْجَارِ حَتَّى ظَنَنْتُ أَنَّهُ سَيُوَرِّثُهُ». [صحيح البخاري] »
QUESTIONS : (1) X = mot après « وَصِيَّةُ اللهِ » : « لِنَبِيِّهِ » (lām + nūn + bāʾ + yāʾ + shadda + yāʾ + hāʾ) ou « لِبَنِيهِ » (lām + bāʾ + nūn + yāʾ + hāʾ) ? Compte les yāʾ et cherche la shadda. (2) « حَتَّى ظَنَنْتُ أَنَّهُ سَيُوَرِّثُهُ » — confirme chaque mot (ظ 1 point ; ن ن ; ت ḍamma ; س ي و ر shadda ث ه). (3) La référence exacte : « [صحيح البخاري] ». (4) Transcris les 2 lignes.`,
  s08: `LIGNE : le milieu de la liste « وَمِنْ إِكْرَامِ الضَّيْفِ : ... » (après « وَإِظْهَارُ التَّرَحُّبِ بِهِ » et avant « وَمَدِّ يَدِ الْعَوْنِ »).
QUESTIONS : transcris CETTE ligne mot à mot. Items attendus approximatifs : (a) « وَتَنْزِيلُهُ الْمَنْزِلَةَ اللَّائِقَةَ بِهِ » ou variante (décris : tāʾ + nūn + zāy + yāʾ + lām + hāʾ ; mīm + nūn + zāy + lām + tāʾ marbūṭa ; lām + alif + qāf + tāʾ marbūṭa). (b) « وَتَأْنِيسُهُ بِالْإِقْبَالِ عَلَيْهِ » ou variante (tāʾ + hamza + nūn + yāʾ + sīn). (c) « وَبِكَرِيمِ الْمُحَادَثَةِ » ou « وَبِمُكَرَّمَاتِ الْمُحَادَثَةِ » ou « وَبِتَكْرِيمِ الْمُحَادَثَةِ » (décris : bāʾ + kāf + rāʾ + ... ; mīm + ḥāʾ + dāl + thāʾ 3 points + tāʾ marbūṭa). (d) « وَحُسْنِ الِاسْتِمَاعِ » (ḥāʾ + sīn + nūn ; alif + sīn + tāʾ + mīʾ + ʿayn) ou « الْإِنْصَاتِ ». Décris chaque item lettre par lettre avec les points.`,
  s09: `LIGNE(S) : citation d'Ibn Hubayra (p.109) : « هَذَا الْحَدِيثُ مِنَ الْفِقْهِ أَنْ يَعْتَقِدَ الْإِنْسَانُ أَنَّ إِكْرَامَ الضَّيْفِ عِبَادَةٌ لَا يَنْقُصُهَا أَنْ يُضِيفَ [X] وَلَا [Y] أَنْ يُقَدِّمَ إِلَى ضَيْفِهِ [Z] مِمَّا عِنْدَهُ ؛ فَإِكْرَامُهُ أَنْ يُسَارِعَ إِلَى الْبَشَاشَةِ فِي وَجْهِهِ وَيُطَيِّبَ الْحَدِيثَ لَهُ. وَعِمَادُ أَمْرِ الضِّيَافَةِ إِطْعَامُ الطَّعَامِ فَيَنْبَغِي أَنْ يُبَادِرَ بِمَا فَتَحَ اللهُ [W] مِنْ غَيْرِ كُلْفَةٍ »
QUESTIONS : (1) X = mot après « يُضِيفَ » : « غَنِيًّا » (ġayn 1 point au-dessus + nūn + yāʾ + shadda + alif + tanwīn) ou « غَرِيبًا » (ġayn + rāʾ + yāʾ + bāʾ) ou « مُوسِرًا » ? Décris les lettres et points. (2) Y = verbe après « وَلَا » : « يُعَيِّرَهَا » (ʿayn 0 point + yāʾ + shadda + rāʾ) ou « يُغَيِّرُهَا » (ġayn 1 point + yāʾ + shadda + rāʾ + ḍamma) ou « يَعْتَبِرَهَا » (ʿayn + tāʾ + bāʾ + rāʾ) ou « يَعِيبَهَا » ? CRUCIAL : la première lettre a-t-elle UN POINT au-dessus (ġayn) ou AUCUN (ʿayn) ? La voyelle finale est-elle fatha (jussive) ou ḍamma ? (3) Z = « الْيَسِيرَ » (yāʾ 2 points dessous + sīn 0 point + rāʾ, fatha) ou « الْبَسِيرَ » (bāʾ) ou autre ? (4) W = « لَهُ » présent après « اللهُ » ou absent ? (5) « وَيُطَيِّبَ الْحَدِيثَ لَهُ » (ṭāʾ + yāʾ + shadda + bāʾ) — confirme. (6) Transcris les 4 lignes.`,
  s10: `LIGNE(S) : fin de l'item 2 et début de l'item 3 de « وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ » : « ... وَالِابْتِعَادِ/وَالِابْتِعَادُ بِهِ عَنْ كُلِّ مَا فِيهِ ضَرَرٌ وَعَمَّا لَا نَفْعَ فِيهِ. » + « حَثَّ/حَثُّ الْإِسْلَامَ/الْإِسْلَامِ عَلَى الْجُودِ وَالْكَرَمِ وَالْإِحْسَانِ إِلَى الْجَارِ وَالضَّيْفِ وَحُسْنِ الْمُعَامَلَةِ »
QUESTIONS : (1) « وَالِابْتِعَادِ » : kasra sous le dāl (génitif) ou ḍamma (nominatif) ? (2) Le premier mot de l'item 3 : « حَثَّ » (ḥāʾ 0 point + thāʾ 3 points + shadda + FATHA sur thāʾ) ou « حَثُّ » (shadda + ḌAMMA/ḍammatayn sur thāʾ) ? Regarde la voyelle APRÈS la shadda. (3) Le mot suivant : « الْإِسْلَامُ » (ḍamma) ou « الْإِسْلَامِ » (kasra) ? (4) « لِمَا فِي ذَلِكَ مِنْ تَمْتِينِ الرَّوَابِطِ » — confirme تَمْتِينِ. (5) Transcris les lignes.`,
  s11: `LIGNE(S) : « ... أَنَّ الضِّيَافَةَ مِنْ سُنَنِ الْمُرْسَلِينَ وَقَدْ ضَيَّفَ [X] عَلَيْهِ السَّلَامُ كَمَا أَخْبَرَ بِذَلِكَ الْحَقُّ سُبْحَانَهُ : ﴿[AYA]﴾ [الذاريات: N] »
QUESTIONS : (1) X = le(s) mot(s) entre « ضَيَّفَ » et « عَلَيْهِ السَّلَامُ » : « إِبْرَاهِيمُ » directement ? ou « الضَّيْفَ إِبْرَاهِيمُ » ? ou autre ? Décris. (2) L'ĀYA exacte imprimée entre ﴿ ﴾ : transcris-la mot à mot. Est-ce « هَلْ أَتَاكَ حَدِيثُ ضَيْفِ إِبْرَاهِيمَ الْمُكْرَمِينَ » ? (3) Le NUMÉRO dans [الذاريات: N] : lis les chiffres arabes très attentivement (٢٤ = 24 ? ٢٥ ? autre ?). (4) Transcris les 2-3 lignes.`,
  s12: `LIGNE(S) : questions 2 et 3 du التقويم (bas de page 109) : « 2. [Q2] » et peut-être « 3. أُبَيِّنُ أَرْبَعَةَ أَنْوَاعٍ مِنَ الْإِكْرَامِ لِكُلٍّ مِنَ الْجَارِ وَالضَّيْفِ. »
QUESTIONS : (1) Q2 : transcris-la mot à mot. Le verbe initial : « أَذْكُرُ » (fatha sur dhāl + ḍamma sur kāf + ḍamma sur rāʾ) ou « اذْكُرْ » (impératif, sukūn sur rāʾ) ? (2) Le mot après : « نَوْعَيْنِ » ou « نُوعَيْنِ » ? (3) « أَسَاسِيَّيْنِ » (alif + sīn + alif + sīn + shadda + yāʾ + nūn + kasratayn) ou « السَّاسَيْنِ » ? (4) Le DERNIER mot de Q2 : « الْجِيرَانِ » (jīm + yāʾ + rāʾ + alif + nūn) ou « الْجَارِ » ou « الْحَيَوَانِ » (ḥāʾ + yāʾ + wāw + alif + nūn) ? DÉCRIS les lettres avec leurs points. (5) Si Q3 est visible : transcris-la. (6) Transcris tout ce qui est visible.`,
};

async function main() {
  const zai = await ZAI.create();
  for (const tag of Object.keys(S)) {
    const img = `${DIR}/z-${tag}.png`;
    const out = `${DIR}/z-${tag}.txt`;
    if (fs.existsSync(out)) { console.log(`skip ${tag}`); continue; }
    const b64 = fs.readFileSync(img).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: PRE + S[tag] },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 3000,
        temperature: 0.1,
      });
      const txt = res?.choices?.[0]?.message?.content ?? JSON.stringify(res);
      fs.writeFileSync(out, txt);
      console.log(`OK ${tag} (${txt.length} car)`);
    } catch (e) {
      console.error(`ÉCHEC ${tag}: ${e.message}`);
    }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
