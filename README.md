# DSA audio pattern drills

Screen-free spoken drills for coding-interview pattern recognition and time/space complexity. Each item is: a cue, a ticking gap to answer aloud, then the answer with a one-line reason.

- `content.py`: all episode text, item IDs (`AU-xxx`, immutable) and sources.
- `generate.py`: renders audio with Kokoro TTS (`bm_lewis`, `en-gb`), inserts the answer gaps with numpy, encodes m4a with ffmpeg, and writes the podcast feed.
- `SCRIPTS.md`, `SOURCES.md`, `DECK-DIFF.md`: readable scripts, the source log with [V]/[U] tags, and the diff against the draft deck.
- `docs/`: what GitHub Pages serves (`feed.xml`, `index.html`, `audio/*.m4a`).

## Rebuild

```bash
pip install kokoro-onnx soundfile numpy
mkdir models && cd models
curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.int8.onnx
curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
cd ..
python generate.py audio      # all episodes, or: python generate.py audio 2
python generate.py feed
python generate.py scripts
```

Set `BASE_URL` if the site is not at `https://akrthk93.github.io/dsa-audio-drills`.

## Subscribe

Feed: `https://akrthk93.github.io/dsa-audio-drills/feed.xml`

Overcast: **+** → **Add URL** → paste the feed address. Turn Smart Speed off for this show and keep 1x speed, so the answer gaps keep their full length.
