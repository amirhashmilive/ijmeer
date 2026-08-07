# IJMEER — Volume, Issue & Publication Standards

## MASTER SCHEDULE

| Volume | Issue | Quarter | Coverage Period | Submission Deadline | Publication Month | ISSN Status | Display ISSN on Cover? |
|--------|-------|---------|-----------------|---------------------|-------------------|-------------|------------------------|
| Volume 1 | Issue 1 | Q1 | January–March | March 15 | April 2026 | Not assigned | ❌ NO (Pre-ISSN) |
| Volume 1 | Issue 2 | Q2 | April–June | June 15 | July 2026 | Not assigned | ❌ NO (Pre-ISSN) |
| Volume 1 | Issue 3 | Q3 | July–September | September 15 | October 2026 | Assigned | ✅ YES (Right-hand top corner) |
| Volume 1 | Issue 4 | Q4 | October–December | December 15 | January 2027 | Assigned | ✅ YES (Right-hand top corner) |
| Volume 2 | Issue 1 | Q1 | January–March | March 15 | April 2027 | Assigned | ✅ YES (Right-hand top corner) |
| Volume 2 | Issue 2 | Q2 | April–June | June 15 | July 2027 | Assigned | ✅ YES (Right-hand top corner) |
| ... and so on | | | | | | | |

## RULES (STRICT ENFORCEMENT)

1. **ISSN Placement Standard**:
   - **Online ISSN**: `3139-6003` (Officially assigned August 2026).
   - **Pre-ISSN Issues (Vol 1 Issue 1 & Issue 2)**: MUST NOT display ISSN on cover pages or PDF text pages as they were published prior to official assignment.
   - **Future Issues (Vol 1 Issue 3 onwards)**: MUST display `E-ISSN: 3139-6003` (or `Online ISSN: 3139-6003`) on the **RIGHT-HAND TOP CORNER** of every cover page.
   - Cover Page Generator Script: `docs/generate_future_cover_template.py`

2. **Volume Numbering**: Always increment by 1 per year. Volume 1 = 2026, Volume 2 = 2027, etc.

3. **Issue Numbering**: Always 1 to 4 per volume (Quarterly). Resets to 1 at the start of each volume/year.

4. **Coverage Period**:
   - Issue 1: January–March
   - Issue 2: April–June
   - Issue 3: July–September
   - Issue 4: October–December

5. **Publication Month**:
   - Issue 1: April
   - Issue 2: July
   - Issue 3: October
   - Issue 4: January (next year)

6. **Year Consistency**: The coverage year and publication year must match. Example: Volume 1, Issue 2 covers April–June 2026 and is published in July 2026.

7. **All References Must Match**: PDF covers, title pages, TOC, website, archive, metadata, DOIs, and citations must ALL use the same Volume, Issue, dates.

## ENFORCEMENT CHECKLIST (For EVERY new issue)

- [ ] Volume number correct?
- [ ] Issue number correct?
- [ ] Coverage period correct?
- [ ] Publication month correct?
- [ ] Year correct?
- [ ] ISSN placement verified? (❌ NO ISSN for Issue 1 & 2; ✅ Right-hand top corner for Issue 3+)
- [ ] DOI matches issue?
- [ ] Front matter (cover, title page, TOC) updated?
- [ ] Website (archive.html, citations.html) updated?
- [ ] Sitemap updated?
- [ ] Print version updated?
- [ ] All article pages correct?

## IN CASE OF ERROR

If a mismatch is detected, priority order to fix:
1. PDF cover and title page
2. Website (archive.html, citations.html)
3. papers.json and issues.json
4. Sitemap.xml
5. Print archive
