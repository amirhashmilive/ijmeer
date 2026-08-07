# MEMORY.md — Project History & Decisions

> **Agents: Update this file at the end of every session with what was changed.**  
> Format: `### YYYY-MM-DD — [Brief title]`

---

## Key Decisions (Permanent Record)

| Decision | Value | Rationale |
|---|---|---|
| **ISSN Starting Year** | **2026** | ISSN application ID 75192 shows Year: 2026. Website must match exactly. |
| **International Members Minimum** | **2** | ISSN requires at least 2 members from outside India |
| **Access Model** | Diamond Open Access (CC BY-NC 4.0) | Free to read, free to publish. NonCommercial license. |
| **Pricing (Indian authors)** | INR only | No GST, no USD for Indian authors |
| **Pricing (International)** | USD | Standard international |
| **Dark Mode** | ❌ Never | Brand decision |
| **Fast Track** | ❌ Never | Not offered |
| **Grid Layout** | Single column (1fr) | All profile cards horizontal, full-width |
| **Reference profile card** | Ashok Sunatkari | Standard DOM structure all others must follow |
| **Image format** | WebP mandatory | Performance and modern standard |
| **Term enforcement** | Yog = Yoga | Always use "Yoga" instead of "Yog" across all pages and documentation |
| **Branch** | main | All deployments to main branch |

---

## Recent Changes (Reverse Chronological)

### 2026-08-08 — Add Editorial Board page with photos to Volume 1, Issue 1 and Issue 2 print versions
- **Changed:**
  1. Built dedicated visual Editorial Board page titled "Meet the Minds Behind IJMEER" with photographs, institutional emails, and designations for 12 members.
  2. Top Section: Editor-in-Chief Dr. Nusrat Ali Hashmi (`dr.nusrathashmi@live.com`) and Managing Editor Sayed Amir Mustafa Hashmi (`editor@ijmeer.com`).
  3. Middle Section: Prominent "INTERNATIONAL" badges for 3 international board members (Dr. Mary Lou Frank — USA `marylou.frank@mga.edu`, Dr. Hafid Zakariya — Indonesia `hafidzakariya@uibs.ac.id`, Lect. Ayşegül Akkaya — Türkiye `aysegulunal@istanbul.edu.tr`).
  4. Bottom Section: 7 Editorial Board members grid (Prof. Nuzhat Parveen Khan, Prof. Ashok L. Sunatkari, Adv. Ashok Yende, Prof. Karuna A. Malviya, Dr. Mohammed Salim Khan, Dr. Shivaji Dhondiram Sargar, Dr. Momin Ali).
  5. Excluded Advisory Board members per instructions.
  6. Updated `papers/volume_1/issue_1/ijmeer_v1_i1_complete_issue.pdf` (Page 4, preserved 29 total pages).
  7. Updated `papers/volume_1/issue_2/ijmeer_v1_i2_complete_issue.pdf` (Page 5, preserved 67 total pages).
- **Reason:** User directive to add dedicated Editorial Board page with photos and institutional emails in print version complete issue PDFs.
- **Files:** `papers/volume_1/issue_1/ijmeer_v1_i1_complete_issue.pdf`, `papers/volume_1/issue_2/ijmeer_v1_i2_complete_issue.pdf`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Add Editorial Board page with photos to Volume 1, Issue 1 and Issue 2 print versions`

### 2026-08-08 — Deep clean: Remove ISSN from all Volume 1, Issue 1 and Issue 2 HTML pages
- **Changed:**
  1. Removed `<meta name="citation_issn" content="3139-6003">` from all 20 article HTML pages (5 Issue 1 + 15 Issue 2).
  2. Removed `"issn": "3139-6003"` from JSON-LD structured data (`Periodical` object) in all 20 article pages.
  3. Removed `ISSN: 3139-6003` from sub-header text line in all 20 article pages (preserving DOI for Issue 2 articles).
  4. Removed `ISSN (Online)` table row from sidebar "Article Details" table in all 20 article pages.
  5. Removed `<meta name="citation_issn">` from `archive.html`.
  6. Removed E-ISSN grid items from both Issue 1 and Issue 2 cards in `print-archive.html`.
  7. Verified: zero references to `3139-6003` remain in any Issue 1/2 file. Remaining references are journal-level only (index.html, journal.html, contact.html, components.js, config.json) — correct and intentional.
  8. Confirmed: `papers.json`, `issues.json`, `sitemap.xml` were already clean (no ISSN field present).
- **Reason:** Volume 1 Issue 1 (April 2026) and Issue 2 (July 2026) were published BEFORE ISSN was officially assigned (August 2026). ISSN 3139-6003 must not appear on pre-assignment issues.
- **Files:** `article-v1i1p01.html` to `article-v1i1p05.html`, `article-v1i2p01.html` to `article-v1i2p15.html`, `archive.html`, `print-archive.html`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Deep clean: Remove ISSN from all Volume 1, Issue 1 and Issue 2 PDFs and HTML pages`

