# DEPLOYMENT.md — Deployment Process

---

## Hosting Setup

| Component | Provider | Details |
|---|---|---|
| **Hosting** | GitHub Pages | Static site, free tier |
| **Repository** | `amirhashmilive/ijmeer` | https://github.com/amirhashmilive/ijmeer |
| **Branch** | `main` | GitHub Pages serves from main |
| **DNS** | Cloudflare (Free) | Proxy enabled |
| **Domain** | GoDaddy | `ijmeer.com` |
| **SSL** | Cloudflare Full (strict) | End-to-end HTTPS |
| **CDN** | Cloudflare | Auto-cached, purge via dashboard |

---

## URLs

| URL | Purpose |
|---|---|
| `https://www.ijmeer.com` | **Primary URL** (canonical) |
| `https://ijmeer.com` | Redirects to www (Cloudflare 301) |
| `https://amirhashmilive.github.io/ijmeer` | **Fallback URL** (GitHub Pages direct) |

---

## Deployment Steps

### Standard deployment (after any code change):

```powershell
# 1. Navigate to project
cd "D:\DRIVE (Ai) Agents\00 Projects\Workplace IJMEER"

# 2. Check status
git status

# 3. Stage changed files
git add [specific-files]
# Or stage everything:
git add .

# 4. Commit with proper format
git commit -m "[action]: [brief description]"

# 5. Push to main
git push origin HEAD:main

# 6. Wait 2-3 minutes for GitHub Pages to rebuild

# 7. Verify at https://www.ijmeer.com
```

### Verification after deploy:

1. Open `https://www.ijmeer.com` in a browser
2. Check the specific page(s) you changed
3. Hard refresh: `Ctrl+Shift+R` (clears browser cache)
4. If still seeing old version, wait 5 minutes (Cloudflare cache)
5. Check GitHub repo → Actions tab for build status (if available)

---

## CNAME Configuration

The file `/CNAME` in the repo root contains:
```
www.ijmeer.com
```

> ⚠️ **NEVER delete or modify the CNAME file** — this will break the custom domain.

---

## Cloudflare DNS Records

| Record | Type | Name | Value | Proxy |
|---|---|---|---|---|
| A | A | `ijmeer.com` | GitHub Pages IPs | Yes |
| CNAME | CNAME | `www` | `amirhashmilive.github.io` | Yes |

### Cloudflare Page Rules:

| Rule | Action |
|---|---|
| `http://ijmeer.com/*` | 301 redirect → `https://www.ijmeer.com/$1` |
| `http://www.ijmeer.com/*` | Always Use HTTPS |

---

## Cache Management

### Cloudflare cache purge (if changes don't appear):
1. Log into Cloudflare dashboard
2. Select `ijmeer.com` domain
3. Go to **Caching** → **Configuration**
4. Click **Purge Everything** (or purge specific URLs)
5. Wait 30 seconds, then reload

### Browser cache:
- `Ctrl+Shift+R` — hard refresh
- `Ctrl+Shift+Delete` → Clear cached images and files

---

## Rollback Procedure

If a deployment breaks the site:

```powershell
# Option 1: Revert the last commit
git revert HEAD
git push origin HEAD:main

# Option 2: Reset to a specific known-good commit
git log --oneline -10  # Find the good commit hash
git reset --hard [commit-hash]
git push origin HEAD:main --force

# Option 3: Restore from backup
# See BACKUP.md for restore instructions
```

> ⚠️ `--force` push rewrites history. Use only as last resort.

---

## Build & Errors

GitHub Pages does NOT run a build step for this project (pure static HTML). Common issues:

| Problem | Cause | Fix |
|---|---|---|
| 404 on custom domain | CNAME file missing or wrong | Verify `/CNAME` contains `www.ijmeer.com` |
| Mixed content warnings | HTTP resources on HTTPS page | Change all `http://` to `https://` |
| CSS not loading | Wrong relative path | Verify asset paths from page location |
| Changes not visible | Cloudflare cache | Purge cache, wait 2-3 minutes |
| Build failed | Invalid HTML syntax (rare) | Check GitHub Actions tab for errors |

---

## Analytics Verification

After deployment, verify analytics are working:

1. Open `https://www.ijmeer.com` in an incognito window
2. Check Google Tag Manager debug mode (GTM-NWHDPZRK)
3. Check GA4 Realtime report (G-2FNJ68WF8J)
4. Verify new pages fire pageview events

---

## Pre-Deployment Checklist

Before pushing any changes:

- [ ] All HTML is valid (no unclosed tags)
- [ ] All links work (no broken hrefs)
- [ ] Images have `alt` text
- [ ] CNAME file is intact
- [ ] No sensitive data in committed files
- [ ] Commit message follows format: `[action]: [description]`
- [ ] Changes tested locally (open HTML in browser)
