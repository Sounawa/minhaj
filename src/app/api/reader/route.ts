import { NextRequest, NextResponse } from "next/server";
import ZAI from "z-ai-web-dev-sdk";

export const runtime = "nodejs";
export const maxDuration = 120;

export async function POST(req: NextRequest) {
  try {
    const { url } = (await req.json()) as { url?: string };

    if (!url?.trim()) {
      return NextResponse.json({ error: "URL is required" }, { status: 400 });
    }

    let target = url.trim();
    if (!/^https?:\/\//i.test(target)) {
      target = `https://${target}`;
    }

    try {
      new URL(target);
    } catch {
      return NextResponse.json({ error: "Invalid URL" }, { status: 400 });
    }

    const zai = await ZAI.create();
    const result = await zai.functions.invoke("page_reader", { url: target });
    const data = result?.data;

    if (!data?.html) {
      return NextResponse.json(
        { error: "Could not extract content from that page." },
        { status: 422 }
      );
    }

    // Convert HTML to readable text
    const text = data.html
      .replace(/<script[\s\S]*?<\/script>/gi, " ")
      .replace(/<style[\s\S]*?<\/style>/gi, " ")
      .replace(/<\/(p|div|h[1-6]|li|tr)>/gi, "\n")
      .replace(/<br\s*\/?>/gi, "\n")
      .replace(/<[^>]*>/g, " ")
      .replace(/&nbsp;/g, " ")
      .replace(/&amp;/g, "&")
      .replace(/&lt;/g, "<")
      .replace(/&gt;/g, ">")
      .replace(/&quot;/g, '"')
      .replace(/&#39;/g, "'")
      .replace(/[ \t]+/g, " ")
      .replace(/\n{3,}/g, "\n\n")
      .trim();

    return NextResponse.json({
      title: data.title || target,
      url: data.url || target,
      publishedTime: data.publishedTime || null,
      text: text.slice(0, 20000),
      tokens: data.usage?.tokens ?? null,
    });
  } catch (err) {
    console.error("[reader] error:", err);
    return NextResponse.json(
      { error: "Failed to read the page. It may block extraction — try another URL." },
      { status: 500 }
    );
  }
}
