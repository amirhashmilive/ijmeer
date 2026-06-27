# MEMORY.md — Project History & Decisions

> **Agents: Update this file at the end of every session with what was changed.**  
> Format: `### YYYY-MM-DD — [Brief title]`

---

## Key Decisions (Permanent Record)

| Decision | Value | Rationale |
|---|---|---|
| **ISSN Starting Year** | **2026** | ISSN application ID 75192 shows Year: 2026. Website must match exactly. |
| **International Members Minimum** | **2** | ISSN requires at least 2 members from outside India |
| **Access Model** | Diamond Open Access | Free to read, free to publish. No APC. |
| **Pricing (Indian authors)** | INR only | No GST, no USD for Indian authors |
| **Pricing (International)** | USD | Standard international |
| **Dark Mode** | ❌ Never | Brand decision |
| **Fast Track** | ❌ Never | Not offered |
| **Grid Layout** | Single column (1fr) | All profile cards horizontal, full-width |
| **Reference profile card** | Ashok Sunatkari | Standard DOM structure all others must follow |
| **Image format** | WebP mandatory | Performance and modern standard |
| **Branch** | main | All deployments to main branch |

---

## Recent Changes (Reverse Chronological)

### 2026-06-27 — Update Dr. Hafid Zakariya's institutional email
- **Changed:** Replaced `info@uniba.ac.id` with `hafidzakariya@uibs.ac.id` for Dr. Hafid Zakariya across all pages where it appeared.
- **Reason:** User request — correct institutional email address.
- **Files:** `editorial-board.html`, `editorial-portfolio.html`
- **Commit:** `update: Dr. Hafid Zakariya institutional email to hafidzakariya@uibs.ac.id`

### 2026-06-24 — Update Media Kit UI & Workflow JSON Automation
- **Changed:** 
  - Updated `media-kit.html` with a fully interactive Post Viewer UI, complete with tab switching for platforms, week selection, dynamic image preview logic, and "copy to clipboard" functionality.
  - Implemented client-side dynamic loading for trending posts in `media-kit.html` using `trending/index.json`.
  - Refactored `.github/workflows/media-kit-weekly.yml` to compile generated weekly posts into a single `social-posts.json`.
  - Updated `.github/workflows/media-kit-trending.yml` to parse and append trending posts into `trending/index.json`.
  - Updated `.github/workflows/media-kit-quarterly.yml` to initialize an empty `social-posts.json` and trim the `trending/index.json` to 10 entries upon quarter rotation.
- **Reason:** Implement structured JSON-driven UI as requested.
- **Files:** `media-kit.html`, `.github/workflows/*.yml`
- **Commit:** Pending

### 2026-06-24 — Add complete Media Kit system
- **Changed:** Created entire Media Kit system with 16 new files across 3 components:
  - `media-kit.html` — New page matching site design with 6 sections (press release, social posts, trending, assets, archive, download)
  - `media-kit/` — Content folder with `memory.md` (agent guidelines), `trending-tracker.md` (detection logic + scholar calendar)
  - `media-kit/quarter-2026-Q3/` — Full Q3 content: social posts for all 5 platforms (LinkedIn, Twitter/X, Instagram, Facebook, WhatsApp), press release, newsletter draft
  - `media-kit/quarter-2026-Q3/images/` — 3 sample Week 1 images in WebP (LinkedIn 16:9, Instagram 4:3, Story 9:16)
  - `.github/workflows/` — 3 GitHub Actions workflows: weekly post generation, daily trending detection, quarterly archive rotation
  - `media-kit/trending/` and `media-kit/archive/` — Empty directories with .gitkeep (populated by workflows)
- **Reason:** User requested automated media kit system with AI-powered content generation.
- **Files:** `media-kit.html`, `media-kit/memory.md`, `media-kit/trending-tracker.md`, `media-kit/quarter-2026-Q3/social-posts/*.txt`, `media-kit/quarter-2026-Q3/press-release.md`, `media-kit/quarter-2026-Q3/newsletter-draft.md`, `media-kit/quarter-2026-Q3/images/*.webp`, `.github/workflows/media-kit-*.yml`
- **Commit:** Pending
- **Note:** No existing files were modified. Footer link to Media Kit was NOT added (user rule: "DO NOT change any existing page"). API keys must be stored in GitHub Secrets only.

