#!/usr/bin/env python3
"""Render the audio drill episodes with Kokoro TTS and build the podcast feed.

Setup (free, no Mac needed):
    pip install kokoro-onnx soundfile numpy
    # model files: github.com/thewh1teagle/kokoro-onnx, release tag model-files-v1.0
    #   kokoro-v1.0.int8.onnx   voices-v1.0.bin   (put them in ./models)
    # ffmpeg must be on PATH

Usage:
    python generate.py audio [episode numbers...]   # render m4a files into docs/audio
    python generate.py feed                         # write docs/feed.xml and docs/index.html
    python generate.py scripts                      # write SCRIPTS.md from content.py
"""
import hashlib
import os
import subprocess
import sys
from email.utils import formatdate
from xml.sax.saxutils import escape

import numpy as np

from content import EPISODES, SHOW_TITLE

HERE = os.path.dirname(os.path.abspath(__file__))
MODELS = os.environ.get("KOKORO_MODELS", os.path.join(HERE, "models"))
OUT = os.path.join(HERE, "docs")
AUDIO = os.path.join(OUT, "audio")
CACHE = os.path.join(HERE, ".cache")
BASE_URL = os.environ.get("BASE_URL", "https://akrthk93.github.io/dsa-audio-drills")

VOICE, LANG, SPEED, SR = "bm_lewis", "en-gb", 1.0, 24000
# Published dates are fixed so episode order is stable in podcast apps (oldest first).
PUB_EPOCH = 1794787200  # 2026-11-16 00:00 UTC

_kokoro = None


def tts(text):
    """Synthesize one sentence, cached on disk by text hash."""
    global _kokoro
    os.makedirs(CACHE, exist_ok=True)
    key = hashlib.sha1(f"{VOICE}|{LANG}|{SPEED}|{text}".encode()).hexdigest()
    path = os.path.join(CACHE, key + ".npy")
    if os.path.exists(path):
        return np.load(path)
    if _kokoro is None:
        from kokoro_onnx import Kokoro
        _kokoro = Kokoro(os.path.join(MODELS, "kokoro-v1.0.int8.onnx"),
                         os.path.join(MODELS, "voices-v1.0.bin"))
    samples, sr = _kokoro.create(text, voice=VOICE, speed=SPEED, lang=LANG)
    assert sr == SR, sr
    samples = np.asarray(samples, dtype=np.float32)
    np.save(path, samples)
    return samples


def silence(seconds):
    return np.zeros(int(SR * seconds), dtype=np.float32)


def thinking_gap(seconds):
    """Answer gap that is NOT digital silence: a soft tick every second over a
    very quiet noise bed, so silence-trimming players have less to cut."""
    n = int(SR * seconds)
    rng = np.random.default_rng(7)
    bed = rng.standard_normal(n).astype(np.float32)
    bed = np.convolve(bed, np.ones(8) / 8, mode="same") * 0.012  # soft, low-passed hiss
    t = np.arange(int(SR * 0.05)) / SR
    tick = (np.sin(2 * np.pi * 880 * t) * np.exp(-t * 70) * 0.10).astype(np.float32)
    out = bed
    for s in range(int(seconds)):
        i = int(SR * (s + 0.5))
        if i + len(tick) < n:
            out[i:i + len(tick)] += tick
    return out.astype(np.float32)


def chime():
    """Two soft notes that mark the start of each question."""
    t = np.arange(int(SR * 0.18)) / SR
    a = np.sin(2 * np.pi * 660 * t) * np.exp(-t * 14) * 0.12
    b = np.sin(2 * np.pi * 990 * t) * np.exp(-t * 14) * 0.12
    return np.concatenate([a, b]).astype(np.float32)


def say(parts, text, after=0.35):
    """Speak text sentence by sentence (keeps each TTS call short)."""
    buf, sentences = "", []
    for ch in text:
        buf += ch
        if ch in ".?!":
            sentences.append(buf.strip())
            buf = ""
    if buf.strip():
        sentences.append(buf.strip())
    for s in sentences:
        parts.append(tts(s))
        parts.append(silence(0.22))
    parts.append(silence(after))


def build_episode(ep):
    parts = [silence(0.4)]
    for line in ep["intro"]:
        say(parts, line, 0.3)
    parts.append(silence(0.5))
    for line in ep["lesson"]:
        say(parts, line, 0.45)
    parts.append(silence(0.6))
    for i, (aid, cue, pause, answer, _src, _tag) in enumerate(ep["items"], 1):
        parts.append(chime())
        parts.append(silence(0.25))
        say(parts, f"Question {i}.", 0.1)
        say(parts, cue, 0.1)
        parts.append(thinking_gap(pause))
        parts.append(silence(0.15))
        say(parts, answer, 0.9)
    for line in ep["outro"]:
        say(parts, line, 0.3)
    parts.append(silence(0.8))
    audio = np.concatenate(parts)
    peak = float(np.max(np.abs(audio)))
    return audio * (0.89 / peak)


