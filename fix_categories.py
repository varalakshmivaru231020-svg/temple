"""
Fetch real YouTube categories for videos still labelled 'General'.
"""
import yt_dlp
from pymongo import MongoClient
from datetime import datetime, timezone

MONGO_URI = "mongodb+srv://rasvikas124verma_db_user:VPMolqJhzu5NO2Mt@cluster0.sqg2nyn.mongodb.net/temple_db?appName=Cluster0"
SITE      = "Sri Surabharathi Foundation"
CHANNEL   = "Sri Surabharathi TV"

client = MongoClient(MONGO_URI)
col    = client["temple_db"]["videogalleryitems"]

general_docs = list(col.find({"category": {"$in": ["General", "Gaming"]}}))
print(f"Videos to re-categorise: {len(general_docs)}\n")

ydl_opts = {"quiet": True, "skip_download": True, "ignoreerrors": True}
updated = 0

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for i, doc in enumerate(general_docs, 1):
        url = doc.get("videoUrl", "")
        title = doc.get("title", "")
        try:
            info = ydl.extract_info(url, download=False)
            if not info:
                print(f"  [{i}/{len(general_docs)}] SKIP (no info): {title[:50]}")
                continue
            cats = info.get("categories", [])
            new_cat = cats[0] if cats else "General"

            # also update when if still missing
            upload_raw = info.get("upload_date", "")
            when_val   = doc.get("when", "")
            if upload_raw and len(upload_raw) == 8:
                when_val = f"{upload_raw[:4]}-{upload_raw[4:6]}-{upload_raw[6:]}"

            # rebuild SEO with corrected category
            meta_title = f"{title} | {SITE}"[:60]
            meta_desc  = (
                f"Watch '{title}' on {CHANNEL}. Category: {new_cat}. "
                f"Explore devotional and cultural programs from Sri Surabharathi Foundation."
            )[:160]
            keywords   = f"{title}, {new_cat}, {CHANNEL}, {SITE}, devotional, Sanskrit, temple"

            col.update_one({"_id": doc["_id"]}, {"$set": {
                "category":            new_cat,
                "when":                when_val,
                "seo.metaTitle":       meta_title,
                "seo.metaDescription": meta_desc,
                "seo.metaKeywords":    keywords,
                "seo.ogTitle":         title[:60],
                "seo.ogDescription":   meta_desc,
                "seo.twitterTitle":    title[:60],
                "seo.twitterDescription": meta_desc,
            }})
            print(f"  [{i}/{len(general_docs)}] {new_cat:20s}  when={when_val}  {title[:45]}")
            updated += 1
        except Exception as e:
            print(f"  [{i}/{len(general_docs)}] ERROR: {e}  {title[:40]}")

print(f"\nUpdated {updated} / {len(general_docs)} videos.")

# Final category summary
from collections import Counter
cats = Counter(d.get("category","") for d in col.find({}, {"category":1}))
print("\nFinal category distribution:")
for k, v in cats.most_common():
    print(f"  {k!r:30s}: {v}")

client.close()
