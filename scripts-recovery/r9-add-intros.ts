/**
 * Minhāj R9 — Introductions bilingues rédigées à la main pour les 10 manuels
 * restés sans présentation (le site officiel n'a pas publié de page d'intro
 * pour ces livres : la galerie s'ouvre directement sur la 1ʳᵉ leçon).
 * Convention : titleAr « تقديم الكتاب », titleFr « Présentation du manuel ».
 * Usage: bun run scripts-recovery/r9-add-intros.ts
 */
import { readFileSync, writeFileSync } from "fs";
import path from "path";

const BOOKS = path.join(process.cwd(), "content", "books");

interface Intro {
  ar: string[];
  fr: string[];
}

const I: Record<string, Intro> = {
  /* ————— Tafsīr al-Jalālayn, 4ᵉ primaire (fusion R9) ————— */
  "tafsir-1ep": {
    ar: [
      "يبدأ التلميذ في السنة الرابعة من التعليم الابتدائي العتيق دراسة مادة التفسير من خلال «تفسير الجلالين» للإمامين جلال الدين المحلي (ت 864هـ) وجلال الدين السيوطي (ت 911هـ)، وهو من أشهر متون التفسير التعليمية وأوجزها، جمعه مصنفاه ليتيسر للحافظ والطالب فهم كتاب الله.",
      "وتتمحور دروس هذا المستوى حول سورة الفاتحة وقصار السور من جزء «عمّ»، بالتوازي مع مقرر الحفظ، مع العناية بالتلاوة المجودة وفهم المعنى الإجمالي للآيات على قدر مدارك الصغار، وربط المعاني بالقيم الإيمانية والخلقية.",
    ],
    fr: [
      "En quatrième année du cycle primaire (taʿlīm ʿatīq), l'élève aborde l'exégèse coranique à travers le <em>Tafsīr al-Jalālayn</em> des deux imams Ǧalāl al-Dīn al-Maḥallī (m. 864/1459) et Ǧalāl al-Dīn al-Suyūṭī (m. 911/1505), l'un des manuels d'exégèse les plus célèbres et les plus concis, composé par ses deux auteurs pour rendre accessible au lecteur et à l'étudiant l'intelligence du Livre de Dieu.",
      "Les leçons de ce niveau sont centrées sur la sourate al-Fātiḥa et les sourates courtes de la partie « ʿAmmā », en parallèle du programme de mémorisation, avec un soin particulier porté à la psalmodie règlée (taǧwīd), à la compréhension globale du sens des versets — adaptée aux jeunes esprits — et à la mise en relation de ces sens avec les valeurs de foi et de conduite.",
    ],
  },

  /* ————— Tafsīr al-Jalālayn, 5ᵉ primaire (59ᵉ ḥizb) ————— */
  "tafsir-5ep": {
    ar: [
      "تتوالى مادة التفسير في السنة الخامسة من التعليم الابتدائي العتيق على «تفسير الجلالين» ذاته، وتغطي دروس هذا المستوى الحزب التاسع والخمسين من القرآن الكريم، بالتوازي مع مقرر الحفظ في هذا الطور.",
      "ويتدرب التلميذ على القراءة المتأنية لتفسير الجلالين، واستخراج المعاني الجزئية والكليات للآيات، والوقوف على أسباب النزول وما تدعو إليه الآيات من قيم تربوية وسلوكية.",
    ],
    fr: [
      "En cinquième année du cycle primaire, l'exégèse se poursuit avec le même <em>Tafsīr al-Jalālayn</em> : les leçons de ce niveau couvrent le cinquante-neuvième <em>ḥizb</em> du Noble Coran, en parallèle du programme de mémorisation propre à ce degré.",
      "L'élève s'exerce à une lecture suivie du commentaire, à l'extraction des sens particuliers et globaux des versets, à l'attention portée aux circonstances de la révélation et aux valeurs éducatives et morales que les versets appellent.",
    ],
  },

  /* ————— al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya, 1ʳᵉ lycée (S. al-Naḥl) ————— */
  "tafsir-tanawi-1": {
    ar: [
      "ينتقل التلميذ في السنة الأولى من السلك الثانوي العتيق إلى «المحرر الوجيز في تفسير الكتاب العزيز» للإمام الحافظ أبي محمد عبد الحق بن عطية الأندلسي (ت 542هـ)، وهو من أجلّ تفاسير الأندلس وأدقها اعتمادا على النقل واللغة والمعقول، وقد اعتمده المنهاج المغربي لكفايات التفسير التحليلية.",
      "وتتناول دروس هذا المستوى سورة النحل بآياتها، مع الوقوف عند مقاصدها الكبرى: التوحيد والنعم، وأحكامها الفقهية المستنبطة، ومنهج ابن عطية في الترجيح بين الأقوال.",
    ],
    fr: [
      "En première année du cycle secondaire, l'élève passe au <em>al-Muḥarrar al-waǧīz fī tafsīr al-kitāb al-ʿazīz</em> de l'imam, le ḥāfiẓ, Abū Muḥammad ʿAbd al-Ḥaqq b. ʿAṭiyya al-Andalusī (m. 542/1147), l'un des plus grands commentaires d'al-Andalus et l'un des plus rigoureux dans l'articulation de la transmission, de la philologie et de la raison, que le programme marocain a retenu pour former aux compétences de l'exégèse analytique.",
      "Les leçons de ce niveau parcourent la sourate al-Naḥl (les Abeilles), en s'arrêtant à ses finalités majeures — l'unicité divine et les grâces —, aux règles juridiques qu'on en déduit et à la méthode d'Ibn ʿAṭiyya dans la pondération des opinions.",
    ],
  },

  /* ————— al-Muḥarrar al-wajīz, 2ᵉ lycée (S. al-Isrāʾ) ————— */
  "tafsir-tanawi-2": {
    ar: [
      "يواصل التلميذ في السنة الثانية من السلك الثانوي العتيق دراسة «المحرر الوجيز» لابن عطية، وتتناول دروس هذا المستوى سورة الإسراء بآياتها كاملة.",
      "ويعنى الدرس بمقاصد السورة: التوحيد والرسالة والمسؤولية، وقصة الإسراء ودلالاتها، وأحكام البنين والآباء والمال والقول، مع التمرن على التفسير الموضوعي وربط الآيات بقضايا الإنسان المعاصر.",
    ],
    fr: [
      "En deuxième année du cycle secondaire, l'étude du <em>al-Muḥarrar al-waǧīz</em> d'Ibn ʿAṭiyya se poursuit : les leçons de ce niveau couvrent l'intégralité de la sourate al-Isrāʾ (le Voyage nocturne).",
      "L'enseignement veille aux finalités de la sourate — unicité, mission prophétique et responsabilité —, au récit du Voyage nocturne et à sa portée, aux règles touchant les enfants, les parents, les biens et la parole, et entraîne à l'exégèse thématique ainsi qu'au rattachement des versets aux questions de l'homme contemporain.",
    ],
  },

  /* ————— ʿUlūm al-Qurʾān, 2ᵉ collège ————— */
  "ulum-quran-2es": {
    ar: [
      "تقدم مادة علوم القرآن في السنة الثانية من السلك الإعدادي العتيق مدخلا منهجيا لعلوم كتاب الله: التفسير مفهومه وشروطه وآدابه، وتطوره في عهد النبوة والصحابة والتابعين، وعصر التدوين، وأقسامه بالمأثور والرأي، ومصادره ومناهجه.",
      "ثم تعالج المادة ترجمة القرآن الكريم وأحكامها، والتفسير الفقهي والكوني والإشاري، بما يكوّن لدى التلميذ ملكة تصور تاريخي منضبط لعلم التفسير ومدارسه.",
    ],
    fr: [
      "En deuxième année du cycle intermédiaire, la matière des sciences coraniques offre une entrée systématique dans les sciences du Livre de Dieu : l'exégèse — notion, conditions et bienséances —, son développement à l'époque prophétique, celle des Compagnons et des Successeurs puis à l'ère de la mise par écrit, sa division en exégèse transmise (maʾṯūr) et fondée sur l'opinion (raʾy), ainsi que ses sources et ses méthodes.",
      "La matière aborde ensuite la traduction du Noble Coran et son statut, ainsi que l'exégèse juridique, cosmique et allusive, afin de doter l'élève d'une représentation historique rigoureuse de la science du tafsīr et de ses écoles.",
    ],
  },

  /* ————— ʿUlūm al-Qurʾān (Manāhil al-ʿIrfān), 3ᵉ collège ————— */
  "ulum-quran-3es": {
    ar: [
      "تختم مادة علوم القرآن في السنة الثالثة من السلك الإعدادي العتيق بدروس من «مناهل العرفان في علوم القرآن» للعلامة محمد عبد العظيم الزرقاني (ت 1367هـ)، وهو من أنفع المدرس في بابه.",
      "وتعالج الدروس إعجاز القرآن وأنواعه، والنسخ وأحكامه، والقراءات القرآنية وشروط قبولها واختلافها وفضل قراء القرآن، مع أنشطة التقويم والدعم، وبذلك يكتمل للتلميذ التصور المنهجي لعلوم القرآن قبل مرحلة الثانوي.",
    ],
    fr: [
      "La matière des sciences coraniques s'achève en troisième année du cycle intermédiaire par des leçons tirées du <em>Manāhil al-ʿIrfān fī ʿulūm al-Qurʾān</em> du savant Muḥammad ʿAbd al-ʿAẓīm al-Zarqānī (m. 1367/1948), l'un des manuels les plus profitables en la matière.",
      "Les leçons traitent du caractère inimitable du Coran (<em>iʿǧāz</em>) et de ses espèces, de l'abrogation (<em>nasḫ</em>) et de ses règles, des lectures coraniques — conditions d'acceptation, divergences et mérite des lecteurs —, avec des activités d'évaluation et de consolidation : l'élève achève ainsi la représentation méthodique des sciences coraniques avant le cycle secondaire.",
    ],
  },

  /* ————— Risāla d'Ibn Abī Zayd (tawḥīd), 1ᵉʳ collège ————— */
  "tawhid-1es": {
    ar: [
      "تفتتح مادة التوحيد في السنة الأولى من السلك الإعدادي العتيق بمقدمة «رسالة» الإمام أبي محمد عبد الله بن أبي زيد القيرواني (ت 386هـ)، فقيه المغرب وإمام المالكية في عصره، بشرح «كفاية الطالب الرباني» لأبي الحسن، وهو الشرح المعتمد في التعليم العتيق المغربي.",
      "وتعرض المادة عقيدة أهل السنة والجماعة على مذهب الإمام مالك كما صورتها المقدمة: صفات الله تعالى ووجوبها واستحالة نقيضها، والقضاء والقدر، والإيمان بالغيبيات كلها، وما يجب في حق الرسل والصحابة، بلغة تعليمية مبسطة.",
    ],
    fr: [
      "La matière du tawḥīd s'ouvre en première année du cycle intermédiaire avec l'introduction de la <em>Risāla</em> de l'imam Abū Muḥammad ʿAbd Allāh b. Abī Zayd al-Qayrawānī (m. 386/996), le juriste du Maghreb et imam des malikites de son temps, commentée par la <em>Kifāyat al-ṭālib al-rabbānī</em> d'Abū al-Ḥasan — le commentaire agréé par l'enseignement traditionnel marocain.",
      "La matière expose la doctrine des gens de la Sunna et de la Communauté selon l'école de l'imam Mālik, telle que la fixe cette introduction : les attributs divins — nécessaires et dont le contraire est impossible —, le décret et la prédestination, la foi en l'ensemble des réalités invisibles et ce qui est dû aux messagers et aux Compagnons, dans une langue pédagogique simplifiée.",
    ],
  },

  /* ————— Muršid al-muʿīn d'Ibn ʿĀšir (tawḥīd), 2ᵉ collège ————— */
  "tawhid-2es": {
    ar: [
      "تتوالى مادة التوحيد في السنة الثانية من السلك الإعدادي العتيق على منظومة «المرشد المعين على الضروري من علوم الدين» للفقيه المربي عبد الواحد بن عاشر الفاسي (ت 1040هـ)، بشرح «مختصر الدر الثمين» للعلامة محمد بن أحمد ميارة (ت 1072هـ).",
      "وتدرس المادة قسم التوحيد من المنظومة: الحكم العقلي وأقسامه، والصفات الواجبة والمستحيلة والجائزة في حق الله تعالى وحق الرسل عليهم السلام، ومراتب الدين الثلاث، على نسق مذهبي أشعري سني مما اعتمده المغاربة قرونا.",
    ],
    fr: [
      "La matière du tawḥīd se poursuit en deuxième année du cycle intermédiaire avec le poème <em>al-Muršid al-muʿīn ʿalā al-ḍarūrī min ʿulūm al-dīn</em> du juriste et éducateur ʿAbd al-Wāḥid b. ʿĀšir al-Fāsī (m. 1040/1631), commenté par le <em>Muḫtaṣar al-Durr al-ṯamīn</em> du savant Muḥammad b. Aḥmad Mayyāra (m. 1072/1661).",
      "La matière étudie la section du tawḥīd du poème : le jugement rationnel et ses catégories, les attributs nécessaires, impossibles et possibles de Dieu Très-Haut comme des messagers (sur eux la paix), et les trois degrés de la religion — selon la trame ašʿarite sunnite que les Marocains ont adoptée depuis des siècles.",
    ],
  },

  /* ————— ʿUmdat al-bayān (rasm), 4ᵉ primaire ————— */
  "rasm-wa-dabt-4ep": {
    ar: [
      "يشرع التلميذ في السنة الرابعة من التعليم الابتدائي العتيق في دراسة رسم المصحف وضبطه من خلال أرجوزة «عمدة البيان في حكم المحذوف من كلام الرحمن» للعلامة إدريس الودغيري، بشرح «بهجة النظر والعيان» للعلامة محمد بن العربي المساري.",
      "وتقدم المادة مدخلا تأريخيا لنشأة علم الرسم والضبط وتطوره، ثم تدرس أحكام المحذوف من حروف الكلمات القرآنية حرفا حرفا، بما يرسخ لدى التلميذ ملكة كتابة المصحف على رسمه العثماني المعتمد.",
    ],
    fr: [
      "En quatrième année du cycle primaire, l'élève entreprend l'étude de la graphie (<em>rasm</em>) et de la vocalisation (<em>ḍabṭ</em>) du muṣḥaf à travers le poème <em>ʿUmdat al-bayān fī ḥukm al-maḥḏūf min kalām al-Raḥmān</em> du savant Idrīs al-Wadghīrī, commenté par la <em>Bahǧat al-naẓar wa-l-ʿiyān</em> de Muḥammad b. al-ʿArabī al-Masārī.",
      "La matière offre d'abord une introduction historique à la naissance et au développement de la science de la graphie et de la vocalisation, puis étudie lettre à lettre les règles d'élision des lettres dans les mots coraniques, afin d'ancrer chez l'élève la capacité d'écrire le muṣḥaf selon la graphie ʿuṯmānienne agréée.",
    ],
  },

  /* ————— al-Muqniʿ d'al-Marghīthī (tawqīt), 1ʳᵉ lycée ————— */
  "taqtit-tanawi-1": {
    ar: [
      "تبدأ مادة التقطيع في السنة الأولى من السلك الثانوي العتيق بعلم التوقيت من خلال منظومة «المقنع» للعلامة محمد بن سعيد المرغتي بشرحه المسمى «المطلع على مسائل المقنع»، في أثر علم التوقيت عند المغاربة: علم مواقيت الصلاة والعبادات وحساب الأهلة والسنين.",
      "وتعالج الدروس حروف الجمل وقيمها العددية، وأيام العام العربي والعجمي وأسماء الشهور، والمنازل والبروج، والاعتدالين والانقلابين، وحساب درجة الشمس في بروجها ومنزلتها لكل تاريخ، ومعرفة برج القمر، وأوقات الصلوات بظل الشمس، وأنشطة البحث والتعلم الذاتي.",
    ],
    fr: [
      "La matière de la découpe coranique (<em>taqṭīʿ</em>) commence en première année du cycle secondaire par la science du comput des temps (<em>tawqīt</em>) à travers le poème <em>al-Muqniʿ</em> du savant Muḥammad b. Saʿīd al-Marghīthī, commenté par <em>al-Muṭlaʿ ʿalā masāʾil al-Muqniʿ</em> — un héritage de la science du comput chez les Marocains : heures des prières et des cultes, calcul des lunaisons et des années.",
      "Les leçons traitent des lettres numérales (abǧad) et de leurs valeurs, des jours de l'année arabe et persane et des noms des mois, des stations lunaires et des signes zodiacaux, des équinoxes et des solstices, du calcul du degré du soleil dans son signe et de sa position pour toute date, de la détermination du signe de la lune, des heures des prières par l'ombre solaire, avec des activités de recherche et d'apprentissage autonome.",
    ],
  },

  /* ————— Sullam d'al-Akhdarī (mantiq), 1ʳᵉ lycée ————— */
  "mantiq-tanawi-1": {
    ar: [
      "يفتتح التلميذ في السنة الأولى من السلك الثانوي العتيق دراسة المنطق بمنظومة «السلم المنورق» للعلامة عبد الرحمن الأخضري (ت 953هـ) بشرح حسن القويسني، وهي المتن التعليمي الأشهر في المقدمة المنطقية بالتعليم المغربي العتيق.",
      "وتمر المادة بمباحث الألفاظ ومفاهيمها، والكليات الخمس، والخبر والطلب، والنسبة بين الألفاظ والمعاني، وأنواع المعرف والنكر، وشروطها، مع أنشطة لاستثمار التعلمات، فيتكون لدى التلميذ السلاح الفكري الذي قصده المتقدمون لصون النظر وصحة الاستدلال.",
    ],
    fr: [
      "En première année du cycle secondaire, l'élève aborde la logique (<em>manṭiq</em>) avec le poème <em>al-Sullam al-munawraq</em> du savant ʿAbd al-Raḥmān al-Akhḍarī (m. 953/1546), commenté par Ḥasan al-Qwaysnī — le manuel d'introduction à la logique le plus répandu dans l'enseignement traditionnel marocain.",
      "La matière parcourt les questions des termes et de leurs concepts, les cinq universaux, l'énoncé assertorique et l'injonctif, la relation des termes aux sens, les espèces du défini et de l'indéfini et leurs conditions, avec des activités de valorisation des acquis : l'élève acquiert ainsi l'outillage intellectuel que les anciens destinaient à préserver la justesse du raisonnement et de la preuve.",
    ],
  },
};

/* ————————————————— Application ————————————————— */
const fixed: string[] = [];
for (const [id, intro] of Object.entries(I)) {
  const p = path.join(BOOKS, id + ".json");
  const b = JSON.parse(readFileSync(p, "utf8"));
  if (b.intro && (b.intro.htmlFr || "").trim()) { console.log("−", id, ": intro déjà présente, ignorée"); continue; }
  b.intro = {
    docId: "muqaddima",
    titleAr: "تقديم الكتاب",
    titleFr: "Présentation du manuel",
    html: intro.ar.map((x) => `<p>${x}</p>`).join("\n"),
    htmlFr: intro.fr.map((x) => `<p>${x}</p>`).join("\n"),
  };
  writeFileSync(p, JSON.stringify(b, null, 1) + "\n");
  fixed.push(id);
}
console.log(`Intros ajoutées : ${fixed.length} → ${fixed.join(", ")}`);
