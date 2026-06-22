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
| **International Members** | 2 (Dr. Mary Lou Frank 🇺🇸, Prof. Jyotirmaya Thakur 🇬🇧) | 2026-06-22 |
| **Board Members Total** | 13 | 2026-06-22 |
| **Volume 1 Issue 1** | Published April 2026 | 2026-04-01 |
