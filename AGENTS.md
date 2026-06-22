# AGENTS.md — Primary Agent Instruction File
> **READ THIS FIRST before taking any action on the IJMEER project.**

---

## 1. Project Identity

| Field | Value |
|---|---|
| **Journal Name** | International Journal of Multidisciplinary Educational Excellence and Research (IJMEER) |
| **Short Name** | IJMEER |
| **Domain** | https://www.ijmeer.com |
| **GitHub Repo** | https://github.com/amirhashmilive/ijmeer |
| **Publisher** | Meer Foundation (NGO), Raipur, Chhattisgarh, India |
| **Editor-in-Chief** | Dr. Nusrat Ali Hashmi |
| **Managing Editor** | Sayed Amir Mustafa Hashmi |
| **ISSN (Print)** | XXXX-XXXX *(pending)* |
| **ISSN (Online)** | XXXX-XXXX *(pending)* |
| **ISSN Application ID** | 75192 |
| **Established Year** | 2026 *(CRITICAL: must match ISSN application)* |
| **Frequency** | Bi-Annual (April & October) |
| **Format** | Open Access, Peer-Reviewed |
| **Access Model** | Diamond Open Access (free to read, free to publish) |
| **Scope** | Multidisciplinary — Law, Education, Management, Social Sciences, Technology, etc. |

---

## 2. Core Rules (NEVER VIOLATE)

### ❌ NEVER DO:
- Change UI colors, fonts, spacing, layout, or navigation structure without explicit approval
- Add dark mode or any theme switching
- Add or mention GST, service tax, or VAT anywhere on the site
- Add "Fast Track" or "Express Publication" services or fees
- Show USD pricing for Indian authors (INR only for Indian authors)
- Make false indexing claims (e.g., "Scopus indexed" before actual indexing)
- Remove or modify the ISSN placeholder `XXXX-XXXX` unless ISSN is officially received
- Change the established/founding year from **2026** to any other year
- Break existing page structure, routing, or anchor links
- Delete content unless explicitly instructed

### ✅ ALWAYS DO:
- Read all memory files before starting work (AGENTS.md, MEMORY.md, CURRENT_TASK.md)
- Update `CURRENT_TASK.md` at the start of your session
- Update `MEMORY.md` after making significant changes
- Preserve all existing content unless instructed otherwise
- Use the exact commit message format specified
- Test all links and structural changes before committing
- Verify ISSN compliance after any editorial board or content changes
- Use WebP format for all new images

---

## 3. Memory File Reading Order

Before starting any task, read these files in order:
1. `AGENTS.md` — This file (rules and identity)
2. `MEMORY.md` — Project history and recent changes
3. `CURRENT_TASK.md` — What is currently being worked on
4. Relevant specialized file (e.g., `ISSN_COMPLIANCE.md`, `EDITORIAL_BOARD.md`, `UI_GUIDELINES.md`)

---

## 4. Agent Workflow

```
START SESSION
  ↓
Read AGENTS.md + MEMORY.md + CURRENT_TASK.md
  ↓
Understand the task fully before making ANY changes
  ↓
Make changes (smallest scope possible)
  ↓
Verify changes (check layout, links, content)
  ↓
Update MEMORY.md with what was changed
  ↓
Update CURRENT_TASK.md with current status
  ↓
Commit using the format below
  ↓
Push to main branch
END SESSION
```

---

## 5. Commit Message Format

```
[action]: [brief description]
```

**Allowed actions:**
- `add` — New file or section added
- `fix` — Bug fix or correction
- `update` — Content or data updated
- `remove` — Content deleted
- `refactor` — Code restructured without content change
- `style` — CSS or visual change (requires explicit approval)
- `docs` — Documentation or memory file update

**Examples:**
```
add: Prof. Nuzhat Parveen Khan to editorial board with profile image
fix: starting year 2026 for ISSN compliance across all pages
update: Dr. Mary Lou Frank postal address for ISSN compliance
docs: update MEMORY.md with session changes
```

---

## 6. Working Directory

```
D:\DRIVE (Ai) Agents\00 Projects\Workplace IJMEER
```

**Git remote:** `origin` → `https://github.com/amirhashmilive/ijmeer.git`  
**Branch:** `main`  
**Push command:** `git push origin HEAD:main`

---

## 7. Key Contacts

| Role | Name | Email |
|---|---|---|
| Editor-in-Chief | Dr. Nusrat Ali Hashmi | *(pending institutional email)* |
| Managing Editor | Sayed Amir Mustafa Hashmi | *(pending institutional email)* |
| Publisher Contact | Meer Foundation | info@meerfoundation.org *(verify)* |

---

## 8. Related Memory Files

| File | Purpose |
|---|---|
| `ARCHITECTURE.md` | Tech stack, folder structure, brand colors |
| `WORKFLOW.md` | Step-by-step SOPs for common tasks |
| `UI_GUIDELINES.md` | What can and cannot be changed visually |
| `CONTENT_RULES.md` | Content policies and prohibited language |
| `MEMORY.md` | Project history and recent changes |
| `CURRENT_TASK.md` | Active task tracker |
| `BACKUP.md` | Backup system instructions |
| `ISSN_COMPLIANCE.md` | All ISSN requirements |
| `EDITORIAL_BOARD.md` | Master list of all 13 board members |
| `SOCIAL_MEDIA.md` | Social media accounts and brand voice |
| `DEPLOYMENT.md` | Deployment process |
| `REMINDERS.md` | Active reminders and their status |
| `POST_ISSN_ROADMAP.md` | Post-approval indexing and growth roadmap |
