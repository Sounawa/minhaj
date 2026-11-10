// R680 — lectures VLM leçon 405 (pages 110-116, bandes b*). Chaque zone tranchée sur
// preuve image ; ne jamais deviner ; [?] pour l'illisible. Numéros : chiffre par chiffre.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/qa-crops-r680';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-405';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Bande d'un manuel arabe marocain (Muwaṭṭaʾ avec Šarḥ az-Zarqānī, 2 colonnes par page). Lecture de droite à gauche : transcris d'abord TOUTE la colonne de DROITE de haut en bas, puis TOUTE la colonne de GAUCHE de haut en bas. Transcris TOUT exactement ligne par ligne, diacritiques comprises, mot pour mot, y compris les paroles entre « ». Pour chaque renvoi [الموطأ رقم: N] : donne le numéro CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9) et aussi tel qu'imprimé. Marque [?] l'illisible, ne complète PAS de mémoire.`;

const PROMPTS = {
  'b110-1': `Haut de la page 110 d'un manuel arabe : médaillon circulaire avec le NUMÉRO DU COURS (donne-le chiffre par chiffre), bannière calligraphiée du TITRE du cours (transcris-la EXACTEMENT), puis la rubrique verte des objectifs (أهداف الدرس) numérotés. Transcris tout mot pour mot. Marque [?] l'illisible, ne complète PAS de mémoire.`,
  'b110-2': BASE + ` Contexte attendu : fin des objectifs, paragraphe tamhīd sur رمي الجمار, questions d'ouverture, puis le PREMIER hadith du Muwaṭṭaʾ (isnad: مالك عن نافع، عن عمر بن الخطاب : «لا يبيتنّ أحد من الحاج...») avec son renvoi [الموطأ رقم: N]. Transcris le hadith ENTIÈREMENT.`,
  'b110-3': BASE + ` Contexte attendu : suite/fin du premier hadith (bivouac des pèlerins), puis le SECOND hadith (isnad: عاصم بن عمر عن أبيه : le Prophète ﷺ accorde une concession aux رعاء الإبل — gardeurs de chameaux — pour le bivouac et le jet des pierres, finissant par «...ليومين ثم يرمون يوم التفرق» avec renvoi [الموطأ رقم: N]). Transcris tout.`,
  'b110-4': BASE + ` Contexte : suite éventuelle des hadiths ou décor de page. Transcris tout fragment de texte lisible.`,
  'b110-5': BASE + ` Contexte : bas de page 110. Transcris tout fragment de texte lisible.`,
  'b111-1': BASE + ` Contexte : haut de page 111 : fin éventuelle du second hadith avec renvoi [الموطأ رقم: N], puis le TROISIÈME hadith (isnad: مالك عن أبي بكر بن نافع عن أبيه, sujet : صفية بنت أبي عبيد, la femme de عبد الله بن عمر — elle نفست / fut retenue à المزدلفة et arriva après le coucher du soleil le jour du النحر, et Ibn ʿUmar leur ordonna de lapider la jamrah) avec renvoi [الموطأ رقم: N]. Transcris tout ENTIEREMENT.`,
  'b111-2': BASE + ` Contexte : suite du hadith de صفية (أمرهما عبد الله بن عمر أن ترميا الجمرة... ولم ير عليهما شيئا) avec son renvoi [الموطأ رقم: N], puis la notice du transmetteur Nافع (tarǧamat ar-rāwī : mawlā d'Ibn ʿUmar, «أصح الأسانيد مالك عن نافع عن ابن عمر» selon al-Bukhārī, mort en l'an H — DONNE L'ANNÉE CHIFFRE PAR CHIFFRE). Transcris tout.`,
  'b111-3': BASE + ` Contexte : suite de la notice de Nافع (envoyé en Égypte par ʿUmar, mort en 117 H ?), puis la rubrique الشرح (gloses): العقبة، الجمار، نفست/تفست. Transcris chaque glose ENTIÈREMENT.`,
  'b111-4': BASE + ` Contexte : fin des gloses éventuelles. Transcris tout.`,
  'b111-5': BASE + ` Contexte : bas de page 111. Transcris tout fragment lisible.`,
  'b112-1': BASE + ` Contexte : haut de page 112 : gloses (البيتوتة، يوم التفر), puis la rubrique استخلاص المضامين (résumé numéroté). Transcris tout.`,
  'b112-2': BASE + ` Contexte : suite du résumé (استخلاص المضامين), puis la recherche légale أولا: le jugement du bivouac à Minā les jours du jet (المبيت بمنى أيام الرمي ثلاث ليال...) et le hadith de هشام بن عروة عن أبيه sur le bivouac à La Mecque les nuits de Minā, avec renvoi [الموطأ رقم: N]. Transcris tout.`,
  'b112-3': BASE + ` Contexte : suite : «ويجب على الحاج المبيت بمنى...»، كالمرض والخوف على المتاع, ومن حبسه مرض فبات بمكة فعليه الهدي..., puis la 2e rubrique: الرخصة لأهل الأعذار في البيات خارج منى — «ففي الموطأ أن رسول الله ﷺ رخص لرعاء الإبل...». Transcris tout.`,
  'b112-4': BASE + ` Contexte : suite de la concession aux gardeurs de chameaux (يرمون يوم النحر ثم يرمون من الغد وبعد الغد ليومين ثم يرمون يوم التفرق), et le début du commentaire de مالك «وقال مالك في تفسير الحديث الذي رخص فيه رسول الله ﷺ لرعاء الإبل في رمي الجمار...». Transcris tout.`,
  'b112-5': BASE + ` Contexte : bas de page 112. Transcris tout.`,
  'b113-1': BASE + ` Contexte : haut de page 113 : suite du commentaire de مالك (أنهم يرمون يوم النحر... فإذا مضى اليوم الذي يلي يوم النحر رموا من الغد... يوم النفر), avec un renvoi [الموطأ رقم: N], puis رعاء الإبل وأهل الأعذار الأخرى, puis la rubrique ثانيا: رمي الجمار. Transcris tout.`,
  'b113-2': BASE + ` Contexte : 1- مكان وزمان الرمي : أ- وقت الرمي (لا ترمى الجمار في الأيام الثلاثة حتى تزول الشمس, hadith de نافع عن ابن عمر avec renvoi [الموطأ رقم: N]), ب- مكان رمي جمرة العقبة (سئل مالك... عبد الرحمن بن القاسم, renvoi [الموطأ رقم: N], وتمتاز جمرة العقبة بأربعة أشياء...). Transcris tout.`,
  'b113-3': BASE + ` Contexte : suite ب- (تمتاز جمرة العقبة بأربعة أشياء: اختصاصها بيوم النحر, رميها من بطن الوادي, لا يوقف عندها...), puis 2- صفة الرمي وآدابه (يذهب الحاج ماشيا... ومعه إحدى وعشرون حصاة, فيبتدئ بالجمرة الأولى...). Transcris tout.`,
  'b113-4': BASE + ` Contexte : suite de la manière du jet (فيبتدئ بالجمرة الأولى... يرميها بسبع حصيات وهو مستقبل القبلة ويدعو, ثم الجمرة الوسطى, ثم يتقدم أمامها... ثم جمرة العقبة يرميها بسبع حصيات...). Transcris tout.`,
  'b113-5': BASE + ` Contexte : bas de page 113. Transcris tout.`,
  'b114-1': BASE + ` Contexte : haut de page 114 : fin de la manière du jet (إن شاء تعجل وسقط عنه المبيت ليلة الرابع...), ثم hadith de نافع sur Ibn ʿUmar s'arrêtant aux deux premières jamarāt (وقوفا طويلا) avec renvoi [الموطأ رقم: N], et كان يكبر عند الرمي avec renvoi [الموطأ رقم: N]. Transcris tout.`,
  'b114-2': BASE + ` Contexte : glose sur les cailloux (الحصى التي يرمى بها الجمار, الحذف, واستحب مالك في الحصيات أن تكون أكبر من... avec renvoi [الموطأ رقم: N]), puis ج- الطهارة للرمي (تستحب الطهارة عند رمي الجمار, قال مالك لا أرى... ولكن... الذي يرمي الجمار أو يسعى بين الصفا والمروة وهو غير متوضئ... avec renvoi [الموطأ رقم: N]). Transcris tout.`,
  'b114-3': BASE + ` Contexte : د- المشي عند الرمي (عبد الرحمن بن القاسم عن أبيه: أن الناس... رموا الجمار مشاة ذاهبين وراجعين وأول من ركب معاوية بن أبي سفيان) AVEC SON RENVOI [الموطأ رقم: N] — donne le numéro CHIFFRE PAR CHIFFRE. ومراده بالناس الصحابة... وأن النبي ﷺ فعل ذلك, أما ركوب ابن أبي سفيان فكان للضرورة. Transcris tout.`,
  'b114-4': BASE + ` Contexte : الرمي عن الصبي والمريض (يصح الرمي عن الصبي والمريض إن لم يمكنهما..., سئل مالك هل يرمى عن الصبي والمريض فقال نعم..., يرمى عنه حين يرمي الذي رمى..., ويكبر وهو في منزله... مع renvoi [الموطأ رقم: N]). Transcris tout.`,
  'b114-5': BASE + ` Contexte : bas de page 114. Transcris tout.`,
  'b115-1': BASE + ` Contexte : haut de page 115 : ثالثا: تأخير رمي جمرة العقبة لعذر — reprise du hadith de صفية بنت أبي عبيد (وقفت بالمزدلفة... يوم النحر بعد ما غربت الشمس, أمرهما عبد الله بن عمر أن ترميا الجمرة... ولم ير عليهما شيئا لأنهما أدركتا وقت...). Transcris tout.`,
  'b115-2': BASE + ` Contexte : suite : قضاء الرمي وقد حبستهما العذر, ولكن يستحب عند مالك لمن عرض له مثل ما عرض لصفية أن يرمي في الوقت المطلوب, لأنه... يهدي؛ لم يرم في الوقت المطلوب. Puis l'évaluation (تقويم): أبين صفة رمي الجمار / أبين حكم ما يأتي مع الاستدلال والتعليل. Transcris tout.`,
  'b115-3': BASE + ` Contexte : les cas d'évaluation : 1- حاج يحضر نهارا لرمي الجمرات وفي المساء يذهب ليبيت بمكة ثم يعود; 2- انتقض وضوء حاج أثناء رمي الجمرة الوسطى; 3- سئل مالك عن من نسي جمرة من الجمار في بعض أيام منى حتى يمسي... قال: يرميها أي ساعة من ليل أو نهار كما يصلي الصلاة إذا نسيها... فعليه الهدي avec renvoi [الموطأ رقم: N]. Transcris tout.`,
  'b115-4': BASE + ` Contexte : l'exploitation (أتأمل النص وأبين نوع الدليل الذي تضمنه جواب الإمام مالك عما سئل عنه) et la suite éventuelle. Transcris tout.`,
  'b115-5': BASE + ` Contexte : bas de page 115. Transcris tout.`,
  'b116-1': BASE + ` Contexte : haut de page 116 (page d'annonce de préparation, décor calligraphié). Transcris tout fragment lisible.`,
  'b116-2': BASE + ` Contexte : milieu de page 116 : l'invite «أحفظ أحاديث الدرس المقبل وأجيب عن الآتي» puis les questions : 1- أشرح: الإشعار - التقليد - [TERME ILLISIBLE À LIRE GLYPHE PAR GLYPHE, possibly a printing flaw] ; 2- أبحث عن معنى المستيسر من الهدي. Transcris tout EXACTEMENT, surtout les TROIS termes de la question 1.`,
  'b116-3': BASE + ` Contexte : suite de la page d'annonce. Transcris tout fragment lisible.`,
  'b116-4': BASE + ` Contexte : bas de page 116. Transcris tout fragment lisible.`,
  'b116-5': BASE + ` Contexte : bas de page 116. Transcris tout fragment lisible.`,
};