### 2026-08-07 — Correction: Remove ISSN from Volume 1, Issue 1 and Issue 2; ISSN applies from Issue 3 onwards
- **Changed:**
  1. Updated `papers/volume_1/issue_1/ijmeer_v1_i1_complete_issue.pdf` — blacked out `E-ISSN: 3139-6003` line from cover image and redacted all ISSN references from internal title page and footers.
  2. Updated `papers/volume_1/issue_2/ijmeer_v1_i2_complete_issue.pdf` — blacked out `E-ISSN: 3139-6003` line from cover image and redacted all ISSN references from internal title page, editorial pages, TOC, and running headers.
  3. Updated 15 individual article PDFs in `papers/volume_1/issue_2/` — redacted ISSN from running headers.
  4. Regenerated WebP cover thumbnails in `assets/images/covers/` (`ijmeer-cover-v1i1.webp`, `ijmeer-cover-v1i2.webp`).
  5. Created `docs/generate_future_cover_template.py` — python generator script for future issue cover pages (Issue 3 onwards) enforcing ISSN placement in the right-hand top corner.
  6. Updated `docs/ISSUE_STANDARDS.md` — documented ISSN placement rules (No ISSN for Issue 1 & 2; ISSN in right-hand top corner for Issue 3+).
- **Reason:** Volume 1 Issue 1 (April 2026) and Issue 2 (July 2026) were published BEFORE ISSN was officially assigned (August 2026). ISSN 3139-6003 will apply starting from Volume 1 Issue 3 (October 2026).
- **Files:** `papers/volume_1/issue_1/ijmeer_v1_i1_complete_issue.pdf`, `papers/volume_1/issue_2/ijmeer_v1_i2_complete_issue.pdf`, `papers/volume_1/issue_2/*.pdf`, `assets/images/covers/ijmeer-cover-v1i1.webp`, `assets/images/covers/ijmeer-cover-v1i2.webp`, `docs/generate_future_cover_template.py` (NEW), `docs/ISSUE_STANDARDS.md`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Correction: Remove ISSN from Volume 1, Issue 1 and Issue 2; ISSN applies from Issue 3 onwards`

### 2026-08-05 — Create ISSUE_STANDARDS.md for agentic memory and enforcement
- **Changed:**
  1. Created `docs/ISSUE_STANDARDS.md` — master volume, issue, quarter, coverage period, submission deadline, and publication schedule standards file with strict enforcement rules and checklist.
  2. Updated `AGENTS.md` — added explicit enforcement instruction requiring agents to reference `ISSUE_STANDARDS.md` before creating or modifying any journal issue.
  3. ISSUE_STANDARDS.md — Created and enforced. All future Volume/Issue numbering must follow the master schedule. Any deviation requires explicit approval.
- **Reason:** Prevent volume, issue, date, or quarter mismatches across website content, PDFs, metadata, and print packages.
- **Files:** `docs/ISSUE_STANDARDS.md` (NEW), `AGENTS.md`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Create ISSUE_STANDARDS.md for agentic memory and enforcement of volume/issue numbering and publication schedule`

### 2026-08-05 — Update second page (Title Page & Journal Specifications) for Volume 1, Issue 1 and Issue 2
- **Changed:**
  1. Updated Page 2 of `papers/volume_1/issue_2/ijmeer_v1_i2_complete_issue.pdf` with corrected Journal Specifications & Profile table for Volume 1, Issue 2 (April – June 2026, E-ISSN: 3139-6003, DOI: 10.5281/zenodo.21809155). Preserved total 67 pages.
  2. Updated Page 2 of `papers/volume_1/issue_1/ijmeer_v1_i1_complete_issue.pdf` with corrected Journal Specifications & Profile table for Volume 1, Issue 1 (January – March 2026, E-ISSN: 3139-6003, DOI: 10.5281/zenodo.19565393). Preserved total 29 pages.
- **Reason:** Update complete issue PDF front matter with official journal specifications table for Volume 1 Issue 1 and Issue 2.
- **Files:** `papers/volume_1/issue_2/ijmeer_v1_i2_complete_issue.pdf`, `papers/volume_1/issue_1/ijmeer_v1_i1_complete_issue.pdf`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Update second page (Title Page & Journal Specifications) for Volume 1, Issue 1 and Issue 2`

### 2026-08-05 — Update cover pages for Volume 1, Issue 1 and Volume 1, Issue 2 with new designs
- **Changed:**
  1. Updated `papers/volume_1/issue_2/ijmeer_v1_i2_complete_issue.pdf` — replaced Page 1 (cover) with new cover design from `cover issue 02.png` (preserved all 67 pages, front matter, and 15 articles).
  2. Updated `papers/volume_1/issue_1/ijmeer_v1_i1_complete_issue.pdf` — replaced Page 1 (cover) with new cover design from `cover issue 01.png` (preserved all 29 pages, front matter, and 5 articles).
  3. Created WebP thumbnails in `assets/images/covers/` (`ijmeer-cover-v1i2.webp`, `ijmeer-cover-v1i1.webp`) and updated `print-archive.html` cards to display new visual cover previews.
- **Reason:** Update complete issue PDF packages with official new cover page designs for Volume 1 Issue 1 and Volume 1 Issue 2.
- **Files:** `papers/volume_1/issue_2/ijmeer_v1_i2_complete_issue.pdf`, `papers/volume_1/issue_1/ijmeer_v1_i1_complete_issue.pdf`, `assets/images/covers/ijmeer-cover-v1i2.webp` (NEW), `assets/images/covers/ijmeer-cover-v1i1.webp` (NEW), `print-archive.html`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Update cover pages for Volume 1, Issue 1 and Volume 1, Issue 2 with new designs`

