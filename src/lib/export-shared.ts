/* ————————————————————————————————————————————————————————————————
 * Socle partagé des exports Minhāj (leçon seule ET livre entier) :
 * sanitisation XHTML, ZIP minimal (CRC32), CSS commune, gabarits.
 * ———————————————————————————————————————————————————————————————— */

export function xmlEscape(s: string): string {
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

export function xhtmlSanitize(html: string): string {
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

export function xhtmlBalance(html: string): string {
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

export const SHARED_CSS = `
:root { --ink:#1c1917; --amber:#b45309; --amber-deep:#92400e; --line:#e7e5e4; --muted:#78716c; }
html { scroll-behavior:smooth; }
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
/* Lettrine — tradition typographique du livre savant (miroir du lecteur en ligne) */
.pane-fr .lesson-content > p:first-of-type::first-letter {
  font-weight:700; font-size:3em; line-height:.82; float:left;
  padding:.06em .12em 0 0; color:var(--amber-deep);
}
/* Citation coranique intégrale (marquage côté serveur) : panneau ambre discret */
.lesson-content p.quran-quote {
  margin-block:1.25em; padding:.85em 1.1em .85em 1.25em;
  border-inline-start:2.5px solid color-mix(in oklab, var(--amber) 55%, transparent);
  border-start-end-radius:12px; border-end-end-radius:12px;
  background:linear-gradient(to right,
    color-mix(in oklab, var(--amber) 8%, transparent),
    color-mix(in oklab, var(--amber) 2.5%, transparent) 62%, transparent);
  hyphens:none;
}
.pane-ar .lesson-content p.quran-quote {
  padding:.85em 1.25em .85em 1.1em;
  border-inline-start:none;
  border-inline-end:2.5px solid color-mix(in oklab, var(--amber) 55%, transparent);
  border-start-end-radius:2px; border-end-end-radius:2px;
  border-start-start-radius:12px; border-end-start-radius:12px;
  background:linear-gradient(to left,
    color-mix(in oklab, var(--amber) 8%, transparent),
    color-mix(in oklab, var(--amber) 2.5%, transparent) 62%, transparent);
}
@media print {
  body { padding:0; }
  section.pane { break-inside:auto; }
  h1,h2,h3 { break-after:avoid; }
  .pane-fr .lesson-content > p:first-of-type::first-letter {
    font-size:2.6em; color:#1c1917; float:none; padding:0; font-weight:inherit;
  }
  .lesson-content p.quran-quote {
    background:none; border-inline-start:2px solid #b8b8b8; padding-inline-start:.8em;
  }
}
`;

export const BOOK_CSS = `
.toc { border:1px solid var(--line); border-radius:10px; padding:1rem 1.4rem; margin:1.6rem 0 2.2rem;
  background:linear-gradient(to bottom, rgba(180,83,9,.035), transparent 5rem); }
.toc h2 { border:none; margin:.2rem 0 .6rem; padding:0; }
.toc ol { margin:0; padding-inline-start:1.6rem; }
.toc li { margin:.28rem 0; }
.toc a { color:var(--ink); text-decoration:none;
  border-bottom:1px dotted transparent; transition:border-color .15s; }
.toc a:hover { color:var(--amber); border-bottom-color:var(--amber); }
.toc .toc-pdf { color:var(--muted); font-size:.72em; letter-spacing:.08em;
  border:1px solid var(--line); border-radius:4px; padding:0 .3em; margin-inline-start:.4em; }
.doc { padding-top:.4rem; }
.doc + .doc { border-top:1px solid var(--line); margin-top:2.6rem; padding-top:1.6rem; }
.doc-header h2 { border-bottom:none; margin-bottom:.2rem; }
.back-toc { display:inline-block; font-size:.75rem; color:var(--muted);
  text-decoration:none; margin-bottom:.35rem; }
.back-toc::before { content:"↩ "; color:var(--amber); }
.back-toc:hover { color:var(--amber); }
.pdf-note { border:1px dashed var(--line); border-radius:8px; padding:.8rem 1rem;
  color:var(--muted); font-size:.9rem; }
@media print {
  .doc { break-before:page; }
  .doc:first-of-type { break-before:auto; }
  .doc + .doc { margin-top:0; border-top:none; }
  .back-toc { display:none; }
  .toc { background:none; }
  .toc ol { columns:2; column-gap:2.5rem; }
}
`;

export const STAR_SVG = `<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4z"/></svg>`;

/* ——————————— Marquage serveur des citations coraniques (export) ———————————
 * Miroir conservateur de la détection client du lecteur : les exports étant
 * des documents statiques, le marquage est fait par regex au moment de la
 * construction. Seuls les <p> dont le début/la fin correspondent strictement
 * aux conventions du corpus savant sont marqués (aucun faux positif toléré).
 *  - FR : ouvre sur « , longueur > 120, clôturé par (Sūra, n-n) ;
 *  - AR : contient les parenthèses ornementales ﴾ ﴿ (sans balise imbriquée)
 *        ou clôturé par [الشورى: 18] (nom : chiffres, sans volume/page). */
export function markQuranQuotes(html: string, pane: "fr" | "ar"): string {
  if (pane === "fr") {
    const FR = /<p>(\s*«[\s\S]{120,}?\([^()]{2,40},\s*[\d\s\u2013-]+\)\s*[»"]?\s*)<\/p>/g;
    return html.replace(FR, '<p class="quran-quote">$1</p>');
  }
  // AR : ﴾…﴿ (paragraphe sans balise imbriquée) ou référence [الشورى: 18] finale
  const AR_ORNATE = /<p>((?:(?!<)[\s\S])*[\u{FD3E}\u{FD3F}](?:(?!<)[\s\S])*)<\/p>/gu;
  let out = html.replace(AR_ORNATE, '<p class="quran-quote quran-quote-ar">$1</p>');
  const AR_REF = /<p>([\s\S]{120,}?\[\s*[\u0600-\u06FF][\u0600-\u06FF\s]{0,25}:\s*[\d\u0660-\u0669][\d\u0660-\u0669\s\u2013-]*\]\s*)<\/p>/g;
  out = out.replace(AR_REF, '<p class="quran-quote quran-quote-ar">$1</p>');
  return out;
}

export interface DocLike {
  bookId: string;
  bookTitleFr: string;
  bookTitleAr?: string;
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

export function docLabel(doc: DocLike): string {
  return doc.isIntro ? "Introduction" : `Leçon ${(doc.index ?? 0) + 1} / ${doc.count ?? "?"}`;
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

export function zipStore(entries: { name: string; data: Uint8Array }[]): Uint8Array {
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

export const encUtf8 = enc;

export function asciiSlug(s: string, fallback = "minhaj"): string {
  const base = (s || fallback)
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/['’]/g, "")
    .replace(/[^A-Za-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .toLowerCase()
    .slice(0, 64);
  return base || fallback;
}
