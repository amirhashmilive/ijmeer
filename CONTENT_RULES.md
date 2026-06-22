# CONTENT_RULES.md — Content Policies

---

## 1. Prohibited Content (NEVER USE)

### Language / Terminology

| ❌ Prohibited | ✅ Use Instead | Reason |
|---|---|---|
| "Gold Open Access" | "Open Access" or "Diamond Open Access" | Incorrect terminology for this journal's model |
| "Fast Track" | — | Not offered; creates false expectations |
| "Express Publication" | — | Not offered |
| "Guaranteed Acceptance" | — | Misleading and unethical |
| "Scopus Indexed" | — | Only after official indexing |
| "UGC Care Listed" | — | Only after official listing |
| "Impact Factor: X.X" | — | Only after official assignment |
| "GST" / "Service Tax" / "VAT" | — | Not to be mentioned anywhere |
| Jokes, slang, casual phrases | Formal academic language | Brand voice must remain professional |
| First-person plural ("we are great") | Third-person or neutral | Avoid self-promotion without evidence |

### Pricing Rules

| Author Type | Currency | Rule |
|---|---|---|
| **Indian authors** | INR (₹) only | Never show USD to Indian authors |
| **International authors** | USD ($) | Standard international pricing |
| **Current model** | Free (Diamond OA) | No APC currently charged |

> ⚠️ If pricing changes, update `fees-pricing.html` ONLY. Do not add GST or any tax line.

---

## 2. Required Content

### Every page MUST have:
- [ ] Correct page `<title>` tag
- [ ] Meta description
- [ ] OG tags (og:title, og:description, og:image, og:url)
- [ ] Canonical URL
- [ ] IJMEER branding in header (via components.js)
- [ ] Footer with contact info and "Since 2026" (via components.js)

### Key pages MUST include:
| Page | Required Elements |
|---|---|
| **Homepage** | ISSN placeholder, submission CTA, current issue info |
| **Journal page** | Founded 2026, ISSN XXXX-XXXX, publisher details |
| **Editorial Board** | All 13 members with full details |
| **Authors page** | Complete submission guidelines, peer review timeline |
| **Archive** | Individual article links (not just full issue PDF) |
| **Contact** | Publisher address, email, Grievance Officer details |
| **Privacy Policy** | Complete, legally sound, updated date |
| **Peer Review** | Full double-blind peer review policy |

---

## 3. Editorial Board Content Requirements

For **every editorial board member**, ALL of the following MUST be present:

| Field | Required? | Notes |
|---|---|---|
| Full Name (with title) | ✅ Mandatory | Dr./Prof./Adv. prefix |
| Designation | ✅ Mandatory | Exact job title |
| Institution | ✅ Mandatory | Full official institution name |
| Institutional Email | ✅ Mandatory | @institution.ac.in or equivalent |
| Complete Postal Address | ✅ Mandatory | Street, City, State, PIN, Country |
| ORCID iD | ⭐ Strongly recommended | Format: 0000-0000-0000-0000 |
| Institutional Profile URL | ⭐ Strongly recommended | Direct link to faculty page |
| Profile Photo | ✅ Mandatory | WebP, minimum 200×200px |
| Biography | ✅ Mandatory | 100–400 words |

For **international members specifically**, ISSN requires:
- Complete postal address with country
- Institutional profile link (publicly accessible)
- Institutional email (not Gmail/Yahoo)

---

## 4. Publisher Details (Must Appear on Website)

| Field | Value |
|---|---|
| **Publisher Name** | Meer Foundation |
| **Publisher Type** | Non-Governmental Organization (NGO) |
| **Address** | Raipur, Chhattisgarh, India *(complete address to be confirmed)* |
| **Contact Email** | *(to be confirmed)* |
| **Grievance Officer** | *(to be confirmed — required by UGC guidelines)* |

---

## 5. ISSN Placeholders

Until ISSN numbers are officially assigned, use:
- Print ISSN: `XXXX-XXXX`
- Online ISSN: `XXXX-XXXX`

**Pages that MUST show ISSN placeholder:**
- index.html
- journal.html
- about-this-journal.html
- archive.html
- editorial-board.html
- authors.html
- footer (via components.js)

**When ISSN is received:**
1. Replace ALL `XXXX-XXXX` placeholders in one commit
2. Update MEMORY.md with date received
3. Commit: `update: add official ISSN numbers [XXXX-XXXX and XXXX-XXXX]`

---

## 6. Tone and Voice

### Brand Voice Principles

| Principle | Description |
|---|---|
| **Professional** | Use formal academic language always |
| **Authoritative** | Confident, evidence-based statements |
| **Accessible** | Clear language; avoid unnecessary jargon |
| **Inclusive** | Gender-neutral, globally accessible |
| **Honest** | No false claims, no puffery |

### Writing Style Rules
- Use third person for the journal ("IJMEER aims to..." not "We aim to...")
- Use Oxford comma
- Spell out numbers below ten (except in data/tables)
- Use "peer-reviewed" (hyphenated)
- Use "open access" (no hyphen unless adjective: "open-access journal")
- Use "manuscript" not "paper" in author-facing content
- Use "article" not "paper" in reader-facing content

---

## 7. Copyright and Attribution

- All published articles carry a **CC BY 4.0** license unless otherwise stated
- Authors retain copyright
- IJMEER retains right of first publication
- Do not remove author names or affiliations from any published content
- Citation format: APA 7th Edition (default)

---

## 8. Image Content Rules

- All editorial board photos must be **professional headshots**
- No AI-generated faces for real people
- No stock photos for board members
- Watermarks: Journal logo watermark is acceptable on promotional images
- All images must have descriptive alt text
- Privacy: Do not use someone's photo without their consent

---

## 9. Accessibility Requirements

- All images: meaningful `alt` text
- All buttons: `aria-label` when icon-only
- All tabs: `role="tab"` and `aria-selected`
- All forms: associated `<label>` elements
- Color contrast: minimum 4.5:1 for body text, 3:1 for large text
- Do not rely on color alone to convey information