### 2026-06-24 — Update editorial board profiles and advisory board
- **Changed:** Added key achievements with book hyperlinks for Editor-in-Chief Dr. Nusrat Ali Hashmi. Added Rajhans Yeshwant Gaikwad to the Advisory Board in the first position. Upgraded Managing Editor Sayed Amir Mustafa Hashmi's profile to match the EIC card format, including expanded layout and key achievements. Updated board statistics. Removed SINTA profile and updated institutional link for Dr. Hafid Zakariya. Redesigned Sayed Amir's card to use badges and added a bio and personal website link.
- **Reason:** User request for profile enhancements and new board member addition.
- **Files:** `editorial-board.html`, `images/editorial/rajhans-gaikwad.webp`
- **Commit:** Pending

### 2026-06-24 — Add Dr. Hafid Zakariya, remove Prof. Mona Purohit
- **Changed:** Removed Prof. (Dr.) Mona Purohit from the Advisory Board. Added Dr. Hafid Zakariya to the Editorial Board Members.
- **Reason:** User request.
- **Files:** `editorial-board.html`, `editorial-portfolio.html`, `images/editorial/dr-hafid-zakariya.webp`
- **Commit:** Pending

### 2026-06-24 — Restructure editorial board layout
- **Changed:** Expanded Editor-in-Chief card to occupy full width and enhanced profile details. Moved Managing Editor to the bottom of the page, after the Advisory Board.
- **Reason:** User request for layout adjustments.
- **Files:** `editorial-board.html`
- **Commit:** Pending

### 2026-06-23 — URGENT ISSN Compliance Fixes
- Standardized founding year to 2026 across `privacy-policy.html`, `rights-permissions.html`, and `data/config.json` to prevent ISSN application rejection.
- Restructured `editorial-board.html` and `editorial-portfolio.html` for ISSN compliance:
  - Removed "International & Special Board Members" section completely.
  - Moved Prof. (Dr.) Jyotirmaya Thakur and Dr. Anupama Patel to the Advisory Board.
  - Restructured the Leadership section: Managing Editor is now displayed alongside Editor-in-Chief in a 3-card/1-card layout.
- Verified Dr. Mary Lou Frank and Lect. Ayşegül Akkaya fulfill the 2-international-member requirement.

### 2026-06-23 — Add Dr. Shivaji Dhondiram Sargar to editorial board
- **Changed:** Added full profile for Dr. Shivaji Dhondiram Sargar to editorial board.
- **Reason:** User request.
- **Files:** `EDITORIAL_BOARD.md`, `editorial-board.html`, `editorial-portfolio.html`, `assets/images/editorial-board/shivaji-sargar.webp`
- **Commit:** `cc2ccb3` (fix: `6076a28`)

### 2026-06-23 — Update Dr. Nusrat Ali Hashmi's designation
- **Changed:** Updated her designation to "Bombay High Court Advocate"
- **Reason:** Content refinement request
- **Files:** `editorial-portfolio.html`
- **Commit:** `3e76e62`

### 2026-06-23 — Update Dr. Nusrat Ali Hashmi's experience
- **Changed:** Updated her experience from "30+ Yrs" to "20+ Yrs"
- **Reason:** Corrected information request
- **Files:** `editorial-portfolio.html`, `EDITORIAL_BOARD.md`
- **Commit:** `1248336`

### 2026-06-23 — Correct Prof. Nuzhat Parveen Khan's name
- **Changed:** Updated her name from "Prof. Nuzhat Parveen Khan" to "Prof. (Dr.) Nuzhat Parveen Khan"
- **Reason:** Name correction request
- **Files:** `editorial-board.html`, `editorial-portfolio.html`, `EDITORIAL_BOARD.md`
- **Commit:** `50910b0`

