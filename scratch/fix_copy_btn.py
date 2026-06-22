import os

BASE_DIR = r"C:\Users\hashm\Desktop\Projects\Workplace IJMEER"

# 1. Update CSS in both files
files_to_update = [
    os.path.join(BASE_DIR, "editorial-board.html"),
    os.path.join(BASE_DIR, "editorial-portfolio.html")
]

for filepath in files_to_update:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update email-copy-wrap CSS
    old_css = """.email-copy-wrap {
      display: inline-flex; align-items: center; gap: 5px;
    }
    .copy-email-btn {"""
    
    new_css = """.email-copy-wrap {
      display: inline-flex; align-items: center; gap: 5px; flex-wrap: wrap; word-break: break-all;
    }
    .copy-email-btn {
      flex-shrink: 0;"""
    
    content = content.replace(old_css, new_css)
    
    # Update inline styles in portfolio
    if "editorial-portfolio" in filepath:
        old_inline = 'style="display:flex;align-items:center;gap:6px;"'
        new_inline = 'style="display:flex;align-items:center;gap:6px;flex-wrap:wrap;word-break:break-all;"'
        content = content.replace(old_inline, new_inline)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