### 2026-08-05 — Add Print Archive page and footer link
- **Changed:**
  1. Created `print-archive.html` — dedicated print version archive page with card-based layout for downloading complete issue PDFs. Displays Vol 1 Issue 2 (67 pages, 15 articles, DOI: 10.5281/zenodo.21809155) and Vol 1 Issue 1 (29 pages, 5 articles, DOI: 10.5281/zenodo.19565393).
  2. Built `papers/volume_1/issue_1/ijmeer_v1_i1_complete_issue.pdf` — compiled 29-page complete issue PDF for Vol 1 Issue 1 (4 front matter pages + 25 article pages) so both issues have real downloadable print packages.
  3. Updated `assets/js/components.js` — added "Print Archive" link (`print-archive.html`) to footer Journal navigation column.
  4. Updated `sitemap.xml` — added `print-archive.html` under Core Pages and `ijmeer_v1_i1_complete_issue.pdf` entry.
  5. Updated `archive.html` — replaced "Download Complete Issue (PDF)" button with "Download Print Versions" button pointing to `print-archive.html`.
- **Reason:** Provide a dedicated page for libraries, institutions, and readers to download complete print-ready issue PDFs.
- **Files:** `print-archive.html` (NEW), `papers/volume_1/issue_1/ijmeer_v1_i1_complete_issue.pdf` (NEW), `assets/js/components.js`, `sitemap.xml`, `archive.html`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Add Print Archive page and footer link for print version downloads`

### 2026-08-05 — Build ISSN-compliant Volume 1, Issue 2 complete issue package
- **Changed:**
  1. Removed `cover-design-samples/` directory as requested.
  2. Built 5 front matter pages: Cover Page (using `ijmeer cover page vol 1 issue 2.png`), Title Page & Journal Profile Specifications, From the Editor-in-Chief's Desk (Dr. Nusrat Ali Hashmi), Table of Contents listing all 15 articles with titles, authors, categories, and page numbers, and Publisher Details (Meer Foundation) with Editorial Board Master List and Governance Policies.
  3. Merged front matter with all 15 individual article PDFs into a single 67-page ISSN-compliant issue PDF: `papers/volume_1/issue_2/ijmeer_v1_i2_complete_issue.pdf` (4.64 MB).
  4. Verified 100% ISSN compliance checklist items (E-ISSN 3139-6003, Publisher Meer Foundation address, Editor-in-Chief, Editorial Board, Peer Review statement, Open Access statement, TOC, Editorial Desk message, page numbers, references).
  5. Updated `data/issues.json`, `archive.html`, and `sitemap.xml` with complete issue PDF link.
- **Reason:** Provide single complete PDF issue package for Volume 1, Issue 2 for physical printing, archiving, and library distribution.
- **Files:** `papers/volume_1/issue_2/ijmeer_v1_i2_complete_issue.pdf`, `data/issues.json`, `archive.html`, `sitemap.xml`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Build ISSN-compliant Volume 1, Issue 2 complete issue package with cover, title page, editorial, TOC, and 15 articles`

### 2026-08-05 — Update Volume 1, Issue 2 DOI: 10.5281/zenodo.21809155
- **Changed:**
  1. Updated `data/papers.json` — added `"doi": "10.5281/zenodo.21809155"` to all 15 Volume 1, Issue 2 article objects.
  2. Updated `data/issues.json` — added `"doi": "10.5281/zenodo.21809155"` to Issue 2 metadata.
  3. Updated `archive.html` — added clickable DOI link (`10.5281/zenodo.21809155`) to hero metadata, Issue 2 section header, and all 15 article cards.
  4. Updated `journal.html` — added Issue 2 DOI reference in Zenodo Archive card description.
  5. Updated 15 article HTML pages (`article-v1i2p01.html` through `article-v1i2p15.html`) — added `<meta name="citation_doi">` Google Scholar tag, JSON-LD `identifier` and `sameAs` properties, sub-header DOI link, sidebar table DOI row, and updated citation box.
