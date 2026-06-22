# ARCHITECTURE.md — Website Structure & Tech Stack

---

## 1. Technical Stack

| Layer | Technology | Details |
|---|---|---|
| **Hosting** | GitHub Pages | Free tier, static hosting |
| **CDN / DNS** | Cloudflare (Free) | Proxy enabled, SSL managed |
| **Domain Registrar** | GoDaddy | ijmeer.com |
| **SSL** | Cloudflare Full (strict) | End-to-end encryption |
| **Redirect** | Cloudflare Page Rule | 301: non-www → www |
| **Analytics** | Google Tag Manager | Container: GTM-NWHDPZRK |
| **Analytics** | Google Analytics 4 | Measurement ID: G-2FNJ68WF8J |
| **Build System** | None (pure static HTML) | No build step required |
| **Version Control** | Git + GitHub | Branch: main |

---

## 2. Domain Configuration

| Record | Type | Value |
|---|---|---|
| `www.ijmeer.com` | CNAME | `amirhashmilive.github.io` |
| `ijmeer.com` | A/CNAME | Redirects to www via Cloudflare |
| **Primary URL** | — | `https://www.ijmeer.com` |
| **Fallback URL** | — | `https://amirhashmilive.github.io/ijmeer` |
| **CNAME file** | `/CNAME` | Contains: `www.ijmeer.com` |

---

## 3. Folder Structure

```
/ (root)
├── AGENTS.md                  # Agent instructions (memory)
├── ARCHITECTURE.md            # This file
├── WORKFLOW.md                # SOPs
├── UI_GUIDELINES.md           # Design rules
├── CONTENT_RULES.md           # Content policy
├── MEMORY.md                  # Project history
├── CURRENT_TASK.md            # Active task tracker
├── BACKUP.md                  # Backup instructions
├── ISSN_COMPLIANCE.md         # ISSN requirements
├── EDITORIAL_BOARD.md         # All 13 board members
├── SOCIAL_MEDIA.md            # Social media accounts
├── DEPLOYMENT.md              # Deployment process
├── REMINDERS.md               # Active reminders
├── POST_ISSN_ROADMAP.md       # Post-approval roadmap
├── index.html                 # Homepage
├── journal.html               # Journal overview
├── about-this-journal.html    # About page
├── editorial-board.html       # Editorial board listing
├── editorial-portfolio.html   # Detailed member profiles
├── archive.html               # Published issues
├── authors.html               # Author guidelines
├── peer-review.html           # Peer review policy
├── fees-pricing.html          # APC / pricing
├── contact.html               # Contact page
├── privacy-policy.html        # Privacy policy
├── privacy.html               # Privacy (alternate)
├── call-for-papers.html       # CfP page
├── submitting.html            # Submission guide
├── preparing.html             # Manuscript preparation
├── ethics.html                # Publication ethics
├── open-access.html           # Open access policy
├── policies.html              # General policies
├── library.html               # Library resources
├── citations.html             # Citation guide
├── sitemap.xml                # XML sitemap
├── robots.txt                 # Search engine rules
├── manifest.json              # Web app manifest
├── 404.html                   # Error page
├── CNAME                      # GitHub Pages domain
│
├── assets/
│   ├── images/
│   │   └── editorial/         # Editorial board photos
│   └── css/                   # (if any external CSS)
│
├── images/
│   ├── editorial/             # Member photos (WebP)
│   ├── advisory_board/        # Advisory board photos
│   └── international_&_special_editorial_board/
│
├── data/                      # JSON data files
├── papers/                    # Published paper HTML pages
└── pdfs/                      # Published paper PDFs
```

---

## 4. Key Pages & URLs

| Page | File | URL |
|---|---|---|
| Homepage | `index.html` | `/` |
| Journal Overview | `journal.html` | `/journal.html` |
| About | `about-this-journal.html` | `/about-this-journal.html` |
| Editorial Board | `editorial-board.html` | `/editorial-board.html` |
| Editorial Profiles | `editorial-portfolio.html` | `/editorial-portfolio.html` |
| Archive | `archive.html` | `/archive.html` |
| Author Guidelines | `authors.html` | `/authors.html` |
| Peer Review | `peer-review.html` | `/peer-review.html` |
| Fees / Pricing | `fees-pricing.html` | `/fees-pricing.html` |
| Call for Papers | `call-for-papers.html` | `/call-for-papers.html` |
| Contact | `contact.html` | `/contact.html` |
| Privacy Policy | `privacy-policy.html` | `/privacy-policy.html` |
| Ethics | `ethics.html` | `/ethics.html` |
| Open Access | `open-access.html` | `/open-access.html` |

---

## 5. Brand System

### Colors

| Name | Hex | Usage |
|---|---|---|
| **Deep Navy** | `#1a2a3a` | Primary background, headings |
| **Gold / Amber** | `#c9a03d` | Accents, highlights, CTA |
| **Royal Blue** | `#2563EB` | Links, interactive elements |
| **White** | `#ffffff` | Page background, card backgrounds |
| **Emerald Green** | `#059669` | Success states, international badges |
| **Border** | `rgba(26,42,58,0.12)` | Subtle borders |

### CSS Variables (from components)

```css
--navy:     #1a2a3a
--gold:     #c9a03d
--blue:     #2563EB
--emerald:  #059669
--bg:       #ffffff
--text-1:   (primary text)
--text-2:   (secondary text)
--text-3:   (muted text)
```

---

## 6. Typography

| Role | Font | Source |
|---|---|---|
| **Headings** | Playfair Display | Google Fonts |
| **Body / UI** | Inter | Google Fonts |
| **Fallback** | Georgia, serif / system-ui | System |

```html
<!-- Google Fonts import -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,700;0,800;1,700&display=swap" rel="stylesheet">
```

---

## 7. Components System

Shared navigation, footer, and scripts are loaded via `components.js` which injects:
- **Header / Navigation** — consistent across all pages
- **Footer** — includes "Since 2026", copyright, social links
- **Cookie consent / GDPR** — if applicable

**File location:** `assets/js/components.js` *(verify exact path)*

---

## 8. SEO Configuration

| Element | Value |
|---|---|
| **Google Tag Manager** | GTM-NWHDPZRK |
| **GA4 Measurement ID** | G-2FNJ68WF8J |
| **Sitemap** | `/sitemap.xml` |
| **Robots** | `/robots.txt` |
| **OG Tags** | Present on all major pages |
| **Twitter Cards** | Present on all major pages |
| **Canonical URLs** | `https://www.ijmeer.com/[page]` |

---

## 9. Image Standards

| Requirement | Standard |
|---|---|
| **Format** | WebP (mandatory for new images) |
| **Editorial photos** | 400×400px (circular display) |
| **Srcset sizes** | 200w, 400w, 800w variants + original |
| **Loading** | `loading="lazy"` on all non-above-fold images |
| **Alt text** | Descriptive, includes name and role |
