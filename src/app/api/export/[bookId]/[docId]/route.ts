import { NextResponse } from "next/server";
import { getDoc } from "@/lib/minhaj";

export const dynamic = "force-dynamic";

/* ————————————————————————————————————————————————————————————————
 * Export d'une leçon : HTML autonome (impression/PDF) ou EPUB 3.
 *  GET /api/export/{bookId}/{docId}?format=html|epub
 * ———————————————————————————————————————————————————————————————— */

function xmlEscape(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

/** Entités HTML nommées non définies en XML strict (EPUB/XHTML) → numériques.
 *  Les 5 entités XML prédéfinies (&amp; &lt; &gt; &quot; &apos;) passent telles quelles. */
const NAMED_ENTITIES: Record<string, string> = {
  nbsp: "\u00a0", iexcl: "\u00a1", cent: "\u00a2", pound: "\u00a3", curren: "\u00a4", yen: "\u00a5",
  brvbar: "\u00a6", sect: "\u00a7", uml: "\u00a8", copy: "\u00a9", ordf: "\u00aa", laquo: "\u00ab",
  not: "\u00ac", shy: "\u00ad", reg: "\u00ae", macr: "\u00af", deg: "\u00b0", plusmn: "\u00b1",
  sup2: "\u00b2", sup3: "\u00b3", acute: "\u00b4", micro: "\u00b5", para: "\u00b6", middot: "\u00b7",
  cedil: "\u00b8", sup1: "\u00b9", ordm: "\u00ba", raquo: "\u00bb", frac14: "\u00bc", frac12: "\u00bd",
  frac34: "\u00be", iquest: "\u00bf", Agrave: "\u00c0", Aacute: "\u00c1", Acirc: "\u00c2", Atilde: "\u00c3",
  Auml: "\u00c4", Aring: "\u00c5", AElig: "\u00c6", Ccedil: "\u00c7", Egrave: "\u00c8", Eacute: "\u00c9",
  Ecirc: "\u00ca", Euml: "\u00cb", Igrave: "\u00cc", Iacute: "\u00cd", Icirc: "\u00ce", Iuml: "\u00cf",
  ETH: "\u00d0", Ntilde: "\u00d1", Ograve: "\u00d2", Oacute: "\u00d3", Ocirc: "\u00d4", Otilde: "\u00d5",
  Ouml: "\u00d6", times: "\u00d7", Oslash: "\u00d8", Ugrave: "\u00d9", Uacute: "\u00da", Ucirc: "\u00db",
  Uuml: "\u00dc", Yacute: "\u00dd", THORN: "\u00de", szlig: "\u00df", agrave: "\u00e0", aacute: "\u00e1",
  acirc: "\u00e2", atilde: "\u00e3", auml: "\u00e4", aring: "\u00e5", aelig: "\u00e6", ccedil: "\u00e7",
  egrave: "\u00e8", eacute: "\u00e9", ecirc: "\u00ea", euml: "\u00eb", igrave: "\u00ec", iacute: "\u00ed",
  icirc: "\u00ee", iuml: "\u00ef", eth: "\u00f0", ntilde: "\u00f1", ograve: "\u00f2", oacute: "\u00f3",
  ocirc: "\u00f4", otilde: "\u00f5", ouml: "\u00f6", divide: "\u00f7", oslash: "\u00f8", ugrave: "\u00f9",
  uacute: "\u00fa", ucirc: "\u00fb", uuml: "\u00fc", yacute: "\u00fd", thorn: "\u00fe", yuml: "\u00ff",
  OElig: "\u0152", oelig: "\u0153", Scaron: "\u0160", scaron: "\u0161", Yuml: "\u0178", fnof: "\u0192",
  circ: "\u02c6", tilde: "\u02dc", ensp: "\u2002", emsp: "\u2003", thinsp: "\u2009", ndash: "\u2013",
  mdash: "\u2014", lsquo: "\u2018", rsquo: "\u2019", sbquo: "\u201a", ldquo: "\u201c", rdquo: "\u201d",
  bdquo: "\u201e", dagger: "\u2020", Dagger: "\u2021", bull: "\u2022", hellip: "\u2026", permil: "\u2030",
  prime: "\u2032", Prime: "\u2033", lsaquo: "\u2039", rsaquo: "\u203a", oline: "\u203e", frasl: "\u2044",
  euro: "\u20ac", trade: "\u2122", larr: "\u2190", uarr: "\u2191", rarr: "\u2192", darr: "\u2193",
  harr: "\u2194", minus: "\u2212", infin: "\u221e", ne: "\u2260", le: "\u2264", ge: "\u2265",
};

function xhtmlSanitize(html: string): string {
  return html.replace(/&([a-zA-Z][a-zA-Z0-9]*);/g, (whole, name: string) =>
    NAMED_ENTITIES[name] !== undefined ? NAMED_ENTITIES[name] : whole,
  );
}

/* ————————————————— HTML → XHTML bien formé (EPUB) —————————————————
 * Le HTML du corpus (scrapé) contient des balises non appariées — p.ex.
 * des `</div>` finaux orphelins — que le navigateur tolère mais que le
 * parseur XML strict de l'EPUB refuse. Cette passe :
 *   1. autofemme les éléments vides (`<br>` → `<br/>`) ;
 *   2. supprime les balises fermantes sans ouvrante correspondante ;
 *   3. referme à la fin les balises encore ouvertes. */
const VOID_TAGS = new Set([
  "br", "hr", "img", "input", "meta", "link", "area", "base", "col",
  "embed", "source", "track", "wbr",
]);

function xhtmlBalance(html: string): string {
  // 1. éléments vides → forme autoscellée
  const selfClosed = html.replace(
    /<(br|hr|img|input|meta|link|area|base|col|embed|source|track|wbr)\b([^>]*?)(\/?)>/gi,
    (_m, tag: string, attrs: string, slash: string) =>
      `<${tag}${attrs.replace(/\s+$/, "")}${slash ? "" : "/"}>`,
  );
  // 2/3. appariement
  const stack: string[] = [];
  let out = "";
  const re = /<(\/)?([a-zA-Z][a-zA-Z0-9]*)((?:"[^"]*"|'[^']*'|[^>"'])*)(\/?)>/g;
  let last = 0;
  let m: RegExpExecArray | null;
  while ((m = re.exec(selfClosed))) {
    out += selfClosed.slice(last, m.index);
    last = re.lastIndex;
    const [, closing, rawName, attrs, selfClose] = m;
    const name = rawName.toLowerCase();
    if (VOID_TAGS.has(name) || selfClose) {
      // NB : le groupe « attrs » englobe le « / » éventuel — le retirer avant
      // d'autosceller, sans quoi on produirait `<br//>`.
      out += `<${rawName}${attrs.replace(/\/+$/, "")}/>`;
      continue;
    }
    if (closing) {
      const i = stack.lastIndexOf(name);
      if (i === -1) continue; // fermante orpheline → supprimée
      for (let k = stack.length - 1; k > i; k--) {
        out += `</${stack[k]}>`; // enfants laissés ouverts → refermés
      }
      out += `</${name}>`;
      stack.length = i;
    } else {
      stack.push(name);
      out += `<${rawName}${attrs}>`;
    }
  }
  out += selfClosed.slice(last);
  for (let k = stack.length - 1; k >= 0; k--) out += `</${stack[k]}>`;
  return out;
}

const SHARED_CSS = `
:root { --ink:#1c1917; --amber:#b45309; --line:#e7e5e4; --muted:#78716c; }
* { box-sizing: border-box; }
body { margin:0; padding:2.2rem 1.4rem; color:var(--ink);
  font-family:"Lora",Georgia,"Times New Roman",serif; line-height:1.75; }
h1 { font-size:1.55rem; line-height:1.3; margin:0 0 .3rem; }
h2 { font-size:1.2rem; margin:1.6rem 0 .5rem; border-bottom:2px solid var(--line); padding-bottom:.25rem; }
h3 { font-size:1.05rem; margin:1.2rem 0 .4rem; }
p { margin:.65rem 0; }
ul,ol { margin:.6rem 0; padding-inline-start:1.5rem; }
li { margin:.3rem 0; }
.meta { color:var(--muted); font-size:.85rem; margin-bottom:1.6rem; }
.meta .sep { margin:0 .45rem; }
.ornament { display:flex; align-items:center; gap:.6rem; margin:.9rem 0; }
.ornament::before,.ornament::after { content:""; flex:1; height:1px; background:var(--line); }
.ornament svg { width:14px; height:14px; fill:var(--amber); }
.ar-title { direction:rtl; text-align:right; font-size:1.25rem; color:var(--amber); margin:.2rem 0 0; }
section.pane { margin:1.8rem 0; }
.pane-label { font-size:.72rem; letter-spacing:.18em; text-transform:uppercase;
  color:var(--amber); font-weight:700; margin-bottom:.4rem; }
.pane-ar .lesson-content { direction:rtl; text-align:right;
  font-size:1.12rem; line-height:2.15; }
footer { margin-top:2.6rem; padding-top:.8rem; border-top:1px solid var(--line);
  color:var(--muted); font-size:.75rem; text-align:center; }
@media print {
  body { padding:0; }
  section.pane { break-inside:auto; }
  h1,h2,h3 { break-after:avoid; }
}
`;

const STAR_SVG = `<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4z"/></svg>`;

interface DocLike {
  bookId: string;
  bookTitleFr: string;
  titleFr?: string | null;
  titleAr: string;
  html?: string | null;
  htmlFr?: string | null;
  isIntro?: boolean;
  savant?: boolean;
  pdfOnly?: boolean;
  level?: { shortFr?: string } | null;
  subject?: { titleFr?: string } | null;
  index?: number;
  count?: number;
}

function docLabel(doc: DocLike): string {
  return doc.isIntro ? "Introduction" : `Leçon ${(doc.index ?? 0) + 1} / ${doc.count ?? "?"}`;
}

/** Fichier HTML autonome, prêt pour l'impression / « Enregistrer en PDF ». */
function buildStandaloneHtml(doc: DocLike): string {
  const meta = [
    docLabel(doc),
    doc.level?.shortFr,
    doc.subject?.titleFr,
    doc.savant ? "traduction savante" : null,
  ]
    .filter(Boolean)
    .map((s) => xmlEscape(String(s)))
    .join('<span class="sep">·</span>');
  const frPane = doc.htmlFr
    ? `<section class="pane pane-fr"><p class="pane-label">Français — traduction${doc.savant ? " savante" : ""}</p><div class="lesson-content">${doc.htmlFr}</div></section>`
    : "";
  const arPane = doc.html
    ? `<section class="pane pane-ar"><p class="pane-label">العربية — النص الأصلي</p><div class="lesson-content" lang="ar" dir="rtl">${doc.html}</div></section>`
    : "";
  return `<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${xmlEscape(doc.titleFr || doc.titleAr)} — Minhāj</title>
<style>${SHARED_CSS}</style>
</head>
<body>
<header>
<h1>${xmlEscape(doc.titleFr || doc.titleAr)}</h1>
<div class="ornament">${STAR_SVG}</div>
<p class="ar-title" lang="ar" dir="rtl">${xmlEscape(doc.titleAr)}</p>
<p class="meta">${meta}<span class="sep">·</span>${xmlEscape(doc.bookTitleFr)}</p>
</header>
${frPane}
${arPane}
<footer>Minhāj — Taʿlīm ʿatīq · programme officiel du ministère des Habous et des Affaires islamiques (Royaume du Maroc)</footer>
</body>
</html>`;
}

/* ——————————————————————— ZIP minimal (entrées stockées, CRC32) ——————————————————————— */

const CRC_TABLE = (() => {
  const t = new Uint32Array(256);
  for (let i = 0; i < 256; i++) {
    let c = i;
    for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    t[i] = c >>> 0;
  }
  return t;
})();

function crc32(data: Uint8Array): number {
  let c = 0xffffffff;
  for (let i = 0; i < data.length; i++) c = CRC_TABLE[(c ^ data[i]) & 0xff] ^ (c >>> 8);
  return (c ^ 0xffffffff) >>> 0;
}

const enc = new TextEncoder();

function zipStore(entries: { name: string; data: Uint8Array }[]): Uint8Array {
  const localChunks: Uint8Array[] = [];
  const centralChunks: Uint8Array[] = [];
  let offset = 0;
  for (const e of entries) {
    const name = enc.encode(e.name);
    const crc = crc32(e.data);
    const lh = new Uint8Array(30 + name.length);
    const dv = new DataView(lh.buffer);
    dv.setUint32(0, 0x04034b50, true); // signature « fichier local »
    dv.setUint16(4, 20, true); // version minimale
    dv.setUint16(6, 0x0800, true); // drapeaux : noms UTF-8
    dv.setUint16(8, 0, true); // méthode : stockée (sans compression)
    dv.setUint16(10, 0, true); // heure
    dv.setUint16(12, 0x21, true); // date (1980-01-01, valeur valide minimale)
    dv.setUint32(14, crc, true);
    dv.setUint32(18, e.data.length, true);
    dv.setUint32(22, e.data.length, true);
    dv.setUint16(26, name.length, true);
    dv.setUint16(28, 0, true); // extra
    lh.set(name, 30);
    localChunks.push(lh, e.data);
    const cd = new Uint8Array(46 + name.length);
    const cdv = new DataView(cd.buffer);
    cdv.setUint32(0, 0x02014b50, true);
    cdv.setUint16(4, 20, true);
    cdv.setUint16(6, 20, true);
    cdv.setUint16(8, 0x0800, true);
    cdv.setUint16(10, 0, true); // méthode
    cdv.setUint16(12, 0, true); // heure
    cdv.setUint16(14, 0x21, true); // date
    cdv.setUint32(16, crc, true);
    cdv.setUint32(20, e.data.length, true);
    cdv.setUint32(24, e.data.length, true);
    cdv.setUint16(28, name.length, true);
    // 30..42 : extra, commentaire, disques, attributs — zéro (déjà à 0)
    cdv.setUint32(42, offset, true); // offset de l'en-tête local
    cd.set(name, 46);
    centralChunks.push(cd);
    offset += lh.length + e.data.length;
  }
  let cdSize = 0;
  for (const c of centralChunks) cdSize += c.length;
  const eocd = new Uint8Array(22);
  const ev = new DataView(eocd.buffer);
  ev.setUint32(0, 0x06054b50, true);
  ev.setUint16(8, entries.length, true);
  ev.setUint16(10, entries.length, true);
  ev.setUint32(12, cdSize, true);
  ev.setUint32(16, offset, true);
  const total = offset + cdSize + 22;
  const out = new Uint8Array(total);
  let p = 0;
  for (const c of localChunks) {
    out.set(c, p);
    p += c.length;
  }
  for (const c of centralChunks) {
    out.set(c, p);
    p += c.length;
  }
  out.set(eocd, p);
  return out;
}

/** EPUB 3 minimal (OCF 3.0) — entrées stockées ; mimetype en tête, sans extra. */
function buildEpub(doc: DocLike): Uint8Array {
  const id = `minhaj-${doc.bookId}-${doc.isIntro ? "intro" : (doc.index ?? 0) + 1}`;
  const title = `${doc.titleFr || doc.titleAr} — ${doc.bookTitleFr}`;
  const lang = doc.htmlFr ? "fr" : "ar";

  const navXhtml = `<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="${lang}">
<head><meta charset="utf-8"/><title>${xmlEscape(title)}</title></head>
<body>
<nav epub:type="toc" id="toc"><h1>Sommaire</h1>
<ol><li><a href="lesson.xhtml">${xmlEscape(title)}</a></li></ol>
</nav>
<nav epub:type="landmarks" hidden=""><ol>
<li><a epub:type="bodymatter" href="lesson.xhtml">Contenu</a></li>
</ol></nav>
</body>
</html>`;

  const contentOpf = `<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid" xml:lang="${lang}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">urn:uuid:${id}</dc:identifier>
<dc:title>${xmlEscape(title)}</dc:title>
<dc:language>${lang}</dc:language>
<dc:creator>Ministère des Habous et des Affaires islamiques (Royaume du Maroc)</dc:creator>
<dc:publisher>Minhāj — Taʿlīm ʿatīq</dc:publisher>
<meta property="dcterms:modified">2024-01-01T00:00:00Z</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="css" href="style.css" media-type="text/css"/>
<item id="lesson" href="lesson.xhtml" media-type="application/xhtml+xml"/>
</manifest>
<spine><itemref idref="lesson"/></spine>
</package>`;

  const meta = [docLabel(doc), doc.level?.shortFr, doc.subject?.titleFr]
    .filter(Boolean)
    .map((s) => xmlEscape(String(s)))
    .join(" · ");
  const frPane = doc.htmlFr
    ? `<section class="pane pane-fr" epub:type="chapter"><p class="pane-label">Français — traduction${doc.savant ? " savante" : ""}</p>
<div class="lesson-content">${xhtmlBalance(xhtmlSanitize(doc.htmlFr))}</div></section>`
    : "";
  const arPane = doc.html
    ? `<section class="pane pane-ar"><p class="pane-label">العربية — النص الأصلي</p>
<div class="lesson-content" lang="ar" dir="rtl">${xhtmlBalance(xhtmlSanitize(doc.html))}</div></section>`
    : "";
  const lessonXhtml = `<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="${lang}">
<head><meta charset="utf-8"/><title>${xmlEscape(title)}</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
<header>
<h1>${xmlEscape(doc.titleFr || doc.titleAr)}</h1>
<div class="ornament">${STAR_SVG}</div>
<p class="ar-title" lang="ar" dir="rtl">${xmlEscape(doc.titleAr)}</p>
<p class="meta">${meta} · ${xmlEscape(doc.bookTitleFr)}</p>
</header>
${frPane}
${arPane}
<footer>Minhāj — Taʿlīm ʿatīq · programme officiel des Habous (Royaume du Maroc)</footer>
</body>
</html>`;

  return zipStore([
    { name: "mimetype", data: enc.encode("application/epub+zip") },
    {
      name: "META-INF/container.xml",
      data: enc.encode(`<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>`),
    },
    { name: "OEBPS/content.opf", data: enc.encode(contentOpf) },
    { name: "OEBPS/nav.xhtml", data: enc.encode(navXhtml) },
    { name: "OEBPS/style.css", data: enc.encode(SHARED_CSS) },
    { name: "OEBPS/lesson.xhtml", data: enc.encode(lessonXhtml) },
  ]);
}

function asciiName(doc: DocLike): string {
  const base = (doc.titleFr || doc.titleAr || "lecon")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/['’]/g, "")
    .replace(/[^A-Za-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .toLowerCase()
    .slice(0, 64);
  return base || "lecon";
}

export async function GET(
  req: Request,
  { params }: { params: Promise<{ bookId: string; docId: string }> },
) {
  const { bookId, docId } = await params;
  const format = new URL(req.url).searchParams.get("format") ?? "html";
  try {
    const doc = (await getDoc(bookId, docId)) as DocLike | null;
    if (!doc) {
      return NextResponse.json(
        { error: "not_found", message: `Document ${docId} introuvable dans le manuel ${bookId}.` },
        { status: 404 },
      );
    }
    if (doc.pdfOnly || (!doc.html && !doc.htmlFr)) {
      return NextResponse.json(
        { error: "no_content", message: "Ce document est publié au format PDF officiel uniquement." },
        { status: 415 },
      );
    }
    if (format === "epub") {
      const epub = buildEpub(doc);
      return new NextResponse(epub as unknown as BodyInit, {
        headers: {
          "Content-Type": "application/epub+zip",
          "Content-Disposition": `attachment; filename="minhaj-${asciiName(doc)}.epub"`,
          "Cache-Control": "no-store",
        },
      });
    }
    const html = buildStandaloneHtml(doc);
    return new NextResponse(html, {
      headers: {
        "Content-Type": "text/html; charset=utf-8",
        "Content-Disposition": `inline; filename="minhaj-${asciiName(doc)}.html"`,
        "Cache-Control": "no-store",
      },
    });
  } catch (e) {
    return NextResponse.json(
      { error: "export_failed", message: e instanceof Error ? e.message : String(e) },
      { status: 503 },
    );
  }
}
