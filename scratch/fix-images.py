import os
import re
from PIL import Image

name_map = {
    'drmonapurohit.webp': 'advisory-mona-purohit',
    'drranushkla.webp': 'advisory-ranu-shukla',
    'AdvDrAshokYende.webp': 'editorial-ashok-yende',
    'DrMaryLouFrank.webp': 'editorial-mary-lou-frank',
    'DrMohammedSalimKhan.webp': 'editorial-mohammed-salim-khan',
    'drmominali.webp': 'editorial-momin-ali',
    'drnusratalihashmi.webp': 'editorial-nusrat-ali-hashmi',
    'ProfDrAshokLSunatkari.webp': 'editorial-ashok-sunatkari',
    'ProfDrKarunaAkshayMalviya.webp': 'editorial-karuna-akshay-malviya',
    'sayedamirmustafahashmi.webp': 'editorial-sayed-amir-hashmi',
    'DrAnupamaPatel.webp': 'intl-board-anupama-patel',
    'ProfDrJyotirmayaThakur.webp': 'intl-board-jyotirmaya-thakur'
}

sizes = [200, 400, 800]

print("Generating resized images...")
# 1. Generate resized images
for root, _, files in os.walk('images'):
    for f in files:
        if f.endswith('.webp') and f in name_map:
            src_path = os.path.join(root, f).replace('\\', '/')
            base_compliant = name_map[f]
            try:
                with Image.open(src_path) as img:
                    orig_w, orig_h = img.size
                    for w in sizes:
                        if w <= orig_w:
                            ratio = w / float(orig_w)
                            h = int((float(orig_h) * float(ratio)))
                            resized = img.resize((w, h), Image.Resampling.LANCZOS)
                            out_path = os.path.join(root, f"{base_compliant}-{w}w.webp").replace('\\', '/')
                            resized.save(out_path, 'WEBP')
                            print(f"Created {out_path}")
                        else:
                            # If the original is smaller than the target width, just use original size
                            pass
            except Exception as e:
                print(f"Error processing {src_path}: {e}")

# 2. Update HTML files
print("Updating HTML files...")
html_files = []
for root, _, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'backup' in root or 'scratch' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f).replace('\\', '/'))

def replacer(match):
    img_tag = match.group(0)
    original_tag = str(img_tag)
    
    # Add width and height to logos if missing
    if 'assets/images/logo/' in img_tag:
        if 'width=' not in img_tag:
            src_match = re.search(r'src="([^"]+)"', img_tag)
            if src_match:
                src_val = src_match.group(1)
                if os.path.exists(src_val):
                    with Image.open(src_val) as img:
                        w, h = img.size
                        img_tag = img_tag.replace('<img ', f'<img width="{w}" height="{h}" ')

    # Editorial and Advisory photos
    if ('images/editorial' in img_tag or 'images/advisory' in img_tag or 'images/international' in img_tag):
        src_match = re.search(r'src="([^"]+)"', img_tag)
        if src_match:
            src_val = src_match.group(1)
            filename = os.path.basename(src_val)
            if filename in name_map:
                base_compliant = name_map[filename]
                root_dir = os.path.dirname(src_val)
                srcset_parts = []
                for w in sizes:
                    out_path = f"{root_dir}/{base_compliant}-{w}w.webp"
                    if os.path.exists(out_path):
                        srcset_parts.append(f"{out_path} {w}w")
                
                if srcset_parts:
                    # Also include the original image as the highest resolution if it's not already in the list
                    with Image.open(src_val) as img:
                        orig_w, _ = img.size
                        if orig_w not in sizes:
                            srcset_parts.append(f"{src_val} {orig_w}w")
                    
                    srcset_str = ', '.join(srcset_parts)
                    sizes_str = '(max-width: 480px) 200px, (max-width: 768px) 400px, 800px'
                    
                    if 'srcset=' not in img_tag:
                        # Insert before src
                        img_tag = img_tag.replace('src=', f'srcset="{srcset_str}" sizes="{sizes_str}" src=')
    return img_tag

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(html_file, 'r', encoding='cp1252') as f:
            content = f.read()
    
    new_content = re.sub(r'<img\s+[^>]+>', replacer, content)
    
    if new_content != content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {html_file}")
