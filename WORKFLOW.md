# WORKFLOW.md — Standard Operating Procedures

---

## SOP 1: Adding a New Editorial Board Member

### Required Information (collect BEFORE starting)
- [ ] Full name (with title: Dr./Prof./Adv.)
- [ ] Designation (exact job title)
- [ ] Institution name (exact official name)
- [ ] Institutional email address
- [ ] Complete postal address (Street, City, State, PIN/ZIP, Country)
- [ ] ORCID iD (format: XXXX-XXXX-XXXX-XXXX)
- [ ] Institutional profile URL
- [ ] Profile photo (minimum 400×400px, clear face photo)
- [ ] Short biography (100–400 words)
- [ ] Areas of expertise (5–10 keywords)
- [ ] Notable achievements (3–5 bullet points)
- [ ] Role category: Editorial Board / International Board / Advisory Board

### Steps

**Step 1: Prepare the image**
```powershell
# Convert image to WebP and create srcset variants
# Place originals in appropriate images/ subfolder
# Naming: firstname-lastname.webp
# Create: -200w.webp, -400w.webp, -800w.webp variants
```

**Step 2: Add to `editorial-board.html`**
- Find the correct section (Editorial Board / International / Advisory)
- Add member card following existing member format
- Include: name, designation, institution, email, address, ORCID, photo

**Step 3: Add to `editorial-portfolio.html`**
- Add a full `profile-section` block with ID matching the anchor
- Follow the standard profile structure (see Ashok Sunatkari as reference):
  - `profile-card-accent` (use correct accent class)
  - `profile-top` (photo + identity side by side)
  - `profile-divider`
  - `profile-tab-bar` (Biography, Expertise, Achievements, Profile Links)
  - `ptab-panel` blocks for each tab
- Add member to the scroll-spy `sections` array in the page's `<script>`
- Add nav pill to the `.pnav` navigation strip

**Step 4: Update navigation pills in `editorial-portfolio.html`**
```javascript
// In the sections array:
{ id: 'member-id', pill: 'pill-N' }
```

**Step 5: Verify**
- [ ] Photo displays correctly (circular)
- [ ] Profile card is horizontal (image left, content right)
- [ ] All tab panels work (Biography, Expertise, etc.)
- [ ] Scroll-spy highlights correct pill
- [ ] Email copy button works
- [ ] ORCID link is correct
- [ ] Institutional profile link works

**Step 6: Commit**
```
add: [Member Name] to editorial board with profile image
```

---

## SOP 2: Fixing ISSN Compliance Issues

### Before making changes, read:
- `ISSN_COMPLIANCE.md` — full requirements
- `EDITORIAL_BOARD.md` — member details

### Common fixes:

**Year mismatch (2025 vs 2026)**
- Search all HTML files for "2025" in context of founding/establishment
- Change ONLY: "Founded: 2025", "Established 2025", "Since 2025", "Starting year: 2025"
- Do NOT change: author publication years, citation years, copyright years unrelated to founding

**Missing international member details**
- Open `editorial-board.html` and `editorial-portfolio.html`
- For each international member, ensure ALL of these are present:
  - Full Name ✓
  - Designation ✓
  - Institution ✓
  - Complete Postal Address ✓
  - Institutional Email ✓
  - Institutional Profile Link ✓

**Missing ISSN placeholders**
- Search for `XXXX-XXXX` — should appear on: index, journal, about, archive, editorial-board, authors pages
- If actual ISSN received: replace ALL instances simultaneously

**Commit format:**
```
fix: [specific issue] for ISSN compliance
```

---

## SOP 3: Updating Existing Content

### Text content updates
1. Identify the file and exact line number
2. Make only the targeted change
3. Verify surrounding content is untouched
4. Commit: `update: [what was changed]`

### Adding a new page section
1. Follow existing section markup exactly
2. Use only existing CSS classes — no new inline styles
3. Maintain consistent heading hierarchy (h2 → h3 → h4)
4. Commit: `add: [section name] to [page name]`

### Updating fees/pricing
1. Edit `fees-pricing.html` ONLY
2. Verify INR pricing for Indian authors, USD for international
3. No mention of GST, tax, or fast track
4. Commit: `update: publication fees`

---

## SOP 4: Handling Social Media Posts

See `SOCIAL_MEDIA.md` for full details.

### Quick reference:
1. Identify post type (CfP, new issue, board member spotlight, etc.)
2. Use the appropriate template from `SOCIAL_MEDIA.md`
3. Brand voice: Professional, academic, accessible
4. Include: IJMEER branding, relevant hashtags, call to action
5. Schedule according to posting calendar

---

## SOP 5: Updating the Archive (New Issue)

When a new issue is published:

1. **Create paper pages** in `/papers/` directory (one HTML per article)
2. **Create PDF files** in `/pdfs/` directory (one PDF per article)
3. **Update `archive.html`:**
   - Add new issue card at the TOP of the list
   - Include: Volume, Issue, Month-Year, article count
   - Link each article individually (not just the full issue)
4. **Update `index.html`:**
   - Update "Latest Issue" section stats
   - Update article count if shown
5. **Update `sitemap.xml`:** Add new page URLs
6. **Verify** all PDF links work before committing
7. **Commit:** `add: Vol [N] Issue [N] [Month Year] to archive`

---

## SOP 6: Deployment After Changes

See `DEPLOYMENT.md` for full details.

### Quick steps:
```powershell
# 1. Stage changes
git add [files]

# 2. Commit
git commit -m "[action]: [description]"

# 3. Push
git push origin HEAD:main

# 4. Wait 2-3 minutes for GitHub Pages to rebuild

# 5. Verify at https://www.ijmeer.com
```

---

## SOP 7: Running a Backup

```powershell
# Navigate to project directory
cd "D:\DRIVE (Ai) Agents\00 Projects\Workplace IJMEER"

# Run backup script
.\backup.ps1 -CommitMessage "description of current state"
```

See `BACKUP.md` for full details.
