# Views + top comments by engagement (likes + 3x replies) for a YouTube video, via the YouTube Data API.
# Usage: python3 tools/yt_comments.py VIDEO_ID [--n 15] [--pages 2]   (1 quota unit per page; 10,000/day)
import argparse, json, os, sys, urllib.parse, urllib.request
sys.path.insert(0, os.path.dirname(__file__)); import _env; _env.load()

def get(ep, **p):
    p["key"] = os.environ["YOUTUBE_API_KEY"]
    return json.load(urllib.request.urlopen(
        f"https://www.googleapis.com/youtube/v3/{ep}?" + urllib.parse.urlencode(p), timeout=30))

def video(vid):
    return get("videos", part="snippet,statistics,contentDetails", id=vid)["items"][0]

def top_comments(vid, pages=2, n=15):
    out, tok = [], None
    for _ in range(pages):
        kw = dict(part="snippet", videoId=vid, order="relevance", maxResults=100, textFormat="plainText")
        if tok: kw["pageToken"] = tok
        d = get("commentThreads", **kw)
        for it in d["items"]:
            s = it["snippet"]["topLevelComment"]["snippet"]
            out.append(dict(likes=s["likeCount"], replies=it["snippet"]["totalReplyCount"], text=s["textDisplay"]))
        tok = d.get("nextPageToken")
        if not tok: break
    out.sort(key=lambda c: c["likes"] + 3 * c["replies"], reverse=True)
    return out[:n]

if __name__ == "__main__":
    a = argparse.ArgumentParser(); a.add_argument("vid"); a.add_argument("--n", type=int, default=15)
    a.add_argument("--pages", type=int, default=2); o = a.parse_args()
    v = video(o.vid); st = v["statistics"]
    print(f'{v["snippet"]["title"]} | {int(st["viewCount"]):,} views | {st.get("commentCount")} comments')
    for c in top_comments(o.vid, o.pages, o.n):
        print(f'{c["likes"]:>7,} likes {c["replies"]:>4} replies | {c["text"][:240]}')