- **Reason:** Integrate official Zenodo release DOI `10.5281/zenodo.21809155` for Volume 1, Issue 2 across the website.
- **Files:** `data/papers.json`, `data/issues.json`, `archive.html`, `journal.html`, `article-v1i2p01.html` to `article-v1i2p15.html`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Update Volume 1, Issue 2 DOI: 10.5281/zenodo.21809155`

### 2026-08-05 — Publish Volume 1, Issue 2 with 15 articles
- **Changed:**
  1. Extracted article metadata from `Vol1_Issue2.pdf` (70 pages) and `Vol1_Issue2.docx` — parsed 15 articles with titles, authors, affiliations, abstracts, keywords, and page ranges.
  2. Split source PDF into 15 individual article PDFs placed in `papers/volume_1/issue_2/` (`ijmeer_v1_i2_p01_2026.pdf` to `ijmeer_v1_i2_p15_2026.pdf`).
  3. Generated 15 individual article HTML landing pages (`article-v1i2p01.html` to `article-v1i2p15.html`) with complete Highwire Press Google Scholar meta tags, Open Graph/Twitter Card tags, JSON-LD ScholarlyArticle structured data, CC BY-NC 4.0 license badges, and citation formatting.
  4. Updated `data/papers.json` with 15 new article entries (total: 20 papers).
  5. Updated `data/issues.json` with Volume 1, Issue 2 entry (id: 2, quarter: April–June, publication_date: July 2026).
  6. Updated `archive.html`: new hero section for Vol 1 Issue 2 (15 articles), 15 article cards with abstracts, Vol 1 Issue 1 moved to previous release section, JSON-LD schema graph updated.
  7. Updated `sitemap.xml` with 30 new URLs (15 article HTML pages + 15 PDF files), all lastmod dates updated to 2026-08-05.
  8. `citations.html` loads dynamically from `data/papers.json` — no manual update needed, automatically shows all 20 articles.
- **Reason:** Publish Volume 1, Issue 2 (April–June 2026) following the established 10-step publication workflow.
- **Articles Published (15):**
  1. Implementation of the Prohibition of Child Marriage Act, 2006 in Rural Rajasthan (Dr. Ramesh Kumar & Sunita Sharma) — Law
  2. Prevalence and Determinants of Anaemia Among Adolescent Girls in Tribal Districts of Chhattisgarh (Dr. Sunita Verma & Kavita Sahu) — Public Health
  3. Digital Financial Inclusion and Financial Literacy Among Rural Women in North Odisha (Dr. Anupam Sahoo & Dr. Bijay Kumar Swain) — Economics
  4. Academic Stress and Coping Strategies Among Undergraduate Students in Marathwada (Dr. Meena Kulkarni) — Psychology
  5. Impact of Organic Farming Practices on Soil Health in Western Uttar Pradesh (Dr. Ramesh Yadav & Manju Devi) — Agriculture
  6. Water Quality Assessment of Urban Lakes in Bhopal (Dr. Shyam Sundar Patel) — Environmental Science
  7. Effectiveness of Activity-Based Learning in Primary Schools of Odisha (Sudha Panda & Dr. Bijaya Kumar Sahoo) — Education
  8. Social Exclusion and Marginalisation of Scheduled Castes in Semi-Urban Bihar (Dr. Renu Devi) — Sociology
  9. Financial Inclusion Through Self-Help Groups in North Karnataka (Dr. Shobha Patil & Rekha Hadimani) — Economics
  10. Corporate Social Responsibility Practices of SMEs in Tirunelveli (Dr. K. Muthuvel) — Management
  11. Comparative Analysis of Machine Learning Algorithms for Crop Disease Detection (Dr. Anoop Kumar Sharma & Dr. James Osei 🇬🇭) — Computer Science
  12. Synthesis and Characterisation of Zinc Oxide Nanoparticles (Dr. Fatima Begum & Dr. Nguyen Van Minh 🇻🇳) — Physics
  13. Green Synthesis of Silver Nanoparticles Using Hibiscus rosa-sinensis (Dr. Mary Joseph & Sr. Anitha Thomas) — Chemistry
  14. Postcolonial Identity and Hybrid Consciousness in Arundhati Roy (Dr. Deepa Rani) — English Literature
  15. Social Media and Political Mobilisation Among Youth Voters in Gujarat (Harshad Trivedi & Dr. Maria Elena Santos 🇵🇭) — Mass Communication
- **International Authors:** 3 (Dr. James Osei — Ghana, Dr. Nguyen Van Minh — Vietnam, Dr. Maria Elena Santos — Philippines)
- **Files:** `papers/volume_1/issue_2/ijmeer_v1_i2_p01_2026.pdf` to `ijmeer_v1_i2_p15_2026.pdf`, `article-v1i2p01.html` to `article-v1i2p15.html`, `data/papers.json`, `data/issues.json`, `archive.html`, `sitemap.xml`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `add: Volume 1 Issue 2 with 15 articles following established publication workflow`

### 2026-08-02 — Fix CDN usage: ensure all static assets are served via Cloudflare
- **Changed:** Downloaded and localized Creative Commons CC BY-NC 4.0 license badge (`assets/images/logo/cc-by-nc-4.0.png`). Replaced all external `https://licensebuttons.net/l/by-nc/4.0/88x31.png` image URLs across 9 HTML pages (`open-access.html`, `open-access-options.html`, `journal.html`, `authors.html`, `article-v1i1p01.html` through `article-v1i1p05.html`) and `assets/js/components.js` footer with relative paths (`assets/images/logo/cc-by-nc-4.0.png`).
- **Reason:** Resolve SEO Site Checkup issue ("This webpage is not serving all resources from CDNs"). Ensuring all static assets are relative paths guarantees they are served through Cloudflare CDN on `ijmeer.com`.
- **Files:** `open-access.html`, `open-access-options.html`, `journal.html`, `authors.html`, `article-v1i1p01.html` to `article-v1i1p05.html`, `assets/js/components.js`, `assets/images/logo/cc-by-nc-4.0.png`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Fix CDN usage: ensure all static assets are served via Cloudflare`

### 2026-08-02 — Fix Yoga Kutumb text in Dr. Mukti Chauhan's profile
- **Changed:** Fixed typo in Dr. Mukti Chauhan's biography in `editorial-portfolio.html` ("Yoga Kutumb Intuitive" → "Yoga Kutumb Initiative").
- **Reason:** User directive to correct text.
- **Files:** `editorial-portfolio.html`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Fix Yoga Kutumb Intuitive to Yoga Kutumb Initiative`

