import os
import re

def analyze_site():
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != '404.html']
    
    with open('assets/js/components.js', 'r', encoding='utf-8') as f:
        components_content = f.read()
        
    # Extract Header and Footer HTML
    header_match = re.search(r'const HEADER = `([\s\S]*?)`;', components_content)
    footer_match = re.search(r'const FOOTER = `([\s\S]*?)`;', components_content)
    
    header_html = header_match.group(1) if header_match else ""
    footer_html = footer_match.group(1) if footer_match else ""
    
    with open('sitemap.xml', 'r', encoding='utf-8') as f:
        sitemap_content = f.read()
        
    results = []
    
    for filename in html_files:
        # Check Main Menu (Header)
        # Note: / counts as index.html
        in_main = "No"
        if filename == "index.html" and 'href="/"' in header_html:
            in_main = "Yes"
        elif filename in header_html:
            in_main = "Yes"
            
        # Check Footer
        in_footer = "No"
        if filename == "index.html" and 'href="/"' in footer_html:
            in_footer = "Yes"
        elif filename in footer_html:
            in_footer = "Yes"
            
        # Check Sitemap
        in_sitemap = "Yes" if filename in sitemap_content or (filename == "index.html" and "com/</loc>" in sitemap_content) else "No"
        
        # Check Internal Links (from other HTML files + components.js)
        has_internal = "No"
        # Check components.js first
        if filename in components_content:
            has_internal = "Yes"
        elif filename == "index.html" and ('href="/"' in components_content or 'href="./"' in components_content):
            has_internal = "Yes"
        
        if has_internal == "No":
            for other in html_files:
                if other == filename: continue
                with open(other, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if filename in content:
                        has_internal = "Yes"
                        break
                    # Special case for index.html linked as /
                    if filename == "index.html" and ('href="/"' in content or 'href="./"' in content):
                        has_internal = "Yes"
                        break
        
        # Status calculation
        # ✅: In Menu or Footer AND In Sitemap AND Has Internal Link
        # ⚠️: Orphan or Missing from Sitemap but in a Menu
        # ❌: Orphan AND Missing from Sitemap (potential junk)
        
        status = "OK"
        if has_internal == "No" and in_main == "No" and in_footer == "No":
            status = "ERROR" # Orphan
        elif in_sitemap == "No" or has_internal == "No":
            status = "WARN"
            
        results.append({
            "Page": filename,
            "InMain": in_main,
            "InFooter": in_footer,
            "HasInternal": has_internal,
            "InSitemap": in_sitemap,
            "Status": status
        })
        
    # Sort results alphabetically
    results.sort(key=lambda x: x['Page'])
    
    print("| Page | In Main Menu | In Footer | Has Internal Link | In Sitemap | Status |")
    print("|------|--------------|-----------|-------------------|------------|--------|")
    for r in results:
        print(f"| {r['Page']} | {r['InMain']} | {r['InFooter']} | {r['HasInternal']} | {r['InSitemap']} | {r['Status']} |")

if __name__ == "__main__":
    analyze_site()
