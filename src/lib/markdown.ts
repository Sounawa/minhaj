/**
 * Lightweight, dependency-free markdown renderer for chat messages.
 * Escapes HTML first, then applies a safe subset of markdown transforms.
 */

function escapeHtml(str: string): string {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function inline(md: string): string {
  let s = md;
  // inline code
  s = s.replace(/`([^`\n]+)`/g, (_m, code) => `<code>${code}</code>`);
  // bold + italic
  s = s.replace(/\*\*\*([^*]+)\*\*\*/g, "<strong><em>$1</em></strong>");
  s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  s = s.replace(/(^|\W)\*([^*\n]+)\*(?=\W|$)/g, "$1<em>$2</em>");
  // links [text](url)
  s = s.replace(
    /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
    '<a href="$2" target="_blank" rel="noopener noreferrer" class="text-primary underline underline-offset-2">$1</a>'
  );
  return s;
}

export function renderMarkdown(markdown: string): string {
  const escaped = escapeHtml(markdown);
  const lines = escaped.split("\n");
  const out: string[] = [];

  let inCode = false;
  let codeLang = "";
  let codeBuf: string[] = [];
  let listType: "ul" | "ol" | null = null;
  let paragraphBuf: string[] = [];

  const flushParagraph = () => {
    if (paragraphBuf.length) {
      out.push(`<p>${inline(paragraphBuf.join(" "))}</p>`);
      paragraphBuf = [];
    }
  };
  const closeList = () => {
    if (listType) {
      out.push(`</${listType}>`);
      listType = null;
    }
  };

  for (const raw of lines) {
    const line = raw.replace(/\s+$/, "");

    // Fenced code blocks
    const fence = line.match(/^```(\w*)/);
    if (fence) {
      if (!inCode) {
        flushParagraph();
        closeList();
        inCode = true;
        codeLang = fence[1] || "text";
        codeBuf = [];
      } else {
        out.push(
          `<pre data-lang="${codeLang}"><code>${codeBuf.join("\n")}</code></pre>`
        );
        inCode = false;
        codeLang = "";
        codeBuf = [];
      }
      continue;
    }
    if (inCode) {
      codeBuf.push(line);
      continue;
    }

    // Blank line
    if (!line.trim()) {
      flushParagraph();
      closeList();
      continue;
    }

    // Headings
    const heading = line.match(/^(#{1,4})\s+(.*)$/);
    if (heading) {
      flushParagraph();
      closeList();
      const level = Math.min(4, heading[1].length + 1); // h2..h5 inside message
      out.push(`<h${level}>${inline(heading[2])}</h${level}>`);
      continue;
    }

    // Unordered list
    const ul = line.match(/^\s*[-*•]\s+(.*)$/);
    if (ul) {
      flushParagraph();
      if (listType !== "ul") {
        closeList();
        out.push("<ul>");
        listType = "ul";
      }
      out.push(`<li>${inline(ul[1])}</li>`);
      continue;
    }

    // Ordered list
    const ol = line.match(/^\s*\d+[.)]\s+(.*)$/);
    if (ol) {
      flushParagraph();
      if (listType !== "ol") {
        closeList();
        out.push("<ol>");
        listType = "ol";
      }
      out.push(`<li>${inline(ol[1])}</li>`);
      continue;
    }

    // Blockquote
    const quote = line.match(/^>\s?(.*)$/);
    if (quote) {
      flushParagraph();
      closeList();
      out.push(
        `<blockquote style="border-left:3px solid var(--border);padding-left:0.75rem;margin:0.4rem 0;color:var(--muted-foreground)">${inline(quote[1])}</blockquote>`
      );
      continue;
    }

    // Horizontal rule
    if (/^\s*([-*_])\s*\1\s*\1[\s\S]*$/.test(line) && line.replace(/[\s\-*_]/g, "") === "") {
      flushParagraph();
      closeList();
      out.push('<hr style="border:none;border-top:1px solid var(--border);margin:0.6rem 0" />');
      continue;
    }

    // Regular paragraph line
    closeList();
    paragraphBuf.push(line);
  }

  if (inCode && codeBuf.length) {
    out.push(`<pre data-lang="${codeLang}"><code>${codeBuf.join("\n")}</code></pre>`);
  }
  flushParagraph();
  closeList();

  return out.join("\n");
}
