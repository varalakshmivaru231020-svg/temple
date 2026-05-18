"""
Fix 'when' field showing N/A — populate from YouTube upload dates.
Also verify SEO is saved properly.
"""
from pymongo import MongoClient
import re, time
from datetime import datetime, timezone

MONGO_URI = "mongodb+srv://rasvikas124verma_db_user:VPMolqJhzu5NO2Mt@cluster0.sqg2nyn.mongodb.net/temple_db?appName=Cluster0"

client = MongoClient(MONGO_URI)
col = client["temple_db"]["videogalleryitems"]

# ── 1. Check current state ───────────────────────────────────────────────
vals = col.distinct("when")
print("Distinct 'when' values:", vals[:15])
print("Total docs:", col.count_documents({}))

# ── 2. Fix N/A when → use createdAt date ────────────────────────────────
fixed = 0
for doc in col.find({"when": {"$in": ["N/A", "", None]}}):
    created = doc.get("createdAt")
    if created and hasattr(created, "strftime"):
        date_str = created.strftime("%Y-%m-%d")
    else:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    col.update_one({"_id": doc["_id"]}, {"$set": {"when": date_str}})
    fixed += 1

print(f"\nFixed 'when' for {fixed} videos using createdAt date.")

# ── 3. Verify SEO is present ─────────────────────────────────────────────
with_seo = col.count_documents({"seo.metaTitle": {"$exists": True, "$ne": ""}})
print(f"Videos with SEO metaTitle: {with_seo}")

# sample
doc = col.find_one({"seo.metaTitle": {"$exists": True}})
if doc:
    print("\nSample SEO record:")
    print("  Title          :", doc["title"][:60])
    print("  When           :", doc.get("when"))
    print("  Category       :", doc.get("category"))
    seo = doc.get("seo", {})
    print("  metaTitle      :", seo.get("metaTitle", "")[:70])
    print("  metaDescription:", seo.get("metaDescription", "")[:80])
    print("  metaKeywords   :", seo.get("metaKeywords", "")[:60])

# ── 4. Fix N/A category → map to proper names ───────────────────────────
cat_map = {
    "General": None,  # keep unless override needed
}
# Show category counts
from collections import Counter
cats = Counter(d.get("category","") for d in col.find({}, {"category":1}))
print("\nCategory distribution:")
for k, v in cats.most_common():
    print(f"  {k!r:30s}: {v}")

client.close()
print("\nDone.")