### 2026-06-22 — Fix editorial portfolio horizontal card layout
- **Changed:** `.profiles-grid` CSS from `repeat(auto-fit, minmax(400px, 1fr))` to `1fr`
- **Reason:** Dr. Nusrat Ali Hashmi and Sayed Amir Mustafa Hashmi were appearing as vertical side-by-side cards instead of horizontal cards like all other members
- **Files:** `editorial-portfolio.html`
- **Commit:** `3f02ee4`

### 2026-06-22 — Fix editorial portfolio structural consistency
- **Changed:** Standardized accent classes, moved intl-spotlight below profile-top for Mary Frank and Jyotirmaya Thakur, added `.accent-advisory` CSS class
- **Reason:** Inconsistent card structure across profiles
- **Files:** `editorial-portfolio.html`
- **Commit:** `5e1c445`

### 2026-06-22 — Add Prof. Nuzhat Parveen Khan + Dr. Mary Lou Frank address
- **Changed:** Added Nuzhat Khan's full profile to both `editorial-board.html` and `editorial-portfolio.html`; Added "100 University Parkway, Macon, GA 31206, USA" to Dr. Mary Lou Frank
- **Reason:** ISSN compliance — missing international member and address
- **Files:** `editorial-board.html`, `editorial-portfolio.html`, `assets/images/editorial/nuzhat-khan.webp`
- **Commit:** `7ccb05b`

### 2026-06-22 — Fix starting year 2025 → 2026
- **Changed:** All references to journal founding/establishment year from 2025 to 2026 across all HTML files and `components.js`
- **Reason:** ISSN application (ID: 75192) shows Year: 2026 — website must match
- **Files:** `index.html`, `about-this-journal.html`, `journal.html`, `editorial-portfolio.html`, `components.js` (and others)
- **Commit:** `d7ecb8f`

### 2026-06-22 — Remove scratch files from git
- **Changed:** Added `scratch/` to `.gitignore`, purged from history
- **Reason:** Temporary files were accidentally committed
- **Files:** `.gitignore`
- **Commit:** `dd1adbc`

### 2026-06-22 — Remove signature from components
- **Changed:** Removed signature/watermark element
- **Commit:** `045d351`

### Prior — Add OG/Twitter Card tags to all major pages
- **Changed:** Added Open Graph and Twitter Card meta tags to all major pages
- **Commits:** `191c24c`, `0457670`, `2f696ea`

---

## Known Issues & Technical Debt

| Issue | Status | Priority |
|---|---|---|
| Institutional emails missing for EIC (Dr. Nusrat) and ME (Amir Hashmi) | ⏳ Pending | High |
| Complete postal addresses needed for some board members | ⏳ Pending | High |
| Individual article PDF links needed in archive | ⏳ Pending | Medium |
| ISSN placeholder needs replacing when numbers arrive | ⏳ Waiting on ISSN | High |
| Google indexing: 7 of 27 pages indexed | 🔄 In progress | Medium |

---

## Pending Tasks

- [ ] Add institutional emails for Dr. Nusrat Ali Hashmi and Sayed Amir Mustafa Hashmi
- [ ] Verify and complete postal addresses for all 13 board members
- [ ] Create individual article pages in `/papers/` for Volume 1 Issue 1
- [ ] Ensure each article has its own PDF link in archive
- [ ] Update all `XXXX-XXXX` placeholders once ISSN is received (expected ~30 working days from April 24, 2026)
- [ ] Submit DOAJ application after ISSN receipt
- [ ] Submit UGC Care application
- [ ] Submit Index Copernicus application

---

## Current Status

| Metric | Value | Date |
|---|---|---|
| **ISSN Application** | Submitted; hard copy received April 24, 2026 | 2026-04-24 |
| **ISSN Expected** | ~30 working days from April 24 (approx. June 2026) | — |
| **Google Pages Indexed** | 7 / 27 discovered | 2026-06-22 |
| **International Members** | 3 (Dr. Mary Lou Frank 🇺🇸, Prof. Jyotirmaya Thakur 🇬🇧, Lect. Ayşegül Akkaya 🇹🇷) | 2026-06-23 |
| **Board Members Total** | 15 | 2026-06-23 |
| **Volume 1 Issue 1** | Published April 2026 | 2026-04-01 |
