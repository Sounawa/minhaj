import { NextResponse } from "next/server";
import { spawn } from "node:child_process";
import { readFile } from "node:fs/promises";
import path from "node:path";

export const dynamic = "force-dynamic";
export const maxDuration = 300;

type OcrCache = {
  docId: string;
  bookId: string;
  pages: number;
  ocrAt: string;
  pdfUrl?: string;
  html: string;
};

const HOME = "/home/z/my-project";
const ID_RE = /^[a-z0-9][a-z0-9_-]{0,80}$/i;

async function readCache(bookId: string, docId: string): Promise<OcrCache | null> {
  try {
    const raw = await readFile(path.join(HOME, "content/ocr-cache", `${docId}.json`), "utf-8");
    const data = JSON.parse(raw) as OcrCache;
    if (data && data.html && data.bookId === bookId && data.pages > 0) return data;
  } catch {
    /* pas de cache (ou illisible) */
  }
  return null;
}

/** GET : sonde le cache OCR (pas de calcul). */
export async function GET(
  _req: Request,
  { params }: { params: Promise<{ bookId: string; docId: string }> }
) {
  const { bookId, docId } = await params;
  if (!ID_RE.test(bookId) || !ID_RE.test(docId)) {
    return NextResponse.json({ error: "bad_request" }, { status: 400 });
  }
  const cached = await readCache(bookId, docId);
  return NextResponse.json(
    { cached: Boolean(cached), pages: cached?.pages ?? 0, html: cached?.html ?? null },
    { headers: { "Cache-Control": "no-store" } }
  );
}

/** POST : lance l'OCR à la demande (python3 ocr-one.py) et retourne le HTML. */
export async function POST(
  _req: Request,
  { params }: { params: Promise<{ bookId: string; docId: string }> }
) {
  const { bookId, docId } = await params;
  if (!ID_RE.test(bookId) || !ID_RE.test(docId)) {
    return NextResponse.json({ error: "bad_request" }, { status: 400 });
  }
  const pre = await readCache(bookId, docId);
  if (pre) {
    return NextResponse.json({ cached: true, pages: pre.pages, html: pre.html });
  }
  const result = await new Promise<{ code: number; stdout: string; stderr: string }>((resolve) => {
    const child = spawn(
      "python3",
      [path.join(HOME, "scripts-translate/ocr-one.py"), bookId, docId],
      { cwd: HOME, env: { ...process.env, PYTHONIOENCODING: "utf-8" } }
    );
    let stdout = "";
    let stderr = "";
    child.stdout.on("data", (d: Buffer) => (stdout += d.toString("utf-8")));
    child.stderr.on("data", (d: Buffer) => (stderr += d.toString("utf-8")));
    child.on("error", (err) => resolve({ code: -1, stdout, stderr: String(err) }));
    child.on("close", (code) => resolve({ code: code ?? -1, stdout, stderr }));
  });
  if (result.code !== 0) {
    return NextResponse.json(
      { error: "ocr_failed", message: result.stderr.slice(0, 500) || `code ${result.code}` },
      { status: 502 }
    );
  }
  try {
    const parsed = JSON.parse(result.stdout.trim().split("\n")[0] ?? result.stdout) as {
      ok: boolean;
      cached?: boolean;
      pages?: number;
      htmlPath?: string;
      error?: string;
    };
    if (!parsed.ok) {
      return NextResponse.json({ error: "ocr_failed", message: parsed.error }, { status: 422 });
    }
    const raw = await readFile(parsed.htmlPath as string, "utf-8");
    const data = JSON.parse(raw) as OcrCache;
    return NextResponse.json({ cached: false, pages: data.pages, html: data.html });
  } catch {
    return NextResponse.json({ error: "ocr_parse", message: result.stdout.slice(0, 300) }, { status: 500 });
  }
}
