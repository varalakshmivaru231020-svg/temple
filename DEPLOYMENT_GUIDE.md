# 🚀 Deployment Guide - Gallery System to Production

## What Was Committed

✅ **Commit**: `e023667` - Frontend submodule update with gallery enhancements
✅ **Changes**: 
- Gallery admin page with category analytics
- Full CRUD for gallery categories
- Optional title in bulk upload
- 42 sample gallery images

---

## 📋 Pre-Deployment Checklist

Before pushing to production, verify:

- [ ] All code is committed
- [ ] No uncommitted changes (`git status` shows clean)
- [ ] Frontend builds without errors
- [ ] Backend is running and accessible
- [ ] Database connection working
- [ ] Upload directory has write permissions
- [ ] SSL certificate valid (if HTTPS)

---

## 🔄 Deployment Steps

### Step 1: Verify All Changes Are Committed

```bash
cd c:\Users\varalakshmi\Desktop\Surabharathi Temple
git status
```

**Expected output**: `nothing to commit, working tree clean`

If not clean, commit remaining changes:
```bash
git add .
git commit -m "your message here"
```

### Step 2: Push to Remote Repository

```bash
git push origin main
```

This pushes:
- Frontend submodule changes (gallery enhancements)
- Updated submodule reference

### Step 3: Deploy Frontend

On your production server:

```bash
# Navigate to frontend directory
cd temple_frontend

# Pull latest changes
git pull origin main

# Install dependencies (if needed)
npm install

# Build the project
npm run build

# Restart the application
# (depends on your hosting - see section below)
```

### Step 4: Deploy Backend (If Needed)

```bash
# Navigate to backend directory
cd temple_backend

# Pull latest changes (if any)
git pull origin main

# Install dependencies (if needed)
npm install

# Restart the server
# (depends on your hosting - see section below)
```

### Step 5: Verify Deployment

1. **Check Frontend**: Visit `https://yoursite.com/admin/gallery`
2. **Check Admin**: Can you see Category Analytics?
3. **Check Categories**: Visit `/admin/galleryCategories` - can you create/edit/delete?
4. **Check Public**: Visit `/gallery` - do images display correctly?
5. **Test Upload**: Try uploading an image

---

## 🏠 Hosting-Specific Instructions

### If Hosted on Vercel (Next.js)

```bash
# Vercel automatically deploys on push to main branch
git push origin main
# Deployment happens automatically in 1-2 minutes
# Check: https://vercel.com/dashboard/projects
```

### If Hosted on AWS/DigitalOcean/Custom VPS

```bash
# SSH into your server
ssh your-user@your-server.com

# Navigate to project
cd /path/to/temple-website

# Pull latest code
git pull origin main

# Update submodules
git submodule update --init --recursive

# Frontend
cd temple_frontend
npm install
npm run build

# If using PM2 or systemd, restart service
pm2 restart temple_frontend
# or
systemctl restart temple-frontend
```

### If Using Docker

```bash
# Build and push Docker image
docker build -t your-registry/temple-frontend:latest .
docker push your-registry/temple-frontend:latest

# On production server, pull and restart
docker pull your-registry/temple-frontend:latest
docker-compose up -d frontend
```

### If Using GitHub Actions/CI-CD

```bash
# Simply push to main branch
git push origin main

# GitHub Actions automatically:
# 1. Runs tests
# 2. Builds the project
# 3. Deploys to production
# 4. Notifies on completion

# Check Actions tab on GitHub for status
```

---

## 📊 What Changed (Detailed)

### Frontend Changes:

1. **Gallery Admin Page** (`src/app/admin/gallery/page.js`)
   - Added category analytics dashboard
   - Shows image count per category
   - Visual grid display
   - Auto-updates when images uploaded

2. **Gallery Categories Page** (`src/app/admin/galleryCategories/page.js`)
   - Changed from read-only to full CRUD
   - Now can create categories ✅
   - Now can edit categories ✅
   - Now can delete categories ✅

3. **Bulk Upload Component** (`src/components/admin/BulkGalleryUpload.js`)
   - Made title field optional (was required)
   - Better UX for optional fields
   - Cleaner validation

4. **Gallery Images** (`public/Gallary/`)
   - Added 42 sample images
   - Ready for demonstration

### Backend Changes:
- ✅ **No changes needed** - Backend API already supports all operations

---

## 🔍 Testing After Deployment

### Admin Panel Tests

1. **Category Management**
   ```
   Go to: /admin/galleryCategories
   ✓ Click "+ Add New"
   ✓ Create a test category
   ✓ Edit the category
   ✓ Delete the category
   ```

