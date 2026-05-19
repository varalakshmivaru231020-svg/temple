# Nginx Configuration Update Required

## Issue
Banner images uploaded through the admin panel are not displaying on the frontend because nginx is not configured to serve the `/uploads/` directory.

## Current Status
- ✅ Backend Express.js server IS configured to serve uploads at `http://127.0.0.1:5001/uploads/`
- ✅ Images ARE being saved to disk correctly
- ✅ Database IS storing correct image filenames
- ❌ Nginx is NOT proxying `/uploads/` requests to the backend service
- ❌ Frontend gets 404 when requesting `/uploads/filename`

## Solution
Add the following location block to your nginx configuration for `srisurabharathi.com`:

### Option 1: Proxy to Backend (Recommended)
```nginx
location /uploads/ {
    proxy_pass http://127.0.0.1:5001/uploads/;
    proxy_cache off;
    proxy_buffering off;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

### Option 2: Direct File Serving (If uploads directory is in web root)
```nginx
location /uploads/ {
    alias /home/srisurabharathi/htdocs/srisurabharathi.com/temple_backend/uploads/;
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```

## What to Request from Hosting Provider

**Subject:** Nginx Configuration Update for /uploads/ Directory

**Message:**
```
Dear Support Team,

I need to update the nginx configuration for my domain srisurabharathi.com to proxy the /uploads/ directory to my backend application.

My setup:
- Domain: srisurabharathi.com
- Backend running on: http://127.0.0.1:5001
- Uploads stored at: /home/srisurabharathi/htdocs/srisurabharathi.com/temple_backend/uploads/

Please add this location block to the nginx configuration for srisurabharathi.com:

```
location /uploads/ {
    proxy_pass http://127.0.0.1:5001/uploads/;
    proxy_cache off;
    proxy_buffering off;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

Then reload nginx:
nginx -s reload

Thank you,
[Your Name]
```

## After Hosting Provider Updates Nginx

Once they confirm the change is complete, run these commands on your server:

```bash
# Verify nginx reload worked
curl -I https://srisurabharathi.com/uploads/

# If you see 200 or 301 (not 404), nginx is configured correctly

# Rebuild frontend to clear cache
cd ~/htdocs/srisurabharathi.com/temple_frontend
rm -rf .next
npm run build

# Restart frontend
pm2 restart frontend

# Test the page
curl https://srisurabharathi.com/facilities
```

## Testing
After the nginx configuration is updated:

1. **Test via curl:**
   ```bash
   curl -I https://srisurabharathi.com/uploads/
   # Should return 200 or 301, NOT 404
   ```

2. **Test in browser:**
   - Go to: https://srisurabharathi.com/admin/pageContent
   - Edit the "Facilities" page
   - Upload a banner image
   - Click Save
   - Visit: https://srisurabharathi.com/facilities
   - The banner image should now display at the top

3. **Test other pages:**
   - About page: https://srisurabharathi.com/about
   - Events page: https://srisurabharathi.com/events (if exists)
   - Any custom page with banner

## Files Referenced
- Backend: `temple_backend/server.js` (line 50)
- Frontend: `temple_frontend/src/app/(website)/page/[key]/page.js` (line 82)
- Database: Storing filenames in `pageContent.bannerImage` field

## Technical Details

**Why this is needed:**
- Frontend requests: `GET https://srisurabharathi.com/uploads/1779108753544-gopuram.webp`
- Nginx sees `/uploads/` and has no rule for it
- Without proxy rule, nginx returns 404
- With proxy rule, nginx forwards request to backend:5001
- Backend serves the file correctly

**Why not direct file serving:**
- Backend application applies image optimization (WebP conversion)
- Backend handles MIME types and caching headers
- Proxying ensures consistency with backend logic

## Contact Information
- Hosting Provider: Hostinger (based on srv1527708.hstgr.cloud)
- Support: Through Hostinger control panel

---

**Status:** ⏳ Awaiting hosting provider response
**Priority:** High - Required for gallery and page content images to display
