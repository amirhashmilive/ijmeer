# check-policy.ps1
# IJMEER Project Policy Enforcement Script
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File scratch/check-policy.ps1
# ------------------------------------------------------------------

param([switch]$Strict)

$projectRoot = Split-Path -Parent $PSScriptRoot
$logFile     = Join-Path $projectRoot "policy-log.md"
$today       = Get-Date -Format "yyyy-MM-dd"
$timestamp   = Get-Date -Format "yyyy-MM-dd HH:mm"

function Write-Red    { param($t) Write-Host $t -ForegroundColor Red }
function Write-Yellow { param($t) Write-Host $t -ForegroundColor Yellow }
function Write-Green  { param($t) Write-Host $t -ForegroundColor Green }
function Write-Cyan   { param($t) Write-Host $t -ForegroundColor Cyan }

$excludeDirs     = @(".git", "node_modules", "temp_docx", "backup")
$imageExts       = @(".webp", ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".avif", ".tiff")
$bannedImageExts = @(".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff")
$bannedCharsRx   = '[&+%#@!(){}\[\]<>,;=\^~` ]'

# Grandfathered filenames that existed before this policy -- skip them in scans
# so the checker only reports NEW violations added after 2026-05-09.
$grandfathered = @(
    # Legacy editorial images (CamelCase) -- widespread HTML references
    "AdvDrAshokYende.webp", "AdvDrAshokYende.png.bak",
    "DrMaryLouFrank.webp", "DrMaryLouFrank.png.bak",
    "DrMohammedSalimKhan.webp", "DrMohammedSalimKhan.png.bak",
    "ProfDrAshokLSunatkari.webp", "ProfDrAshokLSunatkari.png.bak",
    "ProfDrKarunaAkshayMalviya.webp", "ProfDrKarunaAkshayMalviya.png.bak",
    "drnusratalihashmi.webp", "drnusratalihashmi.png.bak",
    "drmominali.webp", "drmominali.png.bak",
    "sayedamirmustafahashmi.webp", "sayedamirmustafahashmi.png.bak",
    "drmonapurohit.webp", "drmonapurohit.png.bak",
    "drranushkla.webp", "drranushkla.png.bak",
    # Legacy .bak image backups
    "hero-bg.png.bak", "mindmap-disciplines.png.bak",
    "open-access-globe.png.bak", "peer-review.png.bak",
    "publication-process.png.bak", "ijmeer-emblem-full.png.bak",
    "ijmeer-favicon.png.bak", "ijmeer-logo-horizontal.png.bak", "ijmeer-logo-square.png.bak",
    # Project-level docs
    "PROJECT_POLICY.md", "README.md", "policy-log.md",
    # Scratch / working scripts
    "defer_resources.ps1", "check-policy.ps1",
    # Legacy misc files
    "advisory_extracted.txt", "analyze_site.py",
    "editorial_board_text.md", "extracted_text.txt", "intl_extracted.txt"
)

$violations = New-Object System.Collections.Generic.List[object]
$warnings   = New-Object System.Collections.Generic.List[object]

function Add-Issue {
    param($Sev, $Rule, $File, $Detail)
    $obj = [PSCustomObject]@{ Severity=$Sev; Rule=$Rule; File=$File; Detail=$Detail }
    if ($Sev -eq "VIOLATION") { $violations.Add($obj) }
    else { $warnings.Add($obj) }
}

function Test-Excluded {
    param($fullPath)
    foreach ($ex in $excludeDirs) {
        if ($fullPath -like "*\$ex\*" -or $fullPath -like "*\$ex") { return $true }
    }
    return $false
}

Write-Host ""
Write-Cyan "========================================================"
Write-Cyan "  IJMEER PROJECT POLICY CHECKER"
Write-Cyan "  $timestamp"
Write-Cyan "========================================================"
Write-Host ""

# ---- Scan files ----
$allFiles = Get-ChildItem -Path $projectRoot -Recurse -File | Where-Object { -not (Test-Excluded $_.FullName) }
$total    = ($allFiles | Measure-Object).Count
Write-Host "Scanning $total files..."
Write-Host ""

