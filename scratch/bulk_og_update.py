import os
import re

# Standard OG block template
OG_TEMPLATE = """
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://www.ijmeer.com/{filename}">
  <meta property="og:site_name" content="IJMEER">
  <meta property="og:image" content="https://www.ijmeer.com/assets/images/social/share-preview.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="IJMEER Journal Social Preview Image">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="https://www.ijmeer.com/assets/images/social/share-preview.png">
  <meta name="twitter:site" content="@ijmeerj">
"""

def process_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has og:image
    if 'property="og:image"' in content or "property='og:image'" in content:
        print(f"Skipping {filename}: OG tags already present.")
        return

    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else "IJMEER"
    # Remove HTML entities if simple
    title = title.replace('&mdash;', '-').replace('&ndash;', '-').replace('&amp;', '&')

    # Extract description
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else ""

    # Find injection point (after canonical or before head)
    injection_point = ""
    canonical_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']\s*>', content, re.IGNORECASE)
    
    og_block = OG_TEMPLATE.format(title=title, description=description, filename=filename)

    if canonical_match:
        target = canonical_match.group(0)
        new_content = content.replace(target, target + og_block)
    else:
        # Fallback: after </title>
        if title_match:
            target = title_match.group(0)
            new_content = content.replace(target, target + og_block)
        else:
            print(f"Could not find injection point for {filename}")
            return

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filename}")

# Target files
files_to_update = [
    'contact.html', 'call-for-papers.html', 'citations.html', 'peer-review.html',
    'ethics.html', 'policies.html', 'editorial-portfolio.html', 'join-reviewer.html',
    'open-access.html', 'submitting.html', 'preparing.html', 'transparency.html',
    'privacy.html', 'rights.html', 'most-cited.html', 'library.html',
    'open-access-options.html', 'privacy-policy.html', 'publication-process.html',
    'publishing-ethics.html', 'research-transparency.html', 'reviewer-instructions.html',
    'rights-permissions.html'
]

working_dir = r'c:\Users\hashm\Desktop\Projects\Workplace IJMEER'

for f in files_to_update:
    path = os.path.join(working_dir, f)
    if os.path.exists(path):
        process_file(path)
    else:
        print(f"File not found: {f}")
