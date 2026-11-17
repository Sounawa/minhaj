// Z2-28 — derniers zooms VLM W44-W50 (arbitrages finaux), leçon 24
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-24';
const R600 = `${DIR}/r600`;
const COMMON = `Recadrage 600 dpi agrandi d'un manuel scolaire marocain d'hadith, leçon 24 «حفظ أوامر الله تعالى». Réponds UNIQUEMENT par ce qui est imprimé, lettre par lettre, avec comptage des points. Ne complète JAMAIS par mémoire d'un texte connu.`;

// (page, y0, y1, x0, x1, tag, scale, question)
const Q = [
  [134, 0.818, 0.850, 0.30, 0.95, 'W44', 5, `Le verset ﴿فَادْعُوا اللهَ مُخْلِصِينَ لَهُ الدِّينِ﴾ et sa référence [غَافِر: ?] ⟵ CHIFFRE final : agrandi ×5 — décris le dernier chiffre de la référence trait par trait : est-ce ١٣ (le ٣ = trois dents successives sans boucle fermée) ou ١٤ (le ٤ = boucle/angle FERMÉ avec descente) ? Donne aussi ce qui suit الدِّينِ avant le crochet fermant (rien ? وَلَوْ كَرِهَ الْكَافِرُونَ ?).`],
  [135, 0.428, 0.460, 0.05, 0.95, 'W45', 5, `Ligne : «فَالْإِيمَانُ بِقَضَاءِ اللهِ وَقَدَرِهِ يُثْمِرُ عَدَمَ تَعَلُّقِ الْإِنْسَانِ بِغَيْرِهِ ... لِأَنَّهُ هُوَ الْفَاعِلُ فِي الْحَقِيقَةِ» ⟵ Quels mots EXACTS sont imprimés entre بِغَيْرِهِ et لِأَنَّهُ ? (rien ? سُبْحَانَهُ ? autre chose ?) Lettre par lettre. Tesseract lit «سبحانه» à cet endroit à 5 reprises — vérifie s'il est bien imprimé.`],
  [136, 0.748, 0.795, 0.05, 0.98, 'W46', 5, `Ouverture de la question 3 du تقويم (ligne entre «2. أبين كيفية التعلق بالله» et la citation «واعلم أن الأمة...») ⟵ Transcris cette ligne d'ouverture MOT À MOT avec les numéros : «3. ...» — le premier mot : أُبَيِّنُ ? أُوَفِّقُ ? أُوَضِّحُ ? أَوْقِفْ ? autre ? Lettre par lettre avec les points, puis la suite de la ligne (مَعْنَى ? مَعْنَى: ?).`],
  [137, 0.383, 0.412, 0.10, 0.90, 'W47', 5, `Référence entre crochets de l'encadré coranique ⟵ Les DEUX chiffres de [الأنعام: ?-?] agrandis ×5 : premier chiffre (٧٩ ? ٨٠ ? autre) et second chiffre (٨٢ ? ٨٣ ? autre) — décris chaque chiffre trait par trait (٧=v, ٨=Λ, ٩=cercle avec queue descendante, ٠=point, ٢=deux dents, ٣=trois dents).`],
  [132, 0.390, 0.426, 0.55, 0.98, 'W48', 4, `Notice d'Ibn ʿAbbās ⟵ le mot entre «أَحَدُ» et «مِنَ الصَّحَابَةِ» : les trois candidats sont (a) الْعُلَمَاءُ (b) الْأَعْلَامُ (c) الْأَعْلَامِ (d) العَبَادِلَةُ — transcris le mot imprimé LETTRE PAR LETTRE en comptant les points de chaque lettre (ع=1 point, ل=0, م=0 point, ب=1 point sous, د=0, ة=2 points). Puis le mot suivant مِنَ ... .`],
  [134, 0.324, 0.362, 0.20, 0.98, 'W49', 5, `Ligne : «...كَانَ اللهُ لَهُ فِي دُنْيَاهُ بِ... وَفِي أُخْرَاهُ بِ... وَالرِّضْوَانِ» ⟵ le mot après دُنْيَاهُ بِ (إِصْلَاحِ + quel nom ? الْحَالِ ? الْبَالِ ? الْآلِ ? الْعَمَلِ ?) et le mot après أُخْرَاهُ بِ (الْإِثَابَةِ ? الْإِتَابَةِ ? الْإِنَابَةِ ?) — lettre par lettre.`],
  [134, 0.630, 0.676, 0.05, 0.98, 'W50', 5, `Ligne : «يَكُونُ قَدْ أَعْرَضَ عَنْ رَبِّهِ وَالْتَجَأَ إِلَى ...» ⟵ la fin de la ligne : «إِلَى مَنْ لَا + [verbe] + وَلَا + [verbe]» — transcris les deux verbes LETTRE PAR LETTRE (يَقْدِرُ ? يَمْلِكُ ? يَضُرُّهُ ? يَنْفَعُهُ ? نَفْعًا ? ضُرًّا ?) avec comptage des points.`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const [page, y0, y1, x0, x1, tag, scale, question] of Q) {
  const out = `${DIR}/vlm24-W-${tag}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${tag}`); continue; }
  const png = `${DIR}/z24v-${tag}.png`;
  execSync(`python3 -c "from PIL import Image; im=Image.open('${R600}/p${page}.png').convert('L'); w,h=im.size; c=im.crop((int(${x0}*w),int(${y0}*h),int(${x1}*w),int(${y1}*h))); c=c.resize((int(c.width*${scale}),int(c.height*${scale})),Image.LANCZOS); c.save('${png}')"`);
  const img = fs.readFileSync(png).toString('base64');
  console.log(`\n======== ${tag} p${page} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + question },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 900,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 600 ? txt.slice(0, 300) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${tag} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(3000);
}
