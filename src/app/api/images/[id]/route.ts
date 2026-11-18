import { NextRequest, NextResponse } from "next/server";
import fs from "fs/promises";
import path from "path";
import { db } from "@/lib/db";

export const runtime = "nodejs";

type Ctx = { params: Promise<{ id: string }> };

export async function DELETE(_req: NextRequest, ctx: Ctx) {
  try {
    const { id } = await ctx.params;
    const record = await db.imageGen.findUnique({ where: { id } });
    if (!record) {
      return NextResponse.json({ error: "Not found" }, { status: 404 });
    }
    // Remove file if exists
    try {
      await fs.unlink(path.join(process.cwd(), "generated-images", record.filePath));
    } catch {
      /* file may already be gone */
    }
    await db.imageGen.delete({ where: { id } });
    return NextResponse.json({ ok: true });
  } catch (err) {
    console.error("[image] delete error:", err);
    return NextResponse.json({ error: "Failed to delete image" }, { status: 500 });
  }
}
