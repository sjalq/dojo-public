#!/usr/bin/env python3
"""
Purpose: Read Kyle Doops' technical-analysis charts from his videos via Gemini vision.
Dependencies: yt-dlp + ffmpeg on PATH. Gemini key read from the twolebot sqlite db.
              Uses only the Python stdlib (urllib, sqlite3) — no extra packages.

What it does, per (video_id, timestamps):
  1. Downloads the video once at low res (<=480p), cached under <workdir>/video/.
  2. Extracts one frame per requested timestamp with ffmpeg, cached under <workdir>/frames/.
  3. Sends each frame to Gemini with a chart-reading prompt and records the read.

Resumable: skips any frame whose Gemini read is already in the output json.

Usage:
  python chart-vision.py <jobs_file> <workdir> [--db PATH] [--model NAME] [--max-frames N]

jobs_file format (one job per line; blank lines and # comments ignored):
  <video_id> <ts1,ts2,ts3,...>      # timestamps as SECONDS or mm:ss / hh:mm:ss
  e.g.  9N7z0cJoC6Q 120,640,1180

Output:
  <workdir>/chart-reads.json   machine-readable, one entry per frame
  <workdir>/chart-reads.md     human-readable rollup
"""

import base64
import json
import os
import re
import sqlite3
import subprocess
import sys
import urllib.request

DEFAULT_DB = os.path.expanduser("~/git/twolebot/data/runtime.sqlite3")
DEFAULT_MODEL = "gemini-2.5-flash"  # cheap, vision-capable; ponytail: bump to 3-flash only if reads are weak

PROMPT = """You are reading a single frame from a crypto technical-analysis livestream by trader Kyle Doops.
The frame shows his charting screen. Extract ONLY what is visibly on the chart — do not invent levels.

Report as terse bullet lines:
- instrument + timeframe (e.g. BTCUSD 4H) if legible, else "unclear"
- price now (approx, if a last-price label is visible)
- horizontal levels he has drawn (support/resistance), with the price if legible
- trendlines / channels / patterns drawn (e.g. ascending triangle, range, wedge)
- indicators visible (EMAs, RSI, volume, fib, etc.) and what they're showing
- any annotation text / arrows / target or stop boxes on the chart
- the trade idea the chart implies: direction, entry zone, invalidation level, target(s)
If something is not visible, write "n/a" for that line rather than guessing."""


def get_key(db_path: str) -> str:
    con = sqlite3.connect(db_path)
    try:
        row = con.execute("SELECT value FROM runtime_secrets WHERE key='gemini_key'").fetchone()
    finally:
        con.close()
    if not row or not row[0]:
        sys.exit(f"gemini_key not found in {db_path}")
    return row[0].strip()


def to_seconds(ts: str) -> int:
    ts = ts.strip()
    if ":" not in ts:
        return int(float(ts))
    parts = [float(p) for p in ts.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    h, m, s = parts
    return int(h * 3600 + m * 60 + s)


def parse_jobs(path: str):
    jobs = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        vid, _, tslist = line.partition(" ")
        secs = [to_seconds(t) for t in tslist.split(",") if t.strip()]
        if vid and secs:
            jobs.append((vid.strip(), secs))
    return jobs


def get_frame(video_id: str, sec: int, frame_path: str, video_dir: str) -> bool:
    # MACHINE-SAFE: download only a ~4s section around the timestamp (<=480p),
    # NOT the whole livestream, then pull one frame. Sequential by caller.
    if os.path.exists(frame_path):
        return True
    os.makedirs(video_dir, exist_ok=True)
    clip = os.path.join(video_dir, f"{video_id}_{sec}.mp4")
    h, m, s = sec // 3600, (sec % 3600) // 60, sec % 60
    start = f"{h:02d}:{m:02d}:{s:02d}"
    e = sec + 4
    end = f"{e//3600:02d}:{(e%3600)//60:02d}:{e%60:02d}"
    try:
        subprocess.run(
            ["yt-dlp", "-f", "bv*[height<=480]/b[height<=480]/b",
             "--download-sections", f"*{start}-{end}",
             "--force-keyframes-at-cuts", "-o", clip,
             f"https://www.youtube.com/watch?v={video_id}"],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return False
    if not os.path.exists(clip):
        return False
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", clip, "-frames:v", "1", "-q:v", "3", frame_path],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    finally:
        try:
            os.remove(clip)  # don't accumulate disk
        except OSError:
            pass
    return os.path.exists(frame_path)


def read_chart(key: str, model: str, frame_path: str) -> str:
    with open(frame_path, "rb") as f:
        img = base64.b64encode(f.read()).decode()
    body = json.dumps({
        "contents": [{"parts": [
            {"text": PROMPT},
            {"inline_data": {"mime_type": "image/jpeg", "data": img}},
        ]}],
        "generationConfig": {"temperature": 0, "maxOutputTokens": 700},
    }).encode()
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
           f"{model}:generateContent?key={key}")
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.load(resp)
    return data["candidates"][0]["content"]["parts"][0]["text"].strip()


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    jobs_file, workdir = sys.argv[1], sys.argv[2]
    db = DEFAULT_DB
    model = DEFAULT_MODEL
    max_frames = 200
    a = sys.argv[3:]
    for i, tok in enumerate(a):
        if tok == "--db":
            db = a[i + 1]
        elif tok == "--model":
            model = a[i + 1]
        elif tok == "--max-frames":
            max_frames = int(a[i + 1])

    key = get_key(db)
    jobs = parse_jobs(jobs_file)
    video_dir = os.path.join(workdir, "video")
    frame_dir = os.path.join(workdir, "frames")
    os.makedirs(frame_dir, exist_ok=True)
    out_json = os.path.join(workdir, "chart-reads.json")
    results = json.load(open(out_json)) if os.path.exists(out_json) else {}

    planned = [(v, s) for v, secs in jobs for s in secs]
    if len(planned) > max_frames:
        print(f"WARNING: {len(planned)} frames requested, capping at {max_frames}")
        planned = planned[:max_frames]

    done = 0
    for video_id, sec in planned:
        fkey = f"{video_id}@{sec}"
        if fkey in results:
            continue
        fpath = os.path.join(frame_dir, f"{video_id}_{sec}.jpg")
        if not get_frame(video_id, sec, fpath, video_dir):
            results[fkey] = {"video_id": video_id, "sec": sec, "error": "frame fetch failed"}
            continue
        try:
            read = read_chart(key, model, fpath)
            results[fkey] = {"video_id": video_id, "sec": sec, "frame": fpath, "read": read}
            done += 1
            print(f"[{done}] {fkey} OK")
        except Exception as e:
            results[fkey] = {"video_id": video_id, "sec": sec, "frame": fpath, "error": str(e)[:200]}
            print(f"[!] {fkey} FAILED: {str(e)[:120]}")
        json.dump(results, open(out_json, "w"), indent=2, ensure_ascii=False)

    # markdown rollup
    with open(os.path.join(workdir, "chart-reads.md"), "w", encoding="utf-8") as f:
        f.write(f"# Kyle Doops chart reads ({model})\n\n")
        for fkey, r in results.items():
            f.write(f"## {fkey}\n\n")
            if "error" in r:
                f.write(f"_error: {r['error']}_\n\n")
            else:
                f.write(r["read"] + "\n\n")
    print(f"Done. {done} new reads, {len(results)} total -> {out_json}")


if __name__ == "__main__":
    main()
