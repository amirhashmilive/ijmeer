param(
    [Parameter(Mandatory=$true)]
    [string]$SessionDescription
)

$BackupDir = "C:\Users\hashm\Desktop\Projects\backup\IJ"
$SourceDir  = "C:\Users\hashm\Desktop\Projects\Workplace IJMEER"

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  IJMEER SESSION GUARD - Backup Enforcer   " -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[GUARD] Creating mandatory pre-session backup..." -ForegroundColor Yellow

& "$SourceDir\backup.ps1" -CommitMessage "PRE-SESSION-$SessionDescription"

if ($LASTEXITCODE -ne 0) {
    Write-Host "[GUARD] backup.ps1 exited with error. Aborting." -ForegroundColor Red
    exit 1
}

# Verify a backup zip was created within the last 90 seconds
$Recent = Get-ChildItem $BackupDir -Filter "*.zip" -ErrorAction SilentlyContinue |
          Where-Object { $_.LastWriteTime -gt (Get-Date).AddSeconds(-90) } |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1

if (-not $Recent) {
    Write-Host ""
    Write-Host "[GUARD] ERROR: Could not verify a recent backup file in:" -ForegroundColor Red
    Write-Host "        $BackupDir" -ForegroundColor Red
    Write-Host "[GUARD] ABORTING. Do NOT proceed without a confirmed backup." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[GUARD] Backup verified: $($Recent.Name)" -ForegroundColor Green
Write-Host "[GUARD] Size: $([math]::Round($Recent.Length / 1MB, 2)) MB" -ForegroundColor Green
Write-Host "[GUARD] Safe to proceed. Opening VS Code..." -ForegroundColor Cyan
Write-Host ""

code "$SourceDir"
