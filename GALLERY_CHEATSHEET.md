# 📸 Gallery System - Cheat Sheet

## Admin URLs

| Action | URL |
|--------|-----|
| Manage Images | `/admin/gallery` |
| Manage Categories | `/admin/galleryCategories` |
| View Public Gallery | `/gallery` |

---

## Admin Panel Workflow

### 1️⃣ Create Category
```
/admin/galleryCategories
→ "+ Add New"
→ Enter name & description
→ Save
```

### 2️⃣ Bulk Upload Images
```
/admin/gallery
→ Expand "⬆️ Bulk Upload Images"
→ Select files
→ Choose category
→ Upload
```

### 3️⃣ Or Add Individual Image
```
/admin/gallery
→ "+ Add New"
→ Fill title, category, image
→ Save
```

### 4️⃣ View Public Gallery
```
/gallery
→ See all images with category filters
→ Click category to filter
→ Click image for lightbox
```

---

## Image Form Fields

| Field | Required | Notes |
|-------|----------|-------|
| Title | ✗ | Optional name/description |
| Category | ✓ | Must select from dropdown |
| Image | ✓ | JPG, PNG, WebP, GIF |
| Alt Text | ✗ | For accessibility |
| Pin | ✗ | Shows image first |
| Active | ✓ | Enable to show publicly |
| SEO | ✗ | For search engines |

---

## Category Management

| Action | How |
|--------|-----|
| Create | `/admin/galleryCategories` → "+ Add New" |
| Edit | `/admin/galleryCategories` → Click row → Edit |
| Delete | `/admin/galleryCategories` → Click row → Delete |
| View Images | `/admin/gallery` → Filter by category |

---

## Frontend Gallery Features

| Feature | How It Works |
|---------|--------------|
| Filter | Click category button |
| View All | Click "All" button |
| Lightbox | Click any image |
| Close | Click X or outside image |
| Responsive | Auto-adjusts to screen size |

---

## Keyboard Shortcuts (Frontend)

| Key | Action |
|-----|--------|
| Click Image | Open lightbox |
| Click X | Close lightbox |
| Click Outside | Close lightbox |
| Esc | Close lightbox |

---

## API Endpoints

### Admin (Auth Required)
```
GET    /api/admin/gallery
POST   /api/admin/gallery
PUT    /api/admin/gallery/:id
DELETE /api/admin/gallery/:id

GET    /api/admin/galleryCategories
POST   /api/admin/galleryCategories
PUT    /api/admin/galleryCategories/:id
DELETE /api/admin/galleryCategories/:id

POST   /api/admin/upload          (Image upload)
```

### Public (No Auth)
```
GET /api/public/gallery
GET /api/public/gallery-categories
```

---

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| Category dropdown empty | Create categories first at `/admin/galleryCategories` |
| Images not showing | Mark images as "Active" ✓ |
| Upload fails | Check file size < 25MB & format (JPG, PNG, etc.) |
| Cache not updating | Wait 60s or hard-refresh (Ctrl+Shift+R) |
| Category not filtering | Ensure exact category name match |

---

## File Size Limits

| Item | Limit |
|------|-------|
| Per Image | 25 MB |
| Format | JPG, PNG, WebP, GIF |
| Auto Convert | WebP (quality 82) |

---

## Performance Tips

✅ **Do This:**
- Upload optimized images
- Use meaningful category names
- Pin only important images
- Add SEO descriptions

❌ **Avoid This:**
- Uploading 1000+ images at once
- Very large file sizes (> 10MB)
- Too many categories
- Leaving images inactive

---

## Category Ideas

**By Location:**
- Temple Interior
- Temple Exterior
- Altar Area
- Entrance

**By Event:**
- Festivals
- Pujas
- Weddings
- Classes

**By Activity:**
- Rituals
- Prayers
- Celebrations
- Community Service

**By Time:**
- 2024
- 2023
- Recent Events
- Archive

---

## Database Fields

### GalleryItem
```
• title (optional)
• category (required)
• image (required)
• altText (optional)
• isPinned (default: false)
• isActive (default: true)
• seo (optional)
```

### GalleryCategory
```
• name (required, unique)
• description (optional)
• isActive (default: true)
```

---

## Column Display (Admin Table)

| Column | Shows |
|--------|-------|
| Title | Image name |
| Category | Category name |
| Image | Thumbnail |
| Pinned | Pin status (📌) |
| Active | Visibility status |
| Actions | Edit, Delete, View |

---

## Sort Order

Images appear in this order on `/gallery`:

1. **Pinned images first** (isPinned: true)
2. **By date (newest first)** (createdAt DESC)
3. **Only active** (isActive: true)

---

## Category Filter Behavior

- **"All"** → Shows all images
- **"Category Name"** → Shows only that category
- **No categories?** → Auto-discovers from image data
- **New category?** → Shows after page refresh (60s cache)

---

## SEO Fields (Optional)

- Meta Title
- Meta Description
- Meta Keywords
- Canonical URL
- OG Title/Description/Image
- Twitter Title/Description/Image
- Robots Index (yes/no)

---

## Troubleshooting Steps

1. **Check browser console** → F12 → Console tab
2. **Check server logs** → Backend terminal
3. **Clear cache** → Ctrl+Shift+R
4. **Verify category exists** → `/admin/galleryCategories`
5. **Verify image marked Active** → `/admin/gallery`
6. **Wait for cache** → 60 seconds if just uploaded

---

## Quick Links

📖 Read: `GALLERY_QUICK_START.md`  
📚 Learn: `GALLERY_GUIDE.md`  
🔧 Dev: `GALLERY_TECHNICAL_GUIDE.md`  
✅ Info: `GALLERY_SETUP_COMPLETE.md`

---

## Key Stats

- Categories: 9 default (customizable)
- Upload Limit: 25MB per file
- Cache: 60 seconds
- Quality: WebP 82% compression
- Grid: 250px minimum width
- Animation: 0.6s fade-in

---

## One-Minute Setup

```
1. Go to /admin/galleryCategories
2. Click "+ Add New"
3. Type "Temple" and Save
4. Go to /admin/gallery
5. Click "⬆️ Bulk Upload Images"
6. Select images, choose category, Upload
7. Visit /gallery to see live!
```

---

**That's it! You're ready to go!** 🎉