2. **Gallery Management**
   ```
   Go to: /admin/gallery
   ✓ See category analytics at top
   ✓ View image counts per category
   ✓ Click "⬆️ Bulk Upload Images"
   ✓ Upload test image
   ✓ Verify image appears in table
   ✓ Edit image details
   ✓ Delete test image
   ```

3. **API Tests**
   ```
   GET /api/admin/gallery → Returns images with pagination
   GET /api/admin/galleryCategories → Returns all categories
   POST /api/admin/gallery → Creates new image
   POST /api/admin/galleryCategories → Creates new category
   ```

### Public Site Tests

1. **Gallery Page**
   ```
   Go to: /gallery
   ✓ See all images
   ✓ Category filter buttons appear
   ✓ Click category to filter
   ✓ Click image to open lightbox
   ✓ Close lightbox
   ```

2. **API Tests**
   ```
   GET /api/public/gallery → Returns active images
   GET /api/public/gallery-categories → Returns active categories
   ```

---

## 🆘 Troubleshooting Deployment

### Issue: Build Fails

```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
npm run build
```

### Issue: Images Not Showing

1. Check upload directory permissions:
   ```bash
   ls -la /path/to/uploads
   chmod 755 /path/to/uploads
   ```

2. Verify image path in API response

3. Check backend is serving uploads correctly

### Issue: Database Errors

```bash
# Verify MongoDB is running
mongosh

# Check connection string in .env
cat .env | grep MONGO

# Restart MongoDB
systemctl restart mongod
```

### Issue: Category Not Appearing in Dropdown

1. Verify category is created in database:
   ```bash
   mongosh
   > use temple
   > db.gallerycategories.find()
   ```

2. Clear browser cache (Ctrl+Shift+R)

3. Wait for API cache to refresh (60 seconds)

### Issue: Upload Failing

1. Check disk space:
   ```bash
   df -h
   ```

2. Check folder permissions:
   ```bash
   chmod 755 temple_backend/uploads
   ```

3. Check file size < 25MB

---

## 📈 Performance Tips for Production

1. **Enable Caching**
   - Set Cache-Control headers
   - Use CDN for images
   - Set revalidation: 60 seconds (already configured)

2. **Optimize Images**
   - WebP conversion (automatic)
   - Compression at 82% quality (already configured)
   - Lazy loading (automatic)

3. **Database Optimization**
   - Create index on `category` field
   - Create index on `isActive` field
   - Create index on `createdAt` field

4. **Monitor Performance**
   - Check API response times
   - Monitor database query times
   - Track upload success rates

---

## 📊 Monitoring

### Key Metrics to Monitor

- API response time: Should be < 200ms
- Upload success rate: Should be > 99%
- Database query time: Should be < 100ms
- Disk space usage: Should not exceed 80%
- Error rate: Should be near 0%

### Log Locations

```
Frontend logs: /var/log/temple-frontend/
Backend logs: /var/log/temple-backend/
Upload errors: temple_backend/logs/
```

---

## 🔄 Rollback Plan

If deployment goes wrong:

### Rollback Frontend

```bash
# Check previous commits
git log --oneline -5

# Revert to previous version
git revert HEAD

# Or reset to previous commit
git reset --hard 9b730a0

# Redeploy
npm run build
# Restart service
```

### Rollback to Previous Submodule Version

```bash
# In parent repository
git reset --hard 9b730a0
git submodule update --init --recursive
```

---

## ✅ Post-Deployment Checklist

After deploying to production:

- [ ] Gallery admin page loads without errors
- [ ] Category analytics dashboard displays
- [ ] Can create new category
- [ ] Can edit existing category
- [ ] Can delete category
- [ ] Can upload image successfully
- [ ] Image appears in public gallery
- [ ] Category filter works
- [ ] Lightbox viewer opens images
- [ ] SEO fields are editable
- [ ] No console errors (F12)
- [ ] Database queries are fast
- [ ] Uploads process correctly

---

## 📞 Support & Help

If you encounter issues:

1. Check browser console: **F12** → Console tab
2. Check server logs: Backend terminal
3. Check database: MongoDB shell
4. Review error messages carefully
5. Refer to documentation files

---

## 🎯 Summary

**What was deployed:**
- ✅ Gallery admin enhancements
- ✅ Category management (full CRUD)
- ✅ Category analytics dashboard
- ✅ 42 sample gallery images

**Deployment time:** ~5-15 minutes
**Downtime:** ~1-2 minutes (if using service restart)
**Rollback time:** ~5 minutes

---

## 📝 Next Steps

1. ✅ Verify deployment successful
2. ✅ Test all gallery features
3. ✅ Create some gallery categories
4. ✅ Upload images via bulk upload
5. ✅ Check public gallery at `/gallery`
6. ✅ Share link with users

**Congratulations! Gallery system is now live!** 🎉
