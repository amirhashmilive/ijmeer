# CURRENT_TASK.md — Active Task Tracker

> **Agents: Update this file at the START of every session.**  
> Replace contents with the current task. Keep last completed task for reference.

---

## Current Task

**Task:** Fix Google Search Console "Page with redirect" issue (2 pages)
**Status:** ? Done
**Started:** 2026-07-18
**Completed:** 2026-07-18
**Agent:** Antigravity

### Progress:
- [x] Scanned all HTML files for meta refresh and JavaScript redirects
- [x] Identified 9 HTML pages acting as redirects (which included the 2 flagged by GSC)
- [x] Removed <meta http-equiv="refresh"> and window.location.replace from all 9 redirect pages
- [x] Updated 10 internal HTML pages to point directly to the final URLs, breaking the redirect chains
- [x] Generated a fresh sitemap.xml with updated dates for all working URLs
- [x] Update MEMORY.md and CURRENT_TASK.md
- [ ] Commit and push changes

### Next Steps:
1. Continue with other pending tasks (e.g., adding institutional emails).

---

## Previous Task

**Task:** Fix remaining SEO issues: render-blocking resources, image sizing, plaintext emails, cross-origin links
**Status:** ? Done
**Started:** 2026-07-17
**Completed:** 2026-07-17
**Agent:** Antigravity

---

## Next Recommended Actions

1. **Add API keys to GitHub Secrets** — GEMINI_API_KEY and NANO_BANANA_API_KEY
2. **Test GitHub Actions** — Manually trigger media-kit-weekly.yml via workflow_dispatch
3. **Add footer link** — (requires explicit approval to modify components.js)
4. **Add institutional emails** for Dr. Nusrat Ali Hashmi and Sayed Amir Mustafa Hashmi
5. **Monitor ISSN** — expected any day now (~30 working days from April 24)
6. **Create individual article pages** in /papers/ for Vol 1 Issue 1

---

## Blockers

- None