foreach ($file in $allFiles) {
    $name     = $file.Name
    $base     = [System.IO.Path]::GetFileNameWithoutExtension($name)
    $ext      = $file.Extension.ToLower()
    $relPath  = $file.FullName.Substring($projectRoot.Length + 1)

    # Skip grandfathered legacy files (matched by filename alone)
    if ($grandfathered -icontains $name) { continue }
    # Also skip anything inside the grandfathered international dir
    if ($relPath -like "*international_*_special_editorial_board*") { continue }
    # Skip legacy PDF names
    if ($name -match '^IJMEER_V\d') { continue }

    # Rule 1: Non-WebP image
    if ($bannedImageExts -contains $ext) {
        Add-Issue "VIOLATION" "1. Image Format" $relPath "File is $($ext.ToUpper()) -- must be converted to WebP"
    }

    # Rule 2: Uppercase in filename
    if ($name -cmatch '[A-Z]') {
        Add-Issue "VIOLATION" "2. Naming - Uppercase" $relPath "Uppercase letters in: $name"
    }

    # Rule 3: Spaces in filename
    if ($name -match ' ') {
        Add-Issue "VIOLATION" "3. Naming - Spaces" $relPath "Spaces in filename: $name"
    }

    # Rule 4: Underscores in filename
    if ($base -match '_') {
        Add-Issue "VIOLATION" "4. Naming - Underscores" $relPath "Underscores in: $name"
    }

    # Rule 5: Filename too long
    if ($base.Length -gt 50) {
        Add-Issue "WARNING" "5. Naming - Length" $relPath "Basename is $($base.Length) chars (max 50): $base"
    }

    # Rule 6: Banned special characters
    if ($name -match $bannedCharsRx) {
        Add-Issue "VIOLATION" "6. Naming - Special Chars" $relPath "Banned chars in: $name"
    }
}

# ---- Scan directories ----
$allDirs = Get-ChildItem -Path $projectRoot -Recurse -Directory | Where-Object { -not (Test-Excluded $_.FullName) }

foreach ($dir in $allDirs) {
    $dn      = $dir.Name
    $relDir  = $dir.FullName.Substring($projectRoot.Length + 1)

    # Skip grandfathered legacy directories
    if ($relDir -like "*international_&_special_editorial_board*") { continue }

    if ($dn -cmatch '[A-Z]') {
        Add-Issue "WARNING" "Dir - Uppercase" $relDir "Directory has uppercase: $dn"
    }
    if ($dn -match ' ') {
        Add-Issue "VIOLATION" "Dir - Spaces" $relDir "Directory has spaces: $dn"
    }
    if ($dn -match $bannedCharsRx) {
        Add-Issue "VIOLATION" "Dir - Special Chars" $relDir "Directory has banned chars: $dn"
    }
}

# ---- Print results ----
Write-Host ""
Write-Cyan "========================================================"
Write-Cyan "  RESULTS"
Write-Cyan "========================================================"
Write-Host ""

if ($violations.Count -eq 0 -and $warnings.Count -eq 0) {
    Write-Green "[OK] ALL CLEAR -- No policy violations found!"
    Write-Host ""
}
else {
    if ($violations.Count -gt 0) {
        Write-Red "[FAIL] VIOLATIONS ($($violations.Count) found):"
        Write-Host ""
        $grouped = $violations | Group-Object Rule | Sort-Object Name
        foreach ($g in $grouped) {
            Write-Yellow "  >> $($g.Name)"
            foreach ($v in $g.Group) {
                Write-Red    "     FILE : $($v.File)"
                Write-Host   "     ISSUE: $($v.Detail)"
                Write-Host ""
            }
        }
    }

    if ($warnings.Count -gt 0) {
        Write-Yellow "[WARN] WARNINGS ($($warnings.Count) found):"
        Write-Host ""
        foreach ($w in $warnings) {
            Write-Yellow "  >> $($w.Rule)"
            Write-Yellow "     FILE: $($w.File)"
            Write-Host   "     NOTE: $($w.Detail)"
            Write-Host ""
        }
    }
}

# ---- Summary ----
Write-Cyan "========================================================"
if ($violations.Count -gt 0) {
    Write-Red   "  SUMMARY: $($violations.Count) violation(s), $($warnings.Count) warning(s)"
    Write-Red   "  Fix violations before committing new files."
}
elseif ($warnings.Count -gt 0) {
    Write-Yellow "  SUMMARY: 0 violations, $($warnings.Count) warning(s)"
    Write-Yellow "  Review warnings -- no blocking issues."
}
else {
    Write-Green "  SUMMARY: [OK] Fully compliant -- 0 violations, 0 warnings"
}
Write-Cyan "========================================================"
Write-Host ""

# ---- Append to policy-log.md ----
$passOrFail = if ($violations.Count -eq 0) { "PASS" } else { "FAIL" }
$logEntry = @"

### [$today] SCAN ($passOrFail) -- Policy compliance check
- Timestamp: $timestamp
- Files scanned: $total
- Violations: $($violations.Count)
- Warnings: $($warnings.Count)
- Result: $passOrFail
"@

Add-Content -Path $logFile -Value $logEntry -Encoding UTF8
Write-Host "Log appended to policy-log.md"
Write-Host ""

if ($Strict -and $violations.Count -gt 0) { exit 1 }
exit 0
