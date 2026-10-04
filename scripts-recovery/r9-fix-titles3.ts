/**
 * Minhāj R9 (lot 3) — Dernière passe : titres GT-ismes résiduels des leçons
 * intégrales à préfixe livre (sira, ʿulūm al-Qurʾān, fiqh 1es/1ep/t1/t2/t3,
 * ḥadīṯ t1, manṭiq, rasm 4ep…). Usage: bun run scripts-recovery/r9-fix-titles3.ts
 */
import { readFileSync, writeFileSync, readdirSync } from "fs";
import path from "path";

const BOOKS = path.join(process.cwd(), "content", "books");

function norm(ar: string): string {
  return ar.replace(/&nbsp;/g, " ").replace(/[\u064B-\u0652\u0670\u0640\u06D6-\u06ED]/g, "").replace(/\s+/g, " ").trim();
}

const D: Record<string, string> = {
  /* ============ Sīra — 1es ============ */
  "السيرة النبوية المدلول والمقصد درس في السيرة النبوية": "La sīra prophétique : sens et finalité",
  "السيرة النبوية نسبه الشريف ومولده صلى الله عليه وسلم": "La sīra : sa noble lignée et sa naissance ﷺ",
  "السيرة النبوية حادثة شق الصدر واليتم": "La sīra : l'ouverture de poitrine et l'orphelinat",
  "السيرة النبوية حلف الفضول": "La sīra : l'alliance des vertueux (ḥilf al-fuḍūl)",
  "السيرة النبوية أنشطة لتقوية التعلمات ودعمها من الدرس 1 إلى 5": "Activités de renforcement et de consolidation des acquis (leçons 1 à 5)",
  "السيرة النبوية تجارة الرسول صلى الله عليه وسلم بمال خديجة رضي الله عنها وزواجه منها": "Le commerce du Prophète ﷺ avec les biens de Khadīja (qu'Allāh l'agrée) et son mariage avec elle",
  "السيرة النبوية مشاركة الرسول صلى الله عليه وسلم في بناء الكعبة": "La participation du Prophète ﷺ à la reconstruction de la Kaʿba",
  "السيرة النبوية البعثة النبوية بدء الوحي": "La mission prophétique : le début de la révélation",
  "السيرة النبوية خديجة أم المؤمنين رضي الله عنها سند رسول الله صلى الله عليه وسلم": "Khadīja, Mère des croyants (qu'Allāh l'agrée), soutien du Messager de Dieu ﷺ",
  "السيرة النبوية مراحل الدعوة النبوية الدعوة سرا": "Les étapes de la prédication : l'appel en secret",
  "السيرة النبوية السابقون الأولون إلى الإسلام وفضلهم": "Les premiers convertis à l'islam et leur mérite",
  "السيرة النبوية أنشطة لتقوية التعلمات ودعمها من الدرس 6 إلى الدرس 11": "Activités de renforcement et de consolidation des acquis (leçons 6 à 11)",
  "السيرة النبوية مراحل الدعوة النبوية الصدع بالحق": "Les étapes de la prédication : l'appel public à la vérité",
  "السيرة النبوية صبر المؤمنين على الابتلاء": "La patience des croyants face à l'épreuve",
  "السيرة النبوية الهجرة إلى الحبشة": "L'émigration vers l'Abyssinie",
  "السيرة النبوية حوار جعفر رضي الله عنه للنجاشي": "Le discours de Ǧaʿfar (qu'Allāh l'agrée) devant le Naǧāšī",
  "السيرة النبوية التأييد الإلهي للدعوة إسلام حمزة بن عبد المطلب وعمر بن الخطاب رضي الله عنهما": "Le soutien divin : la conversion de Ḥamza b. ʿAbd al-Muṭṭalib et de ʿUmar b. al-Ḫaṭṭāb (qu'Allāh les agrée)",
  "السيرة النبوية أنشطة لتقوية التعلمات ودعمها من الدرس 12 إلى الدرس 16": "Activités de renforcement et de consolidation des acquis (leçons 12 à 16)",
  "السيرة النبوية قريش تفاوض الرسول صلى الله عليه وسلم": "Qurayš négocie avec le Prophète ﷺ",
  "السيرة النبوية حصار الدعوة ومقاطعة أهلها": "Le siège de la prédication et le boycott des siens",
  "الرسول صلى الله عليه وسلم في عام الحزن": "Le Prophète ﷺ en l'année du deuil (ʿām al-ḥuzn)",
  "السيرة النبوية هجرة الرسول صلى الله عليه وسلم إلى الطائف": "Le voyage du Prophète ﷺ à Ṭāʾif",
  "السيرة النبوية معجزة الإسراء والمعراج ودلالاتها": "Le miracle du Voyage nocturne et de l'Ascension, et ses enseignements",
  "السيرة النبوية أخلاق وقيم من سيرة المصطفى صلى الله عليه وسلم": "Éthique et valeurs tirées de la sīra de l'Élu ﷺ",
  "السيرة النبوية أنشطة لتقوية التعلمات ودعمها من الدرس 17 إلى 22": "Activités de renforcement et de consolidation des acquis (leçons 17 à 22)",

  /* ============ Sīra — 2es ============ */
  "تباشير النجاح بيعتا العقبة الأولى والثانية درس في السيرة النبوية": "Les prémices du succès : les deux serments d'al-ʿAqaba",
  "الهجرة النبوية السياق والدوافع درس في السيرة النبوية": "L'Hégire : contexte et motifs",
  "الهجرة النبوية دروس وعبر درس في السيرة النبوية": "L'Hégire : leçons et enseignements",
  "أسس المجتمع الإسلامي الجديد أ بناء المساجد درس في السيرة النبوية": "Les fondements de la nouvelle société (1) : la construction des mosquées",
  "أسس المجتمع الإسلامي الجديد ب المؤاخاة بين المسلمين درس في السيرة النبوية": "Les fondements de la nouvelle société (2) : la fraternité entre les musulmans",
  "أسس المجتمع الإسلامي الجديد ج وثيقة المدينة حقوق المواطنة وواجباتها درس في السيرة النبوية": "Les fondements de la nouvelle société (3) : la Charte de Médine — droits et devoirs de citoyenneté",
  "أنشطة لاستثمار التعلمات ودعمها من الدرس 1 إلى 3": "Activités de valorisation et de consolidation des acquis (leçons 1 à 3)",
  "أنشطة لاستثمار التعلمات ودعمها من الدرس 4 إلى 6 درس في السيرة النبوية": "Activités de valorisation et de consolidation des acquis (leçons 4 à 6)",
  "أبو أيوب الأنصاري رضي الله عنه نموذج في صدق محبة النبي صلى الله عليه وسلم درس في السيرة النبوية التعليم العتبق": "Abū Ayyūb al-Anṣārī (qu'Allāh l'agrée), modèle d'amour sincère du Prophète ﷺ",
  "غزوة بدر الكبرى الأسباب والأحداث والنتائج درس في السيرة النبوية": "La grande bataille de Badr : causes, déroulement et conséquences",
  "غزوة بدر الكبرى المعجزات والدلالات درس في السيرة النبوية": "La grande bataille de Badr : miracles et enseignements",
  "دقة التخطيط في منهاج الدعوة بين بيعتي العقبة وغزوة بدر درس في السيرة النبوية": "La précision de la planification dans la méthode de la prédication, des serments d'al-ʿAqaba à Badr",
  "أنشطة لاستثمار التعلمات ودعمها من الدرس 7 إلى 10 درس في السيرة النبوية": "Activités de valorisation et de consolidation des acquis (leçons 7 à 10)",
  "المجتمع الإسلامي بعد بدر الأمن والعلم والتزكية درس في السيرة النبوية": "La société musulmane après Badr : sécurité, savoir et purification",
  "غزوة أحد دروس وعبر درس في السيرة النبوية": "La bataille d'Uḥud : leçons et enseignements",
  "بعث القراء درس في السيرة النبوية السيرة النبوية": "L'envoi des enseignants du Coran",
  "أنشطة لاستثمار التعلمات ودعمها من الدرس 11 إلى 13 درس في السيرة النبوية التعليم لاالعتيق": "Activités de valorisation et de consolidation des acquis (leçons 11 à 13)",
  "بين أحد والأحزاب درس في السيرة النبوية": "Entre Uḥud et les Coalisés",
  "قريش تحشد الأحزاب ضد المسلمين درس في السيرة النبوية": "Qurayš mobilise les coalisés contre les musulmans",
  "المدد الإلهي وفشل حصار الأحزاب درس في السيرة النبوية": "Le secours divin et l'échec du siège des coalisés",
  "أنشطة لاستثمار التعلمات ودعمها من الدرس 14 إلى 16 درس في السيرة النبوية": "Activités de valorisation et de consolidation des acquis (leçons 14 à 16)",
  "بين بيعتي العقبة والأحزاب أسس التربية النبوية وآثارها درس في السيرة النبوية": "Des serments d'al-ʿAqaba aux Coalisés : les fondements de l'éducation prophétique",
  "مصعب بن عمير رضي الله عنه نموذج لأخلاق الداعية درس في السيرة النبوية": "Muṣʿab b. ʿUmayr (qu'Allāh l'agrée), modèle des mœurs du prédicateur",
  "دور المرأة في خدمة الإسلام نسيبة أم عمارة رضي الله عنها نموذجا درس في السيرة النبوية": "Le rôle des femmes au service de l'islam : Nusayba Umm ʿUmāra (qu'Allāh l'agrée), un modèle",
  "بين الهجرة والأحزاب قبسات من الشمائل المحمدية درس في السيرة النبوية": "De l'Hégire aux Coalisés : lueurs des qualités muhammadiennes",
  "أنشطة لاستثمار التعلمات ودعمها من الدرس 17 إلى 20 درس في السيرة النبوية": "Activités de valorisation et de consolidation des acquis (leçons 17 à 20)",

  /* ============ Sīra — 3es ============ */
  "دور المرأة وإسهاماتها أم المؤمنين أم سلمة رضي الله عنها نموذجا": "Le rôle et la contribution des femmes : Umm Salama (qu'Allāh l'agrée), Mère des croyants, un modèle",
  "السيرة النبوية أنشطة لتعزيز التعلمات ودعمها من الدرس2 إلى الدرس4": "Activités de renforcement et de consolidation des acquis (leçons 2 à 4)",
  "السيرة النبوية محمد صلى الله عليه وسلم الرحمة المهداة للعالمين": "Muḥammad ﷺ, la miséricorde offerte aux mondes",
  "السيرة النبوية يوم خيبر ومؤتة، معجزات وقيم": "Khaybar et Muʾta : miracles et valeurs",
  "السيرة النبوية أنشطة لتعزيز التعلمات ودعمها": "Activités de renforcement et de consolidation des acquis",
  "حادثة الإفك دروس وعبر": "L'affaire de la calomnie (ifk) : leçons et enseignements",
  "صلح الحديبية دروس وعبر": "La trêve d'al-Ḥudaybiyya : leçons et enseignements",

  /* ============ ʿUlūm al-Qurʾān — 1es/2es/3es ============ */
  "علوم القرآن للسنة الثانية من التعليم الإعدادي العتيق": "Présentation du manuel",
  "علوم القرآن التفسير في عهد الرسول صلى الله عليه وسلم وأصحابه رضي الله عنهم": "Le tafsīr à l'époque du Prophète ﷺ et de ses Compagnons (qu'Allāh les agrée)",
  "التمييز بين اتجاهات تفسير القرآن الكريم نشاط تربوي": "Distinguer les orientations du tafsīr — activité éducative",
  "فوائد ترجمة القرآن الكريم بمعنى تفسيره بلغات أخرى": "L'intérêt de la traduction-sens du Coran dans d'autres langues",
  "علوم القرآن مصادر ومراجع دروس السنة الثانية إعدادي عتيق": "Sources et références adoptées",
  "علوم القرآن الوحي تعريفه وأنواعه السنة أولى إعدادي عتيق": "La révélation (waḥy) : définition et espèces",
  "علوم القرآن أنشطة لاستثمار التعلمات ودعمها السنة أولى إعدادي عتيق": "Activités de valorisation et de consolidation des acquis",
  "علوم القرآن أنشطة لاستثمار التعلمات ودعمها السنة أولى إعدادي عتيق الدرس السابع": "Activités de valorisation et de consolidation des acquis (leçon 7)",
  "علوم القرآن جمع القرآن في عهد أبي بكر وعثمان رضي الله عنهما": "La collecte du Coran sous Abū Bakr et ʿUṯmān (qu'Allāh les agrée)",
  "علوم القرآن تراجم الأعلام لكتاب علوم القرآن للسنة الأولى إعدادي": "Notices biographiques des figures citées",
  "علوم القرأن مناهل العرفان في علوم القرآن لمحمد عبد العظيم الزرقاني للسنة الثالثة من التعليم الإعدادي العتيق": "Présentation du manuel",
  "النسخ تعريفه والفرق بينه وبين البداء والتخصيص 2": "L'abrogation (nasḫ) : définition et distinction d'avec le badāʾ et la restriction (2)",
  "من القراء السبعة للقرآن الكريم ابن عامر ابن كثير عاصم أبو عمرو": "Les sept lecteurs (1) : Ibn ʿĀmir, Ibn Kaṯīr, ʿĀṣim et Abū ʿAmr",
  "القراء السبعة للقرآن الكريم 2 حمزة نافع الكسائي": "Les sept lecteurs (2) : Ḥamza, Nāfiʿ et al-Kisāʾī",
  "خصائص قراءة الإمام نافع وأهمية اختيار المغاربة لهذه القراءة أنشطة لاستثمار التعلمات ودعمها": "Les caractéristiques de la lecture de l'imam Nāfiʿ et le choix marocain de cette lecture — activités",
  "ورشات حول قراءات القرآن الكريم وسير ومناقب القراء": "Ateliers sur les lectures coraniques et les vies des lecteurs",
  "تراجم الأعلام الواردة بمادة علوم القرآن للسنة الثالثة إعدادي عتيق": "Notices biographiques des figures citées",
  "المصادر والمراجع المعتمدة في مادة علوم القرآن السنة الثالثة إعدادي عتيق": "Sources et références adoptées",
  "المصادر والمراجع المعتمدة في": "Sources et références adoptées",

  /* ============ Fiqh — Risāla 1es ============ */
  "مقدمة الرسالة الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Introduction à la Risāla",
  "طهارة الخبث واللباس في الصلاة الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "La purification des souillures et le vêtement dans la prière",
  "الاستنجاء والاستجمار وسنن الوضوء الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "La propreté intime (istiñǧāʾ) et les pratiques recommandées du wuḍūʾ",
  "صفة الوضوء وكيفيته الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Le wuḍūʾ : sa description et sa manière",
  "صفة الوضوء ومستحباته الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Le wuḍūʾ : sa description et ses actes recommandés",
  "الغسل وأحكامه الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Le ġusl et ses règles",
  "أحكام التيمم والمسح على الخفين الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Le tayammum et l'essuyage sur les khuffs",
  "أوقات الصلوات الخمس وأسماؤها الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Les horaires des cinq prières et leurs noms",
  "أحكام الأذان والإقامة الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "L'appel à la prière (aḏān) et l'iqāma",
  "العمل في الصلوات الإحرام إلى قراءة الركعة الثانية الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Le déroulement de la prière : de l'ouverture (iḥrām) à la récitation de la 2ᵉ rakʿa",
  "العمل في الصلوات القراءة في الصلاة والذكر بعدها الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Le déroulement de la prière : la récitation et les évocations",
  "الإمامة وأحكامها الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "L'imamat de la prière et ses règles",
  "من أحكام اللباس والسهو في الصلاة الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Règles du vêtement et de l'oubli dans la prière",
  "من أحكام السهو وقضاء الفوائت الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "L'oubli (sahw) dans la prière et le rattrapage des manquées",
  "من أسباب الجمع ومسقطات القضاء الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Les motifs du regroupement des prières et les dispenses de rattrapage",
  "من أحكام صلاة المريض والمسافر الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "La prière du malade et du voyageur",
  "الرعاف وسجود التلاوة الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "L'épistaxis (ruʿāf) et la prosternation de récitation",
  "قصر الصلاة في السفر الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "L'abrègement de la prière en voyage",
  "صلاة الجمعة وصلاة الخوف الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "La prière du vendredi et la prière du danger",
  "صلاة العيدين الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Les prières des deux fêtes",
  "صلاة الخسوف والاستسقاء الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Les prières de l'éclipse et de la demande de pluie",
  "ما يفعل بالمحتضر والميت الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Les rites de l'agonisant et du défunt",
  "الصلاة على الجنازة الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "La prière funéraire",
  "الصيام وأحكامه الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Le jeûne et ses règles",
  "الصيام وأحكامه 2 الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "Le jeûne et ses règles (2)",
  "القيام والاعتكاف الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني": "La prière nocturne (qiyām) et la retraite (iʿtikāf)",

  /* ============ Fiqh — Akhḍarī 1ep ============ */
  "الطهارة وأحكامها الفقه من متن الأخضري بشرح الآبي الأزهري": "La purification (ṭahāra) et ses règles",
  "الوضوء وأحكامه تتمة الفقه من متن الأخضري للسنة الرابعة الابتدائي عتيق": "Le wuḍūʾ et ses règles — suite",
  "نواقض الوضوء درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Les annulateurs du wuḍūʾ",
  "موجبات الغسل وأحكامه درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Les causes du ġusl et ses règles",
  "موجبات الغسل وأحكامه تتمة درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Les causes du ġusl et ses règles — suite",
  "التيمم وأحكامه درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Le tayammum et ses règles",
  "نواقض التيمم وما يفعل به درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Les annulateurs du tayammum et son usage",
  "أحكام الحيض درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Les règles des menstrues (ḥayḍ)",
  "أحكام النفاس درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Les règles des lochies (nifās)",
  "قضاء الفوائت درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Le rattrapage des prières manquées",
  "أحكام سجود السهو درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "La prosternation de l'oubli (suǧūd al-sahw) : règles",
  "أحكام سجود السهو تتمة درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "La prosternation de l'oubli — suite",
  "ما لا سجود فيه درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Ce qui n'exige pas de prosternation [de récitation]",
  "ما لا يجوز فعله في الصلاة درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Ce qui est proscrit dans la prière",
  "مالا يجوز فعله في الصلاة تتمة درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Ce qui est proscrit dans la prière — suite",
  "ما يغتفر فعله في الصلاة درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Ce qui est toléré dans la prière",
  "سهو المأموم ودفع الأذى في الصلاة درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "L'oubli du fidèle dirigé (maʾmūm) et l'écartement de la gêne dans la prière",
  "أحكام المسبوق في الصلاة درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Le statut de celui qui rejoint la prière en cours (masbūq)",
  "استدراك الركن في الصلاة درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "La réparation d'un pilier délaissé dans la prière",
  "حكم السهو في صلاة القضاء والنافلة درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "L'oubli dans la prière de rattrapage et la surérogatoire",
  "متابعة المأموم للإمام في السهو درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Le fidèle dirigé derrière l'imam en cas d'oubli",
  "متابعة المأموم للإمام في السهو تتمة درس في الفقه من متن الأخضري بشرح الآبي الأزهري": "Le fidèle dirigé derrière l'imam en cas d'oubli — suite",

  /* ============ Fiqh — Mukhtaṣar Khalīl t1 ============ */
  "صور في البيع يعتريها المنع والجواز الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Cas de vente mêlant prohibition et permission",
  "الربا في الطعام الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "L'usure (ribā) dans les aliments",
  "البيوع الفاسدة الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Les ventes nulles (bayʿ fāsid)",
  "البيوع الفاسدة تتمة الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Les ventes nulles (bayʿ fāsid) — suite",
  "بيع المزابنة والكالىء وبيع العربان الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "La vente muzābana, la vente kalīʾ bi-kalīʾ et l'acompte (ʿurbūn)",
  "البويع المنهي عنها متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Les ventes proscrites",
  "آثار البيع الفاسد ومفوتاته الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Les effets de la vente nulle et ses empêchements",
  "بيوع الآجال شروطها وصورها وحكمها الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Les ventes à terme : conditions, figures et statut",
  "بيوع الآجال شروطها وصورها وحكمها تتمة الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Les ventes à terme : conditions, figures et statut — suite",
  "موانع الرد بالخيار الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Les obstacles à la rétrocession (radd) dans la vente à option (ḫiyār)",
  "التدليس في بيع الخيار الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "La dissimulation (tadlīs) dans la vente à option",
  "أحكام الغلة والضمان بعد رد المبيع الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Le produit (ġalla) et la responsabilité après rétrocession de la chose vendue",
  "اجتماع البيع والصرف متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "La réunion de la vente et de l'échange de monnaies (ṣarf)",
  "أثر العيب في الصرف متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "L'effet du vice dans l'échange de monnaies (ṣarf)",
  "أحكام المحلى والمبادلة والمراطلة متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي": "Les règles du muḥallā (différé monétaire), de la substitution et du report de dette (murāṭala)",

  /* ============ Fiqh — Mukhtaṣar Khalīl t2/t3 ============ */
  "كون المسلم فيه دينا في ذمة المسلم إليه ووجوده عند حلول أجله": "Le salam : dette à la charge du commanditaire et présence [de la chose] à l'échéance",
  "فهرس المصادر والمراجع الفقه من مختصر الشيح خليل بشرح الدردير وحاشية الدسوقي": "Index des sources et références",
  "ما يمنع منه المفلس وما لا يمنع منه الفقه من مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي للسنة الثالثة من التعليم الثانوي العتيق": "Ce qui est interdit au failli et ce qui lui demeure permis",
  "كفايات تدريس مادة الفقه بالسنة الثالثة من التعليم الثانوي العتيق": "Compétences visées par l'enseignement du fiqh",
  "كفايات تدريس مادة الفقه مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي السنة الثالثة من التعليم الثانوي العتيق": "Compétences visées par l'enseignement du fiqh (Mukhtaṣar de Khalīl)",
  "الفقه أحكام تصرفات السفيه البالغ وترتيب الأولياء": "Le fiqh : les actes du prodigue majeur (safīh) et l'ordre des tuteurs",
  "الفقه أحكام ضمان الغائب واختلاف الضامن والمضمون": "Le fiqh : la caution de l'absent et le différend entre garant et garanti",

  /* ============ Fiqh — Muršid Mayyāra 6ep ============ */
  "نصب الزكاة والواجب فيها زكاة الحبوب والثمار والنقود": "Les seuils d'imposition (niṣāb) de la zakāt : céréales, fruits et monnaies",
  "واجبات الحج الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة السادسة الابتدائي": "Les obligations du pèlerinage (wāǧibāt al-ḥaǧǧ)",
  "صفة العمل في الحج الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة السادسة الابتدائي": "Le déroulement des rites du pèlerinage",
  "صفة العمل في الطواف الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة السادسة الابتدائي": "Le déroulement de la circumambulation (ṭawāf)",
  "صفة السعي بين الصفا والمروة الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة السادسة الابتدائي العتيق": "Le déroulement du parcours (saʿy) entre Ṣafā et Marwa",
  "الخروج إلى منى والوقوف بعرفة الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة السادسة الابتدائي العتيق": "Le départ à Minā et la station à ʿArafa",
  "العمل في مزدلفة ومنى ويوم النحر الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة السادسة الابتدائي العتيق": "Les rites à Muzdalifa et Minā et au jour du sacrifice",
  "العمل في أيام التشريق الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة السادسة الابتدائي العتيق 2": "Les rites des jours de tašrīq (2)",
  "ممنوعات الإحرام الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة السادسة الابتدائي العتيق": "Les interdictions de l'iḥrām",
  "ممنوعات الإحرام تتمة الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة السادسة الابتدائي العتيق": "Les interdictions de l'iḥrām — suite",
  "أحكام العمرة وآداب الزيارة الشريفة الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة السادسة الابتدائي العتيق": "Les règles de la ʿumra et les bienséances de la visite [au Prophète ﷺ]",
  "مبادئ التصوف وهوادي التعرف التوبة والتقوى الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة السادسة الابتدائي العتيق": "Les principes du soufisme : le repentir (tawba) et la piété (taqwā)",
  "مبادئ التصوف وهوادي التعرف التوبة والتقوى تابع الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة": "Les principes du soufisme : le repentir et la piété — suite",
  "مبادئ التصوف وهوادي التعرف تابع التحلي بمقامات اليقين الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة للسنة": "Les principes du soufisme : l'ornement des stations de la certitude (yaqīn) — suite",

  /* ============ Ḥadīṯ — Muwaṭṭaʾ t1 ============ */
  "المتعة في الطلاق من كتاب الحديث من موطأ الإمام مالك بشرح الزرقاني 2": "La compensation de la répudiée (mutʿat al-ṭalāq)",
  "طلاق الحائض والعدة بالأقراء من موطأ الإمام مالك بشرح الزرقاني": "Le divorce prononcé durant les menstrues et la retraite comptée en cycles (qurūʾ)",
  "التفريق بين الزوجين للضرر و العيب من موطأ الإمام مالك بشرح الزرقاني": "La séparation des époux pour préjudice ou vice",

  /* ============ Manṭiq — Sullam t1 ============ */
  "المبادئ العشرة لعلم المنطق المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Les dix principes de la science de la logique",
  "مقدمة المؤلف المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Introduction de l'auteur",
  "أهمية علم المنطق المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "L'importance de la science de la logique",
  "التعريف بمتن السلم وقيمته العلمية المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Présentation du mathn al-Sullam et de sa valeur scientifique",
  "حكم الاشتغال بعلم المنطق المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Le statut de l'étude de la logique",
  "أنواع العلم الحادث المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Les espèces de la science occasionnée (ʿilm ḥādiṯ)",
  "أنواع العلم الحادث تتمة المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Les espèces de la science occasionnée — suite",
  "الدلالة اللفظية الوضعية المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "La signification lexicale posée (dalāla lafẓiyya waḍʿiyya)",
  "أنواع المعرف المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Les espèces du défini (maʿrifa)",
  "أنواع المعرف تتمة المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Les espèces du défini (maʿrifa) — suite",
  "شروط المعرف المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Les conditions du défini (maʿrifa)",
  "شروط المعرف تابع المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Les conditions du défini — suite",
  "شروط المعرف تتمة المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Les conditions du défini — suite",
  "أنشطة لاستثمار التعلمات ودعمها المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Activités de valorisation et de consolidation des acquis",
  "أنشطة لاستثمار التعلمات ودعمها المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني 19": "Activités de valorisation et de consolidation des acquis (19)",
  "أنشطة لاستثمار التعلمات ودعمها المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني 20": "Activités de valorisation et de consolidation des acquis (20)",
  "أنشطة تقويمية وتطبيقات داعمة المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Activités d'évaluation et applications de soutien",
  "تراجم الأعلام المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Notices biographiques des figures citées",
  "فهرس المصادر والمراجع المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني": "Index des sources et références",

  /* ============ Rasm 4ep ============ */
  "الغاية من نظم عمدة البيان في حكم المحذوف في القرآن والمنهج المتبع فيه": "La finalité du poème ʿUmdat al-Bayān sur l'élision coranique, et sa méthode",
  "بقية منهج ناظم عمدة البيان في حكم المحذوف في القرآن بالمنظومة وذكر اسمها": "La méthode du poète dans ʿUmdat al-Bayān — suite",
  "الرسم والضبط المصادر والمراجع المعتمدة في دروس مستوى الرابع ابتدائي عتيق": "Sources et références adoptées",

  /* ============ Divers pages-livres ============ */
  "التفسير من خلال التسهيل لعلوم التنزيل لابن جزي": "Présentation du manuel",
  "التوحيد من مقدمة رسالة ابن أبي زيد القيرواني بشرح كفاية الطالب الرباني لأبي الحسن للسنة الأولى الإعدادي العتيق": "Présentation du manuel",
  "كتاب التوحيد من منظومة المرشد المعين على الضروري من علوم الدين لعبد الواحد بن عاشر بشرح مختصر الدر الثمين لمحمد بن أحمد ميارة للسنة الثانية من التعليم الإعدادي العتيق": "Présentation du manuel",
  "التوقيت من منظومة المقنع بشرح المطلع على مسائل المقنع لمحمد بن سعيد المرغتي للسنة الأولى الثانوي العتيق": "Présentation du manuel",
  "التوقيت من منظومة المقنع بشرح المطلع على مسائل المقنع لمحمد بن سعيد المرغتي": "Présentation du manuel",

  /* ============ Tafsīr 1ep — paires de sourates ============ */
  "سورتا التكاثر والعصر التفسير من خلال تفسير الجلالين": "Sourates al-Takāṯur et al-ʿAṣr (Tafsīr al-Jalālayn)",
  "سورتا الفيل وقريش التفسير من خلال تفسير الجلالين": "Sourates al-Fīl et Qurayš (Tafsīr al-Jalālayn)",
  "سورتا الماعون والكوثر التفسير من خلال تفسير الجلالين": "Sourates al-Māʿūn et al-Kawṯar (Tafsīr al-Jalālayn)",
  "سور الكافرون والنصر والمسد التفسير من خلال تفسير الجلالين": "Sourates al-Kāfirūn, al-Naṣr et al-Masad (Tafsīr al-Jalālayn)",
  "سور الإخلاص والمعوذتين التفسير من خلال تفسير الجلالين": "Sourates al-Iḫlāṣ et les deux protectrices (muʿawwiḏāt) (Tafsīr al-Jalālayn)",
};

/* ————————————————— Application ————————————————— */
let changed = 0, kept = 0;
const files = readdirSync(BOOKS).filter((f) => f.endsWith(".json"));
const noMatch = new Set<string>();
for (const f of files) {
  const p = path.join(BOOKS, f);
  const b = JSON.parse(readFileSync(p, "utf8"));
  let dirty = false;
  const apply = (d: any) => {
    if (!d || !d.titleAr) return;
    const k = norm(d.titleAr);
    const v = D[k];
    if (v) {
      if (d.titleFr !== v) { d.titleFr = v; changed++; dirty = true; } else kept++;
    } else noMatch.add(k);
  };
  apply(b.intro);
  for (const l of b.lessons || []) apply(l);
  if (dirty) writeFileSync(p, JSON.stringify(b, null, 1) + "\n");
}
console.log(`Titres mis à jour : ${changed} | déjà corrects : ${kept} | sans entrée : ${noMatch.size}`);
