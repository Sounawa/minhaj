"use client";

import { useCallback, useRef, useState } from "react";
import {
  ScanEye,
  Upload,
  ImageIcon,
  Loader2,
  Link2,
  RotateCcw,
} from "lucide-react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { cn, formatBytes } from "@/lib/utils";
import { renderMarkdown } from "@/lib/markdown";

const MAX_FILE_BYTES = 6 * 1024 * 1024; // 6MB

const QUICK_QUESTIONS = [
  "Describe this image in detail.",
  "Extract all text visible in this image.",
  "Identify objects and count them.",
  "What emotions or mood does this image convey?",
  "Suggest an improved alt-text for accessibility.",
];

interface Analysis {
  prompt: string;
  answer: string;
  image: string;
  createdAt: string;
}

export default function VisionPanel() {
  const [image, setImage] = useState<string | null>(null);
  const [imageMeta, setImageMeta] = useState<{ name: string; size: number } | null>(null);
  const [prompt, setPrompt] = useState("");
  const [urlValue, setUrlValue] = useState("");
  const [analyzing, setAnalyzing] = useState(false);
  const [results, setResults] = useState<Analysis[]>([]);
  const [dragging, setDragging] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFile = useCallback((file: File) => {
    if (!file.type.startsWith("image/")) {
      toast.error("Please choose an image file (PNG, JPG, WebP…)");
      return;
    }
    if (file.size > MAX_FILE_BYTES) {
      toast.error("Image too large — please use one under 6 MB.");
      return;
    }
    const reader = new FileReader();
    reader.onload = () => {
      setImage(reader.result as string);
      setImageMeta({ name: file.name, size: file.size });
    };
    reader.readAsDataURL(file);
  }, []);

  const onDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setDragging(false);
    const file = e.dataTransfer.files?.[0];
    if (file) handleFile(file);
  };

  const applyImageUrl = () => {
    const url = urlValue.trim();
    if (!url) return;
    if (!/^https?:\/\//i.test(url)) {
      toast.error("Enter a full http(s) image URL");
      return;
    }
    setImage(url);
    setImageMeta({ name: url.split("/").pop() || "image from URL", size: 0 });
  };

  const analyze = async () => {
    if (!image || analyzing) return;
    setAnalyzing(true);
    const question = prompt.trim() || "Describe this image in detail.";
    try {
      const res = await fetch("/api/vision", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image, prompt: question }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Analysis failed");
      setResults((prev) => [
        { prompt: question, answer: data.analysis, image, createdAt: new Date().toISOString() },
        ...prev.slice(0, 4),
      ]);
      toast.success("Analysis ready");
    } catch (err) {
      toast.error(err instanceof Error ? err.message : "Analysis failed");
    } finally {
      setAnalyzing(false);
    }
  };

  const reset = () => {
    setImage(null);
    setImageMeta(null);
    setPrompt("");
    setUrlValue("");
  };

  return (
    <div className="grid gap-5 xl:grid-cols-[minmax(0,420px)_1fr]">
      {/* Left: input */}
      <div className="space-y-4">
        <Card>
          <CardContent className="space-y-4 p-5">
            {/* Dropzone */}
            {!image ? (
              <div
                role="button"
                tabIndex={0}
                aria-label="Upload an image"
                onClick={() => fileInputRef.current?.click()}
                onKeyDown={(e) => e.key === "Enter" && fileInputRef.current?.click()}
                onDragOver={(e) => {
                  e.preventDefault();
                  setDragging(true);
                }}
                onDragLeave={() => setDragging(false)}
                onDrop={onDrop}
                onPaste={(e) => {
                  const item = Array.from(e.clipboardData.items).find((i) =>
                    i.type.startsWith("image/")
                  );
                  const file = item?.getAsFile();
                  if (file) handleFile(file);
                }}
                className={cn(
                  "flex cursor-pointer flex-col items-center justify-center gap-3 rounded-xl border-2 border-dashed px-6 py-12 text-center transition-all",
                  dragging
                    ? "border-primary bg-primary/10"
                    : "hover:border-primary/50 hover:bg-accent/30"
                )}
              >
                <span className="flex size-12 items-center justify-center rounded-full bg-primary/10 text-primary">
                  <Upload className="size-5" />
                </span>
                <div>
                  <p className="text-sm font-medium">Drop, paste or click to upload</p>
                  <p className="mt-1 text-xs text-muted-foreground">
                    PNG, JPG, WebP or GIF · up to 6 MB
                  </p>
                </div>
              </div>
            ) : (
              <div className="space-y-3">
                <div className="relative overflow-hidden rounded-xl border">
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img src={image} alt="Selected for analysis" className="max-h-72 w-full object-contain bg-muted/30" />
                  <Button
                    variant="secondary"
                    size="icon-sm"
                    className="absolute right-2 top-2 shadow-md"
                    aria-label="Remove image"
                    onClick={reset}
                  >
                    <RotateCcw className="size-3.5" />
                  </Button>
                </div>
                {imageMeta && (
                  <p className="flex items-center gap-1.5 text-[11px] text-muted-foreground">
                    <ImageIcon className="size-3" />
                    <span className="max-w-[240px] truncate font-medium">{imageMeta.name}</span>
                    {imageMeta.size > 0 && <>· {formatBytes(imageMeta.size)}</>}
                  </p>
                )}
              </div>
            )}

            <input
              ref={fileInputRef}
              type="file"
              accept="image/*"
              className="hidden"
              onChange={(e) => {
                const f = e.target.files?.[0];
                if (f) handleFile(f);
                e.target.value = "";
              }}
            />

            {/* URL input */}
            <div className="flex gap-2">
              <div className="relative flex-1">
                <Link2 className="absolute left-2.5 top-1/2 size-4 -translate-y-1/2 text-muted-foreground" />
                <Input
                  value={urlValue}
                  onChange={(e) => setUrlValue(e.target.value)}
                  onKeyDown={(e) => e.key === "Enter" && applyImageUrl()}
                  placeholder="…or paste an image URL"
                  className="pl-8"
                  aria-label="Image URL"
                />
              </div>
              <Button variant="outline" onClick={applyImageUrl}>
                Load
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Question */}
        <Card>
          <CardContent className="space-y-3 p-5">
            <p className="text-xs font-medium text-muted-foreground">
              What do you want to know about the image?
            </p>
            <Textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Leave empty for a full description, or ask anything specific…"
              className="min-h-20 text-sm"
              aria-label="Question about the image"
            />
            <div className="flex flex-wrap gap-1.5">
              {QUICK_QUESTIONS.map((q) => (
                <button
                  key={q}
                  onClick={() => setPrompt(q)}
                  className="rounded-full border bg-muted/40 px-3 py-1 text-[11px] text-muted-foreground transition-colors hover:border-primary/40 hover:text-foreground"
                >
                  {q}
                </button>
              ))}
            </div>
            <Button className="w-full" size="lg" onClick={analyze} disabled={!image || analyzing}>
              {analyzing ? (
                <>
                  <Loader2 className="size-4.5 animate-spin" /> Analyzing…
                </>
              ) : (
                <>
                  <ScanEye className="size-4.5" /> Analyze image
                </>
              )}
            </Button>
          </CardContent>
        </Card>
      </div>

      {/* Right: results */}
      <div className="space-y-4">
        {results.length === 0 && !analyzing ? (
          <Card className="h-full">
            <CardContent className="flex h-full min-h-72 flex-col items-center justify-center gap-3 p-8 text-center">
              <span className="flex size-14 items-center justify-center rounded-2xl bg-accent text-accent-foreground">
                <ScanEye className="size-7" />
              </span>
              <p className="font-semibold">Vision analysis results appear here</p>
              <p className="max-w-sm text-sm text-muted-foreground">
                Upload an image and ask a question — the vision model will describe
                scenes, read text, identify objects and more.
              </p>
              <div className="mt-2 flex flex-wrap justify-center gap-1.5">
                {["Scene description", "OCR & text", "Object detection", "Mood & style"].map(
                  (t) => (
                    <Badge key={t} variant="secondary">
                      {t}
                    </Badge>
                  )
                )}
              </div>
            </CardContent>
          </Card>
        ) : (
          <>
            {analyzing && (
              <Card>
                <CardContent className="flex items-center gap-3 p-5">
                  <Loader2 className="size-5 animate-spin text-primary" />
                  <div>
                    <p className="text-sm font-medium">Looking at your image…</p>
                    <p className="text-xs text-muted-foreground">
                      The vision model is examining the details
                    </p>
                  </div>
                </CardContent>
              </Card>
            )}
            {results.map((r, i) => (
              <Card key={r.createdAt} className="animate-fade-up">
                <CardContent className="p-5">
                  <div className="mb-3 flex items-start justify-between gap-3">
                    <div className="flex items-center gap-2">
                      <Badge variant="accent" className="gap-1">
                        <ScanEye className="size-3" /> Analysis {results.length - i}
                      </Badge>
                      <p className="hidden max-w-xs truncate text-xs text-muted-foreground sm:block">
                        {r.prompt}
                      </p>
                    </div>
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img
                      src={r.image}
                      alt="Analyzed"
                      className="size-10 shrink-0 rounded-md border object-cover"
                    />
                  </div>
                  <div
                    className="msg-content text-sm"
                    dangerouslySetInnerHTML={{ __html: renderMarkdown(r.answer) }}
                  />
                </CardContent>
              </Card>
            ))}
          </>
        )}
      </div>
    </div>
  );
}
