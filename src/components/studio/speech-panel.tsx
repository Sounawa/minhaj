"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import {
  AudioLines,
  Mic,
  Square,
  Play,
  Pause,
  Download,
  Loader2,
  Upload,
  FileAudio,
  Copy,
  Volume2,
} from "lucide-react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Label } from "@/components/ui/label";
import { Slider } from "@/components/ui/slider";
import { ScrollArea } from "@/components/ui/scroll-area";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { cn, timeAgo } from "@/lib/utils";
import { TTS_VOICES } from "@/lib/personas";

const MAX_AUDIO_BYTES = 25 * 1024 * 1024; // 25MB
const MAX_TTS_CHARS = 800;

interface SpeechRecord {
  id: string;
  kind: string;
  input: string;
  voice: string | null;
  speed: number | null;
  duration: number | null;
  createdAt: string;
}

export default function SpeechPanel() {
  return (
    <Tabs defaultValue="tts" className="gap-4">
      <TabsList>
        <TabsTrigger value="tts">
          <Volume2 className="size-4" /> Text → Speech
        </TabsTrigger>
        <TabsTrigger value="asr">
          <Mic className="size-4" /> Speech → Text
        </TabsTrigger>
      </TabsList>
      <TabsContent value="tts">
        <TTSTab />
      </TabsContent>
      <TabsContent value="asr">
        <ASRTab />
      </TabsContent>
    </Tabs>
  );
}

/* ══════════════ TTS ══════════════ */

