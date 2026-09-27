# Gemini watches a YouTube URL window directly (no download). Reliable for the SAFE layer (foot, finish,
# placement, scorebug, commentary). NOT reliable for counts or camera cuts: on Son v Burnley (27 Sep) it
# reported 21 "CERTAIN" touches and invented 1-second cuts. Treat output as a first watch, never a verdict.
# Usage: python3 tools/gem_watch.py URL "prompt" --start 160 --end 199 --fps 5 [--model M] [--high]
import argparse, json, os, sys, time, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(__file__)); import _env; _env.load()

def watch(url, prompt, start=None, end=None, fps=None, model="gemini-3-flash-preview", high=False):
    vm = {}
    if start is not None: vm["startOffset"] = f"{start}s"
    if end is not None: vm["endOffset"] = f"{end}s"
    if fps: vm["fps"] = fps
    part = {"fileData": {"fileUri": url, "mimeType": "video/*"}}
    if vm: part["videoMetadata"] = vm
    cfg = {"temperature": 0}
    if high: cfg["mediaResolution"] = "MEDIA_RESOLUTION_HIGH"
    body = {"contents": [{"parts": [part, {"text": prompt}]}], "generationConfig": cfg}
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
    t = time.time()
    try:
        d = json.load(urllib.request.urlopen(req, timeout=600))
    except urllib.error.HTTPError as e:
        return f"HTTP {e.code}: {e.read()[:400].decode()}", {}
    txt = "".join(p.get("text", "") for p in d["candidates"][0]["content"]["parts"])
    u = d.get("usageMetadata", {}); u["secs"] = round(time.time() - t)
    return txt, u

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("url"); a.add_argument("prompt")
    a.add_argument("--start", type=float); a.add_argument("--end", type=float); a.add_argument("--fps", type=float)
    a.add_argument("--model", default="gemini-3-flash-preview"); a.add_argument("--high", action="store_true")
    o = a.parse_args()
    txt, u = watch(o.url, o.prompt, o.start, o.end, o.fps, o.model, o.high)
    print(txt); print("USAGE", json.dumps(u))