### 2026-08-01 — Update Dr. Mukti Chauhan biography on editorial portfolio page
- **Changed:** Updated Dr. Mukti Chauhan's biography section in `editorial-portfolio.html` with her full biography detailing her 10 years of yoga & wellness work, Bharatiya Yogini Sangh membership, Yoga Sansad appointment, Mukti Mantra Yoga Kendra AIIMS services, awards (MP Gaurav Ratna, State Yogini, Mahila Audyogik), social initiatives (Madad Foundation, Saket Nari Shakti Sangh), and Meer Foundation Yoga Kutumb coordination.
- **Reason:** User request to replace brief bio with full biography.
- **Files:** `editorial-portfolio.html`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Update Dr. Mukti Chauhan biography on editorial portfolio page`

### 2026-08-01 — Add Dr. Mukti Chauhan to Advisory Board
- **Changed:**
  1. Converted `dr mukti chauhan.png` from Downloads to `images/editorial/dr-mukti-chauhan.webp`.
  2. Added Dr. Mukti Chauhan card to Advisory Board section in `editorial-board.html` (after Dr. Anupama Patel).
  3. Added Dr. Mukti Chauhan detailed profile, tab switching, quick-nav pill, and scroll-spy entry in `editorial-portfolio.html`.
  4. Updated `EDITORIAL_BOARD.md` master list (total members: 16).
  5. Added rule enforcing "Yog" = "Yoga" across all site content in `CONTENT_RULES.md` and `MEMORY.md`.
- **Reason:** User request to add Dr. Mukti Chauhan to Advisory Board with exact display formatting and Yog=Yoga rule.
- **Files:** `editorial-board.html`, `editorial-portfolio.html`, `images/editorial/dr-mukti-chauhan.webp`, `EDITORIAL_BOARD.md`, `CONTENT_RULES.md`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Add Dr. Mukti Chauhan to Advisory Board`

### 2026-07-30 — Fix remaining Turkish characters for Ayşegül Akkaya
- **Changed:** Fixed remaining broken Turkish characters for Lect. Ayşegül Akkaya in `editorial-board.html` and `editorial-portfolio.html` (`AYÅžEGÃœL` → `AYŞEGÜL`, `Ä°stanbul` → `İstanbul`, `BeyazÄ±t` → `Beyazıt`).
- **Reason:** Resolve UTF-8 encoding issues for Lect. Ayşegül Akkaya per user directive.
- **Files:** `editorial-board.html`, `editorial-portfolio.html`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Fix remaining Turkish characters for Ayşegül Akkaya`

### 2026-07-29 — Fix UTF-8 encoding issues: Turkish characters in editorial board pages
- **Changed:** Fixed 11 instances of broken Turkish characters (`Ayşegül` and `ğ`) across `editorial-board.html` and `editorial-portfolio.html`.
- **Reason:** Resolve remaining encoding artifacts flagged in the UTF-8 audit report.
- **Files:** `editorial-board.html`, `editorial-portfolio.html`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Fix UTF-8 encoding issues: Turkish characters in editorial board pages`

### 2026-07-29 — UTF-8 encoding audit report
- **Changed:** Ran a full UTF-8 encoding scan across all 45 HTML files in the project. Verified `<meta charset="UTF-8">` is present on all files. Identified 11 remaining localized mojibake issues affecting Turkish characters (ş, ğ) in `editorial-board.html` and `editorial-portfolio.html`. Generated `UTF8_AUDIT_REPORT.md` with findings. No files were modified.
- **Reason:** User requested a complete UTF-8 encoding audit without making changes.
- **Files:** `UTF8_AUDIT_REPORT.md`, `MEMORY.md`
- **Commit:** `UTF-8 encoding audit report`

### 2026-07-29 — Security Audit and Recommendations Report
- **Changed:** Generated comprehensive safety and security recommendations report (`SECURITY_AUDIT.md`), analyzing Security Headers, Cloudflare features, GitHub Pages configurations, Form submissions, GDPR compliance, Spam prevention, and Backup strategies. Categorized into High, Medium, and Low priorities. No changes made to the live website files.
- **Reason:** User request for a complete security and safety audit.
- **Files:** `SECURITY_AUDIT.md`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Security audit and recommendations report`

### 2026-07-29 — Fix UTF-8 encoding errors (broken emojis) across all HTML files
- **Changed:**
  1. Fixed all remaining UTF-8 double-encoding artifacts (mojibake) across 10 HTML files, including `journal.html`, `editorial-portfolio.html`, `editorial-board.html`, `archive.html`, `peer-review.html`, etc.
  2. Reversed CP1252 misinterpretations at the byte level to correctly restore original Unicode emojis (e.g., 🔬, 🏥, ⚙️, 🌐).
- **Reason:** Resolve broken emojis resulting from encoding errors (mojibake) requested by the user.
- **Files:** `archive.html`, `authors.html`, `citations.html`, `editorial-board.html`, `editorial-portfolio.html`, `index.html`, `journal.html`, `peer-review.html`, `privacy-policy.html`, `rights-permissions.html`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Fix UTF-8 encoding errors (broken emojis) on journal.html`

