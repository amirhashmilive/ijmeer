import os
import re
import glob

# 1. Title optimization (limit to 50-60 chars)
# 85 chars: "INTERNATIONAL JOURNAL OF MULTIDISCIPLINARY EXPLICATION AND EMERGING RESEARCH (IJMEER)"
def shorten_title(html):
    html = html.replace(
        '<title>Privacy Policy &mdash; INTERNATIONAL JOURNAL OF MULTIDISCIPLINARY EXPLICATION AND EMERGING RESEARCH (IJMEER)</title>',
        '<title>Privacy Policy &mdash; IJMEER Open Access Journal</title>'
    )
    html = html.replace(
        'content="INTERNATIONAL JOURNAL OF MULTIDISCIPLINARY EXPLICATION AND EMERGING RESEARCH (IJMEER)"',
        'content="IJMEER: International Multidisciplinary Research Journal"'
    )
    html = html.replace(
        '<title>IJMEER | Open Access Journal</title>',
        '<title>IJMEER: International Multidisciplinary Research Journal</title>'
    )
    return html

# 2. Defer render-blocking CSS/JS
def defer_resources(html):
    # Defer JS
    html = html.replace('<script async src="https://www.googletagmanager.com/gtag/js?id=G-2FNJ68WF8J"></script>', '<script defer src="https://www.googletagmanager.com/gtag/js?id=G-2FNJ68WF8J"></script>')
    
    # CSS is already deferred using the preload/onload hack, but let's make sure it's perfect or if any missed ones.
    # Find any standard blocking stylesheet and convert it.
    def css_repl(m):
        full_tag = m.group(0)
        href = m.group(1)
        if 'media=' in full_tag or 'onload=' in full_tag or '<noscript>' in full_tag:
            return full_tag
        return f'<link rel="preload" href="{href}" as="style" onload="this.onload=null;this.rel=\'stylesheet\'"><noscript><link rel="stylesheet" href="{href}"></noscript>'
    
    html = re.sub(r'<link\s+rel="stylesheet"\s+href="([^"]+)">', css_repl, html)
    return html

# 3. Optimize keywords in headings
def optimize_headings(html, filepath):
    if 'index.html' in filepath:
        # Add keywords to h2
        html = html.replace('<h2 class="section-title" id="metrics-heading">Journal Impact &amp; Performance</h2>', '<h2 class="section-title" id="metrics-heading">IJMEER Journal Impact &amp; Performance Metrics</h2>')
        html = html.replace('<h2 class="section-title" id="why-heading">Why Publish With IJMEER?</h2>', '<h2 class="section-title" id="why-heading">Why Publish Open Access With IJMEER?</h2>')
        html = html.replace('<h2 class="section-title" id="subjects-heading">70+ Subject Areas</h2>', '<h2 class="section-title" id="subjects-heading">70+ Multidisciplinary Subject Areas</h2>')
        html = html.replace('<h2 class="section-title" id="articles-heading">Featured Articles</h2>', '<h2 class="section-title" id="articles-heading">Featured Peer-Reviewed Articles</h2>')
        
        # Add keywords to hero title
        html = html.replace(
            '<h1 class="hero-title">\n          INTERNATIONAL JOURNAL OF<br>\n          MULTIDISCIPLINARY<br>\n          <span class="hero-title-animated">EXPLICATION &amp;</span><br>\n          EMERGING RESEARCH\n        </h1>',
            '<h1 class="hero-title">\n          INTERNATIONAL JOURNAL OF<br>\n          MULTIDISCIPLINARY<br>\n          <span class="hero-title-animated">EXPLICATION &amp;</span><br>\n          EMERGING RESEARCH (IJMEER)\n        </h1>\n        <p style="font-weight:600; color:var(--blue); font-size:1.1rem; margin-top:-10px; margin-bottom:15px;">A Peer-Reviewed Open Access Journal</p>'
        )
    return html

# 4. Serve properly sized images
def size_images(html):
    # Add width="800" height="800" to editorial avatars since they are square and max size is 800px or similar
    def img_repl(m):
        full_img = m.group(0)
        if 'width=' in full_img and 'height=' in full_img:
            return full_img
        if 'profile-photo' in full_img or 'object-fit:cover;border-radius:50%;' in full_img:
            return full_img.replace('<img ', '<img width="400" height="400" ')
        return full_img
    
    html = re.sub(r'<img\s+[^>]+>', img_repl, html)
    return html

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = shorten_title(content)
    new_content = defer_resources(new_content)
    new_content = optimize_headings(new_content, filepath)
    new_content = size_images(new_content)
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
