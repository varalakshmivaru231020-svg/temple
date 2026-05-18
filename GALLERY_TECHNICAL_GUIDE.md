# Gallery System - Technical Guide

## System Architecture

### Data Flow

```
Admin Panel (Upload)
    ↓
Image Upload API (/api/admin/upload)
    ↓
Image Processing (WebP Conversion)
    ↓
File Storage (/uploads/)
    ↓
Database (GalleryItem Document)
    ↓
Public API (/api/public/gallery)
    ↓
Frontend Gallery Page (/gallery)
    ↓
User Browser (Lightbox Viewer)
```

## Database Models

### GalleryItem
```javascript
{
  _id: ObjectId,
  title: String,
  category: String,        // Category name
  image: String,          // Filename or URL
  altText: String,
  isPinned: Boolean,
  isActive: Boolean,
  seo: {
    metaTitle: String,
    metaDescription: String,
    metaKeywords: String,
    canonicalUrl: String,
    ogTitle: String,
    ogDescription: String,
    ogImage: String,
    twitterTitle: String,
    twitterDescription: String,
    twitterImage: String,
    robotsIndex: Boolean
  },
  createdAt: Date,
  updatedAt: Date
}
```

### GalleryCategory
```javascript
{
  _id: ObjectId,
  name: String,           // Category name (unique)
  description: String,
  isActive: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

## API Endpoints

### Admin Endpoints (Require Authentication)

#### Get All Gallery Items
```
GET /api/admin/gallery?page=1&limit=10&fromDate=2024-01-01&toDate=2024-12-31
Response: {
  data: [GalleryItem, ...],
  pagination: { currentPage, totalPages, totalItems, itemsPerPage, hasNextPage, hasPrevPage }
}
```

#### Get Single Gallery Item
```
GET /api/admin/gallery/:id
Response: GalleryItem
```

#### Create Gallery Item
```
POST /api/admin/gallery
Body: {
  title?: String,
  category: String,
  image: String,
  altText?: String,
  isPinned?: Boolean,
  isActive?: Boolean,
  seo?: Object
}
Response: GalleryItem
```

#### Update Gallery Item
```
PUT /api/admin/gallery/:id
Body: Partial GalleryItem
Response: GalleryItem
```

#### Delete Gallery Item
```
DELETE /api/admin/gallery/:id
Response: { message: "Deleted successfully" }
```

#### Upload Image
```
POST /api/admin/upload
Body: FormData with 'image' field
Response: { filename: String }
```

#### Gallery Categories (Same pattern)
```
GET /api/admin/galleryCategories
POST /api/admin/galleryCategories
PUT /api/admin/galleryCategories/:id
DELETE /api/admin/galleryCategories/:id
```

### Public Endpoints (No Authentication)

#### Get All Gallery Items
```
GET /api/public/gallery
Response: [GalleryItem, ...]
- Only returns isActive: true items
- Sorted by isPinned DESC, createdAt DESC
```

#### Get Gallery Categories
```
GET /api/public/gallery-categories
Response: [GalleryCategory, ...]
- Only returns isActive: true items
- Sorted by name ASC
```

## Frontend Components

### GallerySection Component
**Location**: `temple_frontend/src/components/website/GallerySection.js`

**Props**:
```typescript
interface GallerySection {
  items: GalleryItem[];           // Gallery images
  categoryOptions?: Array;        // Category options
  hideExploreLink?: boolean;      // Hide "View All" link
  noTopPadding?: boolean;         // Remove top padding
  hideHeader?: boolean;           // Hide title section
  className?: string;             // CSS class
}
```

**Features**:
- Auto-generates category filter from items if not provided
- Filters items by selected category
- Lightbox viewer for images
- Responsive grid layout
- Sort by pinned status and date

### Image URL Resolution
```javascript
function getImageSrc(image) {
    if (!image) return null;
    if (/^https?:\/\//i.test(image)) return image;  // External URL
    if (image.startsWith('/images/')) return image;  // Static image
    
    // Uploaded image
    let cleanPath = image;
    if (cleanPath.startsWith('/')) cleanPath = cleanPath.slice(1);
    if (cleanPath.toLowerCase().startsWith('uploads/')) {
        cleanPath = cleanPath.slice(8);
    }
    return `${UPLOADS}/${cleanPath}`;
}
```

## Admin Components

### BulkGalleryUpload Component
**Location**: `temple_frontend/src/components/admin/BulkGalleryUpload.js`

**Features**:
- Select multiple image files
- Choose category
- Add optional title (applies to all)
- Pin all images option
- Upload progress tracking
- Error handling

**Props**:
```typescript
interface BulkGalleryUpload {
  categories: string[];           // Available categories
  onComplete?: () => void;        // Callback after upload
}
```

### DataTable Component
**Location**: `temple_frontend/src/components/admin/DataTable.js`

**Supports**:
- CRUD operations
- Search and filtering
- Pagination
- Date range filtering
- Image preview
- SEO editor
- Category selection

## Styling & Customization

### CSS Classes Used
- `.gallery-grid` - Main grid container
- `.g-item` - Gallery item card
- `.g-item.filtering` - Applied during filter
- `.g-cat` - Category label on image
- `.g-overlay` - Hover overlay
- `.lightbox` - Lightbox container
- `.lightbox-content` - Image in lightbox
- `.lightbox-caption` - Image caption
- `.filter-btn` - Category filter button
- `.filter-btn.active` - Active filter button

### Styling Points

Gallery Grid:
```css
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px;
  animation: fadeIn 0.6s ease-in;
}
```

Image Card:
```css
.g-item {
  position: relative;
  cursor: pointer;
  overflow: hidden;
  border-radius: 12px;
  aspect-ratio: 1;
}