async function main() {
  const zai = await ZAI.create();
  const tags = Object.keys(PROMPTS).filter(t => fs.existsSync(`${DIR}/${t}.png`) && !fs.existsSync(`${OUTDIR}/${t}.txt`));
  console.log(`tâches r680: ${tags.length}`);
  for (const tag of tags) {
    for (let k = 1; k <= 4; k++) {
      try {
        const b64 = fs.readFileSync(`${DIR}/${tag}.png`).toString('base64');
        const res = await zai.chat.completions.createVision({
          messages: [{ role: 'user', content: [
            { type: 'text', text: PROMPTS[tag] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
          ] }],
          thinking: { type: 'disabled' },
        });
        const txt = res.choices[0]?.message?.content || '(vide)';
        fs.writeFileSync(`${OUTDIR}/${tag}.txt`, txt, 'utf-8');
        console.log(`${tag}: OK (${txt.length} car)`);
        break;
      } catch (e) {
        const msg = String(e?.message || e);
        if (k === 4) { console.log(`${tag}: ERREUR ${msg}`); break; }
        const wait = msg.includes('429') ? 20000 * k : 5000;
        await new Promise(r => setTimeout(r, wait));
      }
    }
    await new Promise(r => setTimeout(r, 2500));
  }
  console.log('VLM r680 terminé');
}
main().catch(e => { console.error('VLM_ERR: ' + (e?.message || e)); process.exit(1); });
