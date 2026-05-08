# IJMEER Policy Compliance Log

This file is automatically updated by `scratch/check-policy.ps1` after each scan.
Manual entries may also be added for agent compliance decisions.

## Log Format
Each entry follows this pattern:
```
### [YYYY-MM-DD] [PASS|WARN|FIXED|DECISION] — description
- File: `filename`
- Rule checked: rule name
- Result: outcome
- Action taken: none | auto-fixed | user-warned
```

---

### [2026-05-09] POLICY CREATED — Initial policy document established
- File: `PROJECT_POLICY.md`
- Rule checked: N/A — initial creation
- Result: Policy framework created per user instruction
- Action taken: Document created; enforcement script created at `scratch/check-policy.ps1`

### [2026-05-09] KNOWN VIOLATIONS — Grandfathered legacy files documented
- Files: `images/editorial/*.webp` (CamelCase names), `images/international_&_special_editorial_board/` (dir name)
- Rule: 2. File Naming — Uppercase / Special Chars / Underscores
- Result: GRANDFATHERED — these files existed before policy and have widespread HTML references
- Action taken: Documented in PROJECT_POLICY.md Section 1.2; no rename performed to avoid breaking site
- Note: All NEW files added after 2026-05-09 must comply with naming convention

---

### [2026-05-09] SCAN (FAIL) -- Policy compliance check
- Timestamp: 2026-05-09 03:18
- Files scanned: 121
- Violations: 34
- Warnings: 0
- Result: FAIL

### [2026-05-09] SCAN (FAIL) -- Policy compliance check
- Timestamp: 2026-05-09 03:19
- Files scanned: 121
- Violations: 25
- Warnings: 0
- Result: FAIL

### [2026-05-09] SCAN (FAIL) -- Policy compliance check
- Timestamp: 2026-05-09 03:19
- Files scanned: 121
- Violations: 21
- Warnings: 0
- Result: FAIL

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 03:20
- Files scanned: 121
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 03:24
- Files scanned: 123
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (FAIL) -- Policy compliance check
- Timestamp: 2026-05-09 03:33
- Files scanned: 155
- Violations: 1
- Warnings: 0
- Result: FAIL

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 03:33
- Files scanned: 155
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 03:33
- Files scanned: 155
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 03:39
- Files scanned: 155
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 03:50
- Files scanned: 155
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 04:01
- Files scanned: 155
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 04:04
- Files scanned: 155
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 04:08
- Files scanned: 154
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 04:08
- Files scanned: 155
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 04:15
- Files scanned: 155
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (FAIL) -- Policy compliance check
- Timestamp: 2026-05-09 04:21
- Files scanned: 156
- Violations: 1
- Warnings: 0
- Result: FAIL

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 04:22
- Files scanned: 155
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 04:22
- Files scanned: 155
- Violations: 0
- Warnings: 0
- Result: PASS

### [2026-05-09] SCAN (PASS) -- Policy compliance check
- Timestamp: 2026-05-09 04:29
- Files scanned: 155
- Violations: 0
- Warnings: 0
- Result: PASS