### 2026-07-29 — Migrate license from CC BY 4.0 to CC BY-NC 4.0 site-wide
- **Changed:**
  1. Added CC BY-NC 4.0 license badge, text, and full notice section to all 5 published articles (`article-v1i1p01.html` through `article-v1i1p05.html`).
  2. Updated `open-access.html` — replaced all CC BY 4.0 references with CC BY-NC 4.0 (badge, text, links, meta tags).
  3. Updated `open-access-options.html` — replaced all CC BY 4.0 references with CC BY-NC 4.0 (badge, text, links, meta tags).
  4. Updated `journal.html` — replaced CC BY 4.0 text and links with CC BY-NC 4.0.
  5. Updated `authors.html` — replaced CC BY 4.0 references in publishing agreement section and copyright badge with CC BY-NC 4.0.
  6. Updated `policies.html` — changed Open Access Policy and Rights & Permissions card descriptions from CC BY 4.0 to CC BY-NC 4.0.
  7. Updated `publication-process.html` — changed Copyright Agreement step from CC BY 4.0 to CC BY-NC 4.0.
  8. Updated `research-transparency.html` — changed FAIR Accessible card from CC BY 4.0 to CC BY-NC 4.0.
  9. Updated `rights-permissions.html` — changed meta description, og:description, and twitter:description from CC BY 4.0 to CC BY-NC 4.0.
  10. Updated `index.html` — changed credibility badge text and all 3 JSON-LD structured data license URLs from CC BY 4.0 to CC BY-NC 4.0.
  11. Updated `CONTENT_RULES.md`, `POST_ISSN_ROADMAP.md`, and `MEMORY.md` documentation files.
- **Reason:** Align all license references to CC BY-NC 4.0 (Attribution-NonCommercial) per publisher decision. All old CC BY 4.0 references and URLs verified eliminated.

### 2026-07-28 — Fix page redirect issues for Google Search Console validation
- **Changed:**
  1. Fixed 9 stub HTML pages (`about-this-journal.html`, `abstracting-indexing.html`, `book-reviews.html`, `fees-pricing.html`, `metrics.html`, `post-publication-impact.html`, `preparing-materials.html`, `publishing-agreement.html`, `submitting-materials.html`) that had "Redirecting..." titles causing Google Search Console "Page with redirect" validation errors.
  2. Added `<meta name="robots" content="noindex, follow">` to all 9 stubs to tell Google to stop indexing them.
  3. Added proper `<meta http-equiv="refresh" content="0; url=...">` for clean instant redirects.
  4. Replaced "Redirecting..." titles with proper descriptive titles (e.g., "About This Journal | IJMEER").
  5. Removed orphaned BreadcrumbList JSON-LD schema from `fees-pricing.html` and `abstracting-indexing.html`.
  6. Verified: no stub pages are in `sitemap.xml`, no internal links point to stub pages.
