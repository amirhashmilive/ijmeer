# IJMEER Project Policy — Mandatory for All Work

> **Status:** ACTIVE — Enforced on all present and future work  
> **Created:** 2026-05-09  
> **Applies to:** All files, images, scripts, HTML, CSS, JS, PDFs, and JSON in this project  
> **Enforcement:** The agent must check this document before adding or modifying any file

---

## Table of Contents

1. [Image Policy](#1-image-policy)
2. [File Naming Policy](#2-file-naming-policy)
3. [Agent Enforcement Rules](#3-agent-enforcement-rules)
4. [Violation Examples](#4-violation-examples-good-vs-bad)
5. [Automation Scripts](#5-automation-scripts)
6. [Policy Change Log](#6-policy-change-log)

---

## 1. Image Policy

### 1.1 File Format

| Rule | Requirement |
|------|-------------|
| **Primary format** | WebP (`.webp`) — mandatory for all images |
| **Exception** | AVIF (`.avif`) only if WebP causes visible quality loss |
| **Banned formats** | `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.tiff` (for new files) |
| **Legacy bak files** | Existing `.png.bak` / `.jpg.bak` files are permitted as backups — do NOT delete them |

**Auto-conversion rule:** Any PNG or JPG added in the future **MUST** be converted to WebP before the commit is made. Raw originals may be kept as `.original.bak` but must never be the referenced file.

---

### 1.2 File Naming Convention

| Rule | Requirement |
|------|-------------|
| **Case** | All lowercase — no uppercase letters ever |
| **Separators** | Hyphens `-` only — no underscores `_`, no spaces |
| **Special characters** | None (`&`, `+`, `%`, `(`, `)`, `#`, `@`, etc. are all banned) |
| **Max length** | 50 characters (excluding extension) |
| **Prefix system** | Use category prefix followed by descriptive name (see table below) |

#### Naming Prefix Guide

| Image Category | Prefix | Example |
|----------------|--------|---------|
| Editorial board photos | `editorial-` | `editorial-mary-lou-frank.webp` |
| Advisory board photos | `advisory-` | `advisory-mona-purohit.webp` |
| International board photos | `intl-board-` | `intl-board-jyotirmaya-thakur.webp` |
| Journal logos | `logo-` | `logo-ijmeer-horizontal.webp` |
| Favicon | `favicon-` | `favicon-ijmeer.webp` |
| Hero / banner images | `hero-` | `hero-homepage-bg.webp` |
| Icons / illustrations | `icon-` | `icon-open-access.webp` |
| Diagrams / mindmaps | `diagram-` | `diagram-disciplines-mindmap.webp` |
| Blog / chronicle images | `blog-` | `blog-research-ethics-2026.webp` |
| PDF cover thumbnails | `thumb-` | `thumb-vol1-issue1-article1.webp` |

#### Current Files — Compliance Status

The following files exist and are **grandfathered** (not renamed to avoid breaking references), but all **new** files must follow the new convention:

| Current Name (grandfathered) | Policy-Compliant Name (for new additions) |
|------------------------------|-------------------------------------------|
| `DrMaryLouFrank.webp` | `editorial-mary-lou-frank.webp` |
| `ProfDrAshokLSunatkari.webp` | `editorial-ashok-sunatkari.webp` |
| `drnusratalihashmi.webp` | `editorial-nusrat-ali-hashmi.webp` |
| `sayedamirmustafahashmi.webp` | `editorial-sayed-amir-hashmi.webp` |
| `drmonapurohit.webp` | `advisory-mona-purohit.webp` |
| `hero-bg.webp` | ✅ Compliant |
| `ijmeer-favicon.webp` | ✅ Compliant |
| `ijmeer-logo-horizontal.webp` | ✅ Compliant |

> **Note:** The folder `images/international_&_special_editorial_board/` violates policy (contains `&` and `_`). Any new folders must be named `images/intl-board/` or similar. The existing folder is grandfathered.

---

### 1.3 Image Dimensions & Performance

| Rule | Requirement |
|------|-------------|
| **Max file size** | 200 KB for photos, 100 KB for icons/logos, 500 KB for hero images |
| **Display size rule** | No image may be larger than 2× its CSS display size |
| **Responsive images** | Use `srcset` with 2–3 sizes for images wider than 300px at any breakpoint |
| **Lazy loading** | All images below the fold must have `loading="lazy"` |
| **Above-the-fold** | Hero and header images must have `loading="eager"` (or no attribute) |

#### srcset Template
```html
<img
  src="assets/images/hero-bg.webp"
  srcset="assets/images/hero-bg-480.webp 480w,
          assets/images/hero-bg-960.webp 960w,
          assets/images/hero-bg.webp 1920w"
  sizes="100vw"
  alt="IJMEER journal homepage background"
  loading="eager"
  width="1920" height="1080">
```

---

### 1.4 Alt Text Requirements

Every `<img>` tag **must** have a descriptive `alt` attribute. Empty `alt=""` is only permitted for purely decorative images that convey no information.

| Image Type | Alt Text Format | Example |
|------------|-----------------|---------|
| Editorial photos | `"[Full Name] — [Designation]"` | `"Dr. Mary Lou Frank — Editorial Board Member"` |
| EIC photo | `"[Full Name] — Editor-in-Chief, IJMEER"` | `"Dr. Nusrat Ali Hashmi — Editor-in-Chief, IJMEER"` |
| Journal logos | `"IJMEER logo"` or `"IJMEER [variant] logo"` | `"IJMEER horizontal logo"` |
| Favicon | `"IJMEER favicon"` | `"IJMEER favicon"` |
| Hero backgrounds | Descriptive of content | `"Scholarly journal homepage hero"` |
| Icons | Descriptive action/concept | `"Open Access icon"`, `"Peer review shield icon"` |
| Diagrams | Describe what it shows | `"Mindmap of 70+ academic disciplines covered by IJMEER"` |
| Decorative only | `""` (empty string) | `alt=""` |

---

## 2. File Naming Policy

### 2.1 Universal Rules (All Files)

| Rule | Requirement |
|------|-------------|
| **Case** | All lowercase — no CamelCase, no ALLCAPS |
| **Separators** | Hyphens `-` for words — no underscores, no spaces |
| **Special characters** | None allowed in filenames |
| **Max length** | 50 characters (excluding extension) |
| **Versioning** | Do not version files with `_v2`, `-final`, `-copy` suffixes — use Git for versioning |

---

### 2.2 By File Type

#### HTML Files
- Pattern: `[topic-name].html`
- All lowercase, hyphen-separated words
- ✅ `editorial-board.html`, `call-for-papers.html`, `open-access.html`
- ❌ `EditorialBoard.html`, `Call_For_Papers.html`, `openaccess.html`

#### CSS Files
- Pattern: `[purpose].css` or `[scope]-[purpose].css`
- ✅ `style.css`, `main.css`, `premium.css`
- ❌ `Style.css`, `main_style.css`, `MainStyles.css`

#### JavaScript Files
- Pattern: `[purpose].js` or `[scope]-[feature].js`
- ✅ `core.js`, `components.js`, `citation-export.js`, `timeline.js`
- ❌ `Core.js`, `citation_export.js`, `TimelineScript.js`

#### PDF Files
- Pattern: `vol[N]-issue[N]-article[N].pdf`
- ✅ `vol1-issue1-article1.pdf`, `vol2-issue3-article12.pdf`
- ❌ `Vol1-Issue1-Article1.pdf`, `volume1_issue1_article1.pdf`, `paper-mental-health-kerala.pdf`

#### JSON Files
- Pattern: `[data-name].json`
- ✅ `papers.json`, `issues.json`, `editorial-board.json`
- ❌ `Papers.json`, `paper_data.json`, `IssueData.json`

#### PowerShell / Script Files
- Pattern: `[action-verb]-[subject].ps1`
- ✅ `backup.ps1`, `start-session.ps1`, `check-policy.ps1`
- ❌ `Backup.ps1`, `backup_script.ps1`, `BackupScript.ps1`

#### Image Files — see [Section 1.2](#12-file-naming-convention)

---

### 2.3 Directory Naming

| Rule | Requirement |
|------|-------------|
| **Case** | All lowercase |
| **Separators** | Hyphens preferred; no spaces or special characters |
| **Depth** | Max 3 levels deep under project root |

✅ `images/editorial/`, `assets/css/`, `assets/js/`, `images/advisory-board/`  
❌ `Images/Editorial/`, `assets/CSS/`, `images/international_&_special_editorial_board/`

---

## 3. Agent Enforcement Rules

### 3.1 Pre-Change Checklist

Before **any** change that adds, renames, or modifies a file or image, the agent MUST:

1. **Identify** the file(s) being added or changed
2. **Check** the filename against Section 1.2 (images) or Section 2.2 (other files)
3. **Check** the format (images must be WebP)
4. **Check** alt text if an `<img>` tag is being added or modified
5. **Check** file size estimate if an image is being added
6. **Decide**: Auto-correct OR warn the user

---

### 3.2 Auto-Correct vs. Warn

| Situation | Action |
|-----------|--------|
| New image is PNG/JPG with no existing references | Auto-convert to WebP silently, log it |
| New filename violates naming convention (new file) | Auto-rename to compliant name, log it |
| Existing file has a bad name but is widely referenced | Warn user, propose rename plan, do NOT auto-rename |
| Missing alt text on new `<img>` | Warn user and refuse to commit until fixed |
| Image over size limit | Warn user, offer to compress, log it |
| Directory name violates policy (new dir) | Auto-name correctly, log it |
| Existing violation found during unrelated work | Log it as a known violation, do not disrupt current task |

---

### 3.3 Policy Log

After each compliance check, append an entry to `policy-log.md` in the project root.

#### Log Entry Format
```
### [YYYY-MM-DD] [PASS|WARN|FIXED] — [brief description]
- File: `filename.ext`
- Rule checked: [rule name from policy]
- Result: [what happened]
- Action taken: [none | auto-fixed | user-warned]
```

---

### 3.4 Git Commit Rule

The agent must ensure that any commit that adds images or files includes a mention of policy compliance in the commit message or notes. Example:

```
git commit -m "Add editorial photo for new board member (policy-compliant: WebP, correct naming)"
```

---

## 4. Violation Examples — Good vs. Bad

### Images

| ❌ BAD | ✅ GOOD | Rule violated |
|--------|---------|---------------|
| `DrMaryLouFrank.PNG` | `editorial-mary-lou-frank.webp` | Format + naming |
| `Photo of Dr. Hashmi.jpg` | `editorial-nusrat-ali-hashmi.webp` | Spaces + format + naming |
| `IMG_20240512_093412.jpg` | `advisory-ranu-shukla.webp` | Camera default name + format |
| `editorial_board_member_1.webp` | `editorial-mary-lou-frank.webp` | Underscore + vague name |
| `LOGO.PNG` | `logo-ijmeer-square.webp` | Uppercase + format |
| `thisisaverylongfilenamethatisjusttoolargetobeusefulinanyway.webp` | `editorial-john-doe.webp` | Exceeds 50 characters |
| `<img src="photo.webp">` (no alt) | `<img src="photo.webp" alt="Dr. John Doe — Board Member">` | Missing alt text |

### Files

| ❌ BAD | ✅ GOOD | Rule violated |
|--------|---------|---------------|
| `EditorialBoard.html` | `editorial-board.html` | CamelCase |
| `Call_For_Papers.html` | `call-for-papers.html` | Underscores |
| `Volume 1 Issue 1 Article 1.pdf` | `vol1-issue1-article1.pdf` | Spaces + verbose naming |
| `Paper_MentalHealth_Kerala_2026_FINAL_v2.pdf` | `vol1-issue2-article3.pdf` | Underscores + versioning suffix |
| `MainStyles.css` | `style.css` or `main.css` | CamelCase |
| `Papers Data.json` | `papers.json` | Space |
| `script_backup_v3_FINAL.ps1` | `backup.ps1` | Underscores + versioning |

---

## 5. Automation Scripts

### 5.1 Policy Checker Script

See `scratch/check-policy.ps1` for the full enforcement script.

Run it any time to get a compliance report:

```powershell
# From project root:
powershell -NoProfile -ExecutionPolicy Bypass -File scratch/check-policy.ps1
```

The script checks:
- All image files for format violations (non-WebP)
- All files for naming violations (uppercase, spaces, underscores)
- All filenames exceeding 50 characters
- Reports a summary with violation counts

### 5.2 Pre-Commit Hook (Optional)

To enforce policy automatically before every git commit, add to `.git/hooks/pre-commit`:

```bash
#!/bin/sh
powershell -NoProfile -ExecutionPolicy Bypass -File scratch/check-policy.ps1 --strict
if [ $? -ne 0 ]; then
  echo "Policy violations found. Commit blocked."
  exit 1
fi
```

---

## 6. Policy Change Log

| Date | Change | Author |
|------|--------|--------|
| 2026-05-09 | Initial policy created | Agent (per user instruction) |

---

*This document is the authoritative policy for the IJMEER project. When in doubt, refer here first.*
