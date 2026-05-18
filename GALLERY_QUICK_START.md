# 📸 Gallery System - Quick Start

## ✅ What's Already Set Up

Your temple website has a complete gallery management system:

### Backend
- ✅ Gallery Item Model with category field
- ✅ Gallery Category Model
- ✅ API endpoints for CRUD operations
- ✅ Image upload & WebP conversion
- ✅ Public API for frontend

### Admin Panel
- ✅ `/admin/gallery` - Manage gallery images
- ✅ `/admin/galleryCategories` - Manage categories
- ✅ Bulk upload support (multiple images at once)
- ✅ Individual image management
- ✅ SEO settings for images
- ✅ Pin/unpin featured images

### Public Website
- ✅ `/gallery` - Full page gallery display
- ✅ Category filter buttons
- ✅ Image lightbox viewer
- ✅ Responsive grid layout
- ✅ Auto-sort by pinned status & date

---

## 🚀 Getting Started (4 Steps)

### Step 1: Create Categories
1. Go to: **Admin Dashboard** → **Gallery Categories**
2. Click **"+ Add New"** button
3. Enter category name: *Temple, Events, Rituals, etc.*
4. Click **Save**

### Step 2: Upload Images (Bulk - Recommended)
1. Go to: **Admin Dashboard** → **Gallery**
2. Click **"⬆️ Bulk Upload Images"** section
3. Select multiple image files
4. Choose category from dropdown
5. (Optional) Add title, pin images
6. Click **"⬆️ Upload"**

### Step 3: Verify Upload
1. Images appear in the gallery table
2. Check if marked as "Active"

### Step 3: View on Public Site
1. Visit: `/gallery` on your website
2. See images organized by category
3. Click category buttons to filter
4. Click image to open lightbox

---

## 📝 File Structure

```
temple_frontend/
├── src/
│   ├── app/
│   │   ├── (website)/gallery/page.js ← Public gallery page
│   │   └── admin/
│   │       ├── gallery/page.js ← Manage images
│   │       └── galleryCategories/page.js ← Manage categories
│   └── components/admin/
│       └── BulkGalleryUpload.js ← Bulk upload component

temple_backend/
├── models/
│   ├── GalleryItem.js ← Image data model
│   └── GalleryCategory.js ← Category model
└── routes/
    ├── admin.js ← Admin API endpoints
    └── public.js ← Public API endpoints
```

---

## 🔧 Admin API Endpoints

All endpoints require authentication with admin token.

### Gallery Items
- `GET /api/admin/gallery` - List all images
- `POST /api/admin/gallery` - Create new image
- `PUT /api/admin/gallery/:id` - Update image
- `DELETE /api/admin/gallery/:id` - Delete image

### Gallery Categories
- `GET /api/admin/galleryCategories` - List all categories
- `POST /api/admin/galleryCategories` - Create category
- `PUT /api/admin/galleryCategories/:id` - Update category
- `DELETE /api/admin/galleryCategories/:id` - Delete category

### Image Upload
- `POST /api/admin/upload` - Upload image file (returns filename)

---

## 🌐 Public API Endpoints

No authentication required. Cache revalidates every 60 seconds.

- `GET /api/public/gallery` - Get all active gallery items
- `GET /api/public/gallery-categories` - Get all active categories

---

## 💡 Pro Tips

✨ **Pinned Images**: Mark important photos to show them first  
🏷️ **Categories**: Organize images by event type  
🔍 **SEO**: Add meta titles & descriptions for search engines  
📱 **Responsive**: Images automatically adapt to screen size  
⚡ **Performance**: Images are converted to WebP for faster loading  

---

## ❓ FAQ

**Q: Can I bulk upload to multiple categories?**  
A: No, bulk upload applies same category to all images. Upload to different categories separately or use individual uploads.

**Q: How many images can I upload?**  
A: No strict limit, but recommended max 25MB per image and 100+ images per category.

**Q: Can I reorder images?**  
A: Yes, use the pin feature to control order. Pinned images show first.

**Q: Do images need SEO?**  
A: Optional, but recommended for search engine visibility.

**Q: What image formats are supported?**  
A: JPEG, PNG, WebP, GIF. Images are auto-converted to WebP.

---

## 📞 Support

If you need help:
1. Check GALLERY_GUIDE.md for detailed instructions
2. Review error messages in browser console
3. Ensure categories are created before uploading images
4. Verify images are marked as "Active"
