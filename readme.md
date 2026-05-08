# IJMEER Website

---

## ⚠️ CRITICAL: Backup Rule — READ BEFORE ANY ACTION

> **This project has automated backup enforcement. You MUST create a backup before making any changes.**

### For Humans and AI Agents — Non-Negotiable Rules

1. **Always start a work session using the wrapper script:**
   ```powershell
   .\start-session.ps1 -SessionDescription "brief-task-description"
   ```
   This creates a verified backup ZIP and then opens VS Code. **Do not open the project any other way.**

2. **Git commits are blocked** if no backup ZIP exists in `C:\Users\hashm\Desktop\Projects\backup\IJ` within the last 12 hours (enforced by `.git/hooks/pre-commit`).

3. **AI Agents:** Before executing any file-modifying task, your FIRST action must be:
   ```powershell
   .\backup.ps1 -CommitMessage "PRE-SESSION-<task-name>"
   ```
   Do not write, rename, or delete any file until this command succeeds.

### Quick Reference

| Action | Command |
|--------|---------|
| Start a session | `.\start-session.ps1 -SessionDescription "task-name"` |
| Manual backup only | `.\backup.ps1 -CommitMessage "your message"` |
| Restore from backup | Extract ZIP from `..\backup\IJ\` into this directory |

---

## International Journal of Multidisciplinary Explication and Emerging Research

A world-class, production-ready academic journal website built with pure HTML, CSS, and JavaScript.

### Features

- ✅ **Automatic Quarterly Timeline** - All deadlines calculated client-side, no manual updates ever needed
- ✅ **Premium Academic Design** - Nature/Elsevier/Science level quality
- ✅ **Fully Responsive** - Mobile-first approach
- ✅ **Fast Loading** - Static site, optimized for Lighthouse 90+
- ✅ **All 25+ Pages** - Complete navigation structure
- ✅ **DOAJ Integration** - Search widget included
- ✅ **Citation Management** - APA, MLA, Chicago formats with copy functionality
- ✅ **Google Analytics & Tag Manager** - Integrated on all pages
- ✅ **Social Media Links** - All active profiles linked
- ✅ **Tiered Pricing** - ₹2,000–₹5,000 / $50
- ✅ **Dynamic Rotating Announcement Banner** - Swiper.js integration
- ✅ **Ministry–SDG Integrated CfP Framework**

### Deployment

#### GitHub Pages (Recommended)

1. Fork or clone this repository
2. Go to repository Settings → Pages
3. Select "main" branch and "/ (root)" folder
4. Click Save
5. Your site will be live at `https://yourusername.github.io/ijmeer/`

#### Traditional Hosting

Upload all files to your web server's public_html or www directory.

### Updating Content

#### Adding New Papers (papers.json)

Edit `data/papers.json`:

```json
{
  "id": 16,
  "title": "Your Paper Title",
  "authors": ["Author Name 1", "Author Name 2"],
  "year": 2025,
  "volume": 1,
  "issue": 3,
  "subject": "Physics",
  "citation_count": 0,
  "pdf_url": "#",
  "abstract": "Paper abstract here..."
}
```

#### Adding New Issues (issues.json)

Edit `data/issues.json`:

```json
{
  "id": 5,
  "volume": 2,
  "issue": 1,
  "quarter": "Jan-Mar",
  "year": 2025,
  "title": "Volume 2, Issue 1",
  "theme": "Theme for this issue",
  "description": "Issue description",
  "publication_date": "2025-04-25",
  "status": "published",
  "papers": [16, 17, 18]
}
```

### Quarterly Timeline (Automatic)

| Quarter | Deadline | Publication |
|---------|----------|-------------|
| Jan-Mar | March 15 | April 25-30 |
| Apr-Jun | June 15 | July 25-31 |
| Jul-Sep | September 15 | October 25-31 |
| Oct-Dec | December 15 | January 25-31 |

The website automatically:
- Shows current submission status (Open/Late/Closed)
- Displays countdown to deadline
- Applies late fee warning after deadline
- Updates all dates based on server date

### File Structure

```
ijmeer/
├── index.html
├── about.html
├── editorial-board.html
├── most-cited.html
├── contact.html
├── archive.html
├── authors.html
├── peer-review.html
├── publishing-ethics.html
├── privacy-policy.html
├── call-for-papers.html
├── library.html
├── editorial-portfolio.html
├── open-access.html
├── data/
│   ├── papers.json
│   ├── issues.json
│   └── config.json
├── assets/
│   ├── css/
│   │   └── main.css
│   └── js/
│       └── main.js
└── README.md
```

### Backup System

A comprehensive backup system is in place to preserve the project state.

#### Creating a Backup

To create a full backup of the project, run the `backup.ps1` PowerShell script:

```powershell
.\backup.ps1 -CommitMessage "your message describing changes"
```

This will create a timestamped zip file in the `C:\Users\hashm\Desktop\Projects\backup\IJ` directory, capturing all project files (HTML, CSS, JS, JSON, assets, and configurations).

#### Restoring from Backup

1. Navigate to the backup directory: `C:\Users\hashm\Desktop\Projects\backup\IJ`
2. Locate the desired backup file (e.g., `2026-05-08_1430_Added-new-papers.zip`).
3. Extract the contents of the zip file.
4. Replace the contents of the `Workplace IJMEER` directory with the extracted files.

#### Automated Backups (Enforced)

Two enforcement mechanisms are active:

**Option A — Session Wrapper (`start-session.ps1`):**
- Run `.\start-session.ps1 -SessionDescription "task-name"` to begin any work session
- The script runs `backup.ps1`, verifies the ZIP was created within 90 seconds, then opens VS Code
- If backup fails, the session is aborted

**Option B — Git Pre-Commit Hook (`.git/hooks/pre-commit`):**
- Runs automatically on every `git commit`
- Checks that a backup ZIP exists in `..\backup\IJ\` created within the last 12 hours
- Blocks the commit with a clear error message if no recent backup is found

> **For AI Agents:** Your very first command in any task must be `backup.ps1`. This is enforced by convention (Option A) and by Git (Option B). No exceptions.

### Technologies Used

- HTML5 (semantic markup)
- CSS3 (custom properties, Grid, Flexbox)
- JavaScript (ES6+, vanilla)
- Google Fonts (Inter, Playfair Display)
- SVG icons (inline)

### Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

### Contact

- Email: ijmeerj@gmail.com
- Editor: editor@ijmeer.com
- WhatsApp: +91 98261 21177

### Publisher

Published by **Meer Foundation**  
https://www.meerfoundation.co.in/

---

© 2026 IJMEER - International Journal of Multidisciplinary Explication and Emerging Research
