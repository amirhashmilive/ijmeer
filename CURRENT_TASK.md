# CURRENT_TASK.md — Active Task Tracker

> **Agents: Update this file at the START of every session.**  
> Replace contents with the current task. Keep last completed task for reference.

---

## Current Task

**Task:** Fix remaining SEO issues: render-blocking resources, image sizing, plaintext emails, cross-origin links
**Status:** ✅ Done
**Started:** 2026-07-17
**Completed:** 2026-07-17
**Agent:** Antigravity

### Progress:
- [x] Fix Render-blocking resources: Moved Google Fonts from CSS `@import` to `preload` links in all HTML files.
- [x] Fix Images not properly sized: Added `srcset` and `alt` to logo image in `components.js`.
- [x] Fix Plaintext emails: Encoded the 3 `mailto:` emails using HTML entities in `components.js`.
- [x] Fix Unsafe cross-origin links: Added `noreferrer` to 3 target="_blank" links with `rel="noopener"` in `components.js`.
- [x] Update MEMORY.md and CURRENT_TASK.md
- [ ] Commit and push changes

### Next Steps:
1. Continue with other pending tasks (e.g., adding institutional emails).

---

## Previous Task

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