def render(numbers):
    import soundfile as sf
    os.makedirs(AUDIO, exist_ok=True)
    for ep in EPISODES:
        if numbers and ep["n"] not in numbers:
            continue
        audio = build_episode(ep)
        wav = os.path.join(CACHE, ep["slug"] + ".wav")
        m4a = os.path.join(AUDIO, ep["slug"] + ".m4a")
        sf.write(wav, audio, SR)
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-ac", "1", "-ar", "44100",
             "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart",
             "-metadata", f"title={ep['title']}", "-metadata", f"album={SHOW_TITLE}",
             "-metadata", "artist=Karthik", "-metadata", f"track={ep['n']}", m4a],
            check=True)
        os.remove(wav)
        print(f"{m4a}  {len(audio) / SR / 60:.1f} min  {os.path.getsize(m4a) / 1e6:.1f} MB")


def duration_seconds(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return int(float(out.stdout.strip()))


def feed():
    items = []
    for ep in EPISODES:
        path = os.path.join(AUDIO, ep["slug"] + ".m4a")
        url = f"{BASE_URL}/audio/{ep['slug']}.m4a"
        secs = duration_seconds(path)
        desc = f"{len(ep['items'])} listen-and-answer-aloud items. Screen-free."
        items.append(f"""    <item>
      <title>{escape(ep['title'])}</title>
      <description>{escape(desc)}</description>
      <guid isPermaLink="false">dsa-audio-drills-v1-ep{ep['n']}</guid>
      <pubDate>{formatdate(PUB_EPOCH + ep['n'] * 3600, usegmt=True)}</pubDate>
      <enclosure url="{url}" length="{os.path.getsize(path)}" type="audio/x-m4a"/>
      <itunes:duration>{secs}</itunes:duration>
      <itunes:episode>{ep['n']}</itunes:episode>
      <itunes:explicit>false</itunes:explicit>
    </item>""")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{SHOW_TITLE}</title>
    <link>{BASE_URL}/</link>
    <atom:link href="{BASE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
    <language>en-gb</language>
    <description>Spoken pattern-recognition and complexity drills for coding interviews. Listen, answer aloud in the gap, hear the answer.</description>
    <itunes:author>Karthik</itunes:author>
    <itunes:summary>Spoken pattern-recognition and complexity drills for coding interviews.</itunes:summary>
    <itunes:explicit>false</itunes:explicit>
    <itunes:type>serial</itunes:type>
    <itunes:block>yes</itunes:block>
    <itunes:category text="Education"/>
    <itunes:image href="{BASE_URL}/cover.png"/>
    <image><url>{BASE_URL}/cover.png</url><title>{SHOW_TITLE}</title><link>{BASE_URL}/</link></image>
{chr(10).join(items)}
  </channel>
</rss>
"""
    with open(os.path.join(OUT, "feed.xml"), "w") as f:
        f.write(xml)
    links = "\n".join(
        f'<li><a href="audio/{ep["slug"]}.m4a">{escape(ep["title"])}</a></li>' for ep in EPISODES)
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(f"""<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{SHOW_TITLE}</title>
<body style="font:16px/1.5 system-ui;max-width:36em;margin:2em auto;padding:0 1em">
<h1>{SHOW_TITLE}</h1>
<p>Podcast feed: <a href="feed.xml">{BASE_URL}/feed.xml</a></p>
<p>In Overcast: + &rarr; Add URL &rarr; paste the feed address.</p>
<ol>{links}</ol></body>
""")
    print("feed written")


def scripts():
    lines = ["# Audio drill scripts (v1)", "",
             f"Voice: Kokoro `{VOICE}`, `lang=\"{LANG}\"`, speed {SPEED}. "
             "Item format: cue, ticking answer gap, answer plus one-line reason. "
             "Tags: [V] verified, [U] unverified. Sources point to deck cards (CX-/SG-/PS-), "
             "facts in the source log (F-xx) or earlier items (AU-xxx). AU IDs are immutable.", ""]
    for ep in EPISODES:
        lines += [f"## Episode {ep['title']}", ""]
        if ep["lesson"]:
            lines += ["**Lesson (spoken first):**", ""] + [f"- {x}" for x in ep["lesson"]] + [""]
        lines += ["| ID | Cue | Gap | Answer + reason | Source | Tag |", "|---|---|---|---|---|---|"]
        for aid, cue, pause, answer, src, tag in ep["items"]:
            lines.append(f"| {aid} | {cue} | {pause}s | {answer} | {src} | [{tag}] |")
        lines.append("")
    with open(os.path.join(HERE, "SCRIPTS.md"), "w") as f:
        f.write("\n".join(lines))
    print("SCRIPTS.md written")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "audio"
    if cmd == "audio":
        render([int(x) for x in sys.argv[2:]])
    elif cmd == "feed":
        feed()
    elif cmd == "scripts":
        scripts()
