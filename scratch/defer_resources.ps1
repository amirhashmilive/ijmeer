$dir = "C:\Users\hashm\Desktop\Projects\Workplace IJMEER"
$htmlFiles = Get-ChildItem -Path $dir -Filter "*.html" -File

$count = 0
foreach ($file in $htmlFiles) {
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $original = $content

    # 1. Replace render-blocking CSS link with preload + deferred load + noscript fallback
    $oldCSS = '<link rel="stylesheet" href="assets/css/style.css">'
    $newCSS = '<link rel="preload" href="assets/css/style.css" as="style" onload="this.onload=null;this.rel=''stylesheet''">' + "`r`n  " + '<noscript><link rel="stylesheet" href="assets/css/style.css"></noscript>'
    if ($content.Contains($oldCSS)) {
        $content = $content.Replace($oldCSS, $newCSS)
    }

    # 2. Add defer to components.js (if not already deferred)
    $content = $content -replace '<script src="assets/js/components\.js">', '<script defer src="assets/js/components.js">'

    # 3. Add defer to core.js (if not already deferred)
    $content = $content -replace '<script src="assets/js/core\.js">', '<script defer src="assets/js/core.js">'

    # 4. Add defer to papers.js (if not already deferred)
    $content = $content -replace '<script src="assets/js/papers\.js">', '<script defer src="assets/js/papers.js">'

    # 5. Add defer to timeline.js (if not already deferred)
    $content = $content -replace '<script src="assets/js/timeline\.js">', '<script defer src="assets/js/timeline.js">'

    if ($content -ne $original) {
        [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Updated: $($file.Name)"
        $count++
    } else {
        Write-Host "No changes: $($file.Name)"
    }
}
Write-Host ""
Write-Host "Done. $count files updated."
