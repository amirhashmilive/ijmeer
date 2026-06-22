# REMINDERS.md — Active Reminders & Status

> **Agents: Check this file at the start of each session for time-sensitive items.**  
> Update status as items are completed.

---

## 🔴 Critical / Time-Sensitive

| # | Reminder | Deadline | Status | Notes |
|---|---|---|---|---|
| 1 | **ISSN Decision Expected** | ~June 2026 | ⏳ Waiting | Hard copy submitted April 24, 2026. ~30 working days. Check with ISSN India if no response by mid-June. |
| 2 | **Fix starting year to 2026** | Before ISSN decision | ✅ Done (2026-06-22) | All pages now show 2026. Commit: `d7ecb8f` |
| 3 | **International members ≥ 2 with full details** | Before ISSN decision | 🔄 Partial | Members added, but some details incomplete (emails, verified addresses) |

---

## 🟡 High Priority

| # | Reminder | Target | Status | Notes |
|---|---|---|---|---|
| 4 | **Add institutional emails for EIC and ME** | ASAP | ⏳ Pending | Dr. Nusrat Ali Hashmi and Sayed Amir Mustafa Hashmi need @institution email addresses |
| 5 | **Complete postal addresses for all members** | ASAP | ⏳ Pending | Some members missing full street address. See `EDITORIAL_BOARD.md` |
| 6 | **International member institutional emails** | Before ISSN decision | ⏳ Pending | Dr. Mary Lou Frank (need @mga.edu email), Prof. Thakur (need UK institutional email) |
| 7 | **Individual article PDF links in archive** | Before ISSN evaluation | ⏳ Pending | Archive currently may only have full-issue PDFs. Each article needs its own link. |

---

## 🟢 Normal Priority

| # | Reminder | Target | Status | Notes |
|---|---|---|---|---|
| 8 | **Google indexing progress** | Ongoing | 🔄 In Progress | 7 pages indexed / 27 discovered (as of 2026-06-22). Submit sitemap via GSC if not done. |
| 9 | **Add Grievance Officer details** | Before UGC Care application | ⏳ Pending | Required by UGC guidelines. Add to `contact.html`. |
| 10 | **Verify all ORCID links work** | When convenient | ⏳ Pending | Spot-check all ORCID iDs listed in profiles |
| 11 | **Verify institutional profile URLs** | When convenient | ⏳ Pending | Ensure all profile links are live and correct |

---

## 🔵 Post-ISSN Tasks (Activate After Approval)

| # | Reminder | Timeline | Status | Notes |
|---|---|---|---|---|
| 12 | **Update ISSN placeholders** | Day 1 after receipt | ⏳ Not started | Replace ALL `XXXX-XXXX` placeholders |
| 13 | **DOAJ application** | Month 1-3 after ISSN | ⏳ Not started | See `POST_ISSN_ROADMAP.md` Phase 1 |
| 14 | **UGC Care application** | Month 3-6 after ISSN | ⏳ Not started | See `POST_ISSN_ROADMAP.md` Phase 2 |
| 15 | **Index Copernicus registration** | Month 3-6 after ISSN | ⏳ Not started | See `POST_ISSN_ROADMAP.md` Phase 2 |
| 16 | **EBSCO submission** | Month 3-6 after ISSN | ⏳ Not started | See `POST_ISSN_ROADMAP.md` Phase 2 |
| 17 | **Scopus application** | Month 6-12 after ISSN | ⏳ Not started | Requires minimum 2 published issues |
| 18 | **Web of Science application** | Month 6-12 after ISSN | ⏳ Not started | Requires strong citation metrics |
| 19 | **Assign individual DOIs via Zenodo** | After ISSN, before DOAJ | ⏳ Not started | Each article needs a DOI |
| 20 | **Add plain language summaries** | After ISSN | ⏳ Not started | Recommended for DOAJ compliance |

---

## ✅ Completed Reminders

| # | Reminder | Completed | Notes |
|---|---|---|---|
| — | Fix starting year 2025 → 2026 | 2026-06-22 | All pages updated |
| — | Add Dr. Mary Lou Frank postal address | 2026-06-22 | 100 University Parkway, Macon, GA 31206, USA |
| — | Add Prof. Nuzhat Parveen Khan to board | 2026-06-22 | Full profile added to both pages |
| — | Fix editorial portfolio card layout | 2026-06-22 | Horizontal cards for all members |
| — | Standardize profile card structure | 2026-06-22 | All 13 profiles use consistent DOM |
| — | Add OG/Twitter Card tags | Pre-2026-06-22 | All major pages covered |
| — | Remove accidental scratch files | 2026-06-22 | Added to .gitignore |

---

## How to Add a New Reminder

Append to the appropriate priority section:

```markdown
| [#] | **[Description]** | [Deadline/Target] | ⏳ Pending | [Additional notes] |
```

Status legend:
- `⏳ Pending` — Not started
- `🔄 In Progress` — Actively being worked on
- `✅ Done` — Completed (move to Completed section)
- `⏳ Waiting` — Blocked by external factor
- `❌ Cancelled` — No longer needed
