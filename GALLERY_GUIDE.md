# Gallery System Guide

## Overview
The gallery system allows you to upload images from the admin panel and display them on the public website with category-based filtering.

## How to Use

### 1. **Create Gallery Categories** (Admin Panel)
   - Go to: `/admin/galleryCategories`
   - Click **"Add New"** button
   - Fill in:
     - **Category Name**: e.g., "Temple", "Events", "Rituals", "Puja", "Festival", etc.
     - **Description**: Brief description of the category
     - **Is Active**: Enable/disable the category
   - Click **Save**

### 2. **Upload Gallery Images** (Admin Panel)
   - Go to: `/admin/gallery`
   - Two options:

   **Option A: Bulk Upload Images**
   - Click on **"⬆️ Bulk Upload Images"** section to expand
   - Select multiple image files
   - Choose a **Category** from dropdown
   - Add an optional **Title** (applies to all images)
   - Check **"📌 Pin all to top"** if needed
   - Click **"⬆️ Upload"**

   **Option B: Add Individual Images**
   - Click **"+ Add New"** button in the DataTable
   - Fill in:
     - **Title**: Name of the image (optional)
     - **Category**: Select from dropdown
     - **Image**: Upload the image file (required)
     - **Alt Text**: Accessibility text
     - **Pin to Top**: Checkbox to pin important images
     - **Active**: Enable/disable visibility
     - **SEO Settings**: Add meta tags for search engines
   - Click **Save**

### 3. **Manage Gallery Images**
   - View all gallery images in the table
   - **Edit**: Click an image to modify
   - **Delete**: Remove images
   - **View**: Preview image details
   - **Search/Filter**: Use search bar to find images

## Frontend Display

### Gallery Page (`/gallery`)
- Displays all active gallery images
- Shows **Category Filter Buttons** at the top
- Click category to filter images
- Click "All" to show all images
- Click image to open lightbox view
- Images are sorted by:
  1. Pinned status (pinned items first)
  2. Creation date (newest first)

## Features

✅ **Bulk Upload**: Upload multiple images at once  
✅ **Category Filtering**: Organize images by categories  
✅ **Pin Important Images**: Keep featured images at the top  
✅ **SEO Optimization**: Add meta tags for search engines  
✅ **Image Preview**: Quick preview in admin panel  
✅ **Responsive Design**: Works on mobile and desktop  
✅ **Lightbox View**: Beautiful image viewer on public site

## Image Categories (Examples)
- Temple
- Events
- Rituals
- Puja
- Festival
- Cultural Program
- Yagam
- Lecture
- Workshop

## Best Practices

1. **Use Descriptive Titles**: Help visitors understand what they're viewing
2. **Add Alt Text**: Important for accessibility and SEO
3. **Optimize Images**: Use compressed images (under 2MB recommended)
4. **Organize by Category**: Create meaningful categories
5. **Pin Featured Images**: Show off your best photos
6. **Keep Descriptions**: Use SEO fields for search visibility

## Troubleshooting

**Images not showing in gallery?**
- Check if image is marked as "Active" ✓
- Verify the category is created and assigned
- Try refreshing the page

**Can't select category in bulk upload?**
- Create categories first in `/admin/galleryCategories`
- Wait for page to load categories from API
- Try refreshing the page

**Images appearing in wrong order?**
- Pinned images should appear first
- Newer images appear before older ones
- Edit images to change pin status if needed

## File Locations
- **Admin Gallery Page**: `/admin/gallery`
- **Admin Categories Page**: `/admin/galleryCategories`
- **Public Gallery Page**: `/gallery`
- **Component**: `temple_frontend/src/components/website/GallerySection.js`
- **Backend Routes**: `temple_backend/routes/admin.js` & `temple_backend/routes/public.js`
