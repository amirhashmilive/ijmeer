# CURRENT_TASK.md — Active Task Tracker

> **Agents: Update this file at the START of every session.**  
> Replace contents with the current task. Keep last completed task for reference.

---

## Current Task

**Task:** Fix SEO issues: render-blocking resources, image alt tags, email encoding, and cross-origin links
**Status:** ✅ Done
**Started:** 2026-07-14
**Completed:** 2026-07-14
**Agent:** Antigravity (Gemini 3.1 Pro)

### Progress:
- [x] Fix CSS Preload in `<noscript>` tags across all HTML files
- [x] Verified missing `alt` attributes on images
- [x] Encode `mailto:` emails using HTML entities
- [x] Add `rel="noopener noreferrer"` to `target="_blank"` links
- [x] Verify `404.html` exists and is functional
- [x] Update MEMORY.md and CURRENT_TASK.md
- [x] Commit and push changes

### Next Steps:
1. Continue with other pending tasks (e.g., adding institutional emails).

---

## Previous Task

**Task:** Update Online ISSN to 3139-6003
**Status:** ✅ Done
**Started:** 2026-07-14
**Completed:** 2026-07-14
**Agent:** Antigravity (Gemini 3.1 Pro (High))

### Progress:
- [x] Replace E-ISSN in `index.html`
- [x] Replace ISSN (Online) in `journal.html`
- [x] Replace ISSN (Online) in `contact.html`
- [x] Replace `citation_issn` in `index.html`, `journal.html`, `citations.html`, `archive.html`
- [x] Replace `issn_online` in `data/config.json`
- [x] Replace ISSN (Online) in `assets/js/components.js`
- [x] Keep Print ISSN as XXXX-XXXX
- [x] Update MEMORY.md and CURRENT_TASK.md
- [x] Commit and push changes

### Next Steps:
1. Complete Print ISSN updates when received.
2. Continue with other pending tasks (e.g., adding institutional emails).

---

## Previous Task

**Task:** COMPLETELY REMOVE the Media Kit system from the IJMEER website
**Status:** ✅ Done
**Started:** 2026-07-06
**Completed:** 2026-07-06
**Agent:** Antigravity (Gemini 3.1 Pro (High))

### Progress:
- [x] Delete `media-kit.html`
- [x] Delete `/media-kit/` folder
- [x] Delete `.github/workflows/media-kit-*.yml` workflows
- [x] Check `assets/js/components.js` for "Media Kit" footer link (verified it was never added)
- [x] Update MEMORY.md and CURRENT_TASK.md
- [x] Commit and push changes

### Notes:
- The footer link in `assets/js/components.js` was never actually added during the creation of the Media Kit, so no deletion was required there.

---

## Previous Task

**Task:** Generate comprehensive Website Reverse Engineering Report
**Status:** ✅ Done
**Started:** 2026-07-04
**Completed:** 2026-07-04
**Agent:** Antigravity (Gemini 3.1 Pro (High))

### Progress:
- [x] Create Implementation Plan for Reverse Engineering Report
- [x] Run automated Python script to extract directory structure, file inventory, URLs, and project statistics
- [x] Generate semantic Markdown for Architecture, Business Logic, Routing, UI, and Deployment
- [x] Assemble massive 30-section Markdown report
- [x] Export report to `C:\Users\hashm\Desktop\RE IJMEER\Website_Reverse_Engineering_Report.md`
- [x] Update MEMORY.md and CURRENT_TASK.md

### Notes:
- No original source code files were modified during this read-only operation.

---

## Previous Task

**Task:** Update Dr. Hafid Zakariya's institutional email to hafidzakariya@uibs.ac.id
**Status:** ✅ Done
**Started:** 2026-06-27
**Completed:** 2026-06-27
**Agent:** Antigravity (Claude Sonnet 4.6)

---

## Next Recommended Actions

1. **Add API keys to GitHub Secrets** — `GEMINI_API_KEY` and `NANO_BANANA_API_KEY`
2. **Test GitHub Actions** — Manually trigger `media-kit-weekly.yml` via workflow_dispatch
3. **Add footer link** — (requires explicit approval to modify `components.js`)
4. **Add institutional emails** for Dr. Nusrat Ali Hashmi and Sayed Amir Mustafa Hashmi
5. **Monitor ISSN** — expected any day now (~30 working days from April 24)
6. **Create individual article pages** in `/papers/` for Vol 1 Issue 1

---

## Blockers

- None