- **Reason:** Resolve Google Search Console "Page with redirect" validation issue (2 pages flagged).
- **Files:** `about-this-journal.html`, `abstracting-indexing.html`, `book-reviews.html`, `fees-pricing.html`, `metrics.html`, `post-publication-impact.html`, `preparing-materials.html`, `publishing-agreement.html`, `submitting-materials.html`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Fix page redirect issues for Google Search Console validation`

### 2026-07-28 — Create individual article pages and fix Google Scholar indexing issues
- **Changed:**
  1. Created 5 dedicated HTML landing pages (`article-v1i1p01.html` through `article-v1i1p05.html`) for all published articles with complete Highwire Press citation meta tags (`citation_title`, `citation_author`, `citation_publication_date`, `citation_journal_title`, `citation_volume`, `citation_issue`, `citation_firstpage`, `citation_lastpage`, `citation_pdf_url`, `citation_abstract`, `citation_issn`, `citation_language`) and canonical links.
  2. Removed stacked per-article citation meta tags from `index.html`, `archive.html`, and `citations.html` to prevent crawler ambiguity.
  3. Cleaned up `sitemap.xml`: removed legacy `/pdfs/` links, added new `article-v1i1p0*.html` page URLs (priority 0.8), and updated `/papers/*.pdf` URLs (priority 0.7).
  4. Linked article cards in `archive.html` to their respective dedicated article HTML pages.
- **Reason:** Implement all structural requirements for Google Scholar indexing readiness.
- **Files:** `article-v1i1p01.html`, `article-v1i1p02.html`, `article-v1i1p03.html`, `article-v1i1p04.html`, `article-v1i1p05.html`, `index.html`, `archive.html`, `citations.html`, `sitemap.xml`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Create individual article pages and fix Google Scholar indexing issues`

### 2026-07-28 — Google Scholar indexing audit report
- **Changed:** Conducted full audit of Google Scholar indexing readiness. Identified missing dedicated per-article landing pages, incorrect `citation_pdf_url` paths in `citations.html`, missing `citation_abstract` and `citation_doi` tags, and unindexed status in Google search/Scholar.
- **Reason:** User request for Google Scholar readiness audit (analysis only).
- **Files:** `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Google Scholar indexing audit report`

### 2026-07-28 — Remove hero tagline and adjust landing page spacing
- **Changed:** Removed hero tagline paragraph (`.hero-desc`) from `index.html` and adjusted subtitle margin-bottom to `32px` for balanced vertical alignment with CTA action buttons.
- **Reason:** User request to remove hero tagline and maintain clean landing page spacing.
- **Files:** `index.html`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Remove hero tagline and adjust landing page spacing`

### 2026-07-28 — Update quarterly publication dates across all pages and automation logic
- **Changed:**
  1. Audited all date references across HTML, JS, JSON, and documentation files.
  2. Updated `assets/js/timeline.js` Q1 publication label from `April 25–31` to `April 25–30` (matching the 30-day length of April).
  3. Standardized all 4 quarterly issue publication windows:
     - Issue 1 (Jan–Mar): 25–30 April
     - Issue 2 (Apr–Jun): 25–31 July
     - Issue 3 (Jul–Sep): 25–31 October
     - Issue 4 (Oct–Dec): 25–31 January
  4. Updated publication frequency cards in `journal.html` and publication date detail fields in `call-for-papers.html`.
- **Reason:** Standardize exact publication date windows across static HTML, JS timeline logic, JSON configuration, and documentation.
- **Files:** `assets/js/timeline.js`, `journal.html`, `call-for-papers.html`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Update quarterly publication dates across all pages and automation logic`

### 2026-07-28 — Remove APC timing statements and Print ISSN references
- **Changed:**
  1. Removed all APC timing statements ("APC payable only after final acceptance", "Pay before publication", "Pay only after acceptance") across all pages (`index.html`, `journal.html`, `authors.html`, `peer-review.html`, `open-access.html`). Fee structures now display without timing info.
  2. Removed all references to Print ISSN (`Print ISSN: Applied For`, `P-ISSN: XXXX-XXXX`) from `index.html`, `journal.html`, `contact.html`, `assets/js/components.js`, and `data/config.json`. Only Online ISSN (`E-ISSN: 3139-6003`) is displayed.
- **Reason:** User request to eliminate all APC timing and Print ISSN mentions across the website.
- **Files:** `index.html`, `journal.html`, `contact.html`, `authors.html`, `peer-review.html`, `open-access.html`, `assets/js/components.js`, `data/config.json`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Remove APC timing statements and Print ISSN references`

### 2026-07-28 — Fix all issues identified in IJMEER homepage audit
- **Changed:**
  1. Fixed all UTF-8 double-encoding artifacts across homepage (`4×`, `📄`, `→`, `✅`, `⏱`, `📢`, `📚`, `📅`, `📖`, `↗`).
  2. Removed `P-ISSN: XXXX-XXXX` fake ISSN from homepage and footer, replacing with `Print ISSN: Applied For` while keeping valid `E-ISSN: 3139-6003`.
  3. Removed misleading claims: removed "100% Digital Indexing", removed "from 50+ countries", conditionally hid "0 citations" badge on articles, and updated metrics section title to "IJMEER Journal Statistics & Editorial Performance".
  4. Added missing credibility badges: Open Access, Double-Blind Peer Review, DOI for Every Article, ORCID Supported, CC BY-NC 4.0 License.
  5. Updated footer publisher line in `components.js` to `Published by Meer Foundation (Registered Non-Profit Organization)`.
  6. Updated hero tagline to: "An international, peer-reviewed, open-access journal dedicated to publishing high-quality multidisciplinary research that advances scholarship, innovation, and evidence-based practice across diverse academic fields."
  7. Updated metrics section cards to showcase stable statistics (Founded: 2026, Frequency: Quarterly, Review Model: Double-Blind, Access: Open Access).
  8. Updated Benefits section (`why-publish`): renamed to "Timely Peer Review and Publication", "Research Impact & Discoverability" ("Increase the accessibility and visibility of your published research"), and "Transparent Article Processing Charges".
  9. Standardized APC statements across homepage to "APC payable only after final acceptance."
- **Reason:** Resolve all compliance, accuracy, and presentation issues identified in the IJMEER homepage audit.
- **Files:** `index.html`, `assets/js/components.js`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Fix homepage issues: encoding errors, remove fake ISSN, misleading claims, add missing credibility badges`

### 2026-07-27 — Remove Media Kit page and all related files
- **Changed:** Verified deletion of `media-kit.html` and `/media-kit/` directory. Removed "Media Kit" footer link from `assets/js/components.js`.
- **Reason:** User request to completely remove Media Kit page and all related files.
- **Files:** `assets/js/components.js`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `Remove Media Kit page and all related files`

### 2026-07-23 - Address all SEO Site Checkup issues & indexing optimizations
- **Changed:**
  1. Eliminated render-blocking resources: loaded Google Fonts asynchronously with `media="print" onload="this.media='all'"` and preconnect tags, preloaded `assets/css/style.css`, and set `async` attribute on Google Tag Manager scripts across all HTML files.
  2. Fixed character encoding anomalies: replaced all double-encoded UTF-8 artifacts (`Â·`, `â€“`, etc.) with standard HTML entities (`&middot;`, `&ndash;`, etc.) to resolve malformed encoding warnings and eliminate CLS layout shifts.
  3. Obfuscated plaintext email addresses across HTML source code into HTML entities to protect against spam harvesters while preserving full clickability and copy-to-clipboard functionality.
  4. Expanded JSON-LD Structured Data Schema: injected `ScholarlyArticle` schemas for featured articles (with DOI placeholders and reference list citations), `ItemList`/`EditorialBoard` bios schema, `ScholarlyJournal` indexing properties, and `BreadcrumbList` schemas across all inner pages to boost AI Visibility and Google Rich Results.
  5. Created `ads.txt` at root to validate non-commercial open access journal ad policy.
  6. Updated `sitemap.xml` `lastmod` timestamps to `2026-07-23`.
- **Reason:** Resolve HIGH, MEDIUM, and WARNING issues from latest SEO Site Checkup report.
- **Files:** `*.html` (31 files), `ads.txt`, `sitemap.xml`, `MEMORY.md`, `CURRENT_TASK.md`
- **Commit:** `SEO optimization: address all issues identified in Site Checkup report`

### 2026-07-18  Fix 'Page with redirect' indexing issue (2 pages)
- **Changed:** Removed <meta http-equiv="refresh"> and window.location.replace() from 9 placeholder redirect HTML files (including the 2 flagged by GSC). Updated all internal links across 10 HTML files that pointed to these redirects to point directly to their final destination anchors (e.g., journal.html#about). Regenerated sitemap.xml with the current date.
- **Reason:** Resolve Google Search Console CRITICAL ISSUE: "Page with redirect".
- **Files:** *.html (19 files modified), sitemap.xml
- **Commit:** ix: 'Page with redirect' indexing issue (2 pages)

### 2026-07-17 — Fix remaining SEO issues
- **Changed:** Eliminated render-blocking Google Fonts by moving them from CSS `@import` to HTML `<head>` preloads across all pages. Added `srcset` and `alt` attributes to logo images in JS. Encoded three plaintext emails in footer using HTML entities. Upgraded three `target="_blank"` links to include `rel="noopener noreferrer"`.
- **Reason:** Resolve HIGH, MEDIUM, and WARNING issues from SEO Site Checkup report.
- **Files:** `*.html` (all HTML files), `assets/css/style.css`, `assets/js/components.js`
- **Commit:** `fix: remaining SEO issues (render-blocking resources, image sizing, plaintext emails, cross-origin links)`

### 2026-07-14 — Update Online ISSN
- **Changed:** Replaced "E-ISSN: XXXX-XXXX" placeholder with official Online ISSN "3139-6003" across all HTML files, `components.js`, and `config.json`. Left Print ISSN placeholder intact.
- **Reason:** Online ISSN application approved.
- **Files:** `index.html`, `journal.html`, `citations.html`, `archive.html`, `contact.html`, `assets/js/components.js`, `data/config.json`
- **Commit:** `update: Update Online ISSN: 3139-6003 approved for IJMEER`

### 2026-07-06 — Remove Media Kit system
- **Changed:** Deleted `media-kit.html`, the entire `media-kit/` directory, and all associated GitHub Action workflows (`media-kit-*.yml`). Note: The footer link in `components.js` was never added in previous tasks, so no change was needed there.
- **Reason:** User request to completely remove the Media Kit system.
- **Files:** `media-kit.html`, `media-kit/*`, `.github/workflows/media-kit-*.yml`
- **Commit:** `remove: Media Kit page and all related integrations`

### 2026-07-04 — Generate Website Reverse Engineering Report (Re-run)
- **Changed:** No code modifications made to the core project. Ran an automated Python script to extract directory structure, file inventory, and source code into a single Markdown file.
- **Reason:** User request for a complete technical blueprint of the application (audit report).
- **Files:** Output exported to `C:\Users\hashm\Desktop\RE IJMEER\Website_Reverse_Engineering_Report.md`.
- **Commit:** None (Read-only session).

### 2026-06-30 — Generate Website Reverse Engineering Report
- **Changed:** No code modifications made. Executed a read-only analysis of the entire repository to generate a massive 30-section "Website Reverse Engineering Report".
- **Reason:** User request for a complete technical blueprint of the application.
- **Files:** Output strictly isolated to external directory (`C:\Users\hashm\Desktop\RE IJMEER\Website_Reverse_Engineering_Report.md`).
- **Commit:** None (Read-only session).

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
| **Volume 1 Issue 1** | Published April 2026 (5 articles) | 2026-04-30 |
| **Volume 1 Issue 2** | Published July 2026 (15 articles) | 2026-07-31 |
| **Total Published Articles** | 20 | 2026-08-05 |


