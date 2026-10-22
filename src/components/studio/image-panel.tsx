"use client";

import { useCallback, useEffect, useState } from "react";
import {
  Wand2,
  Download,
  Trash2,
  Loader2,
  ImageOff,
  Maximize2,
  RefreshCcw,
} from "lucide-react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { cn, timeAgo } from "@/lib/utils";
import { IMAGE_SIZES } from "@/lib/personas";

interface ImageRecord {
  id: string;
  prompt: string;
  size: string;
  filePath: string;
  createdAt: string;
}

const PROMPT_IDEAS = [
  "A cozy floating bookshop on a cloud at sunset, warm light, storybook illustration",
  "Isometric miniature greenhouse, glass panes, tiny gardener robot, soft studio light",
  "Portrait of an arctic fox wearing a knitted scarf, snowy bokeh, ultra detailed",
  "Retro-futuristic ramen stand in neon Tokyo alley, rain reflections, cinematic",
];

export default function ImagePanel() {
  const [prompt, setPrompt] = useState("");
  const [size, setSize] = useState<string>("1024x1024");
  const [generating, setGenerating] = useState(false);
  const [images, setImages] = useState<ImageRecord[]>([]);
  const [loadingList, setLoadingList] = useState(true);
  const [preview, setPreview] = useState<ImageRecord | null>(null);

  const loadImages = useCallback(async () => {
    try {
      const res = await fetch("/api/images");
      const data = await res.json();
      setImages(data.images || []);
    } catch {
      /* non-fatal */
    } finally {
      setLoadingList(false);
    }
  }, []);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch("/api/images");
        const data = await res.json();
        if (!cancelled) setImages(data.images || []);
      } catch {
        /* non-fatal */
      } finally {
        if (!cancelled) setLoadingList(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  const generate = async () => {
    if (!prompt.trim() || generating) return;
    setGenerating(true);
    try {
      const res = await fetch("/api/images", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt, size }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Generation failed");
      setImages((prev) => [data.image, ...prev]);
      toast.success("Image generated ✨");
    } catch (err) {
      toast.error(err instanceof Error ? err.message : "Generation failed");
    } finally {
      setGenerating(false);
    }
  };

  const remove = async (id: string) => {
    try {
      await fetch(`/api/images/${id}`, { method: "DELETE" });
      setImages((prev) => prev.filter((i) => i.id !== id));
      if (preview?.id === id) setPreview(null);
      toast.success("Image deleted");
    } catch {
      toast.error("Delete failed");
    }
  };

  return (
    <div className="space-y-5">
      {/* Composer */}
      <Card>
        <CardContent className="grid gap-4 p-5 lg:grid-cols-[1fr_280px]">
          <div className="flex flex-col gap-3">
            <Textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Describe the image you want… e.g. “A serene mountain lake at dawn, mist over water, oil painting style”"
              className="min-h-28 flex-1 text-sm"
              aria-label="Image prompt"
            />
            <div className="flex flex-wrap gap-1.5">
              {PROMPT_IDEAS.map((idea) => (
                <button
                  key={idea}
                  onClick={() => setPrompt(idea)}
                  className="max-w-full truncate rounded-full border bg-muted/40 px-3 py-1 text-[11px] text-muted-foreground transition-colors hover:border-primary/40 hover:text-foreground"
                  title={idea}
                >
                  {idea.slice(0, 42)}…
                </button>
              ))}
            </div>
          </div>

          <div className="flex flex-col gap-3">
            <div>
              <p className="mb-2 text-xs font-medium text-muted-foreground">Aspect ratio</p>
              <div className="grid grid-cols-3 gap-1.5">
                {IMAGE_SIZES.map((s) => (
                  <button
                    key={s.value}
                    onClick={() => setSize(s.value)}
                    title={s.label}
                    className={cn(
                      "flex flex-col items-center gap-1.5 rounded-lg border p-2 transition-all",
                      size === s.value
                        ? "border-primary bg-primary/10 text-primary shadow-sm"
                        : "hover:border-primary/40 hover:bg-accent/40"
                    )}
                  >
                    <span
                      className={cn(
                        "block rounded-[3px] border-2",
                        size === s.value ? "border-primary" : "border-muted-foreground/40"
                      )}
                      style={{
                        width: `${Math.min(26, (s.w / Math.max(s.w, s.h)) * 26)}px`,
                        height: `${Math.min(26, (s.h / Math.max(s.w, s.h)) * 26)}px`,
                      }}
                    />
                    <span className="text-[9.5px] font-medium leading-none">
                      {s.value.split("x")[0]}×{s.value.split("x")[1]}
                    </span>
                  </button>
                ))}
              </div>
            </div>
            <Button
              onClick={generate}
              disabled={generating || !prompt.trim()}
              className="w-full"
              size="lg"
            >
              {generating ? (
                <>
                  <Loader2 className="size-4.5 animate-spin" /> Painting…
                </>
              ) : (
                <>
                  <Wand2 className="size-4.5" /> Generate image
                </>
              )}
            </Button>
            <p className="text-center text-[11px] text-muted-foreground">
              Powered by the Image Generation skill
            </p>
          </div>
        </CardContent>
      </Card>

      {/* Generating placeholder */}
      {generating && (
        <div
          className="shimmer-bg relative flex items-center justify-center overflow-hidden rounded-xl border"
          style={{ aspectRatio: size.replace("x", " / ") }}
        >
          <div className="flex flex-col items-center gap-2 text-muted-foreground">
            <Loader2 className="size-6 animate-spin" />
            <p className="text-xs font-medium">Dreaming up your image…</p>
            <p className="max-w-xs px-4 text-center text-[11px] opacity-70">
              This usually takes 10–30 seconds
            </p>
          </div>
        </div>
      )}

      {/* Gallery */}
      <div>
        <div className="mb-3 flex items-center justify-between">
          <h3 className="text-sm font-semibold text-muted-foreground">
            Gallery {images.length > 0 && <Badge variant="secondary" className="ml-1.5">{images.length}</Badge>}
          </h3>
          <Button variant="ghost" size="sm" onClick={loadImages} disabled={loadingList}>
            {loadingList ? <Loader2 className="size-4 animate-spin" /> : <RefreshCcw className="size-4" />}
            Refresh
          </Button>
        </div>

        {loadingList ? (
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 xl:grid-cols-4">
            {Array.from({ length: 4 }).map((_, i) => (
              <div key={i} className="aspect-square animate-pulse rounded-xl bg-muted" />
            ))}
          </div>
        ) : images.length === 0 && !generating ? (
          <div className="flex flex-col items-center justify-center gap-3 rounded-xl border border-dashed py-16">
            <ImageOff className="size-8 text-muted-foreground/50" />
            <p className="text-sm text-muted-foreground">
              Your gallery is empty — create your first masterpiece above!
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 xl:grid-cols-4">
            {images.map((img) => (
              <Card key={img.id} className="group overflow-hidden py-0">
                <button
                  className="relative block w-full"
                  onClick={() => setPreview(img)}
                  aria-label={`Preview: ${img.prompt.slice(0, 50)}`}
                >
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img
                    src={`/api/images/file/${img.filePath}`}
                    alt={img.prompt.slice(0, 80)}
                    className="aspect-square w-full object-cover transition-transform duration-300 group-hover:scale-[1.03]"
                    loading="lazy"
                  />
                  <span className="absolute inset-0 bg-black/0 transition-colors group-hover:bg-black/25" />
                  <span className="absolute right-2 top-2 flex size-8 items-center justify-center rounded-full bg-black/55 text-white opacity-0 backdrop-blur transition-opacity group-hover:opacity-100">
                    <Maximize2 className="size-4" />
                  </span>
                </button>
                <div className="flex items-start justify-between gap-2 p-2.5">
                  <div className="min-w-0">
                    <p className="truncate text-xs font-medium" title={img.prompt}>
                      {img.prompt}
                    </p>
                    <p className="text-[10.5px] text-muted-foreground">
                      {img.size} · {timeAgo(img.createdAt)}
                    </p>
                  </div>
                  <div className="flex shrink-0 gap-0.5">
                    <Button
                      variant="ghost"
                      size="icon-sm"
                      aria-label="Download image"
                      onClick={() => {
                        const a = document.createElement("a");
                        a.href = `/api/images/file/${img.filePath}`;
                        a.download = img.filePath;
                        a.click();
                      }}
                    >
                      <Download className="size-3.5" />
                    </Button>
                    <Button
                      variant="ghost"
                      size="icon-sm"
                      aria-label="Delete image"
                      className="hover:text-destructive"
                      onClick={() => remove(img.id)}
                    >
                      <Trash2 className="size-3.5" />
                    </Button>
                  </div>
                </div>
              </Card>
            ))}
          </div>
        )}
      </div>

      {/* Preview dialog */}
      <Dialog open={!!preview} onOpenChange={(open) => !open && setPreview(null)}>
        <DialogContent className="max-w-2xl">
          {preview && (
            <>
              <DialogHeader>
                <DialogTitle className="pr-6 text-base leading-snug">
                  {preview.prompt}
                </DialogTitle>
                <DialogDescription>
                  {preview.size} · {timeAgo(preview.createdAt)}
                </DialogDescription>
              </DialogHeader>
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={`/api/images/file/${preview.filePath}`}
                alt={preview.prompt}
                className="max-h-[65vh] w-full rounded-lg border object-contain"
              />
              <div className="flex justify-end gap-2">
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => {
                    const a = document.createElement("a");
                    a.href = `/api/images/file/${preview.filePath}`;
                    a.download = preview.filePath;
                    a.click();
                  }}
                >
                  <Download className="size-4" /> Download
                </Button>
                <Button
                  variant="destructive"
                  size="sm"
                  onClick={() => remove(preview.id)}
                >
                  <Trash2 className="size-4" /> Delete
                </Button>
              </div>
            </>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}
