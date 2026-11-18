import { NextRequest, NextResponse } from "next/server";
import fs from "fs/promises";
import path from "path";

export const runtime = "nodejs";

type Ctx = { params: Promise<{ name: string }> };

export async function GET(_req: NextRequest, ctx: Ctx) {
  try {
    const { name } = await ctx.params;
    // Basic path traversal guard
    if (!/^img-[\w-]+\.png$/.test(name)) {
      return NextResponse.json({ error: "Invalid file name" }, { status: 400 });
    }
    const filePath = path.join(process.cwd(), "generated-images", name);
    const buffer = await fs.readFile(filePath);
    return new NextResponse(new Uint8Array(buffer), {
      headers: {
        "Content-Type": "image/png",
        "Cache-Control": "public, max-age=31536000, immutable",
      },
    });
  } catch {
    return NextResponse.json({ error: "File not found" }, { status: 404 });
  }
}