.g-item:hover .g-overlay {
  opacity: 1;
}
```

## Configuration

### Environment Variables Needed
```
UPLOADS_URL=http://localhost:4000/uploads  # Backend upload URL
API_URL=http://localhost:4000              # Backend API URL
```

### Revalidation
Gallery data is cached with 60-second revalidation:
```javascript
fetch(url, { next: { revalidate: 60 } })
```

This means:
- Changes appear within 60 seconds on public site
- Reduces database load
- Improves page load speed

### Image Processing
Images are automatically converted to WebP format:
- Quality: 82%
- Effort: 4 (compression level)
- Max file size: 25MB

## Performance Optimization

### Image Optimization
1. **WebP Conversion**: Reduces file size by 25-35%
2. **Lazy Loading**: Images load as needed
3. **Responsive Images**: Different sizes for different devices
4. **Caching**: Public API cache revalidates every 60s

### Query Optimization
1. **Pagination**: Default 10 items per page
2. **Lean Queries**: Select only needed fields
3. **Sorting**: Indexed by isPinned and createdAt

### Frontend Optimization
1. **Component Memoization**: Prevent unnecessary re-renders
2. **Image Preloading**: Lightbox images preload
3. **Grid Animation**: CSS animation for smooth effects

## Security

### Image Upload Security
1. **File Type Validation**: Only image files allowed
2. **File Size Limit**: 25MB per file
3. **Name Sanitization**: Removes special characters
4. **Path Traversal Prevention**: Resolved paths validated

### API Security
1. **Authentication**: All admin endpoints require token
2. **Authorization**: Permission checks per resource
3. **Validation**: Input validation on all fields
4. **SQL Injection Prevention**: MongoDB prevents injection

## Troubleshooting

### Images Not Uploading
- Check file format (JPEG, PNG, WebP, GIF)
- Verify file size < 25MB
- Ensure category is selected
- Check browser console for errors

### Category Not Appearing
- Verify category is marked `isActive: true`
- Ensure images use exact category name
- Try page refresh (cache expires in 60s)

### Performance Issues
- Reduce number of images per page
- Optimize image sizes before upload
- Clear browser cache
- Check server logs for errors

## Future Enhancements

Possible additions:
1. Image cropping in admin
2. Drag-to-reorder functionality
3. Image tagging system
4. Advanced filters (date, size, etc.)
5. Image statistics dashboard
6. Batch download feature
7. Social media sharing
8. Comments/ratings

## Development Notes

### Adding New Fields
1. Update GalleryItem model
2. Add field to DataTable fields config
3. Update API response handling
4. Add to frontend display (if public)

### Changing Default Categories
Edit line 10 in `/admin/gallery/page.js`:
```javascript
const defaultCategories = ['Category1', 'Category2', ...];
```

### Custom Styling
Modify CSS in:
- `temple_frontend/src/styles/` - Global styles
- Component inline styles - Component-specific

## References

- **Next.js Documentation**: https://nextjs.org/
- **Express.js**: https://expressjs.com/
- **MongoDB**: https://www.mongodb.com/
- **Sharp (Image Processing)**: https://sharp.pixelplumbing.com/
