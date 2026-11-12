// Z2-1 — adjudications pointues (10 micro-crops, une question précise par crop)
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-01';
const jobs = [
  { img: 'm-obj-tamhid.png', ask: `Bande d'une page arabe imprimée. Trois transcriptions STRICTES mot à mot (arabe, lettre à lettre, vocalisation comprise) :
(1) l'objectif n°3 (أَنْ أَتَمَثَّلَ...) : le mot après هِمَّةَ العُلَمَاءِ est-il « فِي العِنَايَةِ » ou « فِي الْعِلْمِ » ?
(2) le paragraphe التمهيد EN ENTIER : après « فِي المَغْرِبِ وَالمَشْرِقِ، » le verbe est-il فأقبلوا / فاقتنعوا / فاقتبلوا / autre ? puis quel mot après أحاديثه (وبيان معانيه ?) ;
(3) la dernière phrase du تمهيد : « فمن هما: الإمامان... » — écris-la exactement.
Réponds uniquement en arabe avec (1), (2), (3).` },
  { img: 'm-fahm-gloses.png', ask: `Bande d'une page arabe imprimée (rubrique التفهم/الفهم + gloses). Transcris STRICTEMENT mot à mot :
(1) le TITRE de la rubrique imprimé : الفهم ou التفهم ?
(2) les TROIS gloses : pour chacune, le terme glosé EXACT et sa définition (3e glose : quel terme glosé exactement — écris ses lettres) ;
(3) استخلاص المضامين et ses 2 numéros ;
(4) le titre suivant (التحليل ?) et LA PHRASE COMPLÈTE qui suit (يشتمل تحليل هذه المقدمة على ما يأتي / يتضمن ... ?) — lettre à lettre.
Réponds uniquement en arabe, structuré (1)-(4).` },
  { img: 'm-bio-fin.png', ask: `Bande d'une page arabe : FIN de la biographie de l'imam al-Nawawī. Transcris STRICTEMENT les deux dernières lignes lettre à lettre, en commençant par « فَسَكَنَ فِي المَدْرَسَةِ... ». La ligne finale « وَكَانَ يَقْرَأُ فِي كُلِّ يَوْمٍ اثْنَيْ عَشَرَ دَرْسًا ... » : écris-la ENTIÈRE, tous les mots qui suivent درسًا (تدريسا؟ عن شيخه؟ درسا وتصديرا؟ تصحيحا؟). Rien que ce qui est imprimé.` },
  { img: 'm-maitres.png', ask: `Bande d'une page arabe : professeurs et élèves de l'imam al-Nawawī. Transcris STRICTEMENT lettre à lettre :
(1) la ligne complète « دَرَسَ عَلَى ... وَغَيْرِهِمْ » : combien de professeurs sont nommés, et chacun EXACTEMENT (premier nom : الرضياني ? البرهان ? ابن ? ... — écris les lettres visibles) ;
(2) la ligne complète « وَمِنْ تَلَامِيذِهِ: ... » : chaque élève EXACTEMENT (الجعفري ou الجعبري ? أحمد بن جعوان / أحمد بن سعيد ? العطَّار ?).
Réponds uniquement en arabe (1)-(2).` },
  { img: 'm-daqiq-birth.png', ask: `Bande d'une page arabe : naissance d'Ibn Daqīq al-ʿĪd. Transcris STRICTEMENT lettre à lettre :
(1) la généalogie complète et les laqabs (محمد بن علي بن وهب بن مطيع، أبو الفتح تقي الدين ... — la nisba est-elle القُشَيري / القَصِيري / القُصَيري ? lettre à lettre) ;
(2) la phrase de naissance : « وُلِدَ فِي شَعْبَانَ ... » — le nom du village EXACTEMENT (ينبع ? بنبع ? من بلاد الحجاز / من أجناد ?) ;
(3) la phrase « نَشَأَ بِقُوصٍ ... » complète.
Réponds uniquement en arabe (1)-(3).` },
  { img: 'm-daqiq-oeuvres.png', ask: `Bande d'une page arabe : œuvres d'Ibn Daqīq al-ʿĪd et sa mort. Transcris STRICTEMENT toute la ligne « لَهُ مُؤَلَّفَاتٌ... » lettre à lettre jusqu'à « ...وَغَيْرُهَا » puis la phrase de la mort. Le nom de l'auteur commenté dans « وَشَرْحُ مُقَدِّمَةِ ... » : écris-le lettre à lettre (المطرزي? المطريزي? المَطَّرِيزِي?). Réponds uniquement en arabe.` },
  { img: 'm-bul123.png', ask: `Bande d'une page arabe : rubrique « ثانيا: مكانة الأربعين النووية ». Transcris STRICTEMENT :
(1) le titre et la phrase d'intro ;
(2) la 1re puce (اشتماله على أحاديث أصول الدين و... — le mot après الدين) ;
(3) la 2e puce entière ;
(4) la 3e puce entière (التزام الإمام النووي ... — avec ou بدون بال ? quel mot exact ; fin : معظمها في صحيح البخاري ومسلم ?).
Réponds uniquement en arabe (1)-(4).` },
  { img: 'm-hadith.png', ask: `Bande d'une page arabe : 4e puce contenant le hadith « مَنْ حَفِظَ ... ». Transcris STRICTEMENT lettre à lettre : le hadith en entier et ses deux déclinaisons « وفي رواية... » — précisément : حفظَ لأمتي ou على أمتي ? من أمر دينها ou من أمور دينها ? بعثه الله ou بُعثَ اللهُ... ? la 2e riwâya exacte ; la 3e : « وفي رواية أخرى » ou « وفي رواية أبي الدرداء » ? puis la référence entre crochets. Réponds uniquement en arabe.` },
  { img: 'm-bul5-stefade.png', ask: `Bande d'une page arabe : 5e puce et rubrique « وما يُستفاد من هذه المقدمة ». Transcris STRICTEMENT :
(1) la 5e puce entière lettre à lettre (تلقّى الناس له بالقبول شرقا وغربا? حيث تتناوله/تعالجه العلماء بالرواية والحفظ والشرح والدراسة والتعليم? النُّشُء?) ;
(2) le titre وما يُستفاد من هذه المقدمة ;
(3) les trois puces suivantes lettre à lettre (la 2e : فضل حفظ أربعين حديثا من أمور الدين استظهارا وفهما ... fin exacte ; la 3e : إبراز فضل العلماء ...).
Réponds uniquement en arabe (1)-(3).` },
  { img: 'm-box-stithmar.png', ask: `Bande d'une page arabe : encadré citant l'introduction d'al-Nawawī sur les compilateurs des Quarante. Transcris STRICTEMENT TOUTE la citation lettre à lettre, de « وَقَدْ صَنَّفَ العُلَمَاءُ » jusqu'à la fin entre « ... », en incluant les noms : عبد الله بن المبارك، محمد بن أسلم الطوسي (+ épithètes), الحسن بن سفيان النسائي، أبو بكر الأجري، أبو بكر بن إبراهيم (+ nisba exacte), الدارقطني، الحاكم، أبو نعيم، أبو عبد الرحمن السلمي, puis TOUS les noms suivants jusqu'à la fin et le mot final (خلفهم أو خلافهم). Réponds uniquement en arabe.` },
];

async function main() {
  const zai = await ZAI.create();
  const out = [];
  for (const j of jobs) {
    const b64 = fs.readFileSync(`${DIR}/${j.img}`).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: j.ask },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ]}],
        model: 'glm-5v-turbo', max_tokens: 1800,
      });
      const txt = res.choices[0].message.content;
      out.push(`\n\n========== ${j.img} ==========\n` + txt);
      console.log(`${j.img} OK (${txt.length})`);
      fs.writeFileSync(`${DIR}/adjud-points.md`, out.join(''));
    } catch (e) {
      console.log(`${j.img} FAIL: ${e.message}`);
      out.push(`\n\n========== ${j.img} = FAIL: ${e.message} ==========\n`);
    }
  }
  fs.writeFileSync(`${DIR}/adjud-points.md`, out.join(''));
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
