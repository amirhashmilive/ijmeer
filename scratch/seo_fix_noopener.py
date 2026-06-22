"""
SEO Fix: Add rel="noopener noreferrer" to all target="_blank" links
that don't already have it.
"""

import os
import re
import glob

BASE_DIR = r"C:\Users\hashm\Desktop\Projects\Workplace IJMEER"
html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))

ENCODING_MAP = {
    'about-this-journal.html': 'latin-1',
    'abstracting-indexing.html': 'latin-1',
    'book-reviews.html': 'latin-1',
    'metrics.html': 'latin-1',
}

def get_encoding(filename):
    return ENCODING_MAP.get(os.path.basename(filename), 'utf-8')

fixed_files = []
total_fixes = 0

def fix_target_blank(line):
    """
    For any <a ... target="_blank" ...> that lacks rel="noopener noreferrer",
    add it. Handles various orderings and existing partial rel values.
    """
    # Match anchor tags with target="_blank" (or target='_blank')
    # We need to handle cases where rel already exists but lacks noopener
    
    def process_tag(m):
        tag = m.group(0)
        
        # Already fully compliant
        if 'noopener' in tag and 'noreferrer' in tag:
            return tag
        
        # Has rel= but missing noopener/noreferrer
        if re.search(r'rel=["\']', tag):
            # Append to existing rel value
            def append_rel(rm):
                existing = rm.group(1)
                additions = []
                if 'noopener' not in existing:
                    additions.append('noopener')
                if 'noreferrer' not in existing:
                    additions.append('noreferrer')
                if additions:
                    return f'rel="{existing} {" ".join(additions)}"'
                return rm.group(0)
            tag = re.sub(r'rel=["\']([^"\']*)["\']', append_rel, tag)
        else:
            # No rel at all — add before the closing >
            tag = re.sub(r'(\s*/?>)', r' rel="noopener noreferrer"\1', tag, count=1)
        
        return tag
    
    # Match full <a ...> opening tags that contain target="_blank"
    pattern = r'<a\s[^>]*target=["\']_blank["\'][^>]*>'
    return re.sub(pattern, process_tag, line)


for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    enc = get_encoding(filepath)
    with open(filepath, 'r', encoding=enc) as f:
        content = f.read()
    
    # Check if file has any target="_blank" before processing
    if 'target="_blank"' not in content and "target='_blank'" not in content:
        continue
    
    lines = content.split('\n')
    new_lines = []
    file_fixes = 0
    
    for line in lines:
        if 'target="_blank"' in line or "target='_blank'" in line:
            new_line = fix_target_blank(line)
            if new_line != line:
                file_fixes += 1
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    
    if file_fixes > 0:
        with open(filepath, 'w', encoding=enc) as f:
            f.write('\n'.join(new_lines))
        fixed_files.append((filename, file_fixes))
        total_fixes += file_fixes
        print(f"  [FIXED] {filename}: {file_fixes} link(s) fixed")
    else:
        print(f"  [OK]    {filename}: already compliant")

print(f"\nDone. {total_fixes} links fixed across {len(fixed_files)} files.")
if fixed_files:
    for f, c in fixed_files:
        print(f"   {f}: {c} fix(es)")