function TTSTab() {
  const [text, setText] = useState("");
  const [voice, setVoice] = useState("tongtong");
  const [speed, setSpeed] = useState(1.0);
  const [generating, setGenerating] = useState(false);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [records, setRecords] = useState<SpeechRecord[]>([]);

  const loadRecords = useCallback(async () => {
    try {
      const res = await fetch("/api/speech");
      const data = await res.json();
      setRecords((data.records || []).filter((r: SpeechRecord) => r.kind === "tts"));
    } catch {
      /* non-fatal */
    }
  }, []);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch("/api/speech");
        const data = await res.json();
        if (!cancelled)
          setRecords((data.records || []).filter((r: SpeechRecord) => r.kind === "tts"));
      } catch {
        /* non-fatal */
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    return () => {
      if (audioUrl) URL.revokeObjectURL(audioUrl);
    };
  }, [audioUrl]);

  const generate = async () => {
    if (!text.trim() || generating) return;
    if (text.length > MAX_TTS_CHARS) {
      toast.error(`Text is ${text.length} chars — the limit is ${MAX_TTS_CHARS}.`);
      return;
    }
    setGenerating(true);
    setIsPlaying(false);
    try {
      const res = await fetch("/api/tts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, voice, speed }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "TTS failed");
      if (audioUrl) URL.revokeObjectURL(audioUrl);
      setAudioUrl(data.audio);
      loadRecords();
      toast.success("Audio ready ▶");
    } catch (err) {
      toast.error(err instanceof Error ? err.message : "TTS failed");
    } finally {
      setGenerating(false);
    }
  };

  const togglePlay = () => {
    if (!audioRef.current) return;
    if (isPlaying) {
      audioRef.current.pause();
    } else {
      audioRef.current.play();
    }
  };

  return (
    <div className="grid gap-5 xl:grid-cols-[minmax(0,1fr)_300px]">
      <div className="space-y-4">
        <Card>
          <CardContent className="space-y-4 p-5">
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <Label htmlFor="tts-text">Text to speak</Label>
                <span
                  className={cn(
                    "text-[11px] tabular-nums",
                    text.length > MAX_TTS_CHARS ? "font-semibold text-destructive" : "text-muted-foreground"
                  )}
                >
                  {text.length}/{MAX_TTS_CHARS}
                </span>
              </div>
              <Textarea
                id="tts-text"
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Type anything — a greeting, a paragraph, a line from a story…"
                className="min-h-32 text-sm"
              />
            </div>

            <div className="grid gap-4 sm:grid-cols-2">
              <div className="space-y-2">
                <Label>Voice</Label>
                <Select value={voice} onValueChange={setVoice}>
                  <SelectTrigger className="w-full">
                    <SelectValue placeholder="Choose voice" />
                  </SelectTrigger>
                  <SelectContent>
                    {TTS_VOICES.map((v) => (
                      <SelectItem key={v.value} value={v.value}>
                        {v.label}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <Label>Speed</Label>
                  <span className="text-[11px] tabular-nums text-muted-foreground">
                    {speed.toFixed(2)}×
                  </span>
                </div>
                <Slider
                  value={[speed]}
                  onValueChange={([v]) => setSpeed(v)}
                  min={0.5}
                  max={2}
                  step={0.05}
                  aria-label="Speech speed"
                />
              </div>
            </div>

            <Button className="w-full" size="lg" onClick={generate} disabled={generating || !text.trim()}>
              {generating ? (
                <>
                  <Loader2 className="size-4.5 animate-spin" /> Synthesizing…
                </>
              ) : (
                <>
                  <AudioLines className="size-4.5" /> Generate speech
                </>
              )}
            </Button>
          </CardContent>
        </Card>

        {/* Player */}
        {audioUrl && (
          <Card className="animate-fade-up">
            <CardContent className="flex flex-col gap-3 p-5 sm:flex-row sm:items-center">
              <button
                onClick={togglePlay}
                className="flex size-12 shrink-0 items-center justify-center rounded-full bg-primary text-primary-foreground shadow-md transition-transform hover:scale-105"
                aria-label={isPlaying ? "Pause" : "Play"}
              >
                {isPlaying ? <Pause className="size-5" /> : <Play className="size-5 ml-0.5" />}
              </button>
              <div className="min-w-0 flex-1">
                <p className="text-sm font-medium">Generated audio</p>
                <p className="text-xs text-muted-foreground">
                  {voice} · {speed.toFixed(2)}× speed
                </p>
                <audio
                  ref={audioRef}
                  src={audioUrl}
                  onPlay={() => setIsPlaying(true)}
                  onPause={() => setIsPlaying(false)}
                  onEnded={() => setIsPlaying(false)}
                  controls
                  className="mt-2 h-9 w-full"
                />
              </div>
              <Button
                variant="outline"
                size="sm"
                onClick={() => {
                  const a = document.createElement("a");
                  a.href = audioUrl;
                  a.download = "tts-voice.wav";
                  a.click();
                }}
              >
                <Download className="size-4" /> Save
              </Button>
            </CardContent>
          </Card>
        )}
      </div>

      {/* History */}
      <Card className="h-fit">
        <CardContent className="p-0">
          <div className="border-b px-4 py-3">
            <h3 className="text-sm font-semibold">Recent clips</h3>
          </div>
          <ScrollArea className="max-h-96">
            <div className="space-y-2 p-3">
              {records.length === 0 ? (
                <p className="py-8 text-center text-xs text-muted-foreground">
                  No voice clips yet.
                </p>
              ) : (
                records.map((r) => (
                  <div key={r.id} className="rounded-lg border bg-muted/30 px-3 py-2.5">
                    <p className="line-clamp-2 text-xs leading-snug">{r.input}</p>
                    <p className="mt-1.5 flex items-center gap-1.5 text-[10.5px] text-muted-foreground">
                      <Badge variant="secondary" className="px-1.5 py-0 text-[10px]">
                        {r.voice}
                      </Badge>
                      {r.speed?.toFixed(1)}× · {r.duration}s · {timeAgo(r.createdAt)}
                    </p>
                  </div>
                ))
              )}
            </div>
          </ScrollArea>
        </CardContent>
      </Card>
    </div>
  );
}

/* ══════════════ ASR ══════════════ */

function ASRTab() {
  const [file, setFile] = useState<File | null>(null);
  const [fileUrl, setFileUrl] = useState<string | null>(null);
  const [transcribing, setTranscribing] = useState(false);
  const [transcript, setTranscript] = useState<string | null>(null);
  const [dragging, setDragging] = useState(false);
  const [recording, setRecording] = useState(false);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const setAudioFile = useCallback((f: File) => {
    if (!f.type.startsWith("audio/") && !/\.(wav|mp3|m4a|flac|ogg)$/i.test(f.name)) {
      toast.error("Please choose an audio file (WAV, MP3, M4A…)");
      return;
    }
    if (f.size > MAX_AUDIO_BYTES) {
      toast.error("Audio too large — max 25 MB.");
      return;
    }
    setFile(f);
    setTranscript(null);
    if (fileUrl) URL.revokeObjectURL(fileUrl);
    setFileUrl(URL.createObjectURL(f));
  }, [fileUrl]);

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mimeType = MediaRecorder.isTypeSupported("audio/webm") ? "audio/webm" : "";
      const recorder = new MediaRecorder(stream, mimeType ? { mimeType } : undefined);
      chunksRef.current = [];
      recorder.ondataavailable = (e) => {
        if (e.data.size > 0) chunksRef.current.push(e.data);
      };
      recorder.onstop = () => {
        stream.getTracks().forEach((t) => t.stop());
        const blob = new Blob(chunksRef.current, { type: recorder.mimeType || "audio/webm" });
        const f = new File([blob], `recording-${Date.now()}.webm`, { type: blob.type });
        setAudioFile(f);
        toast.info("Recording captured — now transcribe it.");
      };
      recorder.start();
      mediaRecorderRef.current = recorder;
      setRecording(true);
      toast.success("Recording… speak now! Click stop when done.");
    } catch {
      toast.error("Microphone access denied or unavailable.");
    }
  };

  const stopRecording = () => {
    mediaRecorderRef.current?.stop();
    setRecording(false);
  };

  const transcribe = async () => {
    if (!file || transcribing) return;
    setTranscribing(true);
    try {
      const b64 = await new Promise<string>((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result as string);
        reader.onerror = reject;
        reader.readAsDataURL(file);
      });
      const res = await fetch("/api/asr", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ audioBase64: b64, fileName: file.name }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Transcription failed");
      setTranscript(data.text);
      toast.success("Transcription ready");
    } catch (err) {
      toast.error(err instanceof Error ? err.message : "Transcription failed");
    } finally {
      setTranscribing(false);
    }
  };

  return (
    <div className="grid gap-5 xl:grid-cols-[minmax(0,1fr)_minmax(0,1fr)]">
      {/* Upload / record */}
      <Card className="h-fit">
        <CardContent className="space-y-4 p-5">
          <div
            role="button"
            tabIndex={0}
            aria-label="Upload audio"
            onClick={() => fileInputRef.current?.click()}
            onKeyDown={(e) => e.key === "Enter" && fileInputRef.current?.click()}
            onDragOver={(e) => {
              e.preventDefault();
              setDragging(true);
            }}
            onDragLeave={() => setDragging(false)}
            onDrop={(e) => {
              e.preventDefault();
              setDragging(false);
              const f = e.dataTransfer.files?.[0];
              if (f) setAudioFile(f);
            }}
            className={cn(
              "flex cursor-pointer flex-col items-center justify-center gap-3 rounded-xl border-2 border-dashed px-6 py-10 text-center transition-all",
              dragging ? "border-primary bg-primary/10" : "hover:border-primary/50 hover:bg-accent/30"
            )}
          >
            <span
              className={cn(
                "flex size-12 items-center justify-center rounded-full",
                recording ? "animate-pulse bg-destructive/15 text-destructive" : "bg-primary/10 text-primary"
              )}
            >
              <Upload className="size-5" />
            </span>
            <div>
              <p className="text-sm font-medium">
                {recording ? "Recording — click Stop when finished" : "Drop or choose an audio file"}
              </p>
              <p className="mt-1 text-xs text-muted-foreground">
                WAV, MP3, M4A… · up to 25 MB
              </p>
            </div>
          </div>

          <input
            ref={fileInputRef}
            type="file"
            accept="audio/*"
            className="hidden"
            onChange={(e) => {
              const f = e.target.files?.[0];
              if (f) setAudioFile(f);
              e.target.value = "";
            }}
          />

          <div className="flex gap-2">
            <Button
              variant="outline"
              className="flex-1"
              onClick={recording ? stopRecording : startRecording}
            >
              {recording ? (
                <>
                  <Square className="size-4" /> Stop recording
                </>
              ) : (
                <>
                  <Mic className="size-4" /> Record with mic
                </>
              )}
            </Button>
            <Button className="flex-1" onClick={transcribe} disabled={!file || transcribing}>
              {transcribing ? (
                <>
                  <Loader2 className="size-4.5 animate-spin" /> Transcribing…
                </>
              ) : (
                <>
                  <FileAudio className="size-4.5" /> Transcribe
                </>
              )}
            </Button>
          </div>

          {file && fileUrl && (
            <div className="space-y-2 rounded-lg border bg-muted/30 p-3">
              <p className="flex items-center gap-1.5 text-xs font-medium">
                <FileAudio className="size-3.5 text-primary" />
                <span className="max-w-[220px] truncate">{file.name}</span>
                <span className="text-muted-foreground">({(file.size / 1024).toFixed(0)} KB)</span>
              </p>
              <audio src={fileUrl} controls className="h-9 w-full" />
            </div>
          )}
        </CardContent>
      </Card>

      {/* Transcript */}
      <Card className="h-fit">
        <CardContent className="p-5">
          <div className="mb-3 flex items-center justify-between">
            <h3 className="text-sm font-semibold">Transcript</h3>
            {transcript && (
              <Button
                variant="ghost"
                size="sm"
                onClick={() => {
                  navigator.clipboard.writeText(transcript);
                  toast.success("Copied to clipboard");
                }}
              >
                <Copy className="size-4" /> Copy
              </Button>
            )}
          </div>
          {transcribing ? (
            <div className="flex flex-col items-center gap-3 py-10">
              <Loader2 className="size-6 animate-spin text-primary" />
              <p className="text-sm text-muted-foreground">Listening carefully…</p>
            </div>
          ) : transcript ? (
            <div className="animate-fade-up rounded-lg border bg-muted/30 p-4">
              <p className="whitespace-pre-wrap text-sm leading-relaxed">{transcript}</p>
            </div>
          ) : (
            <div className="flex flex-col items-center gap-2 py-10 text-center">
              <Mic className="size-8 text-muted-foreground/40" />
              <p className="max-w-xs text-xs text-muted-foreground">
                Upload or record audio, then hit <b>Transcribe</b> — the speech recognition
                skill will turn it into text.
              </p>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
