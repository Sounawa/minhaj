// IA-2 — vlm-h6-16.mjs : passe VLM (dernier recours) pour les mots litigieux de L16.
// Méthode Z2-50/51 : questions neutres, décomposition lettre par lettre,
// jamais de complétion par mémoire d'un texte connu.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const COMMON = `Bande d'un manuel scolaire marocain de hadith (6e primaire), texte arabe imprimé, lecture droite→gauche.
TRANSCRIS ce qui est demandé, mot à mot, avec la vocalisation imprimée. Pour les mots sous SCRUTIN : décompose lettre par lettre (forme, nombre de points et leur place, dents), et décris les voyelles. Ne complète JAMAIS par mémoire d'un texte connu : seulement ce que tu vois.`;

const Q = {
  'v-cartouche': `Le CARTOUCHE BLEU d'en-tête de la leçon (texte blanc/or sur fond bleu). Transcris TOUT ce qui y est imprimé. SCRUTIN : ce qui suit le mot «الدرس» — un numéro ? des mots ? S'il y a un chiffre arabe, décris chaque chiffre séparément (١٥ = un-alif-cinq ? ١٦ = un-alif-six ?) et donne sa valeur. Puis le TITRE de la leçon, mot à mot avec sa vocalisation.`,
  'v-ithn': `La ligne complète se termine par «... لقوله ﷺ: لا حَسَدَ إلا في ...». Transcris la ligne. SCRUTIN : le dernier groupe après «في» — «اثنين» ou «اثنتين» ? Décompose lettre par lettre : combien de lettres après le ا ? Y a-t-il un نون ou un تاء (2 points au-dessus) avant la finale ? Vocalisation du dernier mot.`,
  'v-atah': `La ligne contient «... رجل ... الله مالا فسلط... على هلكته في الحق، ورجل ... الله الحكمة فهو». Transcris-la. SCRUTIN 1 : le verbe après le premier «رجل» — «آتاهُ» (2e lettre = تاء SANS point) ou «آناهُ» (2e lettre = نون AVEC 1 point) ? Compte les points de la 2e lettre. SCRUTIN 2 : même question pour le verbe après le deuxième «رجل». SCRUTIN 3 : après «فسلّط» y a-t-il un «هُ» (فسلطه على هلكته) ?`,
  'v-tasawum': `La ligne commence par «- البيع على بيع ...». Transcris-la entièrement. SCRUTIN 1 : «وهو ال... في الثمن» — «الزيادة» ou «الزياد» ? SCRUTIN 2 : le mot (ou les mots) juste AVANT «المتبايعين» — «حال تساوم» ou «بعد سوم» ou autre ? Décompose-le(s) lettre par lettre.`,
  'v-talaf': `La ligne commence par «2- اجتناب كل ما يؤدي...». Transcris-la entièrement. SCRUTIN : le mot juste après «بالأخوة و» et avant le «؛» — décompose-le lettre par lettre. Y a-t-il «التالف» (alif-ta-alif-lam-fa) ou «التآلف» (avec un signe madda ~ au-dessus de l'alif de la 3e lettre) ou «التلاف» ou autre ? Décris précisément ce qui est imprimé au-dessus de l'alif.`,
  'v-jaa': `Transcris la ligne complète (elle contient «جاء النهي...»). SCRUTIN 1 : le mot après «عن». SCRUTIN 2 : le mot qui suit — «تتنافى» ou «تتناقى» ? La lettre penchée avant le ى final porte UN point (ف) ou DEUX points (ق) ? SCRUTIN 3 : le groupe après «مع» — «ما تقتضيه» ou «مقتضيات» ? SCRUTIN 4 : comment la ligne se termine-t-elle exactement ?`,
  'v-idad': `Deux questions numérotées (1- et 2-) d'un exercice de préparation. Transcris-les entièrement. SCRUTIN 1 (question 1) : le mot après «التي» — «تتنافى» ou «تتناقى» ? Points de la lettre avant le ى final. SCRUTIN 2 (question 2) : le groupe entre les deux tirets « - ... - » — décompose-le lettre par lettre : «التقوى هاهنا», «التقي هاهنا» ou autre ?`,
  'v-asbab': `Fin d'une puce : transcris ce qui est visible («...بوحدة الأمة، ووجوب الأخذ بكل ...»). SCRUTIN : le DERNIER mot — «أسباب» seul ou «أسبابها» (avec هاء après le ب) ? Y a-t-il une lettre de plus après le ب final ? Décris la fin du mot lettre par lettre.`,
  'v-taabbir': `Transcris les 2-3 lignes complètes : «وفي التعبير بعباد الله إشارة إلى أن العباد عبيد لله تعالى، فحقه عليهم أن يطيعوه بالأخوة فيما بينهم؛ فتعيش المجتمعات في ظل الإسلام حياة أمن وعدل واطمئنان ومودة.» — vérifie mot à mot et signale TOUTE divergence avec ma proposition. SCRUTIN : le mot exact entre «فيما» et «بينهم».`,
  'v-versA': `Encadré de versets coraniques (fond ornementé, couleur). Transcris les lignes imprimées mot à mot AVEC la vocalisation, sans compléter de mémoire : commence par «قال الله تعالى:» puis le(s) verset(s). N'INVENTE RIEN : si un mot est illisible, note-le [?].`,
  'v-versB': `Suite et fin de l'encadré de versets coraniques (fond ornementé, couleur), avec la référence entre crochets à la toute fin. Transcris les lignes mot à mot AVEC la vocalisation, sans compléter de mémoire. SCRUTIN final : la RÉFÉRENCE entre crochets — décris les DEUX nombres dans l'ordre DROITE→GAUCHE où ils sont imprimés (ex. : à droite ١١, puis tiret, puis ١٠), avec la valeur de chaque chiffre.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of Object.keys(Q)) {
  const out = `${DIR}/vlm-${k}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${k}`); continue; }
  const img = fs.readFileSync(`${DIR}/${k}.png`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q[k] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 2200,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 600 ? txt.slice(0, 450) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000 * attempt); }
  }
  await sleep(2500);
}
console.log('OK vlm-h6-16');
