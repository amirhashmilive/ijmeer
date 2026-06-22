# ISSN_COMPLIANCE.md — Full ISSN Requirements

> **ISSN Application ID:** 75192  
> **Submitted to:** ISSN India (National Centre, New Delhi)  
> **Hard copy received:** April 24, 2026  
> **Expected decision:** ~30 working days from April 24, 2026  
> **Application Year:** 2026 (ALL website references must show 2026)

---

## 1. Starting Year — CRITICAL

| Requirement | Value | Status |
|---|---|---|
| Application shows year | **2026** | Fixed ✅ |
| `index.html` founded year | 2026 | Fixed ✅ |
| `about-this-journal.html` starting year | 2026 | Fixed ✅ |
| `journal.html` established year | 2026 | Fixed ✅ |
| `archive.html` Vol 1 Issue 1 date | April 2026 | Fixed ✅ |
| `components.js` footer "Since" | 2026 | Fixed ✅ |
| `editorial-portfolio.html` | 2026 | Fixed ✅ |

> ⚠️ Any reference to 2025 as the founding year will cause ISSN application rejection.

---

## 2. International Editorial Board Members — CRITICAL

**Minimum required:** 2 members from outside India

### Current International Members:

| # | Name | Country | Status |
|---|---|---|---|
| 1 | Dr. Mary Lou Frank | 🇺🇸 USA | ✅ Added |
| 2 | Prof. (Dr.) Jyotirmaya Thakur | 🇬🇧 UK | ✅ Added |

### Required details for EACH international member:

| Field | Dr. Mary Lou Frank | Prof. Jyotirmaya Thakur |
|---|---|---|
| Full Name | ✅ Present | ✅ Present |
| Designation | ✅ Present | ✅ Present |
| Institution | ✅ Present | ✅ Present |
| **Complete Postal Address** | ✅ 100 University Parkway, Macon, GA 31206, USA | ⏳ Verify |
| **Institutional Email** | ⏳ Pending | ⏳ Pending |
| **Institutional Profile Link** | ⏳ Verify | ⏳ Verify |
| Photo | ✅ Present | ✅ Present |

---

## 3. All Editorial Board Members — Required Details

Every member (including Indian members) must have ALL of the following:

| Requirement | Standard |
|---|---|
| Full Name with title | Dr. / Prof. / Adv. prefix required |
| Designation | Exact current job title |
| Institution | Full official name |
| **Institutional Email** | @institution.ac.in or .edu equivalent (not Gmail) |
| **Complete Postal Address** | Street, City, State, PIN, Country |
| ORCID | Recommended (not mandatory) |
| Institutional Profile | Recommended (mandatory for international) |

---

## 4. Publisher Details Requirements

The following MUST appear clearly on the website:

| Field | Required | Status |
|---|---|---|
| Publisher Name | Meer Foundation | ✅ Present |
| Publisher Type | NGO | ✅ Present |
| Publisher Address | Complete postal address | ⏳ Verify completeness |
| Publisher Contact | Email and/or phone | ⏳ Verify |
| **Grievance Officer** | Name + contact details | ⏳ Add (UGC requirement) |
| Editor-in-Chief Name | Dr. Nusrat Ali Hashmi | ✅ Present |
| Editor-in-Chief Contact | Email | ⏳ Pending |

---

## 5. ISSN Placeholder Requirements

Until official ISSN numbers are received:
- Use `XXXX-XXXX` for both Print and Online ISSN
- **DO NOT** use random numbers or leave blank

**Pages requiring ISSN placeholder:**
- [x] `index.html`
- [x] `journal.html`
- [x] `about-this-journal.html`
- [x] `archive.html`
- [x] `editorial-board.html`
- [x] `authors.html`
- [x] Footer (via `components.js`)

---

## 6. Archive Requirements

ISSN evaluators will check the archive. Each article must have:
- [ ] Individual article listing (not just full issue)
- [ ] Author name(s) for each article
- [ ] Article title
- [ ] Page numbers
- [ ] Direct PDF link for each article (not just full issue PDF)
- [ ] DOI (if assigned)

**Current status:** Vol 1 Issue 1 (April 2026) is published. Verify individual article links exist.

---

## 7. Author Guidelines Requirements

The `authors.html` page must contain:
- [x] Manuscript preparation guidelines
- [x] Submission process
- [x] Peer review policy (or link to `peer-review.html`)
- [x] Copyright/licensing information
- [x] Article processing charges (even if ₹0 — state it explicitly)
- [ ] Plagiarism policy
- [x] Reference formatting guidelines
- [x] File format requirements

---

## 8. Peer Review Policy Requirements

The `peer-review.html` page must clearly state:
- [x] Type of peer review (Double-blind)
- [x] Number of reviewers (minimum 2)
- [x] Review timeline
- [x] Review criteria
- [x] Appeal process
- [ ] Reviewer selection criteria

---

## 9. Contact Details Requirements

`contact.html` must include:
- [x] Journal email address
- [x] Publisher name and address
- [ ] Phone number (optional but recommended)
- [ ] Grievance Officer name and contact
- [x] Response time commitment

---

## 10. Website Compliance Checklist

Run this checklist before any ISSN-related submission:

- [ ] Starting year is 2026 everywhere
- [ ] At least 2 international members with full details
- [ ] All board members have institutional email and postal address
- [ ] ISSN placeholders (XXXX-XXXX) on all required pages
- [ ] Archive has individual article links
- [ ] Author guidelines are complete
- [ ] Peer review policy is complete
- [ ] Publisher details are complete
- [ ] Contact page has Grievance Officer info
- [ ] Privacy policy is present and updated
- [ ] No false indexing claims

---

## 11. Post-Approval Actions

When ISSN is received:
1. Update ALL `XXXX-XXXX` placeholders in one atomic commit
2. Add ISSN to `journal.html`, `index.html`, `about-this-journal.html`, `archive.html`, footer
3. Update `MEMORY.md` with date received and ISSN numbers
4. Begin DOAJ submission process (see `POST_ISSN_ROADMAP.md`)
5. Commit: `update: add official ISSN [XXXX-XXXX (print)] [XXXX-XXXX (online)]`
