/**
 * Minhāj R9 (lot 2) — Retraduction manuelle : titres GT-ismes résiduels
 * (tawḥīd 1es/2es, tajwīd 2es/5ep/6ep, qirāʾāt numérotés, tawqīt t1,
 * fiqh/hadith « Décisions… », apparat des livres).
 * Usage: bun run scripts-recovery/r9-fix-titles2.ts
 */
import { readFileSync, writeFileSync, readdirSync } from "fs";
import path from "path";

const BOOKS = path.join(process.cwd(), "content", "books");

function norm(ar: string): string {
  return ar
    .replace(/&nbsp;/g, " ")
    .replace(/[\u064B-\u0652\u0670\u0640\u06D6-\u06ED]/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

const D: Record<string, string> = {
  /* ============ Tawḥīd — 1es (Risāla d'Ibn Abī Zayd) ============ */
  "التوحيد ما يجب اعتقاده بالقلب والنطق به": "Le tawḥīd : ce que le cœur doit croire et la langue professer",
  "التوحيد سبب تأليف رسالة ابن أبي زيد القيرواني ومحتواها": "Le tawḥīd : le motif de la rédaction de la Risāla d'Ibn Abī Zayd al-Qayrawānī et son contenu",
  "التوحيد تنزيه الله تعالى عن إحاطة المخلوق بذاته وعلمه": "Le tawḥīd : la transcendance divine à l'égard de l'embrassement de Son essence et de Sa science par la créature",
  "التوحيد من أسماء الله الحسنى الدالة على صفاته": "Le tawḥīd : parmi les plus beaux noms de Dieu indiquant Ses attributs",
  "التوحيد إحاطة علمه سبحانه بكل شيء": "Le tawḥīd : Sa science — glorifié soit-Il — embrasse toute chose",
  "التوحيد أزلية صفاته عز وجل وتكليمه موسى عليه السلام": "Le tawḥīd : l'éternité de Ses attributs et Son adresse à Mūsā (sur lui la paix)",
  "التوحيد الإيمان بالقضاء والقدر": "Le tawḥīd : la foi au décret et à la prédestination (qaḍāʾ et qadar)",
  "التوحيد الهداية والإضلال مما سبق به علم اللطيف الخبير": "Le tawḥīd : la guidance et l'égarement, conformément à la prescience du Subtil, le Bien-Informé",
  "التوحيد القول في المشيئة والسعادة والشقاء": "Le tawḥīd : la volonté divine (mašīʾa), la félicité et l'infortune",
  "التوحيد ربوبيته تعالى للعالمين وبعثته للرسل إليهم": "Le tawḥīd : Sa seigneurie sur les mondes et l'envoi des messagers",
  "التوحيد رسالة سيدنا محمد صلى الله عيه وسلم خاتمة الرسالات السماوية": "Le tawḥīd : la mission de notre maître Muḥammad ﷺ, sceau des révélations célestes",
  "التوحيد الإيمان بقيام الساعة والبعث والجزاء": "Le tawḥīd : la foi en la survenue de l'Heure, la résurrection et la rétribution",
  "التوحيد خروج عصاة المومنين من النار بشفاعة النبي صلى الله عليه وسلم": "Le tawḥīd : la sortie des croyants désobéissants du Feu par l'intercession du Prophète ﷺ",
  "التوحيد الجنة وأهلها ونعيمها": "Le tawḥīd : le Paradis, ses habitants et ses délices",
  "التوحيد عرض الخلائق بين يدي الله تعالى 2": "Le tawḥīd : la présentation des créatures devant Dieu Très-Haut (2)",
  "التوحيد الإيمان بالميزان وإيتاء الصحف": "Le tawḥīd : la foi en la Balance et la remise des feuillets",
  "التوحيد الإيمان بالصراط": "Le tawḥīd : la foi au Pont (ṣirāṭ)",
  "التوحيد الإيمان بحوض النبي صلى الله عليه وسلم وبيان من يرده": "Le tawḥīd : la foi au Bassin du Prophète ﷺ et ses visiteurs",
  "التوحيد مفهوم الإيمان ومراتبه": "Le tawḥīd : la notion de foi (īmān) et ses degrés",
  "التوحيد منع تكفير أحد من أهل القبلة بذنب وما يجب الإيمان به من الغيبيات": "Le tawḥīd : l'interdiction d'excommunier un gens-de-la-qibla pour un péché ; les réalités invisibles à croire",
  "التوحيد الإيمان بالملائكة عليهم السلام": "Le tawḥīd : la foi aux anges (sur eux la paix)",
  "التوحيد تفاضل القرون وأفضلية الخلفاء الراشدين": "Le tawḥīd : la hiérarchie des générations et la supériorité des califes bien guidés",
  "التوحيد ما يجب اعتقاده في شأن الصحابة رضي الله عنهم": "Le tawḥīd : ce qu'il faut croire au sujet des Compagnons (qu'Allāh les agrée)",
  "التوحيد وجوب طاعة ولي الأمر وترك المراء في الدين": "Le tawḥīd : l'obligation d'obéir au détenteur de l'autorité et de délaisser la dispute en religion",

  /* ============ Tawḥīd — 2es (Murshid Mayyāra) ============ */
  "التوحيد حقيقته ومقاصده": "Le tawḥīd : sa réalité et ses finalités",
  "التوحيد أول ما يجب على المكلف وشروط التكليف": "Le tawḥīd : la première obligation du sujet responsable (mukallaf) et les conditions de la charge",
  "التوحيد الحكم العقلي وأقسامه": "Le tawḥīd : le jugement rationnel et ses catégories",
  "التوحيد من الصفات الواجبة في حقه جل جلاله الوجود القدم البقاء": "Le tawḥīd : attributs nécessaires — l'existence, l'éternité antérieure (qidam) et la pérennité (baqāʾ)",
  "التوحيد من الصفات الواجبة في حقه جل جلاله الغنى المطلق المخالفة للحوادث الوحدانية": "Le tawḥīd : attributs nécessaires — la richesse absolue, la dissemblance avec le créé et l'unicité",
  "التوحيد صفات المعاني القدرة الإرادة العلم الحياة": "Le tawḥīd : les attributs de qualification — puissance, volonté, science et vie",
  "التوحيد صفات المعاني القدرة الإرادة العلم الحياة 3": "Le tawḥīd : les attributs de qualification — puissance, volonté, science et vie (3)",
  "التوحيد صفات المعاني القدرة الإرادة العلم الحياة 5": "Le tawḥīd : les attributs de qualification — puissance, volonté, science et vie (5)",
  "التوحيد صفات المعاني القدرة الإرادة العلم الحياة 6": "Le tawḥīd : les attributs de qualification — puissance, volonté, science et vie (6)",
  "التوحيد صفات المعاني القدرة الإرادة العلم الحياة 8": "Le tawḥīd : les attributs de qualification — puissance, volonté, science et vie (8)",
  "التوحيد صفات المعاني القدرة الإرادة العلم الحياة 9": "Le tawḥīd : les attributs de qualification — puissance, volonté, science et vie (9)",
  "التوحيد صفات المعاني القدرة الإرادة العلم الحياة 10": "Le tawḥīd : les attributs de qualification — puissance, volonté, science et vie (10)",
  "التوحيد صفات المعاني القدرة الإرادة العلم الحياة 11": "Le tawḥīd : les attributs de qualification — puissance, volonté, science et vie (11)",
  "التوحيد ما يستحيل في حق الله تعالى العجز والكراهة والجهل والممات والصمم والبكم والعمى": "Le tawḥīd : les attributs impossibles — impuissance, contrainte, ignorance, mort, surdité, mutisme et cécité",
  "التوحيد دلال وجوب اتصافه سبحانه وتعالى بالحياة والإرادة والعلم والقدرة": "Le tawḥīd : la preuve de la nécessité de Ses attributs de vie, volonté, science et puissance",
  "دليل وجوب اتصافه تعالى بالسمع والبصر والكلام 2": "La preuve de Ses attributs d'ouïe, de vue et de parole (2)",
  "ما يجب في حق الرسل وما يستحيل وما يجوز": "Les attributs des messagers : nécessaires, impossibles et possibles",
  "دليل ما يجب وما يستحيل على الرسل عليهم الصلاة والسلام": "La preuve des attributs nécessaires et impossibles des messagers (sur eux la prière et la paix)",
  "براهين مايجوز في حق الرسل عليهم الصلاة والسلام": "Les preuves des attributs possibles des messagers (sur eux la prière et la paix)",
  "قول لا لإله إلا الله محمد رسول الله علامة الإيمان": "La profession « Lā ilāha illā Allāh, Muḥammad rasūl Allāh », marque de la foi",
  "التوحيد الدين مراتب الإسلام والإيمان والإحسان": "Le tawḥīd : les degrés de la religion — islam, īmān et iḥsān",
  "التوحيد أنشطة عامة للدعم والتثبيت": "Le tawḥīd : activités générales de consolidation",

  /* ============ Tajwīd — 2es (Durar al-Lawāmiʿ) ============ */
  "التجويد أحوال الهمز وأسباب تغييره": "Le tajwīd : les états du hamza et les causes de son altération",
  "التجويد حكم الهمزتين في كلمة": "Le tajwīd : le statut des deux hamza en un mot",
  "التجويد حكم الهمزتين من كلمة عند قالون": "Le tajwīd : les deux hamza d'un mot selon Qālūn",
  "التجويد حكم الهمزتين المفتوحتين من كلمتين عند قالون وورش": "Le tajwīd : les deux hamza fatḥés en deux mots, selon Qālūn et Warš",
  "التجويد حكم الهمزتين المكسورتين من كلمتين عند ورش": "Le tajwīd : les deux hamza kasrés en deux mots, selon Warš",
  "التجويد حكم الهمزتين المكسورتين من كلمتين عند قالون": "Le tajwīd : les deux hamza kasrés en deux mots, selon Qālūn",
  "التجويد حكم الهمزتين المضمومتين من كلمتين عند قالون وورش": "Le tajwīd : les deux hamza ḍammés en deux mots, selon Qālūn et Warš",
  "التجويد حكم الهمزتين المختلفتين في الحركة من كلمتين عند نافع": "Le tajwīd : les deux hamza de voyelles différentes en deux mots, selon Nāfiʿ",
  "التجويد حكم اجتماع همزة الاستفهام مع همزة الوصل 2": "Le tajwīd : la rencontre du hamza interrogatif et du hamza de liaison (2)",
  "التجويد حكم الاستفهام المكرر": "Le tajwīd : l'interrogation redoublée (istifhām mukarrar)",
  "التجويد تطبيقات على الهمز المزدوج": "Le tajwīd : applications sur le double hamza",
  "التجويد الهمز المفرد إبدال فاء الفعل عند ورش": "Le tajwīd : le hamza unique — l'altération du hamza initial du verbe selon Warš",
  "التجويد حكم الهمز المفرد الواقع عينا ولاما": "Le tajwīd : le hamza unique en position de ʿayn ou de lām [radicales]",
  "التجويد أحكام نقل الحركة 2": "Le tajwīd : les règles du transfert de voyelle (naql) (2)",
  "التجويد حكم نقل الحركة للام التعريف ولفظ كتابيه": "Le tajwīd : le transfert de voyelle vers le lām de l'article défini et le mot « kitābayhi »",
  "التجويد نقل الحركة عند نافع وتوجيهه": "Le tajwīd : le transfert de voyelle chez Nāfiʿ et sa justification",
  "التجويد باب الإظهار والإدغام حكم ذال إذ": "Le tajwīd : iẓhār et idġām — le statut du ḏāl de « iḏ »",
  "التجويد حكم دال قد باب الإظهار والإدغام": "Le tajwīd : iẓhār et idġām — le dāl de « qad »",
  "التجويد حكم تاء التأنيث باب الإظهار والإدغام": "Le tajwīd : iẓhār et idġām — le tāʾ du féminin",
  "التجويد حكم لام هل وبل باب الإظهار": "Le tajwīd : iẓhār — le lām de « hal » et de « bal »",
  "التجويد فصل في إدغام المثلين والمتقاربين": "Le tajwīd : l'idġām des lettres identiques et proches",
  "التجويد مستثنيات في إدغام المتقاربين والمتجانسين": "Le tajwīd : les exceptions à l'idġām des lettres proches et homogènes",
  "التجويد تطبيقات على باب الإظهار والإدغام": "Le tajwīd : applications sur l'iẓhār et l'idġām",
  "التجويد أحكام النون الساكنة والتنوين باب الإظهار والإدغام": "Le tajwīd : règles du nūn quiescent et du tanwīn — iẓhār et idġām",
  "التجويد أحكام النون الساكنة والتنوين القلب والإخفاء": "Le tajwīd : règles du nūn quiescent et du tanwīn — inversion (qalb) et dissimulation (iḫfāʾ)",
  "التجويد تطبيقات على أحكام النون الساكنة والتنوين": "Le tajwīd : applications sur les règles du nūn quiescent et du tanwīn",
  "التجويد متن نظم الدرر اللوامع لابن بري": "Le tajwīd : le mathn al-Durar al-Lawāmiʿ d'Ibn Barrī",

  /* ============ Tajwīd — 5ep ============ */
  "مادة التجويد السنة الخامسة إبتدائي": "Cours de tajwīd — 5ᵉ année primaire",
  "مادة التجويد السنة الخامسة إبتدائي 2": "Cours de tajwīd — 5ᵉ année primaire (2)",
  "مادة التجويد السنة الخامسة إبتدائي 3": "Cours de tajwīd — 5ᵉ année primaire (3)",
  "مادة التجويد السنة الخامسة إبتدائي 4": "Cours de tajwīd — 5ᵉ année primaire (4)",
  "مادة التجويد السنة الخامسة إبتدائي 5": "Cours de tajwīd — 5ᵉ année primaire (5)",
  "مادة التجويد السنة الخامسة إبتدائي 6": "Cours de tajwīd — 5ᵉ année primaire (6)",
  "التجويد تطبيقات على حكم الإدغام في النون الساكنة والتنوين": "Le tajwīd : applications sur l'idġām du nūn quiescent et du tanwīn",
  "التجويد تطبيقات على حكم الإدغام بغير غنة في النون الساكنة والتنوين": "Le tajwīd : applications sur l'idġām sans nasalisation du nūn quiescent et du tanwīn",
  "التجويد تطبيقات على حكم القلب في النون الساكنة والتنوين": "Le tajwīd : applications sur l'inversion (qalb) du nūn quiescent et du tanwīn",
  "التجويد تطبيقات على حكم الإخفاء في النون الساكنة والتنوين": "Le tajwīd : applications sur l'iḫfāʾ du nūn quiescent et du tanwīn",
  "أحكام النون الساكنة والتنوين أنشطة تطبيقية عامة": "Règles du nūn quiescent et du tanwīn — activités d'application générales",
  "التجويد تطبيقات على حكم الإخفاء في الميم الساكنة": "Le tajwīd : applications sur l'iḫfāʾ du mīm quiescent",
  "التجويد: تطبيقات على المد الطبيعي": "Le tajwīd : applications sur l'allongement naturel (madd ṭabīʿī)",
  "التجويد أنشطة تطبيقية عامة على الميم الساكنة": "Le tajwīd : activités d'application générales sur le mīm quiescent",
  "التجويد المد الطبيعي تطبيقات": "Le tajwīd : l'allongement naturel (madd ṭabīʿī) — applications",
  "التجويد تطبيقات على المد المتصل 2": "Le tajwīd : applications sur l'allongement connecté (madd muttaṣil) (2)",
  "التجويد تطبيقات على المد المنفصل 2": "Le tajwīd : applications sur l'allongement séparé (madd munfaṣil) (2)",
  "التجويد المد الطبيعي والمتصل والمنفصل أنشطة تطبيقية": "Le tajwīd : allongements naturel, connecté et séparé — activités d'application",
  "التجويد مد البدل بسبب الهمز الثابت تطبيقات": "Le tajwīd : applications sur l'allongement de substitution (madd al-badal) à hamza stable",
  "التجويد مد البدل بسبب الهمز المتغير تطبيقات": "Le tajwīd : applications sur l'allongement de substitution (madd al-badal) à hamza altéré",
  "التجويد تطبيقات على مد اللين": "Le tajwīd : applications sur l'allongement de mollesse (madd layyin)",
  "التجويد مد البدل واللين أنشطة تطبيقية عامة": "Le tajwīd : madd al-badal et layyin — activités d'application générales",
  "التجويد المد اللازم الكلمي تطبيقات": "Le tajwīd : applications sur l'allongement obligatoire verbal (madd lāzim kalimī)",
  "التجويد المد اللازم الحرفي تطبيقات": "Le tajwīd : applications sur l'allongement obligatoire littéral (madd lāzim ḥarfī)",
  "التجويد المد اللازم والعارض أنشطة تطبيقية عامة": "Le tajwīd : madd lāzim et ʿāriḍ — activités d'application générales",
  "التجويد أحكام الوقف والابتداء تطبيقات": "Le tajwīd : applications sur l'arrêt (waqf) et le départ (ibtidāʾ)",
  "منظومة تحفة الأطفال للجمزوري": "Le mathn Tuḥfat al-Aṭfāl d'al-Ǧamzūrī",
  "التجويد المد العارض للسكون تطبيقات 2": "Le tajwīd : applications sur l'allongement occasionnel (madd ʿāriḍ li-l-sukūn) (2)",
  "التجويد مستثنيات مد البدل تطبيقات": "Le tajwīd : applications sur les exceptions du madd al-badal",

  /* ============ Tajwīd — 6ep (maḫāriǧ / ṣifāt) ============ */
  "التجويد نظم الدرر اللوامع للإمام ابن بري بشرح النجوم الطوالع لإبراهيم المارغني للسنة السادسة من التعليم الابتدائي": "Le tajwīd : le mathn al-Durar al-Lawāmiʿ d'Ibn Barrī, avec le commentaire al-Nuǧūm al-Ṭawāliʿ d'Ibrāhīm al-Māriġnī",
  "التجويد متن الدرر اللوامع لابن بري": "Le tajwīd : le mathn al-Durar al-Lawāmiʿ d'Ibn Barrī",
  "التجويد مخارج الحروف تعريفها وفوائدها": "Le tajwīd : les points d'articulation (maḫāriǧ) — définition et intérêts",
  "التجويد مخارج الحروف العامة والخاصة": "Le tajwīd : points d'articulation généraux et spécifiques",
  "التجويد مخارج الحروف الحلق والجوف": "Le tajwīd : points d'articulation — la gorge et la cavité buccale",
  "مخارج الحروف اللسان القاف والكاف": "Points d'articulation — la langue : qāf et kāf",
  "التجويد مخارج الحروف اللسان الجيم والشين والياء": "Le tajwīd : points d'articulation — la langue : ǧīm, šīn et yāʾ",
  "التجويد مخارج الحروف اللسان الضاد": "Le tajwīd : points d'articulation — la langue : le ḏād",
  "التجويد تطبيقات على مخارج الحلق وأقصى اللسان ووسطه وحافته": "Le tajwīd : applications — la gorge, la racine, le milieu et le tranchant de la langue",
  "التجويد مخارج الحروف اللسان الذال والثاء والظاء": "Le tajwīd : points d'articulation — la langue : ḏāl, ṯāʾ et ẓāʾ",
  "التجويد مخارج الحروف اللسان اللام والراء والنون": "Le tajwīd : points d'articulation — la langue : lām, rāʾ et nūn",
  "التجويد مخارج الحروف اللسان الطاء والتاء والدال": "Le tajwīd : points d'articulation — la langue : ṭāʾ, tāʾ et dāl",
  "التجويد مخارج الحروف اللسان الصاد والزاي والسين": "Le tajwīd : points d'articulation — la langue : ṣād, zāy et sīn",
  "التجويد مخارج الحروف الشفتان والخيشيوم": "Le tajwīd : points d'articulation — les lèvres et la cavité nasale",
  "التجويد تطبيقات على مخارج طرف اللسان والشفتين والخيشوم": "Le tajwīd : applications — la pointe de la langue, les lèvres et le nez",
  "التجويد صفات الحروف فوائدها وأقسامها": "Le tajwīd : les qualités des lettres (ṣifāt) — intérêts et catégories",
  "التجويد الصفات التي لها ضد الهمس والجهر": "Le tajwīd : qualités opposées — le chuchotement (hams) et la sonorité (ǧahr)",
  "التجويد الصفات التي لها ضد الشدة والرخاوة والبينية": "Le tajwīd : qualités opposées — tension (šidda), mollesse (raxāwa) et intermédiaire (bayniyya)",
  "التجويد الصفات التي لها ضد الانسفال والاستعلاء": "Le tajwīd : qualités opposées — l'abaissement (istifāl) et l'élévation (istiʿlāʾ)",
  "التجويد الصفات التي لها ضد الإطباق والانفتاح": "Le tajwīd : qualités opposées — l'occlusion (iṭbāq) et l'ouverture (infitāḥ)",
  "التجويد الذلاقة والإصمات": "Le tajwīd : la vélocité (ḏalāqa) et l'inaptitude (iṣmāt)",
  "التجويد تطبيقات على الصفات التي لها ضد 2": "Le tajwīd : applications sur les qualités opposées (2)",
  "التجويد الصفات التي لا ضد لها الصفير والتفشي": "Le tajwīd : qualités sans opposé — le sifflement (ṣafīr) et l'expansion (tafaššī)",
  "التجويد الصفات التي لا ضد لها الاستطالة والانحراف والتكرير": "Le tajwīd : qualités sans opposé — l'étendue (istiṭāla), la déviation (inḥirāf) et le roulement (takrīr)",
  "التجويد القلقلة واللين": "Le tajwīd : le rebond (qalqala) et la mollesse (layyin)",
  "التجويد باب الغنة 2": "Le tajwīd : chapitre de la nasalisation (ġunna) (2)",
  "التجويد تطبيقات على الصفات التي ليس لها ضد 3": "Le tajwīd : applications sur les qualités sans opposé (3)",
  "التجويد جدول بحروف الهجاء مع مخارجها وصفاتها": "Le tajwīd : tableau des lettres avec points d'articulation et qualités",

  /* ============ Qirāʾāt — chapitres numérotés (Shāṭibiyya / Ibn al-Qāṣiḥ) ============ */
  "1. باب الهمزتين من كلمة (1)": "1. Chapitre des deux hamza en un seul mot (1)",
  "2. ﴿ءامنتم﴾ باب الهمزتين من كلمة (2) كلمة": "2. ﴿Āmantum﴾ ; chapitre des deux hamza en un seul mot (2)",
  "3.باب الهمزتين من كلمة (3)": "3. Chapitre des deux hamza en un seul mot (3)",
  "4. باب الهمزتين من كلمة (4)": "4. Chapitre des deux hamza en un seul mot (4)",
  "5. باب الهمزتين من كلمتين (1)": "5. Chapitre des deux hamza en deux mots (1)",
  "6. باب الهمزتين من كلمتين (2)": "6. Chapitre des deux hamza en deux mots (2)",
  "7. باب الهمز المفرد (1)": "7. Chapitre du hamza unique (1)",
  "8. باب الهمز المفرد (2)": "8. Chapitre du hamza unique (2)",
  "9. باب نقل حركة الهمزة إلى الساكن قبلها": "9. Chapitre du transfert de la voyelle du hamza vers la consonne quiescente précédente",
  "10. باب وقف حمزة وهشام على الهمز (1)": "10. Chapitre : l'arrêt de Ḥamza et Hišām sur le hamza (1)",
  "11. باب وقف حمزة وهشام على الهمز (2)": "11. Chapitre : l'arrêt de Ḥamza et Hišām sur le hamza (2)",
  "12. باب وقف حمزة وهشام على الهمز (3)": "12. Chapitre : l'arrêt de Ḥamza et Hišām sur le hamza (3)",
  "14. باب الإظهار والإدغام: ذكر ذال «إذ»": "14. Chapitre de l'iẓhār et de l'idġām : le ḏāl de « iḏ »",
  "15. ذكر دال «قد» وتاء التأنيث": "15. Le dāl de « qad » et le tāʾ du féminin",
  "16. ذكر لام «هل» و«بل» باب اتفاقهم في إدغام الحروف الخمسة": "16. Le lām de « hal » et de « bal » ; chapitre de leur accord sur l'idġām des cinq lettres",
  "17. باب حروف قربت مخارجها (1)": "17. Chapitre des lettres aux points d'articulation proches (1)",
  "18. باب حروف قربت مخارجها (2)": "18. Chapitre des lettres aux points d'articulation proches (2)",
  "19. باب أحكام النون الساكنة والتنوين": "19. Chapitre des règles du nūn quiescent et du tanwīn",
  "20. باب الفتح والإمالة وبين اللفظين (1)": "20. Chapitre du fatḥ, de l'imāla et de l'intermédiaire (1)",
  "21. باب الفتح والإمالة وبين اللفظين (2)": "21. Chapitre du fatḥ, de l'imāla et de l'intermédiaire (2)",
  "22. باب الفتح والإمالة وبين اللفظين(3)": "22. Chapitre du fatḥ, de l'imāla et de l'intermédiaire (3)",
  "23. باب الفتح والإمالة وبين اللفظين(4)": "23. Chapitre du fatḥ, de l'imāla et de l'intermédiaire (4)",
  "24. باب الفتح والإمالة وبين اللفظين(5)": "24. Chapitre du fatḥ, de l'imāla et de l'intermédiaire (5)",
  "25. باب الفتح والإمالة وبين اللفظين (6) وباب مذهب الكسائي في إمالة هاء التأنيث في الوقف": "25. Chapitre du fatḥ, de l'imāla et de l'intermédiaire (6) ; l'école d'al-Kisāʾī sur l'imāla du hāʾ féminin à l'arrêt",
  "1. باب مذاهبهم في الراءات (1)": "1. Chapitre : leurs écoles au sujet des rāʾ (1)",
  "2. باب مذاهبهم في الراءات (2)": "2. Chapitre : leurs écoles au sujet des rāʾ (2)",
  "3. باب مذاهبهم في الراءات (3)": "3. Chapitre : leurs écoles au sujet des rāʾ (3)",
  "4. باب اللامات": "4. Chapitre des lām",
  "5. باب الوقف على أواخر الكلم (1)": "5. Chapitre de l'arrêt sur les fins de mots (1)",
  "6. باب الوقف على أواخر الكلم (2)": "6. Chapitre de l'arrêt sur les fins de mots (2)",
  "7. باب الوقف على مرسوم الخط (1)": "7. Chapitre de l'arrêt conforme à la graphie du muṣḥaf (1)",
  "8. باب الوقف على مرسوم الخط (2)": "8. Chapitre de l'arrêt conforme à la graphie du muṣḥaf (2)",
  "9. باب الوقف على مرسوم الخط (3)": "9. Chapitre de l'arrêt conforme à la graphie du muṣḥaf (3)",
  "11. مذاهب القراء في ياءات الإضافة (1)": "11. Les écoles des lecteurs sur les yāʾ de liaison (1)",
  "12. مذاهب القراء في ياءات الإضافة (2)": "12. Les écoles des lecteurs sur les yāʾ de liaison (2)",
  "13. مذاهب القراء في ياءات الإضافة (3)": "13. Les écoles des lecteurs sur les yāʾ de liaison (3)",
  "14. مذاهب القراء في ياءات الإضافة (4)": "14. Les écoles des lecteurs sur les yāʾ de liaison (4)",
  "15. مذاهب القراء في ياءات الإضافة (5)": "15. Les écoles des lecteurs sur les yāʾ de liaison (5)",
  "16. ياءات الزوائد (1)": "16. Les yāʾ pléonastiques (zawāʾid) (1)",
  "17. ياءات الزوائد (2)": "17. Les yāʾ pléonastiques (zawāʾid) (2)",
  "18. ياءات الزوائد (3)": "18. Les yāʾ pléonastiques (zawāʾid) (3)",
  "19. ياءات الزوائد (4)": "19. Les yāʾ pléonastiques (zawāʾid) (4)",
  "القراءات إدغام الحرفين المتقاربين في كلمة و في كلمتين 1": "Les qirāʾāt : l'idġām de deux lettres proches, en un mot et en deux mots (1)",
  "القراءات إدغام الحرفين المتقابلين في كلمتين 2": "Les qirāʾāt : l'idġām de deux lettres en vis-à-vis, en deux mots (2)",
  "القراءات إدغام الحرفين المتقابلين في كلمتين 3": "Les qirāʾāt : l'idġām de deux lettres en vis-à-vis, en deux mots (3)",
  "القراءات إدغام الحرفين المتقابلين في كلمتين 4": "Les qirāʾāt : l'idġām de deux lettres en vis-à-vis, en deux mots (4)",
  "القراءات البسملة": "Les qirāʾāt : la basmala",
  "القراءات سورة أم القرآن": "Les qirāʾāt : la sourate Umm al-Qurʾān (al-Fātiḥa)",
  "القراءات الإدغام الكبير 1": "Les qirāʾāt : la grande assimilation (idġām kabīr) (1)",
  "القراءات الإدغام الكبير 2": "Les qirāʾāt : la grande assimilation (idġām kabīr) (2)",
  "القراءات أنشطة الدعم والتثبيت": "Les qirāʾāt : activités de soutien et de consolidation",

  /* ============ Tawqīt — taqtit-t1 (al-Muqniʿ / al-Marġīṯī) ============ */
  "التوقيت حروف الجمل": "Le tawqīt : les valeurs numériques des lettres (ḥurūf al-ǧumal)",
  "التوقيت عملية استخراج درجة الشمس في برجها 2": "Le tawqīt : le calcul du degré du soleil dans son signe (2)",
  "معرفة وقت صلاة الظهر والعصر بظل الشمس": "La détermination de l'heure du ẓuhr et du ʿaṣr par l'ombre solaire",
  "التوقيت معرفة الساعات، والطالع، والمنزل المتوسط في السماء وقت المغرب والعشاء والسحور والفجر": "Le tawqīt : les heures, l'ascendant (ṭāliʿ) et la mansion médiane, au maġrib, ʿišāʾ, saḥūr et faǧr",
  "التوقيت معرفة الساعات، والطالع، والمنزل المتوسط في السماء وقت المغرب والعشاء والسحور والفجر 2": "Le tawqīt : les heures, l'ascendant (ṭāliʿ) et la mansion médiane, au maġrib, ʿišāʾ, saḥūr et faǧr (2)",

  /* ============ Fiqh / hadith « Décisions… » résiduels ============ */
  "أحكام القنوت والتشهد الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Les règles de la qunūt et du tashahhud",
  "أحكام البيع بالرؤية والبرنامج والصفة الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Les règles de la vente après inspection, sur plan et sur description",
  "أحكام قضاء الدين متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Les règles de l'acquittement de la dette",
  "أحكام بيع العينة الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Les règles de la vente à réméré (bayʿ al-ʿīna)",
  "أحكام الرد في البيع الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Les règles de la rétrocession (radd) dans la vente",
  "أحكام دم الرعاف والجرح": "Les règles du sang [écoulé] de l'épistaxis et de la blessure",
  "أحكام الحيض والاستحاضة": "Les règles des menstrues et des métrorragies (istiḥāḍa)",
  "أحكام السهو في الصلاة تتمة": "Les règles de l'oubli dans la prière — suite",
  "الفقه أحكام الحوالة": "Le fiqh : les règles de la cession de dette (ḥawāla)",
  "الفقه أحكام شركة العنان 2": "Le fiqh : les règles de l'association inan (širka ʿinān) (2)",
  "أحكام مزدلفة": "Les règles du séjour à Muzdalifa",
  "أحكام الهدي (1)": "Les règles de la bête d'offrande (hady) (1)",
  "أحكام الهدي (2)": "Les règles de la bête d'offrande (hady) (2)",
  "أحكام الحلق والتقصير": "Les règles de la tonsure et de la coupe (ḥalq et taqṣīr)",
  "قبض العلم": "La disparition progressive de la science [religieuse]",

  /* ============ Farāʾiḏ / apparat divers ============ */
  "تصحيح الانكسار": "La correction des partages en cas de majoration (ʿawl)",
  "الصلح": "La transaction (ṣulḥ)",
  "كشاف مصطلحات الشيخ خليل": "Glossaire des termes du Mukhtaṣar de Khalīl",
  "لائحة الأعلام من": "Notices biographiques des figures citées",
  "لائحة المصادر والمرجع من": "Liste des sources et références",
  "فهرس الأعلام من": "Index des figures citées",
  "فهرس المصادر والمراجع من": "Index des sources et références",
  "فهرس الإعلام": "Index des figures citées",
  "ترجمة الأعلام": "Notices biographiques des figures",
  "تراجم الأعلام الواردة في": "Notices biographiques des figures citées",
  "مصادر ومراجع": "Sources et références",
  "مصادر ومراجع": "Sources et références",
};

/* ===================== Application ===================== */
let changed = 0, kept = 0;
const noMatch = new Set<string>();
const files = readdirSync(BOOKS).filter((f) => f.endsWith(".json"));

for (const f of files) {
  const p = path.join(BOOKS, f);
  const b = JSON.parse(readFileSync(p, "utf8"));
  let dirty = false;

  const apply = (d: any) => {
    if (!d || !d.titleAr) return;
    const k = norm(d.titleAr);
    const v = D[k];
    if (v) {
      if (d.titleFr !== v) { d.titleFr = v; changed++; dirty = true; }
      else kept++;
    } else if (!/^(&nbsp;)?سورة/.test(k) && d.pdfOnly) {
      noMatch.add(k);
    }
  };

  apply(b.intro);
  for (const l of b.lessons || []) apply(l);
  if (dirty) writeFileSync(p, JSON.stringify(b, null, 1) + "\n");
}

console.log(`Titres mis à jour : ${changed} | déjà corrects : ${kept}`);
console.log(`pdfOnly restants sans entrée : ${noMatch.size}`);
for (const r of noMatch) console.log("  -", r);
