import os

BASE_DIR = r"C:\Users\hashm\Desktop\Projects\Workplace IJMEER"

files_to_update = [
    os.path.join(BASE_DIR, "editorial-board.html"),
    os.path.join(BASE_DIR, "editorial-portfolio.html")
]

old_icon = "&#x1F4CB;"
new_icon = '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>'

for filepath in files_to_update:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_icon in content:
        content = content.replace(old_icon, new_icon)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
    else:
        print(f"Icon not found in {os.path.basename(filepath)}")
