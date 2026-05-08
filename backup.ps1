param (
    [Parameter(Mandatory=$true)]
    [string]$CommitMessage
)

# Define directories
$SourceDir = "C:\Users\hashm\Desktop\Projects\Workplace IJMEER"
$BackupDir = "C:\Users\hashm\Desktop\Projects\backup\IJ"

# Create backup directory if it doesn't exist
if (-not (Test-Path -Path $BackupDir)) {
    New-Item -ItemType Directory -Path $BackupDir -Force | Out-Null
}

# Get current date and time in YYYY-MM-DD_HHMM format
$DateTime = Get-Date -Format "yyyy-MM-dd_HHmm"

# Sanitize commit message to be used in a filename
$SafeCommitMessage = $CommitMessage -replace '[\\/:*?"<>|]', '-'
$SafeCommitMessage = $SafeCommitMessage -replace '\s+', '-'

# Define the full path for the zip file
$ZipFileName = "${DateTime}_${SafeCommitMessage}.zip"
$ZipFilePath = Join-Path -Path $BackupDir -ChildPath $ZipFileName

Write-Host "Creating complete backup of IJMEER project..." -ForegroundColor Cyan

# Compress the entire directory
try {
    # Get all items including hidden ones and compress them
    Compress-Archive -Path "$SourceDir\*" -DestinationPath $ZipFilePath -Force
    Write-Host "Backup successfully created at: $ZipFilePath" -ForegroundColor Green
}
catch {
    Write-Host "An error occurred during backup: $_" -ForegroundColor Red
}
