"""
Run this on the SERVER to re-download YouTube thumbnails
using the exact filenames already stored in MongoDB.

Usage:  python3 restore_thumbnails.py
"""
import os, re, urllib.request
from pymongo import MongoClient

MONGO_URI   = "mongodb+srv://rasvikas124verma_db_user:VPMolqJhzu5NO2Mt@cluster0.sqg2nyn.mongodb.net/temple_db?appName=Cluster0"
UPLOADS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")

os.makedirs(UPLOADS_DIR, exist_ok=True)

def extract_video_id(url):
    m = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url or "")
    return m.group(1) if m else None

def download_thumbnail(video_id, dest_path):
    for quality in ("maxresdefault", "hqdefault", "mqdefault"):
        url = f"https://img.youtube.com/vi/{video_id}/{quality}.jpg"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as r:
                data = r.read()
            if len(data) > 5000:
                with open(dest_path, "wb") as f:
                    f.write(data)
                return True
        except Exception:
            pass
    return False

client = MongoClient(MONGO_URI)
col    = client["temple_db"]["videogalleryitems"]

docs = list(col.find({"thumbnail": {"$nin": ["", None]}, "videoUrl": {"$regex": "youtube"}},
                     {"thumbnail": 1, "videoUrl": 1, "title": 1}))
print(f"Videos with thumbnails to restore: {len(docs)}\n")

ok = skip = fail = 0
for i, doc in enumerate(docs, 1):
    thumb    = doc.get("thumbnail", "")
    dest     = os.path.join(UPLOADS_DIR, thumb)
    title    = doc.get("title", "")[:50]
    video_id = extract_video_id(doc.get("videoUrl", ""))

    if os.path.exists(dest):
        print(f"  [{i}/{len(docs)}] SKIP (exists): {title}")
        skip += 1
        continue

    if not video_id:
        print(f"  [{i}/{len(docs)}] NO ID       : {title}")
        fail += 1
        continue

    success = download_thumbnail(video_id, dest)
    if success:
        print(f"  [{i}/{len(docs)}] OK          : {title}")
        ok += 1
    else:
        print(f"  [{i}/{len(docs)}] FAILED      : {title}")
        fail += 1

client.close()
print(f"\nDone — Downloaded: {ok}  Skipped: {skip}  Failed: {fail}")
print(f"Thumbnails saved to: {UPLOADS_DIR}")
