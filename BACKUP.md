# BACKUP.md — Backup System

---

## Backup Script

**Location:** `D:\DRIVE (Ai) Agents\00 Projects\Workplace IJMEER\backup.ps1`  
**Script exists:** Yes (already in project root)

---

## How to Run a Backup

```powershell
# Navigate to project directory first
cd "D:\DRIVE (Ai) Agents\00 Projects\Workplace IJMEER"

# Run with a descriptive message
.\backup.ps1 -CommitMessage "description of current state"

# Example:
.\backup.ps1 -CommitMessage "after-adding-nuzhat-khan-profile"
.\backup.ps1 -CommitMessage "pre-issn-update"
.\backup.ps1 -CommitMessage "after-volume-1-issue-2-published"
```

---

## Backup Storage Location

```
C:\Users\hashm\Desktop\Projects\backup\IJ\
```

---

## Naming Convention

```
YYYY-MM-DD_HHMM_commit-message.zip
```

**Examples:**
```
2026-06-22_1600_after-adding-nuzhat-khan-profile.zip
2026-06-22_2100_project-memory-system-created.zip
2026-04-01_0900_volume-1-issue-1-published.zip
```

---

## Retention Policy

- Keep **last 10 backups only**
- Delete older backups automatically (script handles this)
- Manual deletion: Check folder and remove oldest files if script fails

---

## What Gets Backed Up

The backup includes the entire project directory:
- All HTML files
- All CSS/JS assets
- All images
- All data files
- All memory/documentation files (AGENTS.md, MEMORY.md, etc.)
- `.gitignore`, `CNAME`, `robots.txt`, `sitemap.xml`

**Excludes:**
- `.git/` folder (version controlled separately via GitHub)
- `node_modules/` (if ever added)

---

## Restore Instructions

### From ZIP backup:
1. Locate the backup ZIP in `C:\Users\hashm\Desktop\Projects\backup\IJ\`
2. Extract to a temporary folder (e.g., `C:\temp\ijmeer-restore\`)
3. Review restored files
4. Copy to working directory: `D:\DRIVE (Ai) Agents\00 Projects\Workplace IJMEER\`
5. Overwrite existing files as needed
6. Verify the site works locally by opening `index.html` in a browser

### From GitHub:
```powershell
# If local is corrupted, clone fresh from GitHub
git clone https://github.com/amirhashmilive/ijmeer.git "D:\DRIVE (Ai) Agents\00 Projects\Workplace IJMEER"

# Or reset to a specific commit
git reset --hard [commit-hash]
git push origin HEAD:main --force  # Use carefully!
```

### Finding a specific version:
```powershell
# View commit history
git log --oneline -20

# Restore a specific file from a specific commit
git checkout [commit-hash] -- [filename]
```

---

## Backup Schedule Recommendation

| Trigger | When to Backup |
|---|---|
| Before major changes | Always backup before adding new board members, changing pricing, or structural edits |
| After each issue published | After Volume N Issue N is live |
| After ISSN received | Immediately after updating ISSN numbers |
| Weekly | Regular maintenance backup |

---

## Emergency Recovery

If the website is broken and GitHub Pages shows errors:
1. Check GitHub Actions tab for build errors
2. Check recent commits: `git log --oneline -5`
3. Revert last commit if needed: `git revert HEAD`
4. Or reset to last known good: `git reset --hard [commit-hash]`
5. Force push: `git push origin HEAD:main --force`

> ⚠️ Force push should be a last resort — it rewrites public history.
