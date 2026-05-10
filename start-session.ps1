param(
    [Parameter(Mandatory=$true)]
    [string]$SessionDescription
)

$BackupDir = "C:\Users\hashm\Desktop\Projects\backup\IJ"
$SourceDir  = "C:\Users\hashm\Desktop\Projects\Workplace IJMEER"

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  IJMEER SESSION START - Backup Helper     " -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[START] Creating pre-session backup..." -ForegroundColor Yellow

& "$SourceDir\backup.ps1" -CommitMessage "PRE-SESSION-$SessionDescription"

if ($LASTEXITCODE -ne 0) {
    Write-Host "[START] backup.ps1 exited with error. Proceeding anyway." -ForegroundColor Yellow
}

# Verify a backup zip was created within the last 90 seconds
$Recent = Get-ChildItem $BackupDir -Filter "*.zip" -ErrorAction SilentlyContinue |
          Where-Object { $_.LastWriteTime -gt (Get-Date).AddSeconds(-90) } |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1

if (-not $Recent) {
    Write-Host ""
    Write-Host "[START] WARNING: Could not verify a recent backup file in:" -ForegroundColor Yellow
    Write-Host "        $BackupDir" -ForegroundColor Yellow
    Write-Host "[START] Proceeding without a confirmed backup." -ForegroundColor Yellow
} else {
    Write-Host ""
    Write-Host "[START] Backup verified: $($Recent.Name)" -ForegroundColor Green
    Write-Host "[START] Size: $([math]::Round($Recent.Length / 1MB, 2)) MB" -ForegroundColor Green
}
Write-Host "[START] Opening VS Code..." -ForegroundColor Cyan
Write-Host ""

code "$SourceDir"
